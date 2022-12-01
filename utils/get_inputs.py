def get_str_inputs(f):
    file = open(f, 'r')
    inputs = file.read().split('\n')
    file.close()
    return inputs

def get_num_inputs(f):
    file = open(f, 'r')
    str_inputs = file.read().split('\n')
    file.close()
    inputs = [int(x) for x in str_inputs]
    return inputs