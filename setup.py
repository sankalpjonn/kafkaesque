# please install python if it is not present in the system
from setuptools import setup

setup(
 name='kafkaesque',
 version='1.0',
 packages=['kafkaesque'],
 install_requires=['kafka-python'],
 license = 'MIT',
 description = 'an easy to use kafka consumer that extends kafka-python, but follows the style of the flask server',
 author = 'Sankalp Jonna',
 author_email = 'sankalpjonna@gmail.com',
 keywords = ['kafka','consumer','kafkaesque','flask','simple','consumer', 'flask style', 'decorator'],
)
