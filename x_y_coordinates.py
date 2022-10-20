#Разработайте программу, которая проверяет, что точка с координатами (x, y)
#лежит в первой (или во второй, или в третьей, или в четвёртой) координатной
#четверти.

def define_coordinate_quarter(x, y):
    if x > 0 and y > 0:
        quarter = 1
    elif x > 0 and y < 0:
        quarter = 2
    elif x < 0 and y < 0:
        quarter = 3
    else:
        quarter = 4
    return quarter


def main():
    x = float(input("Input x coordinator point: "))
    y = float(input("Input x coordinator point: "))

    quarter = define_coordinate_quarter(x, y)

    msg = f"Point with x = {x} and y = {y} coordinate is in {quarter} quarter."

    print(msg)


main()
