from random import randint
for i in range (1,11):
    num1 = randint (1,10)
    num2 = randint (1,10)
    print ("Question",i,":",num1,"*",num2,"=", end = " ")
    guess = int (input())
    answer = num1*num2
    if guess == answer:
        print ("Right!")
    else:
        print ("Wrong. The answer is: ",answer)

