tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
c = 1
print("X começa\n")

def vencer():
    venceu = False
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        venceu = True
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        venceu = True

    for x in range(0, 3):
        if tabuleiro[0][x] == tabuleiro[1][x] == tabuleiro[2][x] != " ":
            venceu = True

        if tabuleiro[x][0] == tabuleiro[x][1] == tabuleiro[x][2] != " ":
            venceu = True
    return venceu


def velha():
    velhou = True
    if tabuleiro[0][0] != tabuleiro[1][1] != tabuleiro[2][2] != " ":
        velhou = False
    elif tabuleiro[0][2] != tabuleiro[1][1] != tabuleiro[2][0] != " ":
        velhou = False

    for x in range(0, 3):
        if tabuleiro[0][x] != tabuleiro[1][x] != tabuleiro[2][x] != " ":
            velhou = False

        if tabuleiro[x][0] != tabuleiro[x][1] != tabuleiro[x][2] != " ":
            velhou = False
    return velhou


while True:
 for x in range(3):
   print(tabuleiro[x])
 c += 1
 linha = int(input("Qual linha você vai preencher?(0,1,2)"))
 coluna = int(input("Qual posição da linha você preencherá/(0,1,2)"))
 if c % 2 == 0:
  tabuleiro[linha][coluna] = "x"
 else:
  tabuleiro[linha][coluna] = "O"
 if vencer() == True:
    for x in range(3):
     print(tabuleiro[x])
    print("Parabéns, você venceu!")
    break
    
 if vencer() == False and tabuleiro[0][0] and tabuleiro[1][1] and tabuleiro[2][2] and tabuleiro[0][2] and tabuleiro[2][0] and tabuleiro[0][1] and tabuleiro[1][0] and tabuleiro[1][2] and tabuleiro[2][1] != " " :
    for x in range(3):
     print(tabuleiro[x])
    print("Deu velha...")
    break