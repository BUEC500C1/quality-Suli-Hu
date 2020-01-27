# copyright Suli sulihu@bu.edu 2020


def arabic2roman(num):
    """
    Transform integer to Roman #.
    Only works for 0 - 10,000.
    """
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    try:
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
    except Exception:
        return "Number too large."


def main():
    print(arabic2roman(8))
    print(arabic2roman(0))

if __name__ == "__main__":
    main()

