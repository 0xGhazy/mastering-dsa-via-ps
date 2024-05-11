class Solution {
    public boolean check(int[] nums) {
        // if array was sorted and rotated the break points will be 1
        // if just only sorted it will be 0
        // otherwise we will return false
        int breakPoints = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > nums[(i + 1) % nums.length])
                breakPoints++;
        }
        if (breakPoints > 1) {
            return false;
        }
        return true;
    }
}