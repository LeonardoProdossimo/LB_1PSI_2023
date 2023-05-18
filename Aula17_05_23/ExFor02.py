n = int(input("Digite um número maior que 0: "))

x = 0
y=1

if ( n >=0):
    print(x, end=', ')
if ( n >=1):
    print(x, end=', ')
while n <= 1:
    print('Número inválido, digite novamente!')
    n = int(input("Digite um número: "))

print(y, end=', ')
for i in range(2,n+1):
    z=x+y
    x=y
    y=z
    print(z, end=", ")
print(end="...")