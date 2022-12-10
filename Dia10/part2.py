file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia10/input.txt')

instructions = file.readlines()
pc = 0
x = 1
pos = 0
current_str = ""
for instr in instructions:
    instr = instr.split(" ")
    if(instr[0] == 'noop\n'):
        if(pc == x-1 or pc == x or pc == x+1):
            current_str += '#'
        else:
            current_str += '.'
        pc += 1
        if(pc%40 == 0 ):
            print(current_str)
            current_str = ""
            pc = 0
    else:
        for i in range(1,3):
            if(pc == x-1 or pc == x or pc == x+1):
                current_str += '#'
            else:
                current_str += '.'
            pc += 1
            if(pc%40 == 0 ):
                print(current_str)
                current_str = ""
                pc = 0
        x += int(instr[1])

