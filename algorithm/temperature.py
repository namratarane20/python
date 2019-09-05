#this program is  convert the temperature from celsius to fahrenheit or fahrenheit to celsius


from util import utility
try:
    temperature_value=int(input("to convert the temperature from Celsius to Fahrenheit press 1\n"
                                "to convert the temperature from Fahrenheit to Celsius press 2:  "))

    if temperature_value == 1:                                        # condition check
        value = int(input("enter the temperature in celsius "))
        utility.fahreheit(value)                    # calls the method
    elif temperature_value == 2:                                      # condition check
        value = int(input("enter the temperature in fahrenheit "))
        utility.celsius(value)                      # calls the method

    else:
        print("enter between 1 and 2")
except ValueError:
    print("Input only accepts decimal numbers")