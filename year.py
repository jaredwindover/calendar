#!/usr/bin/env python3
import arrow
import re

from pyfiglet import figlet_format
from layout.cell import Cell
from layout.row import Row
from layout.column import Column

def figlet_Cell(text, font):
    whitespace_regex = '\s*$'
    return Column([
        Cell(line) for line in
        figlet_format(str(text), font=font).split('\n')
        if not re.match(whitespace_regex, line)
    ])

class Month(Column):
    def __init__(self, start, *args, font=None, **kwargs):
        end = start.replace(months=+1)
        days = arrow.Arrow.range('day', start, end)[:-1]
        pad = (days[0].weekday() + 1) % 7
        Cells = [Cell(" ")] * pad
        Cells += [Cell(d.format('DD')) for d in days]
        super().__init__([
            Row([
                Cell(start.format("MMMM")) if font is None else
                figlet_Cell(start.format("MMMM"), font)
            ]),
            Row(
                Cells,
                alignment="left",
                padding=1
            ).wrap(
                7,
                columnize=True
            )
        ], *args, **kwargs)

class Year(Column):
    def __init__(self, year, *args, font=None, monthFont=None, **kwargs):
        start = arrow.get(year, 1, 1)
        months = arrow.Arrow.range('month', start, limit=12)
        blocks = [Month(m, alignment="center", font=monthFont) for m in months]
        super().__init__([
            Row([
                Cell(start.year) if font is None else
                figlet_Cell(start.year, font)
            ]),
            Row(
                blocks,
                alignment="top",
                padding=2
            ).wrap(
                3,
                columnProps={"padding": 1}
            )
        ], *args, **kwargs)

def main():
    year = Year(
        arrow.now().year,
        alignment="center",
        padding=1,
        font='roman',
        monthFont='short'
    )
    print(year)

if __name__ == '__main__':
    main()
