

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        # if len(s) == 1:
        #     return 1
        current = 0
        for i in range(len(s)):
            j = i
            current = 0
            seen = []
            while j < len(s):
                # print(s[j])
                if s[j] not in seen:
                    # print("add")
                    current += 1
                    seen.append(s[j])
                    j += 1
                else: break
                longest = max(current, longest)
            # print()

        longest = max(current, longest)
        return longest
            


runner = Solution()
print(runner.lengthOfLongestSubstring(" "))