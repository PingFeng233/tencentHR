import math


# 分页函数
def custom_paginator(current_page, total_page, max_page):
    middle = math.ceil(max_page / 2)

    # 总页数<最大页数
    if total_page < max_page:
        start = 1
        end = total_page
    # 总页数>最大页数
    else:
        # 当前页在头部
        if current_page <= middle:
            start = 1
            end = max_page
        # 当前页在中间
        elif current_page > middle and current_page < (total_page - middle):
            start = current_page - middle
            end = current_page + middle - 1
            # 当前页在尾部
        else:
            start = total_page - max_page + 1
            end = total_page

    return start, end
