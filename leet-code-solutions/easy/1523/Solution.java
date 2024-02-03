class Solution {
    public int countOdds(int low, int high) {
        int diff = high - low;
        int numbersCount = diff/2;
        if(low % 2 != 0 || high %2 != 0)
            numbersCount += 1;
        return numbersCount;
    }
}