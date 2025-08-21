try:
    number=int(input("enter a number"))
    print("the number is entered is",number)
except ValueError as ex:
    print("exception:")