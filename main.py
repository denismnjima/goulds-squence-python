def goulds():
    num = 0
    while(num<10):
        binary_num = bin(num)
        yield binary_num.count('1')
        num+=1

for ans in goulds():
    print(ans)