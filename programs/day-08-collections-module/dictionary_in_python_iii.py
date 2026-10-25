# Handle N queries on a dictionary of student marks:
# i name marks -> insert, d name -> delete (True/False), p name -> print marks.
# Returns True if the key was found for delete/print, else False.

def _parts(x):
    return x.split() if isinstance(x, str) else list(x)


def insert_dict(query, dict):
    q = _parts(query)
    if len(q) >= 3:
        dict[q[1]] = int(q[2])
    else:
        dict[q[0]] = int(q[1])


def del_dict(query, dict):
    q = _parts(query)
    k = q[1] if len(q) > 1 else q[0]
    if k in dict:
        del dict[k]
        return True
    return False


def print_dict(key, dict):
    q = _parts(key)
    k = q[-1]
    if k in dict:
        print("Marks of " + k + " is " + str(dict[k]))
        return True
    return False
