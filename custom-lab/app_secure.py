from flask import Flask, request, render_template, redirect, url_for, flash, session
import psycopg2
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import random
import pyotp
import re

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_secure_demo'

# Khởi tạo các công cụ bảo mật
bcrypt = Bcrypt(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

def is_password_strong(password):
    """[SECURE] Kiểm tra độ mạnh mật khẩu (Password Policy)"""
    if len(password) < 8: return False
    if not re.search("[a-z]", password): return False
    if not re.search("[A-Z]", password): return False
    if not re.search("[0-9]", password): return False
    return True

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute") # [SECURE] Chống Brute Force bằng Rate Limiting
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        captcha_input = request.form.get('captcha')
        mfa_code = request.form.get('mfa_code')
        
        # 1. [SECURE] Kiểm tra CAPTCHA (Chống Auto-Bot)
        if not captcha_input or int(captcha_input) != session.get('captcha_result'):
            flash('Mã CAPTCHA không chính xác!', 'danger')
            return redirect(url_for('login'))
        
        # 2. [SECURE] Kiểm tra Password Policy (Demo cảnh báo)
        if not is_password_strong(password):
            flash('Cảnh báo: Mật khẩu của bạn quá yếu theo chính sách mới!', 'warning')

        conn = get_db_connection()
        cur = conn.cursor()
        
        # 3. [SECURE] Truy vấn từ bảng users_secure (Parameterized Query)
        query = "SELECT password, full_name, mfa_secret FROM users_secure WHERE username = %s"
        cur.execute(query, (username,))
        user_data = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if user_data:
            stored_hash = user_data[0]
            full_name = user_data[1]
            mfa_secret = user_data[2]
            
            # 4. [SECURE] Kiểm tra mật khẩu (Bcrypt Hashing)
            if bcrypt.check_password_hash(stored_hash, password):
                
                # 5. [SECURE] Kiểm tra MFA nếu tài khoản đã kích hoạt
                if mfa_secret:
                    totp = pyotp.TOTP(mfa_secret)
                    if not mfa_code or not totp.verify(mfa_code):
                        flash('Mã xác thực MFA không chính xác!', 'danger')
                        return redirect(url_for('login'))
                
                # Đăng nhập thành công
                session.pop('captcha_result', None) # Xóa captcha cũ
                return f"<h1>Chào mừng {full_name}!</h1><p>Bạn đã vượt qua 3 lớp phòng thủ (Pass + CAPTCHA + MFA).</p>"
        
        flash('Đăng nhập thất bại. Vui lòng kiểm tra lại!', 'danger')
            
    # Tạo CAPTCHA mới cho mỗi lần load trang
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    session['captcha_result'] = a + b
    captcha_text = f"{a} + {b} = ?"
            
    return render_template('login.html', captcha_text=captcha_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

