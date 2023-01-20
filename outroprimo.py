def maior_primo (n): 

	while n != 1: 

		divisor = 2 

		primalidade = True 

		while divisor < n and primalidade == True: 

			if n % divisor == 0: 

				primalidade = False 

			divisor = divisor + 1 

		if primalidade == True: 

			return n

		n = n - 1
