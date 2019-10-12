from marian.cli import cli

def test_cli(app):
    runner = app.test_cli_runner()
    result = runner.invoke(cli)
    assert 'Marian CLI' in result.output
