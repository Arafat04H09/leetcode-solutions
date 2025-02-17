def numTilePossibilities(self, tiles: str) -> int:
        letter_count = collections.Counter(tiles)

        def dfs():
            count = 0
            for tile in letter_count:
                if letter_count[tile] == 0:
                    continue
                letter_count[tile] -= 1
                count += dfs() + 1 
                letter_count[tile] += 1
            return count   
        return dfs()