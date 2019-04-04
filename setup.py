import os
import re
from setuptools import setup

base_path = os.path.dirname(__file__)

setup(
  name = 'cloudscrape',
  packages = ['cfscrape'],
  version = 0.2,
  description = 'A fork of cfscrape Cloudflare\'s anti-bot page.',
  author = 'Anorov',
  author_email = 'edmartin101@gmail.com',
  url = 'https://github.com/Anorov/cloudflare-scrape',
  keywords = ['cloudflare', 'scraping'],
  include_package_data = True,
  install_requires = ['requests >= 2.0.0']
)
