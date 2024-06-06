import pandas as pd
import numpy as np
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

page = st.sidebar.selectbox("ページを選択", ("おすすめの映画提案", "上映中映画一覧"))

def home_page():
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
        db_path = '/workspaces/AI_tech_final/maps-flaskdb/Final_work/database.db'

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

def about_page():
    st.title("現在上映中の映画一覧（一部）")
    st.write("リンクから公式サイトを閲覧することができます⭐️")

    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.07.24.png", caption="マッドマックス　フュリオサ", use_column_width=True)
    st.link_button("マッドマックス　フュリオサ", "https://wwws.warnerbros.co.jp/madmaxfuriosa/index.html")

    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.08.00.png", caption="ミッシング", use_column_width=True)
    st.link_button("ミッシング", "https://wwws.warnerbros.co.jp/missing/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.08.24.png", caption="基盤斬り", use_column_width=True)
    st.link_button("基盤斬り", "https://gobangiri-movie.com/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.08.44.png", caption="猿の惑星　キングダム", use_column_width=True)
    st.link_button("猿の惑星　キングダム", "https://www.20thcenturystudios.jp/movies/kingdom-apes")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.09.04.png", caption="関心領域", use_column_width=True)
    st.link_button("関心領域", "https://happinet-phantom.com/thezoneofinterest/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.10.35.png", caption="青春18×2君へと続く道", use_column_width=True)
    st.link_button("青春18×2君へと続く道", "https://happinet-phantom.com/seishun18x2/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.11.02.png", caption="デッドデッドデーモンズデデデデデストラクション　後章", use_column_width=True)
    st.link_button("デッドデッドデーモンズデデデデデストラクション　後章", "https://dededede.jp/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.11.24.png", caption="帰ってきた　あぶない刑事", use_column_width=True)
    st.link_button("帰ってきた　あぶない刑事", "https://abu-deka.com/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.11.44.png", caption="劇場版「ウマ娘　プリティダービー　新時代の扉」", use_column_width=True)
    st.link_button("劇場版「ウマ娘　プリティダービー　新時代の扉」", "https://movie-umamusume.jp/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.12.02.png", caption="ボブ・マーリー　ONE LOVE", use_column_width=True)
    st.link_button("ボブ・マーリー　ONE LOVE", "https://bobmarley-onelove.jp/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.12.21.png", caption="悪は存在しない", use_column_width=True)
    st.link_button("悪は存在しない", "https://aku.incline.life/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.12.45.png", caption="ゴジラ-1.0", use_column_width=True)
    st.link_button("ゴジラ-1.0", "https://godzilla-movie2023.toho.co.jp/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.13.05.png", caption="鬼平犯科帳　血闘", use_column_width=True)
    st.link_button("鬼平犯科帳　血闘", "https://onihei-hankacho.com/movie/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.13.29.png", caption="映画　からかい上手の高木さん", use_column_width=True)
    st.link_button("映画　からかい上手の高木さん", "https://takagi3-movie.jp/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.13.49.png", caption="ゴジラ×コング　新たなる帝国", use_column_width=True)
    st.link_button("ゴジラ×コング　新たなる帝国", "https://godzilla-movie.jp/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.14.06.png", caption="バジーノイズ", use_column_width=True)
    st.link_button("バジーノイズ", "https://gaga.ne.jp/buzzynoise_movie/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.14.25.png", caption="トラペジウム", use_column_width=True)
    st.link_button("トラペジウム", "https://trapezium-movie.com/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.14.47.png", caption="胸騒ぎ", use_column_width=True)
    st.link_button("胸騒ぎ", "https://sundae-films.com/muna-sawagi/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.15.05.png", caption="湖の女たち", use_column_width=True)
    st.link_button("湖の女たち", "https://thewomeninthelakes.jp/")
    
    st.image("/workspaces/AI_tech_final/スクリーンショット 2024-06-06 9.15.25.png", caption="恋するプリテンダー", use_column_width=True)
    st.link_button("恋するプリテンダー", "https://www.koipuri-movie.jp/")
    

if page == "おすすめの映画提案":
    home_page()
elif page == "上映中映画一覧":
    about_page()
