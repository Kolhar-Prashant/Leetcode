class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def find_prefix(L):
            Dict = {}
            for word in L:
                if word == "":
                    continue
                if len(word) == 1:
                    if word in Dict:
                        Dict[word] += 1
                    else:
                        Dict[word] = 1
                    continue
                start = 0
                end = 1
                while end != len(word) + 1:
                    t = "".join(word[start:end])
                    if t not in Dict:
                        Dict[t] = 1
                    else:
                        Dict[t] += 1
                    end += 1
            is_empty = not Dict
            if is_empty == False:
                max_len = max(Dict.values())
                max_len_prefix = ""
                if max_len >= len(L):
                    for prefix, length in Dict.items():
                        if length == max(Dict.values()):
                            max_len_prefix = prefix
                    return max_len_prefix
            return ""

        if len(strs) > 1:
            return find_prefix(strs)
        elif len(strs) == 1:
            if len(strs[0]) == 1:
                return strs[0]
            else:
                return ""
        else:
            return ""

