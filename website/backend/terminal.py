import subprocess
from typing import Dict, List

def _parse_flags(flags : Dict) -> List:
    pass

def execute_command(command : str, flags : Dict) -> str:
    parsed_flags = _parse_flags(flags)
    parsed_flags.insert(0, command)
    return subprocess.run(command)