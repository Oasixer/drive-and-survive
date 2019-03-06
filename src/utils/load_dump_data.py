import os
import pickle


def load_ship_file():  # temp filename, should be parameter?
    direc = os.path.join(os.path.dirname(__file__), '..', 'data', 'player_data')
    with open(direc + '/ship_1', 'rb') as f:
        ship_data = pickle.load(f)
    return ship_data


def generate_ship_file(shipObject):
    directory = os.path.join(os.path.dirname(__file__), '..', 'data', 'player_data')
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + '/ship_1', 'wb') as f:
        pickle.dump(shipObject, f)


'''
def save_without_attribute(obj, attr):
    shipDict = obj.__dict__
    shipDict[attr] = None
    return (obj.__class__, shipDict)


def back_to_object(cls, attributes):
    obj = cls.__new__(cls)
    obj.__dict__.update(attributes)
    return obj
    '''