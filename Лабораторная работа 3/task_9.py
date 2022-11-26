salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0

for _ in range(months):
    debt = spend - salary
    spend *= 1 + increase
    money_capital += debt

print(round(money_capital))
# комментарий