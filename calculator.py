def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")
choice=input("please enter your choice(a/b/c/d)")
num_1 = int(input("please enter the first number "))
num_2 = int(input("please enter the second number "))
if choice=='a':
    print("addition = " , add(num_1 , num_2))
elif choice=='b':
    print("subtraction = " , subtract(num_1 , num_2))
elif choice=='c':
    print("multiply = " , multiply(num_1 , num_2))
elif choice=='d':
    print("devide = " , divide(num_1 , num_2)) 
else:
    print("this is an indvalid input")