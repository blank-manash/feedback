# logger_setup.py
import logging
from colorama import Fore, Style, init

# Initialize colorama for colored output on Windows
init(autoreset=True)


# Custom formatter for colored logs
class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA,
    }

    def format(self, record):
        log_msg = super().format(record)
        log_color = self.COLORS.get(record.levelno, Fore.WHITE)
        log_msg = f"{log_color}[{record.levelname}] {record.filename}: {log_msg}{Style.RESET_ALL}"
        return log_msg


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    log_format = "%(levelname)s: %(filename)s - %(message)s"
    console_handler.setFormatter(ColoredFormatter(log_format))
    logger.addHandler(console_handler)
    return logger
