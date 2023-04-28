class Solution:

    def decodeMessage(self, key: str, message: str) -> str:
        key_map = {" ": " "}
        english_letters = "abcdefghijklmnopqrstuvwxyz"
        counter = 0
        result = ""
        # prepare the key map
        for i in key:
            if i not in key_map:
                key_map[i] = english_letters[counter]
                counter += 1
        
        for i in message:
            result += key_map[i]
        return result




if __name__ == "__main__":
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    x = Solution()
    print(x.decodeMessage(key, message))