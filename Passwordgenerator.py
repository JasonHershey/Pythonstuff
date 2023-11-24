# Passwordgenerator by Jason Hershey jason@jasonhershey.com
# Inspired by Bagels by Al Sweigart al@inventwithpython.com

# requires random
import random

#Define the character sets that can be used in the password
ALPHA_CHARS = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
NUM_CHARS = list('0123456789')
SPEC_CHARS=list('!@#$%^&*()_[]|?>/<-=+~`,.')

# The main program
def main():
    print('''Password generator.
          By Jason Hershey -- jason@jasonhershey.com
          
          Creates a random password based on characteristics you define''')
    
    while True: # Main program loop.
        searchChars = getPassComplex() # Define the password complexity (which character sets to use)
        passLength = getPassLength() #Get the password length
        passWord = ''.join(genPassword(searchChars, passLength)) # Generate the password
        print('Your generated password is {}'.format(passWord)) # Print it



        # Offer to generate another password
        print('''Do you want to generate another password? (yes or no)''')
        if not input('''> ''').lower().startswith('y'):
            print('Have a nice day')
            break
        

# This function gets the password complexity
def getPassComplex():
    choiceOK = False

    while choiceOK == False:
        print('''Choose which characters you wish to include:
                1 - Only alpha characters (upper and lower case)
                2 - Alpha characters and numbers
                3 - Alpha characters and special characters -- {}
                4 - All of the above'''.format(''.join(SPEC_CHARS)))
        complexChoice = input('''>''')
        match complexChoice:
            case '1':
                PASS_CHARS = ALPHA_CHARS
                choiceOK = True
            case '2':
                PASS_CHARS = ALPHA_CHARS+NUM_CHARS
                choiceOK = True
            case '3':
                PASS_CHARS = ALPHA_CHARS+SPEC_CHARS
                choiceOK = True
            case '4':
                PASS_CHARS = ALPHA_CHARS+NUM_CHARS+SPEC_CHARS
                choiceOK = True
            case 'exit':
                exit()
            case _:
                print('''Input invalid. Please choose a valid option''')
                choiceOK = False
    return PASS_CHARS
            

def getPassLength():
    lengthOK = False
    while lengthOK == False:
        print('''Choose password length.
            Choose a whole number between 8 and 20''')
        passLength = input('''> ''')
        if (8 <= int(passLength) <=20):
            lengthOK= True
            
        else:
            lengthOK = False
    return passLength

def genPassword(passChars, passLength):
    i = 1
    passWord=[]
    while i <= int(passLength):
        random.shuffle(passChars)
        passWord += passChars[1]
        i += 1
    return passWord


# if the program is run and not imorted, run the game:
if __name__ =='__main__':
    main()

    