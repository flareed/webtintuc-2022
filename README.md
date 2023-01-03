# News website

Đồ án cuối kỳ Nhập môn công nghệ phần mềm

## Thành viên nhóm

| MSSV  | Họ và tên |
| ------------- | ------------- |
| 20120339  | Nguyễn Nhật Nguyên  |
| 20120393  | Huỳnh Minh Tú  |
| 20120295  | Ngô Võ Quang Huy  |
| 20120556  | Văn Đình Minh Quân  |

## Cài đặt và chạy project

### Bước 0: Cài đặt tool, các thư viện cần thiết
**python 3.10.x**
- Windows: https://www.python.org/downloads/windows/
- Linux: https://www.python.org/downloads/source/
- **Chọn cài pip trong lúc cài.**

**npm (node packet manager)**

 - Để tránh gặp lỗi khi dùng node.js, chúng ta sẽ dùng nvm (node version manager) để cài node.js.
    Windows: https://github.com/coreybutler/nvm-windows/releases
 - Tải file setup.exe về, rồi cài.
 - Sau đó mở command line (hoặc powershell) với admin mode rồi gõ các dòng lệnh sau: 
    `nvm install 18.12.1` 
    `nvm use 18.12.1`
    
 **vuejs**
 
 - Mở commad line (hoặc powershell) và chạy các dòng lệnh sau:
`npm install vue`
`npm install -g @vue/cli`

**django rest framework**

- Mở commad line (hoặc powershell) và chạy các dòng lệnh sau: `pip install djangorestframework`

### Bước 1: Tiến hành clone project

- Vào thư mục cần lưu và chạy lệnh `git clone https://github.com/flareed/webtintuc-2022` trên command line

### Bước 2: Setup Backend

- Sử dụng vscode để mở thử mục Backend trong project vừa mới clone về
- Chạy lệnh `pip install -r requirements.txt` để cài đặt các thư viện cần thiết
- Mở MySQL và tạo database mới với thông số như sau:

```
    Open MySQL --> Create a new database, set:
        Name database: article_website
        Charset: utf8mb4
        Collation: utf8bm4_unicode
```

- Trong file `article_website/settings.py` thay đổi **USER, PASSWORD** giống với mySQL đang chạy trên máy của bạn

- Trở lại terminal vscode, chạy các lệnh sau:

```
py manage.py makemigrations myApp
py manage.py migrate
```

- Thêm data vào csdl ([data](https://studenthcmusedu-my.sharepoint.com/:f:/g/personal/20120393_student_hcmus_edu_vn/EvZ8g_ChoipJgAhPHWTNiNQBCwMzY6MtSdjWditmw1PV-w?e=6GmlhO), link hướng dẫn [import csv file to mysql table](https://www.mysqltutorial.org/import-csv-file-mysql-table/))

- Cuối cùng chạy lệnh `python manage.py runserver` trên terminal vscode để chạy server (mặc định ở port 8000)

### Bước 3: Setup Frontend

- Dùng vscode để mở thự mục Frontend (tổng cộng có 3 chương trình vscode khác nhau: Backend, Frontend news-website, Frontend author-website)

- Chạy Frontend `news-website` (Backend sau khi chạy sẽ ở port 8000 nên khi chạy frontend sẽ chọn port khác 8000)
```
npm install \\chạy lệnh này lần đầu tiên khi clone project về, lần thứ 2 không cần chạy nữa
npm run serve -- --port 3000 \\có thể thay đổi port
```

- Chạy Frontend `author-website` trên port khác
```
npm install \\chạy lệnh này lần đầu tiên khi clone project về, lần thứ 2 không cần chạy nữa
npm run serve -- --port 4000 \\có thể thay đổi port
```

### Bước 4: Nếu cần thì thêm data article thông qua `author-website`
