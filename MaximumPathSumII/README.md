We will put the whole structure in an array or arrays.
This is a tree-like structure but two nodes can share children
The left child of triangle[i][j] = triangle[i+1][j]
Similarly, the right child is triangle[i+1][j+1]
We start adding from the bottom thus only going each element once, making our algorithm O(n)
Example:
              3         ->           3       ->      3     ->    23
            /  \                   /  \            /  \
           7    4                 7    4          20  19
         /   \/  \              /   \/  \
        2    4    6            10   13   15
       /  \/   \/  \
      8   5    9    3
