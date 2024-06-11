

from pony.orm import Database

db = Database()


def init_db(db: Database, provider='sqlite', file_name='MCHS.db') -> Database:
    db.bind(provider=provider, filename='MCHS.db', create_db=True)
    db.generate_mapping(create_tables=True)
    return db
