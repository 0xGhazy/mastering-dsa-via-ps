class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        // calculate the sum of all the numbers in the array. O(1)
        int numsSum = n * (n + 1) / 2;
        for (int i = 0; i < n; i++) {
            // the remaining value of the numsSum is the missing number at the end of the
            // loop.
            numsSum = numsSum - nums[i];
        }
        return numsSum;
    }
}