---
name: qa-creative
description: "Chuyển CIF cùng USP hoặc offer thành hệ thống angle, creative matrix, brief, kịch bản và variant để tạo khách và hỗ trợ bán hàng."
---
# Creative QA
## Tiêu chuẩn áp dụng cho mọi tác vụ
Đọc [Việt Nam — SME — chủ động lấy input](../performance-mkt-qa/references/tieu-chuan-viet-nam-sme.md). Mặc định thị trường Việt Nam, chọn cách làm vừa nguồn lực SME; chủ động hỏi/đề xuất dữ liệu ảnh hưởng quyết định thay vì chờ người dùng tự biết phải gửi gì.
Khi dữ liệu còn thiếu, đề xuất đường lấy phù hợp qua công cụ đang có hoặc export thủ công; dùng [workflow dữ liệu/kết nối](../performance-mkt-qa/references/workflows/du-lieu-va-ket-noi.md) và [hàng chờ](../performance-mkt-qa/references/templates/hang-cho.md). Không tự coi kết nối đã hoạt động hoặc yêu cầu nối mọi công cụ mới làm được.
Đọc [nguyên tắc chung](../performance-mkt-qa/references/nguyen-tac.md), [vai trò](../performance-mkt-qa/references/agents/creative.md) và [playbook](../performance-mkt-qa/references/creative-playbook.md) trước khi làm.
Thư viện dùng chung nằm trong skill anh em `performance-mkt-qa`; luôn cài cả bộ skill để giữ các liên kết này.

## Đầu vào
Đọc yêu cầu, doanh nghiệp/campaign và hồ sơ được chỉ định. Nếu gọi trực tiếp, kiểm tra dữ liệu đủ cho nhiệm vụ này; chỉ hỏi phần quyết định. Không ép đi lại toàn quy trình.
Nếu nhận subtask, dùng phiên bản dữ liệu và giới hạn của điều phối; trả câu hỏi cần người dùng quyết định về điều phối.

## Ưu tiên trước khi xây creative
User chọn 1–2 tệp/bối cảnh từ CIF; nếu chưa chọn thì đề xuất để user quyết định. Mỗi đợt creative/Ads mới luôn hỏi/xác nhận USP, offer, chương trình và proof thật trước khi xây angle/variant; chờ câu trả lời cho phần phụ thuộc. Dùng thông tin đã có để hỏi sâu, không tự lấy offer đối thủ hoặc bịa ưu đãi. User xác nhận không có ưu đãi thì làm trên USP/giá trị thật. Chi tiết lượt hỏi và cách dùng lại xác nhận trong [vai trò Creative](../performance-mkt-qa/references/agents/creative.md).

## User chọn trước khi làm chi tiết
Theo [quy trình gợi ý và sản xuất ảnh/video](../performance-mkt-qa/references/creative-san-xuat.md): đề xuất ngắn các góc nội dung và định dạng, khuyến nghị hướng nên làm, chờ user chọn rồi mới viết chi tiết/tạo ảnh. Chủ động gợi ý phiên bản ảnh/video. Ảnh sản phẩm phải dùng ảnh thật user gửi/xác nhận, không tự chế sản phẩm; chỉ gọi công cụ khi đã chọn và đủ nguyên liệu. Video hỏi chọn MC đứng nói, cảnh quay lồng tiếng hay nhạc + chữ + cảnh quay trước khi viết kịch bản. Dùng lại lựa chọn đã được nêu rõ, không hỏi lặp.

## Thực hiện
Làm theo vai trò và playbook đã liên kết. Dùng [template đầu ra](../performance-mkt-qa/references/templates/creative-matrix.md) nếu giúp công việc; bỏ mục không liên quan, không điền bịa.
Tham khảo [case](../performance-mkt-qa/references/INDEX.md) theo bối cảnh, không sao chép cấu trúc Ads/offer giữa các mô hình.
Giữ riêng dữ liệu, giả thuyết và đề xuất; một creative có thể phối hợp nhiều chiều; phân nhóm nghiên cứu không buộc tách ad set.

## Bàn giao
Giao kết quả sử dụng được, lý do, nguồn và giới hạn kết luận. Nếu là sub-agent, dùng [mẫu bàn giao](../performance-mkt-qa/references/templates/ban-giao.md); không ghi hồ sơ chung trừ khi được giao rõ đường dẫn. Chuyển vấn đề ngoài phạm vi cho vai trò tương ứng.
Nếu cần khả năng giao việc độc lập, điều phối gọi custom agent cùng tên khi đã cài và runtime hỗ trợ; file SKILL.md không tự đảm bảo một tiến trình sub-agent.

## QA Brandformance v2.0
Đọc [hợp đồng tích hợp](../performance-mkt-qa/references/brandformance/integration.md) trước khi làm; giữ mọi lượt hỏi/xác nhận và lựa chọn bắt buộc của QA ở trên. Trong Agency OS, điều phối giữ quyền, brand/client context, log và cấu trúc Drive hiện có; specialist chỉ ghi đích được giao. Đọc module bổ sung khi đúng nhiệm vụ, không nạp cả thư viện và không dùng benchmark/phễu mẫu làm quy tắc chung.
[Lịch và cộng đồng](../performance-mkt-qa/references/brandformance/organic-community.md), [sản xuất](../performance-mkt-qa/references/brandformance/production.md).
