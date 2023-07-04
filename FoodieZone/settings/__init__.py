from .base import *
import os

env = os.environ.get('ENV') if os.environ.get('ENV') else 'local'

if env == 'prod': 
    from .prod import *
elif env == 'dev':
    from .dev import *
else:
    from .local import *