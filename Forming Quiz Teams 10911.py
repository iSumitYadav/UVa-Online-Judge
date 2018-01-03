while 1:
	tc = 1
	t = int(input())

	if t == 0:
		break

	t = 2*t
	x = []

	while t:
		name, x_co, y_co = input().split(' ')
		x.append([int(x_co), int(y_co)])
		t = t-1

	x.sort()
	# print(x)

	first = 0

	for i in range(0, len(x), 2):
		x1, y1 = x[i]
		x2, y2 = x[i+1]
		first += ((x1 - x2)**2 + (y1 - y2)**2)**(.5)

	print("Case " + str(tc) + ": " + str(round(first, 2)))
	tc += 1