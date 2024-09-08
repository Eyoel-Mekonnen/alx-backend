#!/usr/bin/env python3
"""Index page Returned."""
from typing import List, Tuple
import csv, math

def index_range(page: int, page_size: int) -> Tuple:
    """Return tuple."""
    startindex = (page - 1) * page_size
    endindex = startindex + page_size
    indexrange = (startindex, endindex)
    return indexrange


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        """Gets start and end page and asserts."""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        pageitem = data[start:end]
        return pageitem
