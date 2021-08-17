# 1360. Number of Days Between Two Dates https://leetcode.com/problems/number-of-days-between-two-dates/
# https://leetcode.com/submissions/detail/539643280/
from datetime import datetime


def daysBetweenDates(date1: str, date2: str) -> int:
    dateFormat = "%Y-%m-%d"
    difference = datetime.strptime(date1, dateFormat) - datetime.strptime(
        date2, dateFormat
    )
    return abs(difference.days)


print(daysBetweenDates("2019-06-29", "2019-06-30"))
