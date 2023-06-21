from collections import deque
n=11
m=14
krajX=[[6,14],[14,14]]
krajO=[[6,6],[14,6]]
zid=[5,6,9]
tipovi=[1,2,3,4]
zidX=[3,3]
zidO=[3,3]
stanja=[]
zi=0
def postavi():
    zi=int(input("uneti broj zidova: "))      
    n=int(input("uneti n: "))
    m=int(input("uneti m: "))
    matricaX = [[0 for x in range(2*n-1)] for y in range(2*m-1)]
    print("uneti 4 kordinate (za x1,x2)")
    x1,y1,x2,y2=map(int, input().split())
    print("uneti 4 kordinate (za o1,o2)")
    ox1,oy1,ox2,oy2=map(int, input().split())
    krajX[0][0]=(ox1-1)*2
    krajX[0][1]=(oy1-1)*2
    krajX[1][0]=(ox2-1)*2
    krajX[1][1]=(oy2-1)*2
    krajO[0][0]=(x1-1)*2
    krajO[0][1]=(y1-1)*2
    krajO[1][0]=(x2-1)*2
    krajO[1][1]=(y2-1)*2
    matricaX[(x1-1)*2][(y1-1)*2]=1
    matricaX[(x2-1)*2][(y2-1)*2]=2
    matricaX[(ox1-1)*2][(oy1-1)*2]=3
    matricaX[(ox2-1)*2][(oy2-1)*2]=4
    zidX[0]=zi
    zidX[1]=zi
    zidO[0]=zi
    zidO[1]=zi
    return [matricaX,n,m,zi]

def crtaj(matrix):
    #################### gornji deo matrice
    for row in range(2):
        print(" ", end =" ")
        for x in range(n):
            if row == 0:
                if x <= 8:
                    print(x+1, end =" ")
                else:
                    print(chr(ord('A')+x-10+1),end=" ")
            else:
                print("=", end =" ")
        print("") 
    ##################### levi deo matrice
    for i in range(2*m-1):
        if(i%2==0):
            if i < 18:
                print(int(i/2)+1, end ="ǁ")##1. u koloni
            else:
                print(chr(ord('A')+int(i/2)-9),end="ǁ")##1. u koloni
        else:
            print("  ",end="")
    ###################### matrica
        for j in range(2*n-1):
            if(matrix[i][j]==5):
                print("=",end="")
            elif(matrix[i][j]==6):
                print("ǁ",end="")            
            elif(i%2==0 and j%2!=0):
                print("|",end="")            
            elif(i%2!=0 and j%2==0):
                print("-",end="")
            elif(matrix[i][j]==1 or matrix[i][j]==2):
                print("X",end="")
            elif(matrix[i][j]==3 or matrix[i][j]==4):
                print("O",end="")
            elif([i,j]in krajX or [i,j] in krajO):
                print(".",end="")
            elif(matrix[i][j]==0 and i%2==0):
                print(" ",end="")             
            else:
                print(" ",end="")

        if(i%2==0):
            if i < 18:
                print("ǁ",end="")##1. u koloni
                print(int(i/2+1),end="")
            else:
                print("ǁ",end=chr(ord('A')+int(i/2)-9))##1. u koloni
        else:
            print("  ",end="")    

        print("")
    for row in range(2):        
        print(" ", end =" ")
        for x in range(n):
            if row == 0:
                print("=", end =" ")
            else:
                if x <= 8:
                    print(x+1, end =" ")
                else:
                    print(chr(ord('A')+x-10+1),end=" ")
        print("")

def kraj():
    x1=kordinate(matrica, 1)
    x2=kordinate(matrica, 2)
    o1=kordinate(matrica, 3)
    o2=kordinate(matrica, 4)
    if([x1[0],x1[1]] in krajX or [x2[0],x2[1]]in krajX):        
        return 0        
    if([o1[0],o1[1]] in krajO or [o2[0],o2[1]]in krajO):        
        return 1
    return 404

def isPath(matrix,n,m):
    visited = [[False for x in range (n)]
                      for y in range (m)]
    flag = False 
    for i in range (m):
        for j in range (n):
            if (matrix[i][j] == 1 and not
                visited[i][j]):
                if (checkPath(matrix, i,
                              j, visited)):
                    flag = True
                    break
    if (flag):
        return True
    else:
        return False
