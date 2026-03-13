from builtins import str as str27, RuntimeError as RuntimeError30, int as int31, bool as bool33, Exception as Exception37, float as float38, isinstance as isinstance39, list as list3, len as len6, tuple as tuple5
from abc import ABCMeta as ABCMeta28
from typing import Sequence as Sequence29, Dict as Dict34, MutableSequence as MutableSequence36, Union as Union40, Any as Any41, TypeVar as TypeVar42, Callable as Callable43
from types import MappingProxyType as MappingProxyType32
from temper_core import Label as Label35, Pair as Pair25, string_from_code_point as string_from_code_point44, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, date_from_iso_string as date_from_iso_string13, list_get as list_get14, int_add as int_add15, mapped_to_list as mapped_to_list16, list_join as list_join17, list_builder_add_all as list_builder_add_all18, date_to_string as date_to_string19, string_for_each as string_for_each20, float64_to_string as float64_to_string21, map_constructor as map_constructor22, string_get as string_get23, string_next as string_next24
from datetime import date as date26
map_builder_set_5110 = map_builder_set0
list_for_each_5111 = list_for_each1
mapped_to_map_5112 = mapped_to_map2
list_5113 = list3
mapped_has_5114 = mapped_has4
tuple_5116 = tuple5
len_5117 = len6
string_count_between_5118 = string_count_between7
str_cat_5119 = str_cat8
int_to_string_5120 = int_to_string9
string_to_int32_5121 = string_to_int3210
string_to_int64_5122 = string_to_int6411
string_to_float64_5123 = string_to_float6412
date_from_iso_string_5124 = date_from_iso_string13
list_get_5125 = list_get14
int_add_5126 = int_add15
mapped_to_list_5127 = mapped_to_list16
list_join_5128 = list_join17
list_builder_add_all_5129 = list_builder_add_all18
date_to_string_5133 = date_to_string19
string_for_each_5135 = string_for_each20
float64_to_string_5136 = float64_to_string21
map_constructor_5137 = map_constructor22
string_get_5138 = string_get23
string_next_5139 = string_next24
pair_5141 = Pair25
date_5144 = date26
class ChangesetError:
    field_309: 'str27'
    message_310: 'str27'
    __slots__ = ('field_309', 'message_310')
    def __init__(this_159, field_312: 'str27', message_313: 'str27') -> None:
        this_159.field_309 = field_312
        this_159.message_310 = message_313
    @property
    def field(this_864) -> 'str27':
        return this_864.field_309
    @property
    def message(this_867) -> 'str27':
        return this_867.message_310
