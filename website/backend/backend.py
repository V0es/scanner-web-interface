from typing import List
from website.backend.scanner import Scanner
import re


def get_scanner_list() -> List[Scanner]:
    scanners = list()
    a = '''device `hpaio:/usb/HP_LaserJet_Professional_M1132_MFP?serial=000000000QH82HSHPR1a' is a Hewlett-Packard HP_LaserJet_Professional_M1132_MFP all-in-one'''
    #messages = terminal.execute_command('scanimage', '-L').split('/n')
    messages = a.split('/n')
    for message in messages:
        device_name = ''.join(re.findall(r'\/(\w+)\?', message))
        device_id = ''.join(re.findall(r'\`(.*)\'', message))
        scanners.append(Scanner(device_name, device_id))
    return scanners    


