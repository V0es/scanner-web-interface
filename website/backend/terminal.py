from config import shell_arg

import subprocess
from typing import List


import logging

def execute_command(command : str, flags : List) -> str:
    flags.insert(0, command)
    logging.debug('Executed command: ' + ' '.join(flags))
    try:
        stdout = subprocess.run(flags, stdout=subprocess.PIPE, check=True, text=True, shell=shell_arg).stdout
    except subprocess.CalledProcessError() as e:
        logging.debug('Got process error: ' + str(e))
        
    return stdout