class Changeset(metaclass = ABCMeta28):
    def cast(this_91, allowed_fields_323: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_required(this_92, fields_326: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_length(this_93, field_329: 'SafeIdentifier', min_330: 'int31', max_331: 'int31') -> 'Changeset':
        raise RuntimeError30()
    def validate_int(this_94, field_334: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_int64(this_95, field_337: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_float(this_96, field_340: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_bool(this_97, field_343: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def to_insert_sql(this_98) -> 'SqlFragment':
        raise RuntimeError30()
    def to_update_sql(this_99, id_348: 'int31') -> 'SqlFragment':
        raise RuntimeError30()
class ChangesetImpl_100(Changeset):
    table_def_350: 'TableDef'
    params_351: 'MappingProxyType32[str27, str27]'
    changes_352: 'MappingProxyType32[str27, str27]'
    errors_353: 'Sequence29[ChangesetError]'
    is_valid_354: 'bool33'
    __slots__ = ('table_def_350', 'params_351', 'changes_352', 'errors_353', 'is_valid_354')
    @property
    def table_def(this_101) -> 'TableDef':
        return this_101.table_def_350
    @property
    def changes(this_102) -> 'MappingProxyType32[str27, str27]':
        return this_102.changes_352
    @property
    def errors(this_103) -> 'Sequence29[ChangesetError]':
        return this_103.errors_353
    @property
    def is_valid(this_104) -> 'bool33':
        return this_104.is_valid_354
    def cast(this_105, allowed_fields_364: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        mb_366: 'Dict34[str27, str27]' = {}
        def fn_5014(f_367: 'SafeIdentifier') -> 'None':
            t_5012: 'str27'
            t_5009: 'str27' = f_367.sql_value
            val_368: 'str27' = this_105.params_351.get(t_5009, '')
            if not (not val_368):
                t_5012 = f_367.sql_value
                map_builder_set_5110(mb_366, t_5012, val_368)
        list_for_each_5111(allowed_fields_364, fn_5014)
        return ChangesetImpl_100(this_105.table_def_350, this_105.params_351, mapped_to_map_5112(mb_366), this_105.errors_353, this_105.is_valid_354)
    def validate_required(this_106, fields_370: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        return_192: 'Changeset'
        t_5007: 'Sequence29[ChangesetError]'
        t_2977: 'TableDef'
        t_2978: 'MappingProxyType32[str27, str27]'
        t_2979: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_371:
            if not this_106.is_valid_354:
                return_192 = this_106
                fn_371.break_()
            eb_372: 'MutableSequence36[ChangesetError]' = list_5113(this_106.errors_353)
            valid_373: 'bool33' = True
            def fn_5003(f_374: 'SafeIdentifier') -> 'None':
                nonlocal valid_373
                t_5001: 'ChangesetError'
                t_4998: 'str27' = f_374.sql_value
                if not mapped_has_5114(this_106.changes_352, t_4998):
                    t_5001 = ChangesetError(f_374.sql_value, 'is required')
                    eb_372.append(t_5001)
                    valid_373 = False
            list_for_each_5111(fields_370, fn_5003)
            t_2977 = this_106.table_def_350
            t_2978 = this_106.params_351
            t_2979 = this_106.changes_352
            t_5007 = tuple_5116(eb_372)
            return_192 = ChangesetImpl_100(t_2977, t_2978, t_2979, t_5007, valid_373)
        return return_192
    def validate_length(this_107, field_376: 'SafeIdentifier', min_377: 'int31', max_378: 'int31') -> 'Changeset':
        return_193: 'Changeset'
        t_4985: 'str27'
        t_4996: 'Sequence29[ChangesetError]'
        t_2960: 'bool33'
        t_2966: 'TableDef'
        t_2967: 'MappingProxyType32[str27, str27]'
        t_2968: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_379:
            if not this_107.is_valid_354:
                return_193 = this_107
                fn_379.break_()
            t_4985 = field_376.sql_value
            val_380: 'str27' = this_107.changes_352.get(t_4985, '')
            len_381: 'int31' = string_count_between_5118(val_380, 0, len_5117(val_380))
            if len_381 < min_377:
                t_2960 = True
            else:
                t_2960 = len_381 > max_378
            if t_2960:
                msg_382: 'str27' = str_cat_5119('must be between ', int_to_string_5120(min_377), ' and ', int_to_string_5120(max_378), ' characters')
                eb_383: 'MutableSequence36[ChangesetError]' = list_5113(this_107.errors_353)
                eb_383.append(ChangesetError(field_376.sql_value, msg_382))
                t_2966 = this_107.table_def_350
                t_2967 = this_107.params_351
                t_2968 = this_107.changes_352
                t_4996 = tuple_5116(eb_383)
                return_193 = ChangesetImpl_100(t_2966, t_2967, t_2968, t_4996, False)
                fn_379.break_()
            return_193 = this_107
        return return_193
    def validate_int(this_108, field_385: 'SafeIdentifier') -> 'Changeset':
        return_194: 'Changeset'
        t_4976: 'str27'
        t_4983: 'Sequence29[ChangesetError]'
        t_2951: 'TableDef'
        t_2952: 'MappingProxyType32[str27, str27]'
        t_2953: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_386:
            if not this_108.is_valid_354:
                return_194 = this_108
                fn_386.break_()
            t_4976 = field_385.sql_value
            val_387: 'str27' = this_108.changes_352.get(t_4976, '')
            if not val_387:
                return_194 = this_108
                fn_386.break_()
            parse_ok_388: 'bool33'
            try:
                string_to_int32_5121(val_387)
                parse_ok_388 = True
            except Exception37:
                parse_ok_388 = False
            if not parse_ok_388:
                eb_389: 'MutableSequence36[ChangesetError]' = list_5113(this_108.errors_353)
                eb_389.append(ChangesetError(field_385.sql_value, 'must be an integer'))
                t_2951 = this_108.table_def_350
                t_2952 = this_108.params_351
                t_2953 = this_108.changes_352
                t_4983 = tuple_5116(eb_389)
                return_194 = ChangesetImpl_100(t_2951, t_2952, t_2953, t_4983, False)
                fn_386.break_()
            return_194 = this_108
        return return_194
    def validate_int64(this_109, field_391: 'SafeIdentifier') -> 'Changeset':
        return_195: 'Changeset'
        t_4967: 'str27'
        t_4974: 'Sequence29[ChangesetError]'
        t_2938: 'TableDef'
        t_2939: 'MappingProxyType32[str27, str27]'
        t_2940: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_392:
            if not this_109.is_valid_354:
                return_195 = this_109
                fn_392.break_()
            t_4967 = field_391.sql_value
            val_393: 'str27' = this_109.changes_352.get(t_4967, '')
            if not val_393:
                return_195 = this_109
                fn_392.break_()
            parse_ok_394: 'bool33'
            try:
                string_to_int64_5122(val_393)
                parse_ok_394 = True
            except Exception37:
                parse_ok_394 = False
            if not parse_ok_394:
                eb_395: 'MutableSequence36[ChangesetError]' = list_5113(this_109.errors_353)
                eb_395.append(ChangesetError(field_391.sql_value, 'must be a 64-bit integer'))
                t_2938 = this_109.table_def_350
                t_2939 = this_109.params_351
                t_2940 = this_109.changes_352
                t_4974 = tuple_5116(eb_395)
                return_195 = ChangesetImpl_100(t_2938, t_2939, t_2940, t_4974, False)
                fn_392.break_()
            return_195 = this_109
        return return_195
    def validate_float(this_110, field_397: 'SafeIdentifier') -> 'Changeset':
        return_196: 'Changeset'
        t_4958: 'str27'
        t_4965: 'Sequence29[ChangesetError]'
        t_2925: 'TableDef'
        t_2926: 'MappingProxyType32[str27, str27]'
        t_2927: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_398:
            if not this_110.is_valid_354:
                return_196 = this_110
                fn_398.break_()
            t_4958 = field_397.sql_value
            val_399: 'str27' = this_110.changes_352.get(t_4958, '')
            if not val_399:
                return_196 = this_110
                fn_398.break_()
            parse_ok_400: 'bool33'
            try:
                string_to_float64_5123(val_399)
                parse_ok_400 = True
            except Exception37:
                parse_ok_400 = False
            if not parse_ok_400:
                eb_401: 'MutableSequence36[ChangesetError]' = list_5113(this_110.errors_353)
                eb_401.append(ChangesetError(field_397.sql_value, 'must be a number'))
                t_2925 = this_110.table_def_350
                t_2926 = this_110.params_351
                t_2927 = this_110.changes_352
                t_4965 = tuple_5116(eb_401)
                return_196 = ChangesetImpl_100(t_2925, t_2926, t_2927, t_4965, False)
                fn_398.break_()
            return_196 = this_110
        return return_196
    def validate_bool(this_111, field_403: 'SafeIdentifier') -> 'Changeset':
        return_197: 'Changeset'
        t_4949: 'str27'
        t_4956: 'Sequence29[ChangesetError]'
        t_2900: 'bool33'
        t_2901: 'bool33'
        t_2903: 'bool33'
        t_2904: 'bool33'
        t_2906: 'bool33'
        t_2912: 'TableDef'
        t_2913: 'MappingProxyType32[str27, str27]'
        t_2914: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_404:
            if not this_111.is_valid_354:
                return_197 = this_111
                fn_404.break_()
            t_4949 = field_403.sql_value
            val_405: 'str27' = this_111.changes_352.get(t_4949, '')
            if not val_405:
                return_197 = this_111
                fn_404.break_()
            is_true_406: 'bool33'
            if val_405 == 'true':
                is_true_406 = True
            else:
                if val_405 == '1':
                    t_2901 = True
                else:
                    if val_405 == 'yes':
                        t_2900 = True
                    else:
                        t_2900 = val_405 == 'on'
                    t_2901 = t_2900
                is_true_406 = t_2901
            is_false_407: 'bool33'
            if val_405 == 'false':
                is_false_407 = True
            else:
                if val_405 == '0':
                    t_2904 = True
                else:
                    if val_405 == 'no':
                        t_2903 = True
                    else:
                        t_2903 = val_405 == 'off'
                    t_2904 = t_2903
                is_false_407 = t_2904
            if not is_true_406:
                t_2906 = not is_false_407
            else:
                t_2906 = False
            if t_2906:
                eb_408: 'MutableSequence36[ChangesetError]' = list_5113(this_111.errors_353)
                eb_408.append(ChangesetError(field_403.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_2912 = this_111.table_def_350
                t_2913 = this_111.params_351
                t_2914 = this_111.changes_352
                t_4956 = tuple_5116(eb_408)
                return_197 = ChangesetImpl_100(t_2912, t_2913, t_2914, t_4956, False)
                fn_404.break_()
            return_197 = this_111
        return return_197
    def parse_bool_sql_part_409(this_112, val_410: 'str27') -> 'SqlBoolean':
        return_198: 'SqlBoolean'
        t_2889: 'bool33'
        t_2890: 'bool33'
        t_2891: 'bool33'
        t_2893: 'bool33'
        t_2894: 'bool33'
        t_2895: 'bool33'
        with Label35() as fn_411:
            if val_410 == 'true':
                t_2891 = True
            else:
                if val_410 == '1':
                    t_2890 = True
                else:
                    if val_410 == 'yes':
                        t_2889 = True
                    else:
                        t_2889 = val_410 == 'on'
                    t_2890 = t_2889
                t_2891 = t_2890
            if t_2891:
                return_198 = SqlBoolean(True)
                fn_411.break_()
            if val_410 == 'false':
                t_2895 = True
            else:
                if val_410 == '0':
                    t_2894 = True
                else:
                    if val_410 == 'no':
                        t_2893 = True
                    else:
                        t_2893 = val_410 == 'off'
                    t_2894 = t_2893
                t_2895 = t_2894
            if t_2895:
                return_198 = SqlBoolean(False)
                fn_411.break_()
            raise RuntimeError30()
        return return_198
    def value_to_sql_part_412(this_113, field_def_413: 'FieldDef', val_414: 'str27') -> 'SqlPart':
        return_199: 'SqlPart'
        t_2876: 'int31'
        t_2879: 'int64_23'
        t_2882: 'float38'
        t_2887: 'date26'
        with Label35() as fn_415:
            ft_416: 'FieldType' = field_def_413.field_type
            if isinstance39(ft_416, StringField):
                return_199 = SqlString(val_414)
                fn_415.break_()
            if isinstance39(ft_416, IntField):
                t_2876 = string_to_int32_5121(val_414)
                return_199 = SqlInt32(t_2876)
                fn_415.break_()
            if isinstance39(ft_416, Int64Field):
                t_2879 = string_to_int64_5122(val_414)
                return_199 = SqlInt64(t_2879)
                fn_415.break_()
            if isinstance39(ft_416, FloatField):
                t_2882 = string_to_float64_5123(val_414)
                return_199 = SqlFloat64(t_2882)
                fn_415.break_()
            if isinstance39(ft_416, BoolField):
                return_199 = this_113.parse_bool_sql_part_409(val_414)
                fn_415.break_()
            if isinstance39(ft_416, DateField):
                t_2887 = date_from_iso_string_5124(val_414)
                return_199 = SqlDate(t_2887)
                fn_415.break_()
            raise RuntimeError30()
        return return_199
    def to_insert_sql(this_114) -> 'SqlFragment':
        t_4897: 'int31'
        t_4902: 'str27'
        t_4903: 'bool33'
        t_4908: 'int31'
        t_4910: 'str27'
        t_4914: 'str27'
        t_4929: 'int31'
        t_2840: 'bool33'
        t_2848: 'FieldDef'
        t_2853: 'SqlPart'
        if not this_114.is_valid_354:
            raise RuntimeError30()
        i_419: 'int31' = 0
        while True:
            t_4897 = len_5117(this_114.table_def_350.fields)
            if not i_419 < t_4897:
                break
            f_420: 'FieldDef' = list_get_5125(this_114.table_def_350.fields, i_419)
            if not f_420.nullable:
                t_4902 = f_420.name.sql_value
                t_4903 = mapped_has_5114(this_114.changes_352, t_4902)
                t_2840 = not t_4903
            else:
                t_2840 = False
            if t_2840:
                raise RuntimeError30()
            i_419 = int_add_5126(i_419, 1)
        pairs_421: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_5127(this_114.changes_352)
        if len_5117(pairs_421) == 0:
            raise RuntimeError30()
        col_names_422: 'MutableSequence36[str27]' = list_5113()
        val_parts_423: 'MutableSequence36[SqlPart]' = list_5113()
        i_424: 'int31' = 0
        while True:
            t_4908 = len_5117(pairs_421)
            if not i_424 < t_4908:
                break
            pair_425: 'Pair25[str27, str27]' = list_get_5125(pairs_421, i_424)
            t_4910 = pair_425.key
            t_2848 = this_114.table_def_350.field(t_4910)
            fd_426: 'FieldDef' = t_2848
            col_names_422.append(fd_426.name.sql_value)
            t_4914 = pair_425.value
            t_2853 = this_114.value_to_sql_part_412(fd_426, t_4914)
            val_parts_423.append(t_2853)
            i_424 = int_add_5126(i_424, 1)
        b_427: 'SqlBuilder' = SqlBuilder()
        b_427.append_safe('INSERT INTO ')
        b_427.append_safe(this_114.table_def_350.table_name.sql_value)
        b_427.append_safe(' (')
        t_4922: 'Sequence29[str27]' = tuple_5116(col_names_422)
        def fn_4895(c_428: 'str27') -> 'str27':
            return c_428
        b_427.append_safe(list_join_5128(t_4922, ', ', fn_4895))
        b_427.append_safe(') VALUES (')
        b_427.append_part(list_get_5125(val_parts_423, 0))
        j_429: 'int31' = 1
        while True:
            t_4929 = len_5117(val_parts_423)
            if not j_429 < t_4929:
                break
            b_427.append_safe(', ')
            b_427.append_part(list_get_5125(val_parts_423, j_429))
            j_429 = int_add_5126(j_429, 1)
        b_427.append_safe(')')
        return b_427.accumulated
    def to_update_sql(this_115, id_431: 'int31') -> 'SqlFragment':
        t_4882: 'int31'
        t_4885: 'str27'
        t_4890: 'str27'
        t_2821: 'FieldDef'
        t_2827: 'SqlPart'
        if not this_115.is_valid_354:
            raise RuntimeError30()
        pairs_433: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_5127(this_115.changes_352)
        if len_5117(pairs_433) == 0:
            raise RuntimeError30()
        b_434: 'SqlBuilder' = SqlBuilder()
        b_434.append_safe('UPDATE ')
        b_434.append_safe(this_115.table_def_350.table_name.sql_value)
        b_434.append_safe(' SET ')
        i_435: 'int31' = 0
        while True:
            t_4882 = len_5117(pairs_433)
            if not i_435 < t_4882:
                break
            if i_435 > 0:
                b_434.append_safe(', ')
            pair_436: 'Pair25[str27, str27]' = list_get_5125(pairs_433, i_435)
            t_4885 = pair_436.key
            t_2821 = this_115.table_def_350.field(t_4885)
            fd_437: 'FieldDef' = t_2821
            b_434.append_safe(fd_437.name.sql_value)
            b_434.append_safe(' = ')
            t_4890 = pair_436.value
            t_2827 = this_115.value_to_sql_part_412(fd_437, t_4890)
            b_434.append_part(t_2827)
            i_435 = int_add_5126(i_435, 1)
        b_434.append_safe(' WHERE id = ')
        b_434.append_int32(id_431)
        return b_434.accumulated
    def __init__(this_182, table_def_439: 'TableDef', params_440: 'MappingProxyType32[str27, str27]', changes_441: 'MappingProxyType32[str27, str27]', errors_442: 'Sequence29[ChangesetError]', is_valid_443: 'bool33') -> None:
        this_182.table_def_350 = table_def_439
        this_182.params_351 = params_440
        this_182.changes_352 = changes_441
        this_182.errors_353 = errors_442
        this_182.is_valid_354 = is_valid_443
class OrderClause:
    field_538: 'SafeIdentifier'
    ascending_539: 'bool33'
    __slots__ = ('field_538', 'ascending_539')
    def __init__(this_206, field_541: 'SafeIdentifier', ascending_542: 'bool33') -> None:
        this_206.field_538 = field_541
        this_206.ascending_539 = ascending_542
    @property
    def field(this_932) -> 'SafeIdentifier':
        return this_932.field_538
    @property
    def ascending(this_935) -> 'bool33':
        return this_935.ascending_539
class Query:
    table_name_543: 'SafeIdentifier'
    conditions_544: 'Sequence29[SqlFragment]'
    selected_fields_545: 'Sequence29[SafeIdentifier]'
    order_clauses_546: 'Sequence29[OrderClause]'
    limit_val_547: 'Union40[int31, None]'
    offset_val_548: 'Union40[int31, None]'
    __slots__ = ('table_name_543', 'conditions_544', 'selected_fields_545', 'order_clauses_546', 'limit_val_547', 'offset_val_548')
    def where(this_116, condition_550: 'SqlFragment') -> 'Query':
        nb_552: 'MutableSequence36[SqlFragment]' = list_5113(this_116.conditions_544)
        nb_552.append(condition_550)
        return Query(this_116.table_name_543, tuple_5116(nb_552), this_116.selected_fields_545, this_116.order_clauses_546, this_116.limit_val_547, this_116.offset_val_548)
    def select(this_117, fields_554: 'Sequence29[SafeIdentifier]') -> 'Query':
        return Query(this_117.table_name_543, this_117.conditions_544, fields_554, this_117.order_clauses_546, this_117.limit_val_547, this_117.offset_val_548)
    def order_by(this_118, field_557: 'SafeIdentifier', ascending_558: 'bool33') -> 'Query':
        nb_560: 'MutableSequence36[OrderClause]' = list_5113(this_118.order_clauses_546)
        nb_560.append(OrderClause(field_557, ascending_558))
        return Query(this_118.table_name_543, this_118.conditions_544, this_118.selected_fields_545, tuple_5116(nb_560), this_118.limit_val_547, this_118.offset_val_548)
    def limit(this_119, n_562: 'int31') -> 'Query':
        if n_562 < 0:
            raise RuntimeError30()
        return Query(this_119.table_name_543, this_119.conditions_544, this_119.selected_fields_545, this_119.order_clauses_546, n_562, this_119.offset_val_548)
    def offset(this_120, n_565: 'int31') -> 'Query':
        if n_565 < 0:
            raise RuntimeError30()
        return Query(this_120.table_name_543, this_120.conditions_544, this_120.selected_fields_545, this_120.order_clauses_546, this_120.limit_val_547, n_565)
    def to_sql(this_121) -> 'SqlFragment':
        t_4466: 'int31'
        b_569: 'SqlBuilder' = SqlBuilder()
        b_569.append_safe('SELECT ')
        if not this_121.selected_fields_545:
            b_569.append_safe('*')
        else:
            def fn_4451(f_570: 'SafeIdentifier') -> 'str27':
                return f_570.sql_value
            b_569.append_safe(list_join_5128(this_121.selected_fields_545, ', ', fn_4451))
        b_569.append_safe(' FROM ')
        b_569.append_safe(this_121.table_name_543.sql_value)
        if not (not this_121.conditions_544):
            b_569.append_safe(' WHERE ')
            b_569.append_fragment(list_get_5125(this_121.conditions_544, 0))
            i_571: 'int31' = 1
            while True:
                t_4466 = len_5117(this_121.conditions_544)
                if not i_571 < t_4466:
                    break
                b_569.append_safe(' AND ')
                b_569.append_fragment(list_get_5125(this_121.conditions_544, i_571))
                i_571 = int_add_5126(i_571, 1)
        if not (not this_121.order_clauses_546):
            b_569.append_safe(' ORDER BY ')
            first_572: 'bool33' = True
            def fn_4450(oc_573: 'OrderClause') -> 'None':
                nonlocal first_572
                t_2442: 'str27'
                if not first_572:
                    b_569.append_safe(', ')
                first_572 = False
                t_4445: 'str27' = oc_573.field.sql_value
                b_569.append_safe(t_4445)
                if oc_573.ascending:
                    t_2442 = ' ASC'
                else:
                    t_2442 = ' DESC'
                b_569.append_safe(t_2442)
            list_for_each_5111(this_121.order_clauses_546, fn_4450)
        lv_574: 'Union40[int31, None]' = this_121.limit_val_547
        if not lv_574 is None:
            lv_1116: 'int31' = lv_574
            b_569.append_safe(' LIMIT ')
            b_569.append_int32(lv_1116)
        ov_575: 'Union40[int31, None]' = this_121.offset_val_548
        if not ov_575 is None:
            ov_1117: 'int31' = ov_575
            b_569.append_safe(' OFFSET ')
            b_569.append_int32(ov_1117)
        return b_569.accumulated
    def safe_to_sql(this_122, default_limit_577: 'int31') -> 'SqlFragment':
        return_221: 'SqlFragment'
        t_2435: 'Query'
        if default_limit_577 < 0:
            raise RuntimeError30()
        if not this_122.limit_val_547 is None:
            return_221 = this_122.to_sql()
        else:
            t_2435 = this_122.limit(default_limit_577)
            return_221 = t_2435.to_sql()
        return return_221
    def __init__(this_208, table_name_580: 'SafeIdentifier', conditions_581: 'Sequence29[SqlFragment]', selected_fields_582: 'Sequence29[SafeIdentifier]', order_clauses_583: 'Sequence29[OrderClause]', limit_val_584: 'Union40[int31, None]', offset_val_585: 'Union40[int31, None]') -> None:
        this_208.table_name_543 = table_name_580
        this_208.conditions_544 = conditions_581
        this_208.selected_fields_545 = selected_fields_582
        this_208.order_clauses_546 = order_clauses_583
        this_208.limit_val_547 = limit_val_584
        this_208.offset_val_548 = offset_val_585
    @property
    def table_name(this_938) -> 'SafeIdentifier':
        return this_938.table_name_543
    @property
    def conditions(this_941) -> 'Sequence29[SqlFragment]':
        return this_941.conditions_544
    @property
    def selected_fields(this_944) -> 'Sequence29[SafeIdentifier]':
        return this_944.selected_fields_545
    @property
    def order_clauses(this_947) -> 'Sequence29[OrderClause]':
        return this_947.order_clauses_546
    @property
    def limit_val(this_950) -> 'Union40[int31, None]':
        return this_950.limit_val_547
    @property
    def offset_val(this_953) -> 'Union40[int31, None]':
        return this_953.offset_val_548
class SafeIdentifier(metaclass = ABCMeta28):
    pass
class ValidatedIdentifier_124(SafeIdentifier):
    value_630: 'str27'
    __slots__ = ('value_630',)
    @property
    def sql_value(this_125) -> 'str27':
        return this_125.value_630
    def __init__(this_227, value_634: 'str27') -> None:
        this_227.value_630 = value_634
class FieldType(metaclass = ABCMeta28):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_233) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_235) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_237) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_239) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_241) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_243) -> None:
        pass
class FieldDef:
    name_648: 'SafeIdentifier'
    field_type_649: 'FieldType'
    nullable_650: 'bool33'
    __slots__ = ('name_648', 'field_type_649', 'nullable_650')
    def __init__(this_245, name_652: 'SafeIdentifier', field_type_653: 'FieldType', nullable_654: 'bool33') -> None:
        this_245.name_648 = name_652
        this_245.field_type_649 = field_type_653
        this_245.nullable_650 = nullable_654
    @property
    def name(this_870) -> 'SafeIdentifier':
        return this_870.name_648
    @property
    def field_type(this_873) -> 'FieldType':
        return this_873.field_type_649
    @property
    def nullable(this_876) -> 'bool33':
        return this_876.nullable_650
class TableDef:
    table_name_655: 'SafeIdentifier'
    fields_656: 'Sequence29[FieldDef]'
    __slots__ = ('table_name_655', 'fields_656')
    def field(this_126, name_658: 'str27') -> 'FieldDef':
        return_250: 'FieldDef'
        with Label35() as fn_659:
            this_3156: 'Sequence29[FieldDef]' = this_126.fields_656
            n_3157: 'int31' = len_5117(this_3156)
            i_3158: 'int31' = 0
            while i_3158 < n_3157:
                el_3159: 'FieldDef' = list_get_5125(this_3156, i_3158)
                i_3158 = int_add_5126(i_3158, 1)
                f_660: 'FieldDef' = el_3159
                if f_660.name.sql_value == name_658:
                    return_250 = f_660
                    fn_659.break_()
            raise RuntimeError30()
        return return_250
    def __init__(this_247, table_name_662: 'SafeIdentifier', fields_663: 'Sequence29[FieldDef]') -> None:
        this_247.table_name_655 = table_name_662
        this_247.fields_656 = fields_663
    @property
    def table_name(this_879) -> 'SafeIdentifier':
        return this_879.table_name_655
    @property
    def fields(this_882) -> 'Sequence29[FieldDef]':
        return this_882.fields_656
T_145 = TypeVar42('T_145', bound = Any41)
class SqlBuilder:
    buffer_683: 'MutableSequence36[SqlPart]'
    __slots__ = ('buffer_683',)
    def append_safe(this_127, sql_source_685: 'str27') -> 'None':
        t_5072: 'SqlSource' = SqlSource(sql_source_685)
        this_127.buffer_683.append(t_5072)
    def append_fragment(this_128, fragment_688: 'SqlFragment') -> 'None':
        t_5070: 'Sequence29[SqlPart]' = fragment_688.parts
        list_builder_add_all_5129(this_128.buffer_683, t_5070)
    def append_part(this_129, part_691: 'SqlPart') -> 'None':
        this_129.buffer_683.append(part_691)
    def append_part_list(this_130, values_694: 'Sequence29[SqlPart]') -> 'None':
        def fn_5066(x_696: 'SqlPart') -> 'None':
            this_130.append_part(x_696)
        this_130.append_list_739(values_694, fn_5066)
    def append_boolean(this_131, value_698: 'bool33') -> 'None':
        t_5063: 'SqlBoolean' = SqlBoolean(value_698)
        this_131.buffer_683.append(t_5063)
    def append_boolean_list(this_132, values_701: 'Sequence29[bool33]') -> 'None':
        def fn_5060(x_703: 'bool33') -> 'None':
            this_132.append_boolean(x_703)
        this_132.append_list_739(values_701, fn_5060)
    def append_date(this_133, value_705: 'date26') -> 'None':
        t_5057: 'SqlDate' = SqlDate(value_705)
        this_133.buffer_683.append(t_5057)
    def append_date_list(this_134, values_708: 'Sequence29[date26]') -> 'None':
        def fn_5054(x_710: 'date26') -> 'None':
            this_134.append_date(x_710)
        this_134.append_list_739(values_708, fn_5054)
    def append_float64(this_135, value_712: 'float38') -> 'None':
        t_5051: 'SqlFloat64' = SqlFloat64(value_712)
        this_135.buffer_683.append(t_5051)
    def append_float64_list(this_136, values_715: 'Sequence29[float38]') -> 'None':
        def fn_5048(x_717: 'float38') -> 'None':
            this_136.append_float64(x_717)
        this_136.append_list_739(values_715, fn_5048)
    def append_int32(this_137, value_719: 'int31') -> 'None':
        t_5045: 'SqlInt32' = SqlInt32(value_719)
        this_137.buffer_683.append(t_5045)
    def append_int32_list(this_138, values_722: 'Sequence29[int31]') -> 'None':
        def fn_5042(x_724: 'int31') -> 'None':
            this_138.append_int32(x_724)
        this_138.append_list_739(values_722, fn_5042)
    def append_int64(this_139, value_726: 'int64_23') -> 'None':
        t_5039: 'SqlInt64' = SqlInt64(value_726)
        this_139.buffer_683.append(t_5039)
    def append_int64_list(this_140, values_729: 'Sequence29[int64_23]') -> 'None':
        def fn_5036(x_731: 'int64_23') -> 'None':
            this_140.append_int64(x_731)
        this_140.append_list_739(values_729, fn_5036)
    def append_string(this_141, value_733: 'str27') -> 'None':
        t_5033: 'SqlString' = SqlString(value_733)
        this_141.buffer_683.append(t_5033)
    def append_string_list(this_142, values_736: 'Sequence29[str27]') -> 'None':
        def fn_5030(x_738: 'str27') -> 'None':
            this_142.append_string(x_738)
        this_142.append_list_739(values_736, fn_5030)
    def append_list_739(this_143, values_740: 'Sequence29[T_145]', append_value_741: 'Callable43[[T_145], None]') -> 'None':
        t_5025: 'int31'
        t_5027: 'T_145'
        i_743: 'int31' = 0
        while True:
            t_5025 = len_5117(values_740)
            if not i_743 < t_5025:
                break
            if i_743 > 0:
                this_143.append_safe(', ')
            t_5027 = list_get_5125(values_740, i_743)
            append_value_741(t_5027)
            i_743 = int_add_5126(i_743, 1)
    @property
    def accumulated(this_144) -> 'SqlFragment':
        return SqlFragment(tuple_5116(this_144.buffer_683))
    def __init__(this_252) -> None:
        t_5022: 'MutableSequence36[SqlPart]' = list_5113()
        this_252.buffer_683 = t_5022
class SqlFragment:
    parts_750: 'Sequence29[SqlPart]'
    __slots__ = ('parts_750',)
    def to_source(this_149) -> 'SqlSource':
        return SqlSource(this_149.to_string())
    def to_string(this_150) -> 'str27':
        t_5096: 'int31'
        builder_755: 'list3[str27]' = ['']
        i_756: 'int31' = 0
        while True:
            t_5096 = len_5117(this_150.parts_750)
            if not i_756 < t_5096:
                break
            list_get_5125(this_150.parts_750, i_756).format_to(builder_755)
            i_756 = int_add_5126(i_756, 1)
        return ''.join(builder_755)
    def __init__(this_273, parts_758: 'Sequence29[SqlPart]') -> None:
        this_273.parts_750 = parts_758
    @property
    def parts(this_888) -> 'Sequence29[SqlPart]':
        return this_888.parts_750
class SqlPart(metaclass = ABCMeta28):
    def format_to(this_151, builder_760: 'list3[str27]') -> 'None':
        raise RuntimeError30()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_762: 'str27'
    __slots__ = ('source_762',)
    def format_to(this_152, builder_764: 'list3[str27]') -> 'None':
        builder_764.append(this_152.source_762)
    def __init__(this_279, source_767: 'str27') -> None:
        this_279.source_762 = source_767
    @property
    def source(this_885) -> 'str27':
        return this_885.source_762
class SqlBoolean(SqlPart):
    value_768: 'bool33'
    __slots__ = ('value_768',)
    def format_to(this_153, builder_770: 'list3[str27]') -> 'None':
        t_3032: 'str27'
        if this_153.value_768:
            t_3032 = 'TRUE'
        else:
            t_3032 = 'FALSE'
        builder_770.append(t_3032)
    def __init__(this_282, value_773: 'bool33') -> None:
        this_282.value_768 = value_773
    @property
    def value(this_891) -> 'bool33':
        return this_891.value_768
class SqlDate(SqlPart):
    value_774: 'date26'
    __slots__ = ('value_774',)
    def format_to(this_154, builder_776: 'list3[str27]') -> 'None':
        builder_776.append("'")
        t_5077: 'str27' = date_to_string_5133(this_154.value_774)
        def fn_5075(c_778: 'int31') -> 'None':
            if c_778 == 39:
                builder_776.append("''")
            else:
                builder_776.append(string_from_code_point44(c_778))
        string_for_each_5135(t_5077, fn_5075)
        builder_776.append("'")
    def __init__(this_285, value_780: 'date26') -> None:
        this_285.value_774 = value_780
    @property
    def value(this_906) -> 'date26':
        return this_906.value_774
class SqlFloat64(SqlPart):
    value_781: 'float38'
    __slots__ = ('value_781',)
    def format_to(this_155, builder_783: 'list3[str27]') -> 'None':
        t_3021: 'bool33'
        t_3022: 'bool33'
        s_785: 'str27' = float64_to_string_5136(this_155.value_781)
        if s_785 == 'NaN':
            t_3022 = True
        else:
            if s_785 == 'Infinity':
                t_3021 = True
            else:
                t_3021 = s_785 == '-Infinity'
            t_3022 = t_3021
        if t_3022:
            builder_783.append('NULL')
        else:
            builder_783.append(s_785)
    def __init__(this_288, value_787: 'float38') -> None:
        this_288.value_781 = value_787
    @property
    def value(this_903) -> 'float38':
        return this_903.value_781
class SqlInt32(SqlPart):
    value_788: 'int31'
    __slots__ = ('value_788',)
    def format_to(this_156, builder_790: 'list3[str27]') -> 'None':
        t_5086: 'str27' = int_to_string_5120(this_156.value_788)
        builder_790.append(t_5086)
    def __init__(this_291, value_793: 'int31') -> None:
        this_291.value_788 = value_793
    @property
    def value(this_897) -> 'int31':
        return this_897.value_788
class SqlInt64(SqlPart):
    value_794: 'int64_23'
    __slots__ = ('value_794',)
    def format_to(this_157, builder_796: 'list3[str27]') -> 'None':
        t_5084: 'str27' = int_to_string_5120(this_157.value_794)
        builder_796.append(t_5084)
    def __init__(this_294, value_799: 'int64_23') -> None:
        this_294.value_794 = value_799
    @property
    def value(this_900) -> 'int64_23':
        return this_900.value_794
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_800: 'str27'
    __slots__ = ('value_800',)
    def format_to(this_158, builder_802: 'list3[str27]') -> 'None':
        builder_802.append("'")
        def fn_5089(c_804: 'int31') -> 'None':
            if c_804 == 39:
                builder_802.append("''")
            else:
                builder_802.append(string_from_code_point44(c_804))
        string_for_each_5135(this_158.value_800, fn_5089)
        builder_802.append("'")
    def __init__(this_297, value_806: 'str27') -> None:
        this_297.value_800 = value_806
    @property
    def value(this_894) -> 'str27':
        return this_894.value_800
def changeset(table_def_444: 'TableDef', params_445: 'MappingProxyType32[str27, str27]') -> 'Changeset':
    t_4872: 'MappingProxyType32[str27, str27]' = map_constructor_5137(())
    return ChangesetImpl_100(table_def_444, params_445, t_4872, (), True)
def is_ident_start_305(c_635: 'int31') -> 'bool33':
    return_230: 'bool33'
    t_2795: 'bool33'
    t_2796: 'bool33'
    if c_635 >= 97:
        t_2795 = c_635 <= 122
    else:
        t_2795 = False
    if t_2795:
        return_230 = True
    else:
        if c_635 >= 65:
            t_2796 = c_635 <= 90
        else:
            t_2796 = False
        if t_2796:
            return_230 = True
        else:
            return_230 = c_635 == 95
    return return_230
def is_ident_part_306(c_637: 'int31') -> 'bool33':
    return_231: 'bool33'
    if is_ident_start_305(c_637):
        return_231 = True
    elif c_637 >= 48:
        return_231 = c_637 <= 57
    else:
        return_231 = False
    return return_231
def safe_identifier(name_639: 'str27') -> 'SafeIdentifier':
    t_4870: 'int31'
    if not name_639:
        raise RuntimeError30()
    idx_641: 'int31' = 0
    if not is_ident_start_305(string_get_5138(name_639, idx_641)):
        raise RuntimeError30()
    t_4867: 'int31' = string_next_5139(name_639, idx_641)
    idx_641 = t_4867
    while True:
        if not len6(name_639) > idx_641:
            break
        if not is_ident_part_306(string_get_5138(name_639, idx_641)):
            raise RuntimeError30()
        t_4870 = string_next_5139(name_639, idx_641)
        idx_641 = t_4870
    return ValidatedIdentifier_124(name_639)
def delete_sql(table_def_534: 'TableDef', id_535: 'int31') -> 'SqlFragment':
    b_537: 'SqlBuilder' = SqlBuilder()
    b_537.append_safe('DELETE FROM ')
    b_537.append_safe(table_def_534.table_name.sql_value)
    b_537.append_safe(' WHERE id = ')
    b_537.append_int32(id_535)
    return b_537.accumulated
def from_(table_name_586: 'SafeIdentifier') -> 'Query':
    return Query(table_name_586, (), (), (), None, None)
