# Khung vận hành Agency 2.5 — hợp đồng tương thích Codex

Áp dụng cùng [Drive và quyền](drive-workflow.md), [tích hợp](integration.md). Khung ngoài theo Company OS 2.5; QA và RBL chỉ là phương pháp trong từng bước, không thay việc duyệt hoặc tạo hệ điều phối khác. Nguồn 2.5 được đối chiếu là `ai_agent_agency/agency-plugin` và HUONG_DAN_SU_DUNG.md ngày 14/11/2026; dữ liệu/quyền/offer vẫn đọc live, không lấy snapshot này làm nguồn brand.

## Một chiến dịch mới
1. Tiếp nhận → kiểm người/brand/client → đọc Registry và context đúng nguồn → xác định objective, offer, kết quả, hạn, kênh, ngân sách/KPI ở mức đã biết → brief/run theo SOP.
2. Strategy lập kế hoạch; Research hỗ trợ khi cần. **Reviewer kiểm kế hoạch trước G1**, không để owner thay bước kiểm nguồn/logic. REVISE về đúng role, PASS mới trình.
3. **G1 `strategy`**: owner/người có quyền duyệt kế hoạch, chọn 1–2 tệp, xác nhận USP/offer/proof và trả lời lượt hỏi về khách. Ghi câu trả lời và phiên bản, dừng nếu thiếu phần phụ thuộc.
4. Customer Insight xây/cập nhật CIF theo 7 chiều và nguồn đã có. Lượt hỏi ở G1 có thể đáp ứng yêu cầu hỏi owner nếu đúng phạm vi; không hỏi lại máy móc. Chưa được hỏi/trả lời thì NEEDS_OWNER_INPUT. Review chính CIF trước khi dùng làm đầu vào chính thức; giữ phiên bản cũ. Sau Reviewer PASS, Orchestrator cập nhật riêng cột `cif_doc_id` của đúng brand trong BRAND_REGISTRY sang phiên bản mới theo quyền/workflow hoặc approval đang có, rồi readback; đây là con trỏ hồ sơ CIF, không phải quyền đổi folder/account/approver routing. Worker không cập nhật Registry. Thiếu quyền hoặc chưa có phê duyệt cần thiết thì dừng đồng bộ, báo con trỏ còn cũ và dùng ID mới chỉ trong run được phép; không âm thầm coi Registry đã cập nhật. Không thực hiện việc này trong lần ghép/cài bộ skill.
5. Creative bước 1 chỉ trình 3–5 hướng có căn cứ khi phù hợp, kèm CIF ID, angle, format, thông điệp brand, proof cần. **Reviewer kiểm hướng trước G2**, không viết luôn cả bộ chi tiết.
6. **G2 `creative_direction`**: owner chọn hướng và định dạng. Ghi direction_id/phiên bản và ghi chú; dừng chờ lựa chọn. Chỉ phần được chọn đi tiếp.
7. Creative bước 2 viết caption/ad copy/kịch bản/shot list đúng scope. Design xuất ảnh thật khi được chọn và đủ tài sản. Video Editor chỉ gọi khi có video cần dựng và đủ footage/công cụ, không gọi cho bài chữ/ảnh. Các role làm riêng, không tự duyệt nhau.
8. **Reviewer kiểm bản cuối trước G3**, trả lỗi đúng worker, tối đa 2 vòng/stage theo config live. Không PASS nếu thiếu nguồn, lẫn brand, bỏ gate hoặc chưa có file thành phẩm được yêu cầu.
9. **G3 `content`**: người có quyền duyệt chữ/ảnh/video ở phiên bản cụ thể. Lưu bản cuối đúng thư mục hiện có và đúng quyền; không tự tạo 9 folder hoặc cây dự án mới.
10. Ads/Performance nhận các content đã duyệt, đề xuất bảng nhiệm vụ–đối tượng–đường chuyển đổi–chạy cùng/tách để user chọn theo QA. Có thể dùng lại lựa chọn đã chốt trong kế hoạch. Sau lựa chọn mới làm ADS_PLAN/setup chi tiết; **Reviewer kiểm ADS_PLAN**, rồi `l5_action` nếu muốn thực thi. QA không thêm một gate/cột CONTROL mới cho lựa chọn này.
11. Plan A: **người** bật Ads/đăng/gửi tin theo quyền. Approval không phải bằng chứng đã chạy. Xác nhận sau thực thi và nguồn kết quả mới ghi COMPLETED theo SOP.
12. Báo cáo gọn → feedback/memory → Coach khi được yêu cầu → đề xuất cải tiến qua `system_change`; đưa 1–2 gợi ý tiếp theo, không tự mở việc mới.

