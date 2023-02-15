import re


for _ in range(int(input())):
    n = input()

    x = bool(re.match(r"^[456]\d{15}$", n))
    y = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", n))
    n = n.replace("-", "")
    z = bool(re.match(r"(?!.*(\d)(-?\1){3})", n))
    if (x or y) and z:
        print("Valid")
    else:
        print("Invalid")
