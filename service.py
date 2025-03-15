from db import Db
from inject import params

class Service:

    @params(db=Db)
    def __init__(self, db: Db):
        self.res = db.db_name()

