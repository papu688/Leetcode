class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        else:
            prefix = strs[0]

            for word in strs[1:]:
                while word[:len(prefix)] != prefix and prefix:
                    prefix = prefix[:len(prefix)-1]

        return prefix
       