from builtins import str as str34, float as float36, RuntimeError as RuntimeError39, int as int40, bool as bool42, Exception as Exception46, len as len6, isinstance as isinstance47, list as list3, tuple as tuple5
from typing import Union as Union35, Sequence as Sequence38, Dict as Dict43, MutableSequence as MutableSequence45, Any as Any48, TypeVar as TypeVar49, Callable as Callable50
from abc import ABCMeta as ABCMeta37
from types import MappingProxyType as MappingProxyType41
from temper_core import Label as Label44, Pair as Pair32, string_from_code_point as string_from_code_point51, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, mapped_to_list as mapped_to_list13, list_get as list_get14, int_add as int_add15, float_gt as float_gt16, float64_to_string as float64_to_string17, float_lt as float_lt18, float_gt_eq as float_gt_eq19, float_lt_eq as float_lt_eq20, float_eq as float_eq21, require_string_index as require_string_index22, int_sub as int_sub23, string_next as string_next24, string_get as string_get25, date_from_iso_string as date_from_iso_string26, list_join as list_join27, list_builder_add_all as list_builder_add_all28, date_to_string as date_to_string29, string_for_each as string_for_each30, map_constructor as map_constructor31
from datetime import date as date33
map_builder_set_14289 = map_builder_set0
list_for_each_14290 = list_for_each1
mapped_to_map_14291 = mapped_to_map2
list_14292 = list3
mapped_has_14293 = mapped_has4
tuple_14295 = tuple5
len_14296 = len6
string_count_between_14297 = string_count_between7
str_cat_14298 = str_cat8
int_to_string_14299 = int_to_string9
string_to_int32_14300 = string_to_int3210
string_to_int64_14301 = string_to_int6411
string_to_float64_14302 = string_to_float6412
mapped_to_list_14303 = mapped_to_list13
list_get_14304 = list_get14
int_add_14305 = int_add15
float_gt_14306 = float_gt16
float64_to_string_14307 = float64_to_string17
float_lt_14308 = float_lt18
float_gt_eq_14309 = float_gt_eq19
float_lt_eq_14310 = float_lt_eq20
float_eq_14311 = float_eq21
require_string_index_14314 = require_string_index22
int_sub_14315 = int_sub23
string_next_14316 = string_next24
string_get_14318 = string_get25
date_from_iso_string_14319 = date_from_iso_string26
list_join_14320 = list_join27
list_builder_add_all_14321 = list_builder_add_all28
date_to_string_14325 = date_to_string29
string_for_each_14327 = string_for_each30
map_constructor_14328 = map_constructor31
pair_14329 = Pair32
date_14330 = date33
class ChangesetError:
    field_643: 'str34'
    message_644: 'str34'
    __slots__ = ('field_643', 'message_644')
    def __init__(this_354, field_646: 'str34', message_647: 'str34') -> None:
        this_354.field_643 = field_646
        this_354.message_644 = message_647
    @property
    def field(this_1950) -> 'str34':
        return this_1950.field_643
    @property
    def message(this_1953) -> 'str34':
        return this_1953.message_644
class NumberValidationOpts:
    greater_than_648: 'Union35[float36, None]'
    less_than_649: 'Union35[float36, None]'
    greater_than_or_equal_650: 'Union35[float36, None]'
    less_than_or_equal_651: 'Union35[float36, None]'
    equal_to_652: 'Union35[float36, None]'
    __slots__ = ('greater_than_648', 'less_than_649', 'greater_than_or_equal_650', 'less_than_or_equal_651', 'equal_to_652')
    def __init__(this_356, greater_than_654: 'Union35[float36, None]', less_than_655: 'Union35[float36, None]', greater_than_or_equal_656: 'Union35[float36, None]', less_than_or_equal_657: 'Union35[float36, None]', equal_to_658: 'Union35[float36, None]') -> None:
        this_356.greater_than_648 = greater_than_654
        this_356.less_than_649 = less_than_655
        this_356.greater_than_or_equal_650 = greater_than_or_equal_656
        this_356.less_than_or_equal_651 = less_than_or_equal_657
        this_356.equal_to_652 = equal_to_658
    @property
    def greater_than(this_1956) -> 'Union35[float36, None]':
        return this_1956.greater_than_648
    @property
    def less_than(this_1959) -> 'Union35[float36, None]':
        return this_1959.less_than_649
    @property
    def greater_than_or_equal(this_1962) -> 'Union35[float36, None]':
        return this_1962.greater_than_or_equal_650
    @property
    def less_than_or_equal(this_1965) -> 'Union35[float36, None]':
        return this_1965.less_than_or_equal_651
    @property
    def equal_to(this_1968) -> 'Union35[float36, None]':
        return this_1968.equal_to_652
