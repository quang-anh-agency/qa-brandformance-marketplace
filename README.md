# QA Brandformance — kho plugin nội bộ

Bộ marketing cho Quang Anh Agency, chạy theo Company OS 2.5: Điều phối → Strategy/Research → Reviewer → G1 → CIF → hướng Creative → Reviewer → G2 → sản xuất → Reviewer → G3 → Ads Plan → Reviewer → người duyệt/thực hiện → Reporting; Coach riêng khi được yêu cầu.

**Phiên bản phân phối 2.1.0.** Giữ nguyên 14 skill nghiệp vụ của bộ Codex 2.0.1; bổ sung một skill Setup và 13 cấu hình agent portable. Đây là kho private, không phải plugin công khai hoặc server chạy nền.

## Nhân viên cài lần đầu

1. Tài khoản GitHub của bạn phải được owner cấp quyền đọc repo. Kết nối GitHub trong chat và đăng nhập Git để tải repo là hai cơ chế riêng; nếu Codex không tải được private repo, hoàn tất đăng nhập Git theo cách được công ty cho phép. Không dán token vào chat hoặc URL.
2. Dùng Codex CLI có lệnh `plugin` để thêm kho và cài:

```bash
codex plugin marketplace add quanganhcetus-lab/qa-brandformance-marketplace --ref main
codex plugin add qa-brandformance@quang-anh-agency
```

Sau khi thêm kho, cũng có thể mở danh sách Plugins trên bản desktop được hỗ trợ, chọn nguồn **Quang Anh Agency**, rồi cài **QA Brandformance**. Khả năng hiện kho phụ thuộc phiên bản/client và policy tài khoản; chưa thấy thì mở lại app. CLI và app phải dùng cùng cấu hình máy.

3. Chạy **Setup** của plugin hoặc yêu cầu “Dùng qa-team-setup thiết lập bộ agent trên máy này”. Bước này cài riêng 13 agent; chỉ cài plugin chưa chứng minh đã có đủ agent. Cần Python 3.11 trở lên. Xem [chi tiết Setup](plugins/qa-brandformance/SETUP.md).
4. Mở chat mới, kết nối Google Drive bằng tài khoản của bạn và giao việc cho **QA Brandformance**. Chỉ dùng brand được cấp quyền. Không dùng tài khoản, token hoặc mật khẩu của owner.
5. Chạy thử một nhiệm vụ nhỏ trên brand được giao, kiểm nguồn, kết quả Reviewer và đúng người duyệt trước khi dùng rộng.

## Dùng hằng ngày

Giao việc qua `performance-mkt-qa`, nêu brand và yêu cầu. Ví dụ “Lên kế hoạch tuyển sinh Growee”; “Báo cáo tháng của Hoàng Mai”; “Viết thêm bài theo hướng H02 đã duyệt”. Điều phối chọn đúng agent, không chạy toàn đội cho mỗi câu hỏi. Tới điểm duyệt phải dừng. PASS không thay người duyệt và không phải bằng chứng đã đăng/chạy.

Mỗi người có chat riêng. Hồ sơ chung và bàn giao qua Drive đúng cấu trúc hiện có. Mỗi chiến dịch có một người phụ trách chính để tránh ghi log/ID đồng thời. Không tự sửa folder, Registry routing, quyền hoặc ngân sách.

## Cập nhật và gỡ

Làm mới kho bằng `codex plugin marketplace upgrade quang-anh-agency`, cập nhật/cài lại plugin theo client, mở chat mới. Nếu bản phát hành đổi agent thì chạy lại Setup, xem trước xung đột và sao lưu trước khi thay. Không mặc định mọi máy tự cập nhật ngay.

Gỡ plugin bằng `codex plugin remove qa-brandformance@quang-anh-agency`. Cấu hình agent được cài riêng nên không giả định tự bị gỡ cùng plugin. Khôi phục bằng ZIP do Setup trả về nếu các file chưa được sửa sau đó; không tự xoá agent hoặc công việc mới.

## Nguồn, dữ liệu và giới hạn

- Repo chỉ giữ quy trình, tài liệu phương pháp và cấu hình. Không đẩy hồ sơ khách hàng, nội dung chat, credential, raw CRM hoặc bản sao Drive vào đây. Drive bootstrap IDs trong profile là chỉ dẫn tìm nguồn, không cấp quyền truy cập.
- Bảng `SOURCE_MANIFEST.json` giữ hash nguồn nghiệp vụ để kiểm đối chiếu, không chứa đường dẫn máy owner. Không tự đổi core 14 skill trong lần đóng gói.
- Kiểm đóng gói: `python3 scripts/validate_package.py`. Kết quả cấu trúc không chứng minh mọi tài khoản nhân viên, connector ảnh/video hoặc Ads đã hoạt động.
- Tài liệu nền: [Plugin và marketplace](https://developers.openai.com/plugins/build/plugins), [Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents).
