# -*-coding:utf8;-*-
from abc import ABC, abstractmethod
from typing import Callable, Tuple, List, Any, Iterator, Dict
from typing_extensions import Self


class NewTask(ABC):
    func: Callable[..., Any]
    args: Tuple[Any]
    kwargs: Dict[str, Any]

    @abstractmethod
    def __init__(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        pass


class create_task(NewTask):
    def __init__(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
        self.func = func
        self.args: Tuple[Any] = args
        self.kwargs: Dict[str, Any] = kwargs

    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        self.args = args
        self.kwargs = kwargs
        return self


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
