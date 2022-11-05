from typing import List
import os

class FlaskConfiguration(object):
    DEBUG = True
     
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

host = os.getenv('HOST')
port = os.getenv('PORT')