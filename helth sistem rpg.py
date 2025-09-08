vida = 30
print("Vida:", vida)
while vida > 0:
    dano = int(input("Quanto de dano? (Use número negativo para curar): "))

    vida -= dano

    if dano > 0:
        print(f"Você tomou {dano} de dano!")
    elif dano < 0:
        print(f"Você recuperou {abs(dano)} de vida!")
    else:
        print("Nada aconteceu... 🫥")

    if vida > 0:
        print("Vida restante:", vida)
    else:
        print("VOCÊ MORREU! 💀")
