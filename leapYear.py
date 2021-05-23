#prompt
# msg = "Please enter a integer to check if it is a leap year: "
# print(msg)

#store input
# input_data = input()
# input_data = int(input_data)

yes = "is a leap year!"
no = "is not a leap year!"
#looping for verification
def checkLeapYear(input_data):
    if (input_data % 4 == 0):
        if(input_data % 100 == 0):
            if(input_data % 400 == 0):
                #print(input_data,yes)
                return True
            else:
                #print(input_data,no)
                return False
        else:
            #print(input_data,yes)
            return True
    else:
        #print(input_data,no)
        return False


