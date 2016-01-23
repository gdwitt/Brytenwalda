from . import interactions
from . import trade
from . import initialize_trade_routes

dialogs = interactions.dialogs

simple_triggers = trade.simple_triggers + interactions.simple_triggers
scripts = trade.scripts + interactions.scripts + initialize_trade_routes.scripts
triggers = interactions.triggers
