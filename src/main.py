# Example command for benchmarking all tasks:
# python3 <path/to/this/script> <library> <dataset> <repeations> [task] > output/file.txt
# python3 src/main.py networkx data/small.txt 10 > output/networkx-small.txt
# - for library: Networkx
# - Input dataset csv file: data/small.txt
# - Repeat every run number of times: 10
# - task: [Optional], default = All
# - Print the results to output file: output/networkx-small.txt
#
# Example command for benchmarking specific task CONNECTED_COMPONENT:
# python3 src/main.py networkx data/small.txt 10 CONNECTED_COMPONENT > output/networkx-cc-small.txt
#
# Task can be one of enum values from src/profiling/task.py


import sys
from profiling.task import Task

profiler = sys.argv[1]  # name of library to profile
filename = sys.argv[2]  # INPUT file
n = int(sys.argv[3])    # number of repeatition to call in order to build statistics of benchmark

if len(sys.argv) > 4:
    task = Task[sys.argv[4].upper()]

if (profiler == 'networkx'):
    from profiling.networkx_profile import NetworkxProfile
    runner = NetworkxProfile()
elif (profiler == 'grape'):
    from profiling.grape_profile import GrapeProfile
    runner = GrapeProfile()


runner.profile(filename, n, task)
