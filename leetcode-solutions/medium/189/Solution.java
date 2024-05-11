class Solution {
    public void rotate(int[] nums, int k) {
        int[] arr = new int[nums.length];
        for (int j = 0; j < nums.length; j++) {
            arr[(j + k) % nums.length] = nums[j];
        }
        // update the nums
        for (int i = 0; i < nums.length; i++) {
            nums[i] = arr[i];
        }
    }
}