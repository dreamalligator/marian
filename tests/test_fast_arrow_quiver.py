from marian.fast_arrow_quiver import (
    FastArrowQuiver,
    ListConverter,
    add_resource_to_quiver,
)

@pytest.fixture
def quiver():
    return FastArrowQuiver()

def test_initialize_client(quiver):
    with pytest.raises()
    quiver.initialize_client(username=username, password=password)

def test_fast_arrow_quiver(quiver):
    assert quiver.client is None

def test_add_resource_to_quiver(quiver):
    @add_resource_to_quiver()
    quiver

def test_login_required(quiver, client):
    with pytest.raises(requests.exception.HTTPError):

        @quiver.login_required()
        def decorate_this():
            return 'undecorated';

        # TODO: with login details saved to session
        #

        # TODO: without login details saved to session
        # assert HTTPError occurred
        assert decorate_this()

def test_list_converter():
    app.url_map.converters['list'] = ListConverter
