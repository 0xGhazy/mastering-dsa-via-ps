from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars_table = {"a": ".-","b": "-...","c": "-.-.","d": "-..","e": ".","f": "..-.","g": "--.", "h": "....",
                       "i": "..","j": ".---","k": "-.-","l": ".-..","m": "--","n": "-.","o": "---","p": ".--.",
                       "q": "--.-","r": ".-.","s": "...","t": "-","u": "..-","v": "...-","w": ".--","x": "-..-",
                       "y": "-.--","z": "--.."}
        final_list = []
        for word in words:
            cipher = ""
            for i in word:
                cipher += chars_table[i]
            final_list.append(cipher)
        unique_words = {x for x in (final_list)}
        return len(unique_words)


words = ["a"]
x = Solution()
print(x.uniqueMorseRepresentations(words))
