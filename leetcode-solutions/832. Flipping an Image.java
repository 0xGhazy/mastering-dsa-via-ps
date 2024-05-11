class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
       	int n = image[0].length;
        int[][] resultImage = new int[n][n];

		// Flap the image
		for(int i = 0; i < n; i++){
			int reversedInnerIndex = n -1;
			for(int j = 0; j < n; j++){
				resultImage[i][j] = image[i][reversedInnerIndex];
                reversedInnerIndex--;
			}
		}
		// Invert the image
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(resultImage[i][j] ==	0)
					resultImage[i][j] = 1;
				else
					resultImage[i][j] = 0;
			}
		}
		return resultImage; 
    }
}