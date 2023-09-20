def nmax(a):
	if len(a) == 0:
		return 0
	var_max = a[0]
	for i in a:
		if i > var_max:
			var_max = i
	return var_max
