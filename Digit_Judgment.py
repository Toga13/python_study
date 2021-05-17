while True:
    try:
        number = int(input("Please enter an integer number:"))
        break
    except ValueError:
        print("A non-integer number has been entered. Try again...")
count = 1 
while number >= 10:
    number = number / 10
    count = count + 1
else:
    print("Digit number: %d"%(count))