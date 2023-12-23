import java.util.ArrayList;

class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i = 0; i < words.length; i++)
        {
            for(int j = 0; j < words[i].length(); j++)
            {
                if(words[i].charAt(j) == x)
                {
                    result.add(i);
                    break;
                }
            }
        }
        return result;
    }
}
