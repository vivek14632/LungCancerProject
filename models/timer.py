import timeit
from datetime import datetime

start = 0
stop = 0

def get_start_time():
	# Get the start time
	start = timeit.default_timer()
	start_time = datetime.now()
	print('Execution started at {}'.format(start_time))
	
def get_stop_time():
	# Get the stop time
	stop = timeit.default_timer()
	stop_time = datetime.now()
	print('Execution ended at {}'.format(stop_time))
	print('Total Execution time : {}'.format(stop - start))
