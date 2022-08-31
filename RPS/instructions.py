"""
For this challenge, you will create a program to play Rock, Paper, Scissors. 
A program that picks at random will usually win 50% of the time. 
To pass this challenge your program must play matches against four different bots, winning at least 60% of the games in each match.
You will be working on this project with our Replit starter code.
We are still developing the interactive instructional part of the machine learning curriculum. 
For now, you will have to use other resources to learn how to pass this challenge.
"""

"""
In the file RPS.py you are provided with a function called player. 
The function takes an argument that is a string describing the last move of the opponent ("R", "P", or "S"). 
The function should return a string representing the next move for it to play ("R", "P", or "S").
A player function will receive an empty string as an argument for the first game in a match since there is no previous play.
The file RPS.py shows an example function that you will need to update. 
The example function is defined with two arguments (player(prev_play, opponent_history = [])). 
The function is never called with a second argument so that one is completely optional. 
The reason why the example function contains a second argument (opponent_history = []) is because that is the only way to save state between consecutive calls of the player function. 
You only need the opponent_history argument if you want to keep track of the opponent_history.
Hint: To defeat all four opponents, your program may need to have multiple strategies that change depending on the plays of the opponent.
"""
