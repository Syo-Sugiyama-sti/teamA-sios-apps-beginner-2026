# 商品情報の登録
items = [
    {'name': 'りんご', 'price': 100, 'stock': 10},
    {'name': 'バナナ', 'price': 80, 'stock': 20},
    {'name': 'みかん', 'price': 50, 'stock': 15},
    {'name': 'お肉', 'price': 500, 'stock': 5},
    {'name': '牛乳', 'price': 300, 'stock': 25},
    {'name': '魚', 'price': 400, 'stock': 30}
]

if __name__ == '__main__':
    print('お会計システム作成')


def point_card_system(total_price):
    """
    ポイントカードの確認、新規作成、ポイント付与を行う関数
    引数: total_price (合計金額)
    戻り値: points (今回付与されたポイント)
    """
    print("\n--- ポイントカード確認 ---")
    
    # 1. カードの有無を確認
    while True:
        point_card = input("ポイントカードをお持ちですか？ (y/n): ").lower()
        if point_card == 'y' or point_card == 'n':
            break  
        else:
            print("無効な入力です。y か n で答えてください。")

    points = 0 # 付与ポイントの初期化

    # 2. ポイント付与または新規作成の処理
    if point_card == 'y':
        points = int(total_price * 0.01)
        print(f"今回の付与ポイント: {points}pt です。")
        
    else:
        new_make_card = input("カードを新しく作成しますか？ (y/n): ").lower()
        if new_make_card == 'y':
            name = input("氏名を入力してください: ")
            phone = input("電話番号を入力してください: ")
            
            points = int(total_price * 0.01)
            new_customer = {
                'name': name, 
                'phone': phone, 
                'point': points
            }
            
            print(f"\n作成が完了しました！")
            print(f"【登録情報】名前: {new_customer['name']}様 / 電話番号: {new_customer['phone']}")
            print(f"初回ポイントとして {points}pt 付与しました。")
        else:
            print("ポイント付与なしで会計を終了します。")

    return points
