altura = int(input("Digite a sua altura em centimetros: "))


if altura > 120:
    print("Você pode comprar o ingresso para a montanha russa!")
    idade = int(input("Digite a sua idade: "))
    if idade <= 12:
        grana = 5
        print("Por favor pague R$5")    
    elif idade <=18:
        grana = 7
        print("Por favor pague R$7")
    else:
        grana = 12
        print("Por favor pague R$12")

    fotos = input("Você deseja tirar uma foto? SIM/NAO")
    if fotos == "SIM":
        print("Adicionado mais 3 R$")
        grana = grana +3
    else:
        print("Ok, sem problemas")
else:
    print("Você não possui altura suficiente para poder andar de montanha russa!")