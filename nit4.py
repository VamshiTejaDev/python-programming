#count no of alpabets
st = input("enter string : ")
count=0
for x in st:
    if (x>="a" and x<="z") or (x>="A" and x<="Z"):
        count= count+1
print("count is :" , count)
