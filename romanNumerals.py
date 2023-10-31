#create roman numerals

val=input("Enter a value 1-10: ")

while not val.isnumeric():
    print("ERROR ENTER A NUMBER")
    val=input("Enter a value 1-10 ")
val=int(val)       
while val<1 or val>10:
    print("The range is 1-10")
    val=int(input("Enter a number 1-10 "))
    
if val==10:
    print(f"the roman numeral of {val} is: X")
elif val==9:
    print(f"the roman numeral of {val} is: IX")
elif val==8:
    print(f"the roman numeral of {val} is: VII")
elif val==7:
    print(f"the roman numeral of {val} is: VII")
elif val==6:
    print(f"the roman numeral of {val} is: VI")
elif val==5:
    print(f"the roman numeral of {val} is: V")
elif val==4:
    print(f"the roman numeral of {val} is: IV")
elif val==3:
    print(f"the roman numeral of {val} is: III")
elif val==2:
    print(f"the roman numeral of {val} is: II")
elif val==1:
    print(f"the roman numeral of {val} is: I")


    
