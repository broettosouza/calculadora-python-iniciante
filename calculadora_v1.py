
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite operador (+,-,*,/):')
    
    numer = None
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numer = True
        

    except:

     numer = None

    if numer is None:
     print('Um ou ambos os numeros digitados são invalidos')
     continue
    
    operadores_permitidos = '+-/*'

    if operador not in  operadores_permitidos: 
     print('Digite apenas um operador válido (+,-,*,/)')
     continue

    if len(operador) > 1 :
     print('Digite apenas um operador')
     continue
     

    print("O resultado é: ")

    if operador == '+' :
     print(f"{num1_float} + {num2_float}=", num1_float + num2_float)
    
    elif operador == '-':
      print(f"{num1_float} - {num2_float}=", num1_float - num2_float)
    
    elif operador == '*' :
     print(f"{num1_float} * {num2_float}=", num1_float * num2_float)
    
    elif operador == '/' :
     print(f"{num1_float} / {num2_float}=", num1_float / num2_float)


    sair = input('Deseja sair?[s]im ou [n]ão: ').lower().startswith('s')
    
    if sair is True:
     break