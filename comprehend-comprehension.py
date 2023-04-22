"""  Given this sort of dict (country:city-list):

{'Israel': ['Jerusalem', 'Tel Aviv'],
'USA': ['Boston', 'New York', 'Chicago'],
'China': ['Beijing', 'Shanghai']}

    Use a nested list comprehension to produce a list of
    tuples that look like (city, country)."""



"""Answer:"""
country_list = [{(value , key)  for v in country.values() for value in v for key in country.keys() if v == country[key]}]
print(country_list)


""" Write a function sums_to_n that takes an argument n,
    and returns all two-element tuples that sum to n.

    sums_to_n(5)

    [(0,5), (1,4), (2,3), (4,1), (5,0)]"""

"""Answer"""

def sums_to_n(num):
    new_list = [ (i , num - i)  for i in range(num) ]
    return new_list

print(sums_to_n(5))
