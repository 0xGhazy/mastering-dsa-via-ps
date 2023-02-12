// URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits
class Solution {
    public int findNumbers(int[] nums) {
        int counter = 0;
        for (int i = 0; i< nums.length; i++){
            String temp = Integer.toString(nums[i]);
            if (temp.length() % 2 == 0){
                counter += 1;
            }
        }
        return counter;
    }
}
