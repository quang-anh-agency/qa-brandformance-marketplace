---
name: qa-design
description: "Tạo ảnh và creative thành phẩm từ hướng đã chọn, logo/ảnh thật và nhận diện brand; dùng khi người dùng đã chọn sản xuất hình, không thay bước chọn angle."
---
# Thiết kế ảnh QA

Đọc [hợp đồng tích hợp](../performance-mkt-qa/references/brandformance/integration.md) và chỉ phần tài liệu cần cho task. Khi là subagent, dùng nguồn/brand/client/phiên bản/quyền do điều phối giao, không tự gọi thêm subagent hoặc sửa hồ sơ chung. Trong Agency OS giữ nguyên cấu trúc Drive và đọc [profile](../performance-mkt-qa/references/brandformance/drive-workflow.md) trước công việc có nguồn riêng tư.

Chỉ nhận direction/format/chữ và nguồn ảnh/logo đã chọn/xác nhận. Thiếu lựa chọn trả câu hỏi về điều phối; thiếu ảnh thật không tự chế sản phẩm. Đọc [sản xuất](../performance-mkt-qa/references/brandformance/production.md) và [quy trình QA](../performance-mkt-qa/references/creative-san-xuat.md).
Kiểm công cụ thật; yêu cầu tạo/chỉnh bitmap AI dùng imagegen skill/tool hiện có theo hướng dẫn hiện hành, bố cục bằng tài sản sẵn có có thể dùng công cụ thiết kế/code phù hợp. Xuất và mở xem file, đối chiếu chữ/logo/sản phẩm, không báo đã tạo ảnh khi mới có prompt. Output: file thật/source khi có, creative ID, tài sản/nguồn, điều đã kiểm, vấn đề còn lại, đường dẫn được phép ghi; không tự đăng/chia sẻ.
