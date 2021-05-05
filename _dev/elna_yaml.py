import yaml

with open('elna.yaml', 'r') as r:
    data = yaml.load(r)
    new_data = data.append('hello: new')
    print(new_data)
