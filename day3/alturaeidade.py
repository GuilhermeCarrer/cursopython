altura = int(input("Digite a sua altura em centimetros: "))


if altura > 120:
    print("Você pode comprar o ingresso para a montanha russa!")
    idade = int(input("Digite a sua idade: "))
    if idade <= 18:
        print("Por favor pague R$7")    
    else:
        print("Por favor pague R$12")
else:
    print("Você não possui altura suficiente para poder andar de montanha russa!")