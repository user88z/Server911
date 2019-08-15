from django.core.management.base import BaseCommand

from ._getlog import get_log
from ._validation import validation, CRC
from ._data import save_message, get_answer, get_device_data
from ._coordinates import get_GSM_coordinates

from socketserver import StreamRequestHandler, TCPServer

from userProfile.models import Device, Message_from_FM, userProfile

host = '192.168.245.16'
port = 24760
addr = (host,port)
logger = get_log('Aggregator', 'log.log')

class MyTCPHandler(StreamRequestHandler):
    
    def handle(self):     
        self.data = self.request.recv(4096)
        address = self.client_address[0] + ':' + str(self.client_address[1])
        logger.info('Address: %s. Get data: %s' % (address, str(self.data.decode('utf-8'))))
        data = self.data.decode()

        if validation(data, logger):
            device_data = get_device_data(data)
            if device_data == None:
                answer = b'$ERROR'
            else:
                save_message(data, device_data, logger)
                answer = get_answer(data, device_data, logger)    
        else:
            answer = b'$ERROR'
        try:
            self.request.sendall(answer)
            address = self.client_address[0] + ':' + str(self.client_address[1])
            logger.info('Address: %s. Send data: %s' % (address, str(answer.decode('utf-8'))))
        except:
            logger.warn('Send error') 
           

class Command(BaseCommand):
    def handle(self, *args, **options):
        server = TCPServer(addr, MyTCPHandler)
        logger.info('Starting server... for exit press Ctrl+C')
        server.serve_forever() 

    
