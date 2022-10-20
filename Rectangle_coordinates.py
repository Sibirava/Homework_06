def rectangle_coordinate(x1, y1, x2, y2, x, y):
    if x2 > x1 and y2 < y1:
        if x1 <= x <= x2 and y2 <= y <= y1:
            msg = f"Dot is inside rectangle"
        else:
            msg = f"DOt is outside of rectangle"
    else:
        msg = f"It's not rectangle"
    return msg


def main():
    print("Input a top left vertex of rectangle")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    print("Input a lower right vertex of rectangle")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    print("Input a dot coordinate")
    x = float(input("x = "))
    y = float(input("y = "))

    msg = f"{rectangle_coordinate(x1, y1, x2, y2, x, y)}"
    print(msg)


main()
