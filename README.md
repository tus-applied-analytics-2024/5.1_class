# 課題

## 禁則事項
`test_main.py` を修正した場合、不正行為があったと見なされ本講義を含む今学期の全ての単位を失う可能性があります。

## 内容
以下の仕様を満たすクラスを書いてください
- クラス名: LinearRegression
- 内部変数: w
- 命令1: `__init__`
    - 引数: dim
    - 中でやること: 内部変数 w を、要素が全て1で長さ `dim` の `numpy.ndarray` で初期化
- 命令2: `predict`
    - 引数: X (`sample_size` x `dim` の `numpy.ndarray` と想定)
    - 出力: Xw

## 実行環境の作り方
`pip3 install -r requirements.txt`

## 実行コマンド
`python3 test_main.py`
