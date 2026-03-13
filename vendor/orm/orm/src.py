from builtins import str as str27, RuntimeError as RuntimeError30, int as int31, bool as bool33, Exception as Exception37, float as float38, isinstance as isinstance39, list as list3, len as len6, tuple as tuple5
from abc import ABCMeta as ABCMeta28
from typing import Sequence as Sequence29, Dict as Dict34, MutableSequence as MutableSequence36, Union as Union40, Any as Any41, TypeVar as TypeVar42, Callable as Callable43
from types import MappingProxyType as MappingProxyType32
from temper_core import Label as Label35, Pair as Pair25, string_from_code_point as string_from_code_point44, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, date_from_iso_string as date_from_iso_string13, list_get as list_get14, int_add as int_add15, mapped_to_list as mapped_to_list16, list_join as list_join17, list_builder_add_all as list_builder_add_all18, date_to_string as date_to_string19, string_for_each as string_for_each20, float64_to_string as float64_to_string21, map_constructor as map_constructor22, string_get as string_get23, string_next as string_next24
from datetime import date as date26
map_builder_set_7228 = map_builder_set0
list_for_each_7229 = list_for_each1
mapped_to_map_7230 = mapped_to_map2
list_7231 = list3
mapped_has_7232 = mapped_has4
tuple_7234 = tuple5
len_7235 = len6
string_count_between_7236 = string_count_between7
str_cat_7237 = str_cat8
int_to_string_7238 = int_to_string9
string_to_int32_7239 = string_to_int3210
string_to_int64_7240 = string_to_int6411
string_to_float64_7241 = string_to_float6412
date_from_iso_string_7242 = date_from_iso_string13
list_get_7243 = list_get14
int_add_7244 = int_add15
mapped_to_list_7245 = mapped_to_list16
list_join_7246 = list_join17
list_builder_add_all_7247 = list_builder_add_all18
date_to_string_7251 = date_to_string19
string_for_each_7253 = string_for_each20
float64_to_string_7254 = float64_to_string21
map_constructor_7255 = map_constructor22
string_get_7256 = string_get23
string_next_7257 = string_next24
pair_7259 = Pair25
date_7262 = date26
class ChangesetError:
    field_405: 'str27'
    message_406: 'str27'
    __slots__ = ('field_405', 'message_406')
    def __init__(this_212, field_408: 'str27', message_409: 'str27') -> None:
        this_212.field_405 = field_408
        this_212.message_406 = message_409
    @property
    def field(this_1134) -> 'str27':
        return this_1134.field_405
    @property
    def message(this_1137) -> 'str27':
        return this_1137.message_406
