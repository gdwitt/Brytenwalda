from . import interactions
from . import trade

dialogs = interactions.dialogs

simple_triggers = trade.simple_triggers + interactions.simple_triggers
scripts = trade.scripts + interactions.scripts
triggers = interactions.triggers
