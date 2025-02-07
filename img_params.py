# The enumeration classes of different image parameters

from enum import Enum


class Shape(
    Enum
):  # representing categories under A_type, value normally indicates the number of edges
    linesegment = 0
    circle = 1
    triangle = 3
    square = 4
    pentagon = 5
    hexagon = 6
    # dot =
    rectangle = 7
    triangle_rt = 8
    # heptagon =
    # octagon =
    # nonagon =
    # decagon =
    # ellipse =
    # star =
    # diamond =
    arbitrary = 9


class Type(Enum):
    DOT = "dot"
    LINESEGMENT = "linesegment"
    TRIANGLE = "triangle"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    PENTAGON = "pentagon"
    HEXAGON = "hexagon"
    HEPTAGON = "heptagon"
    OCTAGON = "octagon"
    NONAGON = "nonagon"
    DECAGON = "decagon"
    CIRCLE = "circle"
    ELLIPSE = "ellipse"
    STAR = "star"
    DIAMOND = "diamond"
    ARROW = "arrow"
    DOUBLEARROW = "doublearrow"
    ARC = "arc"
    INTERSECTIONDOT = "intersectionDot"
    INTERSECTIONLINESEGMENT = "intersectionLineSegment"
    INTERSECTIONARC = "intersectionArc"
    INTERSECTIONREGION = "intersectionRegion"


class Color(Enum): 
    white = 0
    black = 1
    red = 2
    green = 3
    blue = 4
    cyan = 5
    magenta = 6
    yellow = 7
    purple = 8
    brown = 9
    orange = 10


class Angle(
    Enum
):  
    deg0 = 0
    deg15 = 15
    deg30 = 30
    deg45 = 45
    deg60 = 60
    deg75 = 75
    deg90 = 90
    deg105 = 105
    deg120 = 120
    deg135 = 135
    deg150 = 150
    deg165 = 165
    deg180 = 180
    degMinus15 = -15
    degMinus30 = -30
    degMinus45 = -45
    degMinus60 = -60
    degMinus75 = -75
    degMinus90 = -90
    degMinus105 = -105
    degMinus120 = -120
    degMinus135 = -135
    degMinus150 = -150
    degMinus165 = -165


class Pattern(Enum):  # the pattern (dots, lines, etc) that fills up the shape
    blank = 0
    horizontalLines = 1
    verticalLines = 2
    northEastLines = 3
    northWestLines = 4
    grid = 5
    crosshatch = 6
    dots = 7
    crosshatchDots = 8
    fivepointedStars = 9
    sixpointedStars = 10
    bricks = 11
    checkerboard = 12


class TouchingPosition(Enum):
    ENDPOINT = 0
    MIDDLE = 0.5
    THIRD = 0.33
    QUARTER = 0.25
    FIFTH = 0.2


class AttachType(Enum):
    """defines how 1 shape touches the other."""

    EDGE = 0
    ARC = 1
    CORNER = 2


class AttachPosition(Enum):
    TOP = 0
    NEAR_TOP = 0.25
    MIDDLE = 0.5
    NEAR_BOTTOM = 0.75
    BOTTOM = 1
    NA = -1  # not applicable, used for arc and corner


class Lightness(Enum):
    lightness0 = 0
    lightness20 = 20
    lightness25 = 25
    lightness33 = 33
    lightness40 = 40
    lightness50 = 50
    lightness60 = 60
    lightness67 = 67
    lightness75 = 75
    lightness80 = 80
    lightness100 = 100


class PattenColor(Enum):
    patternWhite = 0
    patternBlack = 1
    patternRed = 2
    patternGreen = 3
    patternBlue = 4
    patternCyan = 5
    patternMagenta = 6
    patternYellow = 7
    patternPurple = 8
    patternBrown = 9
    patternOrange = 10


class PatternLightness(Enum):
    patternLightness20 = 20
    patternLightness25 = 25
    patternLightness33 = 33
    patternLightness40 = 40
    patternLightness50 = 50
    patternLightness60 = 60
    patternLightness67 = 67
    patternLightness75 = 75
    patternLightness80 = 80
    patternLightness100 = 100


class Outline(Enum):
    solid = 0
    dotted = 1
    denselyDotted = 2
    looselyDotted = 3
    dashed = 4
    denselyDashed = 5
    looselyDashed = 6
    dashDot = 7
    denselyDashDot = 8
    dashDotDot = 9
    denselyDashDotDot= 10
    looselyDashDotDot = 11


class OutlineColor(Enum):
    outlineWhite = 0
    outlineBlack = 1
    outlineRed = 2
    outlineGreen = 3
    outlineBlue = 4
    outlineCyan = 5
    outlineMagenta = 6
    outlineYellow = 7
    outlinePurple = 8
    outlineBrown = 9
    outlineOrange = 10


class OutlineLightness(Enum):
    outlineLightness20 = 20
    outlineLightness25 = 25
    outlineLightness33 = 33
    outlineLightness40 = 40
    outlineLightness50 = 50
    outlineLightness60 = 60
    outlineLightness67 = 67
    outlineLightness75 = 75
    outlineLightness80 = 80
    outlineLightness100 = 100


class OutlineThickness(Enum):
    noOutline = 0
    ultraThin = 1
    veryThin = 2
    thin = 3
    semithick = 4
    thick = 5
    veryThick = 6
    ultraThick = 7

class HorizontalPosition(Enum):
    """Given a single entity, this supercategory represents the horizontal position
    of that entity, relative to the panel that the entity belongs to
    """
    left=0
    nearLeft=1
    leftwards=2
    slightlyLeftwards=3
    horizontalMiddle=4
    slightlyRightwards=5
    rightwards=6
    nearRight=7
    right=8

class  VerticalPosition(Enum):
    """Given a single entity, this supercategory represents the vertical position of
    that entity, relative to the panel that the entity belongs to.
    """
    top=0
    nearTop=1
    high=2
    slightlyHigher=3
    verticalMiddle=4
    slightlyLower=5
    low=6
    nearBottom=7
    bottom=8
