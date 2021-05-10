def check_prime(num):
	
	for i in range(2,num):
		if num%i == 0:
			print("This is not a prime number : ",num)
			return False

	return True



num = int(input("Enter the num : \n"))
venu_value = check_prime(num)
print(" Prime number flag is : ",venu_value)
