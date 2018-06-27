import fdb

con = fdb.connect(dsn='localhost/3050:C:/Users/Daulet/PycharmProjects/AkimBaza/P8.FDB',
                  user='sysdba', password='masterkey')
cur = con.cursor()


def make_chunks(total, c):
    chunks = [total//c for i in range(c)]
    chunks[-1] = chunks[-1] + total%c
    return chunks


def kapusta(column_name, table, total, zamen = False):
    print('in function')
    make_one_null = f'update {table} set {column_name} = null where {column_name} is not null rows 1'
    col_sum = f'select sum({column_name}) from {table}'

    first_checking = cur.execute(col_sum).fetchone()[0] or 0
    while first_checking > total:
        cur.execute(make_one_null)
        first_checking = cur.execute(col_sum).fetchone()[0]

    real_total = cur.execute(col_sum).fetchone()[0] or 0

    print(f'After operation sum({column_name})={real_total}')
    print(f'After operation total-real_total={total-real_total}')

    if total - real_total > 0:
        homes = input('На сколько делить? ')
        try:
            homes = int(homes)
            if homes > 0:
                for i, chunk in enumerate(make_chunks(total-real_total, homes)):
                    add_tale = f'update {table} set {column_name} = {chunk} where {column_name} is null rows 1' if not zamen \
                        else f'update {table} set {column_name} = {column_name} + {chunk} where {column_name} is not null rows {1 + i} to {1 + i}'
                    cur.execute(add_tale)
        except ValueError:
            pass

    con.commit()

    print(f'On function end: sum({column_name})={cur.execute(col_sum).fetchone()[0]}')


print('before function')
try:
    kapusta('barany', 'zhiv', 692, zamen=True)
except Exception:
    print('Ошибка какая-то!!!!!!!!!!!!!')
finally:
    print('after function')
    con.commit()
    con.close()
    print('END')