##
from pizza import make_pizza

make_pizza(16, 'onion')
make_pizza(32, 'beef', 'cheese', 'tomato')


##
import pizza

pizza.make_pizza(16, 'onion')
pizza.make_pizza(32, 'beef', 'cheese', 'tomato')

## 
from pizza import make_pizza as mp

mp(16, 'onion')
mp(32, 'beef', 'cheese', 'tomato')

##
import pizza as p

p.make_pizza(16, 'onion')
p.make_pizza(32, 'beef', 'cheese', 'tomato')