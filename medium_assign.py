'''

Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 

=================


1. compute_number_of_occurences(file_name) --> 50% 
Read the file large_sample.txt, and create dictionary of words where the key is the word, and value is the number of occurences of it. 
Your function should output three parameters: word_dictionary and longest_word and no_of_unique_words

------------------------------------------------

2. word_list_game(file_name) & get_leader_board() --> 50%
 
Write a function to create a game that reads the word_list.csv file. 
Based on this create a game where the users are meant to guess the meaning of a word. 
For each turn, display 4 meanings as 4 options, where one is the correct meaning of the word. 
Get input of the option from user, and see if the user got the meaning right. 
Each option entered is to be considered as a "try" by the user. 
A try is successfull if user guesses meaning correctly, and try is mistake otherwise. 
End the game when the user gets 3 mistakes.  

Create a file leaderboard.csv where you maintain the name and successful tries by each user. 
Write a function get_leader_board() which displays the top scorers sorted by score in following fashion:
Rank | Name | Score
1 | John | 10
2 | Jane | 8

'''

1
import string

def strip_text(file_name):
    text = file_name.read()
    words = text.split()
    words = text.split("--")
    words = text.split(",")
    table = str.maketrans("", "", string.punctuation)
    inter_reader = [w.translate(table) for w in words]
    return inter_reader

def compute_number_of_occurences(file_name):
    inter_reader = strip_text(file_name)

    word_dictionary = dict()

    for line in inter_reader:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in word_dictionary:
                word_dictionary[word] = word_dictionary[word] +1 
            else:
                word_dictionary[word] = 1 

    for key in list(word_dictionary.keys()):
        print(key, ":", word_dictionary[key])

    longest_word = ''  
    longest_size = 0   
    for word in word_dictionary:    
        if (len(word) > longest_size):
            longest_word = word
            longest_size = len(word)
    print(longest_word)

    no_of_unique_words = len(word_dictionary)
    

    return f"The full dictionary is :{word_dictionary}, The longest word is {longest_word}. The number of unique words is {no_of_unique_words}"
    

if __name__ == "__main__":

    input_file = open('large_sample.txt','r')
    dictionary = compute_number_of_occurences(input_file)
    print(dictionary)




import random 
import csv 

def word_list_game(file_name):
    csv_fd = open(file_name, 'r')
    csv_reader = csv.reader(csv_fd) # opens and reads file, make it into a string

    player_name = input("Enter name: ") #new name 
    list_of_words = []
    definition_list = []
    for row in csv_reader:
        if row[0] != 'WORD': #word is column, if the row of 0 doesnt = word, means it isnt the first row 
            list_of_words.append(row[0]) # append the value from the file to a new list (all the words)
            definition_list.append(row[1]) # append the definitions (column 2) 
    
    game = "" # initialize the variables, game is = to an empty string right now 
    wrong_try = 0
    successful_try = 0

    while game != 'over': #while the game isn't over 
        guess_key = random.randint(0,len(list_of_words)) #random word from list 
        guess_word = list_of_words[guess_key] #the definition of that random word 
        print(f"The definition of {guess_word} is : ") 
        print()
        letters = ['A', 'B', 'C', 'D']
        correct_alpha = random.randint(0,3)


        for i in range(4):
            if i == correct_alpha: 
                print(f"{letters[correct_alpha]} {definition_list[guess_key]}")
            else:

                rand_def = random.randint(0,len(list_of_words) - 1)
                while rand_def == guess_key:
                    rand_def = random.randint(0,len(list_of_words) - 1)
                print(f"{letters[i]} {definition_list[rand_def]}")
            
            

        guess = input("Which is the correct definition? (A,B,C,D): ")
        guess = guess.upper() #upper cases 

        print()

        if not guess in 'ABCD':
            print("That is simply not an option :)")
        

        if guess != letters[correct_alpha]: #index out of range only when guess != correct alpha
            wrong_try += 1 
            if wrong_try != 3:
                print(f"Not right, but you still have {3 - wrong_try} tries left before the game is absolutely over.")
            if wrong_try == 3:
                print("Game is over, sorry. ")
                game = 'over'
        else: 
            successful_try += 1 
            print("Yes.")
            

    csv_fd.close()
    leader_fd_append = open('leaderboard.csv', 'a')
    csv_writer = csv.writer(leader_fd_append)
    leader_fd_read = open('leaderboard.csv', 'r')
    csv_reader = csv.reader(leader_fd_read)
    if len(list(csv_reader)) == 0:
        csv_writer.writerow(["Player", "Score"])
    
    csv_writer.writerow([player_name, successful_try])

    leader_fd_append.close() 
    leader_fd_read.close()

def get_leader_board():
    leader_fd = open('leaderboard.csv', 'r')
    csv_reader = csv.reader(leader_fd)

    for row in csv_reader: #writing new rows
        print(row[0], " | ", row[1])


if __name__ == "__main__":
    word_list_game("word_list.csv")
    get_leader_board()

     



    


