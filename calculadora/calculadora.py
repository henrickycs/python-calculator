#calculadora simples

# função para adicionar dois números
def adicao(x, y):
    return x + y

# função para subtrair dois números
def sub(x, y):
    return x - y

# função para multiplicar dois números
def multi(x, y):
    return x * y

# função para dividir dois números
def divide(x, y):
    return x / y


print("Selecione a operação.")
print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")
print("5.Sair")

while True:
    # recebe o valor do usuário
    escolha = input("Escolha(1/2/3/4/5): ")
    
    if escolha == '5':
        print("Fim!")
        break
    
    # verifica se a escolha é um operador
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", adicao(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
    else:
        print("Escolha uma das opções")