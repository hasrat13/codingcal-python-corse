try:
    num1, num2=eval(input("enter two numbers , sepreated by a comma"))
    result = num1/num2
    print("Result is",result)
except ZeroDivisionError:
    print("divison by 0 is error !!")
except SyntaxError:
    print("comma is missing , enter numbers seperated by coma like this 1,2")
except:
    print("wrong input")
else:
    print("no exceptions ")
finally:
    print("this will execute no matter what")