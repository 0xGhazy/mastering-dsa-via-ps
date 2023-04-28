class Solution:

    def Bulky(self, dimensions):
        dimensions_trigger = len([x for x in dimensions if x >= 10**4]) > 0
        volume = dimensions[0] * dimensions[1] * dimensions[2] >= 10**9
        return dimensions_trigger or volume

    def Heavy(self, mass):
        return mass >= 100

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_Bulky = self.Bulky([length, width, height])
        is_Heavy = self.Heavy(mass)
        if is_Heavy and is_Bulky :
            return "Both"
        elif not is_Bulky and not is_Heavy:
            return "Neither"
        elif is_Bulky and not is_Heavy:
            return "Bulky"
        else:
            return "Heavy"



x = Solution()
print(x.categorizeBox(length = 200, width = 50, height = 800, mass = 50))

# Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.

# The box is "Bulky" if:
# Any of the dimensions of the box is greater or equal to 104.
# Or, the volume of the box is greater or equal to 109.
# If the mass of the box is greater or equal to 100, it is "Heavy".
# If the box is both "Bulky" and "Heavy", then its category is "Both".
# If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
# If the box is "Bulky" but not "Heavy", then its category is "Bulky".
# If the box is "Heavy" but not "Bulky", then its category is "Heavy".
# Note that the volume of the box is the product of its length, width and height.