import logging

### crear filtro
def show_only_error(record): 
    return record.levelname == 'ERROR'

### create logger
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


### para nivel de consola   .StreamHandler()
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')
### create formater
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


### para escribir en el fichero .FileHandler
file_handler = logging.FileHandler('newlog.log', mode='a', encoding='utf-8')
file_formatter = formatter
file_handler.setLevel('WARNING')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


#### IN exception block
logger.debug('This is a DEBUG')
logger.error('This is a ERROR')


    

