import requests

def get_GSM_coordinates(device, gsm_data):
    url = "https://us1.unwiredlabs.com/v2/process.php"
    data = gsm_data[3:-1].split(',')
    payload = "{\"token\": \"0f918368392db2\",\"radio\": \"gsm\",\"mcc\": 250,\"mnc\": 01,\"cells\": [{\"lac\": 221,\"cid\": 14432}, {\"lac\": 19726,\"cid\": 5352}, {\"lac\": 4741,\"cid\": 11322}, {\"lac\": 4741,\"cid\": 11321}]}"
    response = requests.request("POST", url, data=payload)

    print(response.text)

    device.GSM_latitude
    device.GSM_longitude