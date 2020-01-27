# copyright Suli sulihu@bu.edu 2020


def arabic2roman(num):
    """
    Transform integer to Roman #.
    Only works for 0 - 10,000.
    """
    roman_m = ["", "M", "MM", "MMM"]
    roman_c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    roman_x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    roman_i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    try:
        return roman_m[num//1000] + roman_c[(num % 1000)//100] + \
            roman_x[(num % 100)//10] + roman_i[num % 10]
    except Exception:
        return "Number too large."


def main():
    print(arabic2roman(8))
    print(arabic2roman(0))


if __name__ == "__main__":
    main()
