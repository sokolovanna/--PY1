from pprint import pprint
dict_ = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]
pprint(dict_)
