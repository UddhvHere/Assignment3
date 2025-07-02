
n=int(input('Enter a number:'))
def factor(x):
    if x<2:
        return 1
    else:
        return x*(factor(x-1))
answr=factor(n)
print('Factorial of' , n, 'is:',answr)