class Changeset(metaclass = ABCMeta28):
    def cast(this_120, allowed_fields_419: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_required(this_121, fields_422: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_length(this_122, field_425: 'SafeIdentifier', min_426: 'int31', max_427: 'int31') -> 'Changeset':
        raise RuntimeError30()
    def validate_int(this_123, field_430: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_int64(this_124, field_433: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_float(this_125, field_436: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_bool(this_126, field_439: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def to_insert_sql(this_127) -> 'SqlFragment':
        raise RuntimeError30()
    def to_update_sql(this_128, id_444: 'int31') -> 'SqlFragment':
        raise RuntimeError30()
class ChangesetImpl_129(Changeset):
    table_def_446: 'TableDef'
    params_447: 'MappingProxyType32[str27, str27]'
    changes_448: 'MappingProxyType32[str27, str27]'
    errors_449: 'Sequence29[ChangesetError]'
    is_valid_450: 'bool33'
    __slots__ = ('table_def_446', 'params_447', 'changes_448', 'errors_449', 'is_valid_450')
    @property
    def table_def(this_130) -> 'TableDef':
        return this_130.table_def_446
    @property
    def changes(this_131) -> 'MappingProxyType32[str27, str27]':
        return this_131.changes_448
    @property
    def errors(this_132) -> 'Sequence29[ChangesetError]':
        return this_132.errors_449
    @property
    def is_valid(this_133) -> 'bool33':
        return this_133.is_valid_450
    def cast(this_134, allowed_fields_460: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        mb_462: 'Dict34[str27, str27]' = {}
        def fn_7132(f_463: 'SafeIdentifier') -> 'None':
            t_7130: 'str27'
            t_7127: 'str27' = f_463.sql_value
            val_464: 'str27' = this_134.params_447.get(t_7127, '')
            if not (not val_464):
                t_7130 = f_463.sql_value
                map_builder_set_7228(mb_462, t_7130, val_464)
        list_for_each_7229(allowed_fields_460, fn_7132)
        return ChangesetImpl_129(this_134.table_def_446, this_134.params_447, mapped_to_map_7230(mb_462), this_134.errors_449, this_134.is_valid_450)
    def validate_required(this_135, fields_466: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        return_245: 'Changeset'
        t_7125: 'Sequence29[ChangesetError]'
        t_4163: 'TableDef'
        t_4164: 'MappingProxyType32[str27, str27]'
        t_4165: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_467:
            if not this_135.is_valid_450:
                return_245 = this_135
                fn_467.break_()
            eb_468: 'MutableSequence36[ChangesetError]' = list_7231(this_135.errors_449)
            valid_469: 'bool33' = True
            def fn_7121(f_470: 'SafeIdentifier') -> 'None':
                nonlocal valid_469
                t_7119: 'ChangesetError'
                t_7116: 'str27' = f_470.sql_value
                if not mapped_has_7232(this_135.changes_448, t_7116):
                    t_7119 = ChangesetError(f_470.sql_value, 'is required')
                    eb_468.append(t_7119)
                    valid_469 = False
            list_for_each_7229(fields_466, fn_7121)
            t_4163 = this_135.table_def_446
            t_4164 = this_135.params_447
            t_4165 = this_135.changes_448
            t_7125 = tuple_7234(eb_468)
            return_245 = ChangesetImpl_129(t_4163, t_4164, t_4165, t_7125, valid_469)
        return return_245
    def validate_length(this_136, field_472: 'SafeIdentifier', min_473: 'int31', max_474: 'int31') -> 'Changeset':
        return_246: 'Changeset'
        t_7103: 'str27'
        t_7114: 'Sequence29[ChangesetError]'
        t_4146: 'bool33'
        t_4152: 'TableDef'
        t_4153: 'MappingProxyType32[str27, str27]'
        t_4154: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_475:
            if not this_136.is_valid_450:
                return_246 = this_136
                fn_475.break_()
            t_7103 = field_472.sql_value
            val_476: 'str27' = this_136.changes_448.get(t_7103, '')
            len_477: 'int31' = string_count_between_7236(val_476, 0, len_7235(val_476))
            if len_477 < min_473:
                t_4146 = True
            else:
                t_4146 = len_477 > max_474
            if t_4146:
                msg_478: 'str27' = str_cat_7237('must be between ', int_to_string_7238(min_473), ' and ', int_to_string_7238(max_474), ' characters')
                eb_479: 'MutableSequence36[ChangesetError]' = list_7231(this_136.errors_449)
                eb_479.append(ChangesetError(field_472.sql_value, msg_478))
                t_4152 = this_136.table_def_446
                t_4153 = this_136.params_447
                t_4154 = this_136.changes_448
                t_7114 = tuple_7234(eb_479)
                return_246 = ChangesetImpl_129(t_4152, t_4153, t_4154, t_7114, False)
                fn_475.break_()
            return_246 = this_136
        return return_246
    def validate_int(this_137, field_481: 'SafeIdentifier') -> 'Changeset':
        return_247: 'Changeset'
        t_7094: 'str27'
        t_7101: 'Sequence29[ChangesetError]'
        t_4137: 'TableDef'
        t_4138: 'MappingProxyType32[str27, str27]'
        t_4139: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_482:
            if not this_137.is_valid_450:
                return_247 = this_137
                fn_482.break_()
            t_7094 = field_481.sql_value
            val_483: 'str27' = this_137.changes_448.get(t_7094, '')
            if not val_483:
                return_247 = this_137
                fn_482.break_()
            parse_ok_484: 'bool33'
            try:
                string_to_int32_7239(val_483)
                parse_ok_484 = True
            except Exception37:
                parse_ok_484 = False
            if not parse_ok_484:
                eb_485: 'MutableSequence36[ChangesetError]' = list_7231(this_137.errors_449)
                eb_485.append(ChangesetError(field_481.sql_value, 'must be an integer'))
                t_4137 = this_137.table_def_446
                t_4138 = this_137.params_447
                t_4139 = this_137.changes_448
                t_7101 = tuple_7234(eb_485)
                return_247 = ChangesetImpl_129(t_4137, t_4138, t_4139, t_7101, False)
                fn_482.break_()
            return_247 = this_137
        return return_247
    def validate_int64(this_138, field_487: 'SafeIdentifier') -> 'Changeset':
        return_248: 'Changeset'
        t_7085: 'str27'
        t_7092: 'Sequence29[ChangesetError]'
        t_4124: 'TableDef'
        t_4125: 'MappingProxyType32[str27, str27]'
        t_4126: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_488:
            if not this_138.is_valid_450:
                return_248 = this_138
                fn_488.break_()
            t_7085 = field_487.sql_value
            val_489: 'str27' = this_138.changes_448.get(t_7085, '')
            if not val_489:
                return_248 = this_138
                fn_488.break_()
            parse_ok_490: 'bool33'
            try:
                string_to_int64_7240(val_489)
                parse_ok_490 = True
            except Exception37:
                parse_ok_490 = False
            if not parse_ok_490:
                eb_491: 'MutableSequence36[ChangesetError]' = list_7231(this_138.errors_449)
                eb_491.append(ChangesetError(field_487.sql_value, 'must be a 64-bit integer'))
                t_4124 = this_138.table_def_446
                t_4125 = this_138.params_447
                t_4126 = this_138.changes_448
                t_7092 = tuple_7234(eb_491)
                return_248 = ChangesetImpl_129(t_4124, t_4125, t_4126, t_7092, False)
                fn_488.break_()
            return_248 = this_138
        return return_248
    def validate_float(this_139, field_493: 'SafeIdentifier') -> 'Changeset':
        return_249: 'Changeset'
        t_7076: 'str27'
        t_7083: 'Sequence29[ChangesetError]'
        t_4111: 'TableDef'
        t_4112: 'MappingProxyType32[str27, str27]'
        t_4113: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_494:
            if not this_139.is_valid_450:
                return_249 = this_139
                fn_494.break_()
            t_7076 = field_493.sql_value
            val_495: 'str27' = this_139.changes_448.get(t_7076, '')
            if not val_495:
                return_249 = this_139
                fn_494.break_()
            parse_ok_496: 'bool33'
            try:
                string_to_float64_7241(val_495)
                parse_ok_496 = True
            except Exception37:
                parse_ok_496 = False
            if not parse_ok_496:
                eb_497: 'MutableSequence36[ChangesetError]' = list_7231(this_139.errors_449)
                eb_497.append(ChangesetError(field_493.sql_value, 'must be a number'))
                t_4111 = this_139.table_def_446
                t_4112 = this_139.params_447
                t_4113 = this_139.changes_448
                t_7083 = tuple_7234(eb_497)
                return_249 = ChangesetImpl_129(t_4111, t_4112, t_4113, t_7083, False)
                fn_494.break_()
            return_249 = this_139
        return return_249
    def validate_bool(this_140, field_499: 'SafeIdentifier') -> 'Changeset':
        return_250: 'Changeset'
        t_7067: 'str27'
        t_7074: 'Sequence29[ChangesetError]'
        t_4086: 'bool33'
        t_4087: 'bool33'
        t_4089: 'bool33'
        t_4090: 'bool33'
        t_4092: 'bool33'
        t_4098: 'TableDef'
        t_4099: 'MappingProxyType32[str27, str27]'
        t_4100: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_500:
            if not this_140.is_valid_450:
                return_250 = this_140
                fn_500.break_()
            t_7067 = field_499.sql_value
            val_501: 'str27' = this_140.changes_448.get(t_7067, '')
            if not val_501:
                return_250 = this_140
                fn_500.break_()
            is_true_502: 'bool33'
            if val_501 == 'true':
                is_true_502 = True
            else:
                if val_501 == '1':
                    t_4087 = True
                else:
                    if val_501 == 'yes':
                        t_4086 = True
                    else:
                        t_4086 = val_501 == 'on'
                    t_4087 = t_4086
                is_true_502 = t_4087
            is_false_503: 'bool33'
            if val_501 == 'false':
                is_false_503 = True
            else:
                if val_501 == '0':
                    t_4090 = True
                else:
                    if val_501 == 'no':
                        t_4089 = True
                    else:
                        t_4089 = val_501 == 'off'
                    t_4090 = t_4089
                is_false_503 = t_4090
            if not is_true_502:
                t_4092 = not is_false_503
            else:
                t_4092 = False
            if t_4092:
                eb_504: 'MutableSequence36[ChangesetError]' = list_7231(this_140.errors_449)
                eb_504.append(ChangesetError(field_499.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_4098 = this_140.table_def_446
                t_4099 = this_140.params_447
                t_4100 = this_140.changes_448
                t_7074 = tuple_7234(eb_504)
                return_250 = ChangesetImpl_129(t_4098, t_4099, t_4100, t_7074, False)
                fn_500.break_()
            return_250 = this_140
        return return_250
    def parse_bool_sql_part_505(this_141, val_506: 'str27') -> 'SqlBoolean':
        return_251: 'SqlBoolean'
        t_4075: 'bool33'
        t_4076: 'bool33'
        t_4077: 'bool33'
        t_4079: 'bool33'
        t_4080: 'bool33'
        t_4081: 'bool33'
        with Label35() as fn_507:
            if val_506 == 'true':
                t_4077 = True
            else:
                if val_506 == '1':
                    t_4076 = True
                else:
                    if val_506 == 'yes':
                        t_4075 = True
                    else:
                        t_4075 = val_506 == 'on'
                    t_4076 = t_4075
                t_4077 = t_4076
            if t_4077:
                return_251 = SqlBoolean(True)
                fn_507.break_()
            if val_506 == 'false':
                t_4081 = True
            else:
                if val_506 == '0':
                    t_4080 = True
                else:
                    if val_506 == 'no':
                        t_4079 = True
                    else:
                        t_4079 = val_506 == 'off'
                    t_4080 = t_4079
                t_4081 = t_4080
            if t_4081:
                return_251 = SqlBoolean(False)
                fn_507.break_()
            raise RuntimeError30()
        return return_251
    def value_to_sql_part_508(this_142, field_def_509: 'FieldDef', val_510: 'str27') -> 'SqlPart':
        return_252: 'SqlPart'
        t_4062: 'int31'
        t_4065: 'int64_23'
        t_4068: 'float38'
        t_4073: 'date26'
        with Label35() as fn_511:
            ft_512: 'FieldType' = field_def_509.field_type
            if isinstance39(ft_512, StringField):
                return_252 = SqlString(val_510)
                fn_511.break_()
            if isinstance39(ft_512, IntField):
                t_4062 = string_to_int32_7239(val_510)
                return_252 = SqlInt32(t_4062)
                fn_511.break_()
            if isinstance39(ft_512, Int64Field):
                t_4065 = string_to_int64_7240(val_510)
                return_252 = SqlInt64(t_4065)
                fn_511.break_()
            if isinstance39(ft_512, FloatField):
                t_4068 = string_to_float64_7241(val_510)
                return_252 = SqlFloat64(t_4068)
                fn_511.break_()
            if isinstance39(ft_512, BoolField):
                return_252 = this_142.parse_bool_sql_part_505(val_510)
                fn_511.break_()
            if isinstance39(ft_512, DateField):
                t_4073 = date_from_iso_string_7242(val_510)
                return_252 = SqlDate(t_4073)
                fn_511.break_()
            raise RuntimeError30()
        return return_252
    def to_insert_sql(this_143) -> 'SqlFragment':
        t_7015: 'int31'
        t_7020: 'str27'
        t_7021: 'bool33'
        t_7026: 'int31'
        t_7028: 'str27'
        t_7032: 'str27'
        t_7047: 'int31'
        t_4026: 'bool33'
        t_4034: 'FieldDef'
        t_4039: 'SqlPart'
        if not this_143.is_valid_450:
            raise RuntimeError30()
        i_515: 'int31' = 0
        while True:
            t_7015 = len_7235(this_143.table_def_446.fields)
            if not i_515 < t_7015:
                break
            f_516: 'FieldDef' = list_get_7243(this_143.table_def_446.fields, i_515)
            if not f_516.nullable:
                t_7020 = f_516.name.sql_value
                t_7021 = mapped_has_7232(this_143.changes_448, t_7020)
                t_4026 = not t_7021
            else:
                t_4026 = False
            if t_4026:
                raise RuntimeError30()
            i_515 = int_add_7244(i_515, 1)
        pairs_517: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_7245(this_143.changes_448)
        if len_7235(pairs_517) == 0:
            raise RuntimeError30()
        col_names_518: 'MutableSequence36[str27]' = list_7231()
        val_parts_519: 'MutableSequence36[SqlPart]' = list_7231()
        i_520: 'int31' = 0
        while True:
            t_7026 = len_7235(pairs_517)
            if not i_520 < t_7026:
                break
            pair_521: 'Pair25[str27, str27]' = list_get_7243(pairs_517, i_520)
            t_7028 = pair_521.key
            t_4034 = this_143.table_def_446.field(t_7028)
            fd_522: 'FieldDef' = t_4034
            col_names_518.append(fd_522.name.sql_value)
            t_7032 = pair_521.value
            t_4039 = this_143.value_to_sql_part_508(fd_522, t_7032)
            val_parts_519.append(t_4039)
            i_520 = int_add_7244(i_520, 1)
        b_523: 'SqlBuilder' = SqlBuilder()
        b_523.append_safe('INSERT INTO ')
        b_523.append_safe(this_143.table_def_446.table_name.sql_value)
        b_523.append_safe(' (')
        t_7040: 'Sequence29[str27]' = tuple_7234(col_names_518)
        def fn_7013(c_524: 'str27') -> 'str27':
            return c_524
        b_523.append_safe(list_join_7246(t_7040, ', ', fn_7013))
        b_523.append_safe(') VALUES (')
        b_523.append_part(list_get_7243(val_parts_519, 0))
        j_525: 'int31' = 1
        while True:
            t_7047 = len_7235(val_parts_519)
            if not j_525 < t_7047:
                break
            b_523.append_safe(', ')
            b_523.append_part(list_get_7243(val_parts_519, j_525))
            j_525 = int_add_7244(j_525, 1)
        b_523.append_safe(')')
        return b_523.accumulated
    def to_update_sql(this_144, id_527: 'int31') -> 'SqlFragment':
        t_7000: 'int31'
        t_7003: 'str27'
        t_7008: 'str27'
        t_4007: 'FieldDef'
        t_4013: 'SqlPart'
        if not this_144.is_valid_450:
            raise RuntimeError30()
        pairs_529: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_7245(this_144.changes_448)
        if len_7235(pairs_529) == 0:
            raise RuntimeError30()
        b_530: 'SqlBuilder' = SqlBuilder()
        b_530.append_safe('UPDATE ')
        b_530.append_safe(this_144.table_def_446.table_name.sql_value)
        b_530.append_safe(' SET ')
        i_531: 'int31' = 0
        while True:
            t_7000 = len_7235(pairs_529)
            if not i_531 < t_7000:
                break
            if i_531 > 0:
                b_530.append_safe(', ')
            pair_532: 'Pair25[str27, str27]' = list_get_7243(pairs_529, i_531)
            t_7003 = pair_532.key
            t_4007 = this_144.table_def_446.field(t_7003)
            fd_533: 'FieldDef' = t_4007
            b_530.append_safe(fd_533.name.sql_value)
            b_530.append_safe(' = ')
            t_7008 = pair_532.value
            t_4013 = this_144.value_to_sql_part_508(fd_533, t_7008)
            b_530.append_part(t_4013)
            i_531 = int_add_7244(i_531, 1)
        b_530.append_safe(' WHERE id = ')
        b_530.append_int32(id_527)
        return b_530.accumulated
    def __init__(this_235, table_def_535: 'TableDef', params_536: 'MappingProxyType32[str27, str27]', changes_537: 'MappingProxyType32[str27, str27]', errors_538: 'Sequence29[ChangesetError]', is_valid_539: 'bool33') -> None:
        this_235.table_def_446 = table_def_535
        this_235.params_447 = params_536
        this_235.changes_448 = changes_537
        this_235.errors_449 = errors_538
        this_235.is_valid_450 = is_valid_539
class JoinType(metaclass = ABCMeta28):
    def keyword(this_145) -> 'str27':
        raise RuntimeError30()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_146) -> 'str27':
        return 'INNER JOIN'
    def __init__(this_260) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_147) -> 'str27':
        return 'LEFT JOIN'
    def __init__(this_263) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_148) -> 'str27':
        return 'RIGHT JOIN'
    def __init__(this_266) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_149) -> 'str27':
        return 'FULL OUTER JOIN'
    def __init__(this_269) -> None:
        pass
class JoinClause:
    join_type_648: 'JoinType'
    table_649: 'SafeIdentifier'
    on_condition_650: 'SqlFragment'
    __slots__ = ('join_type_648', 'table_649', 'on_condition_650')
    def __init__(this_272, join_type_652: 'JoinType', table_653: 'SafeIdentifier', on_condition_654: 'SqlFragment') -> None:
        this_272.join_type_648 = join_type_652
        this_272.table_649 = table_653
        this_272.on_condition_650 = on_condition_654
    @property
    def join_type(this_1202) -> 'JoinType':
        return this_1202.join_type_648
    @property
    def table(this_1205) -> 'SafeIdentifier':
        return this_1205.table_649
    @property
    def on_condition(this_1208) -> 'SqlFragment':
        return this_1208.on_condition_650
class OrderClause:
    field_655: 'SafeIdentifier'
    ascending_656: 'bool33'
    __slots__ = ('field_655', 'ascending_656')
    def __init__(this_274, field_658: 'SafeIdentifier', ascending_659: 'bool33') -> None:
        this_274.field_655 = field_658
        this_274.ascending_656 = ascending_659
    @property
    def field(this_1211) -> 'SafeIdentifier':
        return this_1211.field_655
    @property
    def ascending(this_1214) -> 'bool33':
        return this_1214.ascending_656
class WhereClause(metaclass = ABCMeta28):
    def keyword(this_151) -> 'str27':
        raise RuntimeError30()
class AndCondition(WhereClause):
    condition_664: 'SqlFragment'
    __slots__ = ('condition_664',)
    @property
    def condition(this_152) -> 'SqlFragment':
        return this_152.condition_664
    def keyword(this_153) -> 'str27':
        return 'AND'
    def __init__(this_280, condition_670: 'SqlFragment') -> None:
        this_280.condition_664 = condition_670
class OrCondition(WhereClause):
    condition_671: 'SqlFragment'
    __slots__ = ('condition_671',)
    @property
    def condition(this_154) -> 'SqlFragment':
        return this_154.condition_671
    def keyword(this_155) -> 'str27':
        return 'OR'
    def __init__(this_285, condition_677: 'SqlFragment') -> None:
        this_285.condition_671 = condition_677
class Query:
    table_name_678: 'SafeIdentifier'
    conditions_679: 'Sequence29[WhereClause]'
    selected_fields_680: 'Sequence29[SafeIdentifier]'
    order_clauses_681: 'Sequence29[OrderClause]'
    limit_val_682: 'Union40[int31, None]'
    offset_val_683: 'Union40[int31, None]'
    join_clauses_684: 'Sequence29[JoinClause]'
    __slots__ = ('table_name_678', 'conditions_679', 'selected_fields_680', 'order_clauses_681', 'limit_val_682', 'offset_val_683', 'join_clauses_684')
    def where(this_156, condition_686: 'SqlFragment') -> 'Query':
        nb_688: 'MutableSequence36[WhereClause]' = list_7231(this_156.conditions_679)
        nb_688.append(AndCondition(condition_686))
        return Query(this_156.table_name_678, tuple_7234(nb_688), this_156.selected_fields_680, this_156.order_clauses_681, this_156.limit_val_682, this_156.offset_val_683, this_156.join_clauses_684)
    def or_where(this_157, condition_690: 'SqlFragment') -> 'Query':
        nb_692: 'MutableSequence36[WhereClause]' = list_7231(this_157.conditions_679)
        nb_692.append(OrCondition(condition_690))
        return Query(this_157.table_name_678, tuple_7234(nb_692), this_157.selected_fields_680, this_157.order_clauses_681, this_157.limit_val_682, this_157.offset_val_683, this_157.join_clauses_684)
    def where_null(this_158, field_694: 'SafeIdentifier') -> 'Query':
        b_696: 'SqlBuilder' = SqlBuilder()
        b_696.append_safe(field_694.sql_value)
        b_696.append_safe(' IS NULL')
        t_6599: 'SqlFragment' = b_696.accumulated
        return this_158.where(t_6599)
    def where_not_null(this_159, field_698: 'SafeIdentifier') -> 'Query':
        b_700: 'SqlBuilder' = SqlBuilder()
        b_700.append_safe(field_698.sql_value)
        b_700.append_safe(' IS NOT NULL')
        t_6593: 'SqlFragment' = b_700.accumulated
        return this_159.where(t_6593)
    def where_in(this_160, field_702: 'SafeIdentifier', values_703: 'Sequence29[SqlPart]') -> 'Query':
        return_301: 'Query'
        t_6574: 'SqlFragment'
        t_6582: 'int31'
        t_6587: 'SqlFragment'
        with Label35() as fn_704:
            if not values_703:
                b_705: 'SqlBuilder' = SqlBuilder()
                b_705.append_safe('1 = 0')
                t_6574 = b_705.accumulated
                return_301 = this_160.where(t_6574)
                fn_704.break_()
            b_706: 'SqlBuilder' = SqlBuilder()
            b_706.append_safe(field_702.sql_value)
            b_706.append_safe(' IN (')
            b_706.append_part(list_get_7243(values_703, 0))
            i_707: 'int31' = 1
            while True:
                t_6582 = len_7235(values_703)
                if not i_707 < t_6582:
                    break
                b_706.append_safe(', ')
                b_706.append_part(list_get_7243(values_703, i_707))
                i_707 = int_add_7244(i_707, 1)
            b_706.append_safe(')')
            t_6587 = b_706.accumulated
            return_301 = this_160.where(t_6587)
        return return_301
    def where_not(this_161, condition_709: 'SqlFragment') -> 'Query':
        b_711: 'SqlBuilder' = SqlBuilder()
        b_711.append_safe('NOT (')
        b_711.append_fragment(condition_709)
        b_711.append_safe(')')
        t_6569: 'SqlFragment' = b_711.accumulated
        return this_161.where(t_6569)
    def where_between(this_162, field_713: 'SafeIdentifier', low_714: 'SqlPart', high_715: 'SqlPart') -> 'Query':
        b_717: 'SqlBuilder' = SqlBuilder()
        b_717.append_safe(field_713.sql_value)
        b_717.append_safe(' BETWEEN ')
        b_717.append_part(low_714)
        b_717.append_safe(' AND ')
        b_717.append_part(high_715)
        t_6563: 'SqlFragment' = b_717.accumulated
        return this_162.where(t_6563)
    def where_like(this_163, field_719: 'SafeIdentifier', pattern_720: 'str27') -> 'Query':
        b_722: 'SqlBuilder' = SqlBuilder()
        b_722.append_safe(field_719.sql_value)
        b_722.append_safe(' LIKE ')
        b_722.append_string(pattern_720)
        t_6554: 'SqlFragment' = b_722.accumulated
        return this_163.where(t_6554)
    def where_i_like(this_164, field_724: 'SafeIdentifier', pattern_725: 'str27') -> 'Query':
        b_727: 'SqlBuilder' = SqlBuilder()
        b_727.append_safe(field_724.sql_value)
        b_727.append_safe(' ILIKE ')
        b_727.append_string(pattern_725)
        t_6547: 'SqlFragment' = b_727.accumulated
        return this_164.where(t_6547)
    def select(this_165, fields_729: 'Sequence29[SafeIdentifier]') -> 'Query':
        return Query(this_165.table_name_678, this_165.conditions_679, fields_729, this_165.order_clauses_681, this_165.limit_val_682, this_165.offset_val_683, this_165.join_clauses_684)
    def order_by(this_166, field_732: 'SafeIdentifier', ascending_733: 'bool33') -> 'Query':
        nb_735: 'MutableSequence36[OrderClause]' = list_7231(this_166.order_clauses_681)
        nb_735.append(OrderClause(field_732, ascending_733))
        return Query(this_166.table_name_678, this_166.conditions_679, this_166.selected_fields_680, tuple_7234(nb_735), this_166.limit_val_682, this_166.offset_val_683, this_166.join_clauses_684)
    def limit(this_167, n_737: 'int31') -> 'Query':
        if n_737 < 0:
            raise RuntimeError30()
        return Query(this_167.table_name_678, this_167.conditions_679, this_167.selected_fields_680, this_167.order_clauses_681, n_737, this_167.offset_val_683, this_167.join_clauses_684)
    def offset(this_168, n_740: 'int31') -> 'Query':
        if n_740 < 0:
            raise RuntimeError30()
        return Query(this_168.table_name_678, this_168.conditions_679, this_168.selected_fields_680, this_168.order_clauses_681, this_168.limit_val_682, n_740, this_168.join_clauses_684)
    def join(this_169, join_type_743: 'JoinType', table_744: 'SafeIdentifier', on_condition_745: 'SqlFragment') -> 'Query':
        nb_747: 'MutableSequence36[JoinClause]' = list_7231(this_169.join_clauses_684)
        nb_747.append(JoinClause(join_type_743, table_744, on_condition_745))
        return Query(this_169.table_name_678, this_169.conditions_679, this_169.selected_fields_680, this_169.order_clauses_681, this_169.limit_val_682, this_169.offset_val_683, tuple_7234(nb_747))
    def inner_join(this_170, table_749: 'SafeIdentifier', on_condition_750: 'SqlFragment') -> 'Query':
        t_6518: 'InnerJoin' = InnerJoin()
        return this_170.join(t_6518, table_749, on_condition_750)
    def left_join(this_171, table_753: 'SafeIdentifier', on_condition_754: 'SqlFragment') -> 'Query':
        t_6516: 'LeftJoin' = LeftJoin()
        return this_171.join(t_6516, table_753, on_condition_754)
    def right_join(this_172, table_757: 'SafeIdentifier', on_condition_758: 'SqlFragment') -> 'Query':
        t_6514: 'RightJoin' = RightJoin()
        return this_172.join(t_6514, table_757, on_condition_758)
    def full_join(this_173, table_761: 'SafeIdentifier', on_condition_762: 'SqlFragment') -> 'Query':
        t_6512: 'FullJoin' = FullJoin()
        return this_173.join(t_6512, table_761, on_condition_762)
    def to_sql(this_174) -> 'SqlFragment':
        t_6494: 'int31'
        b_766: 'SqlBuilder' = SqlBuilder()
        b_766.append_safe('SELECT ')
        if not this_174.selected_fields_680:
            b_766.append_safe('*')
        else:
            def fn_6476(f_767: 'SafeIdentifier') -> 'str27':
                return f_767.sql_value
            b_766.append_safe(list_join_7246(this_174.selected_fields_680, ', ', fn_6476))
        b_766.append_safe(' FROM ')
        b_766.append_safe(this_174.table_name_678.sql_value)
        def fn_6475(jc_768: 'JoinClause') -> 'None':
            b_766.append_safe(' ')
            t_6464: 'str27' = jc_768.join_type.keyword()
            b_766.append_safe(t_6464)
            b_766.append_safe(' ')
            t_6468: 'str27' = jc_768.table.sql_value
            b_766.append_safe(t_6468)
            b_766.append_safe(' ON ')
            t_6471: 'SqlFragment' = jc_768.on_condition
            b_766.append_fragment(t_6471)
        list_for_each_7229(this_174.join_clauses_684, fn_6475)
        if not (not this_174.conditions_679):
            b_766.append_safe(' WHERE ')
            b_766.append_fragment(list_get_7243(this_174.conditions_679, 0).condition)
            i_769: 'int31' = 1
            while True:
                t_6494 = len_7235(this_174.conditions_679)
                if not i_769 < t_6494:
                    break
                b_766.append_safe(' ')
                b_766.append_safe(list_get_7243(this_174.conditions_679, i_769).keyword())
                b_766.append_safe(' ')
                b_766.append_fragment(list_get_7243(this_174.conditions_679, i_769).condition)
                i_769 = int_add_7244(i_769, 1)
        if not (not this_174.order_clauses_681):
            b_766.append_safe(' ORDER BY ')
            first_770: 'bool33' = True
            def fn_6474(oc_771: 'OrderClause') -> 'None':
                nonlocal first_770
                t_3520: 'str27'
                if not first_770:
                    b_766.append_safe(', ')
                first_770 = False
                t_6458: 'str27' = oc_771.field.sql_value
                b_766.append_safe(t_6458)
                if oc_771.ascending:
                    t_3520 = ' ASC'
                else:
                    t_3520 = ' DESC'
                b_766.append_safe(t_3520)
            list_for_each_7229(this_174.order_clauses_681, fn_6474)
        lv_772: 'Union40[int31, None]' = this_174.limit_val_682
        if not lv_772 is None:
            lv_1452: 'int31' = lv_772
            b_766.append_safe(' LIMIT ')
            b_766.append_int32(lv_1452)
        ov_773: 'Union40[int31, None]' = this_174.offset_val_683
        if not ov_773 is None:
            ov_1453: 'int31' = ov_773
            b_766.append_safe(' OFFSET ')
            b_766.append_int32(ov_1453)
        return b_766.accumulated
    def safe_to_sql(this_175, default_limit_775: 'int31') -> 'SqlFragment':
        return_316: 'SqlFragment'
        t_3513: 'Query'
        if default_limit_775 < 0:
            raise RuntimeError30()
        if not this_175.limit_val_682 is None:
            return_316 = this_175.to_sql()
        else:
            t_3513 = this_175.limit(default_limit_775)
            return_316 = t_3513.to_sql()
        return return_316
    def __init__(this_289, table_name_778: 'SafeIdentifier', conditions_779: 'Sequence29[WhereClause]', selected_fields_780: 'Sequence29[SafeIdentifier]', order_clauses_781: 'Sequence29[OrderClause]', limit_val_782: 'Union40[int31, None]', offset_val_783: 'Union40[int31, None]', join_clauses_784: 'Sequence29[JoinClause]') -> None:
        this_289.table_name_678 = table_name_778
        this_289.conditions_679 = conditions_779
        this_289.selected_fields_680 = selected_fields_780
        this_289.order_clauses_681 = order_clauses_781
        this_289.limit_val_682 = limit_val_782
        this_289.offset_val_683 = offset_val_783
        this_289.join_clauses_684 = join_clauses_784
    @property
    def table_name(this_1217) -> 'SafeIdentifier':
        return this_1217.table_name_678
    @property
    def conditions(this_1220) -> 'Sequence29[WhereClause]':
        return this_1220.conditions_679
    @property
    def selected_fields(this_1223) -> 'Sequence29[SafeIdentifier]':
        return this_1223.selected_fields_680
    @property
    def order_clauses(this_1226) -> 'Sequence29[OrderClause]':
        return this_1226.order_clauses_681
    @property
    def limit_val(this_1229) -> 'Union40[int31, None]':
        return this_1229.limit_val_682
    @property
    def offset_val(this_1232) -> 'Union40[int31, None]':
        return this_1232.offset_val_683
    @property
    def join_clauses(this_1235) -> 'Sequence29[JoinClause]':
        return this_1235.join_clauses_684
class SafeIdentifier(metaclass = ABCMeta28):
    pass
class ValidatedIdentifier_177(SafeIdentifier):
    value_894: 'str27'
    __slots__ = ('value_894',)
    @property
    def sql_value(this_178) -> 'str27':
        return this_178.value_894
    def __init__(this_323, value_898: 'str27') -> None:
        this_323.value_894 = value_898
class FieldType(metaclass = ABCMeta28):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_329) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_331) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_333) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_335) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_337) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_339) -> None:
        pass
