import xml.etree.ElementTree as etree
import json

class PhoneConnector:

    def __init__(self, filepath):
        print('This is the phone object')

    @property
    def parsed_data(self):
        print('I have nothing to do with database')
        print('And I do not think I belong here')

class JsonConnector:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode = 'r', encoding = 'utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XmlConnector:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JsonConnector
    elif filepath.endswith('xml'):
        connector = XmlConnector
    elif filepath is 'phone':
        connector = PhoneConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    sqlite_factory = connect_to('data/person.sq3')
    print()

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    #print('found: {} persons'.format(len(xml_data)))

    for liar in liars:
        print('first name:{}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({}):'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]

    print()
    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t
        in donut['topping']]

    print()
    phone_factory = connect_to('phone')
    phone_factory.parsed_data    
    
if __name__ == '__main__':
    main()





