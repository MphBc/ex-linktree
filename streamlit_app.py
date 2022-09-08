import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('meb_pic.jpg'))

st.header('Meb Shoppp')

st.info('🥣 คอร์นเฟลกคาราเมล 🥣  🍪ซอฟต์คุกกี้ 🍪 อบสดๆใหม่ๆทุกครั้งที่ส่งเลยน้าา')

icon_size = 20

st_button('twitter', 'https://twitter.com/meb_shoppp?s=20&t=fmyjrA_YPXAMsFqjpyFYqQ', 'Twitter', icon_size)
st_button('facebook', 'https://www.facebook.com/meb.shoppp/', 'Facebook', icon_size)
st_button('instagram', 'https://www.instagram.com/meb.bakery/?igshid=NmNmNjAwNzg%3D&fbclid=IwAR3BQZPlqtnmStk7eKMiiP80ef4wDbWYfXEyxjbt8tV9hLzY-T2x328d9FA', 'Instagram Bakery', icon_size)
st_button('instagram', 'https://www.instagram.com/meb_shoppp/?igshid=NmNmNjAwNzg%3D&fbclid=IwAR0PwP_ns38vNHekGW1hXSNreHRARH9k2fYoxVvE0ZFwjAfwWyqcXDFeG1k', 'Instagram Meb shoppp', icon_size)
st_button('line', 'https://line.me/R/ti/p/@638itmws', 'Line official', icon_size)
