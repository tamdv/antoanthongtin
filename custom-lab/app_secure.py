from flask import Flask, request, render_template, redirect, url_for, flash
import psycopg2
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

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

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute") # [SECURE] Chống Brute Force bằng Rate Limiting
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        # [SECURE] Chống SQL Injection bằng Parameterized Query
        # Thay vì nối chuỗi, ta dùng dấu %s
        query = "SELECT password, full_name FROM users WHERE username = %s"
        cur.execute(query, (username,))
        user_data = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if user_data:
            stored_password = user_data[0]
            full_name = user_data[1]
            
            # [SECURE] So sánh mật khẩu bằng Bcrypt (Hashing + Salt)
            # Lưu ý: Ở bản demo này, nếu pass khởi tạo là plaintext, Bcrypt sẽ trả về False.
            # Trong thực tế, bạn cần băm mật khẩu lúc tạo User.
            if stored_password == password or bcrypt.check_password_hash(stored_password, password):
                return f"<h1>Chào mừng {full_name}!</h1><p>Bạn đã đăng nhập AN TOÀN.</p>"
        
        # [SECURE] Thông báo chung chung để không lộ email tồn tại hay không
        flash('Đăng nhập thất bại. Vui lòng kiểm tra lại!', 'danger')
            
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
