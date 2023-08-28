##.. formatted string literals ..##
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')#output : Results of the 2016 Referendum
print("--------------------")
# str.format() 
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))#Output : 42572654 YES votes  49.67%
print("--------------------")
#//Finally
s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# Repr() dari sebuah string menambahkan tanda kutip string dan garis miring terbalik:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# Argumen untuk repr() dapat berupa objek Python apa saja:
print(repr((x, y, ('spam', 'eggs'))))
print("--------------------")

## ..Formatted String Literals ..##
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
print("--------------------")

## ..The String format() Method ..##
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print("------------------")

#..Manual String Formatting..##
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
#mencetak string dan panjang string yang dihasilkan
print('12'.zfill(5)) 
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
print("------------------")

##..Old string formatting..##
import math
#memformat dan mencetak nilai bilangan bulat atau pecahan dalam bentuk string.
print('The value of pi is approximately %5.3f.' % math.pi)
