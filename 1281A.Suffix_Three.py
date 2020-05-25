n = int(input())

for i in range(n):
	suffix_three = list(input())
	j = len(suffix_three)
	if suffix_three[j - 1] == 'u':
		print("JAPANESE")
	elif suffix_three[j - 1] == 'o':
		print("FILIPINO")
	elif suffix_three[j - 1] == 'a':
		print("KOREAN")

