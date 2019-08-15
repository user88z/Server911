import logging
from logging.handlers import RotatingFileHandler

def get_log(name, log_file):
    # создаём logger c именем вызвавшего модуля
    logger = logging.getLogger(name)
    #определяет минимальный уровень сообщений, которые будут обработаны;
    logger.setLevel(logging.DEBUG) 

    # создаём консольный handler и задаём уровень
    st = logging.StreamHandler()
    st.setLevel(logging.DEBUG)

    logging.addLevelName( logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

    fl = RotatingFileHandler(log_file, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None, delay=0)
    fl.setLevel(logging.DEBUG)

    # создаём formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(thread)d - %(levelname)s - %(message)s')

    # добавляем formatter в ch
    st.setFormatter(formatter)
    fl.setFormatter(formatter)

    # добавляем ch к logger
    logger.addHandler(st)
    logger.addHandler(fl)
    return logger

        # logger.debug('debug message')
        # logger.info('info message')
        # logger.warn('warn message')
        # logger.error('error message')
        # logger.critical('critical message')