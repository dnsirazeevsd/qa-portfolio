import pytest

#Увеличение счетчика
@pytest.mark.parametrize("value, expected", 
[
    (1, 1),
    (3, 3),
    (10, 10)
])
def test_func_increment(counter, value, expected):
    assert counter.increment(value) == expected

#Уменьшение счетчика
@pytest.mark.parametrize("value, expected", 
[
    (1, 9),
    (3, 7),
    (10, 0)
])
def test_func_decrement(counter, value, expected):
    counter.increment(10)
    assert counter.decrement(value) == expected

#Негатив Уменьшение счетчика(Число больше чем счетчик)
def test_func_decrement_negative(counter):
    with pytest.raises(ValueError, match="Negative value not allowed"):
        counter.decrement(100)

#Сбрасываения счетчика
def test_func_reset(counter):
    counter.increment(10)
    counter.reset()

    assert counter.get_value() == 0

#Проверка текущего состояния счетчика
def test_func_get_value(counter):
    assert counter.get_value() == 0