def isSafe(i, j, matrix):   
    if (i >= 0 and i < len(matrix) and
        j >= 0 and j < len(matrix[0])):
        return True
    return False
def checkPath(matrix, i, j,visited):
    if (isSafe(i, j, matrix) and
        matrix[i][j] != 0 and not
        visited[i][j]):
        visited[i][j] = True
        if (matrix[i][j] == 2):
           return True
        up = checkPath(matrix, i - 1,
                       j, visited)
        if (up):
           return True
        left = checkPath(matrix, i,
                         j - 1, visited)
        if (left):
           return True
        down = checkPath(matrix, i + 1,
                         j, visited)
        if (down):
           return True
        right = checkPath(matrix, i,
                          j + 1, visited)
        if (right):
           return True
    return False

def postojiput(matrix,startx,starty,endx,endy,mininiz):
    mat = [[0 for x in range(2*n-1)] for y in range(2*m-1)]
    for i in range(2*m-1):
        for j in range(2*n-1):
            if(i == startx and j == starty):
                mat[i][j]=1
            else:
                if (i == endx and j == endy):
                    mat[i][j]=2
                else:  
                    if(matrix[i][j]== 5 or matrix[i][j]== 6 or matrix[i][j]== 9):
                        mat[i][j]= 0
                    else:
                        if([i,j]in mininiz):
                            mat[i][j]= 0   
                        else:        
                            mat[i][j]=3
    return isPath(mat,2*n-1,2*m-1)

def dodajzid(matrix,vrsta,i,j):
    i=(i-1)*2
    j=(j-1)*2
    mininiz=[]
    if(vrsta == 'z' and j>=0 and j< 2*n-2 and
      i>=0 and i < m*2 - 2  and not(matrix[i+1][j]==5 and
      matrix[i+1][j+2]==5) and matrix[i][j+1]!=6 and
      matrix[i+2][j+1]!=6 ):        
        mininiz=[[i,j+1],[i+1,j+1],[i+2,j+1]]
        if(i<2*m-5):
            mininiz.append([i+3,j+1])
        if(postojeSviPutevi(matrix,mininiz)==8):
            matrix[i][j+1]=6
            matrix[i+1][j+1]=9
            matrix[i+2][j+1]=6
            if(i<2*m-5):
                    matrix[i+3][j+1]=9
            return 1               
    else:        
        if(vrsta == 'p' and j>=0 and j< 2*n-2 and
        i>=0 and i<2*m-2 and not(matrix[i][j+1]==6 and
        matrix[i+2][j+1]==6) and matrix[i+1][j]!=5 and
         matrix[i+1][j+2]!=5):            
            mininiz=[[i+1,j],[i+1,j+1],[i+1,j+2]]
            if(j<2*n-5):
                mininiz.append([i+1,j+3])
            if(postojeSviPutevi(matrix,mininiz)==8):                       
                matrix[i+1][j]=5   
                matrix[i+1][j+1]=9         
                matrix[i+1][j+2]=5
                if(j<2*n-5):
                    matrix[i+1][j+3]=9
                return 1    
    return 0
def kordinate(matrix,tip):
    for i in range(2*m-1):
        for j in range(2*n-1):
            if matrix[i][j]==tip:
                return [i,j]
def sviigraci(matrix):
    x1=kordinate(matrix,1)
    x2=kordinate(matrix,2)
    o1=kordinate(matrix,3)
    o2=kordinate(matrix,4)
    return [[x1[0],x1[1]],[x2[0],x2[1]],[o1[0],o1[1]],[o2[0],o2[1]]]

