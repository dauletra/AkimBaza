import fdb
import os
from resource import homes

fdb_file_dir = 'C:/Users/Daulet/PycharmProjects/AkimBaza'
fdb_file_name = 'P1-Aksai-v2.FDB'
fdb_file_path = os.path.join(fdb_file_dir, fdb_file_name)


def to_dot(row):
    row['living_sq'] = row['living_sq'].replace(',', '.')
    row['full_sq'] = row['full_sq'].replace(',', '.')
    return row


def parse_ikd(homesstr):
    hw_ids = homesstr.replace('\t', ' ').split('\n')
    hw_ids = map(lambda x: x.strip(), hw_ids)
    hw_ids = list(filter(lambda x: x != '', hw_ids))
    print(f'Количество: {len(hw_ids)}')

    rows = list()
    for hw_id in hw_ids:
        ikd, ar, house, flat, full_sq, living_sq = hw_id.split(' ')
        rows.append({
            'ikd': ikd.strip(), 'ar': ar.strip(), 'house': house.strip(), 'flat': flat.strip(),
            'full_sq': full_sq.strip(), 'living_sq': living_sq.strip()
        })
    return rows


def find_ar(rows):
    not_found_ikds = []
    found_double_ikds = []
    normal_ikds = []
    for row in rows:
        find_sql = f"select count(ikd) from kpu_rzhf where ikd='{row['ikd']}'"
        cur.execute(find_sql)
        res = cur.fetchone()[0]
        if res == 1:
            normal_ikds.append(row)
        elif res > 1:
            found_double_ikds.append(row)
        elif res == 0:
            not_found_ikds.append(row)
        else:
            print('---- error in find_ar ----')
    return {
        'normal_ikds': normal_ikds,
        'found_double_ikds': found_double_ikds,
        'not_found_ikds': not_found_ikds
    }


def write_to_file(column, file_name):
    with open(file_name, 'w') as f:
        for ikd in column:
            f.write(ikd['ikd'])
            f.write('\n')


def update_ar_codes(codes):
    for code in codes:
        update_sql = f"update kpu_rzhf set ar='{code['ar']}' where ikd={code['ikd']}"
        cur.execute(update_sql)


def make_null_ar_codes():
    update_sql = 'update kpu_rzhf set ar=null'
    cur.execute(update_sql)


if __name__ == '__main__':
    print(fdb_file_path)
    con = fdb.connect(dsn=fdb_file_path, user='sysdba', password='masterkey')
    cur = con.cursor()
    # con.commit()

    rows = parse_ikd(homes)
    result = find_ar(rows)
    print(f"Normal codes: {len(result['normal_ikds'])}")
    update_ar_codes(result['normal_ikds'])

    # write_to_file(result['not_found_ikds'], 'not_found_ikds.txt')
    # write_to_file(result['found_double_ikds'], 'found_double_ikds.txt')
    # write_to_file(result['normal_ikds'], 'normal_ikds.txt')

    con.commit()
    con.close()
