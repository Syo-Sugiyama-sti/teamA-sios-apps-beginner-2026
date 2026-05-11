from datetime import datetime

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


# 商品注文機能
# ・返り値の辞書型の詳細
# キーは商品名 "name" と購入個数 "count" と items のインデックス "items_index" で構成
# 例：
# [
#     {
#         "items_index": 0,
#         "name": "りんご",
#         "count": 5,
#     }
# ]
def order_items() -> tuple[int, list[dict[str, int|str]], datetime]:
    # 1. 注文する商品名と在庫数を表示
    print("* 商品一覧 ***********")
    print("商品名\t価格\t在庫数")
    for item in items:
        print(f"{item['name']}\t{item['price']}\t{item['stock']}")
    print("**********************")
    
    # 2. 注文する商品名と注文数を入力
    order_list = []
    ITEM_NAME_LIST = [item['name'] for item in items]
    while True:
        # 商品選択
        print("\n商品名を入力してください（注文を終了する場合は 'end' を入力してください）")
        user_input = input()
        if user_input == "end":
            break

        # リスト内に存在しない処理を弾くエラー処理
        try:
            order_item_index = ITEM_NAME_LIST.index(user_input)
        except ValueError:
            print("[Error] 存在する商品名を入力してください")
            continue
        order_item_name = user_input

        # 購入数設定
        print("購入個数を入力してください")
        user_input = input()
        
        # 購入数が有効を満たすかの判定
        try:
            order_count = int(user_input)
        except ValueError:
            print("[Error] 有効な整数値を入力してください")
            continue
        if order_count < 1:
            print("[Error] 1以上の数値を入力してください")
            continue
        if order_count > items[order_item_index]["stock"]:
            print(f"[Error] オーダー数は在庫数以下にしてください（'{order_item_name}' のオーダー数は {items[order_item_index]["stock"]} 以下にしてください）")
            continue

        items[order_item_index]["stock"] -= order_count
        order_list.append({"items_index": order_item_index, "name": order_item_name, "count": order_count})

        print(f"'{order_item_name}'を{order_count}個注文リストに追加しました")

    # 3. 注文内容の表示と合計金額の集計・表示
    total_price = 0
    print("* 注文内容 ***********")
    print("商品名\t個数\t金額")
    for order in order_list:
        price = items[order["items_index"]]["price"] * order['count']
        print(f"{order['name']}\t{order['count']}\t{price}")
        total_price += price
    print(f"合計金額：{total_price}")
    print("**********************")

    now = datetime.now()
    return total_price, order_list, now

Log = []

def LogPrint():
    print(f"|{'日時':^23}|{'合計金額':^6}|{'商品':^6}|{'個数':^4}|")
    print("-" * 55)
    for sumprice,Product,Date in Log:
        date_str = Date.strftime("%Y-%m-%d %H:%M:%S")
        for i in range(len(Product)):
            if i==0:
                print(f"|{date_str:>25}|{sumprice:>10}|{Product[i][0]:<5}|{Product[i][1]:>6}|")
            else:
                print(f"|{" ":>25}|{" ":>10}|{Product[i][0]:<5}|{Product[i][1]:>6}|")
        print("-" * 55)
        

if __name__ == '__main__':
    now = datetime.now()

    print('お会計システム作成')

    # 合計金額として仮の値を設定
    test_price = int(1500)
    # 仮の値を入力して結果を出力
    change , num_moneys = process_payment(test_price)
    # お釣りの金額を表示    
    print(f"お釣りは{change}円")
    print(f"内訳:{num_moneys}")

        #ログの作成
    Log.append()
    LogPrint()
