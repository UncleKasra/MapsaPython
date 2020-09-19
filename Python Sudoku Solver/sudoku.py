# Sudoku Solver ?x?  --> for any dimensions it works!!! Because I am Uncle Kasra :) 9x9 , 16x16 and so on

def sudokuvalid(sudo):
    v = 1
    jazr = len(sudo) ** 0.5
    if not jazr.is_integer:
        v = 0
    if v == 1:
        for z in range(len(sudo)):
            if len(sudo) != len(sudo[z]):
                v = 0
    if v == 1:
        for m in range(len(sudo)):
            for n in range(len(sudo)):
                if sudo[m][n] not in range(len(sudo)+1):
                    v = 0
    return v

def countzero(sudo):
    allzero = 0
    for i in range(0, len(sudo[0])):
            for j in range(0, len(sudo)):
                if sudo[i][j] == 0:
                    allzero += 1
    return allzero
                    

def get_box(sudo, i, j):
    jazr = int(len(sudo) ** 0.5)
    boxrow = list(range(jazr))  #i
    while True:
        if i in boxrow:
            break
        else:
            for k in range(jazr):
                boxrow[k] += jazr
    boxcol = list(range(jazr))  #j
    while True:
        if j in boxcol:
            break
        else:
            for k in range(jazr):
                boxcol[k] += jazr
    return boxrow, boxcol


def possible(sudo, i, j):      # sudo:sudoku table, i:row, j:column

    cset = set(range(1, len(sudo)+1))

    #row
    row = cset - set(sudo[i])

    #column
    tmp = []
    for k in range(0, len(sudo)):
        tmp.append(sudo[k][j])
    col = cset - set(tmp)

    #box
    boxrow, boxcol = get_box(sudo, i, j)
    tmp = []
    for x in boxrow:
        for y in boxcol:
            if (x == i) and (y == j):
                continue
            tmp.append(sudo[x][y])
    box = cset - set(tmp)

    p = row.intersection(col, box)
    return p # type(p): set


def sudoku(sudo):
    if sudokuvalid(sudo) == 0:
        print('\n\t This sudoku does not valid format!')
    else:
        allz = countzero(sudo)
        curz = 0
        print(f'\n\t {curz} zero of {allz} zero solved!')
        f = 0
        ff = 1
        while (f == 0) and (ff == 1):
            ff = 0
            print('\n\t Technique: Sole Candidate!!')
            #Easy way: Sole Candidate
            fe = 0
            while fe == 0:
                fe = 1
                for i in range(0, len(sudo[0])):
                    for j in range(0, len(sudo)):
                        if sudo[i][j] == 0:
                            p = possible(sudo, i, j)
                            if len(p) == 1:
                                sudo[i][j] = p.pop()
                                curz += 1
                                print(f'\n\t {curz} zero of {allz} zero solved!')
                                fe = 0
                                ff = 1

            #check if solving is completed
            f = 1
            for i in range(0, len(sudo[0])):
                for j in range(0, len(sudo)):
                    if sudo[i][j] == 0:
                        f = 0
                        break
                if f == 0:
                    break
            if f == 1:
                break

            print('\n\t Technique: Unique Candidate!')
            #Hard way: Unique Candidate
            fh = 0
            for i in range(0, len(sudo[0])):
                for j in range(0, len(sudo)):
                    if sudo[i][j] == 0:
                        rowp = []
                        colp = []
                        boxp = []
                        rowdiff = set()
                        coldiff = set()
                        boxdiff = set()
                        pdiff = set()

                        #row
                        for k in range(0, len(sudo[0])):
                            if k == j:
                                continue
                            for pos in possible(sudo, i, k):
                                rowp.append(pos)    # rowp: list of possible values for rest of row
                        rowdiff = possible(sudo, i, j) - set(rowp)    #is a set
                        if len(rowdiff) == 1:
                            sudo[i][j] = rowdiff.pop()
                            curz += 1
                            print(f'\n\t {curz} zero of {allz} zero solved!')
                            fh = 1
                            ff = 1
                            break
                        
                        #column
                        for k in range(len(sudo)):
                            if k == i:
                                continue
                            for pos in possible(sudo, k, j):
                                colp.append(pos)    # colp: list of possible values for rest of column
                        coldiff = possible(sudo, i, j) - set(colp)    
                        if len(coldiff) == 1:
                            sudo[i][j] = coldiff.pop()
                            curz += 1
                            print(f'\n\t {curz} zero of {allz} zero solved!')
                            fh = 1
                            ff = 1
                            break
                        
                        #box
                        boxrow, boxcol = get_box(sudo, i, j)
                        for x in boxrow:
                            for y in boxcol:
                                if (x == i) and (y == j):
                                    continue
                                for pos in possible(sudo, x, y):
                                    boxp.append(pos)    # boxp: list of possible values for rest of box
                        boxdiff = possible(sudo, i, j) - set(boxp)    
                        if len(boxdiff) == 1:
                            sudo[i][j] = boxdiff.pop()
                            curz += 1
                            print(f'\n\t {curz} zero of {allz} zero solved!')
                            fh = 1
                            ff = 1
                            break
                        
                        pdiff = rowdiff.intersection(coldiff, boxdiff)
                        if len(pdiff) == 1:
                            # print('\n\t very Hard!')
                            sudo[i][j] = pdiff.pop()
                            curz += 1
                            print(f'\n\t {curz} zero of {allz} zero solved!')
                            fh = 1
                            ff = 1
                            break


                if fh == 1:
                    break

            #check if solving is completed
            f = 1
            for i in range(0, len(sudo[0])):
                for j in range(0, len(sudo)):
                    if sudo[i][j] == 0:
                        f = 0
                        break
                if f == 0:
                    break
                
        return ff
        

