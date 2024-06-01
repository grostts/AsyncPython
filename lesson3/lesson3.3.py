# Ожидание корутин
# import asyncio
#
#
# async def coroutine_1():
#     print("Coroutine 1 is done")
#
#
# async def coroutine_2():
#     print("Coroutine 2 is done")
#
#
# async def coroutine_3():
#     print("Coroutine 3 is done")
#
#
# async def main():
#     task1 = asyncio.create_task(coroutine_1())
#     task2 = asyncio.create_task(coroutine_2())
#     task3 = asyncio.create_task(coroutine_3())
#     await asyncio.gather(task1, task2, task3)
#
#
# asyncio.run(main())


# Секундный интервал
# import asyncio
#
#
# async def print_with_delay(num):
#     await asyncio.sleep(1)
#     print(f'Coroutine {num} is done')
#
#
# async def main():
#     tasks = []
#     for i in range(10):
#         task = asyncio.create_task(print_with_delay(i))
#         tasks.append(task)
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())


# # Счётчики #1
# # Counter 1 - имя счётчика
# # 13 - максимальное значение для счётчика Counter_1
# import asyncio
#
#
# max_counts = {
#     "Counter 1": 13,
#     "Counter 2": 7
# }
#
# counters = {
#     "Counter 1": 0,
#     "Counter 2": 0
# }
#
# async def counter(name, delay):
#     for _ in range(max_counts[name]):
#         counters[name] += 1
#         await asyncio.sleep(delay)
#         print(f'{name}: {counters[name]}')
#
# async def main(delay):
#
#     tasks = [asyncio.create_task(counter(el, delay)) for el in max_counts.keys()]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main(1))



# # Счётчики #2
# import asyncio
#
#
# max_counts = {
#     "Counter 1": 10,
#     "Counter 2": 5,
#     "Counter 3": 15
# }
#
# delays = {
#     "Counter 1": 1,
#     "Counter 2": 2,
#     "Counter 3": 0.5
# }
#
# counters = {
#     "Counter 1": 0,
#     "Counter 2": 0,
#     "Counter 3": 0
# }
#
# async def counter(name, delay):
#     for _ in range(max_counts[name]):
#         counters[name] += 1
#         await asyncio.sleep(delay)
#         print(f'{name}: {counters[name]}')
#
#
# async def main():
#     tasks = [asyncio.create_task(counter(name,delay)) for name, delay in delays.items()]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())

