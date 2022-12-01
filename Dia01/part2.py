file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia01/input.txt')
lst = file.readlines()
print(lst)
current = 0
max = 0
res_lst = []

for i in lst:
    if(i == '\n'):
        res_lst.append(current)
        current = 0
    else:
        current += int(i)

res_lst.sort(reverse=True)
print(res_lst)
print(res_lst[0] + res_lst[1] + res_lst[2])