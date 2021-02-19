#number 27
f = open('text.txt', 'r')
k31 = 0
k62 = 0
k2 = 0
kany = 0
n = int(f.readline())
for i in range(n):
    x = int(f.readline())
    if i%62==0:
        itog+=kany+k2+k31+k62
        k62+=1
    elif x%31==0:
        itog+=k2+k62
        k31+=1
    elif x%2==0:
        itog+=k62+k31
        k2+=1
    else:
        itog+=k62
        kany+=1
print(itog)
