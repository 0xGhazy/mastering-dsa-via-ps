import java.util.HashMap;

class Solution {
    public String restoreString(String s, int[] indices) {
		String result = "";
		HashMap<Integer, Character> myMap = new HashMap<>();
		for(int i = 0; i < indices.length ; i++){
			myMap.put(indices[i], s.charAt(i));
		}

		for(int i = 0; i < indices.length; i++){
			result += myMap.get(i);
		}
		return result;
    }
}