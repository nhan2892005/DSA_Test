## 1. Giới thiệu về Make và Valgrind

### 1.1. **Make** – Công cụ quản lý biên dịch

**Make** là một công cụ tự động hóa quá trình biên dịch chương trình. Nó giúp chỉ biên dịch lại các phần thay đổi trong mã nguồn, tiết kiệm thời gian khi làm việc với các dự án lớn.

- **Cài đặt Make trong WSL**:
  
  ```bash
  sudo apt update
  sudo apt install make
  ```

- **Sử dụng cơ bản**:
  - **Makefile**: Chứa các quy tắc biên dịch (rules), mô tả cách các tệp `.cpp` được biên dịch thành `.o` và liên kết thành chương trình thực thi.
  - Cấu trúc cơ bản của Makefile:
    ```make
    target: dependencies
        command
    ```

### 1.2. **Valgrind** – Công cụ kiểm tra rò rỉ bộ nhớ

**Valgrind** là công cụ kiểm tra lỗi bộ nhớ trong chương trình C++, giúp phát hiện các lỗi như rò rỉ bộ nhớ (memory leaks), truy cập vùng nhớ ngoài phạm vi.

- **Cài đặt Valgrind trong WSL**:
  
  ```bash
  sudo apt install valgrind
  ```

- **Cách sử dụng**:
  - Kiểm tra bộ nhớ cho chương trình `program` với tham số `demo`:
  
    ```bash
    valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./program demo
    ```

---

## 2. File cấu hình Makefile và cách hoạt động

### 2.1. **Makefile** trong dự án của bạn

Tôi sẽ cung cấp file Makefile [ở đây](Makefile), bạn có thể dùng và chạy thử. Sau đây là một vài giải thích cho các dòng lệnh:

**Giải thích cấu trúc:**

- **`$(TARGET)`**: Chương trình thực thi cuối cùng (multilayer_perceptron).
- **`$(ANN_SOURCES)`** và **`$(USER_SOURCE)`**: Các tệp nguồn C++ cần biên dịch.
- **`$(ANN_OBJECTS)`** và **`$(USER_OBJECT)`**: Tạo tệp `.o` từ các tệp nguồn.
- **`clean`**: Xóa các tệp thực thi và `.o` khi không còn cần thiết.

### 2.2. Tích hợp với Visual Studio Code

**VSCode** cung cấp cách dễ dàng để chạy các tác vụ **Makefile** và kiểm tra bộ nhớ với **Valgrind** thông qua các tệp cấu hình `tasks.json` và `launch.json`.

#### **tasks.json** – Thiết lập quy trình build và kiểm tra

[Đây là đường dẫn tới file tasks.json](.vscode/tasks.json)

**Một số chức năng được cấu hình trong file tasks.json**

- **`Make Build`**: Sử dụng **Makefile** để biên dịch chương trình.
- **`Check memory leaks`**: Sử dụng **Valgrind** để kiểm tra rò rỉ bộ nhớ.

#### **launch.json** – Cấu hình debugger

[Đây là đường dẫn tới file tasks.json](.vscode/launch.json)

Ngoài việc định nghĩa chức năng debug, launch còn định nghĩa được những tasks cần làm trước và sau khi debug

- **`preLaunchTask`**: Tự động biên dịch chương trình trước khi debug.
- **`postDebugTask`**: Sau khi debug, chạy **Valgrind** để kiểm tra lỗi bộ nhớ và dọn dẹp các file.
