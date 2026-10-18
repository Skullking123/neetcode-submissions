class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)

        # each of the n rolls must be between 1 and 6
        if total < n or total > 6 * n:
            return []

        q, r = divmod(total, n)
        # r rolls get q + 1, the other n - r rolls get q
        return [q + 1] * r + [q] * (n - r)