import json
from userProfile.models import Device, Message_from_FM, userProfile
from datetime import datetime, timedelta
from ._validation import CRC

def get_device_data(data):
    data_list = data.split(';')
    imei_device = get_imei(data_list)
    try:
        device = Device.objects.get(imei=imei_device)
    except:
        if get_type_con(data_list) == 'B':
            profile = userProfile.objects.get(username='NoNameDevice')
            device = Device(user=profile, imei=get_imei(data_list))
            device.save()
        else: 
            return None
    period = device.launch_period
    device_data = {'device': device, 'period': period}
    return device_data


def save_message(message, device_data, logger):
    message_list = message.split(';')
    device = device_data['device']
    return save_message_model(message_list, device, logger)  


def get_answer(message, device_data, logger):
    time_now = datetime.now().strftime('%Y%m%d%H%M')[2:]
    try:
        device = device_data['device']
        period = device_data['period']
    except:
        logger.warn('Can not get launch period')
        return None

    if period < 5:
        time = datetime.now() + timedelta(minutes=5)
        time_wake = time.strftime('%Y%m%d%H%M')[2:]
    else:
        time = datetime.now() + timedelta(minutes=period)
        time_wake = time.strftime('%Y%m%d%H%M')[2:]
    
    data = generate_answer_data(message, device)

    message = '$' + time_now + '0' + ',' + time_wake + '0' +  data 
    messageToSend = message.encode('utf-8') + b'*' + CRC(message) + b'\r\n'
    return messageToSend


def generate_answer_data(message, device):
    data = ''
    message_list = message.split(';')
    if get_type_con(message_list) == 'B':
        data += ',M1,Z110'
    else:
        if device.enable_SearchMode:
            data += ',M2,Z100'
        else:
            data += ',M2,Z010'
    data += (',P' + str(device.time_GPS_search))
    data += (',N' + str(device.time_GSM_registration))
    data += ',U'
    if device.enable_acс:
        data += (',A1')
    else:
        data += (',A0')
    data += ',t-30'  # время ожидания смс
    data += ',C'  # обнулисть статистику С0
    data += ',U'  # сервер отправки пакета
    data += ',E'  # номер порта
    data += ',h0'  # время ожидания смс
    return data


def save_message_model(message_list, device, logger):
    new_message = get_message_model(message_list, device)
    try:
        new_message.save()  
    except:
        logger.warn('New message save to db Error. Device: %s. Connection type: %s' % (device, get_type_con(message_list)))
        return False
    try: 
        device = save_parse_data(message_list, device)
        device.save()
        return True
    except:
        logger.warn('Save parse data to db Error')
        return False


def save_parse_data(message_list, device):
    data = message_list[4:-1]   
    for info in data:
        if info[0] == 'S':
            info = info.split(',')
            device.battery_level = int(info[1], 16)*2.56/512
            device.temperature = info[3]
            device.last_message_sim = info[4]
        elif info[0] == 'P':
            info = info.split(',')
            device.GPS_last_HDOP = info[1][1:]
            device.GPS_time_UTC = info[2]
            device.GPS_status = info[3]
            device.GPS_latitude = info[4]
            device.GPS_n_s = info[5]
            device.GPS_longitude = info[6]
            device.GPS_e_w = info[7]
            device.GPS_speed = info[8]
            device.GPS_course = info[9]
            device.GPS_date = info[10][:-1]
        elif info[0] == 'C':
            pass
            # device.GSM_data = info
        elif info[0] == 'Q':
            info = info.split(',')
            device.motion = info[1]
            device.motion_T = info[2]
            device.motion_TS = info[3]
        elif info[0] == 'B':
            device.balance_info = info
        elif info[0] == 'L':
            device.log_data = info
            try:
                index = info.index('F')
                device.data_F = info[index:index+2]
            except:
                pass
            try:
                info_split = info.split(':')
                device.data_time_GPS = info_split[1]
                device.data_time_GSM = info_split[2]
            except:
                pass  
        elif info[0] == 'N':  
            device.device_param = info
        elif info[0] == 'M': 
            info = info.split(',')
            device.SMS_code = info[1]
            device.SMS_text = info[2]
    return device


def get_message_model(message_list, device):
    new_message = Message_from_FM(
        version = message_list[0][1:],
        type_con = message_list[1],
        imei = device,
        sid = message_list[3].split(',')[0],
        p_roaming = message_list[3].split(',')[1],
        ops = message_list[3].split(',')[2],
        data = json.dumps(message_list[4:-1]),
        #data = json.loads(data)
        cs = message_list[-1:][0][1:]
    )
    return new_message


def get_type_con(message_list):
    return message_list[1]

    
def get_imei(message_list):
    return message_list[2]
