import os
import re
from setuptools import setup

base_path = os.path.dirname(__file__)

setup(
  name='cloudscrape',
  packages=['cfscrape'],
  version=0.4,
  description='A fork of cfscrape Cloudflare\'s anti-bot page.',
  author='Edmund',
  author_email='edmartin101@gmail.com',
  url='https://github.com/EdmundMartin/cloudflare-scrape',
  keywords=['cloudflare', 'scraping'],
  include_package_data=True,
  install_requires=['requests >= 2.0.0', 'js2py >= 0.60']
)
