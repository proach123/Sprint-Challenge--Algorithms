#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Time Complexity: O(n)
This is because there is only one traversial.

Space Complexity: O(n)
The maximum amount of space used is only one variable worth of memory.

b)

Time Complexity: O(n^2)
Their are two traversials completed in a while loop inside of a for loop.

Space Complexity: O(2n) or O(n)
I put O(2n) for this example becuase there are two values taking up space but this can be simplified to O(n) in reality.



c)

Time Complexity: O(n-1) or O(n)
 Their is only one traversial and that traversial is only happening on a base of how many times bunnies is called. So n in this case is how many times bunnies is called. ie if 4 is called then it will pass through the opperation with an O(n) and return out of the function with another O(n) operation, this time with a decrement amount of "bunnies". Once it hits 0 bunnies it will return the values of how many ears each bunnies have, returning first 2, then 4 and so on until 8 in this example. The complexity of the operation never returns more than one value and even though it is recursing it is no actually more complex of an operation than an O(n).

 Space Complexity: O(n)
 Their is only one value being exchanged around "bunnies" so thier is only a compexity of one in this regardless of the recursion.

## Exercise II
    #sudo code
    # floors = n
    # eggs break if > f floors
    # eggs don't break if < f floors.

    so if the eggs are breaking they are too high of a floor count, if they aren't then they are lower or equal to the threshold of egg breaking floor count.

    simply put this is a sorting algorithm. And we can determine which type of sorting algorithm to make the least amount of steps possible. Since this problem works with only one value giving it a space complexity of O(n) we can use a bineary search to reduce the Time Complexity of the problem to O(log(n)).

    We have the maximum number of floors and the minimum so we can find the middle floor. This logic will be recursed on the condition that their are still floors to traverse. Taking the first middle and checking if the egg breaks. If it does then we set this floor to the new max floor and repeat our check. If the egg does not break then we have a new bottom to resituate our mid point and run the same check. When we finally are on one floor left we will have our answer.

    Time Complexity: O(log(n))
    This is because it is reducing the amount of checks we have to do by a base of two on each check.
    
    Space Complexity: O(n): This is because their is only one value being messed with.

