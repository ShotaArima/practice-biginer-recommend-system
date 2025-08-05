# レコメンドシステムの練習
- 参考文献 : [実務で役立つPython機械学習入門](https://www.shoeisha.co.jp/book/detail/9784798184890)
  - Chapter3 様々なアルゴリズムを体験しよう
    - Section 03 レコメンドアルゴリズム : 個人の趣向に沿った商品をおすすめしよう

# 内容
- 

# 使用技術
- ライブラリ
  - `pandas`
  - `surprise`
- モデル (※が使用するもの)
  - ※ SVD(Singular Value Decomposition) : 特異値分解
    - 大量のユーザやアイテム情報を特徴ベクトル(潜在因子)に圧縮する
    - ユーザとアイテム間の関連性を見つけ出し、未評価アイテムに対するユーザの評価を予測する
  - KNN (k-Nearest Neighbors)
    - アイテムやユーザ間の類似性を計算し、最も類似性の高い $k$ 個のアイテムやユーザから推薦を行う
  - NMF (Non-negative Matrix Factorization)
    - 正の値しか持たない行列を2つの正の行列に分解し、欠損値を補完するアルゴリズム
    - SVD同様行列分解を行いますが、すべてが正である必要がある
  - MF (Matrix Factorization)
    - 欠損値が存在する行列に適用可能な特異値分解手法の類似手法
    - 潜在的な特徴(ユーザの隠れた好みやアイテムの隠れた特性)を発見するために使用される
  - 深層学習
    - AutoEncoderを用いた手法
    - NNを用いた協調フィルタリング手法などがある
- 評価
  - MAE (Mean Absolute Error)
    - 予測と実際の評価との差の絶対値の平均
    - 個々の誤差を等しく扱うため、ハズレ値の影響を受けにくい特性がある
  - Precision@k and Recall@k
    - $k$ 個の推薦されたアイテムの中で、以下の計算をする
      - Precision : ユーザが本当に好きだったアイテムの割合
      - Recall : ユーザが好きなアイテムのうち、どれだけ推薦できたか
  - F-score
    - PrecisionとRecallの調和平均を計算する
    - PrecisionとRecallのバランスを取る指標