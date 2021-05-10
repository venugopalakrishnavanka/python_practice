def largest():

	n = int(input("Enter the number of elements  :"))

	input_list = []

	for i in range(n):
		num = input("Enter the number of elem  :")		
		input_list.append(num)

	max_value = input_list[0]

	for element in input_list:
		if element>max_value:
			max_value = element

	print("Maximum value is :",max_value)

largest()
