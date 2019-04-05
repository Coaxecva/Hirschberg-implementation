#!/usr/bin/env python3

def print_matrix(a, m, n):
    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print()

def lcs_algo_A(X, Y, m, n): 
    L = [[0 for x in range(n+1)] for x in range(m+1)]     
    # Following steps build L[m+1][n+1] in bottom up fashion. Note 
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]  
    for i in range(1, m+1): 
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
    return L
    
def lcs(X, Y, m, n, L):
    index = L[m][n]   
    # Create a character array to store the lcs string 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
    # Start from the right-most-bottom-most corner and 
    # one by one store characters in lcs[] 
    i = m 
    j = n 
    while i > 0 and j > 0:   
        # If current character in X and Y are same, then 
        # current character is part of LCS 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    return "".join(lcs)
    
  
def lcs_algo_B(X, Y, m, n):
    if m==0 or n==0:
        return 0
    # Initialization
    K = [[0 for i in range(n+1)] for j in range(2)] 
  
    for i in range(1, m+1):
        K[0] = K[1][:]
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                K[1][j] = K[0][j-1] + 1
            else:
                K[1][j] = max(K[1][j-1], K[0][j])
    #return K
    return K[1][n]

def lcs_algo_C(X, Y, m, n):
    # X is empty
    if m == 0:
        return ""
    if m == 1:
        # Check if only 1 character X in Y
        for c in Y:
            if c == X[0]:
                return c
        return ""
    # X has more than 1 character
    ll = lcs_algo_B(X, Y, m, n)
    l1 = 0
    l2 = 0
    # Split X
    x1 = X[:m//2]
    x2 = X[m//2:]
    # Check for correct split of Y
    kk = -1
    for k in range(n):
        l1 = lcs_algo_B(x1, Y[:k], m//2, k)
        l2 = lcs_algo_B(x2, Y[k:], m-m//2, n-k)
        if ll == l1+l2:
            kk = k
            break

    # Flag!!!!
    if kk == -1:
        print("BUG HERE!!!")

    # Split Y
    y1 = Y[:kk]
    y2 = Y[kk:]
    # Solve simpler problems
    c1 = lcs_algo_C(x1, y1, m//2, kk)
    c2 = lcs_algo_C(x2, y2, m-m//2, n-kk)
    return c1+c2


if __name__ == '__main__':
    
    # Init
    X = "AGGTCCAB"
    Y = "GXTCXXXCXAYB"
    m = len(X) 
    n = len(Y) 

    # Algorithm A
    L_A = lcs_algo_A(X, Y, m, n) 
    print_matrix(L_A, m+1, n+1)    
    strlcs = lcs(X, Y, m, n, L_A)
    print("LCS (" + X + ", " + Y + ") = " + strlcs)

    # Algorithm B
    #L_B = lcs_algo_B(X, Y, m, n)
    #print_matrix(L_B, 2, n+1)

    # Algorithm C
    strlcs1 = lcs_algo_C(X, Y, m, n)
    print("LCS (" + X + ", " + Y + ") = " + strlcs1)    