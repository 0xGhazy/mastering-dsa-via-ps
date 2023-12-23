import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> res = new HashMap<>();
        for (String wo : strs) {
            char tempArray[] = wo.toCharArray();
            Arrays.sort(tempArray);
            String newWord = new String(tempArray);
            if (res.get(newWord) == null) {
                res.put(newWord, new ArrayList<>(Collections.singleton(wo)));
            } else {
                ArrayList<String> tempRes = res.get(newWord);
                tempRes.add(wo);
            }
        }
        ArrayList<List<String>> result = new ArrayList<>();
        for (String key : res.keySet()) {
            result.add(res.get(key));
        }
        return result;
    }
}