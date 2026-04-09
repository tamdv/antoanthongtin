from flask import Flask, request, render_template, redirect, url_for, flash
import psycopg2
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_demo'

# Kết nối cơ sở dữ liệu (Vulnerable: Kết nối trực tiếp, không cấu hình Pooling tốt)
def get_db_connection():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    return conn

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # [VULNERABLE] SQL Injection & Plaintext Comparison
        # Lỗi: Nối chuỗi trực tiếp vào câu lệnh SQL
        conn = get_db_connection()
        cur = conn.cursor()
        
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}") # In ra để demo lúc thuyết trình
        
        cur.execute(query)
        user = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if user:
            return f"<h1>Chào mừng {user[3]}!</h1><p>Bạn đã đăng nhập thành công.</p>"
        else:
            flash('Tài khoản hoặc mật khẩu không đúng!', 'danger')
            
    return render_template('login.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
