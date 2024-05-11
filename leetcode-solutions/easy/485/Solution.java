class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxOnes = 0;
        int temp = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                temp++;
            }
            if (i == nums.length - 1 || nums[i] != 1) {
                maxOnes = Math.max(maxOnes, temp);
                temp = 0;
            }
        }
        return maxOnes;
    }
}