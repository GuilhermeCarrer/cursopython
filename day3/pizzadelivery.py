print("Bem vindo ao Pizza Delivery PYTHON!")
tamanho = input("Qual o tamanho da pizza que você deseja? P, M, G: ")
peperonni = input("Você deseja por Peperonni na sua PIZZA? SIM/NAO: ")
queijo_extra = input("Você deseja por queijo extra sobre a sua PIZZA? SIM/NAO: ")

if tamanho == "P":
    preco = 15
elif tamanho == "M":
    preco = 20
elif tamanho == "G":
    preco = 25
else:
    print("Tamanho inválido")
    preco = 0
       
if peperonni == "SIM":
    preco += 2
elif peperonni != "NAO":
    print("Resposta inválida para peperonni. Considerando como 'não'.")


if queijo_extra == "SIM":
    preco += 1
elif queijo_extra != "NAO":
    print("Resposta inválida para queijo extra. Considerando como 'não'.")


print(f"O preço total da pizza é: R${preco}")