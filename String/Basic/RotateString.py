class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False  
        doubled_s = s + s
        return goal in doubled_s
        
sol = Solution()
print(sol.rotateString("rotation", "tionrota"))