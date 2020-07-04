# 957. Prison Cells After N Days

## Solution 1 -- Simulation with Fast Forward

* Time Complexity: O(K*min(N, 2^K)), N is the number of steps and K is the number of cells.

* Space Complexity: O(K*2^K)

## Solution 2 -- Simulation with Bitmap

* Time Complexity: O(min(N, 2^K)), N is the number of steps and K is the number of cells.

* Space Complexity: O(2^K)
