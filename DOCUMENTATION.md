# SR_Api

Welcome, and thank you for using this api wrapper! This wrapper is completely async! Please note that I am not the creator of some-random-api. I only made this api wrapper! 

## Getting Started:

To begin with, you'll habe to install the package by doing one of the following commands:
- `pip install -U sr_api`
- `python -m pip -U install sr_api`

Or you can install directly from source by doing one of the following commands:
- `pip install -U git+https://github.com/iDutchy/sr_api`
- `python -m pip install -U git+https://github.com/iDutchy/sr_api`

After that, you will have to create the client:
```python
from sr_api.client import Client

client = Client()
```

For future reference in this documentation: when referring to 'client' we refer to what has been defined above!