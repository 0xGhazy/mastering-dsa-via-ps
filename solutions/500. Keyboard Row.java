import java.util.ArrayList;
import java.util.HashMap;

class Solution {
	public String[] findWords(String[] words) {
		String[] FinalResult;
		ArrayList<String> result = new ArrayList<>();
		HashMap<Character, String> myMap = new HashMap<>();
		myMap.put('q', "qwertyuiop");
		myMap.put('w', "qwertyuiop");
		myMap.put('e', "qwertyuiop");
		myMap.put('r', "qwertyuiop");
		myMap.put('t', "qwertyuiop");
		myMap.put('y', "qwertyuiop");
		myMap.put('u', "qwertyuiop");
		myMap.put('i', "qwertyuiop");
		myMap.put('o', "qwertyuiop");
		myMap.put('p', "qwertyuiop");
		myMap.put('a', "asdfghjkl");
		myMap.put('s', "asdfghjkl");
		myMap.put('d', "asdfghjkl");
		myMap.put('f', "asdfghjkl");
		myMap.put('g', "asdfghjkl");
		myMap.put('h', "asdfghjkl");
		myMap.put('j', "asdfghjkl");
		myMap.put('k', "asdfghjkl");
		myMap.put('l', "asdfghjkl");
		myMap.put('z', "zxcvbnm");
		myMap.put('x', "zxcvbnm");
		myMap.put('c', "zxcvbnm");
		myMap.put('v', "zxcvbnm");
		myMap.put('b', "zxcvbnm");
		myMap.put('n', "zxcvbnm");
		myMap.put('m', "zxcvbnm");

		for (String word : words) {
			ArrayList<String> innerArray = new ArrayList<>();
			for (int i = 0; i < word.length(); i++) {
				String row = myMap.get(word.toLowerCase().charAt(i));
				innerArray.add(row);
			}
			if(inSameLine(innerArray))
				result.add(word);
		}
		FinalResult = new String[result.size()];
		for(int i = 0; i < result.size(); i++){
			FinalResult[i] = result.get(i);
		}
		return FinalResult;
	}

	public boolean inSameLine(ArrayList<String> arr){
		int size = arr.size();
		int validWords = 0;
		String fWord = arr.get(0);
		for(String row: arr){
			if( row == fWord)
				validWords++;
		}
		return validWords == size;
	}
}