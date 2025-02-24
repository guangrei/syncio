[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) 
[![mypy](https://github.com/guangrei/syncio/actions/workflows/mypy_check.yml/badge.svg)](https://github.com/guangrei/syncio/actions) 

[![Downloads](https://static.pepy.tech/badge/syncio)](https://pepy.tech/project/syncio)
[![Downloads](https://static.pepy.tech/badge/syncio/month)](https://pepy.tech/project/syncio)
[![Downloads](https://static.pepy.tech/badge/syncio/week)](https://pepy.tech/project/syncio)

Syncio is inspired by `asyncio`. you can easy to create task and gather with `syncio.gather()` (multiprocessing) or `syncio.thread_gather()` (threading).

## Example
```python
from syncio import create_task, gather


def hello(n: int) -> str:
    return f"hello {n + 1}"


tasks = [create_task(hello)(i) for i in range(3)]
results = gather(*tasks)
print("output task_1:", results["task_1"])
print("output task_2:", results["task_2"])
print("output task_3:", results["task_3"])

# or using iterator

for result in results:
    print(result)

```
author: guangrei.