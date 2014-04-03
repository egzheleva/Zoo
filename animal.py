import sqlite3


def cur():
    conn = sqlite3.connect("animals.db")
    return conn.cursor()


class Animal():

    """docstring for Animal"""

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def grow(self):
        '''
        The animal grows with weight_age_ratio
        for 1 month
        '''
        query = '''SELECT average_weight, weight_age_ratio FROM animals 
                   WHERE species = ?'''
        cursor = cur()
        result = cursor.execute(query, (self.species, )).fetchone()
        average = result[0]
        ratio = result[1]

        if self.weight < average:
            self.weight += ratio

    def eat(self):
        query = '''SELECT food_weight_ratio FROM animals 
                   WHERE species = ?'''
        cursor = cur()
        result = cursor.execute(query, (self.species, )).fetchone()
        return result * self.weight

    def is_dead(self):
        query = '''SELECT life_expectancy FROM animals 
                   WHERE species = ?'''
        cursor = cur()
        result = cursor.execute(query, (self.species, )).fetchone()
        return self.age >= result

    def can_give_birth(self):
        return self.gender == "male"


def main():
    a = Animal("tiger", 20, "TIGYR", "male", 100)
    print(a.weight)
    a.grow()
    print(a.weight)


if __name__ == '__main__':
    main()
