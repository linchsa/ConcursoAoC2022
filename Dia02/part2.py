file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia02/input.txt')
lst = file.readlines()
score = 0
dic = {"X": 1, "Y":2, "Z":3, "A":1, "B": 2, "C": 3}
dic_l = {"A": "Z", "B": "X", "C": "Y" }
dic_w = {"A" : "Y", "B" : "Z", "C" :"A"}

for i in lst:
    if(i[2] == "Y"):
        score += 3 + dic[i[0]]
    elif(i[2] == "X"):
        score += dic[dic_l[i[0]]]
    elif(i[2] == "Z"):
        score += 6 + dic[dic_w[i[0]]] 

print(score)