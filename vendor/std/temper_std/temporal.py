from temper_std.json import JsonAdapter, JsonProducer, JsonSyntaxTree, InterchangeContext, JsonString
from datetime import date as date62
from temper_core import cast_by_type as cast_by_type51, date_to_string as date_to_string58, date_from_iso_string as date_from_iso_string59, arith_int_mod as arith_int_mod60, int_to_string as int_to_string5, string_get as string_get21, string_next as string_next23, int_sub as int_sub0, string_count_between as string_count_between61
from typing import Sequence as Sequence45
from builtins import int as int42, bool as bool41, list as list14, str as str36, len as len1
from temper_std.json import JsonAdapter, JsonString
_date_to_string_1365 = date_to_string58
_date_from_iso_string_1366 = date_from_iso_string59
_arith_int_mod_1367 = arith_int_mod60
_int_to_string_1368 = int_to_string5
_len_1369 = len1
_string_get_1371 = string_get21
_string_next_1373 = string_next23
_int_sub_1374 = int_sub0
_string_count_between_1375 = string_count_between61
class _DateJsonAdapter(JsonAdapter['date62']):
    __slots__ = ()
    def encode_to_json(this_120, x_116: 'date62', p_117: 'JsonProducer', /) -> 'None':
        _encode_to_json(x_116, p_117)
    def decode_from_json(this_121, t_118: 'JsonSyntaxTree', ic_119: 'InterchangeContext', /) -> 'date62':
        return _decode_from_json(t_118, ic_119)
    def __init__(this, /) -> None:
        pass
# Type `std/temporal/`.Date connected to datetime.date
def _encode_to_json(this_12: 'date62', p_91: 'JsonProducer', /) -> 'None':
    p_91.string_value(_date_to_string_1365(this_12))
def _decode_from_json(t_94: 'JsonSyntaxTree', ic_95: 'InterchangeContext', /) -> 'date62':
    t_131: 'JsonString' = cast_by_type51(t_94, JsonString)
    return _date_from_iso_string_1366(t_131.content)
def _json_adapter() -> 'JsonAdapter[date62]':
    return _DateJsonAdapter()
_days_in_month: 'Sequence45[int42]' = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
def _is_leap_year(year_41: 'int42', /) -> 'bool41':
    if _arith_int_mod_1367(year_41, 4) == 0:
        if not _arith_int_mod_1367(year_41, 100) == 0:
            return True
        else:
            return _arith_int_mod_1367(year_41, 400) == 0
    else:
        return False
def _pad_to(min_width_43: 'int42', num_44: 'int42', sb_45: 'list14[str36]', /) -> 'None':
    "If the decimal representation of \\|num\\| is longer than [minWidth],\nthen appends that representation.\nOtherwise any sign for [num] followed by enough zeroes to bring the\nwhole length up to [minWidth].\n\n```temper\n// When the width is greater than the decimal's length,\n// we pad to that width.\n\"0123\" == do {\n  let sb = new StringBuilder();\n  padTo(4, 123, sb);\n  sb.toString()\n}\n\n// When the width is the same or lesser, we just use the string form.\n\"123\" == do {\n  let sb = new StringBuilder();\n  padTo(2, 123, sb);\n  sb.toString()\n}\n\n// The sign is always on the left.\n\"-01\" == do {\n  let sb = new StringBuilder();\n  padTo(3, -1, sb);\n  sb.toString()\n}\n```\n\nminWidth__43: Int32\n\nnum__44: Int32\n\nsb__45: builtins.list<String>\n"
    decimal_47: 'str36' = _int_to_string_1368(num_44, 10)
    decimal_index_48: 'int42' = 0
    decimal_end_49: 'int42' = _len_1369(decimal_47)
    t_148: 'bool41'
    if decimal_index_48 < decimal_end_49:
        t_148 = _string_get_1371(decimal_47, decimal_index_48) == 45
    else:
        t_148 = False
    if t_148:
        sb_45.append('-')
        decimal_index_48 = _string_next_1373(decimal_47, decimal_index_48)
    n_needed_50: 'int42' = _int_sub_1374(min_width_43, _string_count_between_1375(decimal_47, decimal_index_48, decimal_end_49))
    while n_needed_50 > 0:
        sb_45.append('0')
        n_needed_50 = _int_sub_1374(n_needed_50, 1)
    sb_45.append(decimal_47[decimal_index_48 : decimal_end_49])
_day_of_week_lookup_table_leapy: 'Sequence45[int42]' = (0, 0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6)
_day_of_week_lookup_table_not_leapy: 'Sequence45[int42]' = (0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5)
