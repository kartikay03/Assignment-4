# python program to  ask user to enter marks and print the corresponding grade.
print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=80 and avg<100:
    print("Your Grade is A")
elif avg>=60 and avg<80:
    print("Your Grade is B")
elif avg>=50 and avg<60:
    print("Your Grade is C")
elif avg>=45 and avg<50:
    print("Your Grade is D")
elif avg>=25 and avg<45:
    print("Your Grade is E")
elif avg<25:
    print("Your Grade is F")
else:
    print("Invalid Input!")