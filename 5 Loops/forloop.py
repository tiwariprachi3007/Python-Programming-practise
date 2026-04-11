tup=(1,2,3,4,4,2,1,4)

for num in tup:
    print(num)


 # for strings

str = "helloworld"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)    
else:
    print("o not found")
