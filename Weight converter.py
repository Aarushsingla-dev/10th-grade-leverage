weight=float(input("Enter your weight "))
x=input("Is this is (L)bs or (K)gs? [write L for pounds and K for kilograms] ")
if x.upper()=='L':
    print(f"Your weight in (K)gs is {weight/2.205}")
elif x.upper()=='K':
    print(f"Your weight in (L)bs is {weight*2.205}")
else:
    print("ERROR")