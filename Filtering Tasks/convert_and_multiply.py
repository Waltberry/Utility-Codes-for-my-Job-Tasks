def convert_and_multiply(value):
    if not isinstance(value, str):
        return 0
    if value.endswith('G'):
        num_value=float(value[:-2])*1000
    if value.endswith('M'):
        num_value=float(value[:-2])*1
    if value.endswith('T'):
        num_value=float(value[:-2])*1000000
    else:
        return value
    return int(num_value)        