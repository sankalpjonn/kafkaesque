# please install python if it is not present in the system
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

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
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://github.com/sankalpjonn/kafkaesque",
 include_package_data=True,
)
