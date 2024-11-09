# write a program to take input 10 num and count even and odd num
eve,odd=0,0
for x in range(10):
    num=int(input("enter numbers"))
    if num%2==0 :
        eve= eve+1
    else :
        odd= odd+1
print('even = ' ,eve ,"odd =" ,odd)
