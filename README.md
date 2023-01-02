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

### Thứ tự các bước

- Bước 0: Cài đặt theo thứ tự: npm, node.js ([link](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)) -> vue ([link](https://vi.vuejs.org/v2/guide/installation.html#NPM)) -> django rest framework
- Bước 1: Chạy Backend (theo hướng dẫn [Readme](/Backend/Readme-Backend.md))
- Bước 2: Thêm data vào csdl ([data](https://studenthcmusedu-my.sharepoint.com/:f:/g/personal/20120393_student_hcmus_edu_vn/EvZ8g_ChoipJgAhPHWTNiNQBCwMzY6MtSdjWditmw1PV-w?e=6GmlhO), link hướng dẫn [import csv file to mysql table](https://www.mysqltutorial.org/import-csv-file-mysql-table/))
- Bước 3: Chạy Frontend news-website (Chạy lần lượt: npm install, npm run serve -- --port 3000)
- Bước 4: Chạy Frontend author-website trên port khác (Chạy lần lượt: npm install, npm run serve -- --port 4000)
- Bước 5: Nếu cần thì thêm data article thông qua author-website
