# -*-coding:utf8;-*-
from abc import ABC, abstractmethod
from typing import Callable, Tuple, List, Any, Iterator, Dict
from typing_extensions import Self
import traceback
import pprint


class NewTask(ABC):
    func: Callable[..., Any]
    args: Tuple[Any, ...]
    kwargs: Dict[str, Any]

    @abstractmethod
    def __init__(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class create_task(NewTask):
    def __init__(
        self,
        func: Callable[..., Any],
        args: Tuple[Any, ...] = (),
        kwargs: Dict[str, Any] = {},
    ) -> None:
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        self.args = args
        self.kwargs = kwargs
        return self

    def __repr__(self) -> str:
        if hasattr(self.func, "__name__"):
            return f"<NewTask '{self.func.__name__}'>"
        else:
            return f"<NewTask '{type(self.func).__name__}'>"


class TaskOutput(dict):  # type: ignore[type-arg]
    def __iter__(self) -> Iterator[Any]:
        output: List[Any] = []
        for _, v in self.items():
            output.append(v)
        self._output_list = output
        self._index = 0
        return self

    def __next__(self) -> Any:
        if self._index >= len(self._output_list):
            raise StopIteration
        value: Any = self._output_list[self._index]
        self._index += 1
        return value

    def __str__(self) -> str:
        return pprint.pformat(self, indent=2)


class TaskReturnException:
    def __init__(self, e: BaseException) -> None:
        self.exception: BaseException = e

    def print_exception(self) -> None:
        traceback.print_exception(
            type(self.exception), self.exception, self.exception.__traceback__
        )

    def __repr__(self) -> str:
        return f"<TaskReturnException '{self.exception.__class__.__name__}'>"

    def __bool__(self) -> bool:
        return False

    def __len__(self) -> int:
        return 0
