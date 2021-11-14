import random

print("""Bine ai venit!

Hai sa jucam x si 0

Tu esti cu x

Asa arata tabla:

1|2|3
4|5|6
7|8|9
""")

lista_casute = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
prioritate0 = ["5"]
prioritate1 = ["1", "3", "7", "9"]
prioritate2 = ["2", "4", "6", "8"]
while prioritate0 or prioritate1 or prioritate2:
    casuta_selectata = input("Alege casuta: \n\n")
    while casuta_selectata not in prioritate0 and casuta_selectata not in prioritate1\
            and casuta_selectata not in prioritate2:
        print("Introdu o casuta valida\n\n")
        for i in range(0, 9, 3):
            print(f"{lista_casute[i]}|{lista_casute[i + 1]}|{lista_casute[i + 2]}")
        casuta_selectata = input("\nAlege casuta: \n\n")
        print()
    lista_casute[int(casuta_selectata)-1] = "x"
    if casuta_selectata in prioritate0:
        prioritate0.remove(casuta_selectata)
    if casuta_selectata in prioritate1:
        prioritate1.remove(casuta_selectata)
    if casuta_selectata in prioritate2:
        prioritate2.remove(casuta_selectata)
    for i in range(0, 9, 3):
        print(f"{lista_casute[i]}|{lista_casute[i + 1]}|{lista_casute[i + 2]}")
    if lista_casute[0] == lista_casute[1] == lista_casute[2] == "x" or\
            lista_casute[3] == lista_casute[4] == lista_casute[5] == "x" or\
            lista_casute[6] == lista_casute[7] == lista_casute[8] == "x" or\
            lista_casute[0] == lista_casute[3] == lista_casute[6] == "x" or\
            lista_casute[1] == lista_casute[4] == lista_casute[7] == "x" or\
            lista_casute[2] == lista_casute[5] == lista_casute[8] == "x" or\
            lista_casute[0] == lista_casute[4] == lista_casute[8] == "x" or\
            lista_casute[2] == lista_casute[4] == lista_casute[6] == "x":
        print("\nAi castigat!")
        break
    print()
    print("\nacum alege calculatorul:\n")
    if prioritate0:
        while prioritate0:
            lista_casute[4] = "0"
            prioritate0.remove("5")
            break
    elif prioritate1:
        while prioritate1:
            casuta_selectata = random.choice(prioritate1)
            lista_casute[int(casuta_selectata)-1] = "0"
            prioritate1.remove(casuta_selectata)
            break
    elif prioritate2:
        while prioritate2:
            casuta_selectata = random.choice(prioritate2)
            lista_casute[int(casuta_selectata) - 1] = "0"
            prioritate2.remove(casuta_selectata)
            break
    for i in range(0, 9, 3):
        print(f"{lista_casute[i]}|{lista_casute[i+1]}|{lista_casute[i+2]}")
    if lista_casute[0] == lista_casute[1] == lista_casute[2] == "0" or\
            lista_casute[3] == lista_casute[4] == lista_casute[5] == "0" or\
            lista_casute[6] == lista_casute[7] == lista_casute[8] == "0" or\
            lista_casute[0] == lista_casute[3] == lista_casute[6] == "0" or\
            lista_casute[1] == lista_casute[4] == lista_casute[7] == "0" or\
            lista_casute[2] == lista_casute[5] == lista_casute[8] == "0" or\
            lista_casute[0] == lista_casute[4] == lista_casute[8] == "0" or\
            lista_casute[2] == lista_casute[4] == lista_casute[6] == "0":
        print("\nA castigat calculatorul")
        break
    if not prioritate0 and not prioritate1 and not prioritate2:
        print("\nE remiza")
        break
