file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia10/input.txt')

instructions = file.readlines()
pc = 0
x = 1
strength = 0
for instr in instructions:
    instr = instr.split(" ")
    if(instr[0] == 'noop\n'):
        pc += 1
        if((pc - 20)%40 == 0 ):
            strength += (pc * x)
    else:
        for i in range(1,3):
            pc += 1
            if((pc - 20)%40 == 0 ):
                strength += (pc * x)
        x += int(instr[1])

print(strength)