class FieldDef:
    name_912: 'SafeIdentifier'
    field_type_913: 'FieldType'
    nullable_914: 'bool33'
    __slots__ = ('name_912', 'field_type_913', 'nullable_914')
    def __init__(this_341, name_916: 'SafeIdentifier', field_type_917: 'FieldType', nullable_918: 'bool33') -> None:
        this_341.name_912 = name_916
        this_341.field_type_913 = field_type_917
        this_341.nullable_914 = nullable_918
    @property
    def name(this_1140) -> 'SafeIdentifier':
        return this_1140.name_912
    @property
    def field_type(this_1143) -> 'FieldType':
        return this_1143.field_type_913
    @property
    def nullable(this_1146) -> 'bool33':
        return this_1146.nullable_914
class TableDef:
    table_name_919: 'SafeIdentifier'
    fields_920: 'Sequence29[FieldDef]'
    __slots__ = ('table_name_919', 'fields_920')
    def field(this_179, name_922: 'str27') -> 'FieldDef':
        return_346: 'FieldDef'
        with Label35() as fn_923:
            this_4373: 'Sequence29[FieldDef]' = this_179.fields_920
            n_4374: 'int31' = len_7235(this_4373)
            i_4375: 'int31' = 0
            while i_4375 < n_4374:
                el_4376: 'FieldDef' = list_get_7243(this_4373, i_4375)
                i_4375 = int_add_7244(i_4375, 1)
                f_924: 'FieldDef' = el_4376
                if f_924.name.sql_value == name_922:
                    return_346 = f_924
                    fn_923.break_()
            raise RuntimeError30()
        return return_346
    def __init__(this_343, table_name_926: 'SafeIdentifier', fields_927: 'Sequence29[FieldDef]') -> None:
        this_343.table_name_919 = table_name_926
        this_343.fields_920 = fields_927
    @property
    def table_name(this_1149) -> 'SafeIdentifier':
        return this_1149.table_name_919
    @property
    def fields(this_1152) -> 'Sequence29[FieldDef]':
        return this_1152.fields_920