def nemaZid(matrix,tip,x2,y2):
    igrac=kordinate(matrix,tip)
    x1=igrac[0]
    y1=igrac[1]
    svi=sviigraci(matrix)    
    #DOLE    
    if x2<0 or x2>2*m-1 or y2 < 0 or y2 > 2*n-1:
        return 0
    if abs(x2-x1)==4 and x2>x1 and y1==y2:#dole dva
        if(matrix[x1+1][y1] in zid or matrix[x1+3][y1] in zid):
            return 0
        else:
            return 1
    if abs(x2-x1)==2 and x2>x1 and y1==y2:#dole jedno
        if (matrix[x1+1][y1] in zid ):
            return 0
        elif(x1==2*(m-2) or matrix[x1+3][y1] in zid or [x2+2,y2]in svi or [x2,y2] in svi or [x2,y2] in krajX or [x2,y2] in krajO):
            return 1
        else:
            return 0
    #GORE
    if abs(x2-x1)==4 and x2<x1 and y1==y2:#gore dva 
        if(matrix[x1-1][y1] in zid or matrix[x1-3][y1] in zid):
            return 0
        else:
            return 1
    if abs(x2-x1)==2 and x2<x1 and y1==y2:#gore jedno
        if (matrix[x1-1][y1] in zid):
            return 0
        elif(x1==2 or matrix[x1-3][y1] in zid or [x2-2,y2]in svi or [x2,y2] in svi or [x2,y2] in krajX or [x2,y2] in krajO):
            return 1
        else:
            return 0
    #LEVO
    if abs(y2-y1)==4 and y2<y1 and x1==x2:#levo dva
        if(matrix[x1][y1-1] in zid or matrix[x1][y1-3] in zid ):
            return 0
        else:            
            return 1
    if abs(y2-y1)==2 and y2<y1 and x1==x2:#levo jedno
        if (matrix[x1][y1-1] in zid):
            return 0
        elif(matrix[x1][y1-3] in zid or [x2,y2-2]in svi or y1==2 or [x2,y2] in svi or [x2,y2] in krajX or [x2,y2] in krajO):
            return 1
        else:
            return 0
    #DESNO
    if abs(y2-y1)==4 and y2>y1 and x1==x2:#desno dva
        if(matrix[x1][y1+1] in zid or matrix[x1][y1+3] in zid ):
            return 0
        else:
            return 1
    if abs(y2-y1)==2 and y2>y1 and x1==x2:#desno jedno
        if (matrix[x1][y1+1] in zid):
            return 0
        elif(y1==2*(n-2) or matrix[x1][y1+3] in zid   or [x2,y2+2]in svi or [x2,y2] in svi or [x2,y2] in krajX or [x2,y2] in krajO):
            return 1
        else:
            return 0
    #COSKOVI
    if(x2==x1-2 and y2==y1-2):#gorelevo
        if ((matrix[x1-2][y1-1]in zid and matrix[x1-1][y1-2]in zid) or (matrix[x1-1][y1]in zid and matrix[x1-1][y1-2]in zid)or (matrix[x1][y1-1] in zid and matrix[x1-2][y1-1]in zid) or (matrix[x1-1][y1]in zid and matrix[x1][y1-1]in zid)):
            return 0
        else:
            return 1
    if(x2==x1-2 and y2==y1+2):#goredesno
        if ((matrix[x1-1][y1] in zid and matrix[x1-1][y1+2] in zid) or (matrix[x1-2][y1+1] in zid and matrix[x1-1][y1+2] in zid) or (matrix[x1-1][y1]in zid and matrix[x1][y1+1]in zid)or (matrix[x1-2][y1+1]in zid and matrix[x1][y1+1]in zid)):
           return 0
        else:
            return 1
    if(x2==x1+2 and y2==y1-2):#dolelevo
        if ((matrix[x1+1][y1] in zid and matrix[x1+1][y1-2] in zid) or (matrix[x1+1][y1-2] in zid and matrix[x1+2][y1-1] in zid)or (matrix[x1][y1-1] in zid and matrix[x1+2][y1-1] in zid)or (matrix[x1][y1-1] in zid and matrix[x1+1][y1] in zid)):
           return 0
        else:
            return 1
    if(x2==x1+2 and y2==y1+2):#doledesno
        if ((matrix[x1+1][y1] in zid and matrix[x1+1][y1+2] in zid) or (matrix[x1+1][y1+2] in zid and matrix[x1+2][y1+1] in zid)or (matrix[x1][y1+1] in zid and matrix[x1+2][y1+1] in zid)or (matrix[x1][y1+1] in zid and matrix[x1+1][y1] in zid)):
           return 0
        else:
            return 1  

