# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример

# @book_ns.route('/')
# class BooksView(Resource):
#     def get(self):
#         all_books = book_service.get_all_books()
#         return books_schema.dump(all_books), 200
#
#     def post(self):
#         req_json = request.json
#         new_book = book_service.create_book(data=req_json)
#         return "", 201
