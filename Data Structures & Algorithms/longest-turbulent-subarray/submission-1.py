class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        if len(arr) <= 1:
            return len(arr)

        # True = curr elm needs to be smaller than prev
        # False = curr elm needs to be bigger than prev
        comp = arr[0] > arr[1]
        # every elm by itself can be a turbulent arr. so bare min is 1
        res = 1

        left = 0
        right = 1
        while right < len(arr) and arr[left] == arr[right]:
            left += 1
            right += 1
        while right < len(arr):
            # continue expanding the subarr
            if (comp and arr[right - 1] > arr[right]) or (not comp and arr[right - 1] < arr[right]):
                comp = not comp
            else:
                left = right - 1
                while right < len(arr) and arr[left] == arr[right]:
                    left += 1
                    right += 1
                
                comp = arr[right - 1] < arr[right] if right < len(arr) else True

            
            res = max(res, right - left + 1)
            right += 1


        return res



