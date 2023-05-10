"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

class FindUnique:
    """
    This class create object that consist of list with alone element and many pair of numbers
    """
    def __init__(self, lst: list[int]) -> None:
        self.lst = lst
        
    def find_only_one(self) -> int:
        """
        This function finds alone element end return it
        """
        unique = set(self.lst)
        for number in unique:
            if self.lst.count(number) == 1:
                return number
            

# create class instances
example_1 = FindUnique([2, 2, 1])
example_2 = FindUnique([4, 1, 2, 1, 2])
example_3 = FindUnique([1])

# return alone number
response_1 = example_1.find_only_one()
response_2 = example_2.find_only_one()
response_3 = example_3.find_only_one()

# print alone number
print(response_1)
print(response_2)
print(response_3)
