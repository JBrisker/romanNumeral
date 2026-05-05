#create roman numerals


numeral=''
try:
    value=input("Enter a value 1-10: ")
    if value.isnumeric():
        value =int(value)
except Exception:
    if not value.isnumeric():
       print("ERROR ENTER A NUMBER")
    value=input("Enter a value 1-10 ")

     
else: 
    while value < 1 or value > 10:
        print("The range is 1-10")
        value=int(input("Enter a number 1-10 "))

    if value == 10:
     numeral += "X"

    elif value == 9:
        numeral = "IX"

    elif value % 5 == 0:
        numeral += "V"

    elif value > 5:
     numeral += "V"
     for num in range(value - 5):
        numeral += "I"

    elif value == 4:
        numeral ="IV"
    else:
     val = value
     while val > 0:
        numeral += "I"
        val -= 1 

print(f"the roman numeral of {value} is: {numeral}")
    

        



    
