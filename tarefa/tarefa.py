while True:
    print('Menu')
    print('1. Escreva um numero para ser exibido na tela')
    print('2. Soma de dois numeros')
    print('3. Calcular a area de um quadrado e o dobro')
    print('4. Converter Fahrenheit para Celsius')
    print('5. Sair')

    escolha = input('Escolha uma opção: ')
    
    if(escolha == '1'):
        numero = input('escreva nuero:')
        print(f"O número escrito foi {numero}\n.")
        
    elif(escolha == '2'):
        numero1 =float (input('digite Numero:'))
        numero2= float (input('digite outro um Numero'))
        soma =  numero1+numero2
        print(f"soma do numero {numero1} com {numero2} e :{soma}\n" )
    
    elif(escolha == '3'):
        lado = float(input("Digite o comprimento do lado do quadrado: "))
        area = lado * lado
        area_dobro = area * 2
        print(f"\nValor do quadrado é {lado}, cálculo da área é {area} e o dobro da área é {area_dobro}\n")

    elif(escolha == '4'):
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = 5 * ((fahrenheit - 32) / 9)
        print(f"A temperatura em graus Celsius é {celsius:.2f}")
    elif escolha == '5':
        print('Saindo do programa')
        break
    else:
        print('Opção inválida. Tente novamente\n')