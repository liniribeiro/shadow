import itertools
from collections import Counter
from functools import reduce
from math import gcd
from typing import List


def cellCompete(states, days):
    # 1 - active cell
    # 0 - inactive cell
    current_states = []
    passed_days = 0
    while passed_days < days:
        passed_days += 1
        for i in range(len(states)):
            before_neighbor_state = states[i - 1] if i > 0 else 0
            after_neighbor_state = states[i + 1] if i < len(states) - 1 else 0

            current = 0 if before_neighbor_state == after_neighbor_state else 1
            current_states.append(current)
        states = current_states
    return current_states


def generalizedGCD(num, arr):
    x = reduce(gcd, arr)
    return x


def topNCompetitors(numCompetitors, topNCompetitors, competitors,
                    numReviews, reviews):
    all_strings = itertools.chain.from_iterable([rev.split() for rev in reviews])
    all_occorrences = Counter(list(all_strings))

    response = {}
    for comp in competitors:
        if all_occorrences.get(comp):
            response.update({all_occorrences.get(comp): comp})

    return [response[k] for k in sorted(response.keys(), reverse=True)[:topNCompetitors]]


def get_new_grid(rows, columns, grid, hours):
    hours += 1
    update_rows = []
    for i in range(rows):
        for x in range(columns):
            column = grid[i][x]
            if column == 1:
                update_rows.append({'row': i - 1, 'column': x})
                update_rows.append({'row': i + 1, 'column': x})
                update_rows.append({'row': i, 'column': x + 1})
                update_rows.append({'row': i, 'column': x - 1})

    updated_grid = update_row(update_rows, grid, columns, rows)
    more_hours = verify_if_need_more_hours(updated_grid)
    if more_hours:
        hours = get_new_grid(rows, columns, grid, hours)
    return hours


def minimumHours(rows, columns, grid):
    hours = 0
    hours = get_new_grid(rows, columns, grid, hours)
    return hours


def verify_if_need_more_hours(updated_grid: List):
    for row in updated_grid:
        for column in row:
            if column == 0:
                return True
    return False


def update_row(update_rows, updated_grid, columns_number, rows_number):
    for x in update_rows:
        row = x['row']
        column = x['column']
        if row >= 0  and row <= rows_number -1 \
                and column >= 0 and column <= columns_number -1:

            updated_grid[row][column] = 1
    return updated_grid



if __name__ == "__main__":
    # s = [1, 0, 0, 0, 0, 1, 0, 0]
    # days = 1
    #
    # pr = cellCompete(s, days)
    #
    # s = [2, 4, 6, 8, 10]
    # num = 5
    #
    # pr = generalizedGCD(num, s)
    # numCompetitors = 6
    #     # nCompetitors = 2
    #     # competitors = ['newshop', 'shopnow', 'mymarket', 'afshion', 'fashionbeats', 'tcellular']
    #     # numReviews = 6
    #     # reviews = ['abc newshop', 'use newshop', 'best newshop', 'fashionbeats is cool', 'mymarket awsome', 'newshop delivery']
    #     #
    #     # pr = topNCompetitors(numCompetitors, nCompetitors, competitors, numReviews, reviews)

    rows = 4
    columns = 5
    grid = [
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
    ]
    pr = minimumHours(rows, columns, grid)
    print(f">>>>>{pr}")


