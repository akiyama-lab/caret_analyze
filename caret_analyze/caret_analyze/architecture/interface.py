# Copyright 2021 Research Institute of Systems Planning, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta
from abc import abstractmethod
from typing import List, Optional

from ..communication import Communication
from ..communication import VariablePassing
from ..node import Node

UNDEFINED_STR = 'UNDEFINED'
IGNORE_TOPICS = ['/parameter_events', '/rosout', '/clock']


class PathAlias:

    def __init__(self, alias: str, callback_names: List[str]):
        self.path_name = alias
        self.callback_names = callback_names


class ArchitectureInterface(metaclass=ABCMeta):

    @property
    @abstractmethod
    def nodes(self) -> List[Node]:
        pass

    @property
    @abstractmethod
    def communications(self) -> List[Communication]:
        pass

    @property
    @abstractmethod
    def variable_passings(self) -> List[VariablePassing]:
        pass

    @property
    @abstractmethod
    def path_aliases(self) -> List[PathAlias]:
        pass


class ArchitectureImporter(ArchitectureInterface):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self, path: str, ignore_topics: Optional[List[str]] = None) -> None:
        pass


class ArchitectureExporter(metaclass=ABCMeta):

    @abstractmethod
    def execute(
        self, architecture: ArchitectureInterface, path_aliases: List[PathAlias], path: str
    ) -> None:
        pass
