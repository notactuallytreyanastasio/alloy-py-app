from builtins import str as str34, float as float36, RuntimeError as RuntimeError39, int as int40, bool as bool42, Exception as Exception46, len as len6, isinstance as isinstance47, list as list3, tuple as tuple5
from typing import Union as Union35, Sequence as Sequence38, Dict as Dict43, MutableSequence as MutableSequence45, Any as Any48, TypeVar as TypeVar49, Callable as Callable50
from abc import ABCMeta as ABCMeta37
from types import MappingProxyType as MappingProxyType41
from temper_core import Label as Label44, Pair as Pair32, string_from_code_point as string_from_code_point51, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, mapped_to_list as mapped_to_list13, list_get as list_get14, int_add as int_add15, float_gt as float_gt16, float64_to_string as float64_to_string17, float_lt as float_lt18, float_gt_eq as float_gt_eq19, float_lt_eq as float_lt_eq20, float_eq as float_eq21, require_string_index as require_string_index22, int_sub as int_sub23, string_next as string_next24, string_get as string_get25, date_from_iso_string as date_from_iso_string26, list_join as list_join27, list_builder_add_all as list_builder_add_all28, date_to_string as date_to_string29, string_for_each as string_for_each30, map_constructor as map_constructor31
from datetime import date as date33
map_builder_set_15563 = map_builder_set0
list_for_each_15564 = list_for_each1
mapped_to_map_15565 = mapped_to_map2
list_15566 = list3
mapped_has_15567 = mapped_has4
tuple_15569 = tuple5
len_15570 = len6
string_count_between_15571 = string_count_between7
str_cat_15572 = str_cat8
int_to_string_15573 = int_to_string9
string_to_int32_15574 = string_to_int3210
string_to_int64_15575 = string_to_int6411
string_to_float64_15576 = string_to_float6412
mapped_to_list_15577 = mapped_to_list13
list_get_15578 = list_get14
int_add_15579 = int_add15
float_gt_15580 = float_gt16
float64_to_string_15581 = float64_to_string17
float_lt_15582 = float_lt18
float_gt_eq_15583 = float_gt_eq19
float_lt_eq_15584 = float_lt_eq20
float_eq_15585 = float_eq21
require_string_index_15588 = require_string_index22
int_sub_15589 = int_sub23
string_next_15590 = string_next24
string_get_15592 = string_get25
date_from_iso_string_15593 = date_from_iso_string26
list_join_15594 = list_join27
list_builder_add_all_15595 = list_builder_add_all28
date_to_string_15599 = date_to_string29
string_for_each_15601 = string_for_each30
map_constructor_15602 = map_constructor31
pair_15603 = Pair32
date_15604 = date33
class ChangesetError:
    field_667: 'str34'
    message_668: 'str34'
    __slots__ = ('field_667', 'message_668')
    def __init__(this_371, field_670: 'str34', message_671: 'str34') -> None:
        this_371.field_667 = field_670
        this_371.message_668 = message_671
    @property
    def field(this_2052) -> 'str34':
        return this_2052.field_667
    @property
    def message(this_2055) -> 'str34':
        return this_2055.message_668
class NumberValidationOpts:
    greater_than_672: 'Union35[float36, None]'
    less_than_673: 'Union35[float36, None]'
    greater_than_or_equal_674: 'Union35[float36, None]'
    less_than_or_equal_675: 'Union35[float36, None]'
    equal_to_676: 'Union35[float36, None]'
    __slots__ = ('greater_than_672', 'less_than_673', 'greater_than_or_equal_674', 'less_than_or_equal_675', 'equal_to_676')
    def __init__(this_373, greater_than_678: 'Union35[float36, None]', less_than_679: 'Union35[float36, None]', greater_than_or_equal_680: 'Union35[float36, None]', less_than_or_equal_681: 'Union35[float36, None]', equal_to_682: 'Union35[float36, None]') -> None:
        this_373.greater_than_672 = greater_than_678
        this_373.less_than_673 = less_than_679
        this_373.greater_than_or_equal_674 = greater_than_or_equal_680
        this_373.less_than_or_equal_675 = less_than_or_equal_681
        this_373.equal_to_676 = equal_to_682
    @property
    def greater_than(this_2058) -> 'Union35[float36, None]':
        return this_2058.greater_than_672
    @property
    def less_than(this_2061) -> 'Union35[float36, None]':
        return this_2061.less_than_673
    @property
    def greater_than_or_equal(this_2064) -> 'Union35[float36, None]':
        return this_2064.greater_than_or_equal_674
    @property
    def less_than_or_equal(this_2067) -> 'Union35[float36, None]':
        return this_2067.less_than_or_equal_675
    @property
    def equal_to(this_2070) -> 'Union35[float36, None]':
        return this_2070.equal_to_676
