class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # given two strings num1 and num2 that represent non-negative integers
        # Return the product of num1 and num2 in the form of a string

        # You may assume that neither num contain any leading zeros unless they are 0 itself
        # Attempt to solve this with the method taught in school
        # Where you multiply the num1 with each digit of num2 with their corresponding decimal place
        # 123 * 456 = 56,088
        # = 123 * 6 + 123 * 50 + 123 * 400

        # keep num1 as the longest number
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        # multiply num1 with every digit of num2 to get the partial products
        partial_prods = []
        
        for i2 in range(len(num2) - 1, -1, -1):
            # pad with the appropriate amount of 0s
            curr_prod = ["0"] * ((len(num2) - 1) - i2)
            d2 = num2[i2]
            digit2 = int(d2)
            carryOver = 0
            for i1 in range(len(num1) - 1, -1, -1):
                d1 = num1[i1]
                digit1 = int(d1)
                digit_prod = digit1 * digit2 + carryOver
                carryOver = digit_prod // 10
                digit_prod %= 10
                curr_prod.append(str(digit_prod))
            
            if carryOver:
                curr_prod.append(str(carryOver))

            curr_prod.reverse()
            # print(curr_prod)
            curr_prod = "".join(curr_prod)
            partial_prods.append(curr_prod)
        
        partial_prods = [int(x) for x in partial_prods]
        # print(partial_prods)

        return str(sum(partial_prods))
        
