# 153. Find Minimum in Rotated Sorted Array
## Solution 1
The concept is same as solution 2 of problem 33
* Time Complexity: O(logN)
* Space Complexity: O(1)

## Thinking:
1. When do you use `while (start < end)`, whereas when do you use `while (start <= end)`?
    *  Use `while (start < end)` if you want to exit out of the loop first, and then use the result of `start` or `end` to return the match.
    *  Use `while (start <= end)` if you are returning the match from inside the loop (in the edge case of `start == end`, the return statement within the while-loop can still be executed)
2. What's the logic behind knowing why it should be `end = mid` and not `end = mid - 1`?
    * Think of it in general for a binary search, you have an array and you do two steps. First you see if what you're looking at now is the answer. In this case we want to see if start is less than end. Ok now if that's not true then you go on to the second step, which is to divide the array into two parts. From start to mid, and mid + 1 to end. Now you chose which side of the array brings your closer to the solution and go back to step 1.
    
    * The point is, if we do as you say, which is to say `end = mid - 1`, then you are always leaving out an element when you divide the array in half. So therefore you aren't dividing it into two contiguous halves.

    * Here's an example to prove the point.
    ```
    Line 1 [4, 7, 8, 9, 13, 14, 18, 1, 2, 3]
    Line 2 [4, 7, 8, 9, 13] [14, 18, 1, 2, 3]
    Line 3 [14, 18, 1, 2, 3]
    Line 4 [14, 18 , 1]
    Line 5 [18, 1]
    Line 6 [1]
    Line 7 return start (1)
    ```
    * If we had said `end = mid - 1`, then line 4 would have excluded the 1, which is the answer.

