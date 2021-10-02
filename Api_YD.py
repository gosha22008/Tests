import requests
import json


def read_file_json(loc_f_name):
    with open(loc_f_name, encoding='utf-8') as f:
        data = json.load(f)
        return data


def get_token():
    tokens = read_file_json('tokens.json')
    return tokens


class YD:
    def get_headers_yandex(self):
        return {'Content-Type': 'application/json',
                'Authorization': get_token()['ya_token']
                }

    def create_direct(self):
        url_create_dir = 'https://cloud-api.yandex.net/v1/disk/resources?path=py_diplom_basic'
        headers = self.get_headers_yandex()
        res = requests.put(url_create_dir, headers=headers)
        if res.status_code == 201:
            print("Папка 'py_diplom_basic' успешно создана")
            return res.status_code
        elif res.status_code == 409:
            print(res.json()['message'])
            return res.status_code


if __name__ == "__main__":
    kek = YD()
    kek.create_direct()
