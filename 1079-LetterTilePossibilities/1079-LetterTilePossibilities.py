class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        letters = list(count.keys())
        freq = [count[ch] for ch in letters]
        
        res = 0

        def helper(i, cur):
            nonlocal res
            if i == len(letters):
                total = sum(cur)
                if total > 0:
                    ways = math.factorial(total)
                    for c in cur:
                        ways //= math.factorial(c)
                    res += ways
                return
            
            for k in range(freq[i] + 1):
                cur.append(k)
                helper(i + 1, cur)
                cur.pop()
        
        helper(0, [])
        return res
