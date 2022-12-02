file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia02/input.txt')
lst = file.readlines()
score = 0
dic = {"X": 1, "Y":2, "Z":3}

for i in lst:
    if(i[0] == "A" and i[2] == "X" or i[0] == "B" and i[2] == "Y" or i[0] == "C" and i[2] == "Z" ):
        score += 3 + dic[i[2]]
    elif(i[0] == "A" and i[2] == "Z" or i[0] == "B" and i[2] == "X" or i[0] == "C" and i[2] == "Y"):
        score += dic[i[2]]
    else:
        score += 6 + dic[i[2]] 

print(score)