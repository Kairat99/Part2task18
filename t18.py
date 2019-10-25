num2 = int(input("Введите ваш возраст: "))

numbers = list(range(num2))
print(numbers)
if num2 % 2== 0:
    print(numbers[2::2])
else:
    print(numbers[1::2])    
