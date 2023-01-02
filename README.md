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

<b>Bước 0</b>: Cài đặt theo thứ tự: `npm, node.js` ([link](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)) -> `vue` ([link](https://vi.vuejs.org/v2/guide/installation.html#NPM)) -> `django rest framework`

<b>Bước 1</b>: Chạy Backend (theo hướng dẫn [Readme](/Backend/Readme-Backend.md))
- Backend sau khi chạy sẽ ở port 8000 nên khi chạy frontend sẽ chọn port khác 8000

<b>Bước 2</b>: Thêm data vào csdl ([data](https://studenthcmusedu-my.sharepoint.com/:f:/g/personal/20120393_student_hcmus_edu_vn/EvZ8g_ChoipJgAhPHWTNiNQBCwMzY6MtSdjWditmw1PV-w?e=6GmlhO), link hướng dẫn [import csv file to mysql table](https://www.mysqltutorial.org/import-csv-file-mysql-table/))

- Dữ liệu `articles_data.csv` của table `myapp_article`
- Dữ liệu `categories_data.csv` của table `myapp_category`

<b>Bước 3</b>: Chạy Frontend `news-website`
```
npm install \\chạy lệnh này lần đầu tiên khi clone project về, lần thứ 2 không cần chạy nữa
npm run serve -- --port 3000 \\có thể thay đổi port
```

<b>Bước 4</b>: Chạy Frontend `author-website` trên port khác
```
npm install \\chạy lệnh này lần đầu tiên khi clone project về, lần thứ 2 không cần chạy nữa
npm run serve -- --port 4000 \\có thể thay đổi port
```

<b>Bước 5</b>: Nếu cần thì thêm data article thông qua `author-website`
