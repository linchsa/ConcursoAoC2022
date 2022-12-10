file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia07/smallinput.txt')
lst = file.readlines()

dir_dict = {}
index = 0
while(index < len(lst)):
    line = lst[index].split(" ")
    if(line[0] == '$' and line[1] == 'cd' and line[2] == '..\n'):
        index += 1
    elif(line[0] == '$' and line[1] == 'cd'):
        current_dir = line[2].strip()
        if current_dir not in dir_dict:
            dir_dict[current_dir] = []
        index += 2
        ls_read = True
        while(ls_read):
            if(index >= len(lst)):
                break
            ls_line = lst[index].split(" ")
            if(ls_line[0] == '$'):
                ls_read =False
                break
            if(ls_line[0] == 'dir'):
                dir_dict[current_dir].append(ls_line[1].strip())
            else:
                dir_dict[current_dir].append(int(ls_line[0]))
            index += 1

print(dir_dict)
print(len(dir_dict))
read =True
dir_remove = []
for dir in dir_dict:
    try:
        dir_dict[dir] = sum(dir_dict[dir])
        if(dir_dict[dir] > 100000):
            dir_remove.append(dir)
    except:
        continue
for dir in dir_remove:
    dir_dict.pop(dir)
print(dir_dict)

print(len(dir_dict))
for dir in dir_dict:
    if(dir != '/'):
        to_dir_lst = dir_dict[dir]
        #while(read):
        for elem in to_dir_lst:
            if elem in dir_remove:
                break
            if elem in dir_dict:
                from_dir_lst = dir_dict[elem]
                to_dir_lst.pop(to_dir_lst.index(elem))
                for el in from_dir_lst:
                    to_dir_lst.append(el)
        print(dir)
        dir_dict[dir] = to_dir_lst

print(dir_dict)
sum_size = []
for dir in dir_dict:
    if(dir != '/'):
        if(sum(dir_dict[dir]) < 100000):
            sum_size.append(sum(dir_dict[dir]))

print(sum(sum_size))




    
        


