
condition = 42>2
if condition:
    print("condition was True.")
elif not condition: 
    print("condition was False.")


age = 0
while age < 19:
    age = age + 1
    if  age % 2:
        print("age is {}".format(age))
    elif age < 17:
        break


try:
    4 / 2
except Exception:
    print("This is executed when theres Exception on the Try block. Fix the Try code block !")
else:
    print("This is executed when theres NO Exception on the Try block. The Try code block is Ok !")
finally:
    print("This is always executed.")
