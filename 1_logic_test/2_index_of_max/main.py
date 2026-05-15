"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if len(numbers) == 0 :
            return "list can not blank"
        
        max_index = 0 

        for i in range(1,len(numbers)):
            if numbers[i] > numbers[max_index]:
                max_index = i 
        return max_index        


sol = Solution()
print(sol.find_max_index([1,9,3,4,5]))
