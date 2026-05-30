'''
def countdown(n):
    if n == 0:
        print("Happy Birthday")
        return
    
    print(n)
    countdown(n-1)
countdown(10)
'''

print("\n")
def sum_natural_num(n):
    if n == 0:
        return 0
    
    return n + sum_natural_num(n-1)

print(sum_natural_num(20))
