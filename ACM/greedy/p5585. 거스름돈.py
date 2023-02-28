start_exchange_money = 500          # 거스름돈 최대치 금액 설정
money = 1000 - int(input())

is_switch = False
result = 0

while(start_exchange_money):
    exchange_cnt = money // start_exchange_money    # 잔돈 개수
    money = money - (start_exchange_money * exchange_cnt)
    result += exchange_cnt

    is_switch = not is_switch
    if (is_switch):
        start_exchange_money = start_exchange_money // 5
    else:
        start_exchange_money = start_exchange_money // 2

print(result)