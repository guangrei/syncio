# -*-coding:utf8;-*-
from abc import ABC, abstractmethod
from typing import Callable, List, Any, Iterator, Dict
from typing_extensions import Self


class NewTask(ABC):
    func: Callable[..., Any]
    args: List[Any]
    kwargs: Dict[str, Any]

    @abstractmethod
    def __init__(self, func: Callable[..., Any]) -> None:
        pass

    @abstractmethod
    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        pass


class create_task(NewTask):
    def __init__(self, func: Callable[..., Any]) -> None:
        self.func = func
        self.args: List[Any] = []
        self.kwargs: Dict[str, Any] = {}

    def __call__(self, *args: Any, **kwargs: Any) -> Self:
        self.args = list(args)
        self.kwargs = dict(kwargs)
        return self


class TaskOutput(dict):  # type: ignore[type-arg]
    def __init__(self, data: Dict[str, Any]) -> None:
        self._data = data
        super().__init__(data)

    def __iter__(self) -> Iterator[Any]:
        output: List[Any] = []
        for _, v in self._data.items():
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
