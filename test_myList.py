from unittest import TestCase
from __init__ import *


class TestMyList(TestCase):
  def test_all(self):
    l: MyList[T] = listOf(3, 4, 5)
    print(l)
    print([3, 5, 6].toList())
    print(l.toList())
    print(l.filter(lambda it: it == 3))
    print(l.zipMany(listOf(4, 5, 6), listOf("s", "d")))
    
    print(l.fold(0, add))
    print(l + [3, 4, 5])
    print(l.filter(lambda it: it > 3).zip([3, 4, 5]).toMap())
    
    s: MySet[T] = setOf(3, 4, 5, 4)
    print(s)
    
    print(s.fold(0, add))
    
    print(s.find(lambda it: it is 5))
    print(s - {3})
    print(s + {3})

    print({3:2, 4:"dd"}.toList())
    print({3:2, 4:"dd"}.toList().toMap())
    print({3:2, 4:"dd"}.toSet())
    print({3:2, 4:"dd"}.toSet().toMap())
    print({3:2, 4:"dd"}.toMap())