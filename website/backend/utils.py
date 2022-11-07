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
    logging.debug('Got message: ' + ' '.join(messages))
    for message in messages:
        device_name = ''.join(re.findall(r'\/(\w+)\?', message))
        device_id = ''.join(re.findall(r'\`(.*)\'', message))
        scanners[device_name] = Scanner(device_name, device_id)
        if len(scanners) == 0:
            logging.debug('No scanners found')
        else:
            logging.debug(f'Found scanners {scanners.items()}')
    return scanners


def start_scanning(form, scanner_list : Dict[str, Scanner]):
    device_name = form.get('scan_select')
    filename = form.get('filename')
    dpi = form.get('dpi_select', '150')
    format = form.get('format_select')
    scanner_list[device_name].scan(filename, format, dpi)
    

