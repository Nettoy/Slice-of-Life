#################################################################################
##  CS 101                                                                     ##
##  Program 3 - Algorithm                                                      ##
##  George McChan                                                              ##
##  gmmg3c@mail.umkc.edu                                                       ##
##                                                                             ##
##  PROBLEM: Develop a program that quizzes the user on random string and      ##
##      slice formations for 3 difficulties. The 'Hard' difficulty will have   ##
##      many more random occurences.                                           ##
##                                                                             ##
##                                                                             ##
##  ALGORITHM:                                                                 ##
##      1. Welcome the user as always!                                         ##
##      2. Ask for input from user for number of rounds to play (1-20).        ##               ##
##          i. In case of incorrect input, warn user and ask again.            ##
##      3. Ask for input from user for level of difficulty (1, 2, 3).          ##
##          i. In case of incorrect input, warn user and ask again.            ##
##                                                                             ##
##      4. Game starts on selected difficulty and number of rounds.            ##
##          i. Program keeps track of correct answers for later use.           ##
##      5. Output to user score gotten correct with %.                         ##
##      6. Ask user if they wish to play again.                                ##
##          i. If yes, go to step 1.                                           ##
##          ii. If no, end program.                                            ##
##                                                                             ##
##                                                                             ##
##  ERROR HANDLING:                                                            ##
##      1. Incorrect inputs from user, (number of rounds, difficulty,          ##
##          incorrect input when asked to play again), dealt with by telling   ##
##          user to enter a correct input and asking again.                    ##
##                                                                             ##
#################################################################################

    #Obvious importing is obvious#
import random
import string

    #Set up names for later use in program#
truefalse        = 0    #Easy true/false statement for loops#
game_state       = 0    #Game state for difficulty#
number_of_rounds = 0    #Name placeholder for rounds#
correct_answer   = 0    #Tracks correct answers during game#
game_end         = 0    #Placeholder for end of game#
game_restart     = 0    #Placeholder for game restart#

    #Start of program, basic introduction#
print("Hello! Welcome to 'Slice of Life'!")

    #Asks user for rounds wished to be played#
print(" ")
while truefalse == 0:
    while truefalse == 0:
        try:    #Try/Except to catch non-integer malicious input#
            number_of_rounds = input("How many rounds would you like to play? (1-20): ")
            print(" ")
            number_of_rounds = int(number_of_rounds)
            if number_of_rounds <= 0 or number_of_rounds >= 21:     #Catches out-of-bounds input#
                print("~~Hey! Put a correct input! 1-20 only!~~")
                print(" ")
            elif number_of_rounds >= 1 and number_of_rounds <= 20:     #Breaks while loop when correct input is entered#
                break
            else:
                print("~~What did you manage to do to get this message? Try again!~~")
                print(" ")
        except ValueError or TypeError:     #Known errors from tested input#
            print("~~Hey! That's not a number! Enter 1-20 only!~~")
            print(" ")

        #Asks user for game difficulty#
    while truefalse == 0:
        try:    #Try/Except to catch non-integer malicious input#
            game_state = input("What difficulty would you like to play on? (1: Easy, 2: Medium, 3: Hard): ")
            print(" ")
            game_state = int(game_state)
            if game_state <= 0 or game_state >= 4:      #Catches out-of-bounds input#
                print("~~Hey! That's not a difficulty input! Choose 1-3, Easy to Hard!~~")
                print(" ")
            elif game_state >= 1 and game_state <= 3:      #Breaks while loop when correct input is entered#
                break
            else:
                print("~~What did you manage to do to get this message? Try again!~~")
                print(" ")
        except ValueError or TypeError:     #Known errors from tested input#
            print("~~Hey! That's not an accepted input! Choose 1-3, Easy to Hard!~~")
            print(" ")

        #Runs game based on difficulty selected#
    while game_state == 1:
        while game_end == 0:
            print("~~Easy Mode Selected!~~")
            print(" ")

            game_end = 1    #Stops game loop, sends to 'Game Restart' section#

            #'Game Restart' section, handles all input for restarting game#
        while game_end == 1:
            game_restart = input("Would you like to play again? (Y, YES, N, NO): ")
            print(" ")
            game_restart = str.upper(game_restart)
            if game_restart == 'Y' or game_restart == 'YES':
                    
                    #Resets all data for new game#
                truefalse        = 0    
                game_state       = 0    
                number_of_rounds = 0    
                correct_answer   = 0    
                game_end         = 0    
                break
            elif game_restart == 'N' or game_restart == 'NO':
                truefalse        = 1    
                game_state       = 0    
                break
            else:
                print("~~That's not a yes or a no! Stop being silly!~~")
                print(" ")
                
    while game_state == 2:
        while game_end == 0:
            print("~~Medium Mode Selected!~~")
            print(" ")

            game_end = 1    #Stops game loop, sends to 'Game Restart' section#

            #'Game Restart' section, handles all input for restarting game#
        while game_end == 1:
            game_restart = input("Would you like to play again? (Y, YES, N, NO): ")
            print(" ")
            game_restart = str.upper(game_restart)
            if game_restart == 'Y' or game_restart == 'YES':
                    
                    #Resets all data for new game#
                truefalse        = 0    
                game_state       = 0    
                number_of_rounds = 0    
                correct_answer   = 0
                game_end         = 0
                break
            elif game_restart == 'N' or game_restart == 'NO':
                truefalse        = 1    
                game_state       = 0    
                break
            else:
                print("~~That's not a yes or a no! Stop being silly!~~")
                print(" ")

    while game_state == 3:
        while game_end == 0:
            print("~~Hard Mode Selected!~~")
            print(" ")

            game_end = 1    #Stops game loop, sends to 'Game Restart' section#
            
            #'Game Restart' section, handles all input for restarting game#
        while game_end == 1:
            game_restart = input("Would you like to play again? (Y, YES, N, NO): ")
            print(" ")
            game_restart = str.upper(game_restart)
            if game_restart == 'Y' or game_restart == 'YES':
                    
                    #Resets all data for new game#
                truefalse        = 0    
                game_state       = 0    
                number_of_rounds = 0    
                correct_answer   = 0
                game_end         = 0
                break
            elif game_restart == 'N' or game_restart == 'NO':
                truefalse        = 1    
                game_state       = 0    
                break
            else:
                print("~~That's not a yes or a no! Stop being silly!~~")
                print(" ")

