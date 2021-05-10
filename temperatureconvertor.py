def temperate_converter():
	
	num = input("Choose the converter 1 for c to f and 0 for f to c  :")	

	if num == 1:
		# Writing C to F logic here
		input_temp_value = float(input("Enter the temp in c : "))
		c = input_temp_value
		temp_sum = (c*9/5.0)
		f_value = temp_sum+32
		print("Fahrenheit value is : ",f_value)
	else:
		# Writing F to C logic here
		input_temp_value =  float(input("Enter the temp in f : "))
		f = input_temp_value
		temp_sum = f-32
		c_value = temp_sum*5/9.0
		print("Celcius value is  : ",c_value)

temperate_converter()
