import re

from math import prod
from src.utils import initialise_day
from typing import Dict, List, Optional, Tuple
from utils import get_lines


class Symbol:
    def __init__(self, symbol:str):
        self.symbol = symbol
        self.adjacent_numbers = []

    @property
    def is_gear(self):
        return (self.symbol == "*") and (len(self.adjacent_numbers) == 2)
    
    @property
    def gear_ratio(self):
        if self.is_gear:
            return prod(self.adjacent_numbers)
        return 0


class Number:
    def __init__(self, value: int, start: Tuple[int,int], end: Tuple[int,int]):
        self.value = value
        self.start = start
        self.end = end
        self._next_to_symbols = False

    def _within_start_ends(self, row: int, col: int):
        return (
            (row == self.start[0]) 
            and (col in range(self.start[1], self.end[1]+1))
        )
    
    def get_perimeter(self):
        """Assumption: numbers won't span across multiple lines."""
        for row in range(self.start[0]-1, self.start[0]+2):
            for col in range(self.start[1]-1, self.end[1]+2):
                if self._within_start_ends(row,col):
                    continue
                yield (row, col)
    
    def is_next_to_symbols(self, symbols: Dict[Tuple[int,int], Symbol]) -> bool:
        if self._next_to_symbols:
            return self._next_to_symbols
        for coord in self.get_perimeter():
            adjacent_symbol = symbols.get(coord)
            if adjacent_symbol is not None:
                adjacent_symbol.adjacent_numbers.append(self.value)
                return True
        return False
    
    def __repr__(self) -> str:
        return f"{self.value} [{self.start},{self.end}]"


def get_sum_part_numbers(numbers: List[Number], symbols: Dict[Tuple[int,int], Symbol]) -> int:
    sum_part_numbers = 0
    for num in numbers:
        if num.is_next_to_symbols(symbols):
            sum_part_numbers += num.value
    return sum_part_numbers


def get_sum_gear_ratios(symbols: Dict[Tuple[int,int], Symbol]) -> int:
    sum_gear_ratios = 0
    for symbol in symbols.values():
        sum_gear_ratios += symbol.gear_ratio
    return sum_gear_ratios


def process_data(filename: str):
    numbers = []
    symbols = {}

    row = -1
    while line:= get_lines(filename):
        row += 1
        # Find numbers
        for match in re.finditer("([0-9])+", line):
            start = (row, match.start())
            end = (row, match.end()-1)
            value = int(match.group(0))
            numbers.append(Number(value, start, end))

        # Find symbols
        for match in re.finditer("[^0-9\.\s]{1}", line):
            symbol = match.group(0)
            if symbol is not None:
                coordinate = (row, match.start())
                symbols[coordinate] = Symbol(symbol)

    return numbers, symbols


if __name__ == "__main__":
    filename = "input.txt"
    numbers, symbols = process_data(filename)

    sum_part_numbers = get_sum_part_numbers(numbers)
    print(f"[Part 1] Sum of all part numbers is {sum_part_numbers}.")

    sum_gear_ratios = get_sum_gear_ratios(symbols)
    print(f"[Part 2] Sum of all gear ratio is {sum_gear_ratios}.")
