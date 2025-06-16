medical_cause = input("did you have a medical cause Y or N : ")
atten =int(input("enter the attendence of students :"))
if medical_cause == 'y' : 
    print(" you are allowed")
else: 
    if atten >= 75:
        print("allowed")
    else:
        print("not allowed")