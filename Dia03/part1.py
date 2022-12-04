file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia03/input.txt')
lst = file.readlines()
priority = 0
for line in lst:
    check = False
    line.split('\n')
    for i in range(0, int(len(line)/2)):
        for j in range(int(len(line)/2), len(line)-1):
            if(line[i] == line[j]):
                if(ord(line[i]) <= 90):
                    priority += ord(line[i]) -90 + 52
                else:
                    priority += ord(line[i]) - 97 + 1
                check = True
                break
        if(check):
            break
print(priority)
    
        
    

