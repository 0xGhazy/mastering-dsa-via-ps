class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        tested_devices = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                tested_devices += 1
                j = i+1
                while j < len(batteryPercentages):
                    batteryPercentages[j] = max(batteryPercentages[j]-1, 0)
                    j += 1
        return tested_devices



x = Solution()
if x.countTestedDevices(batteryPercentages = [1,1,2,1,3]) == 3: print("Passed 1")
if x.countTestedDevices(batteryPercentages = [0,1,2]) == 2: print("Passed 2")
if x.countTestedDevices(batteryPercentages = [2,1]) == 1: print("Passed 3")