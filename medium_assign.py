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