def poslist(sudo):    #cellpos = [[{},{},...], [{},{},...], ...]
    n = range(len(sudo))
    cellpos = [[set() for x in n]for x in n]
    # tmp = set()
    # multiplication = 1
    for i in range(len(sudo[0])):
        for j in range(len(sudo)):
            tmp = set()
            if sudo[i][j] == 0:
                for pos in possible(sudo, i, j):
                    tmp.add(pos)
                cellpos[i][j] = tmp
                # multiplication *= len(tmp)
    return cellpos  #, multiplication

#Naked Subset
def posoptimal(sudo, x, y):
    cellpos = poslist(sudo)
    #row
    for i in range(len(sudo)):
        tmpj = []
        for j in range(len(sudo)):
            if not sudo[i][j]:
                cp = cellpos[i][j]
                break
        for j in range(len(sudo)):
            if not sudo[i][j]:
                cp.intersection(cellpos[i][j])
        if not sudo[i][j]:
            cn = len(cp)    # cp: common possible, cn: number of cp
            for j in range(len(sudo)):
                if cellpos[i][j] == cp:
                    tmpj.append(j)  # tmpj: those ones that its possible exactly equal to cp
            if len(tmpj) == cn:
                for j in range(len(sudo)):
                    if cellpos[i][j]:
                        if j not in tmpj:
                            cellpos[i][j] -= cp

    return cellpos[x][y]

# cellpos, multiplication = poslist(sudo)
rec = 0
def sudorec(sudo):  # Recursive Sudoku Solver (Forcing Chain Technique)
    global rec 
    # global multi
    rec += 1
    if rec % 10000 == 0:
        print(f'Number of recurse: {rec}')
    # percent = rec * 100 / multi 
    # if percent.is_integer():
    #     print(f'{int(percent)}%')
    fr = 0
    cset = set(range(1, len(sudo)+1))
    for i in range(0, len(sudo[0])):
        for j in range(0, len(sudo)):
            if sudo[i][j] == 0:
                fr = 1
                break
        if fr == 1:
            break
    if fr == 0:
        return 1
    for g in cset:  #g: guess
        if g in possible(sudo, i, j):     #possible(sudo, i, j): #cellpos[i][j] #poslist(sudo) #posoptimal(sudo, i, j)
            sudo[i][j] = g
            if sudorec(sudo):
                return 1
            sudo[i][j] = 0
    return 0                              


