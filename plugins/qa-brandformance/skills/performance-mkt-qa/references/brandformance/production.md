# Sản xuất ảnh và video trong Codex

Đọc [hợp đồng](integration.md) và [chọn hướng/nguyên liệu QA](../creative-san-xuat.md). Chỉ sản xuất hướng và định dạng đã chọn, theo ảnh/logo/footage được cấp. Nguồn tài sản chỉ của đúng brand/client; tên file local có brand/client/run để tránh lẫn. Đầu ra local là workspace sản xuất, Drive vẫn là nguồn chính thức; không tự tạo folder trên Drive.

## Ảnh
Kiểm tra ảnh sản phẩm thật/logo gốc, thông điệp/chữ và Identity đã duyệt. Với yêu cầu tạo/chỉnh bitmap bằng AI, dùng skill/tool imagegen hiện có và đọc hướng dẫn của nó; giữ sản phẩm thật và dùng tham chiếu đúng nguồn. Không dùng Python để chỉnh ảnh AI khi hướng dẫn công cụ yêu cầu imagegen. Với thiết kế dựa trên tài sản sẵn có/bố cục chữ, có thể dựng HTML/CSS hoặc công cụ đồ hoạ rồi xuất PNG khi công cụ thực tế hỗ trợ; không bắt buộc AI cho mọi ảnh.

Kích thước theo placement/brief. Chữ Việt đủ dấu, không tràn, tương phản dễ đọc, đúng giá/điều kiện, logo không méo. Mở ảnh xuất ra để xem thật trước khi báo hoàn tất. Có file output mới được ghi đã xuất; chỉ prompt/brief thì gọi đúng là brief. Không tạo testimonial hoặc proof giả. Lưu source chỉnh được khi có ích và đúng phạm vi.

## Video
Video Editor chỉ nhận kịch bản đã chọn và footage thật. Kiểm tra công cụ (`ffmpeg`/`ffprobe`/renderer) và footage ở máy đang chạy; không giả máy nhân viên có bộ Remotion của owner. Thiếu footage: trả shot list/phần cần quay và trạng thái chờ, không tạo video người/sản phẩm giả để thay.

Từ thông số/âm thanh/thoại nguồn lập EDL: file, in/out, cảnh/đích, lời/chữ, phụ đề, âm thanh có quyền, CTA. Sau khi dựng, kiểm tra thời lượng, tỷ lệ, crop, phụ đề/giá/logo, âm thanh và sự khớp với kịch bản. Kiểm metadata, xem frame ở hook/chuyển cảnh/CTA và phần có chữ; kiểm âm thanh thực nếu có công cụ nghe. Nêu giới hạn QA nếu chưa thể xem/nghe đủ. Có file video mới được ghi rendered; không coi EDL là thành phẩm.

## Bàn giao
Content/creative ID → ảnh/footage/logo source → kích thước/thời lượng → file thật và source → điều đã kiểm/phần còn thiếu → link Drive nếu upload đã hoàn tất/readback. Dùng đường dẫn trong workspace hiện tại, không hard-code máy owner. Upload vào folder được giao nếu công cụ/quyền cho phép, không tự chuyển sang browser hay chia sẻ công khai để né lỗi. Đăng bài/gửi khách là thao tác khác.
