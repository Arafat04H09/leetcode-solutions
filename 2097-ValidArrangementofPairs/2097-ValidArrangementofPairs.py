class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        G = defaultdict(list)
        _in = defaultdict(int)
        for s, e in pairs:
            G[s].append(e)
            _in[s] += 1
            _in[e] -= 1
        route = []
        s = [next((n for n in G if _in[n] == 1), pairs[0][0])]
        while s:
            while (arr := G[s[-1]]):
                s.append(arr.pop())
            route.append(s.pop())
        return ((route[i+1], route[i]) for i in range(len(route)-2, -1, -1))