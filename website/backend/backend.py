from typing import Dict
from website.backend import terminal
from website.backend.scanner import Scanner
import re

import logging

from config import SaneCommand
scanimg = SaneCommand('scanimage') 

def get_scanner_list() -> Dict:
    scanners = dict()
    messages = terminal.execute_command(scanimg.main_command, scanimg.device_list_args()).split('/n')
    logging.debug('Got messages' + ' '.join(messages))
    for message in messages:
        device_name = ''.join(re.findall(r'\/(\w+)\?', message))
        device_id = ''.join(re.findall(r'\`(.*)\'', message))
        scanners[device_name] = Scanner(device_name, device_id)
    return scanners

