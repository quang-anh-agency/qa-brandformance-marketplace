---
name: qa-ads
description: "Chọn cấu trúc và kế hoạch triển khai Meta Ads phù hợp mô hình bán, địa bàn, nguồn lực và creative; hướng dẫn setup và test phân phối."
---
# Ads QA
## Tiêu chuẩn áp dụng cho mọi tác vụ
Đọc [Việt Nam — SME — chủ động lấy input](../performance-mkt-qa/references/tieu-chuan-viet-nam-sme.md). Mặc định thị trường Việt Nam, chọn cách làm vừa nguồn lực SME; chủ động hỏi/đề xuất dữ liệu ảnh hưởng quyết định thay vì chờ người dùng tự biết phải gửi gì.
Khi dữ liệu còn thiếu, đề xuất đường lấy phù hợp qua công cụ đang có hoặc export thủ công; dùng [workflow dữ liệu/kết nối](../performance-mkt-qa/references/workflows/du-lieu-va-ket-noi.md) và [hàng chờ](../performance-mkt-qa/references/templates/hang-cho.md). Không tự coi kết nối đã hoạt động hoặc yêu cầu nối mọi công cụ mới làm được.
Đọc [nguyên tắc chung](../performance-mkt-qa/references/nguyen-tac.md), [vai trò](../performance-mkt-qa/references/agents/ads.md) và [playbook](../performance-mkt-qa/references/ads-playbook.md) trước khi làm.
Thư viện dùng chung nằm trong skill anh em `performance-mkt-qa`; luôn cài cả bộ skill để giữ các liên kết này.

## Đầu vào
Đọc yêu cầu, doanh nghiệp/campaign và hồ sơ được chỉ định. Nếu gọi trực tiếp, kiểm tra dữ liệu đủ cho nhiệm vụ này; chỉ hỏi phần quyết định. Không ép đi lại toàn quy trình.
Nếu nhận subtask, dùng phiên bản dữ liệu và giới hạn của điều phối; trả câu hỏi cần người dùng quyết định về điều phối.

## Nối content với cách chạy
Sau khi có content, làm theo [quy trình content → chiến thuật Ads](../performance-mkt-qa/references/content-va-chien-thuat-ads.md): hỏi/xác nhận điều kiện kinh doanh và chạy, đề xuất nhiệm vụ/đối tượng tiếp cận/hành động/cách phân phối cho từng content, giải thích chạy cùng hay tách. User chọn phương án rồi mới làm setup chi tiết; không tự chạy hết. Một content không tự là một chiến dịch, video tạo tin tưởng không mặc định chạy lượt xem.

## Thực hiện
Làm theo vai trò và playbook đã liên kết. Dùng [template đầu ra](../performance-mkt-qa/references/templates/ads-test-plan.md) nếu giúp công việc; bỏ mục không liên quan, không điền bịa.
Tham khảo [case](../performance-mkt-qa/references/INDEX.md) theo bối cảnh, không sao chép cấu trúc Ads/offer giữa các mô hình.
Giữ riêng dữ liệu, giả thuyết và đề xuất; một creative có thể phối hợp nhiều chiều; phân nhóm nghiên cứu không buộc tách ad set.

## Bàn giao
Giao kết quả sử dụng được, lý do, nguồn và giới hạn kết luận. Nếu là sub-agent, dùng [mẫu bàn giao](../performance-mkt-qa/references/templates/ban-giao.md); không ghi hồ sơ chung trừ khi được giao rõ đường dẫn. Chuyển vấn đề ngoài phạm vi cho vai trò tương ứng.
Nếu cần khả năng giao việc độc lập, điều phối gọi custom agent cùng tên khi đã cài và runtime hỗ trợ; file SKILL.md không tự đảm bảo một tiến trình sub-agent.

## QA Brandformance v2.0
Đọc [hợp đồng tích hợp](../performance-mkt-qa/references/brandformance/integration.md) trước khi làm; giữ mọi lượt hỏi/xác nhận và lựa chọn bắt buộc của QA ở trên. Trong Agency OS, điều phối giữ quyền, brand/client context, log và cấu trúc Drive hiện có; specialist chỉ ghi đích được giao. Đọc module bổ sung khi đúng nhiệm vụ, không nạp cả thư viện và không dùng benchmark/phễu mẫu làm quy tắc chung.
[Đo và nguồn](../performance-mkt-qa/references/brandformance/measurement.md). Không mặc định Pixel/CAPI/landing page hoặc nhiều ad set cho mọi nơi chuyển đổi.
