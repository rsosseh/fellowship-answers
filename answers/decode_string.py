def decode_string(s):
	# decode string by specified encoding rule
	# ("4[ab]") => "abababab"
	# l=2,r=4
	# ("2[ab3[c]]") => "abcccabccc"
	# ("") => ""

	left_index = 0
	right_index = 0
	pre_chars = ''

	for i in range(len(s)):
		if s[i].isalpha():
			pre_chars += s[i]
		elif s[i] == '[':
			left_index = i
			break;
	right_index = len(s) - 1
	if(left_index == 0):
		return s
	else:
		return pre_chars + (int(s[left_index-1]) * decode_string(s[left_index+1:right_index]))