T_198 = TypeVar42('T_198', bound = Any41)
class SqlBuilder:
    buffer_947: 'MutableSequence36[SqlPart]'
    __slots__ = ('buffer_947',)
    def append_safe(this_180, sql_source_949: 'str27') -> 'None':
        t_7190: 'SqlSource' = SqlSource(sql_source_949)
        this_180.buffer_947.append(t_7190)
    def append_fragment(this_181, fragment_952: 'SqlFragment') -> 'None':
        t_7188: 'Sequence29[SqlPart]' = fragment_952.parts
        list_builder_add_all_7247(this_181.buffer_947, t_7188)
    def append_part(this_182, part_955: 'SqlPart') -> 'None':
        this_182.buffer_947.append(part_955)
    def append_part_list(this_183, values_958: 'Sequence29[SqlPart]') -> 'None':
        def fn_7184(x_960: 'SqlPart') -> 'None':
            this_183.append_part(x_960)
        this_183.append_list_1003(values_958, fn_7184)
    def append_boolean(this_184, value_962: 'bool33') -> 'None':
        t_7181: 'SqlBoolean' = SqlBoolean(value_962)
        this_184.buffer_947.append(t_7181)
    def append_boolean_list(this_185, values_965: 'Sequence29[bool33]') -> 'None':
        def fn_7178(x_967: 'bool33') -> 'None':
            this_185.append_boolean(x_967)
        this_185.append_list_1003(values_965, fn_7178)
    def append_date(this_186, value_969: 'date26') -> 'None':
        t_7175: 'SqlDate' = SqlDate(value_969)
        this_186.buffer_947.append(t_7175)
    def append_date_list(this_187, values_972: 'Sequence29[date26]') -> 'None':
        def fn_7172(x_974: 'date26') -> 'None':
            this_187.append_date(x_974)
        this_187.append_list_1003(values_972, fn_7172)
    def append_float64(this_188, value_976: 'float38') -> 'None':
        t_7169: 'SqlFloat64' = SqlFloat64(value_976)
        this_188.buffer_947.append(t_7169)
    def append_float64_list(this_189, values_979: 'Sequence29[float38]') -> 'None':
        def fn_7166(x_981: 'float38') -> 'None':
            this_189.append_float64(x_981)
        this_189.append_list_1003(values_979, fn_7166)
    def append_int32(this_190, value_983: 'int31') -> 'None':
        t_7163: 'SqlInt32' = SqlInt32(value_983)
        this_190.buffer_947.append(t_7163)
    def append_int32_list(this_191, values_986: 'Sequence29[int31]') -> 'None':
        def fn_7160(x_988: 'int31') -> 'None':
            this_191.append_int32(x_988)
        this_191.append_list_1003(values_986, fn_7160)
    def append_int64(this_192, value_990: 'int64_23') -> 'None':
        t_7157: 'SqlInt64' = SqlInt64(value_990)
        this_192.buffer_947.append(t_7157)
    def append_int64_list(this_193, values_993: 'Sequence29[int64_23]') -> 'None':
        def fn_7154(x_995: 'int64_23') -> 'None':
            this_193.append_int64(x_995)
        this_193.append_list_1003(values_993, fn_7154)
    def append_string(this_194, value_997: 'str27') -> 'None':
        t_7151: 'SqlString' = SqlString(value_997)
        this_194.buffer_947.append(t_7151)
    def append_string_list(this_195, values_1000: 'Sequence29[str27]') -> 'None':
        def fn_7148(x_1002: 'str27') -> 'None':
            this_195.append_string(x_1002)
        this_195.append_list_1003(values_1000, fn_7148)
    def append_list_1003(this_196, values_1004: 'Sequence29[T_198]', append_value_1005: 'Callable43[[T_198], None]') -> 'None':
        t_7143: 'int31'
        t_7145: 'T_198'
        i_1007: 'int31' = 0
        while True:
            t_7143 = len_7235(values_1004)
            if not i_1007 < t_7143:
                break
            if i_1007 > 0:
                this_196.append_safe(', ')
            t_7145 = list_get_7243(values_1004, i_1007)
            append_value_1005(t_7145)
            i_1007 = int_add_7244(i_1007, 1)
    @property
    def accumulated(this_197) -> 'SqlFragment':
        return SqlFragment(tuple_7234(this_197.buffer_947))
    def __init__(this_348) -> None:
        t_7140: 'MutableSequence36[SqlPart]' = list_7231()
        this_348.buffer_947 = t_7140
