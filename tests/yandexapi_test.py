import requests


def test_newfolder():
    with open("ya_token.txt", "r") as file:
        token = file.read()
    response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources',
                 headers={'Content-Type': 'application/json', 'Authorization': token},
                 params={'path': "xxxxxxxx"})
    assert response.status_code == 201


def test_folders():
    with open("ya_token.txt", "r") as file:
        token = file.read()
    response = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/',
                            headers={'Content-Type': 'application/json', 'Authorization': token},
                            params={'path': "xxxxxxxx"})
    assert response.status_code == 200


def test_deletefolder():
    with open("ya_token.txt", "r") as file:
        token = file.read()
    response = requests.delete('https://cloud-api.yandex.net:443/v1/disk/resources/',
                            headers={'Content-Type': 'application/json', 'Authorization': token},
                            params={'path': "xxxxxxxx"})
    assert response.status_code == 204
