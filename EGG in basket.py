def diagonal_sum_check(matrix_list,sumL):
    ln=len(matrix_list)
    lds=0
    rds=0
    for i in range(ln):
        lds+=matrix_list[i][i]
        rds+=matrix_list[-i-1][i]

    if rds==sumL and lds==sumL:
        return True
    return False

def row_sum_check(matrix_list,suml):
    s=[]
    for i in matrix_list:
        s.append(sum(i))
    for i in s:
        if suml!=i:
            return False
    return True

def column_sum_check(matrix_list,suml):
    r=[]
    for i in range(len(matrix_list)):
        s=0
        for j in range(len(matrix_list)):
            s+=matrix_list[j][i]
        r.append(s)
    for i in r:
        if suml!=i:
            return False
    return True

def magic_matrix_check(matrix_list):
    suml = sum(matrix_list[0])
    if diagonal_sum_check(matrix_list,suml) and row_sum_check(matrix_list,suml) and column_sum_check(matrix_list,suml):
        return True
    return False

def list_matrix_convert(list,order):
    matrix_list=[]
    i=0
    for x in range(order):
        matrix_list.append([])
        for y in range(order):
            matrix_list[x].append(list[i])
            i+=1
    return matrix_list

def matrix_convert(n,order):
    if n%(order**2)==0:
        num=n//(order**2)
        matrix=[]
        for i in range(order):
            l=[]
            for i in range(order):
                l.num(n)
            matrix.append(l)
        return matrix

def addperm(x,l):
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]

 
if __name__=="__main__":

    n=list(map(int,input().split()))
    N=int(input())
    m_list=list_matrix_convert(n,N)

    if magic_matrix_check(m_list):
        print("Required Matrix is:")
        for i in m_list:
            print(*i)
    else:
        for i in perm(n):
            if magic_matrix_check(list_matrix_convert(i,N)):
                
                print("Required Matrix is:")
                for i in list_matrix_convert(i,N):
                    print(*i)
                break