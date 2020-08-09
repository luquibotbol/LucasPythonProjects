def factor(x, y, z):
	for a in range(1, x):
		b = x/a
		if b == int(b):
			print(b)
		for c in range(1, y+1):
			d = y/c
			if d == int(d)and d==b and d != 1:
				print("A common factor of a and b is", d)
		for e in range(1, z+1):
			f = z/e
			if f == int(f) and f == b and f != 1:
				print("A common factor of a and c is", f)

def addup(x, y):
	for a in range(1, x):
		b = x/a
		if b == int(b):
			b = int(b)
			print(b, a)
			r = a+b
			if r == y:
				print("This add up to y:  ", a, "and ",  b)


def compound(principal, rate, years):
        rate = rate/100
        p1 = principal
        for x in range(years):
                interest = principal * rate
                principal = principal + interest
                print(interest, "/  ", principal, "/  ", principal-p1 )


def simple(principal, rate, years):
        rate = rate/100
        interest = principal * rate * years