def postojeSviPutevi(matrix,mininiz):
    br=0
    for i in range(1,5):
        for j in range(2):
            igrac=kordinate(matrix,i)
            if igrac:
                x=igrac[0]
                y=igrac[1]
                if i < 3:
                    end=krajX[j%2]
                    if postojiput(matrix,x,y,end[0],end[1],mininiz):
                        br+=1
                else:
                    end=krajO[j%2]
                    if postojiput(matrix,x,y,end[0],end[1],mininiz):
                        br+=1
            else:
                br=8     
    return br
def prazno(x,y):
    if matrica[x][y] == 0:
        return True
    return False
def pomeriIgraca(matrix,tip,x,y):
    x2=2*(x-1)
    y2=2*(y-1)
    igrac=kordinate(matrix,tip)
    x1=igrac[0]
    y1=igrac[1]
    svi=sviigraci(matrix)
    if nemaZid(matrix,tip,x2,y2):
        if(([x2,y2] in svi and (([x2,y2] in krajX and (tip==1 or tip ==2)) or ([x2,y2] in krajO and (tip==3 or tip ==4))))or not [x2,y2] in svi):
            matrix[x1][y1]=0
            matrix[x2][y2]=tip            
            return True
    return False
def kopiraj(mat1):
    mat2 = [[0 for x in range(2*n-1)] for y in range(2*m-1)]
    for i in range(2*m-1):
            for j in range(2*n-1):
                mat2[i][j]=mat1[i][j]
    return mat2
def sviZidovi(matrix,tip):
    lista = []
    if ((tip==1 or tip==2) and not zidX[0]+zidX[1]==0)or ((tip==3 or tip==4) and  not zidO[0]+zidO[1]==0):
        for i in range(1,m+1):
            for j in range(1,n+1):
                if((tip==1 or tip==2)and zidX[0]>0)or((tip==3 or tip==4)and zidO[0]>0):
                    mat3=kopiraj(matrix) # novi X
                    if krajmat(matrix) or dodajzid(mat3,'p',i,j):
                        lista.append(mat3)
                if((tip==1 or tip==2)and zidX[1]>0)or((tip==3 or tip==4)and zidO[1]>0): 
                    mat3=kopiraj(matrix) # novi X
                    if krajmat(matrix) or dodajzid(mat3,'z',i,j):
                        lista.append(mat3)
        return lista
    else:
        mat3=kopiraj(matrix)
        lista.append(mat3)
        return lista
def krajmat(matrix):
    x1=kordinate(matrix,1)
    x2=kordinate(matrix,2)
    o1=kordinate(matrix,3)
    o2=kordinate(matrix,4)
    if x1 in krajX or x2 in krajX or o1 in krajO or o2 in krajO:
        return True 
def listaStanja(matrix,tip):#1 3    
    list = []    
    for igrac in range(2): #0 1  
        kord=kordinate(matrix,tip+igrac)
        x1=int((kord[0]/2)+1)
        y1=int((kord[1]/2)+1)      
        mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1-2,y1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1-1,y1-1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1-1,y1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1-1,y1+1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1,y1-2):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1,y1-1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1,y1+1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1,y1+2):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1+1,y1-1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1+1,y1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1+1,y1+1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
        if pomeriIgraca(mat2,int(tip+igrac),x1+2,y1):
            l = sviZidovi(mat2,tip)
            for i in range(len(l)):
                list.append(l[i])
            mat2=kopiraj(matrix)
    return list

def dodajStanje(mat):
    matrix = [[0 for x in range(2*n-1)] for y in range(2*m-1)]
    for i in range(2*m-1):
        for j in range(2*n-1):
            matrix[i][j]=mat[i][j]
    stanja.append(matrix)

delta_x = [-1, 1, 0, 0]
delta_y = [0, 0, 1, -1]

def valid(x, y, graph):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[x]):
        return False
    return (graph[x][y] != 1)

