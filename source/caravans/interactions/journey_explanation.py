from source.header_operations import *
from source.header_common import s11, s12, s14, s15

from source.header_dialogs import anyone

from source.module_constants import trade_goods_begin, trade_goods_end


dialogs = [
    [anyone, "merchant_trip_explanation", [
        (party_get_slot, ":origin", "$g_encountered_party", "slot_party_last_traded_center"),
        (party_get_slot, ":destination", "$g_encountered_party", "slot_party_ai_object"),
        (str_store_party_name, s11, ":origin"),
        (str_store_party_name, s12, ":destination"),

        (str_store_string, s14, "str___we_believe_that_there_is_money_to_be_made_selling_"),
        (store_sub, ":item_to_price_slot", "slot_town_trade_good_prices_begin", trade_goods_begin),

        (assign, ":at_least_one_item_found", 0),
        (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
            (party_get_slot, ":origin_price", ":origin", ":cur_goods_price_slot"),
            (party_get_slot, ":destination_price", ":destination", ":cur_goods_price_slot"),

            (gt, ":destination_price", ":origin_price"),
            (store_sub, ":price_dif", ":destination_price", ":origin_price"),

            (gt, ":price_dif", 200),
            (str_store_item_name, s15, ":cur_goods"),
            (str_store_string, s14, "str_s14s15_"),

            (assign, ":at_least_one_item_found", 1),
        (try_end),

        (try_begin),
            (eq, ":at_least_one_item_found", 0),
            (str_store_string, s14, "str__we_carry_a_selection_of_goods_although_the_difference_in_prices_for_each_is_not_so_great_we_hope_to_make_a_profit_off_of_the_whole"),
        (else_try),
            (str_store_string, s14, "str_s14and_other_goods"),
        (try_end),

        ], "We are coming from {s11} and heading to {s12}.{s14}", "merchant_pretalk",
     []],
]
