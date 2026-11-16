---
name: qa-video-editor
description: "Dựng video từ kịch bản đã duyệt và footage thật, gồm cắt ghép, phụ đề, âm thanh và xuất file; dùng khi có nguyên liệu dựng, không thay bước viết kịch bản."
---
# Dựng video QA

Đọc [hợp đồng tích hợp](../performance-mkt-qa/references/brandformance/integration.md) và chỉ phần tài liệu cần cho task. Khi là subagent, dùng nguồn/brand/client/phiên bản/quyền do điều phối giao, không tự gọi thêm subagent hoặc sửa hồ sơ chung. Trong Agency OS giữ nguyên cấu trúc Drive và đọc [profile](../performance-mkt-qa/references/brandformance/drive-workflow.md) trước công việc có nguồn riêng tư.

Đọc [sản xuất](../performance-mkt-qa/references/brandformance/production.md). Xác nhận kịch bản/phong cách và footage đúng brand/client, kiểm công cụ trên máy hiện tại. Không hard-code bộ Remotion máy owner vào máy người khác. Không có footage/công cụ thì bàn giao EDL/shot list và giới hạn, không giả có video thành phẩm.
Dựng theo EDL, giữ offer/proof/logo/voice, dùng nhạc/footage có quyền. Kiểm file thật, thời lượng/tỷ lệ/phụ đề/chữ/âm thanh theo khả năng, nói rõ phần chưa xem/nghe. Output: video và thumbnail nếu được giao, EDL/subtitles/source, nguồn, kiểm tra và phần còn thiếu. Chỉ ghi folder được giao, không tự đăng hoặc gửi ra ngoài.
