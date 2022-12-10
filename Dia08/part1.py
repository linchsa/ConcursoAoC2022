file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia08/input.txt')
matrix = list(map(lambda x: list(map(int, list(x.strip()))),  file.readlines()))

visible_trees = 2*(len(matrix)-2) + 2*(len(matrix[0])-2) + 4
print(visible_trees)
for i in range(1,len(matrix)-1):
    for j in range(1,len(matrix[i])-1):
        current_tree = matrix[i][j]
        visible_up = True
        visible_down = True
        visible_left = True
        visible_right = True
        #up
        for num in range(0,i):
            if not matrix[num][j] < current_tree :
                visible_up = False
                break
        #down
        for num in range(i+1,len(matrix)):
            if not matrix[num][j] < current_tree :
                visible_down = False
                break
        #left
        for num in range(0,j):
            if not matrix[i][num] < current_tree :
                visible_left = False
                break
        #right
        for num in range(j+1,len(matrix[0])):
            if not matrix[i][num] < current_tree :
                visible_right = False
                break
        
        if(visible_up or visible_down or visible_left or visible_right):
            visible_trees += 1




print(visible_trees)