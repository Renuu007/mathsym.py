# This file aggregates all symbol maps from the 'mappings' directory.

from .BasicSymbols import SYMBOL_MAP as basic_map
from .AlgebraSymbols import SYMBOL_MAP as algebra_map
from .Calculus_AnalysisSymbols import SYMBOL_MAP as calculus_map
from .GeometrySymbols import SYMBOL_MAP as geometry_map
from .GreekSymbols import SYMBOL_MAP as greek_map
from .LogicSymbols import SYMBOL_MAP as logic_map
from .NumberSymbols import SYMBOL_MAP as number_map
from .SetTheorySymbols import SYMBOL_MAP as set_map
from .StatisticalSymbols import SYMBOL_MAP as stats_map


MASTER_SYMBOL_MAP = {}
MASTER_SYMBOL_MAP.update(basic_map)
MASTER_SYMBOL_MAP.update(algebra_map)
MASTER_SYMBOL_MAP.update(calculus_map)
MASTER_SYMBOL_MAP.update(geometry_map)
MASTER_SYMBOL_MAP.update(greek_map)
MASTER_SYMBOL_MAP.update(logic_map)
MASTER_SYMBOL_MAP.update(number_map)
MASTER_SYMBOL_MAP.update(set_map)
MASTER_SYMBOL_MAP.update(stats_map) 