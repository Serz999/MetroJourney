import requests

def prepare_frame(url: str)->tuple:
    response = requests.get(url)
    frame = response.json()
    return (frame)    


def build_metro()->tuple:
    frame = prepare_frame('https://api.hh.ru/metro/1') 
    metro = {} 
    for branch in frame['lines']:
        prev_name = None 
        prev = None
        for station in branch['stations']:
            if station['name'] not in metro.keys():
                metro[station['name']] = {}
            curr = metro[station['name']]
            if prev is not None:
                prev[station['name']] = branch['hex_color']
                curr[prev_name] = branch['hex_color']
            prev_name = station['name']
            prev = curr 
        circulars = ['915133', 'CC4C6E', '88CDCF']
        if branch['hex_color'] in circulars:
            first = branch['stations'][0]['name']
            last = branch['stations'][-1]['name']
            metro[first].update({last: branch['hex_color']})
            metro[last].update({first: branch['hex_color']})
    return (metro)
