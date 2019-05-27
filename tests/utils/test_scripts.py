import pytest
from marian.utils.scripts import join_bash_scripts

def test_join_bash_scripts(bash_0, bash_1, joined_script):
    with pytest.raises(NotImplementedError):
        join_bash_scripts([])
    with pytest.raises(NotImplementedError):
        join_bash_scripts([bash_0])

    assert join_bash_scripts([bash_0, bash_1]) == joined_script
