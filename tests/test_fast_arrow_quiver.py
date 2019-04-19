from marian.fast_arrow_quiver import FastArrowQuiver

def test_fast_arrow_quiver():
    quiver = FastArrowQuiver()
    assert quiver.client is None
