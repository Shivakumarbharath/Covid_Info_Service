from datetime import datetime

from cowin.constants import Constants


def today() -> str:
    return datetime.now().strftime(Constants.DD_MM_YYYY)
