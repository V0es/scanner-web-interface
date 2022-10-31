import subprocess
from typing import Dict, List

def _parse_flags(flags : List) -> List:
    pass

def execute_command(command : str, flags : List) -> str:
    flags.insert(0, command)
    return subprocess.getoutput(command)
