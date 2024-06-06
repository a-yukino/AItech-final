# ベースイメージの指定
FROM python:3.9

# 作業ディレクトリの設定
WORKDIR /app

# 必要なライブラリをインストールするためのファイルをコピー
COPY requirements.txt .

# ライブラリのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# ストリームリットのポートを指定
EXPOSE 8501

# コンテナが起動したときに実行されるコマンド
CMD ["streamlit", "run", "aitech_final.py"]


