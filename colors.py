def green():
	color = "jade"
	print("green")
	print("end")
	return -1
def red():
	color = "crimsom"
	print("red")
	green()
def blue():
	red()
	print("blue")
blue()
