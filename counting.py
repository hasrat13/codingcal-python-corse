Amount = int(input("please enter amout for widrawal : "))

note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10

print("notes of 100 dollars", note_1)
print("notes of 50 dollar" , note_2)
print("notes of 10 dollar", note_3)