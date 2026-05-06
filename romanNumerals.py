#create roman numerals

def userInput():
    while True:
        value=input("Enter a value 1-10: ")
        if not value =='':
            try:
                    value.isnumeric()
                    value = int(value)
                    if value < 1 or value > 10:
                        print("ERROR: Value out of range ")
                        continue
                    else:
                        conversion(value)
                        break
            
            except Exception:
                if not value.isnumeric():
                    print("ERROR: Enter a number")
                continue
        else:
                print("Please enter a value")
                continue

def conversion(value):
    numeral=''
    if value == 10:
            numeral += "X"
            

    elif value == 9:
            numeral = "IX"
            
    elif value > 5:
            numeral += "V"
            for num in range(value - 5):
                numeral += "I"

    elif value % 5 == 0:
                numeral += "V"           

    elif value == 4:
            numeral ="IV"
            

    elif value < 4 :
                val = value
                for v in range(value):
                    numeral +="I"
    
                

    print(f"the roman numeral of {value} is: {numeral}")

userInput()   

            



        