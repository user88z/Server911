def validation(message, logger):
    try:
        symbol_index = message.index('*')
        message_crc = message[symbol_index + 1 : symbol_index + 3]
        message = message[:symbol_index]
    except:
        logger.warn('CRC not found')
        return False
    marker = message[0]
    crc = CRC(message).decode('utf-8')
    if message_crc == crc and marker == '$':
        return True
    else:
        logger.warn('CRC error')
    return False

def CRC(message):
    message_inByte = message.encode('utf-8')
    crc = 0
    for symbol in message_inByte:
        crc = crc + symbol
    crc = crc % 256

    if crc < 16:
        crc = b'0' + bytes(str(hex(crc))[2:].upper(), 'utf-8')
    else:
        crc = bytes(str(hex(crc))[2:].upper(), 'utf-8')
    return crc