# -*- coding: utf-8 -*-
import os


class DevConfig:

    DEBUG = os.environ.get('DEBUG', True)
    PORT = os.environ.get('PORT', 9970)
    HOST = os.environ.get('HOST', '0.0.0.0')

    db_name = os.environ.get('DB_NAME', 'gpk')
    db_user = os.environ.get('DB_USER', 'valy')
    db_password = os.environ.get('DB_PASSWORD', 'Elmurza0506')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', 5432)

    SECRET_KEY = os.urandom(24)
    FLASK_ADMIN_SWATCH = 'paper'


    @property
    def alchemy_url(self):
        return f'postgresql+psycopg2://{self.db_user}:{self.db_password}@' \
               f'{self.db_host}:{self.db_port}/{self.db_name}'


config = DevConfig()
