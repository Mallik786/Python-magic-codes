''' This code is written By Mohammad Mallik 
    Linked in profile :: https://www.linkedin.com/in/mohammad-mallik-59a6b4117/
    Github link :: https://github.com/Mallik786/
    '''


def hcf(l):
    l.sort()
    diff = l[1] - l[0]
    count = 0
    fac = []
    for i in range(len(l)):
        if(l[i]%diff!=0):
            count = count +1
    if(count==0):
        print(diff)
    elif(count>0):
        for j in range(1,diff):
            if(diff%j==0):
                fac.append(j)
        for k in range(len(fac)):
            for p in range(len(l)):
                if(l[p]%fac[k]==0):
                    count = 0
                else:
                    count = 1
            if(count == 0):
                print(fac[k])
                break
            break


n = list(map(int,input().split()))
hcf(n)