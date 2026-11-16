# Đọc nguồn theo từng kênh
Đây là hướng dẫn quan sát, không phải cam kết công cụ luôn đọc được nền tảng. Khi giao diện/tính năng thay đổi, kiểm tra hiện trạng, không bịa thao tác hoặc tên API.

## Chọn đường đọc: web → trình duyệt trong app → phiên Chrome khi cần
1. **Nguồn công khai:** dùng công cụ tìm kiếm/đọc web trước để tìm brand, link gốc và thông tin có thể trích xuất. Không mở Chrome chỉ để tìm Google. Nếu không có công cụ Google, dùng tìm kiếm khả dụng và ghi đúng nguồn/cách tìm.
2. **Trang động cần tương tác:** ưu tiên trình duyệt trong GPT/Codex, hoặc trình duyệt riêng tương đương của runtime, nếu công cụ thực sự khả dụng. Dùng khi cần cuộn, mở bài, xem video, comment hoặc bộ lọc Ads Library. Không mặc định phải kiểm tra Chrome/tab người dùng trước bước này.
3. **Nguồn cần đăng nhập/quyền:** chỉ dùng phiên Chrome/extension của người dùng khi phiên đó có quyền cần thiết hoặc người dùng chỉ định. Tab mở trên máy chưa chứng minh công cụ đọc được tab. Hai trình duyệt không mặc nhiên chia sẻ đăng nhập. Không hứa chuyển sang Chrome hoặc đăng nhập sẽ chắc chắn khắc phục lỗi.
4. **Thiếu công cụ/quyền:** chọn nguồn khác có giá trị cho cùng câu hỏi và ghi giới hạn; chỉ hỏi người dùng hỗ trợ tối thiểu khi nguồn thiếu thật sự cần cho quyết định. Không mặc định bắt mở tab, cài extension hay xuất/chụp toàn bộ dữ liệu.

### Điểm dừng khi lỗi
- Phân biệt lỗi kết nối công cụ/transport, trích text, trang đang tải, robots/throttling, yêu cầu đăng nhập và thiếu quyền nhóm. Ghi đúng đường đọc và lỗi quan sát được; không kết luận cả nền tảng không đọc được.
- Với một lỗi công cụ, chỉ thử khắc phục thêm **một lần có lý do cụ thể**. Nếu lỗi tiếp diễn, dừng đường đọc đó, báo ngắn phần chưa đọc, chuyển nguồn khác và ghi hàng chờ. Không lặp inventory/tab/navigation hoặc liên tục mở cửa sổ mới để thử vận may.
- Extension/transport lỗi không phải lý do tự chuyển sang điều khiển ứng dụng Chrome bằng bàn phím/screenshot. Chỉ cân nhắc điều khiển ứng dụng khi người dùng yêu cầu hoặc có nhu cầu cụ thể mà các đường đọc ưu tiên không đáp ứng, công cụ hoạt động và lợi ích rõ; không dùng làm fallback mặc định cho nghiên cứu công khai.
- Giữ nguyên tab/công việc khác của người dùng; nếu phát hiện người dùng đang tương tác cùng phiên, dừng thao tác xung đột. Tái sử dụng tab phù hợp thay vì tạo nhiều tab trùng.
- Tiếp tục phần đủ dữ liệu và trả báo cáo trong phạm vi thực đọc được. Kênh chưa đọc được là khoảng trống, không được lấp bằng suy đoán hoặc nguồn ngoại không phù hợp.

### Đọc đúng nội dung và quyền
- Trang động có thể cần tải tiếp, cuộn, mở “Xem thêm”, video hoặc comment. Nếu accessibility chỉ có tiêu đề/link, dùng DOM hoặc screenshot được công cụ của trình duyệt đang dùng hỗ trợ khi có ích; căn cứ trạng thái mới quan sát, không đoán nút/nội dung. Điểm dừng trên vẫn áp dụng.
- Giữ phạm vi chỉ đọc: không join, đăng, gửi tin hoặc đổi tài khoản/quyền để thử. Chỉ xác nhận đọc video/comment khi nội dung đó thực sự được quan sát; đọc danh sách nhóm hoặc bài seller chưa phải đã nghiên cứu thảo luận khách.

