print('菲波那切数列的前100项：')
s=0
i=0
j=1

for n in range(1,100):
    s=i+j  
    i=j
    j=s
    print(s)
    
