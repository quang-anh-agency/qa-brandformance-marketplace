# Workflow — Input, công cụ và hàng chờ
Đây là workflow chung, không tạo thêm một agent kết nối bắt buộc.

## 1. Xác định nhu cầu dữ liệu
Gắn nhu cầu với doanh nghiệp/campaign và quyết định đang làm. Ghi dữ liệu tối thiểu, nguồn, kỳ, mức chi tiết và lý do; kiểm tra hồ sơ/công cụ đã có trước khi hỏi.
Công việc một lần có thể chỉ cần ảnh/CSV; công việc cập nhật thường xuyên có thể đáng kết nối. Đề xuất một hướng phù hợp nhất với nguồn lực, cùng phương án thay thế.

## 2. Chọn đường lấy dữ liệu
| Nhu cầu | Có thể đề xuất | Phương án SME chưa kết nối |
|---|---|---|
| Đọc spend, phân phối, kết quả Ads theo kỳ/creative | Ads MCP hoặc connector/API có quyền báo cáo tài khoản đúng doanh nghiệp | Export Ads Manager/CSV hoặc ảnh có kỳ và cột |
| Tìm quảng cáo/offer đối thủ | Link/giao diện Ads Library, nguồn công khai hoặc công cụ thực sự hỗ trợ đọc | Link quảng cáo, ảnh/video/copy do người dùng cung cấp |
| Nghiên cứu Page/content/cộng đồng | Google để tìm nguồn gốc, công cụ đọc web/MXH phù hợp, Page API khi có quyền và dữ liệu được hỗ trợ | Link công khai, ảnh, transcript, file tổng hợp |
| CIF từ lời khách, chất lượng lead, lý do mất | Inbox/Page connector hoặc Facebook API có quyền phù hợp; CRM/chat export được phép | Một số hội thoại/record đã chọn và lược thông tin riêng tư không cần thiết |
| Đến cơ sở, đơn, thực thu, mua lại | Dashboard/Google Sheets/CRM/POS nguồn gốc | Bảng record tối thiểu theo ngày/cơ sở/trạng thái |
| Proof, creative đã sản xuất | Thư mục local/Drive hoặc kho content đang dùng | File ảnh/video/link và thông tin nguồn được phép dùng |

Không giả định Ads MCP nào cũng đọc được Ads Library, inbox hoặc đơn hàng; không giả định dashboard có dữ liệu gốc/đúng attribution. Phân biệt Ads account, Page, inbox, CRM và POS. Nếu cần hướng dẫn API/tính năng cụ thể, kiểm tra tài liệu chính thức/phiên bản và quyền tại thời điểm dùng; không hard-code tên tool hoặc scope không xác minh.

## 3. Kiểm tra khả dụng và quyền
Phân biệt: chưa có công cụ / có công cụ nhưng chưa xác thực / đã kết nối nhưng thiếu quyền / có quyền nhưng không có dữ liệu cần / đã đọc thành công.
Chỉ nói đã kết nối/đã đọc khi có bằng chứng. Cài được MCP chưa chứng minh truy cập đúng doanh nghiệp.
Nếu người dùng đã cho phép đọc nguồn/phạm vi này và công cụ có sẵn, tiếp tục trong phạm vi đó; không xin duyệt lại vô cớ. Nếu cần cấp quyền mới, hỏi ngắn nguồn/tài khoản/phạm vi và hướng dẫn thiết lập.
Không nhận hoặc ghi token/mật khẩu trong chat, file output hoặc hàng chờ. Chỉ lấy trường/kỳ/hội thoại cần cho bài toán. Quyền đọc không phải quyền sửa Ads hoặc gửi tin.

## 4. Giữ công việc còn thiếu
Dùng [mẫu hàng chờ](../templates/hang-cho.md) ở chat nếu đang trao đổi, hoặc trong workspace khi được giao lưu tài liệu. Điều phối là đầu mối ghi; sub-agent trả yêu cầu chờ qua bàn giao. Skill gọi trực tiếp giữ vai trò đầu mối cho tác vụ đó.
Mỗi mục có dữ liệu cần, nguồn/kết nối, trạng thái, chủ trì nếu biết, câu hỏi quyết định, phần bị phụ thuộc, cách thay thế và điều kiện tiếp tục.
- **Cần input:** chờ thông tin/file người dùng có thể gửi.
- **Đề xuất kết nối:** chưa chốt có cần kết nối hay dùng file.
- **Chờ thiết lập/quyền:** cần người có quyền cấu hình/xác thực.
- **Sẵn sàng xử lý:** đầu vào đã có và quyền đủ; chưa đồng nghĩa đã chạy.
- **Hoàn tất:** ghi kết quả thực sự đọc được và giới hạn.
- **Bỏ qua:** người dùng chọn không lấy hoặc không cần nữa, ghi ảnh hưởng kết luận.
Mốc xử lý chỉ ghi khi được chốt hoặc là đề xuất. Không tự hứa sẽ chạy nền hoặc báo lại sau. Mỗi lượt mới có dữ liệu, đối chiếu mục liên quan rồi tiếp tục việc được giao; chưa có khả năng tự đánh thức thì nói rõ.

## 5. Tiếp tục và bàn giao
Khi có dữ liệu: kiểm tra đúng DN/kỳ/nguồn/định nghĩa, cập nhật trạng thái và quyết định phụ thuộc. Giữ nguồn, không sửa file gốc.
Nếu vẫn thiếu, nêu giới hạn và làm phần đủ căn cứ. Ví dụ chưa nối được inbox vẫn có thể đánh giá phân phối Ads; chưa có khách trả tiền thì chưa tính CAC khách mua.
Kết thúc bằng việc cần người dùng cung cấp/chọn nếu thực sự có, không kèm một danh sách kết nối dài mặc định.
