from typing import List
import os

from dotenv import load_dotenv
load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
shell_arg = os.getenv("SHELL")


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
    
    def scan_image(self, device_id, filename, dpi, file_format):
        flags = {
            '--device-name=' : device_id,
            '--output-file=': f'imgs/{filename}',
            '--format=' : file_format
        }
        return flags

    @staticmethod
    def device_list_args() -> List[str]:
        return ['-L']

file_extensions = ['jpeg', 'png', 'tiff']

