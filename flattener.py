from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    '''
    returns a flattened iterable with each element in a nested sequence
    '''
    
    # iterate over each top-level item
    for item in items:

        # if item is an iterable and not a string/byte sequence, recursively go deeper
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item, ignore_types)

        # otherwise, we are at the bottom and you can return the element
        else:
            yield item
