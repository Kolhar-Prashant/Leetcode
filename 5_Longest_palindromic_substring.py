class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_pali(t):
            f = 0
            r = len(t) - 1
            mem = []
            while r > f:
                if t[f] == t[r]:
                    mem.append(t[f:r + 1])
                else:
                    mem.clear()
                f += 1
                r -= 1
            if len(mem) > 0:
                return mem

        def create_window(s, start, end, dir):
            if dir != 1:
                s = "".join(list(reversed(s)))
            a = start
            b = end
            while b != len(s):
                temp = s[a:b + 1]
                temp_str = check_pali("".join(temp))
                if temp_str != None:
                    for string in temp_str:
                        mem.append(string)
                b += 1

        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] != s[1]:
                return s[0]
            return s
        mem = []
        max_pali = ""
        create_window(s, 0, 1, -1)
        create_window(s, 0, 1, 1)
        max_len = 0
        if len(mem) > 0:
            for string in mem:
                if len(string) > max_len:
                    max_len = len(string)
                    max_pali = string
            return max_pali
        else:
            return s[0]
