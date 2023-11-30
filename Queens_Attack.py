def total_attacks(n,r_q,c_q):
    r_c = (n-1) * 2
    lu = min(n - r_q , c_q - 1)
    ld = min(r_q - 1 , c_q - 1)
    ru = min(n- r_q , n - c_q)
    rd = min(r_q - 1 , n - c_q)
    
    count = lu + ld + ru + rd + r_c
    return count

def queen_attacks(n,k,r_q,c_q,obstacles):
    
    total = total_attacks(n , r_q ,c_q)
    m = 0
    arr = [[0],[0],[0],[0],[0],[0],[0],[0]]
    if k == 0 :
        return total
    
    else:
        for r , c in obstacles:
            if r == r_q :
                if c > c_q:
                    arr[0].append(n-c+1)
                else:
                    arr[1].append(c-1+1)
                    
            elif c == c_q :
                if r > r_q:
                    arr[2].append(n-r+1)
                    
                else:
                    arr[3].append( r-1+1)
                    
            elif (r_q - c_q) == (r-c):
                if r > r_q and c > c_q :
                    arr[4].append(min(n-r , n-c) + 1)
                    
                elif r < r_q and c < c_q :
                    arr[5].append(min(r-1,c-1) + 1)
                    
            elif r_q + c_q == r+c:
                if r > r_q and c < c_q :
                    arr[6].append(min(n-r , c-1) + 1)
                    
                elif r < r_q and c > c_q :
                    arr[7].append(min(r-1,n-c) + 1)
                    
        
        for s in arr:
            m += max(s)
                    
        return (total - m)

def main():
    n , k = map(int,input().split())
    r_q,c_q = map(int,input().split())
    
    obstacles = []
    for s in range(k):
        obstacles.append(list(map(int,input().strip().split())))
        
    count_attacks = queen_attacks(n,k,r_q,c_q,obstacles)
    print(count_attacks)
    
if __name__ == '__main__':
    main()
    