class SqlFragment:
    parts_1014: 'Sequence29[SqlPart]'
    __slots__ = ('parts_1014',)
    def to_source(this_202) -> 'SqlSource':
        return SqlSource(this_202.to_string())
    def to_string(this_203) -> 'str27':
        t_7214: 'int31'
        builder_1019: 'list3[str27]' = ['']
        i_1020: 'int31' = 0
        while True:
            t_7214 = len_7235(this_203.parts_1014)
            if not i_1020 < t_7214:
                break
            list_get_7243(this_203.parts_1014, i_1020).format_to(builder_1019)
            i_1020 = int_add_7244(i_1020, 1)
        return ''.join(builder_1019)
    def __init__(this_369, parts_1022: 'Sequence29[SqlPart]') -> None:
        this_369.parts_1014 = parts_1022
    @property
    def parts(this_1158) -> 'Sequence29[SqlPart]':
        return this_1158.parts_1014
class SqlPart(metaclass = ABCMeta28):
    def format_to(this_204, builder_1024: 'list3[str27]') -> 'None':
        raise RuntimeError30()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_1026: 'str27'
    __slots__ = ('source_1026',)
    def format_to(this_205, builder_1028: 'list3[str27]') -> 'None':
        builder_1028.append(this_205.source_1026)
    def __init__(this_375, source_1031: 'str27') -> None:
        this_375.source_1026 = source_1031
    @property
    def source(this_1155) -> 'str27':
        return this_1155.source_1026
