import requests


GAI_URL = "http://mvd.gov.by/ajax.asmx/getext"
# REGISTRATION_DATA = {
#     "GuidControl": 2091,
#     "Param1": "Хрипунов Роман Борисович",
#     "Param2": "МАА",
#     "Param3": 1945282
# }

REGISTRATION_DATA = {
    "GuidControl": 2091,
    "Param1": "семенов петр васильевич",
    "Param2": "маа",
    "Param3": 123456
}


def get_fines(url=GAI_URL, reg_data=REGISTRATION_DATA):
    """returns fines from http://mvd.gov.by/ajax.asmx/getext by vehicle registration data"""
    response = requests.post(url, json=reg_data)
    return response.json().replace('<h2>', '').replace('</h2>', '')


if __name__ == '__main__':
    print(get_fines())
