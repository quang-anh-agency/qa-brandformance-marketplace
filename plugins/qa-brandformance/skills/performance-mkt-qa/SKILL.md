---
name: performance-mkt-qa
description: "Điều phối marketing QA Brandformance cho SME: chiến lược, hiểu khách, creative, Ads, chăm sóc lead và đọc kết quả; dùng khi bài toán cần nối nhiều chuyên môn hoặc hỏi việc nên làm tiếp."
---
# QA Brandformance — điều phối

Một đầu mối từ mục tiêu kinh doanh tới khách/đơn và bài học, đúng nhận diện từng brand. Đọc [hợp đồng tích hợp](references/brandformance/integration.md) và [tiêu chuẩn Việt Nam/SME](references/tieu-chuan-viet-nam-sme.md). QA giữ lõi hiểu khách–creative–Ads; Brandformance bổ sung theo nhiệm vụ, không áp phễu/tỷ lệ cố định.

## Bắt đầu và chọn phạm vi
Xác định doanh nghiệp/client, việc được giao, quyết định đã chốt và dữ liệu hiện có; chỉ hỏi phần ảnh hưởng quyết định. Việc nhỏ đi thẳng role cần, dùng lại dữ liệu/hướng còn hiệu lực. Khi làm trong Agency OS, đọc [profile Drive](references/brandformance/drive-workflow.md) và [khung vận hành 2.5](references/brandformance/agency-2.5-flow.md), kiểm quyền trước đọc private và giữ nguyên toàn bộ cấu trúc dự án người dùng đã chia. Không bắt một chat QA ngoài Agency phải có Drive hoặc một bộ hồ sơ hoàn chỉnh.

## Chọn vai trò
| Việc | Skill và tài liệu |
|---|---|
| Mô hình, USP/offer, tệp ưu tiên, kế hoạch chiến dịch/tháng/quý | [qa-strategy](../qa-strategy/SKILL.md); [planning](references/brandformance/planning.md) khi cần kế hoạch kênh/ngân sách |
| Định vị, Bible, Identity, giọng thương hiệu | [qa-brand-system](../qa-brand-system/SKILL.md) |
| Thị trường, đối thủ, Page/Ads Library/TikTok/nguồn khách | [qa-market-research](../qa-market-research/SKILL.md) |
| Từng tệp/bối cảnh, 7 chiều, CIF có nguồn | [qa-customer-insight](../qa-customer-insight/SKILL.md) |
| Chọn hướng, caption, kịch bản, variant, lịch nội dung | [qa-creative](../qa-creative/SKILL.md); [organic/community](references/brandformance/organic-community.md) khi liên quan |
| Tạo/chỉnh ảnh sau khi chọn hướng | [qa-design](../qa-design/SKILL.md) |
| Dựng video đã có kịch bản/footage | [qa-video-editor](../qa-video-editor/SKILL.md) |
| Bảng content–phân phối, setup/test nháp Ads | [qa-ads](../qa-ads/SKILL.md) |
| Điểm nghẽn, quyết định giữ/sửa/tắt/test/mở rộng | [qa-optimization](../qa-optimization/SKILL.md) |
| Chấm lead, tư vấn/chốt, follow-up, Zalo/email, referral | [qa-lead-to-sale](../qa-lead-to-sale/SKILL.md) |
| Báo cáo gọn, dashboard khi được giao, closeout | [qa-reporting](../qa-reporting/SKILL.md) |
| Rút kinh nghiệm và đề xuất cải tiến hệ thống | [qa-coach](../qa-coach/SKILL.md), vai trò riêng khi được yêu cầu |
| Kiểm tra đầu ra độc lập | [qa-reviewer](../qa-reviewer/SKILL.md) |
| Hỏi tình hình/chưa biết nên làm gì | [status-coach](references/brandformance/status-coach.md); chỉ đọc và gợi ý trước |

## Chuỗi và các lựa chọn của người dùng
Theo [chiến dịch QA](references/workflows/chien-dich-moi.md). Strategy/research cần thiết → Reviewer → G1 chọn tệp, xác nhận offer/proof và lượt hỏi người hiểu khách → CIF được kiểm → 3–5 hướng creative khi phù hợp → Reviewer → G2 chọn hướng/định dạng → viết và sản xuất phần đã chọn → Reviewer → G3 bản cuối. Ads: bảng nhiệm vụ từng content/cách chạy để user chọn trước setup chi tiết; Reviewer kiểm ADS_PLAN trước gate l5_action của workspace, không tự chi tiền/đăng bài. Không coi im lặng là lựa chọn. Không bắt lại cả chuỗi cho phần đã được duyệt. Trong Agency áp dụng các mode, approve/resume, feedback và Coach trong [khung 2.5](references/brandformance/agency-2.5-flow.md); không lấy mô tả QA ngắn thay hợp đồng này.

CIF mới/cập nhật đáng kể luôn có lượt hỏi owner/người trực tiếp làm trước phần phụ thuộc; dùng câu trả lời đã có đúng scope thay vì hỏi lại. Creative mới xác nhận USP/offer/chương trình/proof trước angle và chờ chọn trước sản xuất. Hướng video chưa rõ thì hỏi MC/lồng tiếng/nhạc+chữ; có lựa chọn rồi đi tiếp. Research độc lập vẫn có thể làm khi dữ liệu CIF còn chờ; không lấp bằng quote giả.

## Giao việc và nghiệm thu
Khi runtime có công cụ subagent và nhiệm vụ cần nhiều chuyên môn, giao role đúng bằng [bàn giao](references/templates/ban-giao.md), thêm brand/client, nguồn/phiên bản và quyền ghi. Các bước phụ thuộc chờ kết quả/gate; chỉ việc độc lập mới song song. Không gọi mọi role cho một việc nhỏ, không giả đã có agent chạy. Runtime thiếu thì làm tuần tự theo role và nói rõ.

Reviewer độc lập bắt buộc trước G1, G2, G3 và ADS_PLAN trong chuỗi chiến dịch; specialist không sửa hồ sơ chung hoặc tự approve. Điều phối tổng hợp câu hỏi quan trọng vào gate, ghi nguồn/giả thuyết/giới hạn và việc tiếp theo. Log do một đầu mối ghi, giữ đúng nơi hiện có. Mọi write có readback; lỗi quyền dừng phần phụ thuộc, không tự dựng dự án khác. [Thư viện](references/INDEX.md) chỉ đọc phần đúng nhiệm vụ.
