# coding=utf-8
from __future__ import unicode_literals

CANVAS_RENDERER = "canvas"
SVG_RENDERER = "svg"
PAGE_TITLE = "Echarts"

# presentation types for jupyter
# output file types for pure python
SVG = "svg"
PNG = "png"
JPEG = "jpeg"
DEFAULT_HTML = "html"
NTERACT = "nteract"
JUPYTER_PRESENTATIONS = [SVG, PNG, JPEG, DEFAULT_HTML, NTERACT]
ENVIRONMENT_PLUGIN_TYPE = "pyecharts_environment"
JS_EXTENSION_PLUGIN_TYPE = "pyecharts_js_extension"
GEO_DATA_PLUGIN_TYPE = "pyecharts_geo_data_bank"

# themes
LIGHT_THEME = "light"
DARK_THEME = "dark"
VINTAGE_THEME = "vintage"
MACARONS_THEME = "macarons"
INFOGRAPHIC_THEME = "infographic"
SHINE_THEME = "shine"
ROMA_THEME = "roma"

EXTERNAL_THEMES = [
    VINTAGE_THEME, MACARONS_THEME, INFOGRAPHIC_THEME, SHINE_THEME, ROMA_THEME
]
BUILTIN_THEMES = [LIGHT_THEME, DARK_THEME]
ALL_THEMES = EXTERNAL_THEMES + BUILTIN_THEMES

ERROR_MESSAGE = "You need python 3.5+ and pyecharts-javascripthon"

SYMBOL = {
    "plane": "path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208."
    "063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0."
    "305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221."
    "799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0."
    "531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134"
    ".449-92.931l12.238-241.308L1705.06,1318.313z"
}
