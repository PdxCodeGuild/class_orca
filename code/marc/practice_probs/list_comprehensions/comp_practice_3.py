# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.

def dict_swap (ol_dict):
    rev_dict = dict(zip(ol_dict.values(),ol_dict.keys()))
    return rev_dict
mon_key = {"lil":"Sambo",
"Big":"Ape",
"Funny":"chimp"}
print(dict_swap(mon_key))