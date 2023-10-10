# Maximum Path Sums II
## Purpose
The goal of this project is to solve the ProjectEuler+ question: https://www.hackerrank.com/contests/projecteuler/challenges/euler067<br><br>
A Triangle of numbers is given (described in more detail in the input/output sections) and our goal is the find the path with the highest sum
through the triangle.

## Input Format
A number is N is entered for the number of test cases followed by N triangles.<br>
Each Triangle takes a number M for the number of rows followed by M rows.<br>
Here is an example:
<pre>
2
4
3
7 4
2 4 6
8 5 9 3
4
3
7 4
2 4 6
8 5 9 3
</pre>
The first triangle looks like this:
<pre>
            3
          /   \
         7     4
        /   \/   \
       2     4    6
      /   \/   \/   \
     8    5     9    3
</pre>

## Output Format
N lines with the maximum sum for the kth triangle on line k.<br>
The example triangle given in the input section has output 23: 3 + 7 + 4 + 9

## How the Program Works
We will store the whole structure in an array or arrays.<br>
This is a tree-like structure but two nodes can share children<br>
The left child of triangle[i][j] is triangle[i+1][j]<br>
Similarly, the right child of triangle[i][j] is triangle[i+1][j+1]

### Potential Pitfalls
The most intuitive approach is to start from the top of the triangle and go down perhaps using a greedy algorithm in the process.<br>
Here is an extremely simple example showing why this would not work:
<pre>
      1
     / \
    2   1
   /  \/  \
  2    1   1000
</pre>
The larget path is clearly 1 + 1 + 1000 = 1002 but a greedy algorithm would give us 1 + 2 + 2 = 5 << 1002<br>
Another approach is tracing every path and finding the largest one. However, this aproach has time complexity O(2^n)
which is terrible. There is a much cleaner O(n) approach.

### The O(n) Approach
We take advantage of the fact that the children of a node is a smaller version of the same problem.<br>
We start adding from the bottom thus only going each element once, making our algorithm O(n)<br>
Example:
<pre>
              3         ->           3       ->      3     ->    23
            /  \                   /  \            /  \
           7    4                 7    4          20  19
         /   \/  \              /   \/  \
        2    4    6            10   13   15
       /  \/   \/  \
      8   5    9    3
</pre>
This is O(n) because we go over each number once. For example, we see that in the sub-tree 2, 8, 5 the largest path is 2->8 
so we say this subtree has a value of 10 and we never visit it again.