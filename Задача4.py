num_init = int(input('введите целое положительное число- '))
maximum = num_init % 10
num = num_init
while num > 0:
    digit = num % 10
     if digit > maximum:
        maximum = digit

     if digit == 9:
         break

     num //= 10
     print(num)

print(f"наибольшая цифра в числе {num_init} равна { maximum}")