if __name__ == "__main__":

    # sudo = [[5,1,7,6,0,0,0,3,4],
    #         [2,8,9,0,0,4,0,0,0],
    #         [3,4,6,2,0,5,0,9,0],
    #         [6,0,2,0,0,0,0,1,0],
    #         [0,3,8,0,0,6,0,4,7],
    #         [0,0,0,0,0,0,0,0,0],
    #         [0,9,0,0,0,0,0,7,8],
    #         [7,0,3,4,0,0,5,6,0],
    #         [0,0,0,0,0,0,0,0,0]]

    # sudo = [[0, 15, 0, 1, 0, 2, 10, 14, 12, 0, 0, 0, 0, 0, 0, 0],  #this example takes time
    #         [0, 6, 3, 16, 12, 0, 8, 4, 14, 15, 1, 0, 2, 0, 0, 0],
    #         [14, 0, 9, 7, 11, 3, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [4, 13, 2, 12, 0, 0, 0, 0, 6, 0, 0, 0, 0, 15, 0, 0],
    #         [0, 0, 0, 0, 14, 1, 11, 7, 3, 5, 10, 0, 0, 8, 0, 12],
    #         [3, 16, 0, 0, 2, 4, 0, 0, 0, 14, 7, 13, 0, 0, 5, 15],
    #         [11, 0, 5, 0, 0, 0, 0, 0, 0, 9, 4, 0, 0, 6, 0, 0],
    #         [0, 0, 0, 0, 13, 0, 16, 5, 15, 0, 0, 12, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 9, 0, 1, 12, 0, 8, 3, 10, 11, 0, 15, 0],
    #         [2, 12, 0, 11, 0, 0, 14, 3, 5, 4, 0, 0, 0, 0, 9, 0],
    #         [6, 3, 0, 4, 0, 0, 13, 0, 0, 11, 9, 1, 0, 12, 16, 2],
    #         [0, 0, 10, 9, 0, 0, 0, 0, 0, 0, 12, 0, 8, 0, 6, 7],
    #         [12, 8, 0, 0, 16, 0, 0, 10, 0, 13, 0, 0, 0, 5, 0, 0],
    #         [5, 0, 0, 0, 3, 0, 4, 6, 0, 1, 15, 0, 0, 0, 0, 0],
    #         [0, 9, 1, 6, 0, 14, 0, 11, 0, 0, 2, 0, 0, 0, 10, 8],
    #         [0, 14, 0, 0, 0, 13, 9, 0, 4, 12, 11, 8, 0, 0, 2, 0]]

    # sudo = [[0, 11, 9, 0, 0, 16, 13, 4, 0, 0, 14, 0, 10, 6, 15, 0],   # 16x16
    #         [4, 12, 15, 0, 3, 6, 0, 11, 0, 5, 0, 1, 16, 7, 14, 2],
    #         [1, 0, 6, 0, 15, 2, 0, 0, 11, 9, 10, 0, 0, 0, 8, 0],
    #         [0, 13, 0, 0, 0, 1, 0, 0, 4, 6, 0, 15, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 15, 0, 8, 1, 5, 3, 0, 4, 11, 7],
    #         [6, 0, 1, 0, 0, 12, 8, 0, 9, 0, 0, 2, 0, 0, 3, 0],
    #         [14, 0, 4, 13, 6, 0, 0, 3, 0, 12, 7, 10, 8, 0, 2, 0],
    #         [3, 8, 0, 0, 4, 7, 2, 0, 6, 0, 0, 0, 0, 12, 16, 5],
    #         [13, 0, 0, 16, 0, 8, 14, 10, 3, 4, 15, 0, 12, 5, 1, 11],
    #         [0, 0, 0, 6, 2, 0, 0, 1, 10, 0, 11, 0, 15, 3, 0, 9],
    #         [7, 0, 0, 12, 0, 4, 0, 15, 5, 0, 9, 14, 0, 0, 0, 0],
    #         [10, 0, 0, 8, 0, 0, 11, 0, 0, 0, 1, 12, 4, 0, 13, 16],
    #         [0, 0, 0, 0, 0, 0, 7, 0, 15, 2, 0, 0, 0, 0, 12, 3],
    #         [0, 0, 7, 0, 0, 10, 6, 0, 1, 8, 0, 13, 11, 0, 9, 14],
    #         [8, 6, 5, 0, 0, 3, 0, 0, 14, 0, 0, 9, 0, 0, 0, 0],
    #         [0, 16, 0, 2, 0, 0, 0, 14, 0, 10, 0, 0, 0, 0, 0, 0]]


    # sudo = [[24, 0, 0, 0, 0, 14, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # Hardest 25x25
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0],     # this example takes time
    #         [0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 0, 15, 0, 1, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 9, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    #         [0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 8, 0],
    #         [0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 15, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 21, 0, 0],
    #         [0, 0, 14, 0, 0, 0, 20, 0, 0, 0, 4, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0],
    #         [0, 9, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 6, 0, 20, 0, 0, 0],
    #         [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 1, 20, 5, 15, 0, 0, 25, 0, 0, 17, 0, 0, 0, 0, 2, 0, 24, 0, 0],
    #         [0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 8, 0, 0, 0, 0],
    #         [0, 8, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 24, 18, 6, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 6, 0, 3, 0, 0],
    #         [0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 7, 0, 0, 2, 0, 0, 0],
    #         [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 11, 0, 20, 0],
    #         [0, 15, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 2, 19, 0]]

    sudo = [[8, 0, 0, 0, 0, 0, 0, 0, 0],    #hardest 9x9 sudoku untill 2012
            [0, 0, 3, 6, 0, 0 ,0 ,0 ,0],    #Finnish mathematician Arto Inkala
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]]


    ff = sudoku(sudo)
    fff = 1
    if ff == 0:
        print('\n\t Technique: recursive(Forcing Chain)!')
        # cellpos, multi = poslist(sudo)
        # poslist(sudo)
        # print(*cellpos, sep='\n')
        # print(multi)
        if sudorec(sudo) == 0:
            fff = 0
        else:
            ff = 1

    if (ff == 1) and (fff == 1):
        print('\n\t Solved!')
    else:
        print("\n\t It can't be solved anymore!")
    
    print('\n')
    print(*sudo, sep='\n')
            

