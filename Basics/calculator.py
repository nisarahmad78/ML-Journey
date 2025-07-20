try:
    try:
        def add(x,y):
            return print("sum = ",x+y)
        def mul(x,y):
            return print("mul = ",x*y)
        def div(x,y):
            return print("div = ",x/y)
        def sub(x,y):
            return print("sub = ",x-y)
        x = float(input("Enter the First number: "))
        y = float(input("Enter the second number: "))

        num = int(input("What operation did you want \n1 for sum\n2 for mul\n3 for div\n4 for sub\n"))
        if num==1:
            add(x,y)
        elif num==2:
            mul(x,y)
        elif num==3:
            div(x,y)
        elif num==4:
            sub(x,y)
        else:
            print("Enter the correct number")
            num = int(input("What operation did you want \n1 for sum\n2 for mul\n3 for div\n4 for sub\n"))
    except ValueError:
        print("Please correct value")
except ValueError:
    print("Please correct number")
except ZeroDivisionError:
    print("Zero can't...")

