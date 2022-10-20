def triangle (a, b, c):
    if a < b + c and b < a + c and c < a + b:
        msg = f" It's triangle"
    else:
        msg = f"The figure is not triangle"
    return msg

def main():
    a = int(input("Input a = "))
    b = int(input("Input b = "))
    c = int(input("Input c = "))

    print(triangle(a, b, c))

main()