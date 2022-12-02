def get_str_inputs(f):
    file = open(f, 'r')
    inputs = file.read().strip().split('\n')
    inputs = [x.strip() for x in inputs]
    file.close()
    return inputs

def get_num_inputs(f):
    file = open(f, 'r')
    inputs = file.read().strip().split('\n')
    inputs = [int(x.stripe()) for x in inputs]
    file.close()
    return inputs