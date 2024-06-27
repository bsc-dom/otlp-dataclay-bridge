from collections import deque
from threading import Event

import pandas as pd

from dataclay import DataClayObject, activemethod


class TimeSeriesData(DataClayObject):
    columns: list[str]
    dataframes: deque[pd.DataFrame]
    waiters: list[Event]

    def __init__(self):
        self.dataframes = deque(maxlen=5)
        self.waiters = list()

    @activemethod
    def add_dataframe(self, df: pd.DataFrame):
        """Add a DataFrame to the circular buffer."""
        self.dataframes.append(df)
        for waiter in self.waiters:
            waiter.set()
    
    @activemethod
    def get_last_dataframe(self):
        """Get the last DataFrame in the circular buffer."""
        if self.dataframes:
            return self.dataframes[-1]
        else:
            return None

    @activemethod
    def wait_for_dataframe(self):
        """Wait for new data to be added to the buffer."""
        waiter = Event()
        self.waiters.append(waiter)
        waiter.wait()
        self.waiters.remove(waiter)
        return self.get_last_dataframe()

    @activemethod
    def get_all_dataframes(self):
        """Get all the DataFrames in the buffer."""
        return list(self.dataframes)
