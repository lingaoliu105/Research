'''
This file defines the abstract class for the entities' hierachy
'''
import copy
from enum import Enum
import json
import random
from typing import Optional

import numpy as np
import shapely
from shapely.geometry.base import BaseGeometry

from generation_config import GenerationConfig
import img_params
import uid_service

from abc import ABC, abstractmethod
from shapely.affinity import translate,rotate

from util import *
import util


class Entity(ABC):

    def __init__(self) -> None:
        self.uid = uid_service.get_new_entity_uid()
    def to_dict(self):
        dict = {attr_name: getattr(self, attr_name) for attr_name in self.serialized_fields}
        for key in dict:
            value = dict[key]
            try:
                json.dumps(value)
            except TypeError:
                if isinstance(value, np.ndarray):
                    value = value.tolist()
                elif isinstance(value, Enum):
                    value = value.name
                elif isinstance(value, BaseGeometry):
                    value = shapely.geometry.mapping(value)
                elif isinstance(value,Entity): # when attribute is SimpleShape instance, only record down the id
                    value = value.uid
                dict[key] = value

        return dict

    def to_tikz(self)->str:
        return self.tikz_converter.convert(self)

    def copy(self):
        return copy.deepcopy(self)

    @property
    def copy(self):
        return copy.deepcopy(self)


class Relationship(Entity,ABC):
    pass