# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

# from flask import Flask
# from flask_restx import Api
#
# from config import Config
# from views.books import book_ns
#
# config = Config()
#
# app = Flask(__name__)
# app.url_map.strict_slashes = False
# app.config.from_object(config)
#
# api = Api(app)
#
# api.add_namespace(book_ns)
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)
