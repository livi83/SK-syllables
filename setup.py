from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='sk_syllables',
  version='0.0.1',
  description='Divide slovak words to syllables',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Lívia Kelebercová',
  author_email='livia.kelebercova@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='slovak, syllables, nlp', 
  packages=find_packages(),
  install_requires=['re'] 
)