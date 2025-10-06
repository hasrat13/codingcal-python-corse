class fruit:
    taste="sweet"
    def __init__(self,name,color):
        self.name= name 
        self.color= color
apple=fruit('apple','red')
grape=fruit('grape','purple')
mango=fruit('mango','orange-yellow')
print(apple.taste)
print(apple.name,apple.color)
print(grape.name,grape.color)
print(mango.name,mango.color)