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

    #ログの作成
    
    Log.append()
    LogPrint()
