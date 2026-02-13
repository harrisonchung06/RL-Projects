def clamp(x, minimum, maximum):
    if x < minimum:
        return minimum
    if x > maximum:
        return maximum
    return x

def min_cap(x, min):
    if x < min:
        return min
    return x

def max_cap(x, max):
    if x > max:
        return max
    return x