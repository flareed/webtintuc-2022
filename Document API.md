1. Lấy danh sách các thể loại
    Url: api/categories/
    Method: GET
    Response status: 200
    Response data: {
                     "id": int,
                     "name": string,
                     "description": string,
                     }

2. Lấy danh sách tất cả các bài báo, mỗi trang hiển thị 10 bài
    Url: api/articles/
    Method: GET
    Response status: 200
    Response data: {
                    "count": int,
                    "next": string,
                    "previous": string,
                    "results": [{
                        "id": int,
                        "category": string,
                        "author": string,
                        "title": string,
                        "content": text,
                        "date_posted": datetime,
                        "img": string,
                    }]
    }

3. 
