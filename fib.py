def fib(n):
    if n == 0:
        return 0 # First case if n is 0 then return 0
    elif n == 1:
        return 1 # second case if n is 1 then return 1

    return  fib(n-2) + fib(n-1)
  
item_to_calculate = int(input("what fibonnaci item would you like to calculate? "))
print(fib(item_to_calculate))