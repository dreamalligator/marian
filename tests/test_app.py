from marian import create_app

def test_create_app():
    app = create_app({
        'SECRET_KEY': 'acab1312',
    })

    assert app.config['SECRET_KEY'] == 'acab1312'
