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

-- BẢN SECURE: Tạo bảng riêng cho bản an toàn
CREATE TABLE users_secure (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    full_name VARCHAR(100),
    mfa_secret VARCHAR(32) -- Lưu khóa bí mật cho MFA (TOTP)
);

-- Thêm dữ liệu mẫu đã được băm (Bcrypt)
-- JBSWY3DPEHPK3PXP : Hello world --
-- KRQW2RCWEBAWI3LJNY : TamDV Admin --
-- admin - admin123 --
-- tam - Tam141995@ --
-- trung - 123456 --
INSERT INTO users_secure (username, password, full_name, mfa_secret) VALUES 
('admin', '$2b$12$X5qnS8gmMDO4HYLzVvRsQelAKe0crjDJ6ipcpOhxWbBE9fmKR/OPK', 'Hệ thống Quản trị (Secure)', 'JBSWY3DPEHPK3PXP'),
('tam', '$2a$12$ey1LgaBiA4E9QK9/UZHHEu8pvqu4e/8wsZ/X4o3EFn.S/7VY2SvFe', 'Đào Tâm (Secure)', 'KRQW2RCWEBAWI3LJNY'),
('trung', '$2b$12$Ow95Z8IyOwzcsDtz28tnielK1yjbNxcnAaGPPgxCZx206itp21rXC', 'Nguyễn Trung (Secure)', NULL);

