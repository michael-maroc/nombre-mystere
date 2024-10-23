import random

print("*** Le jeu du nombre mystère ***")

computerchoice = random.randint(1, 100)
gamecount = 5

while True:
    print(f"Il te reste {gamecount} essai{'s' if gamecount > 1 else ""}")
    playerinput = input("Devine le nombre : ")

    if not playerinput.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    else:
        player = int(playerinput)

    if computerchoice == player:
        print(f"Bravo ! Le nombre mystète était bien {player}")
        print(f"🎉🎉🎉 Tu as trouvé le nombre en {
              6 - gamecount} essai{'s' if gamecount < 5 else ""}")
        break
    elif computerchoice < player:
        print(f"Le nombre mystère est plus petit que {player}")

    elif computerchoice > player:
        print(f"Le nombre mystère est plus grand que {player}")

    gamecount -= 1

    if gamecount == 0:
        print(f"Dommage ! Le nombre mystère était {computerchoice}")
        break

    print("-" * 25)

print("Fin du jeu.")
