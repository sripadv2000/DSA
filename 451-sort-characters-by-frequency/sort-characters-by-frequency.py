class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        freq = {}
         
        for ch in s:
            freq[ch] = 1 + freq.get(ch, 0)
        
        def my_fun(a):
            return freq[a]

        sorted_arr = sorted(freq.keys(), key = my_fun, reverse = True)
        
        res = []
        for ch in sorted_arr:
            res.append(ch*freq[ch])
        
        return "".join(res)
    