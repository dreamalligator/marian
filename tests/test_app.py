from marian import create_app

def test_create_app():
    app = create_app({
        'TODO': 'temp test',
    })
    assert app.config['TODO'] == 'temp test'
