import numpy as np
import pandas as pd
import time
from PIL import Image
import streamlit as st

st.title("クリスマスプレゼントを探せ！")

tab0,tab1,tab2,tab3,tab4 = st.tabs(["プロローグ","PART1","PART2","PART3","エピローグ"],)

with tab0:
    if ("yousei" not in st.session_state) :
        st.session_state.yousei = False
        st.session_state.aisatu = False
        st.session_state.kaikei = False
        st.session_state.sou = False
        st.session_state.next = 0
        st.session_state.hai = False
        st.session_state.find = False
        time.sleep(5)
        st.text("寒さが深くなり、吐く息が白くなってきた今日この頃。")
        time.sleep(4)
        st.text("街の景色が音楽が雰囲気が、クリスマスに近づくごとに浮かれていく気配を感じつつ、")
        time.sleep(4)
        st.text("僕たちも夫婦としての初めてのクリスマスを迎えることになりました。")
        time.sleep(6)
        st.text("ちょうど10年前、付き合って初めてのクリスマスは僕がスキー合宿に行ってしまって、")
        time.sleep(4)
        st.text("一緒に過ごすことができなかったのは、今となっては笑い話ですね。")
        time.sleep(6)
        st.text("前置きが少し長くなってしまいましたが、")
        time.sleep(4)
        st.text("実は、きみにあげるはずだったプレゼントをなくしてしまったんだ。。。")
        time.sleep(4)
        st.text("全然本当に大したものじゃないんだけど（おそらくバレてるんだけど）、")
        time.sleep(4)
        st.text("クイズを出したいという目的からこんな設定にさせてください。")
        time.sleep(6)
        st.text("ちなみに僕はプレゼントがどこにあるのか皆目見当もつきません。")
        time.sleep(4)
        st.text("だけど、さっきからじっとこっちを見ている妖精が何か知ってそうだ。")
        time.sleep(4)
        st.text("そいつと協力して、プレゼントを探してくれないかな。")
        time.sleep(3)


    if not(st.session_state.yousei):
        st.session_state.yousei = st.button("妖精と探す")
        st.snow()
    if st.session_state.yousei:
        st.write("PART1に進め")

# if st.

if st.session_state.yousei:

    
    with tab1:
        img_npochamu = Image.open("npochamu.png")
        img_kimi = Image.open("kimi.jpg")
        img_ozi = Image.open("ozi.jpg")
        st.write("レストランにて、変な妖精と一緒にプレゼントを探すための会議が始まった")
        with st.chat_message("user",avatar=img_npochamu):
            st.write("んぽちゃむに全て任せるっちゃむ！！")
        if not(st.session_state.aisatu):
            st.session_state.aisatu = st.button("頼んだ")
        if st.session_state.aisatu == True:
            with st.chat_message("user",avatar=img_npochamu):
                st.write("んぽちゃむは見たっちゃむ。「イスはイスでも食べられるイス」だったちゃむ！")
            answer = st.text_input("回答") 

            if answer == "カレーライス":
                with st.chat_message("user",avatar=img_npochamu):
                    st.write("そうっちゃむ！カレーライスっちゃむ！")
                    img_chumon = Image.open("chumon.jpg")
                    st.image(img_chumon,use_column_width=True)
                    st.write("カレーライスとー、ハンバーグとー・・・")
                with st.chat_message("user",avatar=img_kimi):
                    img_kimi3 = Image.open("kimi3.jpg")
                    st.image(img_kimi3,use_column_width=True)
                st.session_state.kaikei = st.button("次へ",key=1)

            elif answer == "オムライス":
                with st.chat_message("user",avatar=img_npochamu):
                    st.write("そうっちゃむ！オムライスっちゃむ！")
                    img_chumon = Image.open("chumon.jpg")
                    st.image(img_chumon,use_column_width=True)
                    st.write("オムライスとー、ハンバーグとー・・・")
                with st.chat_message("user",avatar=img_kimi):
                    img_kimi3 = Image.open("kimi3.jpg")
                    st.image(img_kimi3,use_column_width=True)
                st.session_state.kaikei = st.button("次へ",key=1)

            elif answer=="":
                pass
            else:
                with st.chat_message("user",avatar=img_npochamu):
                    st.write("違うっちゃむ！")      

            if st.session_state.kaikei:
                with st.chat_message("user",avatar=img_npochamu):
                    img = Image.open("gohan.jpg")
                    st.image(img,use_column_width=True)
                    st.write("（ﾑｼｬﾑｼｬﾑｼｬﾑｼｬ）")
                    img22 = Image.open("gohan2.jpg")
                    st.image(img22,use_column_width=True)                    
                st.write("PART2に進め")
                st.session_state.next = 1


