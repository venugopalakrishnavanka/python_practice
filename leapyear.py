def leapYear():

	year_input = int(input("Enter the year to know whether the year is leap year or not : "))
	if (year_input%4 == 0):
		print("This is leap year")
		return True
	else:
		print ("Entered year is not leap year:")
		return False

leapYear()