## Facebook Page đối thủ và brand cùng ngành
- Chủ động tìm Page, tên biến thể và cơ sở liên quan; đối chiếu website/địa chỉ/liên kết để tránh trộn brand, chi nhánh hoặc Page đăng lại. Giữ cả đối thủ trực tiếp và brand tham khảo có lý do.
- Đọc giới thiệu, bài ghim, danh mục/dịch vụ, sản phẩm/offer được đẩy và đường liên hệ/chuyển đổi. Ghi điều brand công bố và phần chưa xác minh.
- Phân tích tuyến content trong kỳ quan sát: vấn đề/nhu cầu, giáo dục lựa chọn, demo/test, công trình/sản phẩm thực tế, trải nghiệm khách, bằng chứng năng lực, chương trình bán hàng hoặc tuyến khác tìm thấy. Không ép mọi Page vào cùng một bộ tuyến.
- Chọn bài/video đại diện để bóc tệp/bối cảnh, angle, hook chữ/hình/lời, mạch thuyết phục, proof, format, CTA. Ghi cách các tuyến bổ trợ và khoảng trống quan sát được. Một mẫu có thể kết hợp nhiều chiều khách.
- Đối chiếu Page với Ads Library: content nào được xác nhận đang quảng cáo, offer/thông điệp/creative giống hay khác. Không suy bài nhiều tương tác là Ads hoặc bài ít tương tác là không hiệu quả.
- Nếu nhận xét nhịp đăng/tỷ trọng tuyến, dùng ngày/số bài thực đã lấy mẫu và ghi giới hạn. Không suy lịch vận hành từ vài bài ghim. Comment/reply là phản hồi bổ sung, không thay phần phân tích Page.

## Facebook Ads Library
- Tìm đúng Page/brand và tên biến thể; dùng thị trường/bộ lọc phù hợp khi có, ghi bộ lọc/ngày.
- Mở creative gốc/chi tiết khi truy cập được: ảnh/video/copy, ưu đãi/điều kiện, đối tượng được nội dung gọi, CTA và trang đích.
- Lưu ID/link quảng cáo nếu hiển thị, Page, ngày bắt đầu/trạng thái đúng như giao diện, sản phẩm, offer, angle, proof, format và variant.
- Gom theo cơ chế thu hút/nhiệm vụ thuyết phục, không tính mỗi ad ID là một angle. Ads có thể bổ trợ nhau.
- Thư viện quảng cáo không tự cung cấp comment, doanh số, CAC/ROAS của quảng cáo thương mại. Chỉ ghi số/đặc điểm thực sự hiển thị.
- Không có kết quả có thể do tên/bộ lọc/quyền/trạng thái; không kết luận “brand không chạy Ads”. Thử tên/nguồn xác minh hợp lý rồi ghi giới hạn.
- Nếu chỉ tìm được caption trên Page thì đó là content Page, chưa xác nhận đang chạy Ads Library.

## TikTok: tìm kênh → phân tích kênh/tuyến → bóc video → đối chiếu phản hồi
- Chủ động search bằng tên brand, sản phẩm/dịch vụ, vấn đề/câu hỏi mua, địa bàn khi liên quan; khám phá kênh đối thủ, brand cùng ngành và creator liên quan. Không chỉ chờ link người dùng mở sẵn. Các kênh đề xuất là đầu mối để xác minh, chưa tự là đối thủ phù hợp.
- Xác minh kênh liên quan brand bằng bio, liên kết, địa chỉ hoặc đối chiếu nguồn chính thức; tài khoản đăng lại/affiliate ghi riêng.
- Phân tích cấp kênh: khách/bối cảnh được gọi, định vị/cách thể hiện, sản phẩm/offer, nhân vật dẫn, phong cách, các tuyến content lặp lại, cách dẫn người xem sang hỏi mua/tư vấn. Ghi vai trò từng tuyến trong thu hút, giải thích, tạo tin tưởng và chuyển đổi; đó là suy luận có dẫn mẫu, không phải khẳng định kế hoạch nội bộ của brand.
- Chọn video đại diện nhiều tuyến, bài gần kỳ nghiên cứu, mẫu nổi bật và mẫu thông thường; bài ghim ghi riêng. Không chỉ chọn video nhiều view hoặc nhiều comment. Tỷ trọng/nhịp đăng chỉ kết luận trong mẫu có ngày và phạm vi.
- Nếu xem được video: ghi hook nói/hình, tình huống, thông điệp/mạch, proof, offer và CTA; nếu chỉ có caption/thumbnail thì giới hạn phân tích ở đó.
- Bóc cách thực hiện: mở đầu bằng vấn đề hay kết quả, người nói/demo/UGC/công trình, trình tự luận điểm, bằng chứng và lời kêu gọi. Gom video cùng cơ chế thành angle/tuyến, giữ khác biệt format và variant; không coi mỗi video là một insight hoặc mỗi format là một angle.
- Đọc comment/reply thực sự mở được: hỏi giá, nơi mua, chất lượng, so sánh, trải nghiệm, phản đối, lời khen/chê và cách brand trả lời. Nếu chỉ thấy vài comment nổi bật thì ghi phạm vi.
- Ghi link video/comment hoặc vị trí có thể kiểm tra, ngày nếu biết, câu gốc ngắn và tình trạng người mua chưa xác minh. Không bịa transcript từ thumbnail, không đoán comment sau màn hình đăng nhập.
- Khi chuyển video/tự phát sang bài khác, kiểm tra lại link/caption trước khi gắn nhận xét hoặc comment vào nguồn. Mở được player và nhìn một vài khung hình chưa đồng nghĩa đã nghe/xem hết mạch video.

