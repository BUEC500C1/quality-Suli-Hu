# copyright Suli sulihu@bu.edu 2020

from arabic2roman import arabic2roman


def test_8():
    assert arabic2roman(8) == 'VIII'


def test_9():
    assert arabic2roman(9) == 'IX'


def test_2():
    assert arabic2roman(2) == 'II'


def main():
    print(arabic2roman(8))
    print(arabic2roman(0))


if __name__ == "__main__":
    main()
