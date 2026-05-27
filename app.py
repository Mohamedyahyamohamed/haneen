```python
import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="رحلة قلبنا", page_icon="💖", layout="centered")

# إضافة ستايل بسيط باستخدام CSS
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        text-align: center;
        color: #ff4b4b;
    }
    .heart-icon {
        font-size: 80px !important;
        text-align: center;
        animation: pulse 1s infinite;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">رحلة قلبنا: من التحديات للصلابة 💎</p>', unsafe_allow_html=True)
st.write("---")

st.write("### حدد التحديات اللي مرينا بيها:")

# تقسيم الشاشة لعمودين عشان شكل المدخلات يكون أحلى
col1, col2 = st.columns(2)

with col1:
    problems = st.number_input("عدد المشاكل 🌪️", min_value=0, max_value=1000, value=10)

with col2:
    fights = st.number_input("عدد الخناقات 🥊", min_value=0, max_value=1000, value=5)

st.write("---")

# الزرار اللي بيبدأ الرحلة
if st.button("شوف إيه اللي حصل لقلبنا ❤️", use_container_width=True):
    total_hardships = problems + fights
    
    if total_hardships == 0:
        st.warning("حياتكم هادية جداً! مفيش تحديات تقوي القلب لسه 😂")
    else:
        # شريط التحميل للمحاكاة
        progress_text = "بنعالج المشاكل وبنعدي الخناقات..."
        my_bar = st.progress(0, text=progress_text)
        
        # مكان فاضي هنغير فيه شكل القلب
        heart_placeholder = st.empty()
        
        # محاكاة مرور الوقت وتأثير المشاكل على القلب
        for percent_complete in range(100):
            time.sleep(0.04) # للتحكم في سرعة التحميل
            my_bar.progress(percent_complete + 1, text=progress_text)
            
            # تغيير شكل القلب بناءً على التقدم (مرحلة الصلابة)
            if percent_complete < 25:
                heart_placeholder.markdown('<div class="heart-icon">💔</div>', unsafe_allow_html=True)
            elif percent_complete < 50:
                heart_placeholder.markdown('<div class="heart-icon">❤️‍🩹</div>', unsafe_allow_html=True)
            elif percent_complete < 75:
                heart_placeholder.markdown('<div class="heart-icon">❤️</div>', unsafe_allow_html=True)
            else:
                heart_placeholder.markdown('<div class="heart-icon">💎</div>', unsafe_allow_html=True)
        
        # إخفاء شريط التحميل والقلب المتحرك بعد الانتهاء
        my_bar.empty()
        heart_placeholder.empty()
        
        # رسالة النجاح
        st.success(f"بعد {problems} مشكلة و {fights} خناقة.. قلبنا مبقاش مجرد قلب، ده بقى أصلب من الألماس ومفيش حاجة تكسره! 💎")
        st.balloons() # تأثير احتفالي لطيف
        
        st.markdown("<h3 style='text-align: center;'>وفي النهاية، دي النتيجة الحلوة بتاعتنا 👇</h3>", unsafe_allow_html=True)
        
        # عرض صورتكم (يجب تغيير الرابط بمسار الصورة الحقيقية)
        # تقدر تحط مسار صورة من جهازك زي: "my_photo.jpg" 
        image_path = "https://via.placeholder.com/800x500.png?text=%D8%B5%D9%88%D8%B1%D8%AA%D9%86%D8%A7+%D9%85%D8%B9+%D8%A8%D8%B9%D8%B6+%D9%87%D9%86%D8%A7" 
        
        st.image(image_path, caption="أنا وأنت ضد الدنيا ❤️", use_container_width=True)
        
        st.info("💡 عشان تظهر صورتكم الحقيقية: افتح الكود، وامسح الرابط اللي في متغير `image_path` واكتب مكانه اسم صورتكم (مثلاً 'our_pic.jpg') وحط الصورة في نفس الفولدر اللي فيه الكود.")

```