class SqlBoolean(SqlPart):
    value_1032: 'bool33'
    __slots__ = ('value_1032',)
    def format_to(this_206, builder_1034: 'list3[str27]') -> 'None':
        t_4218: 'str27'
        if this_206.value_1032:
            t_4218 = 'TRUE'
        else:
            t_4218 = 'FALSE'
        builder_1034.append(t_4218)
    def __init__(this_378, value_1037: 'bool33') -> None:
        this_378.value_1032 = value_1037
    @property
    def value(this_1161) -> 'bool33':
        return this_1161.value_1032
class SqlDate(SqlPart):
    value_1038: 'date26'
    __slots__ = ('value_1038',)
    def format_to(this_207, builder_1040: 'list3[str27]') -> 'None':
        builder_1040.append("'")
        t_7195: 'str27' = date_to_string_7251(this_207.value_1038)
        def fn_7193(c_1042: 'int31') -> 'None':
            if c_1042 == 39:
                builder_1040.append("''")
            else:
                builder_1040.append(string_from_code_point44(c_1042))
        string_for_each_7253(t_7195, fn_7193)
        builder_1040.append("'")
    def __init__(this_381, value_1044: 'date26') -> None:
        this_381.value_1038 = value_1044
    @property
    def value(this_1176) -> 'date26':
        return this_1176.value_1038
