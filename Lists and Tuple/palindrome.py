# wap to check if a list contains a palindrome of elements.(Hint: usecopy()method)

list1=[1,2,3]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list2):
   print("palindrome")    
else:
    print("not a palindrome")   