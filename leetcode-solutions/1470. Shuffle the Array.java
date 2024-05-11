class Solution {
	public int[] shuffle(int[] nums, int n) {
		int[] result = new int[nums.length];
		int start = 0;
		int middle = n;
		int round = 0;
		for(int i = 0; i < nums.length; i++){
			if(round % 2 == 0){
				result[i] = nums[start];
				start++;
			}else{
				result[i] = nums[middle];
				middle++;
			}
			round++;
		}
		return result;
	}

}