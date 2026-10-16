class Solution:
    def reverse(self, x: int) -> int:
        # Return x after reversing each of its digits. 
        # If x goes outside the 32-bit integer range [-2^31, 2^31 - 1], then return 0
        # Solve the problem without using integers that are outside the signed 32-bit integer range

        if x == 0:
            return 0

        num = abs(x)
        power = math.floor(math.log(num, 10))

        reverse = 10**power
        extract = 10
        place = 1
        res = 0
        
        minimum = (-2)**31
        maximum = (2**31) - 1

        while num > 0:
            digit = (num % extract)
            res += digit * reverse
            num -= digit
            print(f"digit: {digit}, res: {res}, num: {num}")
            place *= 10
            extract *= 10
            reverse /= 100
            print(f"place: {place}, extract: {extract}, reverse: {reverse}")
            if res < minimum or res > maximum:
                return 0
        
        # return the neg
        if x < 0:
            res *= -1
        
        return int(res)        



