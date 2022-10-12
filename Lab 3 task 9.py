salary = 5000 # зарплата
spend = 6000 # траты
months = 10 # количество месяцев
increase = 0.03 # рост цен

need_money = 0 # количество денег, чтобы прожить 10 месяцев

def count_capital(salary, spend, months, increase):
    current_spend = spend
    capital = 0
    for i in range(1, months + 1):
        current_capital = (current_spend - salary)
        current_spend = current_spend * (1 + increase)
        capital += current_capital
    final_capital = round(capital)
    return final_capital
print(count_capital(salary, spend, months, increase))
