# import asyncio
#
#
# async def example_coroutine():
#     print("Hello from coroutine!")



# import asyncio
#
#
# async def example_coroutine():
#     await asyncio.sleep(1)  # запускаем внутри корутины асинхронную функцию sleep()
#     print("Hello from coroutine!")



# import asyncio
#
#
# async def example_coroutine(number, *args, **kwargs):
#     await asyncio.sleep(1)  # запускаем внутри корутины асинхронную функцию sleep()
#     print(f"Hello from coroutine {number}!")
#     return f"Корутина {number} завершила работу"



# #НЕ ПРАВИЛЬНО
# async def example_coroutine():
#     print("Hello from coroutine!")
#
# example_coroutine()  # создан объект корутины example_coroutine(), корутина не запущена!
#
#
# #ПРАВИЛЬНО
# async def example_coroutine():
#     print("Hello from coroutine!")
#
# asyncio.run(example_coroutine())  # корутина example_coroutine() запущена.



# import asyncio
#
#
# async def example_coroutine():
#     await asyncio.sleep(1)
#     print("Hello from coroutine!")
#
# async def main():
#     await example_coroutine() # запускаем example_coroutine() и ждем выполнения
#
# asyncio.run(main())  # Точка входа



# import asyncio
#
#
# async def example_coroutine():
#     print("Hello from coroutine!")
#     await asyncio.sleep(1)
#
# async def main():
#     for _ in range(10):
#         await example_coroutine()
#
# asyncio.run(main())



# # Hello, Asyncio!
# import asyncio
#
# async  def main():
#     print("Hello, Asyncio!")
#
# asyncio.run(main())



# # Двойное асинхронное приветствие
# import asyncio
#
#
# async def coro_1():
#     print("coro_1 says, hello coro_2!")
#
# async def coro_2():
#     print("coro_2 says, hello coro_1!")
#
# async def main():
#     await coro_1()
#     await coro_2()
#
# asyncio.run(main())



# # Асинхронная генерация чисел
# import asyncio
#
#
# async def generate(n):
#     print(f"Корутина generate с аргументом {n}")
#
# async def main():
#     for n in range(10):
#         await generate(n)
#
#
# asyncio.run(main())



# # Тайная путаница корутин
# import asyncio
#
#
# async def coro_1():
#     print("Вызываю корутину 0")
#
#
# async def coro_5():
#     print("Вызываю корутину 3")
#     await coro_3()
#
#
# async def coro_3():
#     print("Вызываю корутину 2")
#     await coro_2()
#
#
# async def coro_4():
#     print("Вызываю корутину 1")
#     await coro_1()
#
#
# async def coro_2():
#     print("Вызываю корутину 4")
#     await coro_4()
#
#
# asyncio.run(coro_5())




