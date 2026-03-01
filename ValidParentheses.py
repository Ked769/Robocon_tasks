class Solution:
    def isValid(self, s: str) -> bool:
        starts = "([{"
        ends = ")]}"
        running = ""
        for i in range(len(s)):
            if s[i] in starts:
                running = running + s[i]
            if s[i] in ends:
                if not running:
                    return False
                if starts.index(running[-1]) == ends.index(s[i]):
                    running = running[:-1]
                else:
                    return False
        return True if not running else False
