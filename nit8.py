# program to genarate matematical table of input number
num = int(input('enter which table you want : '))
for x in range(1,11,1):
    pro=num*x
    print(num , "*" ,x , "=" ,pro)
