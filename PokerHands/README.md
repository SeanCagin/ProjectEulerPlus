# Poker Hands
## Purpose
The goal of this project is to determine the winner between two poker hands. It is a solution to the following ProjectEuler+ problem: https://www.hackerrank.com/contests/projecteuler/challenges/euler054/

## Input Format
A number N is entered to indicate the number of test cases followed by N lines of two hands.
T stands for 10. This is done to ensure each card is made up of 2 characters.<br>
The following input is the example on ProjectEuler+:<br>
<pre>
5
5H 5C 6S 7S KD 2C 3S 8S 8D TD
5D 8C 9S JS AC 2C 5C 7D 8S QH
2D 9C AS AH AC 3D 6D 7D TD QD
4D 6S 9H QH QC 3D 6D 7H QD QS
2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
</pre>
In this case, Player 2 wins the first hand since she has a pair of 8's whereas Player 1 has a pair of 5's.

## Output Format
N lines where each line states who won.<br>
For example, the input example above will have the following output:
<pre>
Player 2
Player 1
Player 2
Player 1
Player 1
</pre>
## How the Program Works
High Card = 0<br>
Single Pair = 1<br>
Double Pair = 2<br>
Three of a Kind = 3<br>
Straight = 4<br>
Flush = 5<br>
Full House = 6<br>
Four of a Kind = 7<br>
Straight Flush = 8<br>

Each character pair (e.g. 5H) is converted to a Card object which has a suit and a value field.<br>
5 cards are stored in a hand array in the Poker_Hand class. Then two Poker_Hand objects are compared.<br>
When doing the comparison, the array of cards is converted to a special type of array we call the equivalent array.<br>
In the equivalent array, first the value of the overall hand is stored (see values above). <br>
Afterwards, the values of the cards are stored from most important to least important. Lastly, these arrays compared from front to back.<br>
Thus, the 0th index is the most important, 1st index second most important, 2nd index third most important, and so on.<br>

Here is a quick example:
<pre>
1
2D 2C 2S JS JC 3C 3S 5D 5S 5H
Player 2
</pre>
Here, Player 2 has a full house with three 3's and two 5's, whereas Player 1 has a full house with three 2's and two J's.<br>
Player 1 equivalent array = [6, 2, J]<br>
Player 2 equivalent array = [6, 3, 5]<br>
Notice how we first compare the 0th index and since they are equal we move to the 1st index.<br><br>

Another example would be:
<pre>
1
2D 2C 2S JS JC 2H 3H 4H 5H 6H
Player 2
</pre>

Player 1 has the same full house from earlier. Player 2 has a straight flush.<br>
Player 1 equivalent array = [6, 2, J]<br>
Player 2 equivalent array = [8, 6]<br>
When we compare these two, Player 2 wins because 8 > 6 which is the index with the highest priority.<br>

## Potential Pitfalls

An important thing to look out for is the wheel straight. This is a straight of the following form:<br>
AC 2H 3D 4C 5H<br>
Typically A is a high card but here it is a low card so the equivalent array of this is [4, 5] rather than [4, A].
The array [4, A] would represent TH JC QS KH AS (suits subject to change) which is wrong. 
