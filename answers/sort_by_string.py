def sort_by_string(s, t):
	# sorts string, s, by order of string, t.
	# ("hello", "leho") => "lleho"
	# ("good", "osf") => "oogd"
	# ("", "hea") => ""
	# ("heyyy", "") => "heyyy"

	if len(t) == 0:
		return s

	st = list(s)
	sorted_string = ""

	# sort letters
	for i in range(len(t)):
		for j in range(len(s)):
			if s[j] == t[i]:
				sorted_string += s[j]
				st.remove(s[j])

	# append letters that were not sorted
	sorted_string += ''.join(st)

	return sorted_string