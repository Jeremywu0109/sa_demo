import streamlit as st
import numpy as np
import pandas as pd
import json
base="dark"


def load_data_json():
    return pd.read_json('E:\路外停車資訊.json')
def load_data_excel():
    return pd.read_excel('E:\table.xlsx')
info_column = ['areaId','areaName','parkName','totalSpace','surplusSpace','payGuide','introduction','address','wgsX','wgsY','parkId']
#df.columns=['areaId','areaName','parkName','totalSpace','surplusSpace''payGuide','introduction','address','wgsX','wgsY','parkId','charge']
areaId,areaName,parkName,totalSpace,surplusSpace,payGuide,introduction,address,wgsX,wgsY,parkId = [],[],[],[],[],[],[],[],[],[],[]
df = load_data_json()
charge_df =load_data_excel()

for info in df['parkingLots']:
    areaId.append(info['areaId'])
    areaName.append(info['areaName'])
    parkName.append(info['parkName'])
    totalSpace.append(info['totalSpace'])
    surplusSpace.append(info['surplusSpace'])
    payGuide.append(info['payGuide'])
    introduction.append(info['introduction'])
    address.append(info['address'])
    wgsX.append(info['wgsX'])
    wgsY.append(info['wgsY'])
    parkId.append(info['parkId'])

df1 = pd.DataFrame([areaId,
                    areaName,
                    parkName,
                    totalSpace,
                    surplusSpace,
                    payGuide,
                    introduction,
                    address,
                    wgsX,
                    wgsY,
                    parkId]).T
df1.columns = info_column



charge_df = pd.DataFrame(charge_df['charge'])

df1 = df1.merge(charge_df, how = 'inner', left_index=True, right_index=True) #將兩資料表合併

ops_set = set(df1['areaId'])            #set內容不重複
ops1_set = set(df1['areaName'])
ops_list = list(ops_set)            #各區域選擇
ops1_list = list(ops1_set)
pos_x = 121.2647505
pos_y = 24.9702161

Modes = ['Local','District']
df1['Url'] = ''
#位址網址https://www.google.com.tw/maps/@24.9702161,121.2647505,18z?hl=zh-TW

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""<style>
        .css-d1b1ld.edgvbvh6{
            position: relative;
            top:60px;
        }
        .css-1pd56a0.e1tzin5v4{
            position: relative;
            top:20px;
        }
        </style>""", unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="" target="_blank">桃園車位搜尋系統</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" target="_blank">Logout</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://data.gov.tw/dataset/25940" target="_blank">資料來源</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


df2 = pd.DataFrame(
     np.random().randn(1000, 2) + [23.5, 121.5],
     columns=['lat', 'lon'])


layout = st.container()
output = st.empty()

with layout:
    st.title("Parking lot Searching System")
    st.header("PK_dataframe")
output.text("Waiting for your selection......")
form = st.sidebar.form("my_form")
with form:
    Mode = form.radio('SearchMode',Modes)
    AreaName = form.selectbox("District",ops1_list)
    Search_Range = (form.number_input("Input your standard (km)",step=1,format="%d"))/100
    Price = form.slider("Price",min_value=0,max_value=60)
    submitted = st.form_submit_button("Search")
    map = st.sidebar.checkbox("顯示地圖")
    if submitted and Mode == 'District':        #地區式搜尋
        df1 = df1.loc[df1['areaName'] == AreaName]
    elif submitted and Mode == 'Local':         #定位式搜尋
        df1 = df1.loc[(df1['wgsX'] <= (pos_x + Search_Range))]
        df1 = df1.loc[(df1['wgsX'] >= (pos_x - Search_Range))]
        df1 = df1.loc[(df1['wgsY'] <= (pos_y + Search_Range))]
        df1 = df1.loc[(df1['wgsY'] >= (pos_y - Search_Range))]
if submitted:
    if Price != 0:
        df1 = df1.loc[(df1['charge'] <= Price)]
    output.empty()
    output = st.dataframe(df1[['areaName','parkName','surplusSpace','address','charge','Url']])
if map:
    st.map(df2)
