#  Countdown recursion

def countdown(val):
    if val == 0:
        print("Done")
        return
    else:
        print(val, ".counting.....")
        countdown(val-1)
        print(f"Stack{val}")


countdown(5)
