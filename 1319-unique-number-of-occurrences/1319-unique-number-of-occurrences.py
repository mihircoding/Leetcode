class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for item in arr:
            d[item] += 1
        occurances = list(d.values())
        print(occurances)
        return len(occurances) == len(set(occurances))