class SqlFloat64(SqlPart):
    value_1045: 'float38'
    __slots__ = ('value_1045',)
    def format_to(this_208, builder_1047: 'list3[str27]') -> 'None':
        t_4207: 'bool33'
        t_4208: 'bool33'
        s_1049: 'str27' = float64_to_string_7254(this_208.value_1045)
        if s_1049 == 'NaN':
            t_4208 = True
        else:
            if s_1049 == 'Infinity':
                t_4207 = True
            else:
                t_4207 = s_1049 == '-Infinity'
            t_4208 = t_4207
        if t_4208:
            builder_1047.append('NULL')
        else:
            builder_1047.append(s_1049)
    def __init__(this_384, value_1051: 'float38') -> None:
        this_384.value_1045 = value_1051
    @property
    def value(this_1173) -> 'float38':
        return this_1173.value_1045
class SqlInt32(SqlPart):
    value_1052: 'int31'
    __slots__ = ('value_1052',)
    def format_to(this_209, builder_1054: 'list3[str27]') -> 'None':
        t_7204: 'str27' = int_to_string_7238(this_209.value_1052)
        builder_1054.append(t_7204)
    def __init__(this_387, value_1057: 'int31') -> None:
        this_387.value_1052 = value_1057
    @property
    def value(this_1167) -> 'int31':
        return this_1167.value_1052