class Changeset(metaclass = ABCMeta37):
    def cast(this_214, allowed_fields_668: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError39()
    def validate_required(this_215, fields_671: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError39()
    def validate_length(this_216, field_674: 'SafeIdentifier', min_675: 'int40', max_676: 'int40') -> 'Changeset':
        raise RuntimeError39()
    def validate_int(this_217, field_679: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_int64(this_218, field_682: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_float(this_219, field_685: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_bool(this_220, field_688: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def put_change(this_221, field_691: 'SafeIdentifier', value_692: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def get_change(this_222, field_695: 'SafeIdentifier') -> 'str34':
        raise RuntimeError39()
    def delete_change(this_223, field_698: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_inclusion(this_224, field_701: 'SafeIdentifier', allowed_702: 'Sequence38[str34]') -> 'Changeset':
        raise RuntimeError39()
    def validate_exclusion(this_225, field_705: 'SafeIdentifier', disallowed_706: 'Sequence38[str34]') -> 'Changeset':
        raise RuntimeError39()
    def validate_number(this_226, field_709: 'SafeIdentifier', opts_710: 'NumberValidationOpts') -> 'Changeset':
        raise RuntimeError39()
    def validate_acceptance(this_227, field_713: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_confirmation(this_228, field_716: 'SafeIdentifier', confirmation_field_717: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_contains(this_229, field_720: 'SafeIdentifier', substring_721: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def validate_starts_with(this_230, field_724: 'SafeIdentifier', prefix_725: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def validate_ends_with(this_231, field_728: 'SafeIdentifier', suffix_729: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def to_insert_sql(this_232) -> 'SqlFragment':
        raise RuntimeError39()
    def to_update_sql(this_233, id_734: 'int40') -> 'SqlFragment':
        raise RuntimeError39()
class ChangesetImpl_234(Changeset):
    table_def_736: 'TableDef'
    params_737: 'MappingProxyType41[str34, str34]'
    changes_738: 'MappingProxyType41[str34, str34]'
    errors_739: 'Sequence38[ChangesetError]'
    is_valid_740: 'bool42'
    __slots__ = ('table_def_736', 'params_737', 'changes_738', 'errors_739', 'is_valid_740')
    @property
    def table_def(this_235) -> 'TableDef':
        return this_235.table_def_736
    @property
    def changes(this_236) -> 'MappingProxyType41[str34, str34]':
        return this_236.changes_738
    @property
    def errors(this_237) -> 'Sequence38[ChangesetError]':
        return this_237.errors_739
    @property
    def is_valid(this_238) -> 'bool42':
        return this_238.is_valid_740
    def cast(this_239, allowed_fields_750: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        mb_752: 'Dict43[str34, str34]' = {}
        def fn_14193(f_753: 'SafeIdentifier') -> 'None':
            t_14191: 'str34'
            t_14188: 'str34' = f_753.sql_value
            val_754: 'str34' = this_239.params_737.get(t_14188, '')
            if not (not val_754):
                t_14191 = f_753.sql_value
                map_builder_set_14289(mb_752, t_14191, val_754)
        list_for_each_14290(allowed_fields_750, fn_14193)
        return ChangesetImpl_234(this_239.table_def_736, this_239.params_737, mapped_to_map_14291(mb_752), this_239.errors_739, this_239.is_valid_740)
    def validate_required(this_240, fields_756: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        return_405: 'Changeset'
        t_14186: 'Sequence38[ChangesetError]'
        t_8102: 'TableDef'
        t_8103: 'MappingProxyType41[str34, str34]'
        t_8104: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_757:
            if not this_240.is_valid_740:
                return_405 = this_240
                fn_757.break_()
            eb_758: 'MutableSequence45[ChangesetError]' = list_14292(this_240.errors_739)
            valid_759: 'bool42' = True
            def fn_14182(f_760: 'SafeIdentifier') -> 'None':
                nonlocal valid_759
                t_14180: 'ChangesetError'
                t_14177: 'str34' = f_760.sql_value
                if not mapped_has_14293(this_240.changes_738, t_14177):
                    t_14180 = ChangesetError(f_760.sql_value, 'is required')
                    eb_758.append(t_14180)
                    valid_759 = False
            list_for_each_14290(fields_756, fn_14182)
            t_8102 = this_240.table_def_736
            t_8103 = this_240.params_737
            t_8104 = this_240.changes_738
            t_14186 = tuple_14295(eb_758)
            return_405 = ChangesetImpl_234(t_8102, t_8103, t_8104, t_14186, valid_759)
        return return_405
    def validate_length(this_241, field_762: 'SafeIdentifier', min_763: 'int40', max_764: 'int40') -> 'Changeset':
        return_406: 'Changeset'
        t_14164: 'str34'
        t_14175: 'Sequence38[ChangesetError]'
        t_8085: 'bool42'
        t_8091: 'TableDef'
        t_8092: 'MappingProxyType41[str34, str34]'
        t_8093: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_765:
            if not this_241.is_valid_740:
                return_406 = this_241
                fn_765.break_()
            t_14164 = field_762.sql_value
            val_766: 'str34' = this_241.changes_738.get(t_14164, '')
            len_767: 'int40' = string_count_between_14297(val_766, 0, len_14296(val_766))
            if len_767 < min_763:
                t_8085 = True
            else:
                t_8085 = len_767 > max_764
            if t_8085:
                msg_768: 'str34' = str_cat_14298('must be between ', int_to_string_14299(min_763), ' and ', int_to_string_14299(max_764), ' characters')
                eb_769: 'MutableSequence45[ChangesetError]' = list_14292(this_241.errors_739)
                eb_769.append(ChangesetError(field_762.sql_value, msg_768))
                t_8091 = this_241.table_def_736
                t_8092 = this_241.params_737
                t_8093 = this_241.changes_738
                t_14175 = tuple_14295(eb_769)
                return_406 = ChangesetImpl_234(t_8091, t_8092, t_8093, t_14175, False)
                fn_765.break_()
            return_406 = this_241
        return return_406
    def validate_int(this_242, field_771: 'SafeIdentifier') -> 'Changeset':
        return_407: 'Changeset'
        t_14155: 'str34'
        t_14162: 'Sequence38[ChangesetError]'
        t_8076: 'TableDef'
        t_8077: 'MappingProxyType41[str34, str34]'
        t_8078: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_772:
            if not this_242.is_valid_740:
                return_407 = this_242
                fn_772.break_()
            t_14155 = field_771.sql_value
            val_773: 'str34' = this_242.changes_738.get(t_14155, '')
            if not val_773:
                return_407 = this_242
                fn_772.break_()
            parse_ok_774: 'bool42'
            try:
                string_to_int32_14300(val_773)
                parse_ok_774 = True
            except Exception46:
                parse_ok_774 = False
            if not parse_ok_774:
                eb_775: 'MutableSequence45[ChangesetError]' = list_14292(this_242.errors_739)
                eb_775.append(ChangesetError(field_771.sql_value, 'must be an integer'))
                t_8076 = this_242.table_def_736
                t_8077 = this_242.params_737
                t_8078 = this_242.changes_738
                t_14162 = tuple_14295(eb_775)
                return_407 = ChangesetImpl_234(t_8076, t_8077, t_8078, t_14162, False)
                fn_772.break_()
            return_407 = this_242
        return return_407
    def validate_int64(this_243, field_777: 'SafeIdentifier') -> 'Changeset':
        return_408: 'Changeset'
        t_14146: 'str34'
        t_14153: 'Sequence38[ChangesetError]'
        t_8063: 'TableDef'
        t_8064: 'MappingProxyType41[str34, str34]'
        t_8065: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_778:
            if not this_243.is_valid_740:
                return_408 = this_243
                fn_778.break_()
            t_14146 = field_777.sql_value
            val_779: 'str34' = this_243.changes_738.get(t_14146, '')
            if not val_779:
                return_408 = this_243
                fn_778.break_()
            parse_ok_780: 'bool42'
            try:
                string_to_int64_14301(val_779)
                parse_ok_780 = True
            except Exception46:
                parse_ok_780 = False
            if not parse_ok_780:
                eb_781: 'MutableSequence45[ChangesetError]' = list_14292(this_243.errors_739)
                eb_781.append(ChangesetError(field_777.sql_value, 'must be a 64-bit integer'))
                t_8063 = this_243.table_def_736
                t_8064 = this_243.params_737
                t_8065 = this_243.changes_738
                t_14153 = tuple_14295(eb_781)
                return_408 = ChangesetImpl_234(t_8063, t_8064, t_8065, t_14153, False)
                fn_778.break_()
            return_408 = this_243
        return return_408
    def validate_float(this_244, field_783: 'SafeIdentifier') -> 'Changeset':
        return_409: 'Changeset'
        t_14137: 'str34'
        t_14144: 'Sequence38[ChangesetError]'
        t_8050: 'TableDef'
        t_8051: 'MappingProxyType41[str34, str34]'
        t_8052: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_784:
            if not this_244.is_valid_740:
                return_409 = this_244
                fn_784.break_()
            t_14137 = field_783.sql_value
            val_785: 'str34' = this_244.changes_738.get(t_14137, '')
            if not val_785:
                return_409 = this_244
                fn_784.break_()
            parse_ok_786: 'bool42'
            try:
                string_to_float64_14302(val_785)
                parse_ok_786 = True
            except Exception46:
                parse_ok_786 = False
            if not parse_ok_786:
                eb_787: 'MutableSequence45[ChangesetError]' = list_14292(this_244.errors_739)
                eb_787.append(ChangesetError(field_783.sql_value, 'must be a number'))
                t_8050 = this_244.table_def_736
                t_8051 = this_244.params_737
                t_8052 = this_244.changes_738
                t_14144 = tuple_14295(eb_787)
                return_409 = ChangesetImpl_234(t_8050, t_8051, t_8052, t_14144, False)
                fn_784.break_()
            return_409 = this_244
        return return_409
    def validate_bool(this_245, field_789: 'SafeIdentifier') -> 'Changeset':
        return_410: 'Changeset'
        t_14128: 'str34'
        t_14135: 'Sequence38[ChangesetError]'
        t_8025: 'bool42'
        t_8026: 'bool42'
        t_8028: 'bool42'
        t_8029: 'bool42'
        t_8031: 'bool42'
        t_8037: 'TableDef'
        t_8038: 'MappingProxyType41[str34, str34]'
        t_8039: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_790:
            if not this_245.is_valid_740:
                return_410 = this_245
                fn_790.break_()
            t_14128 = field_789.sql_value
            val_791: 'str34' = this_245.changes_738.get(t_14128, '')
            if not val_791:
                return_410 = this_245
                fn_790.break_()
            is_true_792: 'bool42'
            if val_791 == 'true':
                is_true_792 = True
            else:
                if val_791 == '1':
                    t_8026 = True
                else:
                    if val_791 == 'yes':
                        t_8025 = True
                    else:
                        t_8025 = val_791 == 'on'
                    t_8026 = t_8025
                is_true_792 = t_8026
            is_false_793: 'bool42'
            if val_791 == 'false':
                is_false_793 = True
            else:
                if val_791 == '0':
                    t_8029 = True
                else:
                    if val_791 == 'no':
                        t_8028 = True
                    else:
                        t_8028 = val_791 == 'off'
                    t_8029 = t_8028
                is_false_793 = t_8029
            if not is_true_792:
                t_8031 = not is_false_793
            else:
                t_8031 = False
            if t_8031:
                eb_794: 'MutableSequence45[ChangesetError]' = list_14292(this_245.errors_739)
                eb_794.append(ChangesetError(field_789.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_8037 = this_245.table_def_736
                t_8038 = this_245.params_737
                t_8039 = this_245.changes_738
                t_14135 = tuple_14295(eb_794)
                return_410 = ChangesetImpl_234(t_8037, t_8038, t_8039, t_14135, False)
                fn_790.break_()
            return_410 = this_245
        return return_410
    def put_change(this_246, field_796: 'SafeIdentifier', value_797: 'str34') -> 'Changeset':
        t_14116: 'int40'
        mb_799: 'Dict43[str34, str34]' = {}
        pairs_800: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_14303(this_246.changes_738)
        i_801: 'int40' = 0
        while True:
            t_14116 = len_14296(pairs_800)
            if not i_801 < t_14116:
                break
            map_builder_set_14289(mb_799, list_get_14304(pairs_800, i_801).key, list_get_14304(pairs_800, i_801).value)
            i_801 = int_add_14305(i_801, 1)
        map_builder_set_14289(mb_799, field_796.sql_value, value_797)
        return ChangesetImpl_234(this_246.table_def_736, this_246.params_737, mapped_to_map_14291(mb_799), this_246.errors_739, this_246.is_valid_740)
    def get_change(this_247, field_803: 'SafeIdentifier') -> 'str34':
        t_14110: 'str34' = field_803.sql_value
        if not mapped_has_14293(this_247.changes_738, t_14110):
            raise RuntimeError39()
        t_14112: 'str34' = field_803.sql_value
        return this_247.changes_738.get(t_14112, '')
    def delete_change(this_248, field_806: 'SafeIdentifier') -> 'Changeset':
        t_14097: 'int40'
        mb_808: 'Dict43[str34, str34]' = {}
        pairs_809: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_14303(this_248.changes_738)
        i_810: 'int40' = 0
        while True:
            t_14097 = len_14296(pairs_809)
            if not i_810 < t_14097:
                break
            if list_get_14304(pairs_809, i_810).key != field_806.sql_value:
                map_builder_set_14289(mb_808, list_get_14304(pairs_809, i_810).key, list_get_14304(pairs_809, i_810).value)
            i_810 = int_add_14305(i_810, 1)
        return ChangesetImpl_234(this_248.table_def_736, this_248.params_737, mapped_to_map_14291(mb_808), this_248.errors_739, this_248.is_valid_740)
    def validate_inclusion(this_249, field_812: 'SafeIdentifier', allowed_813: 'Sequence38[str34]') -> 'Changeset':
        return_414: 'Changeset'
        t_14083: 'str34'
        t_14085: 'str34'
        t_14093: 'Sequence38[ChangesetError]'
        t_7987: 'TableDef'
        t_7988: 'MappingProxyType41[str34, str34]'
        t_7989: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_814:
            if not this_249.is_valid_740:
                return_414 = this_249
                fn_814.break_()
            t_14083 = field_812.sql_value
            if not mapped_has_14293(this_249.changes_738, t_14083):
                return_414 = this_249
                fn_814.break_()
            t_14085 = field_812.sql_value
            val_815: 'str34' = this_249.changes_738.get(t_14085, '')
            found_816: 'bool42' = False
            def fn_14082(a_817: 'str34') -> 'None':
                nonlocal found_816
                if a_817 == val_815:
                    found_816 = True
            list_for_each_14290(allowed_813, fn_14082)
            if not found_816:
                eb_818: 'MutableSequence45[ChangesetError]' = list_14292(this_249.errors_739)
                eb_818.append(ChangesetError(field_812.sql_value, 'is not included in the list'))
                t_7987 = this_249.table_def_736
                t_7988 = this_249.params_737
                t_7989 = this_249.changes_738
                t_14093 = tuple_14295(eb_818)
                return_414 = ChangesetImpl_234(t_7987, t_7988, t_7989, t_14093, False)
                fn_814.break_()
            return_414 = this_249
        return return_414
    def validate_exclusion(this_250, field_820: 'SafeIdentifier', disallowed_821: 'Sequence38[str34]') -> 'Changeset':
        return_415: 'Changeset'
        t_14070: 'str34'
        t_14072: 'str34'
        t_14080: 'Sequence38[ChangesetError]'
        t_7973: 'TableDef'
        t_7974: 'MappingProxyType41[str34, str34]'
        t_7975: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_822:
            if not this_250.is_valid_740:
                return_415 = this_250
                fn_822.break_()
            t_14070 = field_820.sql_value
            if not mapped_has_14293(this_250.changes_738, t_14070):
                return_415 = this_250
                fn_822.break_()
            t_14072 = field_820.sql_value
            val_823: 'str34' = this_250.changes_738.get(t_14072, '')
            found_824: 'bool42' = False
            def fn_14069(d_825: 'str34') -> 'None':
                nonlocal found_824
                if d_825 == val_823:
                    found_824 = True
            list_for_each_14290(disallowed_821, fn_14069)
            if found_824:
                eb_826: 'MutableSequence45[ChangesetError]' = list_14292(this_250.errors_739)
                eb_826.append(ChangesetError(field_820.sql_value, 'is reserved'))
                t_7973 = this_250.table_def_736
                t_7974 = this_250.params_737
                t_7975 = this_250.changes_738
                t_14080 = tuple_14295(eb_826)
                return_415 = ChangesetImpl_234(t_7973, t_7974, t_7975, t_14080, False)
                fn_822.break_()
            return_415 = this_250
        return return_415
    def validate_number(this_251, field_828: 'SafeIdentifier', opts_829: 'NumberValidationOpts') -> 'Changeset':
        return_416: 'Changeset'
        t_14019: 'str34'
        t_14021: 'str34'
        t_14027: 'Sequence38[ChangesetError]'
        t_14035: 'Sequence38[ChangesetError]'
        t_14043: 'Sequence38[ChangesetError]'
        t_14051: 'Sequence38[ChangesetError]'
        t_14059: 'Sequence38[ChangesetError]'
        t_14067: 'Sequence38[ChangesetError]'
        t_7906: 'TableDef'
        t_7907: 'MappingProxyType41[str34, str34]'
        t_7908: 'MappingProxyType41[str34, str34]'
        t_7910: 'float36'
        t_7919: 'TableDef'
        t_7920: 'MappingProxyType41[str34, str34]'
        t_7921: 'MappingProxyType41[str34, str34]'
        t_7929: 'TableDef'
        t_7930: 'MappingProxyType41[str34, str34]'
        t_7931: 'MappingProxyType41[str34, str34]'
        t_7939: 'TableDef'
        t_7940: 'MappingProxyType41[str34, str34]'
        t_7941: 'MappingProxyType41[str34, str34]'
        t_7949: 'TableDef'
        t_7950: 'MappingProxyType41[str34, str34]'
        t_7951: 'MappingProxyType41[str34, str34]'
        t_7959: 'TableDef'
        t_7960: 'MappingProxyType41[str34, str34]'
        t_7961: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_830:
            if not this_251.is_valid_740:
                return_416 = this_251
                fn_830.break_()
            t_14019 = field_828.sql_value
            if not mapped_has_14293(this_251.changes_738, t_14019):
                return_416 = this_251
                fn_830.break_()
            t_14021 = field_828.sql_value
            val_831: 'str34' = this_251.changes_738.get(t_14021, '')
            parse_ok_832: 'bool42'
            try:
                string_to_float64_14302(val_831)
                parse_ok_832 = True
            except Exception46:
                parse_ok_832 = False
            if not parse_ok_832:
                eb_833: 'MutableSequence45[ChangesetError]' = list_14292(this_251.errors_739)
                eb_833.append(ChangesetError(field_828.sql_value, 'must be a number'))
                t_7906 = this_251.table_def_736
                t_7907 = this_251.params_737
                t_7908 = this_251.changes_738
                t_14027 = tuple_14295(eb_833)
                return_416 = ChangesetImpl_234(t_7906, t_7907, t_7908, t_14027, False)
                fn_830.break_()
            num_834: 'float36'
            try:
                t_7910 = string_to_float64_14302(val_831)
                num_834 = t_7910
            except Exception46:
                num_834 = 0.0
            gt_835: 'Union35[float36, None]' = opts_829.greater_than
            if not gt_835 is None:
                gt_2466: 'float36' = gt_835
                if not float_gt_14306(num_834, gt_2466):
                    eb_836: 'MutableSequence45[ChangesetError]' = list_14292(this_251.errors_739)
                    eb_836.append(ChangesetError(field_828.sql_value, str_cat_14298('must be greater than ', float64_to_string_14307(gt_2466))))
                    t_7919 = this_251.table_def_736
                    t_7920 = this_251.params_737
                    t_7921 = this_251.changes_738
                    t_14035 = tuple_14295(eb_836)
                    return_416 = ChangesetImpl_234(t_7919, t_7920, t_7921, t_14035, False)
                    fn_830.break_()
            lt_837: 'Union35[float36, None]' = opts_829.less_than
            if not lt_837 is None:
                lt_2467: 'float36' = lt_837
                if not float_lt_14308(num_834, lt_2467):
                    eb_838: 'MutableSequence45[ChangesetError]' = list_14292(this_251.errors_739)
                    eb_838.append(ChangesetError(field_828.sql_value, str_cat_14298('must be less than ', float64_to_string_14307(lt_2467))))
                    t_7929 = this_251.table_def_736
                    t_7930 = this_251.params_737
                    t_7931 = this_251.changes_738
                    t_14043 = tuple_14295(eb_838)
                    return_416 = ChangesetImpl_234(t_7929, t_7930, t_7931, t_14043, False)
                    fn_830.break_()
            gte_839: 'Union35[float36, None]' = opts_829.greater_than_or_equal
            if not gte_839 is None:
                gte_2468: 'float36' = gte_839
                if not float_gt_eq_14309(num_834, gte_2468):
                    eb_840: 'MutableSequence45[ChangesetError]' = list_14292(this_251.errors_739)
                    eb_840.append(ChangesetError(field_828.sql_value, str_cat_14298('must be greater than or equal to ', float64_to_string_14307(gte_2468))))
                    t_7939 = this_251.table_def_736
                    t_7940 = this_251.params_737
                    t_7941 = this_251.changes_738
                    t_14051 = tuple_14295(eb_840)
                    return_416 = ChangesetImpl_234(t_7939, t_7940, t_7941, t_14051, False)
                    fn_830.break_()
            lte_841: 'Union35[float36, None]' = opts_829.less_than_or_equal
            if not lte_841 is None:
                lte_2469: 'float36' = lte_841
                if not float_lt_eq_14310(num_834, lte_2469):
                    eb_842: 'MutableSequence45[ChangesetError]' = list_14292(this_251.errors_739)
                    eb_842.append(ChangesetError(field_828.sql_value, str_cat_14298('must be less than or equal to ', float64_to_string_14307(lte_2469))))
                    t_7949 = this_251.table_def_736
                    t_7950 = this_251.params_737
                    t_7951 = this_251.changes_738
                    t_14059 = tuple_14295(eb_842)
                    return_416 = ChangesetImpl_234(t_7949, t_7950, t_7951, t_14059, False)
                    fn_830.break_()
            eq_843: 'Union35[float36, None]' = opts_829.equal_to
            if not eq_843 is None:
                eq_2470: 'float36' = eq_843
                if not float_eq_14311(num_834, eq_2470):
                    eb_844: 'MutableSequence45[ChangesetError]' = list_14292(this_251.errors_739)
                    eb_844.append(ChangesetError(field_828.sql_value, str_cat_14298('must be equal to ', float64_to_string_14307(eq_2470))))
                    t_7959 = this_251.table_def_736
                    t_7960 = this_251.params_737
                    t_7961 = this_251.changes_738
                    t_14067 = tuple_14295(eb_844)
                    return_416 = ChangesetImpl_234(t_7959, t_7960, t_7961, t_14067, False)
                    fn_830.break_()
            return_416 = this_251
        return return_416
    def validate_acceptance(this_252, field_846: 'SafeIdentifier') -> 'Changeset':
        return_417: 'Changeset'
        t_14009: 'str34'
        t_14011: 'str34'
        t_14017: 'Sequence38[ChangesetError]'
        t_7884: 'bool42'
        t_7885: 'bool42'
        t_7892: 'TableDef'
        t_7893: 'MappingProxyType41[str34, str34]'
        t_7894: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_847:
            if not this_252.is_valid_740:
                return_417 = this_252
                fn_847.break_()
            t_14009 = field_846.sql_value
            if not mapped_has_14293(this_252.changes_738, t_14009):
                return_417 = this_252
                fn_847.break_()
            t_14011 = field_846.sql_value
            val_848: 'str34' = this_252.changes_738.get(t_14011, '')
            accepted_849: 'bool42'
            if val_848 == 'true':
                accepted_849 = True
            else:
                if val_848 == '1':
                    t_7885 = True
                else:
                    if val_848 == 'yes':
                        t_7884 = True
                    else:
                        t_7884 = val_848 == 'on'
                    t_7885 = t_7884
                accepted_849 = t_7885
            if not accepted_849:
                eb_850: 'MutableSequence45[ChangesetError]' = list_14292(this_252.errors_739)
                eb_850.append(ChangesetError(field_846.sql_value, 'must be accepted'))
                t_7892 = this_252.table_def_736
                t_7893 = this_252.params_737
                t_7894 = this_252.changes_738
                t_14017 = tuple_14295(eb_850)
                return_417 = ChangesetImpl_234(t_7892, t_7893, t_7894, t_14017, False)
                fn_847.break_()
            return_417 = this_252
        return return_417
    def validate_confirmation(this_253, field_852: 'SafeIdentifier', confirmation_field_853: 'SafeIdentifier') -> 'Changeset':
        return_418: 'Changeset'
        t_13997: 'str34'
        t_13999: 'str34'
        t_14001: 'str34'
        t_14007: 'Sequence38[ChangesetError]'
        t_7876: 'TableDef'
        t_7877: 'MappingProxyType41[str34, str34]'
        t_7878: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_854:
            if not this_253.is_valid_740:
                return_418 = this_253
                fn_854.break_()
            t_13997 = field_852.sql_value
            if not mapped_has_14293(this_253.changes_738, t_13997):
                return_418 = this_253
                fn_854.break_()
            t_13999 = field_852.sql_value
            val_855: 'str34' = this_253.changes_738.get(t_13999, '')
            t_14001 = confirmation_field_853.sql_value
            conf_856: 'str34' = this_253.changes_738.get(t_14001, '')
            if val_855 != conf_856:
                eb_857: 'MutableSequence45[ChangesetError]' = list_14292(this_253.errors_739)
                eb_857.append(ChangesetError(confirmation_field_853.sql_value, 'does not match'))
                t_7876 = this_253.table_def_736
                t_7877 = this_253.params_737
                t_7878 = this_253.changes_738
                t_14007 = tuple_14295(eb_857)
                return_418 = ChangesetImpl_234(t_7876, t_7877, t_7878, t_14007, False)
                fn_854.break_()
            return_418 = this_253
        return return_418
    def validate_contains(this_254, field_859: 'SafeIdentifier', substring_860: 'str34') -> 'Changeset':
        return_419: 'Changeset'
        t_13985: 'str34'
        t_13987: 'str34'
        t_13995: 'Sequence38[ChangesetError]'
        t_7861: 'TableDef'
        t_7862: 'MappingProxyType41[str34, str34]'
        t_7863: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_861:
            if not this_254.is_valid_740:
                return_419 = this_254
                fn_861.break_()
            t_13985 = field_859.sql_value
            if not mapped_has_14293(this_254.changes_738, t_13985):
                return_419 = this_254
                fn_861.break_()
            t_13987 = field_859.sql_value
            val_862: 'str34' = this_254.changes_738.get(t_13987, '')
            if not val_862.find(substring_860) >= 0:
                eb_863: 'MutableSequence45[ChangesetError]' = list_14292(this_254.errors_739)
                eb_863.append(ChangesetError(field_859.sql_value, 'must contain the given substring'))
                t_7861 = this_254.table_def_736
                t_7862 = this_254.params_737
                t_7863 = this_254.changes_738
                t_13995 = tuple_14295(eb_863)
                return_419 = ChangesetImpl_234(t_7861, t_7862, t_7863, t_13995, False)
                fn_861.break_()
            return_419 = this_254
        return return_419
    def validate_starts_with(this_255, field_865: 'SafeIdentifier', prefix_866: 'str34') -> 'Changeset':
        return_420: 'Changeset'
        t_13972: 'str34'
        t_13974: 'str34'
        t_13978: 'int40'
        t_13983: 'Sequence38[ChangesetError]'
        t_7845: 'TableDef'
        t_7846: 'MappingProxyType41[str34, str34]'
        t_7847: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_867:
            if not this_255.is_valid_740:
                return_420 = this_255
                fn_867.break_()
            t_13972 = field_865.sql_value
            if not mapped_has_14293(this_255.changes_738, t_13972):
                return_420 = this_255
                fn_867.break_()
            t_13974 = field_865.sql_value
            val_868: 'str34' = this_255.changes_738.get(t_13974, '')
            idx_869: 'int40' = val_868.find(prefix_866)
            starts_870: 'bool42'
            if idx_869 >= 0:
                t_13978 = string_count_between_14297(val_868, 0, require_string_index_14314(idx_869))
                starts_870 = t_13978 == 0
            else:
                starts_870 = False
            if not starts_870:
                eb_871: 'MutableSequence45[ChangesetError]' = list_14292(this_255.errors_739)
                eb_871.append(ChangesetError(field_865.sql_value, 'must start with the given prefix'))
                t_7845 = this_255.table_def_736
                t_7846 = this_255.params_737
                t_7847 = this_255.changes_738
                t_13983 = tuple_14295(eb_871)
                return_420 = ChangesetImpl_234(t_7845, t_7846, t_7847, t_13983, False)
                fn_867.break_()
            return_420 = this_255
        return return_420
    def validate_ends_with(this_256, field_873: 'SafeIdentifier', suffix_874: 'str34') -> 'Changeset':
        return_421: 'Changeset'
        t_13944: 'str34'
        t_13946: 'str34'
        t_13951: 'int40'
        t_13957: 'Sequence38[ChangesetError]'
        t_13959: 'int40'
        t_13960: 'bool42'
        t_13964: 'int40'
        t_13965: 'int40'
        t_13970: 'Sequence38[ChangesetError]'
        t_7810: 'TableDef'
        t_7811: 'MappingProxyType41[str34, str34]'
        t_7812: 'MappingProxyType41[str34, str34]'
        t_7816: 'bool42'
        t_7827: 'TableDef'
        t_7828: 'MappingProxyType41[str34, str34]'
        t_7829: 'MappingProxyType41[str34, str34]'
        with Label44() as fn_875:
            if not this_256.is_valid_740:
                return_421 = this_256
                fn_875.break_()
            t_13944 = field_873.sql_value
            if not mapped_has_14293(this_256.changes_738, t_13944):
                return_421 = this_256
                fn_875.break_()
            t_13946 = field_873.sql_value
            val_876: 'str34' = this_256.changes_738.get(t_13946, '')
            val_len_877: 'int40' = string_count_between_14297(val_876, 0, len_14296(val_876))
            t_13951 = len_14296(suffix_874)
            suffix_len_878: 'int40' = string_count_between_14297(suffix_874, 0, t_13951)
            if val_len_877 < suffix_len_878:
                eb_879: 'MutableSequence45[ChangesetError]' = list_14292(this_256.errors_739)
                eb_879.append(ChangesetError(field_873.sql_value, 'must end with the given suffix'))
                t_7810 = this_256.table_def_736
                t_7811 = this_256.params_737
                t_7812 = this_256.changes_738
                t_13957 = tuple_14295(eb_879)
                return_421 = ChangesetImpl_234(t_7810, t_7811, t_7812, t_13957, False)
                fn_875.break_()
            skip_count_880: 'int40' = int_sub_14315(val_len_877, suffix_len_878)
            str_idx_881: 'int40' = 0
            i_882: 'int40' = 0
            while i_882 < skip_count_880:
                t_13959 = string_next_14316(val_876, str_idx_881)
                str_idx_881 = t_13959
                i_882 = int_add_14305(i_882, 1)
            suf_idx_883: 'int40' = 0
            matches_884: 'bool42' = True
            while True:
                if matches_884:
                    t_13960 = len6(suffix_874) > suf_idx_883
                    t_7816 = t_13960
                else:
                    t_7816 = False
                if not t_7816:
                    break
                if not len6(val_876) > str_idx_881:
                    matches_884 = False
                elif string_get_14318(val_876, str_idx_881) != string_get_14318(suffix_874, suf_idx_883):
                    matches_884 = False
                else:
                    t_13964 = string_next_14316(val_876, str_idx_881)
                    str_idx_881 = t_13964
                    t_13965 = string_next_14316(suffix_874, suf_idx_883)
                    suf_idx_883 = t_13965
            if not matches_884:
                eb_885: 'MutableSequence45[ChangesetError]' = list_14292(this_256.errors_739)
                eb_885.append(ChangesetError(field_873.sql_value, 'must end with the given suffix'))
                t_7827 = this_256.table_def_736
                t_7828 = this_256.params_737
                t_7829 = this_256.changes_738
                t_13970 = tuple_14295(eb_885)
                return_421 = ChangesetImpl_234(t_7827, t_7828, t_7829, t_13970, False)
                fn_875.break_()
            return_421 = this_256
        return return_421
    def parse_bool_sql_part_886(this_257, val_887: 'str34') -> 'SqlBoolean':
        return_422: 'SqlBoolean'
        t_7787: 'bool42'
        t_7788: 'bool42'
        t_7789: 'bool42'
        t_7791: 'bool42'
        t_7792: 'bool42'
        t_7793: 'bool42'
        with Label44() as fn_888:
            if val_887 == 'true':
                t_7789 = True
            else:
                if val_887 == '1':
                    t_7788 = True
                else:
                    if val_887 == 'yes':
                        t_7787 = True
                    else:
                        t_7787 = val_887 == 'on'
                    t_7788 = t_7787
                t_7789 = t_7788
            if t_7789:
                return_422 = SqlBoolean(True)
                fn_888.break_()
            if val_887 == 'false':
                t_7793 = True
            else:
                if val_887 == '0':
                    t_7792 = True
                else:
                    if val_887 == 'no':
                        t_7791 = True
                    else:
                        t_7791 = val_887 == 'off'
                    t_7792 = t_7791
                t_7793 = t_7792
            if t_7793:
                return_422 = SqlBoolean(False)
                fn_888.break_()
            raise RuntimeError39()
        return return_422
    def value_to_sql_part_889(this_258, field_def_890: 'FieldDef', val_891: 'str34') -> 'SqlPart':
        return_423: 'SqlPart'
        t_7774: 'int40'
        t_7777: 'int64_23'
        t_7780: 'float36'
        t_7785: 'date33'
        with Label44() as fn_892:
            ft_893: 'FieldType' = field_def_890.field_type
            if isinstance47(ft_893, StringField):
                return_423 = SqlString(val_891)
                fn_892.break_()
            if isinstance47(ft_893, IntField):
                t_7774 = string_to_int32_14300(val_891)
                return_423 = SqlInt32(t_7774)
                fn_892.break_()
            if isinstance47(ft_893, Int64Field):
                t_7777 = string_to_int64_14301(val_891)
                return_423 = SqlInt64(t_7777)
                fn_892.break_()
            if isinstance47(ft_893, FloatField):
                t_7780 = string_to_float64_14302(val_891)
                return_423 = SqlFloat64(t_7780)
                fn_892.break_()
            if isinstance47(ft_893, BoolField):
                return_423 = this_258.parse_bool_sql_part_886(val_891)
                fn_892.break_()
            if isinstance47(ft_893, DateField):
                t_7785 = date_from_iso_string_14319(val_891)
                return_423 = SqlDate(t_7785)
                fn_892.break_()
            raise RuntimeError39()
        return return_423
    def to_insert_sql(this_259) -> 'SqlFragment':
        t_13892: 'int40'
        t_13897: 'str34'
        t_13898: 'bool42'
        t_13903: 'int40'
        t_13905: 'str34'
        t_13909: 'str34'
        t_13924: 'int40'
        t_7738: 'bool42'
        t_7746: 'FieldDef'
        t_7751: 'SqlPart'
        if not this_259.is_valid_740:
            raise RuntimeError39()
        i_896: 'int40' = 0
        while True:
            t_13892 = len_14296(this_259.table_def_736.fields)
            if not i_896 < t_13892:
                break
            f_897: 'FieldDef' = list_get_14304(this_259.table_def_736.fields, i_896)
            if not f_897.nullable:
                t_13897 = f_897.name.sql_value
                t_13898 = mapped_has_14293(this_259.changes_738, t_13897)
                t_7738 = not t_13898
            else:
                t_7738 = False
            if t_7738:
                raise RuntimeError39()
            i_896 = int_add_14305(i_896, 1)
        pairs_898: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_14303(this_259.changes_738)
        if len_14296(pairs_898) == 0:
            raise RuntimeError39()
        col_names_899: 'MutableSequence45[str34]' = list_14292()
        val_parts_900: 'MutableSequence45[SqlPart]' = list_14292()
        i_901: 'int40' = 0
        while True:
            t_13903 = len_14296(pairs_898)
            if not i_901 < t_13903:
                break
            pair_902: 'Pair32[str34, str34]' = list_get_14304(pairs_898, i_901)
            t_13905 = pair_902.key
            t_7746 = this_259.table_def_736.field(t_13905)
            fd_903: 'FieldDef' = t_7746
            col_names_899.append(fd_903.name.sql_value)
            t_13909 = pair_902.value
            t_7751 = this_259.value_to_sql_part_889(fd_903, t_13909)
            val_parts_900.append(t_7751)
            i_901 = int_add_14305(i_901, 1)
        b_904: 'SqlBuilder' = SqlBuilder()
        b_904.append_safe('INSERT INTO ')
        b_904.append_safe(this_259.table_def_736.table_name.sql_value)
        b_904.append_safe(' (')
        t_13917: 'Sequence38[str34]' = tuple_14295(col_names_899)
        def fn_13890(c_905: 'str34') -> 'str34':
            return c_905
        b_904.append_safe(list_join_14320(t_13917, ', ', fn_13890))
        b_904.append_safe(') VALUES (')
        b_904.append_part(list_get_14304(val_parts_900, 0))
        j_906: 'int40' = 1
        while True:
            t_13924 = len_14296(val_parts_900)
            if not j_906 < t_13924:
                break
            b_904.append_safe(', ')
            b_904.append_part(list_get_14304(val_parts_900, j_906))
            j_906 = int_add_14305(j_906, 1)
        b_904.append_safe(')')
        return b_904.accumulated
    def to_update_sql(this_260, id_908: 'int40') -> 'SqlFragment':
        t_13877: 'int40'
        t_13880: 'str34'
        t_13885: 'str34'
        t_7719: 'FieldDef'
        t_7725: 'SqlPart'
        if not this_260.is_valid_740:
            raise RuntimeError39()
        pairs_910: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_14303(this_260.changes_738)
        if len_14296(pairs_910) == 0:
            raise RuntimeError39()
        b_911: 'SqlBuilder' = SqlBuilder()
        b_911.append_safe('UPDATE ')
        b_911.append_safe(this_260.table_def_736.table_name.sql_value)
        b_911.append_safe(' SET ')
        i_912: 'int40' = 0
        while True:
            t_13877 = len_14296(pairs_910)
            if not i_912 < t_13877:
                break
            if i_912 > 0:
                b_911.append_safe(', ')
            pair_913: 'Pair32[str34, str34]' = list_get_14304(pairs_910, i_912)
            t_13880 = pair_913.key
            t_7719 = this_260.table_def_736.field(t_13880)
            fd_914: 'FieldDef' = t_7719
            b_911.append_safe(fd_914.name.sql_value)
            b_911.append_safe(' = ')
            t_13885 = pair_913.value
            t_7725 = this_260.value_to_sql_part_889(fd_914, t_13885)
            b_911.append_part(t_7725)
            i_912 = int_add_14305(i_912, 1)
        b_911.append_safe(' WHERE id = ')
        b_911.append_int32(id_908)
        return b_911.accumulated
    def __init__(this_395, table_def_916: 'TableDef', params_917: 'MappingProxyType41[str34, str34]', changes_918: 'MappingProxyType41[str34, str34]', errors_919: 'Sequence38[ChangesetError]', is_valid_920: 'bool42') -> None:
        this_395.table_def_736 = table_def_916
        this_395.params_737 = params_917
        this_395.changes_738 = changes_918
        this_395.errors_739 = errors_919
        this_395.is_valid_740 = is_valid_920
class JoinType(metaclass = ABCMeta37):
    def keyword(this_261) -> 'str34':
        raise RuntimeError39()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_262) -> 'str34':
        return 'INNER JOIN'
    def __init__(this_431) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_263) -> 'str34':
        return 'LEFT JOIN'
    def __init__(this_434) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_264) -> 'str34':
        return 'RIGHT JOIN'
    def __init__(this_437) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_265) -> 'str34':
        return 'FULL OUTER JOIN'
    def __init__(this_440) -> None:
        pass
class CrossJoin(JoinType):
    __slots__ = ()
    def keyword(this_266) -> 'str34':
        return 'CROSS JOIN'
    def __init__(this_443) -> None:
        pass
class JoinClause:
    join_type_1141: 'JoinType'
    table_1142: 'SafeIdentifier'
    on_condition_1143: 'Union35[SqlFragment, None]'
    __slots__ = ('join_type_1141', 'table_1142', 'on_condition_1143')
    def __init__(this_446, join_type_1145: 'JoinType', table_1146: 'SafeIdentifier', on_condition_1147: 'Union35[SqlFragment, None]') -> None:
        this_446.join_type_1141 = join_type_1145
        this_446.table_1142 = table_1146
        this_446.on_condition_1143 = on_condition_1147
    @property
    def join_type(this_2067) -> 'JoinType':
        return this_2067.join_type_1141
    @property
    def table(this_2070) -> 'SafeIdentifier':
        return this_2070.table_1142
    @property
    def on_condition(this_2073) -> 'Union35[SqlFragment, None]':
        return this_2073.on_condition_1143
class NullsPosition(metaclass = ABCMeta37):
    def keyword(this_267) -> 'str34':
        raise RuntimeError39()
class NullsFirst(NullsPosition):
    __slots__ = ()
    def keyword(this_268) -> 'str34':
        return ' NULLS FIRST'
    def __init__(this_450) -> None:
        pass
class NullsLast(NullsPosition):
    __slots__ = ()
    def keyword(this_269) -> 'str34':
        return ' NULLS LAST'
    def __init__(this_453) -> None:
        pass
class OrderClause:
    field_1156: 'SafeIdentifier'
    ascending_1157: 'bool42'
    nulls_pos_1158: 'Union35[NullsPosition, None]'
    __slots__ = ('field_1156', 'ascending_1157', 'nulls_pos_1158')
    def __init__(this_456, field_1160: 'SafeIdentifier', ascending_1161: 'bool42', nulls_pos_1162: 'Union35[NullsPosition, None]') -> None:
        this_456.field_1156 = field_1160
        this_456.ascending_1157 = ascending_1161
        this_456.nulls_pos_1158 = nulls_pos_1162
    @property
    def field(this_2076) -> 'SafeIdentifier':
        return this_2076.field_1156
    @property
    def ascending(this_2079) -> 'bool42':
        return this_2079.ascending_1157
    @property
    def nulls_pos(this_2082) -> 'Union35[NullsPosition, None]':
        return this_2082.nulls_pos_1158
class LockMode(metaclass = ABCMeta37):
    def keyword(this_270) -> 'str34':
        raise RuntimeError39()
class ForUpdate(LockMode):
    __slots__ = ()
    def keyword(this_271) -> 'str34':
        return ' FOR UPDATE'
    def __init__(this_460) -> None:
        pass
class ForShare(LockMode):
    __slots__ = ()
    def keyword(this_272) -> 'str34':
        return ' FOR SHARE'
    def __init__(this_463) -> None:
        pass
class WhereClause(metaclass = ABCMeta37):
    def keyword(this_274) -> 'str34':
        raise RuntimeError39()
class AndCondition(WhereClause):
    condition_1175: 'SqlFragment'
    __slots__ = ('condition_1175',)
    @property
    def condition(this_275) -> 'SqlFragment':
        return this_275.condition_1175
    def keyword(this_276) -> 'str34':
        return 'AND'
    def __init__(this_470, condition_1181: 'SqlFragment') -> None:
        this_470.condition_1175 = condition_1181
class OrCondition(WhereClause):
    condition_1182: 'SqlFragment'
    __slots__ = ('condition_1182',)
    @property
    def condition(this_277) -> 'SqlFragment':
        return this_277.condition_1182
    def keyword(this_278) -> 'str34':
        return 'OR'
    def __init__(this_475, condition_1188: 'SqlFragment') -> None:
        this_475.condition_1182 = condition_1188
class Query:
    table_name_1189: 'SafeIdentifier'
    conditions_1190: 'Sequence38[WhereClause]'
    selected_fields_1191: 'Sequence38[SafeIdentifier]'
    order_clauses_1192: 'Sequence38[OrderClause]'
    limit_val_1193: 'Union35[int40, None]'
    offset_val_1194: 'Union35[int40, None]'
    join_clauses_1195: 'Sequence38[JoinClause]'
    group_by_fields_1196: 'Sequence38[SafeIdentifier]'
    having_conditions_1197: 'Sequence38[WhereClause]'
    is_distinct_1198: 'bool42'
    select_exprs_1199: 'Sequence38[SqlFragment]'
    lock_mode_1200: 'Union35[LockMode, None]'
    __slots__ = ('table_name_1189', 'conditions_1190', 'selected_fields_1191', 'order_clauses_1192', 'limit_val_1193', 'offset_val_1194', 'join_clauses_1195', 'group_by_fields_1196', 'having_conditions_1197', 'is_distinct_1198', 'select_exprs_1199', 'lock_mode_1200')
    def where(this_279, condition_1202: 'SqlFragment') -> 'Query':
        nb_1204: 'MutableSequence45[WhereClause]' = list_14292(this_279.conditions_1190)
        nb_1204.append(AndCondition(condition_1202))
        return Query(this_279.table_name_1189, tuple_14295(nb_1204), this_279.selected_fields_1191, this_279.order_clauses_1192, this_279.limit_val_1193, this_279.offset_val_1194, this_279.join_clauses_1195, this_279.group_by_fields_1196, this_279.having_conditions_1197, this_279.is_distinct_1198, this_279.select_exprs_1199, this_279.lock_mode_1200)
    def or_where(this_280, condition_1206: 'SqlFragment') -> 'Query':
        nb_1208: 'MutableSequence45[WhereClause]' = list_14292(this_280.conditions_1190)
        nb_1208.append(OrCondition(condition_1206))
        return Query(this_280.table_name_1189, tuple_14295(nb_1208), this_280.selected_fields_1191, this_280.order_clauses_1192, this_280.limit_val_1193, this_280.offset_val_1194, this_280.join_clauses_1195, this_280.group_by_fields_1196, this_280.having_conditions_1197, this_280.is_distinct_1198, this_280.select_exprs_1199, this_280.lock_mode_1200)
    def where_null(this_281, field_1210: 'SafeIdentifier') -> 'Query':
        b_1212: 'SqlBuilder' = SqlBuilder()
        b_1212.append_safe(field_1210.sql_value)
        b_1212.append_safe(' IS NULL')
        t_12997: 'SqlFragment' = b_1212.accumulated
        return this_281.where(t_12997)
    def where_not_null(this_282, field_1214: 'SafeIdentifier') -> 'Query':
        b_1216: 'SqlBuilder' = SqlBuilder()
        b_1216.append_safe(field_1214.sql_value)
        b_1216.append_safe(' IS NOT NULL')
        t_12991: 'SqlFragment' = b_1216.accumulated
        return this_282.where(t_12991)
    def where_in(this_283, field_1218: 'SafeIdentifier', values_1219: 'Sequence38[SqlPart]') -> 'Query':
        return_495: 'Query'
        t_12972: 'SqlFragment'
        t_12980: 'int40'
        t_12985: 'SqlFragment'
        with Label44() as fn_1220:
            if not values_1219:
                b_1221: 'SqlBuilder' = SqlBuilder()
                b_1221.append_safe('1 = 0')
                t_12972 = b_1221.accumulated
                return_495 = this_283.where(t_12972)
                fn_1220.break_()
            b_1222: 'SqlBuilder' = SqlBuilder()
            b_1222.append_safe(field_1218.sql_value)
            b_1222.append_safe(' IN (')
            b_1222.append_part(list_get_14304(values_1219, 0))
            i_1223: 'int40' = 1
            while True:
                t_12980 = len_14296(values_1219)
                if not i_1223 < t_12980:
                    break
                b_1222.append_safe(', ')
                b_1222.append_part(list_get_14304(values_1219, i_1223))
                i_1223 = int_add_14305(i_1223, 1)
            b_1222.append_safe(')')
            t_12985 = b_1222.accumulated
            return_495 = this_283.where(t_12985)
        return return_495
    def where_in_subquery(this_284, field_1225: 'SafeIdentifier', sub_1226: 'Query') -> 'Query':
        b_1228: 'SqlBuilder' = SqlBuilder()
        b_1228.append_safe(field_1225.sql_value)
        b_1228.append_safe(' IN (')
        b_1228.append_fragment(sub_1226.to_sql())
        b_1228.append_safe(')')
        t_12967: 'SqlFragment' = b_1228.accumulated
        return this_284.where(t_12967)
    def where_not(this_285, condition_1230: 'SqlFragment') -> 'Query':
        b_1232: 'SqlBuilder' = SqlBuilder()
        b_1232.append_safe('NOT (')
        b_1232.append_fragment(condition_1230)
        b_1232.append_safe(')')
        t_12958: 'SqlFragment' = b_1232.accumulated
        return this_285.where(t_12958)
    def where_between(this_286, field_1234: 'SafeIdentifier', low_1235: 'SqlPart', high_1236: 'SqlPart') -> 'Query':
        b_1238: 'SqlBuilder' = SqlBuilder()
        b_1238.append_safe(field_1234.sql_value)
        b_1238.append_safe(' BETWEEN ')
        b_1238.append_part(low_1235)
        b_1238.append_safe(' AND ')
        b_1238.append_part(high_1236)
        t_12952: 'SqlFragment' = b_1238.accumulated
        return this_286.where(t_12952)
    def where_like(this_287, field_1240: 'SafeIdentifier', pattern_1241: 'str34') -> 'Query':
        b_1243: 'SqlBuilder' = SqlBuilder()
        b_1243.append_safe(field_1240.sql_value)
        b_1243.append_safe(' LIKE ')
        b_1243.append_string(pattern_1241)
        t_12943: 'SqlFragment' = b_1243.accumulated
        return this_287.where(t_12943)
    def where_i_like(this_288, field_1245: 'SafeIdentifier', pattern_1246: 'str34') -> 'Query':
        b_1248: 'SqlBuilder' = SqlBuilder()
        b_1248.append_safe(field_1245.sql_value)
        b_1248.append_safe(' ILIKE ')
        b_1248.append_string(pattern_1246)
        t_12936: 'SqlFragment' = b_1248.accumulated
        return this_288.where(t_12936)
    def select(this_289, fields_1250: 'Sequence38[SafeIdentifier]') -> 'Query':
        return Query(this_289.table_name_1189, this_289.conditions_1190, fields_1250, this_289.order_clauses_1192, this_289.limit_val_1193, this_289.offset_val_1194, this_289.join_clauses_1195, this_289.group_by_fields_1196, this_289.having_conditions_1197, this_289.is_distinct_1198, this_289.select_exprs_1199, this_289.lock_mode_1200)
    def select_expr(this_290, exprs_1253: 'Sequence38[SqlFragment]') -> 'Query':
        return Query(this_290.table_name_1189, this_290.conditions_1190, this_290.selected_fields_1191, this_290.order_clauses_1192, this_290.limit_val_1193, this_290.offset_val_1194, this_290.join_clauses_1195, this_290.group_by_fields_1196, this_290.having_conditions_1197, this_290.is_distinct_1198, exprs_1253, this_290.lock_mode_1200)
    def order_by(this_291, field_1256: 'SafeIdentifier', ascending_1257: 'bool42') -> 'Query':
        nb_1259: 'MutableSequence45[OrderClause]' = list_14292(this_291.order_clauses_1192)
        nb_1259.append(OrderClause(field_1256, ascending_1257, None))
        return Query(this_291.table_name_1189, this_291.conditions_1190, this_291.selected_fields_1191, tuple_14295(nb_1259), this_291.limit_val_1193, this_291.offset_val_1194, this_291.join_clauses_1195, this_291.group_by_fields_1196, this_291.having_conditions_1197, this_291.is_distinct_1198, this_291.select_exprs_1199, this_291.lock_mode_1200)
    def order_by_nulls(this_292, field_1261: 'SafeIdentifier', ascending_1262: 'bool42', nulls_1263: 'NullsPosition') -> 'Query':
        nb_1265: 'MutableSequence45[OrderClause]' = list_14292(this_292.order_clauses_1192)
        nb_1265.append(OrderClause(field_1261, ascending_1262, nulls_1263))
        return Query(this_292.table_name_1189, this_292.conditions_1190, this_292.selected_fields_1191, tuple_14295(nb_1265), this_292.limit_val_1193, this_292.offset_val_1194, this_292.join_clauses_1195, this_292.group_by_fields_1196, this_292.having_conditions_1197, this_292.is_distinct_1198, this_292.select_exprs_1199, this_292.lock_mode_1200)
    def limit(this_293, n_1267: 'int40') -> 'Query':
        if n_1267 < 0:
            raise RuntimeError39()
        return Query(this_293.table_name_1189, this_293.conditions_1190, this_293.selected_fields_1191, this_293.order_clauses_1192, n_1267, this_293.offset_val_1194, this_293.join_clauses_1195, this_293.group_by_fields_1196, this_293.having_conditions_1197, this_293.is_distinct_1198, this_293.select_exprs_1199, this_293.lock_mode_1200)
    def offset(this_294, n_1270: 'int40') -> 'Query':
        if n_1270 < 0:
            raise RuntimeError39()
        return Query(this_294.table_name_1189, this_294.conditions_1190, this_294.selected_fields_1191, this_294.order_clauses_1192, this_294.limit_val_1193, n_1270, this_294.join_clauses_1195, this_294.group_by_fields_1196, this_294.having_conditions_1197, this_294.is_distinct_1198, this_294.select_exprs_1199, this_294.lock_mode_1200)
    def join(this_295, join_type_1273: 'JoinType', table_1274: 'SafeIdentifier', on_condition_1275: 'SqlFragment') -> 'Query':
        nb_1277: 'MutableSequence45[JoinClause]' = list_14292(this_295.join_clauses_1195)
        nb_1277.append(JoinClause(join_type_1273, table_1274, on_condition_1275))
        return Query(this_295.table_name_1189, this_295.conditions_1190, this_295.selected_fields_1191, this_295.order_clauses_1192, this_295.limit_val_1193, this_295.offset_val_1194, tuple_14295(nb_1277), this_295.group_by_fields_1196, this_295.having_conditions_1197, this_295.is_distinct_1198, this_295.select_exprs_1199, this_295.lock_mode_1200)
    def inner_join(this_296, table_1279: 'SafeIdentifier', on_condition_1280: 'SqlFragment') -> 'Query':
        t_12898: 'InnerJoin' = InnerJoin()
        return this_296.join(t_12898, table_1279, on_condition_1280)
    def left_join(this_297, table_1283: 'SafeIdentifier', on_condition_1284: 'SqlFragment') -> 'Query':
        t_12896: 'LeftJoin' = LeftJoin()
        return this_297.join(t_12896, table_1283, on_condition_1284)
    def right_join(this_298, table_1287: 'SafeIdentifier', on_condition_1288: 'SqlFragment') -> 'Query':
        t_12894: 'RightJoin' = RightJoin()
        return this_298.join(t_12894, table_1287, on_condition_1288)
    def full_join(this_299, table_1291: 'SafeIdentifier', on_condition_1292: 'SqlFragment') -> 'Query':
        t_12892: 'FullJoin' = FullJoin()
        return this_299.join(t_12892, table_1291, on_condition_1292)
    def cross_join(this_300, table_1295: 'SafeIdentifier') -> 'Query':
        nb_1297: 'MutableSequence45[JoinClause]' = list_14292(this_300.join_clauses_1195)
        nb_1297.append(JoinClause(CrossJoin(), table_1295, None))
        return Query(this_300.table_name_1189, this_300.conditions_1190, this_300.selected_fields_1191, this_300.order_clauses_1192, this_300.limit_val_1193, this_300.offset_val_1194, tuple_14295(nb_1297), this_300.group_by_fields_1196, this_300.having_conditions_1197, this_300.is_distinct_1198, this_300.select_exprs_1199, this_300.lock_mode_1200)
    def group_by(this_301, field_1299: 'SafeIdentifier') -> 'Query':
        nb_1301: 'MutableSequence45[SafeIdentifier]' = list_14292(this_301.group_by_fields_1196)
        nb_1301.append(field_1299)
        return Query(this_301.table_name_1189, this_301.conditions_1190, this_301.selected_fields_1191, this_301.order_clauses_1192, this_301.limit_val_1193, this_301.offset_val_1194, this_301.join_clauses_1195, tuple_14295(nb_1301), this_301.having_conditions_1197, this_301.is_distinct_1198, this_301.select_exprs_1199, this_301.lock_mode_1200)
    def having(this_302, condition_1303: 'SqlFragment') -> 'Query':
        nb_1305: 'MutableSequence45[WhereClause]' = list_14292(this_302.having_conditions_1197)
        nb_1305.append(AndCondition(condition_1303))
        return Query(this_302.table_name_1189, this_302.conditions_1190, this_302.selected_fields_1191, this_302.order_clauses_1192, this_302.limit_val_1193, this_302.offset_val_1194, this_302.join_clauses_1195, this_302.group_by_fields_1196, tuple_14295(nb_1305), this_302.is_distinct_1198, this_302.select_exprs_1199, this_302.lock_mode_1200)
    def or_having(this_303, condition_1307: 'SqlFragment') -> 'Query':
        nb_1309: 'MutableSequence45[WhereClause]' = list_14292(this_303.having_conditions_1197)
        nb_1309.append(OrCondition(condition_1307))
        return Query(this_303.table_name_1189, this_303.conditions_1190, this_303.selected_fields_1191, this_303.order_clauses_1192, this_303.limit_val_1193, this_303.offset_val_1194, this_303.join_clauses_1195, this_303.group_by_fields_1196, tuple_14295(nb_1309), this_303.is_distinct_1198, this_303.select_exprs_1199, this_303.lock_mode_1200)
    def distinct(this_304) -> 'Query':
        return Query(this_304.table_name_1189, this_304.conditions_1190, this_304.selected_fields_1191, this_304.order_clauses_1192, this_304.limit_val_1193, this_304.offset_val_1194, this_304.join_clauses_1195, this_304.group_by_fields_1196, this_304.having_conditions_1197, True, this_304.select_exprs_1199, this_304.lock_mode_1200)
    def lock(this_305, mode_1313: 'LockMode') -> 'Query':
        return Query(this_305.table_name_1189, this_305.conditions_1190, this_305.selected_fields_1191, this_305.order_clauses_1192, this_305.limit_val_1193, this_305.offset_val_1194, this_305.join_clauses_1195, this_305.group_by_fields_1196, this_305.having_conditions_1197, this_305.is_distinct_1198, this_305.select_exprs_1199, mode_1313)
    def to_sql(this_306) -> 'SqlFragment':
        t_12783: 'int40'
        t_12802: 'int40'
        t_12821: 'int40'
        b_1317: 'SqlBuilder' = SqlBuilder()
        if this_306.is_distinct_1198:
            b_1317.append_safe('SELECT DISTINCT ')
        else:
            b_1317.append_safe('SELECT ')
        if not (not this_306.select_exprs_1199):
            b_1317.append_fragment(list_get_14304(this_306.select_exprs_1199, 0))
            i_1318: 'int40' = 1
            while True:
                t_12783 = len_14296(this_306.select_exprs_1199)
                if not i_1318 < t_12783:
                    break
                b_1317.append_safe(', ')
                b_1317.append_fragment(list_get_14304(this_306.select_exprs_1199, i_1318))
                i_1318 = int_add_14305(i_1318, 1)
        elif not this_306.selected_fields_1191:
            b_1317.append_safe('*')
        else:
            def fn_12776(f_1319: 'SafeIdentifier') -> 'str34':
                return f_1319.sql_value
            b_1317.append_safe(list_join_14320(this_306.selected_fields_1191, ', ', fn_12776))
        b_1317.append_safe(' FROM ')
        b_1317.append_safe(this_306.table_name_1189.sql_value)
        def fn_12775(jc_1320: 'JoinClause') -> 'None':
            b_1317.append_safe(' ')
            t_12763: 'str34' = jc_1320.join_type.keyword()
            b_1317.append_safe(t_12763)
            b_1317.append_safe(' ')
            t_12767: 'str34' = jc_1320.table.sql_value
            b_1317.append_safe(t_12767)
            oc_1321: 'Union35[SqlFragment, None]' = jc_1320.on_condition
            if not oc_1321 is None:
                oc_2478: 'SqlFragment' = oc_1321
                b_1317.append_safe(' ON ')
                b_1317.append_fragment(oc_2478)
        list_for_each_14290(this_306.join_clauses_1195, fn_12775)
        if not (not this_306.conditions_1190):
            b_1317.append_safe(' WHERE ')
            b_1317.append_fragment(list_get_14304(this_306.conditions_1190, 0).condition)
            i_1322: 'int40' = 1
            while True:
                t_12802 = len_14296(this_306.conditions_1190)
                if not i_1322 < t_12802:
                    break
                b_1317.append_safe(' ')
                b_1317.append_safe(list_get_14304(this_306.conditions_1190, i_1322).keyword())
                b_1317.append_safe(' ')
                b_1317.append_fragment(list_get_14304(this_306.conditions_1190, i_1322).condition)
                i_1322 = int_add_14305(i_1322, 1)
        if not (not this_306.group_by_fields_1196):
            b_1317.append_safe(' GROUP BY ')
            def fn_12774(f_1323: 'SafeIdentifier') -> 'str34':
                return f_1323.sql_value
            b_1317.append_safe(list_join_14320(this_306.group_by_fields_1196, ', ', fn_12774))
        if not (not this_306.having_conditions_1197):
            b_1317.append_safe(' HAVING ')
            b_1317.append_fragment(list_get_14304(this_306.having_conditions_1197, 0).condition)
            i_1324: 'int40' = 1
            while True:
                t_12821 = len_14296(this_306.having_conditions_1197)
                if not i_1324 < t_12821:
                    break
                b_1317.append_safe(' ')
                b_1317.append_safe(list_get_14304(this_306.having_conditions_1197, i_1324).keyword())
                b_1317.append_safe(' ')
                b_1317.append_fragment(list_get_14304(this_306.having_conditions_1197, i_1324).condition)
                i_1324 = int_add_14305(i_1324, 1)
        if not (not this_306.order_clauses_1192):
            b_1317.append_safe(' ORDER BY ')
            first_1325: 'bool42' = True
            def fn_12773(orc_1326: 'OrderClause') -> 'None':
                nonlocal first_1325
                t_12758: 'str34'
                t_6760: 'str34'
                if not first_1325:
                    b_1317.append_safe(', ')
                first_1325 = False
                t_12753: 'str34' = orc_1326.field.sql_value
                b_1317.append_safe(t_12753)
                if orc_1326.ascending:
                    t_6760 = ' ASC'
                else:
                    t_6760 = ' DESC'
                b_1317.append_safe(t_6760)
                np_1327: 'Union35[NullsPosition, None]' = orc_1326.nulls_pos
                if not np_1327 is None:
                    t_12758 = np_1327.keyword()
                    b_1317.append_safe(t_12758)
            list_for_each_14290(this_306.order_clauses_1192, fn_12773)
        lv_1328: 'Union35[int40, None]' = this_306.limit_val_1193
        if not lv_1328 is None:
            lv_2480: 'int40' = lv_1328
            b_1317.append_safe(' LIMIT ')
            b_1317.append_int32(lv_2480)
        ov_1329: 'Union35[int40, None]' = this_306.offset_val_1194
        if not ov_1329 is None:
            ov_2481: 'int40' = ov_1329
            b_1317.append_safe(' OFFSET ')
            b_1317.append_int32(ov_2481)
        lm_1330: 'Union35[LockMode, None]' = this_306.lock_mode_1200
        if not lm_1330 is None:
            b_1317.append_safe(lm_1330.keyword())
        return b_1317.accumulated
    def count_sql(this_307) -> 'SqlFragment':
        t_12722: 'int40'
        t_12741: 'int40'
        b_1333: 'SqlBuilder' = SqlBuilder()
        b_1333.append_safe('SELECT COUNT(*) FROM ')
        b_1333.append_safe(this_307.table_name_1189.sql_value)
        def fn_12710(jc_1334: 'JoinClause') -> 'None':
            b_1333.append_safe(' ')
            t_12700: 'str34' = jc_1334.join_type.keyword()
            b_1333.append_safe(t_12700)
            b_1333.append_safe(' ')
            t_12704: 'str34' = jc_1334.table.sql_value
            b_1333.append_safe(t_12704)
            oc2_1335: 'Union35[SqlFragment, None]' = jc_1334.on_condition
            if not oc2_1335 is None:
                oc2_2483: 'SqlFragment' = oc2_1335
                b_1333.append_safe(' ON ')
                b_1333.append_fragment(oc2_2483)
        list_for_each_14290(this_307.join_clauses_1195, fn_12710)
        if not (not this_307.conditions_1190):
            b_1333.append_safe(' WHERE ')
            b_1333.append_fragment(list_get_14304(this_307.conditions_1190, 0).condition)
            i_1336: 'int40' = 1
            while True:
                t_12722 = len_14296(this_307.conditions_1190)
                if not i_1336 < t_12722:
                    break
                b_1333.append_safe(' ')
                b_1333.append_safe(list_get_14304(this_307.conditions_1190, i_1336).keyword())
                b_1333.append_safe(' ')
                b_1333.append_fragment(list_get_14304(this_307.conditions_1190, i_1336).condition)
                i_1336 = int_add_14305(i_1336, 1)
        if not (not this_307.group_by_fields_1196):
            b_1333.append_safe(' GROUP BY ')
            def fn_12709(f_1337: 'SafeIdentifier') -> 'str34':
                return f_1337.sql_value
            b_1333.append_safe(list_join_14320(this_307.group_by_fields_1196, ', ', fn_12709))
        if not (not this_307.having_conditions_1197):
            b_1333.append_safe(' HAVING ')
            b_1333.append_fragment(list_get_14304(this_307.having_conditions_1197, 0).condition)
            i_1338: 'int40' = 1
            while True:
                t_12741 = len_14296(this_307.having_conditions_1197)
                if not i_1338 < t_12741:
                    break
                b_1333.append_safe(' ')
                b_1333.append_safe(list_get_14304(this_307.having_conditions_1197, i_1338).keyword())
                b_1333.append_safe(' ')
                b_1333.append_fragment(list_get_14304(this_307.having_conditions_1197, i_1338).condition)
                i_1338 = int_add_14305(i_1338, 1)
        return b_1333.accumulated
    def safe_to_sql(this_308, default_limit_1340: 'int40') -> 'SqlFragment':
        return_520: 'SqlFragment'
        t_6710: 'Query'
        if default_limit_1340 < 0:
            raise RuntimeError39()
        if not this_308.limit_val_1193 is None:
            return_520 = this_308.to_sql()
        else:
            t_6710 = this_308.limit(default_limit_1340)
            return_520 = t_6710.to_sql()
        return return_520
    def __init__(this_479, table_name_1343: 'SafeIdentifier', conditions_1344: 'Sequence38[WhereClause]', selected_fields_1345: 'Sequence38[SafeIdentifier]', order_clauses_1346: 'Sequence38[OrderClause]', limit_val_1347: 'Union35[int40, None]', offset_val_1348: 'Union35[int40, None]', join_clauses_1349: 'Sequence38[JoinClause]', group_by_fields_1350: 'Sequence38[SafeIdentifier]', having_conditions_1351: 'Sequence38[WhereClause]', is_distinct_1352: 'bool42', select_exprs_1353: 'Sequence38[SqlFragment]', lock_mode_1354: 'Union35[LockMode, None]') -> None:
        this_479.table_name_1189 = table_name_1343
        this_479.conditions_1190 = conditions_1344
        this_479.selected_fields_1191 = selected_fields_1345
        this_479.order_clauses_1192 = order_clauses_1346
        this_479.limit_val_1193 = limit_val_1347
        this_479.offset_val_1194 = offset_val_1348
        this_479.join_clauses_1195 = join_clauses_1349
        this_479.group_by_fields_1196 = group_by_fields_1350
        this_479.having_conditions_1197 = having_conditions_1351
        this_479.is_distinct_1198 = is_distinct_1352
        this_479.select_exprs_1199 = select_exprs_1353
        this_479.lock_mode_1200 = lock_mode_1354
    @property
    def table_name(this_2085) -> 'SafeIdentifier':
        return this_2085.table_name_1189
    @property
    def conditions(this_2088) -> 'Sequence38[WhereClause]':
        return this_2088.conditions_1190
    @property
    def selected_fields(this_2091) -> 'Sequence38[SafeIdentifier]':
        return this_2091.selected_fields_1191
    @property
    def order_clauses(this_2094) -> 'Sequence38[OrderClause]':
        return this_2094.order_clauses_1192
    @property
    def limit_val(this_2097) -> 'Union35[int40, None]':
        return this_2097.limit_val_1193
    @property
    def offset_val(this_2100) -> 'Union35[int40, None]':
        return this_2100.offset_val_1194
    @property
    def join_clauses(this_2103) -> 'Sequence38[JoinClause]':
        return this_2103.join_clauses_1195
    @property
    def group_by_fields(this_2106) -> 'Sequence38[SafeIdentifier]':
        return this_2106.group_by_fields_1196
    @property
    def having_conditions(this_2109) -> 'Sequence38[WhereClause]':
        return this_2109.having_conditions_1197
    @property
    def is_distinct(this_2112) -> 'bool42':
        return this_2112.is_distinct_1198
    @property
    def select_exprs(this_2115) -> 'Sequence38[SqlFragment]':
        return this_2115.select_exprs_1199
    @property
    def lock_mode(this_2118) -> 'Union35[LockMode, None]':
        return this_2118.lock_mode_1200
class SetClause:
    field_1401: 'SafeIdentifier'
    value_1402: 'SqlPart'
    __slots__ = ('field_1401', 'value_1402')
    def __init__(this_535, field_1404: 'SafeIdentifier', value_1405: 'SqlPart') -> None:
        this_535.field_1401 = field_1404
        this_535.value_1402 = value_1405
    @property
    def field(this_2121) -> 'SafeIdentifier':
        return this_2121.field_1401
    @property
    def value(this_2124) -> 'SqlPart':
        return this_2124.value_1402
class UpdateQuery:
    table_name_1406: 'SafeIdentifier'
    set_clauses_1407: 'Sequence38[SetClause]'
    conditions_1408: 'Sequence38[WhereClause]'
    limit_val_1409: 'Union35[int40, None]'
    __slots__ = ('table_name_1406', 'set_clauses_1407', 'conditions_1408', 'limit_val_1409')
    def set(this_309, field_1411: 'SafeIdentifier', value_1412: 'SqlPart') -> 'UpdateQuery':
        nb_1414: 'MutableSequence45[SetClause]' = list_14292(this_309.set_clauses_1407)
        nb_1414.append(SetClause(field_1411, value_1412))
        return UpdateQuery(this_309.table_name_1406, tuple_14295(nb_1414), this_309.conditions_1408, this_309.limit_val_1409)
    def where(this_310, condition_1416: 'SqlFragment') -> 'UpdateQuery':
        nb_1418: 'MutableSequence45[WhereClause]' = list_14292(this_310.conditions_1408)
        nb_1418.append(AndCondition(condition_1416))
        return UpdateQuery(this_310.table_name_1406, this_310.set_clauses_1407, tuple_14295(nb_1418), this_310.limit_val_1409)
    def or_where(this_311, condition_1420: 'SqlFragment') -> 'UpdateQuery':
        nb_1422: 'MutableSequence45[WhereClause]' = list_14292(this_311.conditions_1408)
        nb_1422.append(OrCondition(condition_1420))
        return UpdateQuery(this_311.table_name_1406, this_311.set_clauses_1407, tuple_14295(nb_1422), this_311.limit_val_1409)
    def limit(this_312, n_1424: 'int40') -> 'UpdateQuery':
        if n_1424 < 0:
            raise RuntimeError39()
        return UpdateQuery(this_312.table_name_1406, this_312.set_clauses_1407, this_312.conditions_1408, n_1424)
    def to_sql(this_313) -> 'SqlFragment':
        t_12557: 'int40'
        t_12571: 'int40'
        if not this_313.conditions_1408:
            raise RuntimeError39()
        if not this_313.set_clauses_1407:
            raise RuntimeError39()
        b_1428: 'SqlBuilder' = SqlBuilder()
        b_1428.append_safe('UPDATE ')
        b_1428.append_safe(this_313.table_name_1406.sql_value)
        b_1428.append_safe(' SET ')
        b_1428.append_safe(list_get_14304(this_313.set_clauses_1407, 0).field.sql_value)
        b_1428.append_safe(' = ')
        b_1428.append_part(list_get_14304(this_313.set_clauses_1407, 0).value)
        i_1429: 'int40' = 1
        while True:
            t_12557 = len_14296(this_313.set_clauses_1407)
            if not i_1429 < t_12557:
                break
            b_1428.append_safe(', ')
            b_1428.append_safe(list_get_14304(this_313.set_clauses_1407, i_1429).field.sql_value)
            b_1428.append_safe(' = ')
            b_1428.append_part(list_get_14304(this_313.set_clauses_1407, i_1429).value)
            i_1429 = int_add_14305(i_1429, 1)
        b_1428.append_safe(' WHERE ')
        b_1428.append_fragment(list_get_14304(this_313.conditions_1408, 0).condition)
        i_1430: 'int40' = 1
        while True:
            t_12571 = len_14296(this_313.conditions_1408)
            if not i_1430 < t_12571:
                break
            b_1428.append_safe(' ')
            b_1428.append_safe(list_get_14304(this_313.conditions_1408, i_1430).keyword())
            b_1428.append_safe(' ')
            b_1428.append_fragment(list_get_14304(this_313.conditions_1408, i_1430).condition)
            i_1430 = int_add_14305(i_1430, 1)
        lv_1431: 'Union35[int40, None]' = this_313.limit_val_1409
        if not lv_1431 is None:
            lv_2484: 'int40' = lv_1431
            b_1428.append_safe(' LIMIT ')
            b_1428.append_int32(lv_2484)
        return b_1428.accumulated
    def __init__(this_537, table_name_1433: 'SafeIdentifier', set_clauses_1434: 'Sequence38[SetClause]', conditions_1435: 'Sequence38[WhereClause]', limit_val_1436: 'Union35[int40, None]') -> None:
        this_537.table_name_1406 = table_name_1433
        this_537.set_clauses_1407 = set_clauses_1434
        this_537.conditions_1408 = conditions_1435
        this_537.limit_val_1409 = limit_val_1436
    @property
    def table_name(this_2127) -> 'SafeIdentifier':
        return this_2127.table_name_1406
    @property
    def set_clauses(this_2130) -> 'Sequence38[SetClause]':
        return this_2130.set_clauses_1407
    @property
    def conditions(this_2133) -> 'Sequence38[WhereClause]':
        return this_2133.conditions_1408
    @property
    def limit_val(this_2136) -> 'Union35[int40, None]':
        return this_2136.limit_val_1409
class DeleteQuery:
    table_name_1437: 'SafeIdentifier'
    conditions_1438: 'Sequence38[WhereClause]'
    limit_val_1439: 'Union35[int40, None]'
    __slots__ = ('table_name_1437', 'conditions_1438', 'limit_val_1439')
    def where(this_314, condition_1441: 'SqlFragment') -> 'DeleteQuery':
        nb_1443: 'MutableSequence45[WhereClause]' = list_14292(this_314.conditions_1438)
        nb_1443.append(AndCondition(condition_1441))
        return DeleteQuery(this_314.table_name_1437, tuple_14295(nb_1443), this_314.limit_val_1439)
    def or_where(this_315, condition_1445: 'SqlFragment') -> 'DeleteQuery':
        nb_1447: 'MutableSequence45[WhereClause]' = list_14292(this_315.conditions_1438)
        nb_1447.append(OrCondition(condition_1445))
        return DeleteQuery(this_315.table_name_1437, tuple_14295(nb_1447), this_315.limit_val_1439)
    def limit(this_316, n_1449: 'int40') -> 'DeleteQuery':
        if n_1449 < 0:
            raise RuntimeError39()
        return DeleteQuery(this_316.table_name_1437, this_316.conditions_1438, n_1449)
    def to_sql(this_317) -> 'SqlFragment':
        t_12517: 'int40'
        if not this_317.conditions_1438:
            raise RuntimeError39()
        b_1453: 'SqlBuilder' = SqlBuilder()
        b_1453.append_safe('DELETE FROM ')
        b_1453.append_safe(this_317.table_name_1437.sql_value)
        b_1453.append_safe(' WHERE ')
        b_1453.append_fragment(list_get_14304(this_317.conditions_1438, 0).condition)
        i_1454: 'int40' = 1
        while True:
            t_12517 = len_14296(this_317.conditions_1438)
            if not i_1454 < t_12517:
                break
            b_1453.append_safe(' ')
            b_1453.append_safe(list_get_14304(this_317.conditions_1438, i_1454).keyword())
            b_1453.append_safe(' ')
            b_1453.append_fragment(list_get_14304(this_317.conditions_1438, i_1454).condition)
            i_1454 = int_add_14305(i_1454, 1)
        lv_1455: 'Union35[int40, None]' = this_317.limit_val_1439
        if not lv_1455 is None:
            lv_2485: 'int40' = lv_1455
            b_1453.append_safe(' LIMIT ')
            b_1453.append_int32(lv_2485)
        return b_1453.accumulated
    def __init__(this_547, table_name_1457: 'SafeIdentifier', conditions_1458: 'Sequence38[WhereClause]', limit_val_1459: 'Union35[int40, None]') -> None:
        this_547.table_name_1437 = table_name_1457
        this_547.conditions_1438 = conditions_1458
        this_547.limit_val_1439 = limit_val_1459
    @property
    def table_name(this_2139) -> 'SafeIdentifier':
        return this_2139.table_name_1437
    @property
    def conditions(this_2142) -> 'Sequence38[WhereClause]':
        return this_2142.conditions_1438
    @property
    def limit_val(this_2145) -> 'Union35[int40, None]':
        return this_2145.limit_val_1439
class SafeIdentifier(metaclass = ABCMeta37):
    pass
class ValidatedIdentifier_319(SafeIdentifier):
    value_1690: 'str34'
    __slots__ = ('value_1690',)
    @property
    def sql_value(this_320) -> 'str34':
        return this_320.value_1690
    def __init__(this_561, value_1694: 'str34') -> None:
        this_561.value_1690 = value_1694
class FieldType(metaclass = ABCMeta37):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_567) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_569) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_571) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_573) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_575) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_577) -> None:
        pass
class FieldDef:
    name_1708: 'SafeIdentifier'
    field_type_1709: 'FieldType'
    nullable_1710: 'bool42'
    __slots__ = ('name_1708', 'field_type_1709', 'nullable_1710')
    def __init__(this_579, name_1712: 'SafeIdentifier', field_type_1713: 'FieldType', nullable_1714: 'bool42') -> None:
        this_579.name_1708 = name_1712
        this_579.field_type_1709 = field_type_1713
        this_579.nullable_1710 = nullable_1714
    @property
    def name(this_1971) -> 'SafeIdentifier':
        return this_1971.name_1708
    @property
    def field_type(this_1974) -> 'FieldType':
        return this_1974.field_type_1709
    @property
    def nullable(this_1977) -> 'bool42':
        return this_1977.nullable_1710
class TableDef:
    table_name_1715: 'SafeIdentifier'
    fields_1716: 'Sequence38[FieldDef]'
    __slots__ = ('table_name_1715', 'fields_1716')
    def field(this_321, name_1718: 'str34') -> 'FieldDef':
        return_584: 'FieldDef'
        with Label44() as fn_1719:
            this_8420: 'Sequence38[FieldDef]' = this_321.fields_1716
            n_8421: 'int40' = len_14296(this_8420)
            i_8422: 'int40' = 0
            while i_8422 < n_8421:
                el_8423: 'FieldDef' = list_get_14304(this_8420, i_8422)
                i_8422 = int_add_14305(i_8422, 1)
                f_1720: 'FieldDef' = el_8423
                if f_1720.name.sql_value == name_1718:
                    return_584 = f_1720
                    fn_1719.break_()
            raise RuntimeError39()
        return return_584
    def __init__(this_581, table_name_1722: 'SafeIdentifier', fields_1723: 'Sequence38[FieldDef]') -> None:
        this_581.table_name_1715 = table_name_1722
        this_581.fields_1716 = fields_1723
    @property
    def table_name(this_1980) -> 'SafeIdentifier':
        return this_1980.table_name_1715
    @property
    def fields(this_1983) -> 'Sequence38[FieldDef]':
        return this_1983.fields_1716
T_340 = TypeVar49('T_340', bound = Any48)
class SqlBuilder:
    buffer_1743: 'MutableSequence45[SqlPart]'
    __slots__ = ('buffer_1743',)
    def append_safe(this_322, sql_source_1745: 'str34') -> 'None':
        t_14251: 'SqlSource' = SqlSource(sql_source_1745)
        this_322.buffer_1743.append(t_14251)
    def append_fragment(this_323, fragment_1748: 'SqlFragment') -> 'None':
        t_14249: 'Sequence38[SqlPart]' = fragment_1748.parts
        list_builder_add_all_14321(this_323.buffer_1743, t_14249)
    def append_part(this_324, part_1751: 'SqlPart') -> 'None':
        this_324.buffer_1743.append(part_1751)
    def append_part_list(this_325, values_1754: 'Sequence38[SqlPart]') -> 'None':
        def fn_14245(x_1756: 'SqlPart') -> 'None':
            this_325.append_part(x_1756)
        this_325.append_list_1799(values_1754, fn_14245)
    def append_boolean(this_326, value_1758: 'bool42') -> 'None':
        t_14242: 'SqlBoolean' = SqlBoolean(value_1758)
        this_326.buffer_1743.append(t_14242)
    def append_boolean_list(this_327, values_1761: 'Sequence38[bool42]') -> 'None':
        def fn_14239(x_1763: 'bool42') -> 'None':
            this_327.append_boolean(x_1763)
        this_327.append_list_1799(values_1761, fn_14239)
    def append_date(this_328, value_1765: 'date33') -> 'None':
        t_14236: 'SqlDate' = SqlDate(value_1765)
        this_328.buffer_1743.append(t_14236)
    def append_date_list(this_329, values_1768: 'Sequence38[date33]') -> 'None':
        def fn_14233(x_1770: 'date33') -> 'None':
            this_329.append_date(x_1770)
        this_329.append_list_1799(values_1768, fn_14233)
    def append_float64(this_330, value_1772: 'float36') -> 'None':
        t_14230: 'SqlFloat64' = SqlFloat64(value_1772)
        this_330.buffer_1743.append(t_14230)
    def append_float64_list(this_331, values_1775: 'Sequence38[float36]') -> 'None':
        def fn_14227(x_1777: 'float36') -> 'None':
            this_331.append_float64(x_1777)
        this_331.append_list_1799(values_1775, fn_14227)
    def append_int32(this_332, value_1779: 'int40') -> 'None':
        t_14224: 'SqlInt32' = SqlInt32(value_1779)
        this_332.buffer_1743.append(t_14224)
    def append_int32_list(this_333, values_1782: 'Sequence38[int40]') -> 'None':
        def fn_14221(x_1784: 'int40') -> 'None':
            this_333.append_int32(x_1784)
        this_333.append_list_1799(values_1782, fn_14221)
    def append_int64(this_334, value_1786: 'int64_23') -> 'None':
        t_14218: 'SqlInt64' = SqlInt64(value_1786)
        this_334.buffer_1743.append(t_14218)
    def append_int64_list(this_335, values_1789: 'Sequence38[int64_23]') -> 'None':
        def fn_14215(x_1791: 'int64_23') -> 'None':
            this_335.append_int64(x_1791)
        this_335.append_list_1799(values_1789, fn_14215)
    def append_string(this_336, value_1793: 'str34') -> 'None':
        t_14212: 'SqlString' = SqlString(value_1793)
        this_336.buffer_1743.append(t_14212)
    def append_string_list(this_337, values_1796: 'Sequence38[str34]') -> 'None':
        def fn_14209(x_1798: 'str34') -> 'None':
            this_337.append_string(x_1798)
        this_337.append_list_1799(values_1796, fn_14209)
    def append_list_1799(this_338, values_1800: 'Sequence38[T_340]', append_value_1801: 'Callable50[[T_340], None]') -> 'None':
        t_14204: 'int40'
        t_14206: 'T_340'
        i_1803: 'int40' = 0
        while True:
            t_14204 = len_14296(values_1800)
            if not i_1803 < t_14204:
                break
            if i_1803 > 0:
                this_338.append_safe(', ')
            t_14206 = list_get_14304(values_1800, i_1803)
            append_value_1801(t_14206)
            i_1803 = int_add_14305(i_1803, 1)
    @property
    def accumulated(this_339) -> 'SqlFragment':
        return SqlFragment(tuple_14295(this_339.buffer_1743))
    def __init__(this_586) -> None:
        t_14201: 'MutableSequence45[SqlPart]' = list_14292()
        this_586.buffer_1743 = t_14201
class SqlFragment:
    parts_1810: 'Sequence38[SqlPart]'
    __slots__ = ('parts_1810',)
    def to_source(this_344) -> 'SqlSource':
        return SqlSource(this_344.to_string())
    def to_string(this_345) -> 'str34':
        t_14275: 'int40'
        builder_1815: 'list3[str34]' = ['']
        i_1816: 'int40' = 0
        while True:
            t_14275 = len_14296(this_345.parts_1810)
            if not i_1816 < t_14275:
                break
            list_get_14304(this_345.parts_1810, i_1816).format_to(builder_1815)
            i_1816 = int_add_14305(i_1816, 1)
        return ''.join(builder_1815)
    def __init__(this_607, parts_1818: 'Sequence38[SqlPart]') -> None:
        this_607.parts_1810 = parts_1818
    @property
    def parts(this_1989) -> 'Sequence38[SqlPart]':
        return this_1989.parts_1810
class SqlPart(metaclass = ABCMeta37):
    def format_to(this_346, builder_1820: 'list3[str34]') -> 'None':
        raise RuntimeError39()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_1822: 'str34'
    __slots__ = ('source_1822',)
    def format_to(this_347, builder_1824: 'list3[str34]') -> 'None':
        builder_1824.append(this_347.source_1822)
    def __init__(this_613, source_1827: 'str34') -> None:
        this_613.source_1822 = source_1827
    @property
    def source(this_1986) -> 'str34':
        return this_1986.source_1822
class SqlBoolean(SqlPart):
    value_1828: 'bool42'
    __slots__ = ('value_1828',)
    def format_to(this_348, builder_1830: 'list3[str34]') -> 'None':
        t_8157: 'str34'
        if this_348.value_1828:
            t_8157 = 'TRUE'
        else:
            t_8157 = 'FALSE'
        builder_1830.append(t_8157)
    def __init__(this_616, value_1833: 'bool42') -> None:
        this_616.value_1828 = value_1833
    @property
    def value(this_1992) -> 'bool42':
        return this_1992.value_1828
class SqlDate(SqlPart):
    value_1834: 'date33'
    __slots__ = ('value_1834',)
    def format_to(this_349, builder_1836: 'list3[str34]') -> 'None':
        builder_1836.append("'")
        t_14256: 'str34' = date_to_string_14325(this_349.value_1834)
        def fn_14254(c_1838: 'int40') -> 'None':
            if c_1838 == 39:
                builder_1836.append("''")
            else:
                builder_1836.append(string_from_code_point51(c_1838))
        string_for_each_14327(t_14256, fn_14254)
        builder_1836.append("'")
    def __init__(this_619, value_1840: 'date33') -> None:
        this_619.value_1834 = value_1840
    @property
    def value(this_2007) -> 'date33':
        return this_2007.value_1834
class SqlFloat64(SqlPart):
    value_1841: 'float36'
    __slots__ = ('value_1841',)
    def format_to(this_350, builder_1843: 'list3[str34]') -> 'None':
        t_8146: 'bool42'
        t_8147: 'bool42'
        s_1845: 'str34' = float64_to_string_14307(this_350.value_1841)
        if s_1845 == 'NaN':
            t_8147 = True
        else:
            if s_1845 == 'Infinity':
                t_8146 = True
            else:
                t_8146 = s_1845 == '-Infinity'
            t_8147 = t_8146
        if t_8147:
            builder_1843.append('NULL')
        else:
            builder_1843.append(s_1845)
    def __init__(this_622, value_1847: 'float36') -> None:
        this_622.value_1841 = value_1847
    @property
    def value(this_2004) -> 'float36':
        return this_2004.value_1841
class SqlInt32(SqlPart):
    value_1848: 'int40'
    __slots__ = ('value_1848',)
    def format_to(this_351, builder_1850: 'list3[str34]') -> 'None':
        t_14265: 'str34' = int_to_string_14299(this_351.value_1848)
        builder_1850.append(t_14265)
    def __init__(this_625, value_1853: 'int40') -> None:
        this_625.value_1848 = value_1853
    @property
    def value(this_1998) -> 'int40':
        return this_1998.value_1848
class SqlInt64(SqlPart):
    value_1854: 'int64_23'
    __slots__ = ('value_1854',)
    def format_to(this_352, builder_1856: 'list3[str34]') -> 'None':
        t_14263: 'str34' = int_to_string_14299(this_352.value_1854)
        builder_1856.append(t_14263)
    def __init__(this_628, value_1859: 'int64_23') -> None:
        this_628.value_1854 = value_1859
    @property
    def value(this_2001) -> 'int64_23':
        return this_2001.value_1854
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_1860: 'str34'
    __slots__ = ('value_1860',)
    def format_to(this_353, builder_1862: 'list3[str34]') -> 'None':
        builder_1862.append("'")
        def fn_14268(c_1864: 'int40') -> 'None':
            if c_1864 == 39:
                builder_1862.append("''")
            else:
                builder_1862.append(string_from_code_point51(c_1864))
        string_for_each_14327(this_353.value_1860, fn_14268)
        builder_1862.append("'")
    def __init__(this_631, value_1866: 'str34') -> None:
        this_631.value_1860 = value_1866
    @property
    def value(this_1995) -> 'str34':
        return this_1995.value_1860
def changeset(table_def_921: 'TableDef', params_922: 'MappingProxyType41[str34, str34]') -> 'Changeset':
    t_13867: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
    return ChangesetImpl_234(table_def_921, params_922, t_13867, (), True)
def is_ident_start_639(c_1695: 'int40') -> 'bool42':
    return_564: 'bool42'
    t_7693: 'bool42'
    t_7694: 'bool42'
    if c_1695 >= 97:
        t_7693 = c_1695 <= 122
    else:
        t_7693 = False
    if t_7693:
        return_564 = True
    else:
        if c_1695 >= 65:
            t_7694 = c_1695 <= 90
        else:
            t_7694 = False
        if t_7694:
            return_564 = True
        else:
            return_564 = c_1695 == 95
    return return_564
def is_ident_part_640(c_1697: 'int40') -> 'bool42':
    return_565: 'bool42'
    if is_ident_start_639(c_1697):
        return_565 = True
    elif c_1697 >= 48:
        return_565 = c_1697 <= 57
    else:
        return_565 = False
    return return_565
def safe_identifier(name_1699: 'str34') -> 'SafeIdentifier':
    t_13865: 'int40'
    if not name_1699:
        raise RuntimeError39()
    idx_1701: 'int40' = 0
    if not is_ident_start_639(string_get_14318(name_1699, idx_1701)):
        raise RuntimeError39()
    t_13862: 'int40' = string_next_14316(name_1699, idx_1701)
    idx_1701 = t_13862
    while True:
        if not len6(name_1699) > idx_1701:
            break
        if not is_ident_part_640(string_get_14318(name_1699, idx_1701)):
            raise RuntimeError39()
        t_13865 = string_next_14316(name_1699, idx_1701)
        idx_1701 = t_13865
    return ValidatedIdentifier_319(name_1699)
def delete_sql(table_def_1120: 'TableDef', id_1121: 'int40') -> 'SqlFragment':
    b_1123: 'SqlBuilder' = SqlBuilder()
    b_1123.append_safe('DELETE FROM ')
    b_1123.append_safe(table_def_1120.table_name.sql_value)
    b_1123.append_safe(' WHERE id = ')
    b_1123.append_int32(id_1121)
    return b_1123.accumulated
def from_(table_name_1355: 'SafeIdentifier') -> 'Query':
    return Query(table_name_1355, (), (), (), None, None, (), (), (), False, (), None)
def col(table_1357: 'SafeIdentifier', column_1358: 'SafeIdentifier') -> 'SqlFragment':
    b_1360: 'SqlBuilder' = SqlBuilder()
    b_1360.append_safe(table_1357.sql_value)
    b_1360.append_safe('.')
    b_1360.append_safe(column_1358.sql_value)
    return b_1360.accumulated
def count_all() -> 'SqlFragment':
    b_1362: 'SqlBuilder' = SqlBuilder()
    b_1362.append_safe('COUNT(*)')
    return b_1362.accumulated
def count_col(field_1363: 'SafeIdentifier') -> 'SqlFragment':
    b_1365: 'SqlBuilder' = SqlBuilder()
    b_1365.append_safe('COUNT(')
    b_1365.append_safe(field_1363.sql_value)
    b_1365.append_safe(')')
    return b_1365.accumulated
def sum_col(field_1366: 'SafeIdentifier') -> 'SqlFragment':
    b_1368: 'SqlBuilder' = SqlBuilder()
    b_1368.append_safe('SUM(')
    b_1368.append_safe(field_1366.sql_value)
    b_1368.append_safe(')')
    return b_1368.accumulated
def avg_col(field_1369: 'SafeIdentifier') -> 'SqlFragment':
    b_1371: 'SqlBuilder' = SqlBuilder()
    b_1371.append_safe('AVG(')
    b_1371.append_safe(field_1369.sql_value)
    b_1371.append_safe(')')
    return b_1371.accumulated
def min_col(field_1372: 'SafeIdentifier') -> 'SqlFragment':
    b_1374: 'SqlBuilder' = SqlBuilder()
    b_1374.append_safe('MIN(')
    b_1374.append_safe(field_1372.sql_value)
    b_1374.append_safe(')')
    return b_1374.accumulated
def max_col(field_1375: 'SafeIdentifier') -> 'SqlFragment':
    b_1377: 'SqlBuilder' = SqlBuilder()
    b_1377.append_safe('MAX(')
    b_1377.append_safe(field_1375.sql_value)
    b_1377.append_safe(')')
    return b_1377.accumulated
def union_sql(a_1378: 'Query', b_1379: 'Query') -> 'SqlFragment':
    sb_1381: 'SqlBuilder' = SqlBuilder()
    sb_1381.append_safe('(')
    sb_1381.append_fragment(a_1378.to_sql())
    sb_1381.append_safe(') UNION (')
    sb_1381.append_fragment(b_1379.to_sql())
    sb_1381.append_safe(')')
    return sb_1381.accumulated
def union_all_sql(a_1382: 'Query', b_1383: 'Query') -> 'SqlFragment':
    sb_1385: 'SqlBuilder' = SqlBuilder()
    sb_1385.append_safe('(')
    sb_1385.append_fragment(a_1382.to_sql())
    sb_1385.append_safe(') UNION ALL (')
    sb_1385.append_fragment(b_1383.to_sql())
    sb_1385.append_safe(')')
    return sb_1385.accumulated
def intersect_sql(a_1386: 'Query', b_1387: 'Query') -> 'SqlFragment':
    sb_1389: 'SqlBuilder' = SqlBuilder()
    sb_1389.append_safe('(')
    sb_1389.append_fragment(a_1386.to_sql())
    sb_1389.append_safe(') INTERSECT (')
    sb_1389.append_fragment(b_1387.to_sql())
    sb_1389.append_safe(')')
    return sb_1389.accumulated
def except_sql(a_1390: 'Query', b_1391: 'Query') -> 'SqlFragment':
    sb_1393: 'SqlBuilder' = SqlBuilder()
    sb_1393.append_safe('(')
    sb_1393.append_fragment(a_1390.to_sql())
    sb_1393.append_safe(') EXCEPT (')
    sb_1393.append_fragment(b_1391.to_sql())
    sb_1393.append_safe(')')
    return sb_1393.accumulated
def subquery(q_1394: 'Query', alias_1395: 'SafeIdentifier') -> 'SqlFragment':
    b_1397: 'SqlBuilder' = SqlBuilder()
    b_1397.append_safe('(')
    b_1397.append_fragment(q_1394.to_sql())
    b_1397.append_safe(') AS ')
    b_1397.append_safe(alias_1395.sql_value)
    return b_1397.accumulated
def exists_sql(q_1398: 'Query') -> 'SqlFragment':
    b_1400: 'SqlBuilder' = SqlBuilder()
    b_1400.append_safe('EXISTS (')
    b_1400.append_fragment(q_1398.to_sql())
    b_1400.append_safe(')')
    return b_1400.accumulated
def update(table_name_1460: 'SafeIdentifier') -> 'UpdateQuery':
    return UpdateQuery(table_name_1460, (), (), None)
def delete_from(table_name_1462: 'SafeIdentifier') -> 'DeleteQuery':
    return DeleteQuery(table_name_1462, (), None)
