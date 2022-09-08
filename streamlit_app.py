import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('meb_pic.jpg'))

st.header('Meb Shop')

st.info('🥣 คอร์นเฟลกคาราเมล 🥣  🍪ซอฟต์คุกกี้ 🍪 อบสดๆใหม่ๆทุกครั้งที่ส่งเลยน้าา')

icon_size = 20

st_button('twitter', 'https://twitter.com/meb_shoppp?s=20&t=fmyjrA_YPXAMsFqjpyFYqQ', 'Follow me on Twitter', icon_size)
st_button('facebook', 'https://www.facebook.com/meb.shoppp/', 'Follow me on Facebook', icon_size)
st_button('instagram', 'https://www.instagram.com/meb.bakery/?igshid=NmNmNjAwNzg%3D&fbclid=IwAR3BQZPlqtnmStk7eKMiiP80ef4wDbWYfXEyxjbt8tV9hLzY-T2x328d9FA', 'Follow me on Instagram', icon_size)
