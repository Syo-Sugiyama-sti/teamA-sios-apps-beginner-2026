# 商品情報の登録
items = [
    {'name': 'りんご', 'price': 100, 'stock': 10},
    {'name': 'バナナ', 'price': 80, 'stock': 20},
    {'name': 'みかん', 'price': 50, 'stock': 15},
    {'name': 'お肉', 'price': 500, 'stock': 5},
    {'name': '牛乳', 'price': 300, 'stock': 25},
    {'name': '魚', 'price': 400, 'stock': 30}
]
def process_payment(total_price):
    # 支払うべき金額を計算
    need_to_pay = total_price
    while need_to_pay > 0:
        # ユーザーの支払金額入力
        paid_price = int (input(f"必要な金額は{need_to_pay}円です。支払金額を入力してください："))
        need_to_pay -= paid_price

        if need_to_pay > 0:
            print(f"{need_to_pay}円不足しています")

    
    # 差額をお釣りとする
    change = -(need_to_pay)
    if change == 0:
        print("お釣りはありません")
        return 0
    else:
        money = [10000,5000,1000,500,100,50,10,5,1]
        num_of_money = {}
        num_coin = change
        for i in money:
            num_moneys = num_coin // i
            num_coin %= i

            if num_moneys > 0:
                num_of_money[i]=num_moneys

        return change,num_of_money


if __name__ == '__main__':
    print('お会計システム作成')
    # 合計金額として仮の値を設定
    test_price = int(1500)
    # 仮の値を入力して結果を出力
    change , num_moneys = process_payment(test_price)
    # お釣りの金額を表示    
    print(f"お釣りは{change}円")
    print(f"内訳:{num_moneys}")
