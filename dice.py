#This program aims to throw a dice and the user has to guess the number

#To Do:
# -Menu (play, view log, delete log, change user, difficulty, activate advises)
# -Read log lastlines maybe(?)
# -Multiuser implementation with stadistics stored in files
#   Ability to change user in a season, store what user is playing in log
#   One .txt per user that stores statistics
#   Create users
# -Difficulty (changing tries) implementation in function of the size of the dice
# -Give advise (warm, cold)

import random, time, datetime, os

#--------------FUNCTIONS--------------#

#Generates a random integer
def generate_random_integer(b):
    n = random.randint(1, int(b))
    return n

#Play again query
def play_again_query():
    while True: #Checking if input was either 'y' or 'n'
        response = input("Wanna play again? (y/n): ")
        valid_responses = ['y', 'n'] #Valid responses for this function
        valid_response = check_valid_response(response, valid_responses) #Call to check valid response
        if valid_response == True:
            break
    return response

#Check valid response
def check_valid_response(response, valid_responses):
    for i in range(0, len(valid_responses)): #Checking all valid responses
        if response != valid_responses[i]: #[i] is not a match in the list
            valid_response = False
        else:
            valid_response = True
            break
    if valid_response == False:
        print("Not a valid response!")
    return valid_response

#Write_file
def write_file(data, file):
    try:
        log = open(file, 'x') #Create file if doesn't exist
    except OSError:
        log = open(file, 'a') #Append mode if file exists
    log.write("%s\n" % data)
    log.close()
    return

#Main game function
def game(tries):
    while True: #Running forever until user don't want to play :(
        print("\nRemember the size of the dice must be %d or over" %int(tries))
        while True: #Checking if input was an integer greater than 1
            try:
                b = input("Select the maximum number of the dice: ")
                if int(b) >= 1:
                    if int(b) >= int(tries):
                        break
                    print("\nWarning! The size of the dice must be over %d" %int(tries))
            except ValueError:
                print("Attention! You need to print a number from 1 to infinite")
                
        loop_count = 1
        n = generate_random_integer(int(b)) #Generating random number
        valid_responses = [] 
        for i in range(0, int(b)): #Storing valid responses in list
            valid_responses.insert(len(valid_responses), i+1)    

        valid_responses_string = []
        for i in range(0, len(valid_responses)): #Converting to string for comparing in check_valid_response string
            valid_responses_string.append(str(valid_responses[i]))
    
        while loop_count <= int(tries): #Loop for different tries
            print("\nThis is your %d try:" % loop_count)
            probability = 100*loop_count/int(b)
        
            while True: #Checking if input is in range until it is
                decision = input("Your guess is ")
                valid_response = check_valid_response(decision, valid_responses_string)
                if valid_response == True:
                    break
                else:
                    print("Input was out of range! Write a number from 1 to %d. Try again!\n" % int(b))

            if(n == int(decision)): #Good guess
                print("\nCongratulations! You guessed the correct number although the probability was %.2f percent\n" % probability)
                break
            else: #Bad guess
                if loop_count == tries: #No more tries, exits while loop
                    print("Game over!\n")
                    break
                else: #Increasing tries counter
                    print("I'm sorry, try again!")
                    loop_count = loop_count + 1
        response = play_again_query() #Asking for another game
        if response == 'n':
            break #Doesn't want to play anymore :(
    return

#--------------END OF FUNCTIONS--------------#

#Script starts executing here
start = datetime.datetime.now().replace(microsecond=0) #Current time
tries = 3 #Number of tries (basic difficulty is 3 tries)
message_to_write = "[Login] %s\nTries set to %d as default" % (time.strftime("%A, %d %B %Y at %H:%M:%S"), tries)
file = 'D:\Python\Dice\log.txt'
print(message_to_write)
write_file(message_to_write, file)

menu = True
while menu == True: #Loop menu
    print("\n-------MENU-------\n1. Start the game!\n2. View log\n3. Delete log (needs to restart)\n4. Change difficulty\n5. Exit\n")
    valid_responses = ['1', '2', '3', '4', '5']
    valid_response = False
    while valid_response == False: #Checking valid response
        c = input("Select one option: ")
        valid_response = check_valid_response(c, valid_responses)
        if valid_response == True:
            #print("It's valid!")
            break

    if(c == '1'):
        print("\nStarting the game...\n")
        print("Number of tries: %d" % int(tries))
        game(tries)
    elif(c == '2'):
        print("\nOpening log.txt...\n")
        log = open('D:\Python\Dice\log.txt', 'r')
        for line in log: #Printing file
            print(line, end='')
        log.close()
    elif(c == '3'):
        print("\nDeleting log.txt")
        os.remove('log.txt')
        print("Deleted.\nExiting...")
        exit()
    elif(c == '4'):#Change difficulty (tries)
        while True: #Checking valid response
            try:
                tries = input("\nHow many tries do you want? ")
                if int(tries) >= 1:
                    print("Tries set to %d" % int(tries))
                    message_to_write = "Tries set to %d at %s" % (int(tries), time.strftime("%H:%M:%S"))
                    file = 'D:\Python\Dice\log.txt'
                    write_file(message_to_write, file)
                    break
            except ValueError:
                print("Attention! You need to print a number from 1 to infinite")
            
    elif(c == '5'): #Bye bye
        print("\nSee you buddy!\n")
        end = datetime.datetime.now().replace(microsecond=0)
        message_to_write = "[Logout] %s\nSeason lasted %s\n" % (time.strftime("%A, %d %B %Y at %H:%M:%S"), end-start)
        file = 'D:\Python\Dice\log.txt'
        print(message_to_write)
        write_file(message_to_write, file)
        exit()
