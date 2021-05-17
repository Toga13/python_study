i = 0 
for i in range(1,101):  
    if i%15==0:    #15で割り切れる場合
        print("FizzBuzz")

    elif i%5==0:  #5で割り切れる場合
        print("Buzz")

    elif i%3==0:  #3で割り切れる場合
        print("Fizz")

    else:  #どれでも割り切れない場合
        print(i)