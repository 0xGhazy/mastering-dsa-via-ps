class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, (len(nums) // 2)):
            alice_pick = min(nums)
            nums.remove(alice_pick)
            bob_pick = min(nums)
            nums.remove(bob_pick)
            result.append(bob_pick)
            result.append(alice_pick)
        return result
        