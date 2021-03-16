class Solution:
	def romanToInt(self, s: str) -> int:
        vals_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
		if not s:
			return 0
		answer = 0
		prev = vals_dict.get(s[0])
		for num in s:
			answer += vals_dict.get(num)
			if prev < vals_dict.get(num):
				answer -= 2 * prev
			prev = vals_dict.get(num)
		
    return answer

    