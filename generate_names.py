import random
import sqlite3
import string

vowels = list('aeiou')
consonents = list(set(string.ascii_lowercase) - set(vowels))


class GenerateNames(object):
    def __init__(self, min_length=4, max_length=5):
        self.min_length = min_length
        self.max_length = max_length

    def new_name(self):
        name = 'a'  # First letter has to be a

        name += random.choice(consonents)
        name += random.choice(vowels)

        length = random.randrange(self.min_length, self.max_length + 1)
        for i in range(length - 3):
            name += random.choice(string.ascii_lowercase)

        return name

    def get(self, count=1000):
        names = []
        for i in range(count):
            name = self.new_name()
            while name in names:
                name = self.new_name()

            names.append(name)

        return names


if __name__ == '__main__':
    names = GenerateNames().get()
    print(names)

    # CREATE TABLE domains (name TEXT, com TEXT, io TEXT, co TEXT, ai TEXT)
    conn = sqlite3.connect('domains.db')
    c = conn.cursor()

    for name in names:
        c.execute('SELECT * FROM domains WHERE name = "{}"'.format(name))
        fetched_names = c.fetchall()
        if len(fetched_names) > 0:
            continue

        # Insert
        c.execute('INSERT INTO domains (name) VALUES ("{}")'.format(name))
        conn.commit()
