# Data-Integration-Streamlit

## 準備
* .venvを作成する

```
 python -m venv .venv
```

* .venvを有効化する(Macの場合)

```
 source .venv/bin/activate
```

* requirements.txtに記載のライブラリをインストールする

```
 pip install -r requirements.txt
```

## 環境変数

* rootに`.env`ファイルを作成し、以下の環境変数を設定する

```
# DataLakeの接続先情報
AZURE_STORAGE_ACCOUNT_NAME='${xxx}'
# Azureに登録したアプリの認証情報
AZURE_TENANT_ID='${xxx}'
AZURE_CLIENT_ID='${xxx}'
AZURE_CLIENT_SECRET='${xxx}'
```


## 実行

```
python main.py
```
