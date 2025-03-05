from abc import abstractmethod, ABC
from typing import Any


class AbstractEndpointRequestor(ABC):

    @abstractmethod
    def get(self,  **kwargs) -> Any:
        ...

    @abstractmethod
    def post(self, **kwargs) -> Any:
        ...

    @abstractmethod
    def put(self, **kwargs) -> Any:
        ...

    @abstractmethod
    def delete(self, **kwargs) -> Any:
        ...