## Các nhánh và điểm vào như 2.5
| Workflow | Phạm vi và đường đi |
|---|---|
| `brand_status` | Chỉ đọc đúng quyền: kế hoạch/CIF/run/gate/báo cáo/Memory/offer có hạn → thẻ + 2–3 gợi ý → user chọn mới chạy. Không tạo run. |
| `campaign_planning` | Chuỗi 12 bước ở trên, đủ ba gate và các review trước gate. |
| `monthly_cycle` | Đọc kỳ trước, mục tiêu và learning → kế hoạch tháng/đợt → review + G1 khi là kế hoạch mới; tái dùng CIF/hướng còn hiệu lực. |
| `quarter_plan` / `plan_6m` | Strategy lập kế hoạch quý/tối đa 6 tháng → reviewer → G1. Không tự sản xuất tất cả nội dung theo kế hoạch dài. |
| `brandformance_daily` | Lịch duy trì từ CIF/thông điệp/Identity và kế hoạch còn hiệu lực; nhánh kế hoạch mới qua G1, hướng mới qua G2, bản cuối qua reviewer/G3. Dùng lại gate đã duyệt cho phần không đổi. |
| `content_production` | Chỉ vào sản xuất khi đã có kế hoạch/hướng duyệt hoặc owner yêu cầu rõ làm luôn/bỏ kế hoạch; giữ các xác nhận QA và review/G3 phù hợp. |
| `video_production` | Kịch bản/phong cách đã chọn + footage thật → dựng → review → G3, không gọi kế hoạch mới vô cớ. |
| `creative_only` | Brief/hướng đã chốt → Design → reviewer → G3. |
| `ads_plan` | Đầu vào strategy/creative còn hiệu lực → bảng phân phối để chọn → kế hoạch chi tiết → reviewer → l5_action nếu thực thi, người thực hiện. |
| `lead_to_sale_setup` | Strategy/sau-lead → reviewer → G1 → Creative/kịch bản/chuỗi → reviewer → G3; Performance/Optimization định nghĩa đo theo nguồn. Không gửi tin. |
| `performance_report` | Lấy số đúng kỳ/nguồn/định nghĩa → Reporting theo form gọn → reviewer đối chiếu số, không tự đổi dashboard. |
| `diagnosis` / `deep_analysis` | QA Optimization phân tích khi user yêu cầu; không lấy báo cáo định kỳ làm lý do mở phân tích dài. |
| `campaign_closeout` | Reporting → reviewer → người quyết định → Memory/feedback theo quyền. |
| `onboarding` | Chỉ khi được yêu cầu rõ; đọc nguồn/hỏi thiếu, lập tài liệu vào vị trí owner chỉ định, review và duyệt Bible/Guideline. Không tạo lại các dự án đã chia. Nếu cần folder/Registry mới, phải được giao riêng đúng scope. |

## Duyệt và tiếp tục (`approve-run` của 2.5)
Tới gate, điều phối tạo APPROVALS pending theo header live, có APR duy nhất, run/client, gate và output_version_hash = Drive ID + thời điểm sửa cuối; cập nhật RUN_LOG rồi dừng. Không tự ghi approved. Sau quyết định thật cập nhật status/approved_by/approved_at (ISO +07:00)/notes đúng cột; mọi chỉnh sửa trong duyệt chuyển qua feedback.

Điều phối đọc approval pending đúng run/client và phiên bản output; xác minh người quyết định trong TEAM_ROLES. Gate strategy dùng can_approve_strategy; content và creative_direction dùng can_approve_content; l5_action/system_change dùng quyền tương ứng. Không có quyền thì không ghi approval và không tiếp tục phần đó.

