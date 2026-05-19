import time
from fastapi import Request
from typing import Callable
from starlette.responses import Response

async def logging_middleware(request: Request, call_next: Callable) -> Response:

    print("Request URL:", request.url)

    start = time.time()

    response = await call_next(request)

    end = time.time()

    print("Time Taken:", end - start)

    return response