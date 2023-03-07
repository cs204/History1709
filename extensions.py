
name = input("File name: ")
match name:
	case "hello.jpg":
		print("image/jpeg")
	case "document.pdf":
		print("application/pdf")
	case _:
		print("Which?")
