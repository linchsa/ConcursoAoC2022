file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia08/input.txt')
matrix = list(map(lambda x: list(map(int, list(x.strip()))),  file.readlines()))
max_score = 0

for i in range(1,len(matrix)-1):
    for j in range(1,len(matrix[i])-1):
        current_tree = matrix[i][j]
        visible_up = 0
        visible_down = 0
        visible_left = 0
        visible_right = 0
        current_score = 0
        #up
        for num in range(i-1,-1,-1):
            if(matrix[num][j] >= current_tree):
                visible_up += 1
                break
            visible_up += 1
        #down
        for num in range(i+1,len(matrix)):
            if (matrix[num][j] >= current_tree):
                visible_down += 1
                break
                
            visible_down += 1
        #left
        for num in range(j-1,-1,-1):
            if(matrix[i][num] >= current_tree) :
                visible_left += 1
                break
            
            visible_left += 1
        #right
        for num in range(j+1,len(matrix[0])):
            if(matrix[i][num] >= current_tree) :
                visible_right += 1
                break
        
            visible_right += 1

        current_score = visible_down * visible_up * visible_left * visible_right
        if(current_score > max_score):
            max_score = current_score




print(max_score)