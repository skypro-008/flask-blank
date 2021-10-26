# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

# from flask import Flask
#
# from config import Config
#
# config = Config()
#
# app = Flask(__name__)
# app.url_map.strict_slashes = False
# app.config.from_object(config)
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)
