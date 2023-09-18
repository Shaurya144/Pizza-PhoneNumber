# in this program we ask the customer for their order and their phone number
# we then take their phone number and make sure it is starts with a 0 or +44 followed by ten digits
# Remove the spaces and print back as an international format

import re # regular Expressions

print("Hello and welcome to PizzaPeletons")
userOrder = input("What would you like? ")

while True:
    userPhoneNumber = input("AAnd what is your phone number: ")

    if userPhoneNumber [0] == "0":
        userPhoneNumber == userPhoneNumber[0:]
    elif userPhoneNumber[0, 3] == "+44":
        userPhoneNumber == userPhoneNumber[3:]
    
    userPhoneNumber = int(re.sub(" ", "", userPhoneNumber))

    if len(str(userPhoneNumber)) == 10:
        break
    else:
        print("invalid Phone Number")

print("Great Thanks for That")
userPhoneNumber = ("+44" + str(userPhoneNumber))
print("Hear's you're order : " + userOrder)
print(userPhoneNumber)