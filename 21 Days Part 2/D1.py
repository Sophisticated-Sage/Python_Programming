n = int(input("Enter a limit: "))
x = int(input("Enter a term no: "))
    
def fig(n):
    if n == 0 or n == 1:
        return n
    else:
        return fig(n-1) + fig(n-2)

def fig2(x):    
    if x == 0 or x == 1:
        return x
    else:
        return fig2(x-1) + fig2(x-2)

print("Fibonacci sequence (Option 1):")
for i in range(n):
    print(fig(i), end=" ")
    
print(f"\n\nFibonacci sequence (Option 2): {fig2(x)}")