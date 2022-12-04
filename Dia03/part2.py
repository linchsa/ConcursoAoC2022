file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia03/input.txt')
lst = file.readlines()

priority = 0
for i in range(0, len(lst)-1, 3):
    ruck_1 = set(lst[i].strip())
    ruck_2 = set(lst[i+1].strip())
    ruck_3 = set(lst[i+2].strip())
    common = list(ruck_1.intersection(ruck_2).intersection(ruck_3))[0]
    if(ord(common) <= 90):
        priority += ord(common) -90 + 52
    else:
        priority += ord(common) - 97 + 1
print(priority)
    