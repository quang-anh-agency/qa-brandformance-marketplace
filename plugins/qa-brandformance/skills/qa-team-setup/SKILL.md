---
name: qa-team-setup
description: "Thiết lập hoặc kiểm tra 13 vai trò agent của plugin QA Brandformance sau khi cài trên Codex; dùng khi cài lần đầu, chuyển máy hoặc cập nhật bộ agent."
---
# Thiết lập QA Brandformance cho nhân viên

Đây là thiết lập máy, không phải campaign hoặc onboarding brand. Không đọc/ghi Drive, không sửa quyền, không tạo run. Bộ nghiệp vụ là 14 skill QA; skill này chỉ làm bước thiết lập bổ sung.

1. Xác định plugin root từ vị trí SKILL.md này, đi lên hai thư mục. Đọc [hướng dẫn](../../SETUP.md). Không dùng đường dẫn máy của owner hoặc đoán cache. Kiểm tra phiên có `performance-mkt-qa` và các skill `qa-*` nghiệp vụ; thiếu thì yêu cầu cài/bật plugin và mở chat mới.
2. Chạy `scripts/setup_agents.py --dry-run` bằng Python 3.11 trở lên tại plugin root. Nếu không có shell/Python hoặc chính sách máy không cho cài, báo điều kiện thiếu; không giả đã thiết lập.
3. Khi người dùng đã yêu cầu Setup/cài hệ thống, chạy script không có `--dry-run` để cài 13 vai trò. Script chỉ ghi các tên agent của gói; không sao chép skills, đổi model, quyền, config chung hoặc kết nối tài khoản.
4. Trùng tên khác nội dung: mặc định dừng. Trình rõ tên agent và việc thay hướng dẫn; chỉ chạy `--replace-existing` khi người dùng đồng ý thay các file được nêu. Có ZIP sao lưu và lệnh khôi phục. Không tự vượt xung đột hoặc ghi đè chỉnh sửa sau cài.
5. Chạy `--check` và báo kết quả thực tế. Đề nghị mở chat mới để nhận vai trò. Khi phiên mới có công cụ giao việc và user muốn kiểm thử, thử một tác vụ local với qa-reviewer, không truy cập nguồn doanh nghiệp; chỉ xác nhận agent chạy khi có kết quả thật. Không tự tạo một chiến dịch để thử.

Mỗi người kết nối Google Drive bằng tài khoản được cấp quyền của họ. Chưa nhận diện/quyền live thì chưa xác nhận đã sẵn sàng làm cho brand. Nếu thấy hai skill trùng tên do bộ cài thủ công cũ, báo để người dùng chọn một nguồn; không tự xoá bộ cũ.
