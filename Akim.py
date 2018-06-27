import fdb


class Zem:
    semena_pods: int = None
    kapusta: int = None
    pertsy: int = None
    ogurcy: int = None
    baklazhan: int = None
    pomidor: int = None
    morkov: int = None
    luk: int = None
    kartofel: int = None
    korm_seno: int = None

    def update_posev_sum_sql(self):
        sum_posev_sql = 'update zem set posev=coalesce(semena_masl, 0) + coalesce(ovoshi, 0) + coalesce(soloma, 0)'
        sum_semena_masl_sql = 'update zem set semena_masl=semena_pods'
        sum_ovoshi_sql = ('update zem set ovoshi=coalesce(kapusta, 0) + coalesce(pertsy, 0) + coalesce(ogurcy, 0) + '
                          'coalesce(baklazhan, 0) + coalesce(pomidor, 0) + coalesce(morkov, 0) + coalesce(luk, 0) + '
                          'coalesce(kartofel, 0)')
        sum_soloma_sql = 'update zem set soloma=korm_seno'

    def select_column_sum_sql(self, column_name):
        return f'select sum({column_name}) from zem'


class Akim:
    con: fdb.fbcore.Connection
    cur: fdb.fbcore.Cursor
    zem: Zem = None

    def __init__(self, abs_path):
        self.con = fdb.connect(dsn=abs_path, user='sysdba', password='masterkey')
        self.cur = self.con.cursor()

    def totalize_zem_columns(self, column_name):
        column_sum = self.cur.execute(self.zem.column_sum(column_name)).fetchone()[0] or 0




if __name__ == '__main__':
    print('Akim')
