import requests
from datetime import datetime
from os import getcwd, chdir
from pathlib import Path
from pytz import timezone
from typing import Optional, Tuple


def get_current_day(year: Optional[int] = None) -> Tuple[int, int]:
    tz = timezone("US/Eastern")
    current_time = datetime.now(tz=tz)
    if year is None:
        year = current_time.year
    aoc_start_time = datetime(year,12,1,tzinfo=tz)
    day = (current_time - aoc_start_time).days + 1
    return day, year


def initialise_day(day: Optional[int] = None) -> Path:
    """Creates day folder and set workdir to day folder."""
    if day is None:
        day, _ = get_current_day()
    try:
        workdir = Path(__file__).parent / str(day)
    except:
        workdir = Path(getcwd()) / f"src/{day}"

    workdir.mkdir(parents=True, exist_ok=True)
    # Change working directory
    chdir(workdir)
    return workdir


def get_lines(filename: str):
    workdir = initialise_day()
    file = open(workdir / filename)

    while line:= file.readline().replace("\n", ""):
        yield line

    file.close()
