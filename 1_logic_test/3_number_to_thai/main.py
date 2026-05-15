"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0 :
            return "number can not less than 0"

        if number == 0:
            return "ศูนย์"

        nums = ["","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]      

        units = ["","สิบ","ร้อย","พัน","หมื่น","แสน","ล้าน"]    

        result = ""
        num_str = str(number)
        length = len(num_str)

        for i in range(length):
            digit = int(num_str[i])

            if digit == 0:
                continue    

            pos = length-i-1

            if pos == 1:
                if digit ==1:
                    result += "สิบ"
                elif digit == 2:
                        result +="ยี่สิบ"
                else:
                    result += nums[digit] + "สิบ"

            elif pos == 0:
                if digit ==1 and length > 1:
                    result += "เอ็ด"
                else:
                    result += nums[digit]    
            else:
                result += nums[digit] + units[pos]   

        return result

sol = Solution()
print(sol.number_to_thai(101))        