if st.session_state.next == 1:
    with tab2:
        with st.chat_message("user",avatar=img_npochamu):
            st.write("げぷっ。もうお腹いっぱいちゃむ…")
            st.write("そういや、何か探し物をしてるみたいっちゃむね")  
        if not(st.session_state.sou):
            st.session_state.sou = st.button("そう")             
        
        if st.session_state.sou==True:
            with st.chat_message("user",avatar=img_npochamu):
                st.write("んぽちゃむこの前ー、空からやってきたモノに急に連れ去られてー、")
                st.write("そこでー、変な奴に捕まってー、大変だったちゃむ。")
                st.write("ありえんちゃむよねー。何に捕まったと思うちゃむ？")
            answer = st.text_input("回答.")             

            if answer == "宇宙人":
                with st.chat_message("user",avatar=img_npochamu):
                    st.write("そうそう！")
                    img = Image.open("kimimaro2.jpg")
                    st.image(img,use_column_width=True)
                    st.write("あの時きみまろが助けに来なかったらどうなることかと思ったちゃむ")
                with st.chat_message("user",avatar=img_kimi):
                    img = Image.open("kimi4.jpg")
                    st.image(img,use_column_width=True)

                st.write("PART3に進め")
                st.session_state.next = 2

            elif answer == "エイリアン":
                with st.chat_message("user",avatar=img_npochamu):
                    st.write("そうそう！")
                    img = Image.open("kimimaro2.jpg")
                    st.image(img,use_column_width=True)
                    st.write("あの時きみまろが助けに来なかったらどうなることかと思ったちゃむ")
                with st.chat_message("user",avatar=img_kimi):
                    img = Image.open("kimi4.jpg")
                    st.image(img,use_column_width=True)

                st.write("PART3に進め")
                st.session_state.next = 2
            elif answer=="":
                pass
            else:
                with st.chat_message("user",avatar=img_npochamu):
                    st.write("違うっちゃむ！")  


if st.session_state.next ==2:
    with tab3:
        with st.chat_message("user",avatar=img_npochamu):
            st.write("そんな話はどうでもいいっちゃむ！！")
            st.write("早く探し物を探すっちゃむよ！！")
            img = Image.open("npo2.jpg")
            st.image(img,use_column_width=True)      
        if not(st.session_state.hai):
            st.session_state.hai = st.button("わかった")        
                  
        if st.session_state.hai==True:
            with st.chat_message("user",avatar=img_npochamu):
                st.write("もうしょうがないから んぽちゃむがそこまで案内するちゃむ！")
                st.write("ついてくるちゃむ！")
            with st.chat_message("user",avatar=img_ozi):
                st.write("（この家の中で、んぽちゃむがいるところを探してね）")
            st.session_state.find = st.button("見つけた")

        if st.session_state.find:
            st.write("エピローグへ進め")
            st.session_state.next = 3

if st.session_state.next == 3:
    with tab4:
        with st.chat_message("user",avatar=img_npochamu):
            st.write("メリークリスマスちゃむ！")
        with st.chat_message("user",avatar=img_kimi):
            st.write("メリークリスマス！")
        img = Image.open("end.jpg")
        st.image(img,use_column_width=True)         
        
        with st.chat_message("user",avatar=img_ozi):
            st.write("以上で終了です。遊んでくれてありがとう！")
        
       
# a = st.slider("aa",0,100)
# st.sidebar(st.slider("bb",0,1000))
# bt = st.button("回答ボタン")

# if a==50 and bt == True:
#     st.text("正解")
#     flag = 1

# if flag == 1:
#     st.write(flag)

    



###計画
#んぽちゃむがクイズの手助け
#最後以外はんぽちゃむの適当なクイズ（答えが食べ物だったらそれを食べたり、ものだったら遊んだり（んぽちゃむ）がして）
#最終的にプレゼント（箱に入ってる想定）の箱の側面に何かステッカーを張っておいて、それを物体検出→正解→開けるという流れ
#最終的にはんぽちゃむがその箱を隠していた（わざと）。それをひよりが探すという流れ

# st.write("Display image")
# from PIL import Image

# #チェックボックス（チェックを入れるとTrueになる）
# if st.checkbox("Show Image"):
#     img = Image.open("001_hiyoko.jpg")
#     st.image(img, caption="hiyoko",use_column_width=True)