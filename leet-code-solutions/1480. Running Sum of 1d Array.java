class Solution {
	public int[] runningSum(int[] nums) {
		// int[] runningSum = new int[nums.length];
		// for(int i = 0; i < nums.length; i++){
		// 	int sum = 0;
		// 	for(int j = 0; j <= i; j++){
		// 		sum += nums[j];
		// 	}
		// 	runningSum[i] = sum;
		// }
		// return  runningSum;
        int[] result = new int[nums.length];
		int sum = nums[0];
        result[0] = sum;
		for(int i = 0; i < nums.length - 1; i++){
			sum += nums[i+1];
			result[i+1] = sum;
		}
		result[nums.length-1] = sum;
		return result;
	}

}