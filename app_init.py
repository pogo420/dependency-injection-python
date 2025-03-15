# Application initialization
# Configures inject as well

from dotenv import load_dotenv
import os
from inject import Binder, configure
from db import Db, DevDb, ProdDb

# More details: https://github.com/ivankorobkov/python-inject
# Adding inject.
def _configure_inject(binder: Binder):
    load_dotenv()
    if os.environ.get("IS_DEV") == "T":
        binder.bind_to_constructor(Db, DevDb) # singleton
    else:
        binder.bind_to_constructor(Db, ProdDb)

def init_app():
    configure(
        _configure_inject,
        once=True # guarantees configured loaded once. Seen issues with few webframework.
    )
