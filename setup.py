from distutils.core import setup

setup(
  name = 'sr_api',
  packages = ['sr_api'],
  version = '1.1.1',
  license='MIT',
  description = 'An async wrapper for some-random-api',
  author = 'Niels Steenman',
  author_email = 'ngssteenman@gmail.com',
  url = 'https://github.com/iDutchy/sr_api',
  download_url = 'https://github.com/iDutchy/sr_api/archive/1.1.1.tar.gz',
  keywords = ['wrapper', 'api', 'random'],
  install_requires=['aiohttp'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)