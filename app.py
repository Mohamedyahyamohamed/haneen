import streamlit as st
import base64
import os

# --- إعدادات الصفحة ---
st.set_page_config(page_title="سؤال من القلب ❤️", page_icon="💍", layout="centered")

# --- دالة لتحويل الصورة ---
def get_image_as_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        return None

current_dir = os.path.dirname(os.path.abspath(__file__))

# الكود هيبحث بنفسه عن أي ملف صورته اسمه pic بغض النظر عن امتداده
image_path = None
for file in os.listdir(current_dir):
    if "pic" in file.lower() and file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(current_dir, file)
        break

if image_path:
    img_base64 = get_image_as_base64(image_path)
else:
    img_base64 = None

if img_base64 is None:
    st.error(f"⚠️ مفيش أي صورة اسمها pic خالص في الفولدر ده: {current_dir}")
else:
    # --- كود HTML و CSS و JS (النسخة الكريتف) ---
    html_code = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;900&display=swap');
            
            body {{
                font-family: 'Tajawal', sans-serif;
                background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
                margin: 0;
                padding: 0;
                text-align: center;
                overflow: hidden;
                border-radius: 20px;
                height: 100vh;
            }}
            
            .heart-bg {{
                position: absolute;
                font-size: 24px;
                color: rgba(255, 255, 255, 0.6);
                animation: float 4s ease-in infinite;
                z-index: 0;
            }}
            @keyframes float {{
                0% {{ transform: translateY(100vh) scale(0); opacity: 1; }}
                100% {{ transform: translateY(-10vh) scale(1.5); opacity: 0; }}
            }}

            #main-card {{
                background: rgba(255, 255, 255, 0.9);
                padding: 40px 20px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(233, 30, 99, 0.2);
                max-width: 500px;
                margin: 60px auto;
                position: relative;
                z-index: 10;
                height: 400px;
            }}

            .question-title {{
                font-size: 30px;
                color: #d81b60;
                margin-bottom: 10px;
                font-weight: 900;
            }}
            
            .question-subtitle {{
                font-size: 20px;
                color: #555;
                margin-bottom: 40px;
                font-weight: 700;
            }}

            .buttons-area {{
                position: relative;
                width: 100%;
                height: 250px;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .btn {{
                font-family: 'Tajawal', sans-serif;
                font-size: 20px;
                padding: 12px 30px;
                border: none;
                border-radius: 50px;
                cursor: pointer;
                font-weight: bold;
                color: white;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
                white-space: nowrap;
            }}

            #btn-yes {{
                background: linear-gradient(45deg, #4CAF50, #81C784);
                margin-left: 20px;
                z-index: 20;
            }}

            #btn-yes:hover {{
                transform: scale(1.1);
                box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
            }}

            #btn-no {{
                background: linear-gradient(45deg, #f44336, #e57373);
                position: absolute;
                left: 60%;
                top: 40%;
                z-index: 20;
            }}

            #success-container {{
                display: none;
                text-align: center;
                background: rgba(255, 255, 255, 0.95);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(233, 30, 99, 0.3);
                max-width: 500px;
                margin: 20px auto;
                animation: popIn 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                position: relative;
                z-index: 10;
            }}

            #success-container img {{
                max-width: 90%;
                max-height: 350px;
                border-radius: 15px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                margin-top: 20px;
                border: 5px solid #ff9a9e;
            }}

            .love-text {{
                font-size: 32px;
                color: #d81b60;
                margin-top: 10px;
                font-weight: 900;
            }}

            @keyframes popIn {{
                0% {{ transform: scale(0.5); opacity: 0; }}
                100% {{ transform: scale(1); opacity: 1; }}
            }}
        </style>
    </head>
    <body>
        <div class="heart-bg" style="left: 10%; animation-duration: 3s;">❤️</div>
        <div class="heart-bg" style="left: 30%; animation-duration: 5s;">💖</div>
        <div class="heart-bg" style="left: 50%; animation-duration: 4s;">✨</div>
        <div class="heart-bg" style="left: 70%; animation-duration: 6s;">💍</div>
        <div class="heart-bg" style="left: 90%; animation-duration: 3.5s;">💕</div>

        <div id="main-card">
            <div class="question-title">أنا عندي سؤال مهم جداً...</div>
            <div class="question-subtitle">تتجوزيني وتكملي معايا الباقي من عمري؟ 💍❤️</div>
            
            <div class="buttons-area">
                <button class="btn" id="btn-yes" onclick="sayYes()">أيوة طبعاً!</button>
                <button class="btn" id="btn-no" onmouseover="moveButton()" ontouchstart="moveButton()">لأ</button>
            </div>
        </div>

        <div id="success-container">
            <div class="love-text">بحبك يا أحلى حاجة في حياتي! ❤️</div>
            <div style="font-size: 18px; color: #555;">ربنا يخليكي ليا وميحرمنيش منك أبداً</div>
            <img src="data:image/jpeg;base64,{img_base64}" alt="صورتنا الحلوة">
        </div>

        <script>
            const noBtn = document.getElementById('btn-no');
            
            // 👇 هنا كترتلك الجمل وخليتها بتضحك جداً
            const funnyTexts = [
                'لأ', 
                'متهزريش!', 
                'فكرى تاني!', 
                'قولي أيوة أحسنلك', 
                'مفيش هروب!',
                'الزرار ده بايظ على فكرة',
                'مش هتلحقيني',
                'طب عشان خاطري؟',
                'هتفضلي تجري ورايا كتير؟',
                'أنا صبور جداً عادي',
                'دوسى أيوة وريحي نفسك',
                'يا بنتي اتهدي بقى',
                'عاجبك الماوس وهو بيجري؟',
                'طب والله بحبك',
                'مفيش اختيارات تانية',
                'هتتجوزيني يعني هتتجوزيني',
                'خلاص بقى خليكي عاقلة',
                'ايدي وجعتني من الجري',
                'هعد لحد تلاتة...',
                'برضه مش هتدوسي!'
            ];
            let textIndex = 0;

            function moveButton() {{
                const area = document.querySelector('.buttons-area');
                const areaRect = area.getBoundingClientRect();
                
                const maxX = areaRect.width - noBtn.offsetWidth;
                const maxY = areaRect.height - noBtn.offsetHeight;
                
                const randomX = Math.floor(Math.random() * maxX);
                const randomY = Math.floor(Math.random() * maxY);
                
                noBtn.style.left = randomX + 'px';
                noBtn.style.top = randomY + 'px';
                
                textIndex = (textIndex + 1) % funnyTexts.length;
                noBtn.innerText = funnyTexts[textIndex];
            }}

            function sayYes() {{
                document.getElementById('main-card').style.display = 'none';
                document.getElementById('success-container').style.display = 'block';
                
                for(let i=0; i<15; i++) {{
                    let heart = document.createElement('div');
                    heart.innerHTML = (i % 2 === 0) ? '🎉' : '❤️';
                    heart.className = 'heart-bg';
                    heart.style.left = Math.random() * 100 + '%';
                    heart.style.animationDuration = (Math.random() * 3 + 2) + 's';
                    document.body.appendChild(heart);
                }}
            }}
        </script>
    </body>
    </html>
    """

    st.components.v1.html(html_code, height=750)