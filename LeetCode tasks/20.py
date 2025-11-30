class Solution:
    def isValid(self, s: str) -> bool:
        s = s.replace('[]', '')
        s = s.replace(f'{{}}', '')
        s = s.replace('()', '')
        return s == ''
