import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr]); ptr += 1
    m = int(data[ptr]); ptr += 1
    x = int(data[ptr]); ptr += 1
    y = int(data[ptr]); ptr += 1
    
    threshold = (x * y + 1) // 2
    awake = 0
    
    
    windows = []
    for _ in range(n * x):
        windows.append(data[ptr])
        ptr += 1
    
   
    for floor in range(n):
        for apt in range(m):
            lit = 0
            
            for i in range(x):
                row = windows[floor * x + i]
                start_col = apt * y
                for j in range(y):
                    if row[start_col + j] == 'X':
                        lit += 1
                        if lit >= threshold:  
                            break
                if lit >= threshold:
                    break
            if lit >= threshold:
                awake += 1
    
    print(awake)

if __name__ == "__main__":
    main()
