# DATA STRUCTURES -> Sequential Lists - linear search


def search(lst, elem):
    """ Description:
            Return the index of the element if it's in the list, or None if it isn't.
        Parameters:
            lst = the list containing (or not) the values.
            elem = the element you want to find it index.
        Usage:
            search(list, element) """
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return None

