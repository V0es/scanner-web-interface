from typing import List
from website.backend import scanning
from website.backend import terminal
from config import sane_commands


def get_scanner_list() -> List[str]:
    message = terminal.get_output_message(sane_commands['find_scanner'])
    scanners = scanning.parse_device_message(message)
    return scanners    