print('请输入水位：')
level=input()
if level=='low': 
    print('注水，20')
    print('搅拌，30m')
elif level=='high':
    print('注水，50')
    print('搅拌，50m')
print('请输入次数：')
times=int(input())
for i in range(times):    
    print('放水')
    print('注入清水，50')
    print('搅拌,30m')
    print('放水')
    print('甩干')
