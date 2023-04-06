from parser import build_metro
import json
import os.path
import codecs

if __name__ == '__main__':
    if not os.path.exists('moscow_metro.json'):
        with codecs.open('moscow_metro.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(build_metro(), indent=4, ensure_ascii=False))
