import java.util.*;

class Solution {
	public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
		int matchedItems = 0;
		for (List<String> item : items) {
			switch (ruleKey){

				case "type":
					if(item.get(0).equals(ruleValue))
						matchedItems++;
					break;
				case "color":
					if(item.get(1).equals(ruleValue))
						matchedItems++;
					break;
				case "name":
					if(item.get(2).equals(ruleValue))
						matchedItems++;
					break;
			}
		}
		return matchedItems;
	}
}