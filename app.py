import streamlit as st
import pandas as pd
import os

# تحميل بيانات الألوان
df = pd.read_json("colors_metadata_with_names.json")

# إعداد الواجهة
st.set_page_config(page_title="مساعد ديكور بيوتي", layout="wide")
st.title("🎨 مساعد ديكور بيوتي الذكي")

# اختيار النمط
style = st.selectbox("اختر النمط المفضل", ["مودرن", "كلاسيك", "تراثي"])

# اختيار اللون المفضل
color_name = st.selectbox("اختر لونك المفضل", df["name"])

# عرض بيانات اللون المختار
selected_row = df[df["name"] == color_name].iloc[0]
st.markdown(f"### اللون المختار: {selected_row['name']} ({selected_row['code']})")

# ✅ تصحيح امتداد الصورة: نحول الاسم إلى حروف صغيرة
filename = selected_row["filename"].lower()
image_path = os.path.join("colors", filename)

# عرض صورة اللون
st.image(image_path, width=300, caption=filename)

# إدخال مساحة التصميم
area = st.number_input("أدخل مساحة الجدار (بالمتر المربع):", min_value=1, step=1)

# حساب تكلفة تقديرية (سعر رمزي تجريبي)
estimated_price = area * 125  # نفترض 125 ريال/م2 كمثال
st.markdown(f"💰 **التكلفة التقديرية:** {estimated_price:,.0f} ريال")

# عرض لون متناسق بشكل تجريبي (عشوائي من نفس المجموعة)
similar_colors = df[df["name"] != selected_row["name"]].sample(1)
similar_filename = similar_colors.iloc[0]["filename"].lower()

st.markdown("### 🎯 لون ثانٍ متناسق مقترح:")
st.image(os.path.join("colors", similar_filename), width=200,
         caption=f"{similar_colors.iloc[0]['name']} ({similar_colors.iloc[0]['code']})")