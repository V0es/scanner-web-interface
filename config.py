from typing import List, Dict
import os

from dotenv import load_dotenv
load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
shell_arg = os.getenv("SHELL_ARG")
img_folder = os.getenv("IMG_FOLDER")


if shell_arg == 'True':
    shell_arg = True
elif shell_arg == 'False':
    shell_arg = False
else:
    raise Exception('Shell argument is invalid')

class FlaskConfiguration(object):
    DEBUG = False
     
class SaneCommand():

    def __init__(self, main_command : str) -> None:
        self.main_command = main_command
    
    def scan_image_args(self, device_id : str, filename : str, 
                    dpi : str, file_format : str) -> Dict[str, str]:
        flags = {
            '--device=' : device_id,
            '--file=': f'{img_folder}/{filename}.{file_format}',
            '--resolution=' : dpi,
            '--mode=': 'gray',
            '--logging=' : 'debug'
        }
        return flags

    @staticmethod
    def device_list_args() -> List[str]:
        return ['-L']

file_extensions = ['jpg', 'png', 'tiff']
dpis = ['100', '150', '200', '300', '600', '1200']

