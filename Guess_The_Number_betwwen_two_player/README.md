<h1>Guess The Number Between Two Player</h1>

<h2>Problem Statement:</h2>

Generate a random integer from a to b. You and your friend have to guess a number between two numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number, and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game, and then the person with the minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.
<br>
Input:
<br>
Enter the value of a : 4
<br>
Enter the value of b: 13
<br>
Output:
<br>
Player1 :
<br>
Please guess the number between 4 and 13: 5
<br>
Wrong guess a greater number again
<br>
8
<br>
Wrong guess a smaller number again
<br>
6
<br>
Correct, you took 3 trials to guess the number
<br>
Player 2:
<br>
Correct, you took 7 trials to guess the number
<br>
Player 1 wins!
 
<h2>Description:</h2>

First of all, import random library and create two variables to store the input for fixing the range between two number. Then, also create two variable to store the integer value between two number using random library for different player. Then, define a function which take three parameter i.e. first two is range between two number and last one is store integer for guessing this number. And, while loop is used and if else statement is used inside while loop and return number of chance player take to guess the number. Then, while is used again and function is pass for two player and if else statement is used to find who is winner or may tie.

This program create a variable to store number generated by randomint function between 1 and 100, used for loop for 9 chance to play this game and take input as integer number. If your guess is correct, it will return you win and number of chance you take to guess this number. If your guess number is not match (if your guess number is larger than that number, it will return your guess number is greater than number so choose guess number smaller number. If your guess number is smaller than that number, it will return your guess number is smaller than number so choose guess number greater number). And, also continue and print your chance left. If number of chance is zero, it print game over.


<h2>Note:</h2>

* You can run this code by downloading or copy it in any plateform which support python.
