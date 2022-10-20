def triangle_type (a, b, c):
    if a == b == c:
        msg = f" It's equilateral triangle"
    elif a == b or a == c or b == c:
        msg = f" It's isosceles triangle"
    elif a == c / 2:
        msg = f" It's rectangular triangle"
    elif a == c / 2 and a == b:
        msg = f" It's right isosceles triangle"
    else:
        msg = f"The figure is not triangle"
    return msg

def main():
    a = int(input("Input a = "))
    b = int(input("Input b = "))
    c = int(input("Input c = "))

    print(triangle_type(a, b, c))

main()