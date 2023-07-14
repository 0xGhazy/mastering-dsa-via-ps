class Solution {
    public void sortColors(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        int p = 0;
        while (p <= end) {
            if (nums[p] == 0) {
                // swap here
                swap(nums, p, start);
                start++;
                p++;
            } else if (nums[p] == 1) {
                p++;
            } else {
                swap(nums, p, end);
                end--;
            }
        }
    }

    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}