from .base import *
import os

env = os.environ.get('ENV') if os.environ.get('ENV') else 'dev'

if env == 'prod': 
    from .prod import *
else:
    from .dev import *
