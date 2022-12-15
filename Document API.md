1. Lấy danh sách các thể loại
    Url: api/categories/
    Method: GET
    Response status: 200
    Response data: {
                     "id": int,
                     "name": string,
                     "description": string,
                     }

2. Lấy danh sách tất cả các bài báo, mỗi trang hiển thị 20 bài
    Url: api/articles/?page=?
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


3. Truy cập chi tiết từng bài báo
    Url: api/articles/{article_id}
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

4. Lấy danh sách bài báo của một thể loại
    Url: api/categories/{category_id}/articles/
    Method: GET
    Response status: 200
    Response data: {
                    
                        "id": int,
                        "category": string,
                        "author": string,
                        "title": string,
                        "content": text,
                        "date_posted": datetime,
                        "img": string,
    }

5. Tìm kiếm danh sách các bài báo theo từ khoá
    Url: api/articles/?q= {key word}
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


