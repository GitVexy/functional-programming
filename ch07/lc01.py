from functools import reduce
from typing import Callable


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"
    
    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")
    
    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


# don't touch above this line


def create_html_table(data_rows: list) -> Callable[[list], str]:
    rows = accumulate_rows(map(accumulate_data_cells, data_rows))
    
    def create_table_headers(headers: list):
        nonlocal rows                                           # 1.   Access the nonlocal rows string
        headers_string = tag_row(accumulate_headers(headers))   # 2.   Accumulate headers in single row 
        rows = headers_string + rows                            # 3.   Add row of headers to beginning of rows
        return tag_table(rows)                                  # 4/5. Add final tag table, and return complete string
    
    return create_table_headers
