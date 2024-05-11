// URL: https://leetcode.com/problems/container-with-most-water/
class Solution {
    public int maxArea(int[] height) {
        int maxArea = Integer.MIN_VALUE;
        int begain = 0;
        int last = height.length - 1;
        while (begain < last){
            int h = Math.min(height[begain], height[last]);
            int w = last - begain;
            maxArea = Math.max(maxArea, h * w);
            if (height[begain] < height[last]){begain++;}
            else{last--;}
        }
        return maxArea;
    }
}