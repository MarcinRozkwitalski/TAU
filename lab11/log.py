import logging

logging.basicConfig(filename='Testing.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def addition(a,b):
    return a + b
def multiply(a,b):
    return a * b

a = 7
b = 13

logging.info("Test from 'log.py' has been started")
logging.debug('Adding two numbers: {} + {} '.format(a, b))
additionResult = addition(a,b)
logging.info(additionResult)
logging.debug('Multiplying two numbers: {} * {} '.format(a, b))
multiplyResult = multiply(a,b)
logging.info(multiplyResult)
logging.debug('Adding two numbers: {} + {} '.format("b", "a"))
additionResult2 = addition("b","a")
logging.error(additionResult2)
logging.debug('Multiplying two numbers: {} * {} '.format("a", "b"))
multiplyResult2 = multiply("a", "b")
logging.error(multiplyResult2)
logging.info("Test from 'log.py' has been ended")