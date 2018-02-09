from boltons import (iterutils,
                     strutils,
                     )
from pprint import pprint


for chunk in iterutils.chunked_iter(range(0, 97), 3):
	break
	print(chunk)
else:
	print()
'----------------------------------------------------------------------------------------------------'

for window in iterutils.windowed_iter(range(0, 97), 3):
	break
	print(window)
else:
	print()
'----------------------------------------------------------------------------------------------------'

coffee_pet_words = ('mary', 'had', 'interruption', 'a', 'little', 'python','interruption', 'who', 'loved', 'coffee',
                    'interruption', 'so', 'she', 'named', 'it', 'interruption', 'jython',
                    )
# print(*iterutils.split(coffee_pet_words, sep='interruption'), sep='\n')
'----------------------------------------------------------------------------------------------------'

nope_filename = 'ghjhy6565**^*//\\'
dope_filename = strutils.slugify(nope_filename)
# print(dope_filename)
'----------------------------------------------------------------------------------------------------'


for num in range(0, 102):
	break
	print(strutils.ordinalize(num))
else:
	print()
'----------------------------------------------------------------------------------------------------'

singulars = ['Foot', 'TOOth', 'Fish', 'help', 'python', 'locus', ]
for singular_ in singulars:
	break
	print(strutils.cardinalize(singular_, 1),
	      strutils.cardinalize(singular_, 200),
	      )  # preserves case.
else:
	print('\npluralize:\t',
	      strutils.pluralize('Tetanus'),
	      )
	print('singularize:\t',
	      strutils.singularize('locii'),
	      )
	print()
'----------------------------------------------------------------------------------------------------'


byte_sizes = [1, 200, 1024, 1025, 4096, 1024*1024, 1000, 1e6]
for byte_size_ in byte_sizes:
	break
	print(f'{byte_size_} : {strutils.bytes2human(byte_size_)}')
else:
	print()
'----------------------------------------------------------------------------------------------------'

quit()

import functools

@functools.lru_cache()
def somefunc():
	pass
"""
Memoizes calls by caching functions results in a dict.
When same params are passed in, the cached values are returned instead of new computation.

boltons.cacheutils is a more convenient take on the same thing

"""

