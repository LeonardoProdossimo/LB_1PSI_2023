n = int(input("Digite um número: "))

x = 0
y=1
for i in range(2,n+1):
    c=x+y
    x=y
    y=c
    print(f'{c}')