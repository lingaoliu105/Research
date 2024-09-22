from typing import Optional
from img_params import *
import math
import random
import numpy as np

import img_params
from shapely.geometry import Point, LineString, Polygon
from shapely.geometry.base import BaseGeometry
import json
import uid_service
from Entity import Entity


class SimpleShape(Entity):

    direct_categories = [
        "pattern",
        "color",
        "lightness",
        "pattern_color",
        "pattern_lightness",
        "outline",
        "outline_color",
        "outline_thickness",
        "outline_lightness",
    ]  # attributes that can be directly interpreted as categories in dataset annotations
    
    __slots__ = [
        "uid",
        "shape",
        "size",
        "position",
        "rotation",
        "base_geometry",
    ] + direct_categories
    
    touching_tolerance = 1e-11

    def __init__(
        self,
        position: np.ndarray,
        rotation: float,
        size: Optional[float] = None,
        shape: Optional[img_params.Shape] = None,
        color: Optional[img_params.Color] = None,
        pattern: Optional[img_params.Pattern] = None,
        lightness: Optional[img_params.Lightness] = None,
        outline=None,
        outline_lightness=None,
        pattern_color=None,
        pattern_lightness=None,
        outline_color=None,
        outline_thickness=None,
        excluded_shapes_set: set = {},
    ) -> None:
        self.uid = uid_service.get_id_simple_shape()
        self.position = position
        self.rotation = rotation
        self.shape = (
            shape
            if shape is not None
            else random.choice(
                [x for x in list(img_params.Shape) if x not in excluded_shapes_set]
            )
        )
        self.size = size if size is not None else (random.random() + 0.25) * 2
        self.color = (
            color if color is not None else random.choice(list(img_params.Color))
        )
        self.pattern = (
            pattern if pattern is not None else random.choice(list(img_params.Pattern))
        )
        self.pattern_lightness = (
            pattern_lightness
            if pattern_lightness is not None
            else random.choice(list(img_params.PatternLightness))
        )
        self.pattern_color = (
            pattern_color
            if pattern_color is not None
            else random.choice(list(img_params.PattenColor))
        )
        self.outline = (
            outline if outline is not None else random.choice(list(img_params.Outline))
        )
        self.outline_color = (
            outline_color
            if outline_color is not None
            else random.choice(list(img_params.OutlineColor))
        )
        self.outline_thickness = (
            outline_thickness
            if outline_thickness is not None
            else random.choice(list(img_params.OutlineThickness))
        )
        self.outline_lightness = (
            outline_lightness
            if outline_lightness is not None
            else random.choice(list(img_params.OutlineLightness))
        )
        self.lightness = (
            lightness
            if lightness is not None
            else random.choice(list(img_params.Lightness))
        )

        self.compute_base_geometry()

    def compute_base_geometry(self):
        rot_rad = math.radians(self.rotation)
        rot_sin = math.sin(rot_rad)
        rot_cos = math.cos(rot_rad)
        rot_polar = np.array((rot_cos, rot_sin))
        rot_cart = self.size * rot_polar
        if self.shape == Shape.LINE:
            endpoints = [
                np.array(x)
                for x in [
                    (
                        self.position[0] + self.size / 2 * rot_cos,
                        self.position[1] + self.size / 2 * rot_sin,
                    ),
                    (
                        self.position[0] - self.size / 2 * rot_cos,
                        self.position[1] - self.size / 2 * rot_sin,
                    ),
                ]
            ]
            self.base_geometry = LineString(endpoints)

        # TODO: complete other shapes. remember to add last -- first
        elif self.shape == Shape.CIRCLE:
            self.base_geometry = Point(self.position).buffer(self.size)
        else:
            if self.shape == Shape.TRIANGLE_EQ:
                angle_list = [-30, 90, 210]
            elif self.shape == Shape.SQUARE:
                angle_list = [-45, 45, 135, 225]
            elif self.shape == Shape.PENTAGON:
                angle_list = [-54 + 72 * x for x in range(5)]
            elif self.shape == Shape.HEXAGON:
                angle_list = [60 * x for x in range(6)]

            vertices = [None] * (len(angle_list))
            index = 0
            for angle in angle_list:
                rot_rad = math.radians(angle + self.rotation)
                rot_sin = math.sin(rot_rad)
                rot_cos = math.cos(rot_rad)
                rot_polar = np.array((rot_cos, rot_sin))
                rot_cart = self.size * rot_polar
                vertices[index] = self.position + rot_cart
                index += 1
            self.base_geometry = Polygon(vertices)

    def get_vertices(self) -> list:
        return self.base_geometry.exterior.coords

    def get_attach_point(self) -> np.ndarray:
        if self.shape == Shape.CIRCLE:
            rand_rad = random.random() * 2 * math.pi
            return self.position + self.size * np.array(
                [math.cos(rand_rad), math.sin(rand_rad)]
            )
        fraction = (
            random.choice(list(TouchingPosition)).value * random.randint(1, 5) % 1
        )
        vertices = self.get_vertices()
        edge_index = random.randint(
            0, len(vertices) - 2
        )  # the edge is vert[index] -- vert[index+1]
        return vertices[edge_index] + fraction * (
            vertices[edge_index + 1] - vertices[edge_index]
        )

    def check_overlap(self, other: "SimpleShape") -> bool:
        return self.base_geometry.overlaps(other.base_geometry)

    def set_size(self, new_size: float):
        self.size = new_size
        self.compute_base_geometry()

    def search_touching_size(self, other: "SimpleShape"):
        """with a initial size that guarantees to overlap, search the appropriate size that touches the other shape (with tolerance defined in the class), and set the own size to it

        Args:
            other (SimpleShape): the other size you want to touch
        """
        # TODO: optimize performance
        upper = self.size
        lower = 0
        other_shape = other.base_geometry
        while (
            not other_shape.touches(self.base_geometry)
            and (upper - lower) > self.touching_tolerance
        ):
            mid = (upper + lower) / 2.0
            self.set_size(mid)
            if self.base_geometry.overlaps(
                other_shape
            ) or self.base_geometry.intersects(other_shape):
                upper = mid
            else:
                lower = mid

    def search_touching_rotation(self, other: "SimpleShape"):
        self.size = 10000
        self.compute_base_geometry()

        # iterate over all exterior coordinates to find valid rotaion range
        # if other.shape == img_params.Shape.LINE:

    def shift(self, offset: np.ndarray):
        self.position += offset
        self.compute_base_geometry()
