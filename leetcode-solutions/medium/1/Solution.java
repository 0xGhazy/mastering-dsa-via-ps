class Solution {
	public static int[] twoSum(int[] nums, int target) {
		int[] result = new int[2];
		for (int i = 0; i < nums.length; i++) {
			int searchTarget = target - nums[i];
			for (int j = i + 1; j < nums.length; j++) {
				if (nums[j] == searchTarget) {
					result[0] = j;
					result[1] = i;
				}
			}
		}
		return result;
	}

	/* O(N^2) Solution ==> Beats 38.51% */
	// public static int[] twoSum(int[] nums, int target) {
	// int[] result = new int[2];
	// for(int i = 0; i < nums.length; i++){
	// for(int j = i+1; j < nums.length; j++){
	// if(nums[i] + nums[j] == target){
	// result[0] = j;
	// result[1] = i;
	// break;
	// }
	// }
	// }
	// return result;
	// }
}