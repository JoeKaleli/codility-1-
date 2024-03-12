#Cardpayments
from datetime import datetime

#Solution Function
def solution(amount, dates):
    total_sum = 0
    card_payment = {}
    #Iterates over the months and caluclates month difference
    for date_str, amount in dates:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        month_key = (date.year, date.month)


        
    for date_str, amount in dates:
        date = datetime.strptime(date_str,"%Y-%m-%d")
        month_key = (date.year, date.month)

        if amount >= 100 and card_payment.get(month_key, 0) >= 3:
            total_sum += amount
        elif amount >= 100 and card_payment.get(month_key, 0) < 3:
            total_sum += amount - 5
        elif amount < 0:
            total_sum += amount

    return total_sum


amounts = [100, -50, 200, -20, -80, -30, -30, -30]
dates = [("2020-01-01", 100), ("2020-01-02", -50), ("2020-01-10", 200), ("2020-02-15", -20),
         ("2020-02-20", -80), ("2020-03-05", -30), ("2020-03-10", -30), ("2020-03-25", -30)]
    


final_balance = solution(amounts, dates)
print("Final balance at the end of 2020:", final_balance)