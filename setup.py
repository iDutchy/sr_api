from distutils.core import setup
setup(
  name = 'sr_api',
  packages = ['sr_api'],
  version = '0.1',
  license='MIT',
  description = 'An async wrapper for some-random-api',
  author = 'Niels Steenman',
  author_email = 'ngssteenman@gmail.com',
  url = 'https://github.com/iDutchy',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['wrapper', 'api', 'random'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
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
