class Solution {
    public String firstPalindrome(String[] words) {
		for(int i = 0; i < words.length; i++){
			if(isPalindrome(words[i]))
				return words[i];
		}
		return "";
    }

	public boolean isPalindrome(String word){
		String reversedWord = "";
		for(int i = word.length()-1; i >= 0; i--)
			reversedWord += word.charAt(i);
		if(reversedWord.equals(word))
			return true;
		return false;
	}
}