# Thiết lập lần đầu

Plugin có 14 skill nghiệp vụ từ QA Brandformance 2.0.1 theo luồng Company OS 2.5 và một skill `qa-team-setup` phục vụ cài đặt. Phiên bản phân phối là 2.1.0.

Sau khi cài plugin, chọn **Setup** hoặc yêu cầu “Dùng qa-team-setup thiết lập bộ agent trên máy này”. Cần Python 3.11 trở lên, Codex có quyền chạy lệnh local và ghi thư mục agent của người đang đăng nhập.

Plugin không được giả định tự nạp 13 agent từ thư mục assets. Script `scripts/setup_agents.py` cài riêng các TOML vào `~/.codex/agents`. Không sao chép skill sang `~/.agents/skills`, không sửa model/quyền/config hoặc token. Agent tìm skill hiện hành theo tên trong phiên, không phụ thuộc đường dẫn máy owner.

Xem trước: `python3 scripts/setup_agents.py --dry-run`.
Cài: `python3 scripts/setup_agents.py`.
Kiểm: `python3 scripts/setup_agents.py --check`.
Thực hiện tại plugin root, hoặc dùng đường dẫn tuyệt đối tới script từ vị trí plugin đã cài.

Nếu gặp file agent trùng tên khác nội dung, script dừng trước ghi. Chỉ sau khi đã xem và đồng ý thay, chạy thêm `--replace-existing`. Trước ghi có ZIP sao lưu; khôi phục bằng `python3 scripts/setup_agents.py --restore /duong/dan/qa-agents-....zip`. Khôi phục từ chối nếu file đã được sửa sau cài.

Mở chat mới sau thiết lập. Kiểm tra 13 vai trò có trong công cụ giao việc; nếu runtime không cung cấp, báo chưa kiểm chứng. Không dùng kết quả parse file thay bằng chứng agent thực sự chạy.

Mỗi người tự kết nối Google Drive bằng tài khoản được cấp quyền. Hồ sơ doanh nghiệp, run và approval ở Drive, không nằm trong repo. Quyền Drive hiện có không bị script này thay đổi.

Bản cài cũ có thể chứa các skill cùng tên trong thư mục cá nhân. Không bật đồng thời hai nguồn cho cùng bộ. Script Setup không tự xoá hoặc sửa bộ cũ; quyết định chuyển nguồn thực hiện riêng và có sao lưu.
