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
  5551000    8.326    0.000   16.054    0.000 app.py:46(is_barycentric)
     1000    1.933    0.002   19.104    0.019 app.py:57(triangle)
        1    0.000    0.000    0.000    0.000 cProfile.py:117(__exit__)
     3000    0.000    0.000    0.000    0.000 model.py:17(__eq__)
  5551000    3.042    0.000    4.111    0.000 model.py:20(__xor__)
 22204000    4.380    0.000    4.380    0.000 model.py:9(__init__)
  2521000    1.113    0.000    1.113    0.000 np_image.py:33(set_color)
  5551000    0.305    0.000    0.305    0.000 {built-in method builtins.abs}
    12000    0.002    0.000    0.002    0.000 {built-in method builtins.max}
    12000    0.002    0.000    0.002    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
