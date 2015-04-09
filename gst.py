x=1
while True:
	amount = input(("Input Original Price: RM"))
	gst = amount * 1.06
	print "Price after GST is RM%s" % gst
	x += 1