class SqlInt64(SqlPart):
    value_1058: 'int64_23'
    __slots__ = ('value_1058',)
    def format_to(this_210, builder_1060: 'list3[str27]') -> 'None':
        t_7202: 'str27' = int_to_string_7238(this_210.value_1058)
        builder_1060.append(t_7202)
    def __init__(this_390, value_1063: 'int64_23') -> None:
        this_390.value_1058 = value_1063
    @property
    def value(this_1170) -> 'int64_23':
        return this_1170.value_1058
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_1064: 'str27'
    __slots__ = ('value_1064',)
    def format_to(this_211, builder_1066: 'list3[str27]') -> 'None':
        builder_1066.append("'")
        def fn_7207(c_1068: 'int31') -> 'None':
            if c_1068 == 39:
                builder_1066.append("''")
            else:
                builder_1066.append(string_from_code_point44(c_1068))
        string_for_each_7253(this_211.value_1064, fn_7207)
        builder_1066.append("'")
    def __init__(this_393, value_1070: 'str27') -> None:
        this_393.value_1064 = value_1070
    @property
    def value(this_1164) -> 'str27':
        return this_1164.value_1064
def changeset(table_def_540: 'TableDef', params_541: 'MappingProxyType32[str27, str27]') -> 'Changeset':
    t_6990: 'MappingProxyType32[str27, str27]' = map_constructor_7255(())
    return ChangesetImpl_129(table_def_540, params_541, t_6990, (), True)
def is_ident_start_401(c_899: 'int31') -> 'bool33':
    return_326: 'bool33'
    t_3981: 'bool33'
    t_3982: 'bool33'
    if c_899 >= 97:
        t_3981 = c_899 <= 122
    else:
        t_3981 = False
    if t_3981:
        return_326 = True
    else:
        if c_899 >= 65:
            t_3982 = c_899 <= 90
        else:
            t_3982 = False
        if t_3982:
            return_326 = True
        else:
            return_326 = c_899 == 95
    return return_326
def is_ident_part_402(c_901: 'int31') -> 'bool33':
    return_327: 'bool33'
    if is_ident_start_401(c_901):
        return_327 = True
    elif c_901 >= 48:
        return_327 = c_901 <= 57
    else:
        return_327 = False
    return return_327
def safe_identifier(name_903: 'str27') -> 'SafeIdentifier':
    t_6988: 'int31'
    if not name_903:
        raise RuntimeError30()
    idx_905: 'int31' = 0
    if not is_ident_start_401(string_get_7256(name_903, idx_905)):
        raise RuntimeError30()
    t_6985: 'int31' = string_next_7257(name_903, idx_905)
    idx_905 = t_6985
    while True:
        if not len6(name_903) > idx_905:
            break
        if not is_ident_part_402(string_get_7256(name_903, idx_905)):
            raise RuntimeError30()
        t_6988 = string_next_7257(name_903, idx_905)
        idx_905 = t_6988
    return ValidatedIdentifier_177(name_903)
def delete_sql(table_def_630: 'TableDef', id_631: 'int31') -> 'SqlFragment':
    b_633: 'SqlBuilder' = SqlBuilder()
    b_633.append_safe('DELETE FROM ')
    b_633.append_safe(table_def_630.table_name.sql_value)
    b_633.append_safe(' WHERE id = ')
    b_633.append_int32(id_631)
    return b_633.accumulated
def from_(table_name_785: 'SafeIdentifier') -> 'Query':
    return Query(table_name_785, (), (), (), None, None, ())
def col(table_787: 'SafeIdentifier', column_788: 'SafeIdentifier') -> 'SqlFragment':
    b_790: 'SqlBuilder' = SqlBuilder()
    b_790.append_safe(table_787.sql_value)
    b_790.append_safe('.')
    b_790.append_safe(column_788.sql_value)
    return b_790.accumulated