## Google và nguồn gốc
- Tìm bằng tên/sản phẩm + giá/review/so sánh/địa bàn/câu hỏi mua; dùng tên thay thế khi có.
- Kết quả tìm kiếm là bước khám phá. Mở website/Page/bài gốc để kiểm tra nội dung, ngày và vai trò người nói; chỉ có snippet thì ghi rõ.
- Website/Page: kiểm tra danh mục, giá/đơn vị, định vị, điều kiện, quy trình, bảo hành/proof được công bố. Đây là lời thương hiệu, chưa phải xác nhận thực hiện hoặc lời khách.
- Giá cần phạm vi: sản phẩm, vật liệu/cấu hình, mét/bộ/lần, đã gồm gì, điều kiện/thời điểm. Không xếp brand “rẻ nhất” khi báo giá khác phạm vi.
- Có thể tìm báo cáo/mùa vụ/xu hướng khi câu hỏi cần và có nguồn phù hợp; không mặc định dựng TAM/SAM/SOM hay forecast để làm báo cáo SME có vẻ đầy đủ.
- Công cụ tìm kiếm thay thế phải được gọi đúng, không ghi đã dùng Google nếu thực tế không có.

## Group Facebook
- Tìm nhóm đúng ngành/nhu cầu/địa bàn và bài hỏi thật: xin tư vấn, so sánh, lựa chọn, trải nghiệm, khiếu nại hoặc lý do mua.
- Đọc bài gốc khách tự đăng, không chỉ comment: hoàn cảnh, giải pháp đang cân nhắc, ngân sách tự nêu, tiêu chí, trải nghiệm và điều chưa giải quyết. Mở “Xem thêm” khi có, giữ link và ngôn ngữ nguyên văn cần thiết. Bài gốc có giá trị độc lập với lượng comment.
- Phân biệt bài khách, bài bán hàng, seeding và reply của seller; không coi câu quảng cáo là câu khách.
- Xét cả mục đích nhóm và người đăng: nhóm xưởng/B2B có thể dùng nghiên cứu nguồn cung/cạnh tranh, chưa đại diện khách tiêu dùng. Nếu toàn seller, tìm thêm cộng đồng người dùng phù hợp; không lấy dữ liệu seller lấp CIF.
- Khi đọc được, ghi link bài/comment, loại nhóm/phạm vi và đoạn quan sát; không thu cả danh sách thành viên hoặc thông tin cá nhân không cần.
- Nhóm riêng chỉ đọc bằng quyền/session được cấp sẵn; không tự join, đăng bài, nhắn tin hoặc vượt quyền. Chỉ thấy tiêu đề/preview thì chưa phải đã đọc thảo luận.
- Tìm được nhóm nhưng không xem được bài thì trạng thái “tìm thấy, chưa đọc được”, không phải “không có nhu cầu”.

## Google Maps review
- Xác minh đúng cơ sở/brand/địa điểm; không trộn review chi nhánh hoặc brand trùng tên.
- Khi truy cập được, xem cả đánh giá tốt/xấu và nhiều tình huống liên quan, chú ý ngày và phản hồi của chủ cơ sở.
- Ghi điểm khách hài lòng/bất mãn, tiêu chí chọn, bước trải nghiệm bị vướng và bối cảnh. Điểm sao là tín hiệu tổng hợp, không tự chứng minh nguyên nhân hay doanh thu.
- Review là lời công khai; chưa chắc xác minh đã mua/sử dụng, có thể thiên lệch. Không suy toàn bộ thị trường từ một cơ sở hay vài review.
- Snippet Google có trích review chưa đồng nghĩa đã đọc trang Maps và toàn bộ review; ghi đúng mức.

## Nguồn bổ sung theo mô hình
- Sàn bán hàng: cấu hình/giá/đánh giá/Q&A và điều kiện; tách shop/phiên bản/người mua chưa xác minh.
- F&B: ứng dụng đặt món, menu/review và trải nghiệm liên quan khi có quyền đọc.
- YouTube/diễn đàn: giải thích dài, demo, thảo luận chuyên biệt; không giả xem video khi chỉ có bài giới thiệu.
- Nguồn nội bộ: inbox, call, tư vấn, CRM/POS, lý do mua/chưa mua do người dùng cấp; giữ nhãn nguồn và quyền.
Không biến việc thiếu nguồn nội bộ thành lý do dừng nghiên cứu công khai.

## Bằng chứng và lỗi truy cập
Mỗi nguồn cần link/đường dẫn, ngày quan sát, thị trường, loại nguồn và mức đã đọc: đầy đủ trong phạm vi quan sát / một phần / snippet / tìm thấy chưa đọc / bị chặn / chưa tìm thấy sau khi thử / chưa thử / không phù hợp.
Ghi công cụ/đường đọc và điều quan sát, không chỉ đánh dấu xanh có nền tảng. Một công cụ đã cài hoặc một link mở được chưa chứng minh đã đọc comment/video.
Khi bị chặn: thử đường công khai/connector/browser có quyền phù hợp nếu có; nếu vẫn không được, nêu input hoặc công cụ cần để tiếp tục và làm phần độc lập. Không lặp cùng lỗi vô hạn, không thay bằng nguồn ngoại rồi che mất khoảng trống.
