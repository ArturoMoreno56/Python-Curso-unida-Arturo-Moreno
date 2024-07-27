
array1 =["ariel","ptr",1,2.3,[1,2,3],True,False,"ptr"]
array2=[1,3,4]
array3=array1+array2

print("ptr" in array1)


print(array1.index("ptr"))

print(array1.count("ptr"))


array1.remove("ptr")

print(array1)

array1.reverse()

print(array1)

array3.sort()