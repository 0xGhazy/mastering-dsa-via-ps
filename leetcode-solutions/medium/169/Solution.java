class Solution {
    public int majorityElement(int[] nums) {
        int maxPosElement = 0;
        int maxNegElement = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > maxPosElement)
                maxPosElement = nums[i];
            if (nums[i] < maxNegElement)
                maxNegElement = nums[i];
        }

        int[] posArr = new int[maxPosElement + 1];
        int[] negArr = new int[maxNegElement * -1 + 1];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                posArr[nums[i]] += 1;
            } else {
                negArr[nums[i] * -1] += 1;
            }

        }
        int maxPosIndex = getMaxIndex(posArr);
        int maxNegIndex = getMaxIndex(negArr) * -1;
        return Math.max(maxPosIndex, maxNegIndex);
    }

    public int getMaxIndex(int[] arr) {
        int maxCount = 0;
        int maxIndex = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > maxCount) {
                maxCount = arr[i];
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}