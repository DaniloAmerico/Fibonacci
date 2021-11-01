t = int(input('Digite até onde ira o Fibonacci: '))
n=0
while n < t:
    FN = ( pow((1+pow(5,1/2))/2,n) - pow((1-pow(5,1/2))/2,n) ) / (pow(5,1/2))
    n = n+1
    print('{:.0f}'.format(FN))
