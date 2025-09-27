import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

logging.debug('Debug message')
logging.info('Info message: starting file processing')
logging.warning('Warning: example warning')
logging.error('Error: example error')

print('Wrote app.log — last lines:')
with open('app.log','r', encoding='utf-8') as f:
    for ln in f.readlines()[-5:]:
        print(ln.strip())