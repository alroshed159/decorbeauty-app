import streamlit as st

st.title("🎨 ديكور بيوتي")
st.write("مرحبًا بك في تطبيق ديكور بيوتي لتجربة الذكاء الاصطناعي في التصميم!")

style = st.selectbox("اختر النمط:", ["كلاسيك", "مودرن", "بوهو", "إسكندنافي"])
color = st.color_picker("اختر لونك المفضل")

if st.button("اقتراح تصميم"):
    st.success(f"🎉 نقترح عليك تصميم {style} بألوان {color}")
