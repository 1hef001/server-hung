import asyncio
import time


async def wait_host_port(host, port, duration=10, delay=2):
    """Repeatedly try if a port on a host is open until duration seconds passed

    Parameters
    ----------
    host : str
        host ip address or hostname
    port : int
        port number
    duration : int, optional
        Total duration in seconds to wait, by default 10
    delay : int, optional
        delay in seconds between each try, by default 2

    Returns
    -------
    awaitable bool
    """
    tmax = time.time() + duration
    while time.time() < tmax:
        try:
            _reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=5)
            writer.close()
            await writer.wait_closed()
            return True
        except:
            if delay:
                await asyncio.sleep(delay)
    return False

# task = asyncio.create_task(wait_host_port("www.google.com", 79))

# asyncio.run_until_complete(task)


if(asyncio.run(wait_host_port("www.google.com", 8))):
    print("port is free")
else:
    print("port is engaged")


NO_OF_PORTS = 10
PORTS = []
THRESHOLD = int(0.75 * NO_OF_PORTS)
