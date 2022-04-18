# Python Mimic TinyRenderer

Inspire by <https://github.com/ssloy/tinyrenderer>

## Chapter 1

running the profiling, seeking any optimization applicable, testing @30000 iter

@ 3rd attempt:

``` txt
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  2040000    0.742    0.000    0.742    0.000 app.py:12(set_color)
    30000    0.547    0.000    1.292    0.000 app.py:16(line)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
    60000    0.003    0.000    0.003    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

@ 4th attempt, reducing the calc, reduce exec time by ~20%:

``` txt
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  2040000    0.712    0.000    0.712    0.000 app.py:12(set_color)
    30000    0.432    0.000    1.148    0.000 app.py:16(line)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
    90000    0.004    0.000    0.004    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

@ 5th attempt, seems further optz ~10%:

``` txt
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  2040000    0.694    0.000    0.694    0.000 app.py:12(set_color)
    30000    0.388    0.000    1.086    0.000 app.py:16(line)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
    90000    0.004    0.000    0.004    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## Chapter 2

line sweeping method

``` txt
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.450    0.000    1.377    0.001 app.py:57(triangle)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
  2661000    0.927    0.000    0.927    0.000 np_image.py:25(set_color)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

barycentric method, this may scan unneccessary pixel?

``` txt
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  5551000    3.630    0.000    3.630    0.000 app.py:46(barycentric)
     1000    1.389    0.001    5.985    0.006 app.py:57(triangle)
     1000    0.000    0.000    0.000    0.000 app.py:79(<listcomp>)
     1000    0.000    0.000    0.000    0.000 app.py:80(<listcomp>)
     1000    0.000    0.000    0.000    0.000 app.py:81(<listcomp>)
     1000    0.000    0.000    0.000    0.000 app.py:82(<listcomp>)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
  2519000    0.963    0.000    0.963    0.000 np_image.py:25(set_color)
     2000    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     2000    0.001    0.000    0.001    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
