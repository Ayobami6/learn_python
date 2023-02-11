# factorial recursion function
def fact(val):
    if val == 1:
        return 1
    else:
        result = val * fact(val - 1)
        return result


print(fact(5))
