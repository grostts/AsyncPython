import asyncio

async def fetch_data():
    print("Начинаем загрузку данных")
    await asyncio.sleep(2)  # Имитация асинхронной операции ввода-вывода
    print("Данные загружены")
    return {'data': 123}

async def main():
    tasks = [fetch_data() for _ in range(500)]
    results = await asyncio.gather(*tasks)
    print(f"Загружено {len(results)} задач")

asyncio.run(main())