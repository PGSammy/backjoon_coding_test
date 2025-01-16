import sys
input = sys.stdin.readline

def count_triangles(n):
    if n < 3:
        return 0
    
    count = 0
    max_side = (n - 1) // 2 
    
    for a in range(1, min(n//3 + 1, max_side)):
        b_start = a
        b_end = min((n-a)//2, max_side)
        
        if b_start > b_end:
            break
            
        count += max(0, b_end - b_start + 1)
        
    return count

n = int(input())

result = count_triangles(n)

print(result)