class Solution {
	public int[] sort(int arr[])
	{
		int n = arr.length;
		// One by one move boundary of unsorted subarray
		for (int i = 0; i < n-1; i++)
		{
			// Find the minimum element in unsorted array
			int min_idx = i;
			for (int j = i+1; j < n; j++)
				if (arr[j] < arr[min_idx])
					min_idx = j;
			// Swap the found minimum element with the first
			// element
			int temp = arr[min_idx];
			arr[min_idx] = arr[i];
			arr[i] = temp;
		}
		return arr;
	}

	public double average(int[] salary) {
		int[] sortedArray =  sort(salary);
		double runningTotal = 0;
		for(int i = 1; i < salary.length-1 ; i++){
			System.out.println(salary[i]);
			runningTotal += salary[i];
		}
		int arrayLength = salary.length-2;
		return (runningTotal/arrayLength);
	}
}