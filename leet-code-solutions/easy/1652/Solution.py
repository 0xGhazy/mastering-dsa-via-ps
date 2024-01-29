class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        result = [0] * len(code)
        for idx in range(0, len(code)):
            sum_ = 0
            for i in range(0, abs(k)):
                if k < 0:
                    sum_ += code[(idx + (i*-1) - 1) % len(code)]
                else:
                    sum_ += code[(idx + i + 1) % len(code)]
            result[idx] = sum_
        return result


x = Solution()
code, k, result = [5, 7, 1, 4], 3, [12, 10, 16, 13]
if x.decrypt(code, k) == result:
    print("Passed 1")

code, k, result = [1,2,3,4], 0, [0,0,0,0]
if x.decrypt(code, k) == result:
    print("Passed 2")

code, k, result = [2,4,9,3], -2, [12,5,6,13]
if x.decrypt(code, k) == result:
    print("Passed 3")
