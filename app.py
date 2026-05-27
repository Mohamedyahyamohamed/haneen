
import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="قصتنا", page_icon="🖤", layout="centered")

# 2. ستايل الصفحة (عشان نخليها سودة بالكامل وتدي نفس شكل الفيديو)
st.markdown("""
    <style>
    /* تغيير لون الخلفية للأسود */
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
        color: white;
    }
    /* إخفاء شريط ستريم ليت العلوي عشان يبان كأنه فيديو */
    [data-testid="stHeader"] {
        background-color: transparent;
    }
    
    /* ستايل الجملة اللي فوق */
    .quote-text {
        text-align: center;
        font-size: 28px;
        color: #e0e0e0;
        font-family: 'Arial', sans-serif;
        margin-top: 40px;
        margin-bottom: 20px;
        direction: rtl;
        text-shadow: 0px 0px 5px #ffffff;
    }
    
    /* ستايل جملة "أنا وهو" */
    .me-and-him {
        text-align: right;
        font-size: 22px;
        color: #ffffff;
        font-weight: bold;
        background: rgba(255,255,255,0.15);
        padding: 5px 15px;
        border-radius: 12px;
        display: inline-block;
        direction: rtl;
        margin-top: 10px;
    }
    
    /* القلب المكسور */
    .heart-broken {
        text-align: center;
        font-size: 140px !important;
        color: #555;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
        margin: 30px 0;
    }
    
    /* القلب السليم اللي بينور */
    .heart-glowing {
        text-align: center;
        font-size: 150px !important;
        animation: pulse 1.5s infinite;
        margin: 30px 0;
    }
    
    /* حركة النبض والنور الأحمر زي الفيديو */
    @keyframes pulse {
        0% { transform: scale(1); text-shadow: 0 0 20px #ff0000; }
        50% { transform: scale(1.05); text-shadow: 0 0 50px #ff0000, 0 0 80px #ff0000; }
        100% { transform: scale(1); text-shadow: 0 0 20px #ff0000; }
    }
    </style>
""", unsafe_allow_html=True)

# 3. عرض الجملة الدرامية اللي في الفيديو
st.markdown('<p class="quote-text">شوية مشاكل بيناتهم ويتفارقو</p>', unsafe_allow_html=True)

# 4. مكان القلب 
heart_placeholder = st.empty()

# في البداية بنعرض القلب المكسور
heart_placeholder.markdown('<div class="heart-broken">💔</div>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# 5. زرار بيبدأ الحركة (عشان نثبت العكس)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    start_animation = st.button("اثبتلهم العكس ❤️", use_container_width=True)

if start_animation:
    # حركة العلاج
    heart_placeholder.markdown('<div class="heart-broken" style="font-size: 130px !important;">❤️‍🩹</div>', unsafe_allow_html=True)
    time.sleep(1.5)
    
    # القلب بينور وبينبض
    heart_placeholder.markdown('<div class="heart-glowing">❤️</div>', unsafe_allow_html=True)
    time.sleep(1)
    
    # ظهور جملة "أنا وهو"
    st.markdown('<div style="text-align: right;"><div class="me-and-him">أنا وهو ∞❤️</div></div>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # عرض الصورة 
    try:
        # عرض الصورة المرفوعة
        st.image("pic.jpeg", use_container_width=True)
    except:
        st.info("عشان تكمل الفرحة: اتأكد إن صورتكم مرفوعة في نفس المكان على GitHub واسمها pic.jpeg بالظبط ✨")


