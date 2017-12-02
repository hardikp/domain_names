import sqlite3
from time import sleep

import boto3


class CheckNames(object):
    def __init__(self):
        self.client = boto3.client('route53domains')

    def get_status(self, name):
        # http://boto3.readthedocs.io/en/latest/reference/services/route53domains.html#Route53Domains.Client.check_domain_availability
        response = self.client.check_domain_availability(DomainName=name)
        status = response['Availability']

        if status == 'PENDING':
            sleep(1)

            response = self.client.check_domain_availability(DomainName=name)
            status = response['Availability']

        return status


if __name__ == '__main__':
    check_names = CheckNames()

    # CREATE TABLE domains (name TEXT, com TEXT, io TEXT, co TEXT, ai TEXT)
    conn = sqlite3.connect('domains.db')
    c = conn.cursor()

    # Fetch 10 null entries
    c.execute('SELECT * FROM domains WHERE com is NULL LIMIT 10')
    entries = c.fetchall()

    for entry in entries:
        name = entry[0]
        status = check_names.get_status(name + '.com')

        query = 'UPDATE domains SET com = "{}" WHERE name = "{}"'.format(status, name)
        print(query)
        c.execute(query)
        conn.commit()
