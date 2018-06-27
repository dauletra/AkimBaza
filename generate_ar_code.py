import fdb
import random

con = fdb.connect(dsn='localhost/3050:D:/P1.FDB',
                  user='sysdba', password='masterkey')
cur = con.cursor()


def gen_ar():
    return f'020130025{random.randint(10000, 99999)}99'

print('Start...')
i = 0
while i < 70:
    sample_ar = f'020130025{random.randint(10000, 99999)}99'
    cur.execute(f'select ar from kpu_rzhf where ar = {sample_ar}')
    ar_in_db = cur.fetchone()
    if ar_in_db is None:
        cur.execute(f'update kpu_rzhf set ar = {sample_ar} where ar is null rows 1')
        i = i + 1

print('End...')
con.commit()
con.close()