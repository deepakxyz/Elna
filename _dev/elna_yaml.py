import yaml

with open('elna.yaml', 'r') as r:
    data = yaml.load(r)
    new_data = data
    new_data['name'] = "/mnt/x/y"
    print(data)


with open('elna.yaml', 'w') as w:
    yaml.dump(data, w)
