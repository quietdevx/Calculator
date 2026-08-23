print("--------------------\nCalculator\n--------------------")
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input")
        continue
    

def calculate():
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  operation = input("Enter operation: ")

  if operation == "1":
      print(num1 + num2)

  elif operation == "2":
      print(num1 - num2)

  elif operation == "3":
      print(num1 * num2)

  elif operation == "4":
    try:
      print(num1 / num2)
    except ZeroDivisionError:
      print("Cannot divide by zero")
      close()
  else:
      print("Invalid operation")
      close()




def close():
    print("Do you want to calculate again? (Y/N)")
    choice = input("").strip().upper()
    if choice == "Y":
        calculate()
    elif choice == "N":
        print("Goodbye!")
        exit()
    else:
        print("Please enter Y or N")
        close()


calculate()


