# Triển khai Meta Ads tinh gọn

## Bắt đầu từ content và lựa chọn của user
Dùng [content → chiến thuật Ads](content-va-chien-thuat-ads.md) trước setup chi tiết: hỏi điều kiện triển khai, đề xuất cách dùng từng content trong hệ thống rồi chờ user chọn. Khi user đã chọn rõ thì đi tiếp đúng phạm vi; không biến yêu cầu lập plan thành được phép chạy thật.

## Chọn cấu trúc theo bài toán
Đọc mô hình/đường chuyển đổi, mục tiêu, địa bàn, chu kỳ cân nhắc, nguồn lực, creative và khả năng nhận khách trước khi đề xuất campaign.
Chọn đơn giản đủ dùng; tách thêm khi mục tiêu, địa bàn cơ sở, offer, cách chuyển đổi, phân bổ ngân sách hoặc cách học dữ liệu cần khác biệt. Không buộc “mỗi tệp CIF = một ad set”.
Không tự mặc định website/pixel/CAPI hoặc nhiều tầng funnel. Đề xuất tracking vừa đủ để biết chi tiền, hành động và kết quả kinh doanh; đào sâu khi yêu cầu/case cần.

## Cách làm Quang Anh đã chia sẻ — có điều kiện
Ở nhiều case local như GS: thường 1 campaign, 1 ad set, nhiều ads; tập trung sản xuất angle/creative để hệ thống phân phối. Không dành phần lớn công sức chia interest khi địa bàn hẹp.
Biến cấp ad set được nêu: bật/tắt **Advantage+ Audience**; không có mẫu số chung, cần kiểm chứng từng case.
Đây không phải công thức bắt mọi ngành dùng. Mèo Béo có nhiều hướng/campaign và bán kính theo cơ sở; sản phẩm giá trị cao có chu kỳ/đường đi riêng. Case thiếu cấu trúc cụ thể thì phải nêu chưa được giảng viên cung cấp.

“Content chính là target” là ưu tiên phương pháp: lời gọi, nhân vật, sản phẩm, tình huống và proof giúp đúng khách nhận ra mình. Không suy ra nội dung sẽ tự đảm bảo địa bàn, phân phối hay chuyển đổi; các giới hạn phục vụ vẫn phải cấu hình phù hợp.

## Setup cần bàn giao
- Business/campaign ID, bài toán, sản phẩm/offer, nhóm/bối cảnh creative.
- Hành động tối ưu và nơi chuyển đổi phù hợp (Messenger, lead, offline…); kiểm tra lựa chọn hiện có trong tài khoản.
- Page, tài sản, quyền, thanh toán theo quyền thực tế.
- Địa bàn/phạm vi, ngân sách, lịch, placement và lý do.
- Creative ID, copy, CTA, tin nhắn mở đầu/form và người tiếp nhận.
- Custom/retargeting khi có nguồn hợp lệ, quy mô phù hợp và mục đích. Không mặc định cần tạo mọi loại tệp.
- Đặt tên nhận diện cơ sở/dịch vụ/angle/variant; không cần naming quá phức tạp.
- Kiểm tra hiển thị, điều kiện offer, đường đi tiếp nhận, giới hạn chi tiêu và cách record trước publish.

Tính năng Meta, cách đặt mục tiêu, audience expansion và giao diện có thể thay đổi. Khi hướng dẫn thao tác cụ thể, kiểm tra tài liệu Meta chính thức/giao diện hiện tại nếu có công cụ; không có thì giao logic setup và ghi phần cần xác nhận. Không giả vờ đã tạo campaign hoặc audience.

## Phân phối và test
Nhiều ads cùng nhóm không tự là thí nghiệm chia đều. Đọc spend, mức phân phối, thời gian, offer, mục tiêu và chất lượng khách; phân biệt hệ thống lựa chọn phân phối với thử nghiệm có kiểm soát.
Nếu so bật/tắt Advantage+ Audience, mô tả phương án chạy, khác biệt, điều kiện giữ tương đương và khả năng trùng tệp; không đảm bảo kết luận nhân quả chỉ từ hai nhóm chạy khác thời điểm.
Ngân sách test, thời gian review và giới hạn lỗ do doanh nghiệp chốt hoặc được đề xuất có nhãn. Không đặt quy tắc “tắt sau X tiền/ngày” cho mọi ngành.

## Retargeting
GS dùng người xem nội dung/đã nhắn Page để tiếp tục xem nội dung dựa CIF. Chọn nội dung bổ sung proof, giải đáp và nhu cầu khác phù hợp; không chỉ lặp ưu đãi. Cửa sổ, exclusions, quy mô và nguồn tạo tệp cần kiểm tra khả dụng tại thời điểm setup.
Local thường có trùng người giữa nhiều hướng creative; không tách bằng mọi giá. Tuy nhiên không mặc định trùng luôn có lợi: xem frequency, phản hồi, chi phí và khả năng tiếp cận trong vùng phục vụ.

## Ranh giới hành động
Lập plan, tạo tài liệu và kiểm tra dữ liệu khác publish/thay ngân sách. Bản Kit không có connector. Nếu người dùng muốn thao tác tài khoản, xác định quyền và phạm vi rõ trước khi thực hiện. Không xin lại khi đã có phép cụ thể, nhưng không mở rộng phép từ “viết plan” thành “chạy thật”.
