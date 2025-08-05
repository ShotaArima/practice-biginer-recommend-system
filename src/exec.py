# ライブラリの追加
import pandas as pd


# データのインポート
df = pd.read_csv("data/animal_rating.csv", index_col=0)

# print(df.head())

# 前処理
df_stacked = df.stack().to_frame().reset_index()
df_stacked.columns = ["ユーザID", "商品ID", "rating"]
# print(df_stacked.head())

from surprise import Dataset, Reader

reader = Reader(rating_scale=(1, 5)) # rating_scaleというパラメータでratingの範囲を設定 レビュースコアが1~5までなので、(1, 5)と設定している
data = Dataset.load_from_df(df_stacked, reader=reader)

# データの分割
from surprise.model_selection import train_test_split
train, test = train_test_split(data, test_size=.25)

# 学習 SVD
from surprise import SVD
model = SVD()
model.fit(train)

# モデルの評価
from surprise import accuracy
test_pred = model.test(test)
print(f"accuracy : {accuracy.rmse(test_pred)}")

# 予測
user_id = "user_70"
print(f"{user_id}に対するおすすめ度")
for item_id in ["犬", "猫", "ペンギン", "イルカ", "パンダ"]:
    pred = model.predict(user_id,item_id)
    print(f"{item_id}\t\t{pred.est:.2}",)