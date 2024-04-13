# 1)
academy = input("რომელ პროგრამირების აკადემიაში სწავლობ? ")
if academy == "GOA":
    print("სწორია.")
else:
    print("არასწორი გადაწყვეტილება მიიღე.")


# 2)
price = float(input("შეიყვანეთ ფასი: "))
budget = float(input("შეიყვანეთ თქვენი ბიუჯეტი: "))

if budget >= price:
    print("თანხა გყოფნით.")
else:
    print("თანხა არ გყოფნით.")


# 3)
num =  int(input("შეიყვანეთ რიცხვი: "))
if num >= 5:
    print(num * 2)
else:
    print(num * 4)


# 4)
ticket_price = 10
quantity = int(input("რამდენი ბილეთის ყიდვა გსურთ? "))
if quantity < 5:
    print(("ბილეთების ფასი არის ") + str(quantity * ticket_price))
else:
    print(("ბილეთების ფასი არის ") + str(quantity * (ticket_price - ticket_price * 30/100)))

