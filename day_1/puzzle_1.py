from pathlib import Path
import os, sys

abs_file_path = os.path.abspath(__file__)
one_dir_up = Path(abs_file_path).parents[1]
utils_abs_path = os.path.join(one_dir_up, 'utils')
sys.path.insert(0, utils_abs_path)

from get_inputs import get_str_inputs, get_num_inputs

file = 'puzzle_inputs.txt'
inputs = get_str_inputs(file)
i = 0
curr_cal_count = 0
max_cal_count = 0
while i < len(inputs):
    if inputs[i] != '':
        curr_cal_count += int(inputs[i])
    else:
        if curr_cal_count > max_cal_count:
            max_cal_count = curr_cal_count
        curr_cal_count = 0
    i += 1
print(max_cal_count)