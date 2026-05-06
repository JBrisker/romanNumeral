#create roman numerals


numeral=''
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
                    break
        
        except Exception:
         if not value.isnumeric():
            print("ERROR: Enter a number")
            continue
    else:
          print("Please enter a value")
          continue

if value == 10:
         numeral += "X"
        

elif value == 9:
         numeral = "IX"
        
elif value > 5 and value < 9:
        numeral += "V"
        for num in range(value - 5):
            numeral += "I"

elif value % 5 == 0:
            numeral += "V"           

elif value == 4:
         numeral ="IV"
         

elif value < 4 :
            val = value
            while val > 0:
                numeral += "I"
                val -= 1 
              

print(f"the roman numeral of {value} is: {numeral}")
    

        



    