- `approved strategy`: ghi tệp/USP/offer/proof/câu trả lời → chuyển CIF rồi creative bước 1, chưa sản xuất chi tiết.
- `approved creative_direction`: ghi đúng direction → creative bước 2 và phần sản xuất đã chọn.
- `approved content`: giữ bản cuối/version và trạng thái APPROVED, chưa gọi là đã đăng/bật Ads.
- `approved l5_action`: Plan A người thực hiện, chỉ ghi COMPLETED sau có xác nhận/after-state phù hợp.
- `changes_requested`: quay đúng role/stage, review lại và trình phiên bản mới, không dùng approval bản cũ cho nội dung đã đổi.
- `rejected`: REJECTED_BY_HUMAN theo SOP. `system_change`: chỉ áp dụng thay đổi đã được duyệt trong scope, ghi CHANGE_LOG; không tự nâng quyền hoặc mở rộng sang policy khác.

Reviewer REVISE → REVISION_REQUIRED, gửi đúng role gây lỗi và chạy lại phần sau nếu đầu vào đổi; tối đa 2 vòng/stage theo config live, rồi FAILED_REVIEW. Lỗi kỹ thuật thử lại 1 lần cùng context, còn lỗi thì FAILED_AGENT. Không dùng sửa nhỏ làm lý do né việc kiểm lại đầu ra đã đổi.

“OK” chỉ có nghĩa duyệt nếu trước đó đã trình đúng action/target/version và không mơ hồ có nhiều approval. Khi câu trả lời không chỉ rõ, hỏi một câu để xác định, không tự chọn pending mới nhất. Không chấp nhận output đã đổi sau duyệt như cùng phiên bản.

## Feedback và cập nhật hồ sơ (`log-feedback`)
Giữ brand/client/run/item, ai phản hồi, đã sửa gì, nguồn/ngày và tag: wrong_voice, wrong_fact, unapproved_claim, weak_hook, too_long, too_short, weak_cta, policy_violation, wrong_audience, poor_design, off_brand_visual, wrong_targeting, budget_issue, wrong_brand_context, good, other. Severity light/medium/heavy theo mức sửa. Không tự mở taxonomy mới hoặc đổi schema CONTROL.

Một lần owner chốt thông tin chỉ đồng bộ các mục liên quan trong nguồn chính thức khi có quyền/approval hợp lệ: Bible/mục quyết định owner, Guideline, Identity và Catalog/Registry nếu trong scope được duyệt. Giữ cấu trúc đã chia; sửa đúng mục gốc, ghi nhật ký và readback thay vì append các đoạn “cập nhật” mâu thuẫn. Không coi yêu cầu sửa hook là yêu cầu đổi hồ sơ brand.

## Coach độc lập (`coach-review`)
Gọi [qa-coach](../../../qa-coach/SKILL.md) riêng khi được yêu cầu, không gộp vai trò này vào Reporting. Reporting tóm tắt kết quả; Coach đọc feedback/run/review/learning để tìm mẫu lỗi và đề xuất cải tiến đúng tầng. CIF được duyệt do Customer Insight tạo v<n+1>, Reviewer kiểm và Orchestrator cập nhật riêng con trỏ cif_doc_id theo quyền như bước 4; không để lượt sau nạp nhầm bản cũ. Không tự sửa hệ thống hoặc tự phát hành skill. Theo khoảng thời gian được giao hoặc 7 ngày gần nhất nếu không chỉ rõ; proposal/learning log ghi vào các vị trí COACH/PROPOSALS và learning log đã được xác minh, đề xuất cần duyệt tạo APPROVALS pending gate system_change theo schema live; không có lịch nền được ngầm tạo.

Tất cả chức năng trên là mode của đầu mối điều phối và module/role đúng nhiệm vụ. Tên SKILL/TOML trong Codex có thể khác gói Claude; không nhân đôi thêm một Orchestrator hoặc một bộ dữ liệu vì tên khác.
