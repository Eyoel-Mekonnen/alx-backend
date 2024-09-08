#!/usr/bin/env python3
"""Index page Returned."""
from typing import List, Tuple
import csv
import math


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List:
        """Gets start and end page and asserts."""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        pageitem = data[start:end]
        return pageitem

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List:
        """ Return data information."""
        pagedata = self.get_page(page, page_size)
        data = self.dataset()
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(data) / page_size)
        if end + 1 < len(self.__dataset):
            next_page = end + 1
        else:
            next_page = None
        if start - 1 > 0:
            prev_page = start - 1
        else:
            prev_page = None
        dict_ = {
                    'page_size': page_size,
                    'page': page,
                    'data': pagedata,
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': total_pages
                }
        return dict_
