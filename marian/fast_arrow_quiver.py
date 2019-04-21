'''
Methods grouped becuase they all need a instantiated Fast Arrow client to reference.
'''

from functools import wraps
import inspect
import requests
import fast_arrow
from flask import (
    redirect,
    request,
    session,
    url_for,
)
from .utils.strings import (
    hlt,
    warn,
    snake_case,
)

class FastArrowQuiver():
    @staticmethod
    def resources():
        return [
            fast_arrow.Account,
            fast_arrow.Collection,
            fast_arrow.Dividend,
            fast_arrow.Option,
            fast_arrow.OptionChain,
            fast_arrow.OptionEvent,
            fast_arrow.OptionMarketdata,
            fast_arrow.OptionOrder,
            fast_arrow.OptionPosition,
            fast_arrow.Portfolio,
            fast_arrow.Stock,
            fast_arrow.StockMarketdata,
            fast_arrow.StockOrder,
            fast_arrow.StockPosition,
            fast_arrow.User,
        ]

    def __init__(self, **kwargs):
        self.options = kwargs
        self.client = None

        print('dynamically attaching fast_arrow resources.')
        print(f'{hlt("Marian.quiver")} receiving the following methods:')
        for resource in self.resources():
            self.add_fast_arrow_resource(resource)
        print('')

    def add_fast_arrow_resource(self, resource):
        """
        attach a fast_arrow resource class as a class-attribute on the
        FastArrowQuiver instance. each resource's classmethod is decorated to
        automatically passed in the client defined on this instance.
        """

        resource_name = snake_case(resource.__name__)
        if hasattr(self, resource_name):
            print(f'attempting to overwrite resource {warn(resource_name)}.')
            raise AttributeError

        setattr(self, resource_name, resource)
        quiver_resource = getattr(self, resource_name)

        member_tuples = inspect.getmembers(resource, predicate=inspect.ismethod)
        for resource_method_name, resource_method in member_tuples:
            constructed_route = '/' + resource_name + '/' + resource_method_name
            constructed_endpoint = 'quiver.' + resource_name + '.' + resource_method_name
            self.options['app'].add_url_rule(
                constructed_route,
                constructed_endpoint,
                resource_method,
            )

            decorated_method = self.login_required(self.include_client(resource_method))
            setattr(quiver_resource, resource_method_name, decorated_method)
            print('  ' + hlt('.' + resource_name + '.' + resource_method_name) + ' attached.')

    def include_client(self, member_func):
        """
        this decorator prefills in the first client parameter with the current
        FastArrowQuiver instance's memoized client.
        """

        @wraps(member_func)
        def decorated_function(*args, **kwargs):
            return member_func(client=self.client, *args, **kwargs)

        return decorated_function

    def initialize_client(self, username, password):
        """start and memoize a RH connection via fast_arrow."""

        if self.client is None or self.client.authenticated is False:
            print('setting up client...')

            self.client = fast_arrow.Client(username=username, password=password)

            print('authenticating....')

            try:
                self.client.authenticate()
            except requests.exceptions.HTTPError as e:
                print('authentication failed (HTTPError).')
                raise e
            except fast_arrow.exceptions.AuthenticationError as e:
                print('authentication failed (AuthenticationError).')
                raise e

            session['rh_username'] = username
            session['rh_password'] = password

            print('done.')
        else:
            print('didnt need to initialize client. one already exists.')

    def login_required(self, f):
        """use saved session info to authenticate"""

        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('rh_username') is None or session.get('rh_password') is None:
                print('no stored login details found. redirecting to login page.')
                return redirect(url_for('login', next=request.url))

            try:
                print('authenticating using stored login details.')
                self.initialize_client(
                    username=session.get('rh_username'),
                    password=session.get('rh_password'),
                )
            except requests.exceptions.HTTPError:
                return redirect(url_for('login', next=request.url))

            return f(*args, **kwargs)

        return decorated_function
