def advance_funtion(guest="name"):
    return print(f"Hell0 {guest}")


name = input("Enter the Name of user: ")

advance_funtion(name)


def advance_funtion2(guest,age):
    return print(f"Hell0 {guest}. Your age is = {age}")


name = input("Enter the Name of user: ")
age = int(input("Enter your age: "))

advance_funtion2(name,age)


def sum_number(*summ):
    summ = sum(summ)
    print("Sum =",summ)
sum_number(1,2,3,4)

def show_detail(**arg):
    for key, value in arg.items():
         print(f"{key}: {value}")

show_detail(name="Nisar", skill="Python", level="Intermediate")

numbers = [1,2,3]

square = list(map(lambda x:x**2,numbers))
print(square)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


def outers():
    def iner():
        print("This is inter function:...")
    iner()
outers()

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))


def decorator(func):
    def wrapper():
        print("Before function")
    func()
    print("After function")
    return wrapper


@decorator
def say_hello():
    print("Hello!")
say_hello()


def fectorial(n):
    if n ==1:
        return 1
    return n *fectorial(n-1)
print(fectorial(5))
