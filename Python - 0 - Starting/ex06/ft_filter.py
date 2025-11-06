import sys
import string


def ft_filter(func, iretable):
    if func is None:
        return [item for item in iretable if item]
    else:
        return [item for item in iretable if func(item)]