def solve(start, end,graph):
    Q = deque([start])
    dist = {start: 0}
    while len(Q):
        curPoint = Q.popleft()
        curDist = dist[curPoint]
        if curPoint == end:
            return curDist
        for dx, dy in zip(delta_x, delta_y):
            nextPoint = (curPoint[0] + dx, curPoint[1] + dy)
            if not valid(nextPoint[0], nextPoint[1],graph) or nextPoint in dist.keys():
                continue
            dist[nextPoint] = curDist + 1
            Q.append(nextPoint)

def oceni(stanje):     
    mat = [[0 for x in range(2*n-1)] for y in range(2*m-1)]
    for i in range(2*m-1):
        for j in range(2*n-1):
            if(stanje[i][j]==1):
                x1x=i
                x1y=j
                if [x1x,x1y] in krajX:
                    return -999           
            elif(stanje[i][j]==2):
                x2x=i
                x2y=j
                if [x2x,x2y] in krajX:
                    return -999
            elif(stanje[i][j]==3):
                o1x=i
                o1y=j
                if [o1x,o1y] in krajO:
                    return 999
            elif(stanje[i][j]==4):
                o2x=i
                o2y=j
                if [o2x,o2y] in krajO:
                    return 999                 
            elif(stanje[i][j]== 5 or stanje[i][j]== 6 or stanje[i][j]== 9):
                mat[i][j]= 1

    x=min(solve((x1x,x1y),(krajX[0][0],krajX[0][1]),mat),
    solve((x1x,x1y),(krajX[1][0],krajX[1][1]),mat),
    solve((x2x,x2y),(krajX[0][0],krajX[0][1]),mat),
    solve((x2x,x2y),(krajX[1][0],krajX[1][1]),mat))

    o=min(solve((o1x,o1y),(krajO[0][0],krajO[0][1]),mat),
    solve((o1x,o1y),(krajO[1][0],krajO[1][1]),mat),
    solve((o2x,o2y),(krajO[0][0],krajO[0][1]),mat),
    solve((o2x,o2y),(krajO[1][0],krajO[1][1]),mat))
    return x-o
def brzidova(stanje,tip):#1-x 2-O
    brz=0
    brp=0
    for i in range(2*m-1):
        for j in range(2*n-1):
            if stanje[i][j]==5:
                brp+=1
            elif stanje[i][j]==6:
                brz+=1
    if tip==1:
        if brp/2 + zidX[0] + zidO[0] != 2*zi:
            zidX[0]-=1
            return
        if brz/2 + zidX[1]+zidO[1]!=2*zi:
            zidX[1]-=1
            return
    if tip==2:
        if brp/2 + zidX[0] + zidO[0] != 2*zi:
            zidO[0]-=1
            return
        if brz/2 + zidX[1]+zidO[1]!=2*zi:
            zidO[1]-=1
            return
end=2
br=0
pos = postavi()
n=pos[1]
m=pos[2]
zi=pos[3]
matrica=pos[0]
crtaj(matrica)

def minimax(depth, stanje, maximizingPlayer, alpha, beta,pocetno=None):
    if depth == 2 or krajmat(stanje):
        return (pocetno,oceni(stanje))
    if maximizingPlayer: 
        novastanja = listaStanja(stanje,3)
        if novastanja is None or len(novastanja)==0:
            return (pocetno,oceni(stanje))   
        best = ('a',-1000)
        for s in novastanja:             
            val = minimax(depth + 1, s ,
                          False, alpha, beta,s if pocetno is None else pocetno)
            best = max(best, val,key=lambda x:x[1])
            alpha = max(alpha, best,key=lambda x:x[1])             
            if beta[1] <= alpha[1]:
                break          
        return best      
    else:
        novastanja = listaStanja(stanje,1)
        if novastanja is None or len(novastanja)==0:
            return (pocetno,oceni(stanje))
        best = ('a',1000)
        for s in novastanja:          
            val = minimax(depth + 1,s,
                            True, alpha, beta,s if pocetno is None else pocetno)
            best = min(best, val,key=lambda x:x[1])
            beta = min(beta, best,key=lambda x:x[1]) 
            if beta[1] <= alpha[1]:
                break          
        return best