class Changeset(metaclass = ABCMeta37):
    def cast(this_229, allowed_fields_692: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError39()
    def validate_required(this_230, fields_695: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError39()
    def validate_length(this_231, field_698: 'SafeIdentifier', min_699: 'int40', max_700: 'int40') -> 'Changeset':
        raise RuntimeError39()
    def validate_int(this_232, field_703: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_int64(this_233, field_706: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_float(this_234, field_709: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_bool(this_235, field_712: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def put_change(this_236, field_715: 'SafeIdentifier', value_716: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def get_change(this_237, field_719: 'SafeIdentifier') -> 'str34':
        raise RuntimeError39()
    def delete_change(this_238, field_722: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_inclusion(this_239, field_725: 'SafeIdentifier', allowed_726: 'Sequence38[str34]') -> 'Changeset':
        raise RuntimeError39()
    def validate_exclusion(this_240, field_729: 'SafeIdentifier', disallowed_730: 'Sequence38[str34]') -> 'Changeset':
        raise RuntimeError39()
    def validate_number(this_241, field_733: 'SafeIdentifier', opts_734: 'NumberValidationOpts') -> 'Changeset':
        raise RuntimeError39()
    def validate_acceptance(this_242, field_737: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_confirmation(this_243, field_740: 'SafeIdentifier', confirmation_field_741: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_contains(this_244, field_744: 'SafeIdentifier', substring_745: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def validate_starts_with(this_245, field_748: 'SafeIdentifier', prefix_749: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def validate_ends_with(this_246, field_752: 'SafeIdentifier', suffix_753: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def to_insert_sql(this_247) -> 'SqlFragment':
        raise RuntimeError39()
    def to_update_sql(this_248, id_758: 'int40') -> 'SqlFragment':
        raise RuntimeError39()
class ChangesetImpl_249(Changeset):
    table_def_760: 'TableDef'
    params_761: 'MappingProxyType41[str34, str34]'
    changes_762: 'MappingProxyType41[str34, str34]'
    errors_763: 'Sequence38[ChangesetError]'
    is_valid_764: 'bool42'
    __slots__ = ('table_def_760', 'params_761', 'changes_762', 'errors_763', 'is_valid_764')
    @property
    def table_def(this_250) -> 'TableDef':
        return this_250.table_def_760
    @property
    def changes(this_251) -> 'MappingProxyType41[str34, str34]':
        return this_251.changes_762
    @property
    def errors(this_252) -> 'Sequence38[ChangesetError]':
        return this_252.errors_763
    @property
    def is_valid(this_253) -> 'bool42':
        return this_253.is_valid_764
    def cast(this_254, allowed_fields_774: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        mb_776: 'Dict43[str34, str34]' = {}
        def fn_15462(f_777: 'SafeIdentifier') -> 'None':
            t_15460: 'str34'
            t_15457: 'str34' = f_777.sql_value
            val_778: 'str34' = this_254.params_761.get(t_15457, '')
            if not (not val_778):
                t_15460 = f_777.sql_value
                map_builder_set_15563(mb_776, t_15460, val_778)
        list_for_each_15564(allowed_fields_774, fn_15462)
        return ChangesetImpl_249(this_254.table_def_760, this_254.params_761, mapped_to_map_15565(mb_776), this_254.errors_763, this_254.is_valid_764)
    def validate_required(this_255, fields_780: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        return_422: 'Changeset'
        t_15455: 'Sequence38[ChangesetError]'
        t_8795: 'TableDef'
        t_8796: 'MappingProxyType41[str34, str34]'
        t_8797: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_781:
            if not this_255.is_valid_764:
                return_422 = this_255
                fn_781.break_()
            eb_782: 'MutableSequence45[ChangesetError]' = list_15566(this_255.errors_763)
            valid_783: 'bool42' = True
            def fn_15451(f_784: 'SafeIdentifier') -> 'None':
                nonlocal valid_783
                t_15449: 'ChangesetError'
                t_15446: 'str34' = f_784.sql_value
                if not mapped_has_15567(this_255.changes_762, t_15446):
                    t_15449 = ChangesetError(f_784.sql_value, 'is required')
                    eb_782.append(t_15449)
                    valid_783 = False
            list_for_each_15564(fields_780, fn_15451)
            t_8795 = this_255.table_def_760
            t_8796 = this_255.params_761
            t_8797 = this_255.changes_762
            t_15455 = tuple_15569(eb_782)
            return_422 = ChangesetImpl_249(t_8795, t_8796, t_8797, t_15455, valid_783)
        return return_422
    def validate_length(this_256, field_786: 'SafeIdentifier', min_787: 'int40', max_788: 'int40') -> 'Changeset':
        return_423: 'Changeset'
        t_15433: 'str34'
        t_15444: 'Sequence38[ChangesetError]'
        t_8778: 'bool42'
        t_8784: 'TableDef'
        t_8785: 'MappingProxyType41[str34, str34]'
        t_8786: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_789:
            if not this_256.is_valid_764:
                return_423 = this_256
                fn_789.break_()
            t_15433 = field_786.sql_value
            val_790: 'str34' = this_256.changes_762.get(t_15433, '')
            len_791: 'int40' = string_count_between_15571(val_790, 0, len_15570(val_790))
            if len_791 < min_787:
                t_8778 = True
            else:
                t_8778 = len_791 > max_788
            if t_8778:
                msg_792: 'str34' = str_cat_15572('must be between ', int_to_string_15573(min_787), ' and ', int_to_string_15573(max_788), ' characters')
                eb_793: 'MutableSequence45[ChangesetError]' = list_15566(this_256.errors_763)
                eb_793.append(ChangesetError(field_786.sql_value, msg_792))
                t_8784 = this_256.table_def_760
                t_8785 = this_256.params_761
                t_8786 = this_256.changes_762
                t_15444 = tuple_15569(eb_793)
                return_423 = ChangesetImpl_249(t_8784, t_8785, t_8786, t_15444, False)
                fn_789.break_()
            return_423 = this_256
        return return_423
    def validate_int(this_257, field_795: 'SafeIdentifier') -> 'Changeset':
        return_424: 'Changeset'
        t_15424: 'str34'
        t_15431: 'Sequence38[ChangesetError]'
        t_8769: 'TableDef'
        t_8770: 'MappingProxyType41[str34, str34]'
        t_8771: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_796:
            if not this_257.is_valid_764:
                return_424 = this_257
                fn_796.break_()
            t_15424 = field_795.sql_value
            val_797: 'str34' = this_257.changes_762.get(t_15424, '')
            if not val_797:
                return_424 = this_257
                fn_796.break_()
            parse_ok_798: 'bool42'
            try:
                string_to_int32_15574(val_797)
                parse_ok_798 = True
            except Exception46:
                parse_ok_798 = False
            if not parse_ok_798:
                eb_799: 'MutableSequence45[ChangesetError]' = list_15566(this_257.errors_763)
                eb_799.append(ChangesetError(field_795.sql_value, 'must be an integer'))
                t_8769 = this_257.table_def_760
                t_8770 = this_257.params_761
                t_8771 = this_257.changes_762
                t_15431 = tuple_15569(eb_799)
                return_424 = ChangesetImpl_249(t_8769, t_8770, t_8771, t_15431, False)
                fn_796.break_()
            return_424 = this_257
        return return_424
    def validate_int64(this_258, field_801: 'SafeIdentifier') -> 'Changeset':
        return_425: 'Changeset'
        t_15415: 'str34'
        t_15422: 'Sequence38[ChangesetError]'
        t_8756: 'TableDef'
        t_8757: 'MappingProxyType41[str34, str34]'
        t_8758: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_802:
            if not this_258.is_valid_764:
                return_425 = this_258
                fn_802.break_()
            t_15415 = field_801.sql_value
            val_803: 'str34' = this_258.changes_762.get(t_15415, '')
            if not val_803:
                return_425 = this_258
                fn_802.break_()
            parse_ok_804: 'bool42'
            try:
                string_to_int64_15575(val_803)
                parse_ok_804 = True
            except Exception46:
                parse_ok_804 = False
            if not parse_ok_804:
                eb_805: 'MutableSequence45[ChangesetError]' = list_15566(this_258.errors_763)
                eb_805.append(ChangesetError(field_801.sql_value, 'must be a 64-bit integer'))
                t_8756 = this_258.table_def_760
                t_8757 = this_258.params_761
                t_8758 = this_258.changes_762
                t_15422 = tuple_15569(eb_805)
                return_425 = ChangesetImpl_249(t_8756, t_8757, t_8758, t_15422, False)
                fn_802.break_()
            return_425 = this_258
        return return_425
    def validate_float(this_259, field_807: 'SafeIdentifier') -> 'Changeset':
        return_426: 'Changeset'
        t_15406: 'str34'
        t_15413: 'Sequence38[ChangesetError]'
        t_8743: 'TableDef'
        t_8744: 'MappingProxyType41[str34, str34]'
        t_8745: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_808:
            if not this_259.is_valid_764:
                return_426 = this_259
                fn_808.break_()
            t_15406 = field_807.sql_value
            val_809: 'str34' = this_259.changes_762.get(t_15406, '')
            if not val_809:
                return_426 = this_259
                fn_808.break_()
            parse_ok_810: 'bool42'
            try:
                string_to_float64_15576(val_809)
                parse_ok_810 = True
            except Exception46:
                parse_ok_810 = False
            if not parse_ok_810:
                eb_811: 'MutableSequence45[ChangesetError]' = list_15566(this_259.errors_763)
                eb_811.append(ChangesetError(field_807.sql_value, 'must be a number'))
                t_8743 = this_259.table_def_760
                t_8744 = this_259.params_761
                t_8745 = this_259.changes_762
                t_15413 = tuple_15569(eb_811)
                return_426 = ChangesetImpl_249(t_8743, t_8744, t_8745, t_15413, False)
                fn_808.break_()
            return_426 = this_259
        return return_426
    def validate_bool(this_260, field_813: 'SafeIdentifier') -> 'Changeset':
        return_427: 'Changeset'
        t_15397: 'str34'
        t_15404: 'Sequence38[ChangesetError]'
        t_8718: 'bool42'
        t_8719: 'bool42'
        t_8721: 'bool42'
        t_8722: 'bool42'
        t_8724: 'bool42'
        t_8730: 'TableDef'
        t_8731: 'MappingProxyType41[str34, str34]'
        t_8732: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_814:
            if not this_260.is_valid_764:
                return_427 = this_260
                fn_814.break_()
            t_15397 = field_813.sql_value
            val_815: 'str34' = this_260.changes_762.get(t_15397, '')
            if not val_815:
                return_427 = this_260
                fn_814.break_()
            is_true_816: 'bool42'
            if val_815 == 'true':
                is_true_816 = True
            else:
                if val_815 == '1':
                    t_8719 = True
                else:
                    if val_815 == 'yes':
                        t_8718 = True
                    else:
                        t_8718 = val_815 == 'on'
                    t_8719 = t_8718
                is_true_816 = t_8719
            is_false_817: 'bool42'
            if val_815 == 'false':
                is_false_817 = True
            else:
                if val_815 == '0':
                    t_8722 = True
                else:
                    if val_815 == 'no':
                        t_8721 = True
                    else:
                        t_8721 = val_815 == 'off'
                    t_8722 = t_8721
                is_false_817 = t_8722
            if not is_true_816:
                t_8724 = not is_false_817
            else:
                t_8724 = False
            if t_8724:
                eb_818: 'MutableSequence45[ChangesetError]' = list_15566(this_260.errors_763)
                eb_818.append(ChangesetError(field_813.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_8730 = this_260.table_def_760
                t_8731 = this_260.params_761
                t_8732 = this_260.changes_762
                t_15404 = tuple_15569(eb_818)
                return_427 = ChangesetImpl_249(t_8730, t_8731, t_8732, t_15404, False)
                fn_814.break_()
            return_427 = this_260
        return return_427
    def put_change(this_261, field_820: 'SafeIdentifier', value_821: 'str34') -> 'Changeset':
        t_15385: 'int40'
        mb_823: 'Dict43[str34, str34]' = {}
        pairs_824: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_15577(this_261.changes_762)
        i_825: 'int40' = 0
        while True:
            t_15385 = len_15570(pairs_824)
            if not i_825 < t_15385:
                break
            map_builder_set_15563(mb_823, list_get_15578(pairs_824, i_825).key, list_get_15578(pairs_824, i_825).value)
            i_825 = int_add_15579(i_825, 1)
        map_builder_set_15563(mb_823, field_820.sql_value, value_821)
        return ChangesetImpl_249(this_261.table_def_760, this_261.params_761, mapped_to_map_15565(mb_823), this_261.errors_763, this_261.is_valid_764)
    def get_change(this_262, field_827: 'SafeIdentifier') -> 'str34':
        t_15379: 'str34' = field_827.sql_value
        if not mapped_has_15567(this_262.changes_762, t_15379):
            raise RuntimeError39()
        t_15381: 'str34' = field_827.sql_value
        return this_262.changes_762.get(t_15381, '')
    def delete_change(this_263, field_830: 'SafeIdentifier') -> 'Changeset':
        t_15366: 'int40'
        mb_832: 'Dict43[str34, str34]' = {}
        pairs_833: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_15577(this_263.changes_762)
        i_834: 'int40' = 0
        while True:
            t_15366 = len_15570(pairs_833)
            if not i_834 < t_15366:
                break
            if list_get_15578(pairs_833, i_834).key != field_830.sql_value:
                map_builder_set_15563(mb_832, list_get_15578(pairs_833, i_834).key, list_get_15578(pairs_833, i_834).value)
            i_834 = int_add_15579(i_834, 1)
        return ChangesetImpl_249(this_263.table_def_760, this_263.params_761, mapped_to_map_15565(mb_832), this_263.errors_763, this_263.is_valid_764)
    def validate_inclusion(this_264, field_836: 'SafeIdentifier', allowed_837: 'Sequence38[str34]') -> 'Changeset':
        return_431: 'Changeset'
        t_15352: 'str34'
        t_15354: 'str34'
        t_15362: 'Sequence38[ChangesetError]'
        t_8680: 'TableDef'
        t_8681: 'MappingProxyType41[str34, str34]'
        t_8682: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_838:
            if not this_264.is_valid_764:
                return_431 = this_264
                fn_838.break_()
            t_15352 = field_836.sql_value
            if not mapped_has_15567(this_264.changes_762, t_15352):
                return_431 = this_264
                fn_838.break_()
            t_15354 = field_836.sql_value
            val_839: 'str34' = this_264.changes_762.get(t_15354, '')
            found_840: 'bool42' = False
            def fn_15351(a_841: 'str34') -> 'None':
                nonlocal found_840
                if a_841 == val_839:
                    found_840 = True
            list_for_each_15564(allowed_837, fn_15351)
            if not found_840:
                eb_842: 'MutableSequence45[ChangesetError]' = list_15566(this_264.errors_763)
                eb_842.append(ChangesetError(field_836.sql_value, 'is not included in the list'))
                t_8680 = this_264.table_def_760
                t_8681 = this_264.params_761
                t_8682 = this_264.changes_762
                t_15362 = tuple_15569(eb_842)
                return_431 = ChangesetImpl_249(t_8680, t_8681, t_8682, t_15362, False)
                fn_838.break_()
            return_431 = this_264
        return return_431
    def validate_exclusion(this_265, field_844: 'SafeIdentifier', disallowed_845: 'Sequence38[str34]') -> 'Changeset':
        return_432: 'Changeset'
        t_15339: 'str34'
        t_15341: 'str34'
        t_15349: 'Sequence38[ChangesetError]'
        t_8666: 'TableDef'
        t_8667: 'MappingProxyType41[str34, str34]'
        t_8668: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_846:
            if not this_265.is_valid_764:
                return_432 = this_265
                fn_846.break_()
            t_15339 = field_844.sql_value
            if not mapped_has_15567(this_265.changes_762, t_15339):
                return_432 = this_265
                fn_846.break_()
            t_15341 = field_844.sql_value
            val_847: 'str34' = this_265.changes_762.get(t_15341, '')
            found_848: 'bool42' = False
            def fn_15338(d_849: 'str34') -> 'None':
                nonlocal found_848
                if d_849 == val_847:
                    found_848 = True
            list_for_each_15564(disallowed_845, fn_15338)
            if found_848:
                eb_850: 'MutableSequence45[ChangesetError]' = list_15566(this_265.errors_763)
                eb_850.append(ChangesetError(field_844.sql_value, 'is reserved'))
                t_8666 = this_265.table_def_760
                t_8667 = this_265.params_761
                t_8668 = this_265.changes_762
                t_15349 = tuple_15569(eb_850)
                return_432 = ChangesetImpl_249(t_8666, t_8667, t_8668, t_15349, False)
                fn_846.break_()
            return_432 = this_265
        return return_432
    def validate_number(this_266, field_852: 'SafeIdentifier', opts_853: 'NumberValidationOpts') -> 'Changeset':
        return_433: 'Changeset'
        t_15288: 'str34'
        t_15290: 'str34'
        t_15296: 'Sequence38[ChangesetError]'
        t_15304: 'Sequence38[ChangesetError]'
        t_15312: 'Sequence38[ChangesetError]'
        t_15320: 'Sequence38[ChangesetError]'
        t_15328: 'Sequence38[ChangesetError]'
        t_15336: 'Sequence38[ChangesetError]'
        t_8599: 'TableDef'
        t_8600: 'MappingProxyType41[str34, str34]'
        t_8601: 'MappingProxyType41[str34, str34]'
        t_8603: 'float36'
        t_8612: 'TableDef'
        t_8613: 'MappingProxyType41[str34, str34]'
        t_8614: 'MappingProxyType41[str34, str34]'
        t_8622: 'TableDef'
        t_8623: 'MappingProxyType41[str34, str34]'
        t_8624: 'MappingProxyType41[str34, str34]'
        t_8632: 'TableDef'
        t_8633: 'MappingProxyType41[str34, str34]'
        t_8634: 'MappingProxyType41[str34, str34]'
        t_8642: 'TableDef'
        t_8643: 'MappingProxyType41[str34, str34]'
        t_8644: 'MappingProxyType41[str34, str34]'
        t_8652: 'TableDef'
        t_8653: 'MappingProxyType41[str34, str34]'
        t_8654: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_854:
            if not this_266.is_valid_764:
                return_433 = this_266
                fn_854.break_()
            t_15288 = field_852.sql_value
            if not mapped_has_15567(this_266.changes_762, t_15288):
                return_433 = this_266
                fn_854.break_()
            t_15290 = field_852.sql_value
            val_855: 'str34' = this_266.changes_762.get(t_15290, '')
            parse_ok_856: 'bool42'
            try:
                string_to_float64_15576(val_855)
                parse_ok_856 = True
            except Exception46:
                parse_ok_856 = False
            if not parse_ok_856:
                eb_857: 'MutableSequence45[ChangesetError]' = list_15566(this_266.errors_763)
                eb_857.append(ChangesetError(field_852.sql_value, 'must be a number'))
                t_8599 = this_266.table_def_760
                t_8600 = this_266.params_761
                t_8601 = this_266.changes_762
                t_15296 = tuple_15569(eb_857)
                return_433 = ChangesetImpl_249(t_8599, t_8600, t_8601, t_15296, False)
                fn_854.break_()
            num_858: 'float36'
            try:
                t_8603 = string_to_float64_15576(val_855)
                num_858 = t_8603
            except Exception46:
                num_858 = 0.0
            gt_859: 'Union35[float36, None]' = opts_853.greater_than
            if not gt_859 is None:
                gt_2610: 'float36' = gt_859
                if not float_gt_15580(num_858, gt_2610):
                    eb_860: 'MutableSequence45[ChangesetError]' = list_15566(this_266.errors_763)
                    eb_860.append(ChangesetError(field_852.sql_value, str_cat_15572('must be greater than ', float64_to_string_15581(gt_2610))))
                    t_8612 = this_266.table_def_760
                    t_8613 = this_266.params_761
                    t_8614 = this_266.changes_762
                    t_15304 = tuple_15569(eb_860)
                    return_433 = ChangesetImpl_249(t_8612, t_8613, t_8614, t_15304, False)
                    fn_854.break_()
            lt_861: 'Union35[float36, None]' = opts_853.less_than
            if not lt_861 is None:
                lt_2611: 'float36' = lt_861
                if not float_lt_15582(num_858, lt_2611):
                    eb_862: 'MutableSequence45[ChangesetError]' = list_15566(this_266.errors_763)
                    eb_862.append(ChangesetError(field_852.sql_value, str_cat_15572('must be less than ', float64_to_string_15581(lt_2611))))
                    t_8622 = this_266.table_def_760
                    t_8623 = this_266.params_761
                    t_8624 = this_266.changes_762
                    t_15312 = tuple_15569(eb_862)
                    return_433 = ChangesetImpl_249(t_8622, t_8623, t_8624, t_15312, False)
                    fn_854.break_()
            gte_863: 'Union35[float36, None]' = opts_853.greater_than_or_equal
            if not gte_863 is None:
                gte_2612: 'float36' = gte_863
                if not float_gt_eq_15583(num_858, gte_2612):
                    eb_864: 'MutableSequence45[ChangesetError]' = list_15566(this_266.errors_763)
                    eb_864.append(ChangesetError(field_852.sql_value, str_cat_15572('must be greater than or equal to ', float64_to_string_15581(gte_2612))))
                    t_8632 = this_266.table_def_760
                    t_8633 = this_266.params_761
                    t_8634 = this_266.changes_762
                    t_15320 = tuple_15569(eb_864)
                    return_433 = ChangesetImpl_249(t_8632, t_8633, t_8634, t_15320, False)
                    fn_854.break_()
            lte_865: 'Union35[float36, None]' = opts_853.less_than_or_equal
            if not lte_865 is None:
                lte_2613: 'float36' = lte_865
                if not float_lt_eq_15584(num_858, lte_2613):
                    eb_866: 'MutableSequence45[ChangesetError]' = list_15566(this_266.errors_763)
                    eb_866.append(ChangesetError(field_852.sql_value, str_cat_15572('must be less than or equal to ', float64_to_string_15581(lte_2613))))
                    t_8642 = this_266.table_def_760
                    t_8643 = this_266.params_761
                    t_8644 = this_266.changes_762
                    t_15328 = tuple_15569(eb_866)
                    return_433 = ChangesetImpl_249(t_8642, t_8643, t_8644, t_15328, False)
                    fn_854.break_()
            eq_867: 'Union35[float36, None]' = opts_853.equal_to
            if not eq_867 is None:
                eq_2614: 'float36' = eq_867
                if not float_eq_15585(num_858, eq_2614):
                    eb_868: 'MutableSequence45[ChangesetError]' = list_15566(this_266.errors_763)
                    eb_868.append(ChangesetError(field_852.sql_value, str_cat_15572('must be equal to ', float64_to_string_15581(eq_2614))))
                    t_8652 = this_266.table_def_760
                    t_8653 = this_266.params_761
                    t_8654 = this_266.changes_762
                    t_15336 = tuple_15569(eb_868)
                    return_433 = ChangesetImpl_249(t_8652, t_8653, t_8654, t_15336, False)
                    fn_854.break_()
            return_433 = this_266
        return return_433
    def validate_acceptance(this_267, field_870: 'SafeIdentifier') -> 'Changeset':
        return_434: 'Changeset'
        t_15278: 'str34'
        t_15280: 'str34'
        t_15286: 'Sequence38[ChangesetError]'
        t_8577: 'bool42'
        t_8578: 'bool42'
        t_8585: 'TableDef'
        t_8586: 'MappingProxyType41[str34, str34]'
        t_8587: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_871:
            if not this_267.is_valid_764:
                return_434 = this_267
                fn_871.break_()
            t_15278 = field_870.sql_value
            if not mapped_has_15567(this_267.changes_762, t_15278):
                return_434 = this_267
                fn_871.break_()
            t_15280 = field_870.sql_value
            val_872: 'str34' = this_267.changes_762.get(t_15280, '')
            accepted_873: 'bool42'
            if val_872 == 'true':
                accepted_873 = True
            else:
                if val_872 == '1':
                    t_8578 = True
                else:
                    if val_872 == 'yes':
                        t_8577 = True
                    else:
                        t_8577 = val_872 == 'on'
                    t_8578 = t_8577
                accepted_873 = t_8578
            if not accepted_873:
                eb_874: 'MutableSequence45[ChangesetError]' = list_15566(this_267.errors_763)
                eb_874.append(ChangesetError(field_870.sql_value, 'must be accepted'))
                t_8585 = this_267.table_def_760
                t_8586 = this_267.params_761
                t_8587 = this_267.changes_762
                t_15286 = tuple_15569(eb_874)
                return_434 = ChangesetImpl_249(t_8585, t_8586, t_8587, t_15286, False)
                fn_871.break_()
            return_434 = this_267
        return return_434
    def validate_confirmation(this_268, field_876: 'SafeIdentifier', confirmation_field_877: 'SafeIdentifier') -> 'Changeset':
        return_435: 'Changeset'
        t_15266: 'str34'
        t_15268: 'str34'
        t_15270: 'str34'
        t_15276: 'Sequence38[ChangesetError]'
        t_8569: 'TableDef'
        t_8570: 'MappingProxyType41[str34, str34]'
        t_8571: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_878:
            if not this_268.is_valid_764:
                return_435 = this_268
                fn_878.break_()
            t_15266 = field_876.sql_value
            if not mapped_has_15567(this_268.changes_762, t_15266):
                return_435 = this_268
                fn_878.break_()
            t_15268 = field_876.sql_value
            val_879: 'str34' = this_268.changes_762.get(t_15268, '')
            t_15270 = confirmation_field_877.sql_value
            conf_880: 'str34' = this_268.changes_762.get(t_15270, '')
            if val_879 != conf_880:
                eb_881: 'MutableSequence45[ChangesetError]' = list_15566(this_268.errors_763)
                eb_881.append(ChangesetError(confirmation_field_877.sql_value, 'does not match'))
                t_8569 = this_268.table_def_760
                t_8570 = this_268.params_761
                t_8571 = this_268.changes_762
                t_15276 = tuple_15569(eb_881)
                return_435 = ChangesetImpl_249(t_8569, t_8570, t_8571, t_15276, False)
                fn_878.break_()
            return_435 = this_268
        return return_435
    def validate_contains(this_269, field_883: 'SafeIdentifier', substring_884: 'str34') -> 'Changeset':
        return_436: 'Changeset'
        t_15254: 'str34'
        t_15256: 'str34'
        t_15264: 'Sequence38[ChangesetError]'
        t_8554: 'TableDef'
        t_8555: 'MappingProxyType41[str34, str34]'
        t_8556: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_885:
            if not this_269.is_valid_764:
                return_436 = this_269
                fn_885.break_()
            t_15254 = field_883.sql_value
            if not mapped_has_15567(this_269.changes_762, t_15254):
                return_436 = this_269
                fn_885.break_()
            t_15256 = field_883.sql_value
            val_886: 'str34' = this_269.changes_762.get(t_15256, '')
            if not val_886.find(substring_884) >= 0:
                eb_887: 'MutableSequence45[ChangesetError]' = list_15566(this_269.errors_763)
                eb_887.append(ChangesetError(field_883.sql_value, 'must contain the given substring'))
                t_8554 = this_269.table_def_760
                t_8555 = this_269.params_761
                t_8556 = this_269.changes_762
                t_15264 = tuple_15569(eb_887)
                return_436 = ChangesetImpl_249(t_8554, t_8555, t_8556, t_15264, False)
                fn_885.break_()
            return_436 = this_269
        return return_436
    def validate_starts_with(this_270, field_889: 'SafeIdentifier', prefix_890: 'str34') -> 'Changeset':
        return_437: 'Changeset'
        t_15241: 'str34'
        t_15243: 'str34'
        t_15247: 'int40'
        t_15252: 'Sequence38[ChangesetError]'
        t_8538: 'TableDef'
        t_8539: 'MappingProxyType41[str34, str34]'
        t_8540: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_891:
            if not this_270.is_valid_764:
                return_437 = this_270
                fn_891.break_()
            t_15241 = field_889.sql_value
            if not mapped_has_15567(this_270.changes_762, t_15241):
                return_437 = this_270
                fn_891.break_()
            t_15243 = field_889.sql_value
            val_892: 'str34' = this_270.changes_762.get(t_15243, '')
            idx_893: 'int40' = val_892.find(prefix_890)
            starts_894: 'bool42'
            if idx_893 >= 0:
                t_15247 = string_count_between_15571(val_892, 0, require_string_index_15588(idx_893))
                starts_894 = t_15247 == 0
            else:
                starts_894 = False
            if not starts_894:
                eb_895: 'MutableSequence45[ChangesetError]' = list_15566(this_270.errors_763)
                eb_895.append(ChangesetError(field_889.sql_value, 'must start with the given prefix'))
                t_8538 = this_270.table_def_760
                t_8539 = this_270.params_761
                t_8540 = this_270.changes_762
                t_15252 = tuple_15569(eb_895)
                return_437 = ChangesetImpl_249(t_8538, t_8539, t_8540, t_15252, False)
                fn_891.break_()
            return_437 = this_270
        return return_437
    def validate_ends_with(this_271, field_897: 'SafeIdentifier', suffix_898: 'str34') -> 'Changeset':
        return_438: 'Changeset'
        t_15213: 'str34'
        t_15215: 'str34'
        t_15220: 'int40'
        t_15226: 'Sequence38[ChangesetError]'
        t_15228: 'int40'
        t_15229: 'bool42'
        t_15233: 'int40'
        t_15234: 'int40'
        t_15239: 'Sequence38[ChangesetError]'
        t_8503: 'TableDef'
        t_8504: 'MappingProxyType41[str34, str34]'
        t_8505: 'MappingProxyType41[str34, str34]'
        t_8509: 'bool42'
        t_8520: 'TableDef'
        t_8521: 'MappingProxyType41[str34, str34]'
        t_8522: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_899:
            if not this_271.is_valid_764:
                return_438 = this_271
                fn_899.break_()
            t_15213 = field_897.sql_value
            if not mapped_has_15567(this_271.changes_762, t_15213):
                return_438 = this_271
                fn_899.break_()
            t_15215 = field_897.sql_value
            val_900: 'str34' = this_271.changes_762.get(t_15215, '')
            val_len_901: 'int40' = string_count_between_15571(val_900, 0, len_15570(val_900))
            t_15220 = len_15570(suffix_898)
            suffix_len_902: 'int40' = string_count_between_15571(suffix_898, 0, t_15220)
            if val_len_901 < suffix_len_902:
                eb_903: 'MutableSequence45[ChangesetError]' = list_15566(this_271.errors_763)
                eb_903.append(ChangesetError(field_897.sql_value, 'must end with the given suffix'))
                t_8503 = this_271.table_def_760
                t_8504 = this_271.params_761
                t_8505 = this_271.changes_762
                t_15226 = tuple_15569(eb_903)
                return_438 = ChangesetImpl_249(t_8503, t_8504, t_8505, t_15226, False)
                fn_899.break_()
            skip_count_904: 'int40' = int_sub_15589(val_len_901, suffix_len_902)
            str_idx_905: 'int40' = 0
            i_906: 'int40' = 0
            while i_906 < skip_count_904:
                t_15228 = string_next_15590(val_900, str_idx_905)
                str_idx_905 = t_15228
                i_906 = int_add_15579(i_906, 1)
            suf_idx_907: 'int40' = 0
            matches_908: 'bool42' = True
            while True:
                if matches_908:
                    t_15229 = len6(suffix_898) > suf_idx_907
                    t_8509 = t_15229
                else:
                    t_8509 = False
                if not t_8509:
                    break
                if not len6(val_900) > str_idx_905:
                    matches_908 = False
                elif string_get_15592(val_900, str_idx_905) != string_get_15592(suffix_898, suf_idx_907):
                    matches_908 = False
                else:
                    t_15233 = string_next_15590(val_900, str_idx_905)
                    str_idx_905 = t_15233
                    t_15234 = string_next_15590(suffix_898, suf_idx_907)
                    suf_idx_907 = t_15234
            if not matches_908:
                eb_909: 'MutableSequence45[ChangesetError]' = list_15566(this_271.errors_763)
                eb_909.append(ChangesetError(field_897.sql_value, 'must end with the given suffix'))
                t_8520 = this_271.table_def_760
                t_8521 = this_271.params_761
                t_8522 = this_271.changes_762
                t_15239 = tuple_15569(eb_909)
                return_438 = ChangesetImpl_249(t_8520, t_8521, t_8522, t_15239, False)
                fn_899.break_()
            return_438 = this_271
        return return_438
    def parse_bool_sql_part_910(this_272, val_911: 'str34') -> 'SqlBoolean':
        return_439: 'SqlBoolean'
        t_8480: 'bool42'
        t_8481: 'bool42'
        t_8482: 'bool42'
        t_8484: 'bool42'
        t_8485: 'bool42'
        t_8486: 'bool42'
        with Label44() as fn_912:
            if val_911 == 'true':
                t_8482 = True
            else:
                if val_911 == '1':
                    t_8481 = True
                else:
                    if val_911 == 'yes':
                        t_8480 = True
                    else:
                        t_8480 = val_911 == 'on'
                    t_8481 = t_8480
                t_8482 = t_8481
            if t_8482:
                return_439 = SqlBoolean(True)
                fn_912.break_()
            if val_911 == 'false':
                t_8486 = True
            else:
                if val_911 == '0':
                    t_8485 = True
                else:
                    if val_911 == 'no':
                        t_8484 = True
                    else:
                        t_8484 = val_911 == 'off'
                    t_8485 = t_8484
                t_8486 = t_8485
            if t_8486:
                return_439 = SqlBoolean(False)
                fn_912.break_()
            raise RuntimeError39()
        return return_439
    def value_to_sql_part_913(this_273, field_def_914: 'FieldDef', val_915: 'str34') -> 'SqlPart':
        return_440: 'SqlPart'
        t_8467: 'int40'
        t_8470: 'int64_23'
        t_8473: 'float36'
        t_8478: 'date33'
        with Label44() as fn_916:
            ft_917: 'FieldType' = field_def_914.field_type
            if isinstance47(ft_917, StringField):
                return_440 = SqlString(val_915)
                fn_916.break_()
            if isinstance47(ft_917, IntField):
                t_8467 = string_to_int32_15574(val_915)
                return_440 = SqlInt32(t_8467)
                fn_916.break_()
            if isinstance47(ft_917, Int64Field):
                t_8470 = string_to_int64_15575(val_915)
                return_440 = SqlInt64(t_8470)
                fn_916.break_()
            if isinstance47(ft_917, FloatField):
                t_8473 = string_to_float64_15576(val_915)
                return_440 = SqlFloat64(t_8473)
                fn_916.break_()
            if isinstance47(ft_917, BoolField):
                return_440 = this_273.parse_bool_sql_part_910(val_915)
                fn_916.break_()
            if isinstance47(ft_917, DateField):
                t_8478 = date_from_iso_string_15593(val_915)
                return_440 = SqlDate(t_8478)
                fn_916.break_()
            raise RuntimeError39()
        return return_440
    def to_insert_sql(this_274) -> 'SqlFragment':
        t_15145: 'int40'
        t_15152: 'str34'
        t_15157: 'int40'
        t_15159: 'str34'
        t_15164: 'str34'
        t_15167: 'int40'
        t_15173: 'str34'
        t_15193: 'int40'
        t_8417: 'bool42'
        t_8418: 'bool42'
        t_8425: 'FieldDef'
        t_8431: 'SqlPart'
        if not this_274.is_valid_764:
            raise RuntimeError39()
        i_920: 'int40' = 0
        while True:
            with Label44() as continue_15556:
                t_15145 = len_15570(this_274.table_def_760.fields)
                if not i_920 < t_15145:
                    break
                f_921: 'FieldDef' = list_get_15578(this_274.table_def_760.fields, i_920)
                if f_921.virtual:
                    continue_15556.break_()
                dv_922: 'Union35[SqlPart, None]' = f_921.default_value
                if not f_921.nullable:
                    t_15152 = f_921.name.sql_value
                    if not mapped_has_15567(this_274.changes_762, t_15152):
                        t_8417 = dv_922 is None
                    else:
                        t_8417 = False
                    t_8418 = t_8417
                else:
                    t_8418 = False
                if t_8418:
                    raise RuntimeError39()
            i_920 = int_add_15579(i_920, 1)
        col_names_923: 'MutableSequence45[str34]' = list_15566()
        val_parts_924: 'MutableSequence45[SqlPart]' = list_15566()
        pairs_925: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_15577(this_274.changes_762)
        i_926: 'int40' = 0
        while True:
            with Label44() as continue_15557:
                t_15157 = len_15570(pairs_925)
                if not i_926 < t_15157:
                    break
                pair_927: 'Pair32[str34, str34]' = list_get_15578(pairs_925, i_926)
                t_15159 = pair_927.key
                t_8425 = this_274.table_def_760.field(t_15159)
                fd_928: 'FieldDef' = t_8425
                if fd_928.virtual:
                    continue_15557.break_()
                col_names_923.append(fd_928.name.sql_value)
                t_15164 = pair_927.value
                t_8431 = this_274.value_to_sql_part_913(fd_928, t_15164)
                val_parts_924.append(t_8431)
            i_926 = int_add_15579(i_926, 1)
        i_929: 'int40' = 0
        while True:
            with Label44() as continue_15558:
                t_15167 = len_15570(this_274.table_def_760.fields)
                if not i_929 < t_15167:
                    break
                f_930: 'FieldDef' = list_get_15578(this_274.table_def_760.fields, i_929)
                if f_930.virtual:
                    continue_15558.break_()
                dv_931: 'Union35[SqlPart, None]' = f_930.default_value
                if not dv_931 is None:
                    dv_2622: 'SqlPart' = dv_931
                    t_15173 = f_930.name.sql_value
                    if not mapped_has_15567(this_274.changes_762, t_15173):
                        col_names_923.append(f_930.name.sql_value)
                        val_parts_924.append(dv_2622)
            i_929 = int_add_15579(i_929, 1)
        if len_15570(val_parts_924) == 0:
            raise RuntimeError39()
        b_932: 'SqlBuilder' = SqlBuilder()
        b_932.append_safe('INSERT INTO ')
        b_932.append_safe(this_274.table_def_760.table_name.sql_value)
        b_932.append_safe(' (')
        t_15186: 'Sequence38[str34]' = tuple_15569(col_names_923)
        def fn_15143(c_933: 'str34') -> 'str34':
            return c_933
        b_932.append_safe(list_join_15594(t_15186, ', ', fn_15143))
        b_932.append_safe(') VALUES (')
        b_932.append_part(list_get_15578(val_parts_924, 0))
        j_934: 'int40' = 1
        while True:
            t_15193 = len_15570(val_parts_924)
            if not j_934 < t_15193:
                break
            b_932.append_safe(', ')
            b_932.append_part(list_get_15578(val_parts_924, j_934))
            j_934 = int_add_15579(j_934, 1)
        b_932.append_safe(')')
        return b_932.accumulated
    def to_update_sql(this_275, id_936: 'int40') -> 'SqlFragment':
        t_15126: 'int40'
        t_15128: 'str34'
        t_15135: 'str34'
        t_8392: 'FieldDef'
        t_8399: 'SqlPart'
        if not this_275.is_valid_764:
            raise RuntimeError39()
        pairs_938: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_15577(this_275.changes_762)
        if len_15570(pairs_938) == 0:
            raise RuntimeError39()
        b_939: 'SqlBuilder' = SqlBuilder()
        b_939.append_safe('UPDATE ')
        b_939.append_safe(this_275.table_def_760.table_name.sql_value)
        b_939.append_safe(' SET ')
        set_count_940: 'int40' = 0
        i_941: 'int40' = 0
        while True:
            with Label44() as continue_15559:
                t_15126 = len_15570(pairs_938)
                if not i_941 < t_15126:
                    break
                pair_942: 'Pair32[str34, str34]' = list_get_15578(pairs_938, i_941)
                t_15128 = pair_942.key
                t_8392 = this_275.table_def_760.field(t_15128)
                fd_943: 'FieldDef' = t_8392
                if fd_943.virtual:
                    continue_15559.break_()
                if set_count_940 > 0:
                    b_939.append_safe(', ')
                b_939.append_safe(fd_943.name.sql_value)
                b_939.append_safe(' = ')
                t_15135 = pair_942.value
                t_8399 = this_275.value_to_sql_part_913(fd_943, t_15135)
                b_939.append_part(t_8399)
                set_count_940 = int_add_15579(set_count_940, 1)
            i_941 = int_add_15579(i_941, 1)
        if set_count_940 == 0:
            raise RuntimeError39()
        b_939.append_safe(' WHERE ')
        b_939.append_safe(this_275.table_def_760.pk_name())
        b_939.append_safe(' = ')
        b_939.append_int32(id_936)
        return b_939.accumulated
    def __init__(this_412, table_def_945: 'TableDef', params_946: 'MappingProxyType41[str34, str34]', changes_947: 'MappingProxyType41[str34, str34]', errors_948: 'Sequence38[ChangesetError]', is_valid_949: 'bool42') -> None:
        this_412.table_def_760 = table_def_945
        this_412.params_761 = params_946
        this_412.changes_762 = changes_947
        this_412.errors_763 = errors_948
        this_412.is_valid_764 = is_valid_949
class JoinType(metaclass = ABCMeta37):
    def keyword(this_276) -> 'str34':
        raise RuntimeError39()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_277) -> 'str34':
        return 'INNER JOIN'
    def __init__(this_448) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_278) -> 'str34':
        return 'LEFT JOIN'
    def __init__(this_451) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_279) -> 'str34':
        return 'RIGHT JOIN'
    def __init__(this_454) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_280) -> 'str34':
        return 'FULL OUTER JOIN'
    def __init__(this_457) -> None:
        pass
class CrossJoin(JoinType):
    __slots__ = ()
    def keyword(this_281) -> 'str34':
        return 'CROSS JOIN'
    def __init__(this_460) -> None:
        pass
class JoinClause:
    join_type_1214: 'JoinType'
    table_1215: 'SafeIdentifier'
    on_condition_1216: 'Union35[SqlFragment, None]'
    __slots__ = ('join_type_1214', 'table_1215', 'on_condition_1216')
    def __init__(this_463, join_type_1218: 'JoinType', table_1219: 'SafeIdentifier', on_condition_1220: 'Union35[SqlFragment, None]') -> None:
        this_463.join_type_1214 = join_type_1218
        this_463.table_1215 = table_1219
        this_463.on_condition_1216 = on_condition_1220
    @property
    def join_type(this_2187) -> 'JoinType':
        return this_2187.join_type_1214
    @property
    def table(this_2190) -> 'SafeIdentifier':
        return this_2190.table_1215
    @property
    def on_condition(this_2193) -> 'Union35[SqlFragment, None]':
        return this_2193.on_condition_1216
class NullsPosition(metaclass = ABCMeta37):
    def keyword(this_282) -> 'str34':
        raise RuntimeError39()
class NullsFirst(NullsPosition):
    __slots__ = ()
    def keyword(this_283) -> 'str34':
        return ' NULLS FIRST'
    def __init__(this_467) -> None:
        pass
class NullsLast(NullsPosition):
    __slots__ = ()
    def keyword(this_284) -> 'str34':
        return ' NULLS LAST'
    def __init__(this_470) -> None:
        pass
class OrderClause:
    field_1229: 'SafeIdentifier'
    ascending_1230: 'bool42'
    nulls_pos_1231: 'Union35[NullsPosition, None]'
    __slots__ = ('field_1229', 'ascending_1230', 'nulls_pos_1231')
    def __init__(this_473, field_1233: 'SafeIdentifier', ascending_1234: 'bool42', nulls_pos_1235: 'Union35[NullsPosition, None]') -> None:
        this_473.field_1229 = field_1233
        this_473.ascending_1230 = ascending_1234
        this_473.nulls_pos_1231 = nulls_pos_1235
    @property
    def field(this_2196) -> 'SafeIdentifier':
        return this_2196.field_1229
    @property
    def ascending(this_2199) -> 'bool42':
        return this_2199.ascending_1230
    @property
    def nulls_pos(this_2202) -> 'Union35[NullsPosition, None]':
        return this_2202.nulls_pos_1231
class LockMode(metaclass = ABCMeta37):
    def keyword(this_285) -> 'str34':
        raise RuntimeError39()
class ForUpdate(LockMode):
    __slots__ = ()
    def keyword(this_286) -> 'str34':
        return ' FOR UPDATE'
    def __init__(this_477) -> None:
        pass
class ForShare(LockMode):
    __slots__ = ()
    def keyword(this_287) -> 'str34':
        return ' FOR SHARE'
    def __init__(this_480) -> None:
        pass
class WhereClause(metaclass = ABCMeta37):
    def keyword(this_289) -> 'str34':
        raise RuntimeError39()
class AndCondition(WhereClause):
    condition_1248: 'SqlFragment'
    __slots__ = ('condition_1248',)
    @property
    def condition(this_290) -> 'SqlFragment':
        return this_290.condition_1248
    def keyword(this_291) -> 'str34':
        return 'AND'
    def __init__(this_487, condition_1254: 'SqlFragment') -> None:
        this_487.condition_1248 = condition_1254
class OrCondition(WhereClause):
    condition_1255: 'SqlFragment'
    __slots__ = ('condition_1255',)
    @property
    def condition(this_292) -> 'SqlFragment':
        return this_292.condition_1255
    def keyword(this_293) -> 'str34':
        return 'OR'
    def __init__(this_492, condition_1261: 'SqlFragment') -> None:
        this_492.condition_1255 = condition_1261
class Query:
    table_name_1262: 'SafeIdentifier'
    conditions_1263: 'Sequence38[WhereClause]'
    selected_fields_1264: 'Sequence38[SafeIdentifier]'
    order_clauses_1265: 'Sequence38[OrderClause]'
    limit_val_1266: 'Union35[int40, None]'
    offset_val_1267: 'Union35[int40, None]'
    join_clauses_1268: 'Sequence38[JoinClause]'
    group_by_fields_1269: 'Sequence38[SafeIdentifier]'
    having_conditions_1270: 'Sequence38[WhereClause]'
    is_distinct_1271: 'bool42'
    select_exprs_1272: 'Sequence38[SqlFragment]'
    lock_mode_1273: 'Union35[LockMode, None]'
    __slots__ = ('table_name_1262', 'conditions_1263', 'selected_fields_1264', 'order_clauses_1265', 'limit_val_1266', 'offset_val_1267', 'join_clauses_1268', 'group_by_fields_1269', 'having_conditions_1270', 'is_distinct_1271', 'select_exprs_1272', 'lock_mode_1273')
    def where(this_294, condition_1275: 'SqlFragment') -> 'Query':
        nb_1277: 'MutableSequence45[WhereClause]' = list_15566(this_294.conditions_1263)
        nb_1277.append(AndCondition(condition_1275))
        return Query(this_294.table_name_1262, tuple_15569(nb_1277), this_294.selected_fields_1264, this_294.order_clauses_1265, this_294.limit_val_1266, this_294.offset_val_1267, this_294.join_clauses_1268, this_294.group_by_fields_1269, this_294.having_conditions_1270, this_294.is_distinct_1271, this_294.select_exprs_1272, this_294.lock_mode_1273)
    def or_where(this_295, condition_1279: 'SqlFragment') -> 'Query':
        nb_1281: 'MutableSequence45[WhereClause]' = list_15566(this_295.conditions_1263)
        nb_1281.append(OrCondition(condition_1279))
        return Query(this_295.table_name_1262, tuple_15569(nb_1281), this_295.selected_fields_1264, this_295.order_clauses_1265, this_295.limit_val_1266, this_295.offset_val_1267, this_295.join_clauses_1268, this_295.group_by_fields_1269, this_295.having_conditions_1270, this_295.is_distinct_1271, this_295.select_exprs_1272, this_295.lock_mode_1273)
    def where_null(this_296, field_1283: 'SafeIdentifier') -> 'Query':
        b_1285: 'SqlBuilder' = SqlBuilder()
        b_1285.append_safe(field_1283.sql_value)
        b_1285.append_safe(' IS NULL')
        t_14044: 'SqlFragment' = b_1285.accumulated
        return this_296.where(t_14044)
    def where_not_null(this_297, field_1287: 'SafeIdentifier') -> 'Query':
        b_1289: 'SqlBuilder' = SqlBuilder()
        b_1289.append_safe(field_1287.sql_value)
        b_1289.append_safe(' IS NOT NULL')
        t_14038: 'SqlFragment' = b_1289.accumulated
        return this_297.where(t_14038)
    def where_in(this_298, field_1291: 'SafeIdentifier', values_1292: 'Sequence38[SqlPart]') -> 'Query':
        return_512: 'Query'
        t_14019: 'SqlFragment'
        t_14027: 'int40'
        t_14032: 'SqlFragment'
        with Label44() as fn_1293:
            if not values_1292:
                b_1294: 'SqlBuilder' = SqlBuilder()
                b_1294.append_safe('1 = 0')
                t_14019 = b_1294.accumulated
                return_512 = this_298.where(t_14019)
                fn_1293.break_()
            b_1295: 'SqlBuilder' = SqlBuilder()
            b_1295.append_safe(field_1291.sql_value)
            b_1295.append_safe(' IN (')
            b_1295.append_part(list_get_15578(values_1292, 0))
            i_1296: 'int40' = 1
            while True:
                t_14027 = len_15570(values_1292)
                if not i_1296 < t_14027:
                    break
                b_1295.append_safe(', ')
                b_1295.append_part(list_get_15578(values_1292, i_1296))
                i_1296 = int_add_15579(i_1296, 1)
            b_1295.append_safe(')')
            t_14032 = b_1295.accumulated
            return_512 = this_298.where(t_14032)
        return return_512
    def where_in_subquery(this_299, field_1298: 'SafeIdentifier', sub_1299: 'Query') -> 'Query':
        b_1301: 'SqlBuilder' = SqlBuilder()
        b_1301.append_safe(field_1298.sql_value)
        b_1301.append_safe(' IN (')
        b_1301.append_fragment(sub_1299.to_sql())
        b_1301.append_safe(')')
        t_14014: 'SqlFragment' = b_1301.accumulated
        return this_299.where(t_14014)
    def where_not(this_300, condition_1303: 'SqlFragment') -> 'Query':
        b_1305: 'SqlBuilder' = SqlBuilder()
        b_1305.append_safe('NOT (')
        b_1305.append_fragment(condition_1303)
        b_1305.append_safe(')')
        t_14005: 'SqlFragment' = b_1305.accumulated
        return this_300.where(t_14005)
    def where_between(this_301, field_1307: 'SafeIdentifier', low_1308: 'SqlPart', high_1309: 'SqlPart') -> 'Query':
        b_1311: 'SqlBuilder' = SqlBuilder()
        b_1311.append_safe(field_1307.sql_value)
        b_1311.append_safe(' BETWEEN ')
        b_1311.append_part(low_1308)
        b_1311.append_safe(' AND ')
        b_1311.append_part(high_1309)
        t_13999: 'SqlFragment' = b_1311.accumulated
        return this_301.where(t_13999)
    def where_like(this_302, field_1313: 'SafeIdentifier', pattern_1314: 'str34') -> 'Query':
        b_1316: 'SqlBuilder' = SqlBuilder()
        b_1316.append_safe(field_1313.sql_value)
        b_1316.append_safe(' LIKE ')
        b_1316.append_string(pattern_1314)
        t_13990: 'SqlFragment' = b_1316.accumulated
        return this_302.where(t_13990)
    def where_i_like(this_303, field_1318: 'SafeIdentifier', pattern_1319: 'str34') -> 'Query':
        b_1321: 'SqlBuilder' = SqlBuilder()
        b_1321.append_safe(field_1318.sql_value)
        b_1321.append_safe(' ILIKE ')
        b_1321.append_string(pattern_1319)
        t_13983: 'SqlFragment' = b_1321.accumulated
        return this_303.where(t_13983)
    def select(this_304, fields_1323: 'Sequence38[SafeIdentifier]') -> 'Query':
        return Query(this_304.table_name_1262, this_304.conditions_1263, fields_1323, this_304.order_clauses_1265, this_304.limit_val_1266, this_304.offset_val_1267, this_304.join_clauses_1268, this_304.group_by_fields_1269, this_304.having_conditions_1270, this_304.is_distinct_1271, this_304.select_exprs_1272, this_304.lock_mode_1273)
    def select_expr(this_305, exprs_1326: 'Sequence38[SqlFragment]') -> 'Query':
        return Query(this_305.table_name_1262, this_305.conditions_1263, this_305.selected_fields_1264, this_305.order_clauses_1265, this_305.limit_val_1266, this_305.offset_val_1267, this_305.join_clauses_1268, this_305.group_by_fields_1269, this_305.having_conditions_1270, this_305.is_distinct_1271, exprs_1326, this_305.lock_mode_1273)
    def order_by(this_306, field_1329: 'SafeIdentifier', ascending_1330: 'bool42') -> 'Query':
        nb_1332: 'MutableSequence45[OrderClause]' = list_15566(this_306.order_clauses_1265)
        nb_1332.append(OrderClause(field_1329, ascending_1330, None))
        return Query(this_306.table_name_1262, this_306.conditions_1263, this_306.selected_fields_1264, tuple_15569(nb_1332), this_306.limit_val_1266, this_306.offset_val_1267, this_306.join_clauses_1268, this_306.group_by_fields_1269, this_306.having_conditions_1270, this_306.is_distinct_1271, this_306.select_exprs_1272, this_306.lock_mode_1273)
    def order_by_nulls(this_307, field_1334: 'SafeIdentifier', ascending_1335: 'bool42', nulls_1336: 'NullsPosition') -> 'Query':
        nb_1338: 'MutableSequence45[OrderClause]' = list_15566(this_307.order_clauses_1265)
        nb_1338.append(OrderClause(field_1334, ascending_1335, nulls_1336))
        return Query(this_307.table_name_1262, this_307.conditions_1263, this_307.selected_fields_1264, tuple_15569(nb_1338), this_307.limit_val_1266, this_307.offset_val_1267, this_307.join_clauses_1268, this_307.group_by_fields_1269, this_307.having_conditions_1270, this_307.is_distinct_1271, this_307.select_exprs_1272, this_307.lock_mode_1273)
    def limit(this_308, n_1340: 'int40') -> 'Query':
        if n_1340 < 0:
            raise RuntimeError39()
        return Query(this_308.table_name_1262, this_308.conditions_1263, this_308.selected_fields_1264, this_308.order_clauses_1265, n_1340, this_308.offset_val_1267, this_308.join_clauses_1268, this_308.group_by_fields_1269, this_308.having_conditions_1270, this_308.is_distinct_1271, this_308.select_exprs_1272, this_308.lock_mode_1273)
    def offset(this_309, n_1343: 'int40') -> 'Query':
        if n_1343 < 0:
            raise RuntimeError39()
        return Query(this_309.table_name_1262, this_309.conditions_1263, this_309.selected_fields_1264, this_309.order_clauses_1265, this_309.limit_val_1266, n_1343, this_309.join_clauses_1268, this_309.group_by_fields_1269, this_309.having_conditions_1270, this_309.is_distinct_1271, this_309.select_exprs_1272, this_309.lock_mode_1273)
    def join(this_310, join_type_1346: 'JoinType', table_1347: 'SafeIdentifier', on_condition_1348: 'SqlFragment') -> 'Query':
        nb_1350: 'MutableSequence45[JoinClause]' = list_15566(this_310.join_clauses_1268)
        nb_1350.append(JoinClause(join_type_1346, table_1347, on_condition_1348))
        return Query(this_310.table_name_1262, this_310.conditions_1263, this_310.selected_fields_1264, this_310.order_clauses_1265, this_310.limit_val_1266, this_310.offset_val_1267, tuple_15569(nb_1350), this_310.group_by_fields_1269, this_310.having_conditions_1270, this_310.is_distinct_1271, this_310.select_exprs_1272, this_310.lock_mode_1273)
    def inner_join(this_311, table_1352: 'SafeIdentifier', on_condition_1353: 'SqlFragment') -> 'Query':
        t_13945: 'InnerJoin' = InnerJoin()
        return this_311.join(t_13945, table_1352, on_condition_1353)
    def left_join(this_312, table_1356: 'SafeIdentifier', on_condition_1357: 'SqlFragment') -> 'Query':
        t_13943: 'LeftJoin' = LeftJoin()
        return this_312.join(t_13943, table_1356, on_condition_1357)
    def right_join(this_313, table_1360: 'SafeIdentifier', on_condition_1361: 'SqlFragment') -> 'Query':
        t_13941: 'RightJoin' = RightJoin()
        return this_313.join(t_13941, table_1360, on_condition_1361)
    def full_join(this_314, table_1364: 'SafeIdentifier', on_condition_1365: 'SqlFragment') -> 'Query':
        t_13939: 'FullJoin' = FullJoin()
        return this_314.join(t_13939, table_1364, on_condition_1365)
    def cross_join(this_315, table_1368: 'SafeIdentifier') -> 'Query':
        nb_1370: 'MutableSequence45[JoinClause]' = list_15566(this_315.join_clauses_1268)
        nb_1370.append(JoinClause(CrossJoin(), table_1368, None))
        return Query(this_315.table_name_1262, this_315.conditions_1263, this_315.selected_fields_1264, this_315.order_clauses_1265, this_315.limit_val_1266, this_315.offset_val_1267, tuple_15569(nb_1370), this_315.group_by_fields_1269, this_315.having_conditions_1270, this_315.is_distinct_1271, this_315.select_exprs_1272, this_315.lock_mode_1273)
    def group_by(this_316, field_1372: 'SafeIdentifier') -> 'Query':
        nb_1374: 'MutableSequence45[SafeIdentifier]' = list_15566(this_316.group_by_fields_1269)
        nb_1374.append(field_1372)
        return Query(this_316.table_name_1262, this_316.conditions_1263, this_316.selected_fields_1264, this_316.order_clauses_1265, this_316.limit_val_1266, this_316.offset_val_1267, this_316.join_clauses_1268, tuple_15569(nb_1374), this_316.having_conditions_1270, this_316.is_distinct_1271, this_316.select_exprs_1272, this_316.lock_mode_1273)
    def having(this_317, condition_1376: 'SqlFragment') -> 'Query':
        nb_1378: 'MutableSequence45[WhereClause]' = list_15566(this_317.having_conditions_1270)
        nb_1378.append(AndCondition(condition_1376))
        return Query(this_317.table_name_1262, this_317.conditions_1263, this_317.selected_fields_1264, this_317.order_clauses_1265, this_317.limit_val_1266, this_317.offset_val_1267, this_317.join_clauses_1268, this_317.group_by_fields_1269, tuple_15569(nb_1378), this_317.is_distinct_1271, this_317.select_exprs_1272, this_317.lock_mode_1273)
    def or_having(this_318, condition_1380: 'SqlFragment') -> 'Query':
        nb_1382: 'MutableSequence45[WhereClause]' = list_15566(this_318.having_conditions_1270)
        nb_1382.append(OrCondition(condition_1380))
        return Query(this_318.table_name_1262, this_318.conditions_1263, this_318.selected_fields_1264, this_318.order_clauses_1265, this_318.limit_val_1266, this_318.offset_val_1267, this_318.join_clauses_1268, this_318.group_by_fields_1269, tuple_15569(nb_1382), this_318.is_distinct_1271, this_318.select_exprs_1272, this_318.lock_mode_1273)
    def distinct(this_319) -> 'Query':
        return Query(this_319.table_name_1262, this_319.conditions_1263, this_319.selected_fields_1264, this_319.order_clauses_1265, this_319.limit_val_1266, this_319.offset_val_1267, this_319.join_clauses_1268, this_319.group_by_fields_1269, this_319.having_conditions_1270, True, this_319.select_exprs_1272, this_319.lock_mode_1273)
    def lock(this_320, mode_1386: 'LockMode') -> 'Query':
        return Query(this_320.table_name_1262, this_320.conditions_1263, this_320.selected_fields_1264, this_320.order_clauses_1265, this_320.limit_val_1266, this_320.offset_val_1267, this_320.join_clauses_1268, this_320.group_by_fields_1269, this_320.having_conditions_1270, this_320.is_distinct_1271, this_320.select_exprs_1272, mode_1386)
    def to_sql(this_321) -> 'SqlFragment':
        t_13830: 'int40'
        t_13849: 'int40'
        t_13868: 'int40'
        b_1390: 'SqlBuilder' = SqlBuilder()
        if this_321.is_distinct_1271:
            b_1390.append_safe('SELECT DISTINCT ')
        else:
            b_1390.append_safe('SELECT ')
        if not (not this_321.select_exprs_1272):
            b_1390.append_fragment(list_get_15578(this_321.select_exprs_1272, 0))
            i_1391: 'int40' = 1
            while True:
                t_13830 = len_15570(this_321.select_exprs_1272)
                if not i_1391 < t_13830:
                    break
                b_1390.append_safe(', ')
                b_1390.append_fragment(list_get_15578(this_321.select_exprs_1272, i_1391))
                i_1391 = int_add_15579(i_1391, 1)
        elif not this_321.selected_fields_1264:
            b_1390.append_safe('*')
        else:
            def fn_13823(f_1392: 'SafeIdentifier') -> 'str34':
                return f_1392.sql_value
            b_1390.append_safe(list_join_15594(this_321.selected_fields_1264, ', ', fn_13823))
        b_1390.append_safe(' FROM ')
        b_1390.append_safe(this_321.table_name_1262.sql_value)
        def fn_13822(jc_1393: 'JoinClause') -> 'None':
            b_1390.append_safe(' ')
            t_13810: 'str34' = jc_1393.join_type.keyword()
            b_1390.append_safe(t_13810)
            b_1390.append_safe(' ')
            t_13814: 'str34' = jc_1393.table.sql_value
            b_1390.append_safe(t_13814)
            oc_1394: 'Union35[SqlFragment, None]' = jc_1393.on_condition
            if not oc_1394 is None:
                oc_2623: 'SqlFragment' = oc_1394
                b_1390.append_safe(' ON ')
                b_1390.append_fragment(oc_2623)
        list_for_each_15564(this_321.join_clauses_1268, fn_13822)
        if not (not this_321.conditions_1263):
            b_1390.append_safe(' WHERE ')
            b_1390.append_fragment(list_get_15578(this_321.conditions_1263, 0).condition)
            i_1395: 'int40' = 1
            while True:
                t_13849 = len_15570(this_321.conditions_1263)
                if not i_1395 < t_13849:
                    break
                b_1390.append_safe(' ')
                b_1390.append_safe(list_get_15578(this_321.conditions_1263, i_1395).keyword())
                b_1390.append_safe(' ')
                b_1390.append_fragment(list_get_15578(this_321.conditions_1263, i_1395).condition)
                i_1395 = int_add_15579(i_1395, 1)
        if not (not this_321.group_by_fields_1269):
            b_1390.append_safe(' GROUP BY ')
            def fn_13821(f_1396: 'SafeIdentifier') -> 'str34':
                return f_1396.sql_value
            b_1390.append_safe(list_join_15594(this_321.group_by_fields_1269, ', ', fn_13821))
        if not (not this_321.having_conditions_1270):
            b_1390.append_safe(' HAVING ')
            b_1390.append_fragment(list_get_15578(this_321.having_conditions_1270, 0).condition)
            i_1397: 'int40' = 1
            while True:
                t_13868 = len_15570(this_321.having_conditions_1270)
                if not i_1397 < t_13868:
                    break
                b_1390.append_safe(' ')
                b_1390.append_safe(list_get_15578(this_321.having_conditions_1270, i_1397).keyword())
                b_1390.append_safe(' ')
                b_1390.append_fragment(list_get_15578(this_321.having_conditions_1270, i_1397).condition)
                i_1397 = int_add_15579(i_1397, 1)
        if not (not this_321.order_clauses_1265):
            b_1390.append_safe(' ORDER BY ')
            first_1398: 'bool42' = True
            def fn_13820(orc_1399: 'OrderClause') -> 'None':
                nonlocal first_1398
                t_13805: 'str34'
                t_7240: 'str34'
                if not first_1398:
                    b_1390.append_safe(', ')
                first_1398 = False
                t_13800: 'str34' = orc_1399.field.sql_value
                b_1390.append_safe(t_13800)
                if orc_1399.ascending:
                    t_7240 = ' ASC'
                else:
                    t_7240 = ' DESC'
                b_1390.append_safe(t_7240)
                np_1400: 'Union35[NullsPosition, None]' = orc_1399.nulls_pos
                if not np_1400 is None:
                    t_13805 = np_1400.keyword()
                    b_1390.append_safe(t_13805)
            list_for_each_15564(this_321.order_clauses_1265, fn_13820)
        lv_1401: 'Union35[int40, None]' = this_321.limit_val_1266
        if not lv_1401 is None:
            lv_2625: 'int40' = lv_1401
            b_1390.append_safe(' LIMIT ')
            b_1390.append_int32(lv_2625)
        ov_1402: 'Union35[int40, None]' = this_321.offset_val_1267
        if not ov_1402 is None:
            ov_2626: 'int40' = ov_1402
            b_1390.append_safe(' OFFSET ')
            b_1390.append_int32(ov_2626)
        lm_1403: 'Union35[LockMode, None]' = this_321.lock_mode_1273
        if not lm_1403 is None:
            b_1390.append_safe(lm_1403.keyword())
        return b_1390.accumulated
    def count_sql(this_322) -> 'SqlFragment':
        t_13769: 'int40'
        t_13788: 'int40'
        b_1406: 'SqlBuilder' = SqlBuilder()
        b_1406.append_safe('SELECT COUNT(*) FROM ')
        b_1406.append_safe(this_322.table_name_1262.sql_value)
        def fn_13757(jc_1407: 'JoinClause') -> 'None':
            b_1406.append_safe(' ')
            t_13747: 'str34' = jc_1407.join_type.keyword()
            b_1406.append_safe(t_13747)
            b_1406.append_safe(' ')
            t_13751: 'str34' = jc_1407.table.sql_value
            b_1406.append_safe(t_13751)
            oc2_1408: 'Union35[SqlFragment, None]' = jc_1407.on_condition
            if not oc2_1408 is None:
                oc2_2628: 'SqlFragment' = oc2_1408
                b_1406.append_safe(' ON ')
                b_1406.append_fragment(oc2_2628)
        list_for_each_15564(this_322.join_clauses_1268, fn_13757)
        if not (not this_322.conditions_1263):
            b_1406.append_safe(' WHERE ')
            b_1406.append_fragment(list_get_15578(this_322.conditions_1263, 0).condition)
            i_1409: 'int40' = 1
            while True:
                t_13769 = len_15570(this_322.conditions_1263)
                if not i_1409 < t_13769:
                    break
                b_1406.append_safe(' ')
                b_1406.append_safe(list_get_15578(this_322.conditions_1263, i_1409).keyword())
                b_1406.append_safe(' ')
                b_1406.append_fragment(list_get_15578(this_322.conditions_1263, i_1409).condition)
                i_1409 = int_add_15579(i_1409, 1)
        if not (not this_322.group_by_fields_1269):
            b_1406.append_safe(' GROUP BY ')
            def fn_13756(f_1410: 'SafeIdentifier') -> 'str34':
                return f_1410.sql_value
            b_1406.append_safe(list_join_15594(this_322.group_by_fields_1269, ', ', fn_13756))
        if not (not this_322.having_conditions_1270):
            b_1406.append_safe(' HAVING ')
            b_1406.append_fragment(list_get_15578(this_322.having_conditions_1270, 0).condition)
            i_1411: 'int40' = 1
            while True:
                t_13788 = len_15570(this_322.having_conditions_1270)
                if not i_1411 < t_13788:
                    break
                b_1406.append_safe(' ')
                b_1406.append_safe(list_get_15578(this_322.having_conditions_1270, i_1411).keyword())
                b_1406.append_safe(' ')
                b_1406.append_fragment(list_get_15578(this_322.having_conditions_1270, i_1411).condition)
                i_1411 = int_add_15579(i_1411, 1)
        return b_1406.accumulated
    def safe_to_sql(this_323, default_limit_1413: 'int40') -> 'SqlFragment':
        return_537: 'SqlFragment'
        t_7190: 'Query'
        if default_limit_1413 < 0:
            raise RuntimeError39()
        if not this_323.limit_val_1266 is None:
            return_537 = this_323.to_sql()
        else:
            t_7190 = this_323.limit(default_limit_1413)
            return_537 = t_7190.to_sql()
        return return_537
    def __init__(this_496, table_name_1416: 'SafeIdentifier', conditions_1417: 'Sequence38[WhereClause]', selected_fields_1418: 'Sequence38[SafeIdentifier]', order_clauses_1419: 'Sequence38[OrderClause]', limit_val_1420: 'Union35[int40, None]', offset_val_1421: 'Union35[int40, None]', join_clauses_1422: 'Sequence38[JoinClause]', group_by_fields_1423: 'Sequence38[SafeIdentifier]', having_conditions_1424: 'Sequence38[WhereClause]', is_distinct_1425: 'bool42', select_exprs_1426: 'Sequence38[SqlFragment]', lock_mode_1427: 'Union35[LockMode, None]') -> None:
        this_496.table_name_1262 = table_name_1416
        this_496.conditions_1263 = conditions_1417
        this_496.selected_fields_1264 = selected_fields_1418
        this_496.order_clauses_1265 = order_clauses_1419
        this_496.limit_val_1266 = limit_val_1420
        this_496.offset_val_1267 = offset_val_1421
        this_496.join_clauses_1268 = join_clauses_1422
        this_496.group_by_fields_1269 = group_by_fields_1423
        this_496.having_conditions_1270 = having_conditions_1424
        this_496.is_distinct_1271 = is_distinct_1425
        this_496.select_exprs_1272 = select_exprs_1426
        this_496.lock_mode_1273 = lock_mode_1427
    @property
    def table_name(this_2205) -> 'SafeIdentifier':
        return this_2205.table_name_1262
    @property
    def conditions(this_2208) -> 'Sequence38[WhereClause]':
        return this_2208.conditions_1263
    @property
    def selected_fields(this_2211) -> 'Sequence38[SafeIdentifier]':
        return this_2211.selected_fields_1264
    @property
    def order_clauses(this_2214) -> 'Sequence38[OrderClause]':
        return this_2214.order_clauses_1265
    @property
    def limit_val(this_2217) -> 'Union35[int40, None]':
        return this_2217.limit_val_1266
    @property
    def offset_val(this_2220) -> 'Union35[int40, None]':
        return this_2220.offset_val_1267
    @property
    def join_clauses(this_2223) -> 'Sequence38[JoinClause]':
        return this_2223.join_clauses_1268
    @property
    def group_by_fields(this_2226) -> 'Sequence38[SafeIdentifier]':
        return this_2226.group_by_fields_1269
    @property
    def having_conditions(this_2229) -> 'Sequence38[WhereClause]':
        return this_2229.having_conditions_1270
    @property
    def is_distinct(this_2232) -> 'bool42':
        return this_2232.is_distinct_1271
    @property
    def select_exprs(this_2235) -> 'Sequence38[SqlFragment]':
        return this_2235.select_exprs_1272
    @property
    def lock_mode(this_2238) -> 'Union35[LockMode, None]':
        return this_2238.lock_mode_1273
class SetClause:
    field_1474: 'SafeIdentifier'
    value_1475: 'SqlPart'
    __slots__ = ('field_1474', 'value_1475')
    def __init__(this_552, field_1477: 'SafeIdentifier', value_1478: 'SqlPart') -> None:
        this_552.field_1474 = field_1477
        this_552.value_1475 = value_1478
    @property
    def field(this_2241) -> 'SafeIdentifier':
        return this_2241.field_1474
    @property
    def value(this_2244) -> 'SqlPart':
        return this_2244.value_1475
class UpdateQuery:
    table_name_1479: 'SafeIdentifier'
    set_clauses_1480: 'Sequence38[SetClause]'
    conditions_1481: 'Sequence38[WhereClause]'
    limit_val_1482: 'Union35[int40, None]'
    __slots__ = ('table_name_1479', 'set_clauses_1480', 'conditions_1481', 'limit_val_1482')
    def set(this_324, field_1484: 'SafeIdentifier', value_1485: 'SqlPart') -> 'UpdateQuery':
        nb_1487: 'MutableSequence45[SetClause]' = list_15566(this_324.set_clauses_1480)
        nb_1487.append(SetClause(field_1484, value_1485))
        return UpdateQuery(this_324.table_name_1479, tuple_15569(nb_1487), this_324.conditions_1481, this_324.limit_val_1482)
    def where(this_325, condition_1489: 'SqlFragment') -> 'UpdateQuery':
        nb_1491: 'MutableSequence45[WhereClause]' = list_15566(this_325.conditions_1481)
        nb_1491.append(AndCondition(condition_1489))
        return UpdateQuery(this_325.table_name_1479, this_325.set_clauses_1480, tuple_15569(nb_1491), this_325.limit_val_1482)
    def or_where(this_326, condition_1493: 'SqlFragment') -> 'UpdateQuery':
        nb_1495: 'MutableSequence45[WhereClause]' = list_15566(this_326.conditions_1481)
        nb_1495.append(OrCondition(condition_1493))
        return UpdateQuery(this_326.table_name_1479, this_326.set_clauses_1480, tuple_15569(nb_1495), this_326.limit_val_1482)
    def limit(this_327, n_1497: 'int40') -> 'UpdateQuery':
        if n_1497 < 0:
            raise RuntimeError39()
        return UpdateQuery(this_327.table_name_1479, this_327.set_clauses_1480, this_327.conditions_1481, n_1497)
    def to_sql(this_328) -> 'SqlFragment':
        t_13604: 'int40'
        t_13618: 'int40'
        if not this_328.conditions_1481:
            raise RuntimeError39()
        if not this_328.set_clauses_1480:
            raise RuntimeError39()
        b_1501: 'SqlBuilder' = SqlBuilder()
        b_1501.append_safe('UPDATE ')
        b_1501.append_safe(this_328.table_name_1479.sql_value)
        b_1501.append_safe(' SET ')
        b_1501.append_safe(list_get_15578(this_328.set_clauses_1480, 0).field.sql_value)
        b_1501.append_safe(' = ')
        b_1501.append_part(list_get_15578(this_328.set_clauses_1480, 0).value)
        i_1502: 'int40' = 1
        while True:
            t_13604 = len_15570(this_328.set_clauses_1480)
            if not i_1502 < t_13604:
                break
            b_1501.append_safe(', ')
            b_1501.append_safe(list_get_15578(this_328.set_clauses_1480, i_1502).field.sql_value)
            b_1501.append_safe(' = ')
            b_1501.append_part(list_get_15578(this_328.set_clauses_1480, i_1502).value)
            i_1502 = int_add_15579(i_1502, 1)
        b_1501.append_safe(' WHERE ')
        b_1501.append_fragment(list_get_15578(this_328.conditions_1481, 0).condition)
        i_1503: 'int40' = 1
        while True:
            t_13618 = len_15570(this_328.conditions_1481)
            if not i_1503 < t_13618:
                break
            b_1501.append_safe(' ')
            b_1501.append_safe(list_get_15578(this_328.conditions_1481, i_1503).keyword())
            b_1501.append_safe(' ')
            b_1501.append_fragment(list_get_15578(this_328.conditions_1481, i_1503).condition)
            i_1503 = int_add_15579(i_1503, 1)
        lv_1504: 'Union35[int40, None]' = this_328.limit_val_1482
        if not lv_1504 is None:
            lv_2629: 'int40' = lv_1504
            b_1501.append_safe(' LIMIT ')
            b_1501.append_int32(lv_2629)
        return b_1501.accumulated
    def __init__(this_554, table_name_1506: 'SafeIdentifier', set_clauses_1507: 'Sequence38[SetClause]', conditions_1508: 'Sequence38[WhereClause]', limit_val_1509: 'Union35[int40, None]') -> None:
        this_554.table_name_1479 = table_name_1506
        this_554.set_clauses_1480 = set_clauses_1507
        this_554.conditions_1481 = conditions_1508
        this_554.limit_val_1482 = limit_val_1509
    @property
    def table_name(this_2247) -> 'SafeIdentifier':
        return this_2247.table_name_1479
    @property
    def set_clauses(this_2250) -> 'Sequence38[SetClause]':
        return this_2250.set_clauses_1480
    @property
    def conditions(this_2253) -> 'Sequence38[WhereClause]':
        return this_2253.conditions_1481
    @property
    def limit_val(this_2256) -> 'Union35[int40, None]':
        return this_2256.limit_val_1482
class DeleteQuery:
    table_name_1510: 'SafeIdentifier'
    conditions_1511: 'Sequence38[WhereClause]'
    limit_val_1512: 'Union35[int40, None]'
    __slots__ = ('table_name_1510', 'conditions_1511', 'limit_val_1512')
    def where(this_329, condition_1514: 'SqlFragment') -> 'DeleteQuery':
        nb_1516: 'MutableSequence45[WhereClause]' = list_15566(this_329.conditions_1511)
        nb_1516.append(AndCondition(condition_1514))
        return DeleteQuery(this_329.table_name_1510, tuple_15569(nb_1516), this_329.limit_val_1512)
    def or_where(this_330, condition_1518: 'SqlFragment') -> 'DeleteQuery':
        nb_1520: 'MutableSequence45[WhereClause]' = list_15566(this_330.conditions_1511)
        nb_1520.append(OrCondition(condition_1518))
        return DeleteQuery(this_330.table_name_1510, tuple_15569(nb_1520), this_330.limit_val_1512)
    def limit(this_331, n_1522: 'int40') -> 'DeleteQuery':
        if n_1522 < 0:
            raise RuntimeError39()
        return DeleteQuery(this_331.table_name_1510, this_331.conditions_1511, n_1522)
    def to_sql(this_332) -> 'SqlFragment':
        t_13564: 'int40'
        if not this_332.conditions_1511:
            raise RuntimeError39()
        b_1526: 'SqlBuilder' = SqlBuilder()
        b_1526.append_safe('DELETE FROM ')
        b_1526.append_safe(this_332.table_name_1510.sql_value)
        b_1526.append_safe(' WHERE ')
        b_1526.append_fragment(list_get_15578(this_332.conditions_1511, 0).condition)
        i_1527: 'int40' = 1
        while True:
            t_13564 = len_15570(this_332.conditions_1511)
            if not i_1527 < t_13564:
                break
            b_1526.append_safe(' ')
            b_1526.append_safe(list_get_15578(this_332.conditions_1511, i_1527).keyword())
            b_1526.append_safe(' ')
            b_1526.append_fragment(list_get_15578(this_332.conditions_1511, i_1527).condition)
            i_1527 = int_add_15579(i_1527, 1)
        lv_1528: 'Union35[int40, None]' = this_332.limit_val_1512
        if not lv_1528 is None:
            lv_2630: 'int40' = lv_1528
            b_1526.append_safe(' LIMIT ')
            b_1526.append_int32(lv_2630)
        return b_1526.accumulated
    def __init__(this_564, table_name_1530: 'SafeIdentifier', conditions_1531: 'Sequence38[WhereClause]', limit_val_1532: 'Union35[int40, None]') -> None:
        this_564.table_name_1510 = table_name_1530
        this_564.conditions_1511 = conditions_1531
        this_564.limit_val_1512 = limit_val_1532
    @property
    def table_name(this_2259) -> 'SafeIdentifier':
        return this_2259.table_name_1510
    @property
    def conditions(this_2262) -> 'Sequence38[WhereClause]':
        return this_2262.conditions_1511
    @property
    def limit_val(this_2265) -> 'Union35[int40, None]':
        return this_2265.limit_val_1512
class SafeIdentifier(metaclass = ABCMeta37):
    pass
class ValidatedIdentifier_334(SafeIdentifier):
    value_1763: 'str34'
    __slots__ = ('value_1763',)
    @property
    def sql_value(this_335) -> 'str34':
        return this_335.value_1763
    def __init__(this_578, value_1767: 'str34') -> None:
        this_578.value_1763 = value_1767
class FieldType(metaclass = ABCMeta37):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_584) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_586) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_588) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_590) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_592) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_594) -> None:
        pass
class FieldDef:
    name_1781: 'SafeIdentifier'
    field_type_1782: 'FieldType'
    nullable_1783: 'bool42'
    default_value_1784: 'Union35[SqlPart, None]'
    virtual_1785: 'bool42'
    __slots__ = ('name_1781', 'field_type_1782', 'nullable_1783', 'default_value_1784', 'virtual_1785')
    def __init__(this_596, name_1787: 'SafeIdentifier', field_type_1788: 'FieldType', nullable_1789: 'bool42', default_value_1790: 'Union35[SqlPart, None]', virtual_1791: 'bool42') -> None:
        this_596.name_1781 = name_1787
        this_596.field_type_1782 = field_type_1788
        this_596.nullable_1783 = nullable_1789
        this_596.default_value_1784 = default_value_1790
        this_596.virtual_1785 = virtual_1791
    @property
    def name(this_2073) -> 'SafeIdentifier':
        return this_2073.name_1781
    @property
    def field_type(this_2076) -> 'FieldType':
        return this_2076.field_type_1782
    @property
    def nullable(this_2079) -> 'bool42':
        return this_2079.nullable_1783
    @property
    def default_value(this_2082) -> 'Union35[SqlPart, None]':
        return this_2082.default_value_1784
    @property
    def virtual(this_2085) -> 'bool42':
        return this_2085.virtual_1785
class TableDef:
    table_name_1792: 'SafeIdentifier'
    fields_1793: 'Sequence38[FieldDef]'
    primary_key_1794: 'Union35[SafeIdentifier, None]'
    __slots__ = ('table_name_1792', 'fields_1793', 'primary_key_1794')
    def field(this_336, name_1796: 'str34') -> 'FieldDef':
        return_603: 'FieldDef'
        with Label44() as fn_1797:
            this_9149: 'Sequence38[FieldDef]' = this_336.fields_1793
            n_9150: 'int40' = len_15570(this_9149)
            i_9151: 'int40' = 0
            while i_9151 < n_9150:
                el_9152: 'FieldDef' = list_get_15578(this_9149, i_9151)
                i_9151 = int_add_15579(i_9151, 1)
                f_1798: 'FieldDef' = el_9152
                if f_1798.name.sql_value == name_1796:
                    return_603 = f_1798
                    fn_1797.break_()
            raise RuntimeError39()
        return return_603
    def pk_name(this_337) -> 'str34':
        return_604: 'str34'
        with Label44() as fn_1800:
            pk_1801: 'Union35[SafeIdentifier, None]' = this_337.primary_key_1794
            if not pk_1801 is None:
                pk_2609: 'SafeIdentifier' = pk_1801
                return_604 = pk_2609.sql_value
                fn_1800.break_()
            return_604 = 'id'
        return return_604
    def __init__(this_599, table_name_1803: 'SafeIdentifier', fields_1804: 'Sequence38[FieldDef]', primary_key_1805: 'Union35[SafeIdentifier, None]') -> None:
        this_599.table_name_1792 = table_name_1803
        this_599.fields_1793 = fields_1804
        this_599.primary_key_1794 = primary_key_1805
    @property
    def table_name(this_2088) -> 'SafeIdentifier':
        return this_2088.table_name_1792
    @property
    def fields(this_2091) -> 'Sequence38[FieldDef]':
        return this_2091.fields_1793
    @property
    def primary_key(this_2094) -> 'Union35[SafeIdentifier, None]':
        return this_2094.primary_key_1794
T_356 = TypeVar49('T_356', bound = Any48)
class SqlBuilder:
    buffer_1838: 'MutableSequence45[SqlPart]'
    __slots__ = ('buffer_1838',)
    def append_safe(this_338, sql_source_1840: 'str34') -> 'None':
        t_15520: 'SqlSource' = SqlSource(sql_source_1840)
        this_338.buffer_1838.append(t_15520)
    def append_fragment(this_339, fragment_1843: 'SqlFragment') -> 'None':
        t_15518: 'Sequence38[SqlPart]' = fragment_1843.parts
        list_builder_add_all_15595(this_339.buffer_1838, t_15518)
    def append_part(this_340, part_1846: 'SqlPart') -> 'None':
        this_340.buffer_1838.append(part_1846)
    def append_part_list(this_341, values_1849: 'Sequence38[SqlPart]') -> 'None':
        def fn_15514(x_1851: 'SqlPart') -> 'None':
            this_341.append_part(x_1851)
        this_341.append_list_1894(values_1849, fn_15514)
    def append_boolean(this_342, value_1853: 'bool42') -> 'None':
        t_15511: 'SqlBoolean' = SqlBoolean(value_1853)
        this_342.buffer_1838.append(t_15511)
    def append_boolean_list(this_343, values_1856: 'Sequence38[bool42]') -> 'None':
        def fn_15508(x_1858: 'bool42') -> 'None':
            this_343.append_boolean(x_1858)
        this_343.append_list_1894(values_1856, fn_15508)
    def append_date(this_344, value_1860: 'date33') -> 'None':
        t_15505: 'SqlDate' = SqlDate(value_1860)
        this_344.buffer_1838.append(t_15505)
    def append_date_list(this_345, values_1863: 'Sequence38[date33]') -> 'None':
        def fn_15502(x_1865: 'date33') -> 'None':
            this_345.append_date(x_1865)
        this_345.append_list_1894(values_1863, fn_15502)
    def append_float64(this_346, value_1867: 'float36') -> 'None':
        t_15499: 'SqlFloat64' = SqlFloat64(value_1867)
        this_346.buffer_1838.append(t_15499)
    def append_float64_list(this_347, values_1870: 'Sequence38[float36]') -> 'None':
        def fn_15496(x_1872: 'float36') -> 'None':
            this_347.append_float64(x_1872)
        this_347.append_list_1894(values_1870, fn_15496)
    def append_int32(this_348, value_1874: 'int40') -> 'None':
        t_15493: 'SqlInt32' = SqlInt32(value_1874)
        this_348.buffer_1838.append(t_15493)
    def append_int32_list(this_349, values_1877: 'Sequence38[int40]') -> 'None':
        def fn_15490(x_1879: 'int40') -> 'None':
            this_349.append_int32(x_1879)
        this_349.append_list_1894(values_1877, fn_15490)
    def append_int64(this_350, value_1881: 'int64_23') -> 'None':
        t_15487: 'SqlInt64' = SqlInt64(value_1881)
        this_350.buffer_1838.append(t_15487)
    def append_int64_list(this_351, values_1884: 'Sequence38[int64_23]') -> 'None':
        def fn_15484(x_1886: 'int64_23') -> 'None':
            this_351.append_int64(x_1886)
        this_351.append_list_1894(values_1884, fn_15484)
    def append_string(this_352, value_1888: 'str34') -> 'None':
        t_15481: 'SqlString' = SqlString(value_1888)
        this_352.buffer_1838.append(t_15481)
    def append_string_list(this_353, values_1891: 'Sequence38[str34]') -> 'None':
        def fn_15478(x_1893: 'str34') -> 'None':
            this_353.append_string(x_1893)
        this_353.append_list_1894(values_1891, fn_15478)
    def append_list_1894(this_354, values_1895: 'Sequence38[T_356]', append_value_1896: 'Callable50[[T_356], None]') -> 'None':
        t_15473: 'int40'
        t_15475: 'T_356'
        i_1898: 'int40' = 0
        while True:
            t_15473 = len_15570(values_1895)
            if not i_1898 < t_15473:
                break
            if i_1898 > 0:
                this_354.append_safe(', ')
            t_15475 = list_get_15578(values_1895, i_1898)
            append_value_1896(t_15475)
            i_1898 = int_add_15579(i_1898, 1)
    @property
    def accumulated(this_355) -> 'SqlFragment':
        return SqlFragment(tuple_15569(this_355.buffer_1838))
    def __init__(this_607) -> None:
        t_15470: 'MutableSequence45[SqlPart]' = list_15566()
        this_607.buffer_1838 = t_15470
class SqlFragment:
    parts_1905: 'Sequence38[SqlPart]'
    __slots__ = ('parts_1905',)
    def to_source(this_360) -> 'SqlSource':
        return SqlSource(this_360.to_string())
    def to_string(this_361) -> 'str34':
        t_15544: 'int40'
        builder_1910: 'list3[str34]' = ['']
        i_1911: 'int40' = 0
        while True:
            t_15544 = len_15570(this_361.parts_1905)
            if not i_1911 < t_15544:
                break
            list_get_15578(this_361.parts_1905, i_1911).format_to(builder_1910)
            i_1911 = int_add_15579(i_1911, 1)
        return ''.join(builder_1910)
    def __init__(this_628, parts_1913: 'Sequence38[SqlPart]') -> None:
        this_628.parts_1905 = parts_1913
    @property
    def parts(this_2100) -> 'Sequence38[SqlPart]':
        return this_2100.parts_1905
class SqlPart(metaclass = ABCMeta37):
    def format_to(this_362, builder_1915: 'list3[str34]') -> 'None':
        raise RuntimeError39()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_1917: 'str34'
    __slots__ = ('source_1917',)
    def format_to(this_363, builder_1919: 'list3[str34]') -> 'None':
        builder_1919.append(this_363.source_1917)
    def __init__(this_634, source_1922: 'str34') -> None:
        this_634.source_1917 = source_1922
    @property
    def source(this_2097) -> 'str34':
        return this_2097.source_1917
class SqlBoolean(SqlPart):
    value_1923: 'bool42'
    __slots__ = ('value_1923',)
    def format_to(this_364, builder_1925: 'list3[str34]') -> 'None':
        t_8850: 'str34'
        if this_364.value_1923:
            t_8850 = 'TRUE'
        else:
            t_8850 = 'FALSE'
        builder_1925.append(t_8850)
    def __init__(this_637, value_1928: 'bool42') -> None:
        this_637.value_1923 = value_1928
    @property
    def value(this_2103) -> 'bool42':
        return this_2103.value_1923
class SqlDate(SqlPart):
    value_1929: 'date33'
    __slots__ = ('value_1929',)
    def format_to(this_365, builder_1931: 'list3[str34]') -> 'None':
        builder_1931.append("'")
        t_15525: 'str34' = date_to_string_15599(this_365.value_1929)
        def fn_15523(c_1933: 'int40') -> 'None':
            if c_1933 == 39:
                builder_1931.append("''")
            else:
                builder_1931.append(string_from_code_point51(c_1933))
        string_for_each_15601(t_15525, fn_15523)
        builder_1931.append("'")
    def __init__(this_640, value_1935: 'date33') -> None:
        this_640.value_1929 = value_1935
    @property
    def value(this_2118) -> 'date33':
        return this_2118.value_1929
class SqlFloat64(SqlPart):
    value_1936: 'float36'
    __slots__ = ('value_1936',)
    def format_to(this_366, builder_1938: 'list3[str34]') -> 'None':
        t_8839: 'bool42'
        t_8840: 'bool42'
        s_1940: 'str34' = float64_to_string_15581(this_366.value_1936)
        if s_1940 == 'NaN':
            t_8840 = True
        else:
            if s_1940 == 'Infinity':
                t_8839 = True
            else:
                t_8839 = s_1940 == '-Infinity'
            t_8840 = t_8839
        if t_8840:
            builder_1938.append('NULL')
        else:
            builder_1938.append(s_1940)
    def __init__(this_643, value_1942: 'float36') -> None:
        this_643.value_1936 = value_1942
    @property
    def value(this_2115) -> 'float36':
        return this_2115.value_1936
class SqlInt32(SqlPart):
    value_1943: 'int40'
    __slots__ = ('value_1943',)
    def format_to(this_367, builder_1945: 'list3[str34]') -> 'None':
        t_15534: 'str34' = int_to_string_15573(this_367.value_1943)
        builder_1945.append(t_15534)
    def __init__(this_646, value_1948: 'int40') -> None:
        this_646.value_1943 = value_1948
    @property
    def value(this_2109) -> 'int40':
        return this_2109.value_1943
class SqlInt64(SqlPart):
    value_1949: 'int64_23'
    __slots__ = ('value_1949',)
    def format_to(this_368, builder_1951: 'list3[str34]') -> 'None':
        t_15532: 'str34' = int_to_string_15573(this_368.value_1949)
        builder_1951.append(t_15532)
    def __init__(this_649, value_1954: 'int64_23') -> None:
        this_649.value_1949 = value_1954
    @property
    def value(this_2112) -> 'int64_23':
        return this_2112.value_1949
class SqlDefault(SqlPart):
    '`SqlDefault` renders the literal SQL keyword `DEFAULT`, used for columns\nwith server-side default values (e.g., `NOW()` for timestamps).'
    __slots__ = ()
    def format_to(this_369, builder_1956: 'list3[str34]') -> 'None':
        builder_1956.append('DEFAULT')
    def __init__(this_652) -> None:
        pass
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_1959: 'str34'
    __slots__ = ('value_1959',)
    def format_to(this_370, builder_1961: 'list3[str34]') -> 'None':
        builder_1961.append("'")
        def fn_15537(c_1963: 'int40') -> 'None':
            if c_1963 == 39:
                builder_1961.append("''")
            else:
                builder_1961.append(string_from_code_point51(c_1963))
        string_for_each_15601(this_370.value_1959, fn_15537)
        builder_1961.append("'")
    def __init__(this_655, value_1965: 'str34') -> None:
        this_655.value_1959 = value_1965
    @property
    def value(this_2106) -> 'str34':
        return this_2106.value_1959
def changeset(table_def_950: 'TableDef', params_951: 'MappingProxyType41[str34, str34]') -> 'Changeset':
    t_15116: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
    return ChangesetImpl_249(table_def_950, params_951, t_15116, (), True)
def is_ident_start_663(c_1768: 'int40') -> 'bool42':
    return_581: 'bool42'
    t_8366: 'bool42'
    t_8367: 'bool42'
    if c_1768 >= 97:
        t_8366 = c_1768 <= 122
    else:
        t_8366 = False
    if t_8366:
        return_581 = True
    else:
        if c_1768 >= 65:
            t_8367 = c_1768 <= 90
        else:
            t_8367 = False
        if t_8367:
            return_581 = True
        else:
            return_581 = c_1768 == 95
    return return_581
def is_ident_part_664(c_1770: 'int40') -> 'bool42':
    return_582: 'bool42'
    if is_ident_start_663(c_1770):
        return_582 = True
    elif c_1770 >= 48:
        return_582 = c_1770 <= 57
    else:
        return_582 = False
    return return_582
def safe_identifier(name_1772: 'str34') -> 'SafeIdentifier':
    t_15114: 'int40'
    if not name_1772:
        raise RuntimeError39()
    idx_1774: 'int40' = 0
    if not is_ident_start_663(string_get_15592(name_1772, idx_1774)):
        raise RuntimeError39()
    t_15111: 'int40' = string_next_15590(name_1772, idx_1774)
    idx_1774 = t_15111
    while True:
        if not len6(name_1772) > idx_1774:
            break
        if not is_ident_part_664(string_get_15592(name_1772, idx_1774)):
            raise RuntimeError39()
        t_15114 = string_next_15590(name_1772, idx_1774)
        idx_1774 = t_15114
    return ValidatedIdentifier_334(name_1772)
def timestamps() -> 'Sequence38[FieldDef]':
    t_7625: 'SafeIdentifier'
    t_7625 = safe_identifier('inserted_at')
    t_14213: 'FieldDef' = FieldDef(t_7625, DateField(), True, SqlDefault(), False)
    t_7629: 'SafeIdentifier'
    t_7629 = safe_identifier('updated_at')
    return (t_14213, FieldDef(t_7629, DateField(), True, SqlDefault(), False))
def delete_sql(table_def_1193: 'TableDef', id_1194: 'int40') -> 'SqlFragment':
    b_1196: 'SqlBuilder' = SqlBuilder()
    b_1196.append_safe('DELETE FROM ')
    b_1196.append_safe(table_def_1193.table_name.sql_value)
    b_1196.append_safe(' WHERE ')
    b_1196.append_safe(table_def_1193.pk_name())
    b_1196.append_safe(' = ')
    b_1196.append_int32(id_1194)
    return b_1196.accumulated
def from_(table_name_1428: 'SafeIdentifier') -> 'Query':
    return Query(table_name_1428, (), (), (), None, None, (), (), (), False, (), None)
def col(table_1430: 'SafeIdentifier', column_1431: 'SafeIdentifier') -> 'SqlFragment':
    b_1433: 'SqlBuilder' = SqlBuilder()
    b_1433.append_safe(table_1430.sql_value)
    b_1433.append_safe('.')
    b_1433.append_safe(column_1431.sql_value)
    return b_1433.accumulated
def count_all() -> 'SqlFragment':
    b_1435: 'SqlBuilder' = SqlBuilder()
    b_1435.append_safe('COUNT(*)')
    return b_1435.accumulated
def count_col(field_1436: 'SafeIdentifier') -> 'SqlFragment':
    b_1438: 'SqlBuilder' = SqlBuilder()
    b_1438.append_safe('COUNT(')
    b_1438.append_safe(field_1436.sql_value)
    b_1438.append_safe(')')
    return b_1438.accumulated
def sum_col(field_1439: 'SafeIdentifier') -> 'SqlFragment':
    b_1441: 'SqlBuilder' = SqlBuilder()
    b_1441.append_safe('SUM(')
    b_1441.append_safe(field_1439.sql_value)
    b_1441.append_safe(')')
    return b_1441.accumulated
def avg_col(field_1442: 'SafeIdentifier') -> 'SqlFragment':
    b_1444: 'SqlBuilder' = SqlBuilder()
    b_1444.append_safe('AVG(')
    b_1444.append_safe(field_1442.sql_value)
    b_1444.append_safe(')')
    return b_1444.accumulated
def min_col(field_1445: 'SafeIdentifier') -> 'SqlFragment':
    b_1447: 'SqlBuilder' = SqlBuilder()
    b_1447.append_safe('MIN(')
    b_1447.append_safe(field_1445.sql_value)
    b_1447.append_safe(')')
    return b_1447.accumulated
def max_col(field_1448: 'SafeIdentifier') -> 'SqlFragment':
    b_1450: 'SqlBuilder' = SqlBuilder()
    b_1450.append_safe('MAX(')
    b_1450.append_safe(field_1448.sql_value)
    b_1450.append_safe(')')
    return b_1450.accumulated
def union_sql(a_1451: 'Query', b_1452: 'Query') -> 'SqlFragment':
    sb_1454: 'SqlBuilder' = SqlBuilder()
    sb_1454.append_safe('(')
    sb_1454.append_fragment(a_1451.to_sql())
    sb_1454.append_safe(') UNION (')
    sb_1454.append_fragment(b_1452.to_sql())
    sb_1454.append_safe(')')
    return sb_1454.accumulated
def union_all_sql(a_1455: 'Query', b_1456: 'Query') -> 'SqlFragment':
    sb_1458: 'SqlBuilder' = SqlBuilder()
    sb_1458.append_safe('(')
    sb_1458.append_fragment(a_1455.to_sql())
    sb_1458.append_safe(') UNION ALL (')
    sb_1458.append_fragment(b_1456.to_sql())
    sb_1458.append_safe(')')
    return sb_1458.accumulated
def intersect_sql(a_1459: 'Query', b_1460: 'Query') -> 'SqlFragment':
    sb_1462: 'SqlBuilder' = SqlBuilder()
    sb_1462.append_safe('(')
    sb_1462.append_fragment(a_1459.to_sql())
    sb_1462.append_safe(') INTERSECT (')
    sb_1462.append_fragment(b_1460.to_sql())
    sb_1462.append_safe(')')
    return sb_1462.accumulated
def except_sql(a_1463: 'Query', b_1464: 'Query') -> 'SqlFragment':
    sb_1466: 'SqlBuilder' = SqlBuilder()
    sb_1466.append_safe('(')
    sb_1466.append_fragment(a_1463.to_sql())
    sb_1466.append_safe(') EXCEPT (')
    sb_1466.append_fragment(b_1464.to_sql())
    sb_1466.append_safe(')')
    return sb_1466.accumulated
def subquery(q_1467: 'Query', alias_1468: 'SafeIdentifier') -> 'SqlFragment':
    b_1470: 'SqlBuilder' = SqlBuilder()
    b_1470.append_safe('(')
    b_1470.append_fragment(q_1467.to_sql())
    b_1470.append_safe(') AS ')
    b_1470.append_safe(alias_1468.sql_value)
    return b_1470.accumulated
def exists_sql(q_1471: 'Query') -> 'SqlFragment':
    b_1473: 'SqlBuilder' = SqlBuilder()
    b_1473.append_safe('EXISTS (')
    b_1473.append_fragment(q_1471.to_sql())
    b_1473.append_safe(')')
    return b_1473.accumulated
def update(table_name_1533: 'SafeIdentifier') -> 'UpdateQuery':
    return UpdateQuery(table_name_1533, (), (), None)
def delete_from(table_name_1535: 'SafeIdentifier') -> 'DeleteQuery':
    return DeleteQuery(table_name_1535, (), None)
