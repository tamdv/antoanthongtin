CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL, -- Lưu dạng plaintext cho bản Vulnerable
    full_name VARCHAR(100)
);

-- Thêm một số tài khoản mẫu để thực hành
INSERT INTO users (username, password, full_name) VALUES 
('admin', 'admin123', 'Hệ thống Quản trị'),
('tam', 'attt2024', 'Đào Tâm'),
('trung', '123456', 'Nguyễn Trung');
