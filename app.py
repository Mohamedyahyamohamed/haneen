import streamlit as st
import time

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="قصتنا", page_icon="❤️", layout="centered")

# 2. ستايل الصفحة عشان الكلام يكون في النص وشكله حلو
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #e91e63;
        font-family: 'Arial', sans-serif;
    }
    .emoji-big {
        text-align: center;
        font-size: 120px !important;
        margin: 20px 0px;
    }
    .result-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان
st.markdown("<h1 class='main-title'>قصتنا في أرقام ❤️</h1>", unsafe_allow_html=True)
st.write("---")

# 4. المدخلات (خليناها Sliders عشان شكلها أحلى في الاستخدام زي الفيديوهات)
col1, col2 = st.columns(2)
with col1:
    fights = st.slider("عدد الخناقات 🥊", min_value=0, max_value=500, value=15)
with col2:
    problems = st.slider("عدد المشاكل 🌪️", min_value=0, max_value=500, value=30)

st.write("---")

# 5. الزرار اللي بيبدأ الأنيميشن
if st.button("احسب قوة علاقتنا 💪", use_container_width=True):
    
    # بنعمل مكان فاضي في الصفحة عشان نعرض فيه الأنيميشن خطوة بخطوة
    animation_space = st.empty()
    
    # المرحلة الأولى: القلب مكسور
    with animation_space.container():
        st.info("جاري تحليل العلاقة وكمية المشاكل...")
        st.markdown("<div class='emoji-big'>💔</div>", unsafe_allow_html=True)
        time.sleep(2) # بنستنى ثانيتين
        
    # المرحلة التانية: القلب بيتعالج
    with animation_space.container():
        st.warning("بنعالج الجروح والخناقات اللي فاتت...")
        st.markdown("<div class='emoji-big'>❤️‍🩹</div>", unsafe_allow_html=True)
        time.sleep(2)
        
    # المرحلة التالتة: القلب رجع سليم
    with animation_space.container():
        st.success("الحب بيكبر وبيقوى...")
        st.markdown("<div class='emoji-big'>❤️</div>", unsafe_allow_html=True)
        time.sleep(2)
        
    # بنفضي المكان عشان نعرض النتيجة النهائية
    animation_space.empty()
    
    # 6. النتيجة النهائية
    st.balloons() # بلالين بتطير على الشاشة
    
    st.markdown("<div class='emoji-big'>💎</div>", unsafe_allow_html=True)
    st.markdown(f"<p class='result-text'>بعد {fights} خناقة و {problems} مشكلة..<br>قلبنا بقى صلب زي الألماس ومفيش أي حاجة تقدر تكسره!</p>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h2 class='main-title'>صورتنا مع بعض 👩‍❤️‍👨</h2>", unsafe_allow_html=True)
    
    # 7. صورتكم 
    # امسح الرابط ده واكتب مكانه اسم صورتكم (مثلاً "image.png")
    image_path = "https://via.placeholder.com/600x400.png?text=Your+Photo+Here"
    
    try:
        st.image(image_path, use_container_width=True)
    except:
        st.error("مش قادر ألاقي الصورة.. اتأكد إنك كاتب اسمها صح وحاططها في نفس الفولدر.")


