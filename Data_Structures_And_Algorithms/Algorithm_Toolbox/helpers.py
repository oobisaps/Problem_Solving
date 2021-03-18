
import time 
import numpy as np

from random import randint, randrange
from operator import attrgetter


def stress_test(input_type,slice_object,*functions):
    n_iteration = 0
    log_time_data = {}
    result_attributes = attrgetter()

    while(True):
        if input_type == 'list':
            genetated_input = randrange(slice_object.start, slice_object.end)
        else:
            genetated_input = randint(slice_object.start, slice_object.end)
        
        functions_result = [function(log_time = log_time_data, input = genetated_input) for function in functions]

        print('Iteration_1 : ')
        print()
        for log_time in log_time_data:
            print('Function {} : Execution Time {} : Result {}'.format(log_time, 
                                                                       log_time_data[log_time]['execution_time'], 
                                                                       log_time_data['result']))
            print()
        
        if len(set(tuple(item['result']) for item in log_time_data.values())) > 1:
            print('SOMETHING IS GOING WRONG')
            break

        else:
            continue

        n_iteration += 1

        if n_iteration > 500:
            break
        


        
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = {
                'execution_time' : te - ts,
                'result' : result
            }
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        # return result
    return timed


a = [{'name' : 'alem', 'age' : 2},{'name' : 'almas', 'age' : 2}]

a_1 = [attrgetter('name') for i in a]
a_1 = set(map(attrgetter('name'), a))