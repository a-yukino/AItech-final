import pandas as pd
import numpy as np
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

st.title('おすすめの映画提案AIシステム')
st.write('あなたの見たい映画の :blue[感情の度合い]を回答してください！')

st.write('ー感情分析において感情は10種類に分けられることが多いです。')
st.write('😊ここではあなたの今観たい映画を感情の面から検索し、提案します😊')

st.write('以下の項目にそれぞれどの程度求めるか回答してください。')
st.write('')

pick_1 = int(st.select_slider("🤗喜び🤗", ["1", "2", "3","4","5"]))
pick_2 = int(st.select_slider("👹怒り👹", ["1", "2", "3","4","5"]))
pick_3 = int(st.select_slider("😆昂り😆", ["1", "2", "3","4","5"]))
pick_4 = int(st.select_slider("😢哀しみ😢", ["1", "2", "3","4","5"]))
pick_5 = int(st.select_slider("😍好感😍", ["1", "2", "3","4","5"]))
pick_6 = int(st.select_slider("😱怖い😱", ["1", "2", "3","4","5"]))
pick_7 = int(st.select_slider("☺️安心☺️", ["1", "2", "3","4","5"]))
pick_8 = int(st.select_slider("😵嫌悪😵", ["1", "2", "3","4","5"]))
pick_9 = int(st.select_slider("😮驚き😮", ["1", "2", "3","4","5"]))
pick_10 = int(st.select_slider("🫣恥🫣", ["1", "2", "3","4","5"]))

if st.button("映画を提案してもらう"):
    # ユーザーの選択をリストにまとめる
    answer_list = [pick_1, pick_2, pick_3, pick_4, pick_5, pick_6, pick_7, pick_8, pick_9, pick_10]
    
    # データベースのパス
    db_path = '/Users/yukino/maps-flaskdb/Final_work/database.db'

    # データベースに接続
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # データを読み込む
    cur.execute("SELECT title, happy, angry, up, sard, like, scare, luh, no, surp, emba FROM final_work_ai")
    rows = cur.fetchall()

    # データフレームに変換
    df = pd.DataFrame(rows, columns=["映画タイトル", "喜", "怒", "昂", "哀", "好", "怖", "安", "嫌", "驚", "恥"])

    # 特徴量を抽出
    features = df[["喜", "怒", "昂", "哀", "好", "怖", "安", "嫌", "驚", "恥"]].values

    # NaNを含む行がないか確認し、あれば0で埋める
    if np.isnan(features).any():
        st.write("データにNaN値が含まれています。NaN値を0に置き換えます。")
        features = np.nan_to_num(features)

    # コサイン類似度を計算
    similarity = cosine_similarity([answer_list], features)[0]

    # 最も類似度の高い映画を見つける
    most_similar_index = similarity.argmax()
    recommended_movie = df.iloc[most_similar_index]["映画タイトル"]
    st.write(f"おすすめの映画: {recommended_movie}")

    # DBへの接続を閉じる
    con.close()