#тестирую выборку моделей сканеров из вывода sane-find-scanner
import re

def get_scanner_list():
    a = (0, '\n  # sane-find-scanner will now attempt to detect your scanner. If the\n  # result is different from what you expected, first make sure your\n  # scanner is powered up and properly connected to your computer.\n\n  # No SCSI scanners found. If you expected something different, make sure that\n  # you have loaded a kernel SCSI driver for your SCSI adapter.\n  # Also you need support for SCSI Generic (sg) in your operating system.\n  # If using Linux, try "modprobe sg".\n\nfound USB scanner (vendor=0x03f0 [Hewlett-Packard], product=0x042a [HP LaserJet Professional M1132 MFP]) at libusb:001:005\ncould not open USB device 0x0424/0xec00 at 001:003: Access denied (insufficient permissions)\ncould not open USB device 0x0424/0x9514 at 001:002: Access denied (insufficient permissions)\ncould not open USB device 0x1d6b/0x0002 at 001:001: Access denied (insufficient permissions)\n  # Your USB scanner was (probably) detected. It may or may not be supported by\n  # SANE. Try scanimage -L and read the backend\'s manpage.\n\n  # Not checking for parallel port scanners.\n\n  # Most Scanners connected to the parallel port or other proprietary ports\n  # can\'t be detected by this program.\n\n  # You may want to run this program as root to find all devices. Once you\n  # found the scanner devices, be sure to adjust access permissions as\n  # necessary.')
    b = a[1].rstrip()
    c = b.split('\n')
    d = filter(lambda x: x.count('#') == 0 and len(x) != 0, c)
    success_scanners = filter(lambda x: x.split()[0] == 'found', list(d))
    print(list(success_scanners)[0])

