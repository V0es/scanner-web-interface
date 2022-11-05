from website import app
from website import views
from config import host, port

import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

if  (__name__ == '__main__'):     
    logging.debug('\nApp Started')
    app.run(host=host, port=port)
    
    