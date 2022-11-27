import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, "r") as f:
        table = []
        for line in f:
            symbols = line.rstrip("\n").split(',')
            table.append(symbols)
        headers = table[0]
        table = table[1:]

        dict_ = []
        for values in table:
            values = dict_.append(dict(zip(headers, values)))
        return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
