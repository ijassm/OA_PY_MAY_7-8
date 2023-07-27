try:
    a = 10
    print("working")
    print(a)
except NameError:
    print("Please check your variables")
except ZeroDivisionError:
    raise ZeroDivisionError("you can't divide by zero")
except:
    print("something went wrong")
else:
    print("try block ran without error")
finally:
    print("finally code ends☻")
