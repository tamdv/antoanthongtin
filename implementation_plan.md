# Kế hoạch Triển khai Báo cáo Tiểu luận (Học phần ATTT - Thạc sĩ HTTT)

Tài liệu này đề xuất cấu trúc và nội dung chi tiết cho bài báo cáo tiểu luận, tập trung vào việc tích hợp các kiến thức lý thuyết đã học (Chương 1-6) vào hệ thống thực nghiệm tự xây dựng (Custom Web App).

## 1. Mục tiêu Báo cáo
- Hệ thống hóa kiến thức về tấn công và phòng thủ xác thực Web.
- Chứng minh khả năng xây dựng và triển khai hệ thống thực nghiệm an toàn.
- Đánh giá hiệu quả của các biện pháp phòng thủ (Bcrypt, Rate Limiting, MFA).

## 2. Cấu trúc Báo cáo dự kiến (Table of Contents)

### Lời mở đầu
- Lý do chọn đề tài (Tính cấp thiết của bảo mật xác thực trong kỷ nguyên số).
- Mục tiêu và đối tượng nghiên cứu (Tấn công Brute Force, Dictionary, Credential Stuffing).
- Phương pháp nghiên cứu (Xây dựng Lab thực nghiệm, so sánh đối chiếu).

### Chương 1: Cơ sở lý thuyết về An toàn Thông tin Xác thực
- **1.1. Các đặc tính an toàn thông tin cốt lõi (CIA, Authenticity, Accountability).**
- **1.2. Tổng quan về các lỗ hổng xác thực Web (OWASP Top 10).**
- **1.3. Phân loại các phương thức phá mã mật khẩu.**
  - 1.3.1. Brute Force (Vét cạn).
  - 1.3.2. Dictionary Attack (Từ điển).
  - 1.3.3. Credential Stuffing (Sử dụng dữ liệu rò rỉ).

### Chương 2: Mô hình và Môi trường Thực nghiệm
- **2.1. Kiến trúc hệ thống Lab tự xây dựng (Custom Web App).**
  - Backend: Flask; Database: PostgreSQL; Containerization: Docker.
- **2.2. Thiết kế mô hình "Vulnerable App" (Lỗ hổng mặc định).**
- **2.3. Thiết kế mô hình "Secure App" (Giải pháp an toàn).**

### Chương 3: Thực thi Tấn công và Phân tích Lỗ hổng
- **3.1. Triển khai tấn công SQL Injection (Bypass Authentication).**
- **3.2. Triển khai tấn công Brute Force & Dictionary trên bản Vulnerable.**
- **3.3. Triển khai tấn công Credential Stuffing.**
- **3.4. Phân tích nguyên nhân gốc rễ của các lỗ hổng.**

### Chương 4: Giải pháp Phòng thủ và Đánh giá Thực nghiệm
- **4.1. Cơ chế Lưu trữ mật khẩu an toàn (Password Hashing với Bcrypt).**
- **4.2. Cơ chế Chặn tấn công tự động (Rate Limiting với Flask-Limiter).**
- **4.3. Xác thực đa yếu tố (TOTP/MFA) và CAPTCHA.**
- **4.4. So sánh kết quả: Vulnerable vs Secure.**

### Chương 5: Đề xuất Chính sách và Kết luận
- **5.1. Xây dựng Password Policy cho tổ chức (Tham chiếu Chương 6).**
- **5.2. Kết luận và định hướng phát triển (WAF, IDS/IPS).**

## 3. Các đầu mục công việc tiếp theo
1.  [ ] Viết nội dung chi tiết cho Chương 1-2 (Dựa trên `summaries.md`).
2.  [ ] Tổng hợp hình ảnh/code demo cho Chương 3-4 (Dựa trên `app.py`, `app_secure.py`).
3.  [ ] Xây dựng bảng so sánh kết quả tấn công thực tế.

> [!IMPORTANT]
> **Câu hỏi cho người dùng:** 
> - Bạn có muốn tôi tập trung sâu hơn vào phần nào (Ví dụ: Mã hóa Bcrypt hay Cơ chế chặn IP)?
> - Bạn có cần tôi hỗ trợ viết nội dung chi tiết cho từng chương ngay bây giờ không?
