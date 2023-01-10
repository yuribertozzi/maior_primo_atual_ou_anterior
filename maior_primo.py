def maior_primo (n):

    divisor = 2

    primalidade = True

    while divisor < n and primalidade == True:

        if n % divisor == 0:

            primalidade = False

        divisor = divisor + 1

    if primalidade == True and n != 1:

        return n

    else:

        return maior_primo (n - 1)
