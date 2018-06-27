"""24372357
4446690
4453276
24372663
24372634
24372675
24372640
4445414
24372657
24372338
24372321
24372321
4446496
24372344
4445727
4446566
897879700
897879860
24372611
651150346
4452443
897880085
897879983
897880168
"""
import fdb

con = fdb.connect(dsn='localhost/3050:C:/Users/Daulet/PycharmProjects/AkimBaza/P1_Aksai.FDB',
                  user='sysdba', password='masterkey')
cur = con.cursor()


def make_chunks(total, c):
    chunks = [total//c for i in range(c)]
    chunks[-1] = chunks[-1] + total%c
    return chunks


def update_posev_sum_sql(self):
    sum_posev_sql = 'update zem set posev=coalesce(semena_masl, 0) + coalesce(ovoshi, 0) + coalesce(soloma, 0)'
    sum_semena_masl_sql = 'update zem set semena_masl=semena_pods'
    sum_ovoshi_sql = ('update zem set ovoshi=coalesce(kapusta, 0) + coalesce(pertsy, 0) + coalesce(ogurcy, 0) + '
                      'coalesce(baklazhan, 0) + coalesce(pomidor, 0) + coalesce(morkov, 0) + coalesce(luk, 0) + '
                      'coalesce(kartofel, 0)')
    sum_soloma_sql = 'update zem set soloma=korm_seno'


def totalize_zem_column(column_name, total):
    print(f'Нужная сумма: {total}')

    make_one_null_sql = f'update zem set {column_name} = null where {column_name} is not null rows 1'
    column_sum_sql = f'select sum({column_name}) from zem'

    column_sum = cur.execute(column_sum_sql).fetchone()[0] or 0
    print(f'Реальная сумма: {column_sum}')
    while column_sum > total:
        cur.execute(make_one_null_sql)
        column_sum = cur.execute(column_sum_sql).fetchone()[0]

    print(f'После while: sum({column_name})={column_sum}')
    print(f'После while: total-column_sum={total-column_sum}')

    if total > column_sum:
        homes = input(f'На сколько делить? [{total-column_sum}] ')
        try:
            homes = int(homes)
            less_than_pashnya = 'coalesce(semena_pods, 0) + coalesce(ovoshi, 0) + coalesce(soloma, 0)'
            if homes > 0:
                for i, chunk in enumerate(make_chunks(total-column_sum, homes)):
                    add_tale = f'update zem set {column_name} = coalesce({column_name}, 0) + {chunk} where pashnya >= ({less_than_pashnya} + {chunk}) rows {1 + i} to {1 + i}'
                    cur.execute(add_tale)
        except ValueError:
            print('Остаток не добавлено...')

    con.commit()

    print(f'Конец: sum({column_name})={cur.execute(column_sum_sql).fetchone()[0]}')


print('Старт...')
try:
    totalize_zem_column('kapusta', 10000)
except Exception:
    print('Ошибка в функции kapusta!!!')
finally:
    print('Операция завершен. Коммит...')
    con.commit()
    con.close()
    print('Соединение закрыто')
