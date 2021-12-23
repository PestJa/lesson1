revenue = float(input("введите значение выручки-"))
coasts = float(input("введите значение издержек - "))
result = revenue - coasts
if result > 0:
    print(f"поздравлямба !!! Ваша компания работает с прибылью {result} !")
    print(f"рентабильность выручки - {result / revenue:.3f}")
    persons = int(input("Сколько счастливых целых сотрудников работает в вашей компании?-"))
    print(f"прибыль на одного сотрудника - {result / persons:.2f}")
elif result < 0:
    print(f"Вы работаете с убытком - {-result}")
else:
    print(f" ноль - это тоже результат! зато стабильно!!!")
