s1={1,4,3}
s2={5,6,9}
s3=list(zip(s1,s2))
print(s3,"\n")
list1=[15,14,3,13]
list2=[6,7,9,10]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
stocks=['reliance','infosys','tsc']
prices=[6700,1303,1705]
new_dict={stocks: prices for stocks,prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))
