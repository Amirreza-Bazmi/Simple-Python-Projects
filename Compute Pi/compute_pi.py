# Claculation of pi
for i in range(10000,110000,10000):
    sum = 0
    pi_number = 0
    counter = 1
    while counter <= i:
        sum += ( (-1) ** (counter + 1) ) / (2 * counter - 1)
        counter += 1
    pi_number = 4 * sum
    print(f"pi value for {i}: {pi_number}")