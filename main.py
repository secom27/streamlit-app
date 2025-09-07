import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

######################
# DataFrame
######################
st.title('Streamlit超入門')
st.write('DataFrame')
st.sidebar.title('入力欄')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

df_json = pd.DataFrame({
    "家": ["house"],
    "七海": ["la mer"]
})

# DataFrame表示
# （writeも使えるが、引数指定可能なのはdataframe）
# st.table(df.style.highlight_max(axis=0))
# st.dataframe(df.style.highlight_max(axis=0), width=300)
# st.json(df_json.to_dict())

######################
# MagicCommand
######################
# """
# # TEST
# ## List
# - [ ] testファイル作成削除
# ## CMD
# >色文字や絵文字を入れることも出来る
# :rainbow[rainbow]
# :tulip:
# ```sql
# select * from testtable;
# desc testtable;
# ```
# """

######################
# VariousChart
######################
df_chart = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)

# st.line_chart(df_chart)
# st.bar_chart(df_chart)
# st.area_chart(df_chart)
# st.scatter_chart(df_chart)

# map
df_map = pd.DataFrame(
    np.random.rand(300, 2)/[50, 50] + [35.0, 139.0],
    columns = ['lat', 'lon']
)
# st.map(df_map)

# display_image
st.write('Image')

######################
# Interactive
######################
# CheckBox
if st.sidebar.checkbox('Show Image'):
    img = Image.open('zoom.jpg')
    st.image(img, caption='zoom_img_sample', use_column_width=True)

# SelectBox
option = st.sidebar.selectbox(
    '好きな数字を教えてね',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です。'

# TextInput
hobby = st.sidebar.text_input('趣味を書いてね')
'あなたの趣味：', hobby

# Slider
condition = st.sidebar.slider('今の調子は？', 0, 100, 50)
'あなたの調子：', condition

if condition >= 80:
    st.write('絶好調だね')
elif condition >= 50:
    st.write('好調だね')
elif condition >= 20:
    st.write('まずまずかな')
else:
    st.write('どしたん話聞こか？')

######################
# 2ColumnsLayout
######################
left_column, right_column = st.columns(2)
toggle = left_column.toggle('右カラムに表示')
if toggle:
    right_column.write('ボタンが押されました')
    
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

######################
# ProgressBar
######################
st.write('Start!!!')
latest_ireration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_ireration.text(f'{i+1}%...')
    bar.progress(i+1)
    if i+1 == 100:
        latest_ireration.text(f'{i+1}%')
        break
    time.sleep(0.05)
st.write('Done!!!')
