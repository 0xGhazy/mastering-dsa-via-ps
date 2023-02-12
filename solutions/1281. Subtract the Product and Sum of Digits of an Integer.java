class Solution {
    public int subtractProductAndSum(int n) {
        String numbers = "" + n;
		int[] numsArray = new int[numbers.length()];
		int product = 1;
		int summation = 0;
		for(int i = 0; i < numbers.length(); i++){
			int x = Integer.parseInt(String.valueOf(numbers.charAt(i)));
			product *= x;
			summation += x;
		}

		return product - summation;
    }
}