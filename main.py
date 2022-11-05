from website import app
from website import views
from config import host, port

import logging
logging.basicConfig(filename='example.log', format='%(levelname)s %(asctime)s %(message)s', datefmt='%H:%M:%S %d/%m/%Y %p', encoding='utf-8', level=logging.DEBUG)

if  (__name__ == '__main__'):     
    logging.info(f'App Started on {host}:{port}')

    app.run(host=host, port=port)

    