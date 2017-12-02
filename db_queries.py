from argparse import ArgumentParser
import sqlite3

# CREATE TABLE domains (name TEXT, com TEXT, io TEXT, co TEXT, ai TEXT)
conn = sqlite3.connect('domains.db')
c = conn.cursor()


def get_com_domains(limit=10):
    query = 'SELECT name FROM domains WHERE com = "AVAILABLE"'
    c.execute(query)
    results = c.fetchall()

    domains = []
    for result in results:
        domains.append(result[0] + '.com')

    return domains


def count_all():
    query = 'SELECT COUNT(*) as count FROM domains'
    c.execute(query)
    results = c.fetchall()
    return results[0][0]


def count_non_null():
    query = 'SELECT COUNT(*) as count FROM domains WHERE com is not NULL'
    c.execute(query)
    results = c.fetchall()
    return results[0][0]


def count_available():
    query = 'SELECT COUNT(*) as count FROM domains WHERE com = "AVAILABLE"'
    c.execute(query)
    results = c.fetchall()
    return results[0][0]


def count_unavailable():
    query = 'SELECT COUNT(*) as count FROM domains WHERE com = "UNAVAILABLE"'
    c.execute(query)
    results = c.fetchall()
    return results[0][0]


if __name__ == '__main__':
    parser = ArgumentParser(description='Query domain availability database')
    # parser.add_argument('--com_domains')

    print('ALL:', count_all())
    print('NonNull:', count_non_null())
    print('AVAILABLE:', count_available())
    print('UNAVAILABLE:', count_unavailable())

    for domain in get_com_domains():
        print(domain)
