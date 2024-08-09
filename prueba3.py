import asyncio

async def funcion() -> None:
    ## Conseguir una lista de las tuplas con los sensores
    await out: Tuple[float|int] = asyncio.get_event_loop().run_in_executor(None, get_data, n_sensor)
    out: List[Tuple[int|float]] = await asyncio.gather([get_data_new(n) for n in range(6)])
    return out

if __name__ == '__main__':
    asyncio.run(funcion)




