answer=1

guesscount=0
guesslimit=3
print("Given Equation 6x+3x=18, find the value of x")
while guesscount<guesslimit:
   answer2=int(input("Please Enter Your Answer"))
   guesscount+=1
   if answer2==answer:
       print("You Won")
       break
else:
    print("Bruh you actually failed in Maths")








































