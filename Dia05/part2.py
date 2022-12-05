file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia05/input.txt')
lst = file.readlines()
cont = 0

dict_stack = {}
for i in range(1,10):
    dict_stack[i] = []

for line in lst:
    for char in line:
        if(char != "[" and char != "]" and char != " " and char != "\n"):
            pos = int(cont / 4) +1
            dict_stack[pos].append(char)
        cont += 1
    cont = 0
    if (line == lst[7]): break
for i in range(10, len(lst)):
    new_line = lst[i].split(' ')
    num_mov = int(new_line[1])
    from_lst = int(new_line[3])
    to_lst = int(new_line[5])

    if(num_mov == 1):
            dict_stack[to_lst].insert(0,dict_stack[from_lst].pop(0))
    elif(num_mov > 1):
        while(num_mov > 0):
            dict_stack[to_lst].insert(0,dict_stack[from_lst].pop(num_mov-1))
            num_mov -=1
            
for stack in dict_stack.values():
    print(stack[0], end="")