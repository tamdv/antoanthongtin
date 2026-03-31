# Kế hoạch Bài tập nhóm: Tấn công Password & Phòng thủ xác thực Web

**Chủ đề:** Tấn công Password & Phòng thủ xác thực Web (Brute force, Dictionary, Credential Stuffing)
**Nhóm thực hiện (4 người):** Tâm, Trung, Tùng, Dũng.

---

## 1. Kịch bản (The Storytelling Concept)
**"Vụ án: Lỗ hổng sau cánh cửa đăng nhập"**
*   **Mở đầu:** Một startup thương mại điện tử vừa bị rò rỉ cơ sở dữ liệu khách hàng.
*   **Diễn biến:** Nhóm đóng vai 2 bên: 
    *   **Đội Tấn công (Red Team):** Thực hiện các đòn đánh vào trang login để chiếm quyền điều khiển tài khoản Admin.
    *   **Đội Phòng thủ (Blue Team):** Phát hiện, phân tích và triển khai các lớp phòng vệ (MFA, Rate Limiting, Hashing, Web Application Firewall).
*   **Kết thúc:** Bài học rút ra về sự cân bằng giữa bảo mật và trải nghiệm người dùng.

---

## 2. Phân công công việc (Roles & Responsibilities)

| Thành viên | Vai trò chính | Nhiệm vụ cụ thể |
| :--- | :--- | :--- |
| **Trung (Team Leader)** | **Atacker (Red Team)** | Thực hiện Brute Force và Dictionary Attack. Chuẩn bị wordlist (từ điển mật khẩu). |
| **Dũng** | **Atacker (Red Team)** | Thực hiện Credential Stuffing (sử dụng dữ liệu rò rỉ từ nguồn khác). Demo các công cụ tự động. |
| **Tâm** | **Defender (Blue Team)** | Xây dựng hệ thống Lab, cấu hình các lớp phòng thủ (MFA, CAPTCHA, Password Policy). |
| **Tùng** | **Analyst & Presenter** | Phân tích cơ chế mã hóa (hashing), ghi log (System Audit). Biên tập nội dung slide và thuyết trình. |

---

## 3. Bảng công việc chi tiết (Task Table)

| STT | Hạng mục công việc | Công cụ (Tools) | Cách làm (Methodology) | Thành viên |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Xây dựng Lab & Target** | **DVWA, OWASP Juice Shop** | Cài đặt Docker/VMWARE để chạy các ứng dụng Web có lỗ hổng (Vulnerable Apps). | **Tâm** |
| **2** | **Brute Force & Dictionary Attack** | **Burp Suite Intruder, Hydra** | Bắt gói tin login, thử nghiệm các tổ hợp mật khẩu từ wordlist (rockyou.txt). | **Trung** |
| **3** | **Credential Stuffing** | **Sentry MBA, Python Script** | Giả lập kịch bản dùng combo (email:pass) rò rỉ để đăng nhập loạt vào hệ thống mới. | **Dũng** |
| **4** | **Phòng thủ mức ứng dụng** | **Google reCAPTCHA, Google Authenticator** | Tích hợp CAPTCHA và MFA (xác thực đa yếu tố) vào trang login. | **Tâm** |
| **5** | **Cơ chế Hashing & Policy** | **PHP/Python (Bcrypt), Policy Manager** | Demo sự khác biệt giữa lưu mật khẩu thuần túy vs Hashing + Salting. Thiết lập chính sách mật khẩu mạnh. | **Tùng** |
| **6** | **Giám sát & Ngăn chặn** | **Fail2Ban, ModSecurity (WAF)** | Cấu hình chặn IP sau 5 lần đăng nhập sai (Lockout/Rate Limiting). Theo dõi logs truy cập. | **Tâm + Tùng** |
| **7** | **Tổng hợp & Thuyết trình** | **PowerPoint, Canva** | Viết kịch bản kể chuyện, quay video demo, tổng kết kiến thức từ Chương 1-6 đã học. | **Tùng + Trung** |

---

## 4. Cấu trúc bài thuyết trình (Presentation Outline)

1.  **Chương 1: Mở màn (The Incident):** Giới thiệu vụ rò rỉ dữ liệu giả lập (Kết nối kiến thức Chương 1: Tổng quan ATTT).
2.  **Chương 2: Đột nhập (The Attack):**
    *   Demo Brute Force/Dictionary Attack (Sử dụng kiến thức Chương 3: Các dạng tấn công).
    *   Giải thích cơ chế Credential Stuffing.
3.  **Chương 3: Phân tích (The Analysis):**
    *   Tại sao mật khẩu yếu lại dễ bị phá?
    *   Tầm quan trọng của Hashing & Salt (Kết nối Chương 4: Đảm bảo ATTT bằng mã hóa).
4.  **Chương 4: Phản kích (The Defense):**
    *   Triển khai Firewall (WAF), IDS/IPS để chặn tấn công (Kết nối Chương 5: Công nghệ ATTT).
    *   Giới thiệu quy trình xác thực đa lớp.
5.  **Chương 5: Kết luận (Lessons Learned):**
    *   Quản lý, chính sách mật khẩu trong tổ chức (Kết nối Chương 6: Quản lý & Pháp luật).
    *   Đạo đức nghề nghiệp của một Pentester/Admin.

---

## 5. Danh sách công cụ sử dụng (Resource List)
*   **Target:** DVWA (Damn Vulnerable Web Application) hoặc OWASP Juice Shop.
*   **Attack:** Burp Suite (Professional/Community), Hydra, Hashcat.
*   **Defense:** Fail2Ban, ModSecurity, libpam-google-authenticator.
*   **Presentation:** OBS Studio (quay video demo), Canva.
