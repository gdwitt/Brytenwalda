####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference.
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################
import logging

import source.module_game_menus as m_menus

from . import GenericEntity


class Menu(GenericEntity):
    tag = 'menu'
    raw_objects = m_menus.game_menus

    def __init__(self, index, id, flags, text, mesh_name, block, menu_options):
        super(Menu, self).__init__(index, id)
        self._flags = flags
        self._text = text
        if mesh_name is not 'none':
            logging.warning('Menu "%s" mesh_name is not "none".' % self._id)
        self._mesh_name = 'none'
        self._block = block
        self._menu_options = menu_options

    def export(self, compiler):
        result = "%s %d %s %s" % (self._id, self._flags, self._text.replace(" ", "_"), self._mesh_name)
        result += compiler.process_statement_block(0, 1, self._block)
        result += "%d\n" % len(self._menu_options)
        for menu_item in self._menu_options:
            result += " mno_%s " % menu_item[0]
            result += compiler.process_statement_block(0, 1, menu_item[1])
            result += " %s " % menu_item[2].replace(" ", "_")
            result += compiler.process_statement_block(0, 1, menu_item[3])
            door_name = "."
            if len(menu_item) > 4:
                door_name = menu_item[4]
            result += " %s " % door_name.replace(" ", "_")
        result += '\n'
        return result

    @property
    def statement_blocks(self):
        s = [self._block]
        for x in self._menu_options:
            s.append(x[1])
            s.append(x[3])
        return s
