import java.util.Arrays;

class Solution {
    public int arraySign(int[] nums) {
		Arrays.sort(nums);
		int negCount = 0;
		for(int num: nums){
			if(num < 0)
				negCount++;
			else if(num == 0)
				return 0;
			else
				break;
		}
		
		if(negCount % 2 == 0){
			return 1;
		}
		return -1;
    }

}