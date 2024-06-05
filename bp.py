import math
decisao = input('Você deseja fazer uma equação de 1º grau ou de 2º grau? (1,2)')
match decisao:
    case '1':
        def calcular_x(a, x, b, y):
            x == a*x+b == y
            return x
        a = float(input('Informe o valor de a: '))
        x = float(input('Informe o valor de x: '))
        b = float(input('Informe o valor de b: '))
        y = float(input('Informe o valor de y: '))
        def calcular_equacao(a, x, b, y):
            calculo = a*x+b == y
            return calculo
        print(f'O resultado da equação é {calcular_equacao(a, x , b, y)}')
        print(f'O valor de x é {calcular_x(a,x,b, y)}')
