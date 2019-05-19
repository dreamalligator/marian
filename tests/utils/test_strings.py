from marian.utils.strings import (
    hlt,
    snake_case,
)

def test_hlt():
    constructed = f'i like {hlt("food")}. food is {hlt("good")}.'
    expected = 'i like \x1b[1;32mfood\x1b[0m. food is \x1b[1;32mgood\x1b[0m.'
    assert constructed == expected

def test_snake_case():
    assert snake_case('ClassName') == 'class_name'
    assert snake_case('Name') == 'name'
    assert snake_case('class_name') == 'class_name'
    assert snake_case('name') == 'name'
