#!/usr/bin/env python3
""" Helper function."""


def index_range(page: int, page_size: int) -> tuple:
    """Return tuple."""
    startindex = (page - 1) * page_size
    endindex = startindex + page_size
    indexrange = (startindex, endindex)
    return indexrange
