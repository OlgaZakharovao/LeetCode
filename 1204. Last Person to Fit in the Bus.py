'''
There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may
be some people who cannot board.

Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit.
The test cases are generated such that the first person does not exceed the weight limit.
'''


import pandas as pd


def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    summa = 0
    i = 0
    queue.sort_values('turn', inplace=True)
    weight = queue['weight']
    if weight.sum() <= 1000:
        return pd.DataFrame({'person_name':[queue.iloc[-1]['person_name']]})
    while summa <= 1000:
        summa += weight.iloc[i]
        i += 1
    return pd.DataFrame({'person_name':[queue.iloc[i-2]['person_name']]})

