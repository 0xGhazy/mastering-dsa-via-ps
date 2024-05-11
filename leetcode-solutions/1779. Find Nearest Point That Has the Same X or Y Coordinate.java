class Solution {
	public int nearestValidPoint(int x, int y, int[][] points) {
		int smallestIndex = 0;
		int distance = Integer.MAX_VALUE;
		for(int i = 0; i < points.length; i++){
			if(points[i][0] == x || points[i][1] == y) {
				if(calcManhattanDistance(x, y, points[i]) < distance){
					distance = calcManhattanDistance(x, y, points[i]);
					smallestIndex = i;
				}
			}
		}
		if(distance != Integer.MAX_VALUE){
			return smallestIndex;
		}
		return -1;
	}

	public int calcManhattanDistance(int x, int y, int[] p2){
		return Math.abs(x - p2[0]) + Math.abs(y - p2[1]);
	}
}