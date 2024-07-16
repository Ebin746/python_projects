import random
def guess(x):
    randomNumber=random.randint(1,x)
    guess=0
    while guess!=randomNumber:
     guess=int(input(f"genarete a random number between 0 and {x}:"))
     if guess<randomNumber:
        print("it is too small")
     elif guess>randomNumber:
        print("it is too high")
    print(f"you found it Right:{guess}")


def computer_guess(x):
   low=1
   high=x


   randonNumber=int(input(f"enter the a number betwwen 0 and {x} :"))
   feedback=''
   while feedback!='c' :
    if low ==high :
      return print(f"sure it is {low}")
    guess=random.randint(low,high) 
    feedback=input(f" is it :{guess}:")
    if guess>randonNumber:
       high=guess-1
    elif guess<randonNumber:
     low=guess+1
   print(f"Yeah ,I found it {guess}")
computer_guess(10)