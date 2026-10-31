print("The number is between 1 to 10")
a=9
i=1
while i<=3:
    c=int(input("Guess:"))
    if c==a:
        print("You WIN!")
        i=i+10
    i+=1    
if i==4:
    print("You couldn't guess, you lose")


    




