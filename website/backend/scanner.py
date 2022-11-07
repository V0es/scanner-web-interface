from config import SaneCommand
from website.backend.terminal import execute_command
from typing import List, Dict
import logging


class Scanner():
    def __init__(self, device_name : str, device_id : str):
        self.device_name = device_name
        self.device_id = device_id
        

    def scan(self, filename : str, format : str, dpi : str):
        scan_cmd = SaneCommand('scanimage')
        scan_args = scan_cmd.scan_image_args(self.device_id, filename, dpi, format)
        arg_list = self._make_args_list(scan_args)

        msg = execute_command(scan_cmd.main_command, arg_list)
        logging.debug(f'Message from scanning: {msg}')

    def _make_args_list(self, args : Dict[str, str]) -> List[str]:
        arg_list = list()
        for key, value in args.items():
            arg_list.append(key + value)
        return arg_list

