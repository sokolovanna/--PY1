money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
delta  = money_capital
month = 0  # количество месяцев, которое можно прожить

while delta >= spend:
    month += 1
    delta = salary + delta
    spend *= 1.05
    delta = delta - spend


print(month)