prvi = int(input("Unesite 1 da igrate prvi ili 2 da racunar igra prvi"))
while end!=0 and end!=1:   
        ispravno = False    
        if br%2==0:
            while(ispravno==False):#X igrac
                if prvi == 1:
                    tip12=False
                    print("igrac X(1|2),nova koordinata x , y: ")           
                    tip, x, y = map(int, input().split())
                    if tip == 1 or tip ==2:
                        tip12=True        
                        
                    if tip12 and pomeriIgraca(matrica,tip,x,y):
                        ispravanzid=False
                        if kraj()==0:
                            ispravno=True
                            ispravanzid=True
                        if zidX[0]+zidX[1]!=0:
                            while not ispravanzid:
                                print("boja zida(p|z):",end="")
                                boja=input()     
                                print("x: ",end="")               
                                x=int(input())
                                print("y: ",end="")
                                y=int(input())
                                if boja =='p':
                                    if zidX[0]>0:
                                        if dodajzid(matrica,'p',x,y):
                                            zidX[0]-=1
                                            ispravanzid=True
                                            ispravno = True
                                            br+=1
                                            crtaj(matrica)
                                            dodajStanje(matrica)
                                    else:
                                        print("NEMATE PLAVIH ZIDOVA,DODAJTE ZELENE")
                                elif boja =='z':
                                        if zidX[1]>0:
                                            if dodajzid(matrica,'z',x,y):
                                                zidX[1]-=1
                                                ispravanzid=True
                                                ispravno = True
                                                br+=1
                                                crtaj(matrica)
                                                dodajStanje(matrica)
                                        else:
                                            print("NEMATE ZELENIH ZIDOVA,DODAJTE PLAVE")
                                else:
                                    print("UNESITE z ili p")
                        else:
                            ispravno = True
                            crtaj(matrica)
                            br+=1
                else:
                    potez = minimax(0,matrica,False,(matrica,-1000),(matrica,1000))                    
                    matrica = potez[0]
                    brzidova(matrica,1)
                    print(zidX)
                    print(zidO)
                    ispravno = True
                    br+=1
                    crtaj(matrica)
        else:
            while(ispravno==False):#O igrac
                if prvi == 2:
                    tip12=False
                    print("igrac O(1|2),nova koordinata x , y: ")           
                    tip, x, y = map(int, input().split())
                    if tip == 1 or tip ==2:
                        tip12=True        
                    tip+=2    
                    if tip12 and pomeriIgraca(matrica,tip,x,y):
                        ispravanzid=False
                        if kraj()==1:
                                ispravno=True
                                ispravanzid=True
                        if zidO[0]+zidO[1]!=0:                
                            while not ispravanzid :
                                print("boja zida(p|z):",end="")
                                boja=input()     
                                print("x: ",end="")               
                                x=int(input())
                                print("y: ",end="")
                                y=int(input())
                                if boja =='p':
                                    if zidO[0]>0:
                                        if dodajzid(matrica,'p',x,y):
                                            zidO[0]-=1
                                            ispravanzid=True
                                            ispravno = True
                                            br+=1
                                            crtaj(matrica)
                                            dodajStanje(matrica)
                                    else:
                                        print("NEMATE PLAVIH ZIDOVA,DODAJTE ZELENE")
                                elif boja =='z':
                                        if zidO[1]>0:
                                            if dodajzid(matrica,'z',x,y):
                                                zidO[1]-=1
                                                ispravanzid=True
                                                ispravno = True
                                                br+=1
                                                crtaj(matrica)
                                                dodajStanje(matrica)
                                        else:
                                            print("NEMATE ZELENIH ZIDOVA,DODAJTE PLAVE")
                                else:
                                    print("UNESITE z ili p")
                        else:
                                ispravno = True
                                crtaj(matrica)
                                br+=1
                else:
                   potez = minimax(0,matrica,True,(matrica,-1000),(matrica,1000))
                   matrica = potez[0]
                   brzidova(matrica,2)
                   print(zidX)
                   print(zidO)
                   ispravno = True
                   br+=1
                   crtaj(matrica)
        end=kraj()

##for x in range(len(stanja)):
##    crtaj(stanja[x])
if (end==0):
    print("POBEDA X")
else:
    print("POBEDA O")