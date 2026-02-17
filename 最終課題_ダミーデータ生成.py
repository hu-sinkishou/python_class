import csv
import random
from datetime import datetime, timedelta

# ダミーデータの生成設定
NUM_RECORDS = 20
OUTPUT_FILE = "dummy_data.csv"

# 商品名のリスト
product_names = [
    "ノートPC", "マウス", "キーボード", "モニター", "ウェブカメラ",
    "イヤホン", "スピーカー", "マイク", "USB充電器", "LANケーブル",
    "外付けHDD", "SSD", "メモリーカード", "ルーター", "モデム",
    "ディスプレイ", "プロジェクター", "プリンター", "スキャナー", "複合機",
    "デスクトップPC", "タブレット", "スマートフォン", "スマートウォッチ", "ゲーム機",
    "冷却パッド", "PCスタンド", "キーボード保護フィルム", "スクリーンプロテクター", "カメラ保護ガラス"
]

def generate_dummy_data(num_records):
    """ダミーデータを生成する"""
    data = []
    
    for i in range(num_records):
        product = random.choice(product_names)
        # 売上は100から50000の間のランダムな整数
        sales = random.randint(100, 50000)
        data.append([product, sales])
    
    return data


def save_to_csv(data, filename):
    """データをCSVファイルに保存"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # ヘッダーを書き込む
        writer.writerow(['商品名', '売上'])
        # データを書き込む
        writer.writerows(data)
    
    print(f"✓ {filename} を生成しました ({len(data)} レコード)")


def main():
    print("="*50)
    print("CSVダミーデータ生成プログラム")
    print("="*50)
    
    # ダミーデータを生成
    dummy_data = generate_dummy_data(NUM_RECORDS)
    
    # CSVファイルに保存
    save_to_csv(dummy_data, OUTPUT_FILE)
    
    # 生成されたデータの最初の5件を表示
    print("\n生成されたデータのサンプル（最初の5件）:")
    print("-"*40)
    for i, (product, sales) in enumerate(dummy_data[:5], 1):
        print(f"{i}. {product:15} : ¥{sales:,}")
    
    print("\n..." )
    print(f"合計：{NUM_RECORDS} レコード")


if __name__ == "__main__":
    main()
