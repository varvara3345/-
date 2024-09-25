import sqlite3
import json

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('../../Desktop/NoteBot/Records.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS record (id INTEGER PRIMARY KEY NOT NULL UNIQUE, recordss TEXT,name_id  TEXT UNIQUE);')

    def add_user(self, nid):
        with self.connection:
            result = self.cursor.execute(
                "SELECT name_id FROM record WHERE name_id == {key}".format(key=nid)).fetchone()
        if not result:
            self.cursor.execute(f"INSERT INTO record (name_id) VALUES ({nid})")
            self.connection.commit()

    def add_record(self,nid,rec):
            res = self.cursor.execute("SELECT recordss FROM record WHERE name_id == {key}".format(key=nid)).fetchone()
            if res[0] is not None:
                r = json.loads(res[0])
                for k,v in rec.items():
                    r[k] = r.get(k,'')+f'\n{v}'
                self.cursor.execute("UPDATE record SET recordss = ? WHERE name_id = ?", (json.dumps(r), nid))
                self.connection.commit()
            else:
                self.cursor.execute("UPDATE record SET recordss = ? WHERE name_id = ?", (json.dumps(rec), nid))
                self.connection.commit()

    def ret_record(self,date,nid):
        d = json.loads(self.cursor.execute("SELECT recordss FROM record WHERE name_id == {key}".format(key=nid)).fetchone()[0])
        return d.get(date,False)


    def get_key(self,nid):
        try:
            return json.loads(self.cursor.execute("SELECT recordss FROM record WHERE name_id == {key}".format(key=nid)).fetchone()[0]).keys()
        except:
            return None

