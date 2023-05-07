# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:49:52 2023

@author: hadaw
"""
from random import choice
from numpy.random import randint

class Prkg:
    def __init__(self, size):
        super().__init__()
        self.alphabet = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z"
        ]
        self.size = size
        self.keys = self._gk_()
    
    def _res_(self, res):
        try:
            for result in res:
                result=result
            return result
        
        except TypeError:
            result_gen = res()
            return next(result_gen, None) or self._res_(result_gen)
    
    def _prk_(self, cache):
        ch = [1, 2]
        decision = choice(ch)
        random_integer = randint(0, 3)
        split = cache[random_integer].split(",")
        cache.pop(random_integer)
        split.pop(-1)
        split.pop(randint(0, 3))

        for i in range(0, decision):
            split.insert(randint(0, 4), randint(0, 9))

        if decision == 2:
            split.pop(randint(0, 4))

        result = "".join(str(i) for i in split)
        cache.insert(randint(0, 4), result)
    
        x, y, z, t = cache
        
        res = "".join(string for string in (ii for i in cache for ii in i if ii != ","))
        res = "-".join(string for string in (res[i:i+4] for i in range(0, len(res), 4)))
    
        return res

        
   
    def _prl_(self, size):
        result = ""
        
        cache = set()
        for i in range(0, 26):
            result = result+self.alphabet[randint(0,26)]+","
            
            if len(result) >= size+3:
                cache.add(result)
                result = ""
                
                
                if len(cache) >= size:
                    yield list(cache)
                    cache.clear()
                    break
        if cache:
            yield list(cache)
            
    def _gk_(self):
        keys = set()
        self._res_((keys.add(self._prk_(self._res_(self._prl_(4)))) for i in range(0, self.size)))
        
        with open("key_file.txt", "w") as file:
            file.write(",\n".join(keys))
        
        return list(keys)
        
    
# pkg = Prkg(1000)
# keys = pkg.keys




