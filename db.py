# DB implementations

class Db:
    def db_name(self):
        pass


class ProdDb(Db):
    def db_name(self):
        return "Prod DB"


class DevDb(Db):
    def db_name(self):
        return "Dev DB"
