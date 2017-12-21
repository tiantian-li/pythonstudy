print('100以内的质数为：')
count=0
s=0
for i in range(1,101):
    for j in range(2,i):
        if i%j == 0:
            s=1
            break
    if s==0:
        print(i)
        count+=1
    s=0
print ('一共有质数%d个：'%count)   
    
        
