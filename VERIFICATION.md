# Kiểm tra bản phân phối 2.1.0 — 16/11/2026

- 14 skill nghiệp vụ giữ nguyên 83 file so với gói Codex 2.0.1; khung Company OS 2.5 không đổi.
- Có thêm một skill Setup và 13 cấu hình agent portable. Không nhúng đường dẫn máy owner hoặc cache phiên bản vào hướng dẫn agent.
- Validator skill chính thức: 15/15 hợp lệ. Validator gói kiểm catalog, manifest, liên kết, checksum và nguồn core.
- Codex CLI thực tế dùng kiểm: 0.169.0-alpha.11.1. Native marketplace add/list nhận tên `quang-anh-agency`, native plugin add/list nhận `qa-brandformance` 2.1.0. Đã cài thử và đối chiếu file trong cache, rồi gỡ bản thử để không trùng 14 skill cá nhân đang dùng. Sau phát hành, đã chuyển nguồn đăng ký của owner sang kho GitHub Private.
- Đã kiểm tra GitHub Private `quanganhcetus-lab/qa-brandformance-marketplace`: đủ 110 file với Git blob hash khớp bản local; thêm kho từ GitHub bằng Codex CLI, cài plugin từ nguồn Git và đối chiếu 101 file trong cache. Sau thử đã gỡ bản plugin thử để giữ bộ skill cá nhân hiện tại. Đây là kiểm thử bằng tài khoản owner, chưa thay cho tài khoản nhân viên.
- Setup được thử ở thư mục cách ly: preview không ghi, cài và đọc lại 13 agent, chạy lại không đổi, giữ file ngoài bộ, từ chối xung đột, thay có sao lưu, khôi phục khớp nguyên trạng, chặn khôi phục sau chỉnh sửa, từ chối symlink đích.
- Đánh giá độc lập đã chạy từ đường dẫn khác có dấu cách và giả lập lỗi ghi giữa cài. Lỗi ghi dở đã được sửa bằng file tạm và thay nguyên tử; sau kiểm lại target cũ và file ngoài bộ còn nguyên, không sót file tạm.
- Không sửa Drive, Registry, quyền nhân viên, offer hoặc ngân sách. Không đưa hồ sơ khách, credential hoặc raw CRM lên gói. Không triển khai server hoặc lịch nền.

Các kiểm tra này xác nhận gói local và cách cài trong môi trường kiểm. Nhân viên vẫn cần quyền GitHub đọc repo, đăng nhập Git phù hợp, Codex hỗ trợ plugin, Python 3.11+, kết nối nguồn theo tài khoản của họ và mở chat mới sau Setup. Chưa xác nhận bằng tài khoản nhân viên thật hoặc chạy chiến dịch marketing từ đầu đến cuối. Không coi sự tồn tại của 13 TOML là bằng chứng cả 13 agent đã được gọi trong mọi client.
