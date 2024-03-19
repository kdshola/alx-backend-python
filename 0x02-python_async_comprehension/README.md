## Python - Async Comprehension
This task introduces Learners to:

How to write an asynchronous generator
How to use async comprehensions
How to type-annotate generators

[0-async_generator.py](./0-async_generator.py)
A coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. 

[1-async_comprehension.py](./1-async_comprehension.py)
Coroutine async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

[2-measure_runtime.py](./2-measure_runtime.py)
Contains measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather. measure_runtime measures the total runtime and return it.
