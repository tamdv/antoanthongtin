#!/bin/bash

# Thư mục hiện tại
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "------------------------------------------------"
echo "Khởi động Lab An Toàn Thông Tin (Port 5005)"
echo "------------------------------------------------"

# Kiểm tra xem venv có tồn tại không
if [ ! -d "venv" ]; then
    echo "Đang tạo môi trường ảo (venv)..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Dừng các tiến trình cũ nếu có (dựa trên port 5005)
PID=$(lsof -t -i:5005)
if [ ! -z "$PID" ]; then
    echo "Đang dừng tiến trình cũ trên port 5005 (PID: $PID)..."
    kill -9 $PID
fi

# Chạy Flask app trên port 5005
echo "Đang khởi động ứng dụng..."
export PORT=5005
export DATABASE_URL="postgresql://user_attt:password_secret@localhost:5432/user_management"

# Lưu ý: file app.py kết nối DB qua DATABASE_URL
# Nếu bạn chạy DB bằng Docker (port 5433 mapping sang 5432)
# Hãy đảm bảo container 'custom_lab_db' đang chạy.

python3 app.py > app.log 2>&1 &
echo $! > app.pid

echo "✅ Ứng dụng đã được khởi động trên: http://localhost:5005/login"
echo "Logs được ghi vào: app.log"
echo "Để dừng ứng dụng, hãy chạy lệnh: kill \$(cat app.pid)"
echo "------------------------------------------------"
