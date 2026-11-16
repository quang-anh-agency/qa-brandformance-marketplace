# Agency OS — giữ nguyên các dự án hiện có

Profile này áp dụng khi người dùng làm với AI Agency OS, không bắt mọi chat QA ngoài workspace kết nối Drive.

## Cấu hình nguồn
- ROOT `AI Agency OS`: `1ijPiqEWPnZDaB7NYUMB_vz2AvE6Mf7YA`.
- CONTROL: `1pPH9f8UH9kJ9nxNX8_8E0zyoRbQp3tJZgoyilVvZZqc`.
- POLICY_AND_PERMISSIONS: `1wS-7MIaxq--IIygc_t_qpcvnzBHLfOUwQUFJD5LIGQk`.
- SOP_GENERAL: `10Mtvh9LGZ37AEYZpT2ea4Nkv_UTkAcPTxVUlXRA1HS0`.
- AGENT_CONFIG: `1w118tYCTWBc5wL2rZElQ4DZASNC8IMr0iwrzgXS9wcU`.
- Mẫu báo cáo tháng: `1hnwd_o88agVgYzrAAj0DFJgfAQ2yzbxViwm4smtwhic`.

Đây là ID bootstrap, không chứa credential, không phải bản sao quyền/giá/offer/KPI. Luôn đọc nguồn hiện hành. Đọc phần cập nhật mới còn hiệu lực trong AGENT_CONFIG; không chạy lại phần đánh dấu cũ/đã thay.

## Trước đọc hồ sơ brand
1. Xác định người yêu cầu từ danh tính thực sự được công cụ/phiên cung cấp và đối chiếu TEAM_ROLES. Không giả dùng tên owner trong chat để xác thực tài khoản khác. Nếu công cụ không cung cấp danh tính, nêu giới hạn; không tự cấp quyền hoặc xác nhận người khác là owner. Kiểm quyền trước cả `brand_status`, không chờ tới bước tạo run.
2. Đọc metadata CONTROL, rồi range giới hạn đúng header/tab hiện có. Tra BRAND_REGISTRY bằng ID/tên không mơ hồ; không cache số thứ tự cột. TEAM_ROLES chỉ là policy, không thay quyền truy cập thật của nguồn.
3. Resolve Drive ID của hồ sơ brand và output folder từ nguồn đã xác minh. Không đoán folder con từ tên brand, không lấy account theo tab trình duyệt đang mở. Brand paused/archived, mapping thiếu hoặc quyền thiếu: dừng phần phụ thuộc, báo rõ; có thể tiếp tục phần độc lập không cần truy cập riêng tư.
4. Đọc policy/SOP/config và context cần cho task: Bible, Identity, Guideline, Catalog/OFFERS, CIF, Memory, nguồn dashboard khi liên quan. Không đọc mọi brand để làm cho một brand. Không suy ưu đãi còn hiệu lực từ ví dụ hoặc tên campaign cũ.

## Cấu trúc đã khóa theo yêu cầu owner
Giữ nguyên root, các dự án, folder, file và Registry routing đã chia. Không thêm bảng điều khiển khác, không tạo cây folder mới mặc định. Các tên GSERVICE/GLUX/HOANGMAI/GROWEE/NOITHAT là gợi ý tìm trong Registry, không phải snapshot quyền hay account. Với NOITHAT tra danh sách khách hiện có, chọn đúng khách; gắn `client_key` ổn định trong brief/handoff/output và nguồn allowlist. Thiếu tên khách thì hỏi; không đọc trộn Bible/ảnh/giá của các khách để tổng hợp.

## Lưu việc và duyệt
- Chỉ tạo output trong folder đích hiện có người dùng giao hoặc Registry/campaign đã xác minh, không tạo campaign/folder để “cho đủ chuẩn”. Header theo SOP live, kèm client_key khi cần và danh sách nguồn. Đọc lại phần đã ghi.
- CONTROL RUN_LOG/APPROVALS/FEEDBACK_LOG theo schema đang có. Không ghi vào CSV local hoặc tab MOVED_*. Run ID/campaign ID/approval ID không hard-code; điều phối đọc lại ID trước ghi và kiểm tra sau ghi. Khi có người khác ghi đồng thời không bảo đảm cấp ID duy nhất: không đoán/ghi đè, nêu xung đột và chờ cơ chế phù hợp.
- Append log đúng run là thao tác nghiệp vụ; không đổi TEAM_ROLES, Registry routing, trần ngân sách hoặc danh sách người duyệt từ đề xuất của agent. Approval approved chỉ ghi sau quyết định thật của đúng người, gắn target + version đã trình bày. Bản đổi sau duyệt phải xem lại phạm vi duyệt. Riêng CIF mới đã được Reviewer PASS: Orchestrator đồng bộ đúng cột cif_doc_id theo quyền/workflow hoặc approval hiện hành, giữ bản cũ và readback theo [khung 2.5](agency-2.5-flow.md); không coi đó là quyền đổi folder/account/approver routing. Thiếu quyền thì báo chưa đồng bộ, không ngầm dùng con trỏ cũ.
- Theo [khung 2.5](agency-2.5-flow.md): Strategy/Research → Reviewer → G1 strategy → hỏi owner/nhận chọn tệp, offer, proof → CIF được kiểm → hướng creative → Reviewer → G2 chọn hướng → sản xuất → Reviewer → G3 bản cuối. Bảng content–cách phân phối cho owner chọn trước setup Ads chi tiết; lựa chọn có thể ghi trong gate hiện có, không tự thêm cột/gate mới vào CONTROL. Không bắt lại các gate đã có quyết định hợp lệ.
- Reviewer độc lập, chỉ PASS/REVISE theo stage; tối đa 2 vòng sửa nếu SOP hiện hành quy định. PASS không đồng nghĩa đã đăng/chạy. Plan A: người thực thi các thao tác đăng, Ads, chi tiền, gửi tin, xoá, đổi quyền. Không cài connector có quyền ghi bên ngoài như một phần của bộ skill.
- Feedback/memory theo SOP và quyền hiện hành; Coach là role qa-coach độc lập, chỉ gọi khi được yêu cầu. Approve/resume phải gắn đúng item/version và quyền theo [khung 2.5](agency-2.5-flow.md). Thay đổi tài liệu nguồn đã duyệt phải có chỉ đạo/approval đúng phạm vi; sửa tại mục gốc liên quan, giữ cấu trúc, ghi nhật ký và readback. Không tự sửa trong lượt đọc tình hình hay đề xuất.
- SĐT/tên khách cuối, token, CRM raw không đưa vào Brain/log/output. Dùng mã lead và số tổng; quyền đọc dữ liệu chi tiết xử lý tại nguồn được cấp riêng.

## Khi thiếu connector
Không coi cả hệ thống đã nối chỉ vì ID đọc được. Báo nguồn không truy cập, đề nghị export/link/context cần thiết và tiếp tục phần chat/local được phép. Không đổi nguồn chính sang Notion hay tạo dự án thay thế. Đây là việc chạy theo yêu cầu, không có tiến trình chờ nền.
