#!/usr/bin/env python3
from math import floor
from time import localtime

from layout.utilities import consoleWidth
from layout.cell import Cell
from layout.row import Row
from layout.column import Column

warningColor = '\033[93m'
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

months = [month[:3] for month in months]

class Year(Column):
    def __init__(self, year, abbrev, monthColor, *args, **kwargs):
        Cells = [Cell(month, color=monthColor(month)) for month in months]
        super().__init__([
            Row([
                Cell(year)
            ], alignment="center"),
            Row(
                Cells,
                alignment="center",
                padding=1
            ).wrap(
                3,
                columnize=True,
                columnProps={"alignment": "center"}
            )
        ], *args, **kwargs)

def main():
    fullWidth = consoleWidth()
    padding = 3
    start = 1992
    age = 74
    currentYear = localtime().tm_year
    currentMonth = localtime().tm_mon
    table = Row(
        [
            Year(
                year,
                abbrev=True,
                alignment="center",
                color=None if year >= currentYear else warningColor,
                monthColor=(lambda m: warningColor
                            if m in months[0:currentMonth]
                            else None)
                if year == currentYear
                else lambda x: None
            )
            for year in range(start, start + age)
        ],
        padding=3
    )
    yearWidth = table.blocks[0].width()
    columnCount = max(
        1,
        floor((fullWidth - yearWidth) / (yearWidth + padding)) + 1
    )

    print(table.wrap(columnCount, columnize=True))


if __name__ == '__main__':
    main()
