try:
    n = float(input("Please input a number"))
    devide = 10/n
except ValueError:
    print("Please enter correct number")
except ZeroDivisionError:
    print("0 cannot devide this number")