# copyright Suli sulihu@bu.edu 2020

from arabic2roman import arabic2roman


def test_0():
    assert arabic2roman(0) == ''
    assert arabic2roman(2) == 'II'
    assert arabic2roman(8) == 'VIII'
    assert arabic2roman(9) == 'IX'
    assert arabic2roman(20) == 'XX'
    assert arabic2roman(999) == 'CMXCIX'
    assert arabic2roman(3999) == 'MMMCMXCIX'
    assert arabic2roman(4000) == 'Number too large.'


def main():
    pass


if __name__ == "__main__":
    main()
