from uvicmuse.MuseWrapper import MuseWrapper as MW
import asyncio

loop = asyncio.get_event_loop()
M_wrapper = MW(loop=loop, target_name=None, timeout=10, max_buff_len=500)

try:
    M_wrapper.search_and_connect()  # returns True if the connection is successful
except TypeError as e:
    print(f"An error occurred: {e}")
else:
    EEG_data = M_wrapper.pull_eeg()
    EEG_data = M_wrapper.pull_eeg()
    print(str(EEG_data))
    M_wrapper.disconnect()