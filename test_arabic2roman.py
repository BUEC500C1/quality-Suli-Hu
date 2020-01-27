# copyright Suli sulihu@bu.edu 2020

from arabic2roman import arabic2roman


def test_0():
    assert arabic2roman(0) == ''


def test_2():
    assert arabic2roman(2) == 'II'


def test_8():
    assert arabic2roman(8) == 'VIII'


def test_9():
    assert arabic2roman(9) == 'IX'


def test_20():
    assert arabic2roman(20) == 'XX'


def test_999():
    assert arabic2roman(999) == 'CMXCIX'


def test_3999():
    assert arabic2roman(3999) == 'MMMCMXCIX'


def test_4000():
    assert arabic2roman(4000) == 'Number too large.'


def main():
    pass


if __name__ == "__main__":
    main()
