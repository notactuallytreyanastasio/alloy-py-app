from builtins import str as str27, RuntimeError as RuntimeError30, int as int31, bool as bool33, Exception as Exception37, float as float38, isinstance as isinstance39, list as list3, len as len6, tuple as tuple5
from abc import ABCMeta as ABCMeta28
from typing import Sequence as Sequence29, Dict as Dict34, MutableSequence as MutableSequence36, Union as Union40, Any as Any41, TypeVar as TypeVar42, Callable as Callable43
from types import MappingProxyType as MappingProxyType32
from temper_core import Label as Label35, Pair as Pair25, string_from_code_point as string_from_code_point44, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, date_from_iso_string as date_from_iso_string13, list_get as list_get14, int_add as int_add15, mapped_to_list as mapped_to_list16, list_join as list_join17, list_builder_add_all as list_builder_add_all18, date_to_string as date_to_string19, string_for_each as string_for_each20, float64_to_string as float64_to_string21, map_constructor as map_constructor22, string_get as string_get23, string_next as string_next24
from datetime import date as date26
map_builder_set_5796 = map_builder_set0
list_for_each_5797 = list_for_each1
mapped_to_map_5798 = mapped_to_map2
list_5799 = list3
mapped_has_5800 = mapped_has4
tuple_5802 = tuple5
len_5803 = len6
string_count_between_5804 = string_count_between7
str_cat_5805 = str_cat8
int_to_string_5806 = int_to_string9
string_to_int32_5807 = string_to_int3210
string_to_int64_5808 = string_to_int6411
string_to_float64_5809 = string_to_float6412
date_from_iso_string_5810 = date_from_iso_string13
list_get_5811 = list_get14
int_add_5812 = int_add15
mapped_to_list_5813 = mapped_to_list16
list_join_5814 = list_join17
list_builder_add_all_5815 = list_builder_add_all18
date_to_string_5819 = date_to_string19
string_for_each_5821 = string_for_each20
float64_to_string_5822 = float64_to_string21
map_constructor_5823 = map_constructor22
string_get_5824 = string_get23
string_next_5825 = string_next24
pair_5827 = Pair25
date_5830 = date26
class ChangesetError:
    field_349: 'str27'
    message_350: 'str27'
    __slots__ = ('field_349', 'message_350')
    def __init__(this_177, field_352: 'str27', message_353: 'str27') -> None:
        this_177.field_349 = field_352
        this_177.message_350 = message_353
    @property
    def field(this_976) -> 'str27':
        return this_976.field_349
    @property
    def message(this_979) -> 'str27':
        return this_979.message_350
class Changeset(metaclass = ABCMeta28):
    def cast(this_99, allowed_fields_363: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_required(this_100, fields_366: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_length(this_101, field_369: 'SafeIdentifier', min_370: 'int31', max_371: 'int31') -> 'Changeset':
        raise RuntimeError30()
    def validate_int(this_102, field_374: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_int64(this_103, field_377: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_float(this_104, field_380: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_bool(this_105, field_383: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def to_insert_sql(this_106) -> 'SqlFragment':
        raise RuntimeError30()
    def to_update_sql(this_107, id_388: 'int31') -> 'SqlFragment':
        raise RuntimeError30()
class ChangesetImpl_108(Changeset):
    table_def_390: 'TableDef'
    params_391: 'MappingProxyType32[str27, str27]'
    changes_392: 'MappingProxyType32[str27, str27]'
    errors_393: 'Sequence29[ChangesetError]'
    is_valid_394: 'bool33'
    __slots__ = ('table_def_390', 'params_391', 'changes_392', 'errors_393', 'is_valid_394')
    @property
    def table_def(this_109) -> 'TableDef':
        return this_109.table_def_390
    @property
    def changes(this_110) -> 'MappingProxyType32[str27, str27]':
        return this_110.changes_392
    @property
    def errors(this_111) -> 'Sequence29[ChangesetError]':
        return this_111.errors_393
    @property
    def is_valid(this_112) -> 'bool33':
        return this_112.is_valid_394
    def cast(this_113, allowed_fields_404: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        mb_406: 'Dict34[str27, str27]' = {}
        def fn_5700(f_407: 'SafeIdentifier') -> 'None':
            t_5698: 'str27'
            t_5695: 'str27' = f_407.sql_value
            val_408: 'str27' = this_113.params_391.get(t_5695, '')
            if not (not val_408):
                t_5698 = f_407.sql_value
                map_builder_set_5796(mb_406, t_5698, val_408)
        list_for_each_5797(allowed_fields_404, fn_5700)
        return ChangesetImpl_108(this_113.table_def_390, this_113.params_391, mapped_to_map_5798(mb_406), this_113.errors_393, this_113.is_valid_394)
    def validate_required(this_114, fields_410: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        return_210: 'Changeset'
        t_5693: 'Sequence29[ChangesetError]'
        t_3382: 'TableDef'
        t_3383: 'MappingProxyType32[str27, str27]'
        t_3384: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_411:
            if not this_114.is_valid_394:
                return_210 = this_114
                fn_411.break_()
            eb_412: 'MutableSequence36[ChangesetError]' = list_5799(this_114.errors_393)
            valid_413: 'bool33' = True
            def fn_5689(f_414: 'SafeIdentifier') -> 'None':
                nonlocal valid_413
                t_5687: 'ChangesetError'
                t_5684: 'str27' = f_414.sql_value
                if not mapped_has_5800(this_114.changes_392, t_5684):
                    t_5687 = ChangesetError(f_414.sql_value, 'is required')
                    eb_412.append(t_5687)
                    valid_413 = False
            list_for_each_5797(fields_410, fn_5689)
            t_3382 = this_114.table_def_390
            t_3383 = this_114.params_391
            t_3384 = this_114.changes_392
            t_5693 = tuple_5802(eb_412)
            return_210 = ChangesetImpl_108(t_3382, t_3383, t_3384, t_5693, valid_413)
        return return_210
    def validate_length(this_115, field_416: 'SafeIdentifier', min_417: 'int31', max_418: 'int31') -> 'Changeset':
        return_211: 'Changeset'
        t_5671: 'str27'
        t_5682: 'Sequence29[ChangesetError]'
        t_3365: 'bool33'
        t_3371: 'TableDef'
        t_3372: 'MappingProxyType32[str27, str27]'
        t_3373: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_419:
            if not this_115.is_valid_394:
                return_211 = this_115
                fn_419.break_()
            t_5671 = field_416.sql_value
            val_420: 'str27' = this_115.changes_392.get(t_5671, '')
            len_421: 'int31' = string_count_between_5804(val_420, 0, len_5803(val_420))
            if len_421 < min_417:
                t_3365 = True
            else:
                t_3365 = len_421 > max_418
            if t_3365:
                msg_422: 'str27' = str_cat_5805('must be between ', int_to_string_5806(min_417), ' and ', int_to_string_5806(max_418), ' characters')
                eb_423: 'MutableSequence36[ChangesetError]' = list_5799(this_115.errors_393)
                eb_423.append(ChangesetError(field_416.sql_value, msg_422))
                t_3371 = this_115.table_def_390
                t_3372 = this_115.params_391
                t_3373 = this_115.changes_392
                t_5682 = tuple_5802(eb_423)
                return_211 = ChangesetImpl_108(t_3371, t_3372, t_3373, t_5682, False)
                fn_419.break_()
            return_211 = this_115
        return return_211
    def validate_int(this_116, field_425: 'SafeIdentifier') -> 'Changeset':
        return_212: 'Changeset'
        t_5662: 'str27'
        t_5669: 'Sequence29[ChangesetError]'
        t_3356: 'TableDef'
        t_3357: 'MappingProxyType32[str27, str27]'
        t_3358: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_426:
            if not this_116.is_valid_394:
                return_212 = this_116
                fn_426.break_()
            t_5662 = field_425.sql_value
            val_427: 'str27' = this_116.changes_392.get(t_5662, '')
            if not val_427:
                return_212 = this_116
                fn_426.break_()
            parse_ok_428: 'bool33'
            try:
                string_to_int32_5807(val_427)
                parse_ok_428 = True
            except Exception37:
                parse_ok_428 = False
            if not parse_ok_428:
                eb_429: 'MutableSequence36[ChangesetError]' = list_5799(this_116.errors_393)
                eb_429.append(ChangesetError(field_425.sql_value, 'must be an integer'))
                t_3356 = this_116.table_def_390
                t_3357 = this_116.params_391
                t_3358 = this_116.changes_392
                t_5669 = tuple_5802(eb_429)
                return_212 = ChangesetImpl_108(t_3356, t_3357, t_3358, t_5669, False)
                fn_426.break_()
            return_212 = this_116
        return return_212
    def validate_int64(this_117, field_431: 'SafeIdentifier') -> 'Changeset':
        return_213: 'Changeset'
        t_5653: 'str27'
        t_5660: 'Sequence29[ChangesetError]'
        t_3343: 'TableDef'
        t_3344: 'MappingProxyType32[str27, str27]'
        t_3345: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_432:
            if not this_117.is_valid_394:
                return_213 = this_117
                fn_432.break_()
            t_5653 = field_431.sql_value
            val_433: 'str27' = this_117.changes_392.get(t_5653, '')
            if not val_433:
                return_213 = this_117
                fn_432.break_()
            parse_ok_434: 'bool33'
            try:
                string_to_int64_5808(val_433)
                parse_ok_434 = True
            except Exception37:
                parse_ok_434 = False
            if not parse_ok_434:
                eb_435: 'MutableSequence36[ChangesetError]' = list_5799(this_117.errors_393)
                eb_435.append(ChangesetError(field_431.sql_value, 'must be a 64-bit integer'))
                t_3343 = this_117.table_def_390
                t_3344 = this_117.params_391
                t_3345 = this_117.changes_392
                t_5660 = tuple_5802(eb_435)
                return_213 = ChangesetImpl_108(t_3343, t_3344, t_3345, t_5660, False)
                fn_432.break_()
            return_213 = this_117
        return return_213
    def validate_float(this_118, field_437: 'SafeIdentifier') -> 'Changeset':
        return_214: 'Changeset'
        t_5644: 'str27'
        t_5651: 'Sequence29[ChangesetError]'
        t_3330: 'TableDef'
        t_3331: 'MappingProxyType32[str27, str27]'
        t_3332: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_438:
            if not this_118.is_valid_394:
                return_214 = this_118
                fn_438.break_()
            t_5644 = field_437.sql_value
            val_439: 'str27' = this_118.changes_392.get(t_5644, '')
            if not val_439:
                return_214 = this_118
                fn_438.break_()
            parse_ok_440: 'bool33'
            try:
                string_to_float64_5809(val_439)
                parse_ok_440 = True
            except Exception37:
                parse_ok_440 = False
            if not parse_ok_440:
                eb_441: 'MutableSequence36[ChangesetError]' = list_5799(this_118.errors_393)
                eb_441.append(ChangesetError(field_437.sql_value, 'must be a number'))
                t_3330 = this_118.table_def_390
                t_3331 = this_118.params_391
                t_3332 = this_118.changes_392
                t_5651 = tuple_5802(eb_441)
                return_214 = ChangesetImpl_108(t_3330, t_3331, t_3332, t_5651, False)
                fn_438.break_()
            return_214 = this_118
        return return_214
    def validate_bool(this_119, field_443: 'SafeIdentifier') -> 'Changeset':
        return_215: 'Changeset'
        t_5635: 'str27'
        t_5642: 'Sequence29[ChangesetError]'
        t_3305: 'bool33'
        t_3306: 'bool33'
        t_3308: 'bool33'
        t_3309: 'bool33'
        t_3311: 'bool33'
        t_3317: 'TableDef'
        t_3318: 'MappingProxyType32[str27, str27]'
        t_3319: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_444:
            if not this_119.is_valid_394:
                return_215 = this_119
                fn_444.break_()
            t_5635 = field_443.sql_value
            val_445: 'str27' = this_119.changes_392.get(t_5635, '')
            if not val_445:
                return_215 = this_119
                fn_444.break_()
            is_true_446: 'bool33'
            if val_445 == 'true':
                is_true_446 = True
            else:
                if val_445 == '1':
                    t_3306 = True
                else:
                    if val_445 == 'yes':
                        t_3305 = True
                    else:
                        t_3305 = val_445 == 'on'
                    t_3306 = t_3305
                is_true_446 = t_3306
            is_false_447: 'bool33'
            if val_445 == 'false':
                is_false_447 = True
            else:
                if val_445 == '0':
                    t_3309 = True
                else:
                    if val_445 == 'no':
                        t_3308 = True
                    else:
                        t_3308 = val_445 == 'off'
                    t_3309 = t_3308
                is_false_447 = t_3309
            if not is_true_446:
                t_3311 = not is_false_447
            else:
                t_3311 = False
            if t_3311:
                eb_448: 'MutableSequence36[ChangesetError]' = list_5799(this_119.errors_393)
                eb_448.append(ChangesetError(field_443.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_3317 = this_119.table_def_390
                t_3318 = this_119.params_391
                t_3319 = this_119.changes_392
                t_5642 = tuple_5802(eb_448)
                return_215 = ChangesetImpl_108(t_3317, t_3318, t_3319, t_5642, False)
                fn_444.break_()
            return_215 = this_119
        return return_215
    def parse_bool_sql_part_449(this_120, val_450: 'str27') -> 'SqlBoolean':
        return_216: 'SqlBoolean'
        t_3294: 'bool33'
        t_3295: 'bool33'
        t_3296: 'bool33'
        t_3298: 'bool33'
        t_3299: 'bool33'
        t_3300: 'bool33'
        with Label35() as fn_451:
            if val_450 == 'true':
                t_3296 = True
            else:
                if val_450 == '1':
                    t_3295 = True
                else:
                    if val_450 == 'yes':
                        t_3294 = True
                    else:
                        t_3294 = val_450 == 'on'
                    t_3295 = t_3294
                t_3296 = t_3295
            if t_3296:
                return_216 = SqlBoolean(True)
                fn_451.break_()
            if val_450 == 'false':
                t_3300 = True
            else:
                if val_450 == '0':
                    t_3299 = True
                else:
                    if val_450 == 'no':
                        t_3298 = True
                    else:
                        t_3298 = val_450 == 'off'
                    t_3299 = t_3298
                t_3300 = t_3299
            if t_3300:
                return_216 = SqlBoolean(False)
                fn_451.break_()
            raise RuntimeError30()
        return return_216
    def value_to_sql_part_452(this_121, field_def_453: 'FieldDef', val_454: 'str27') -> 'SqlPart':
        return_217: 'SqlPart'
        t_3281: 'int31'
        t_3284: 'int64_23'
        t_3287: 'float38'
        t_3292: 'date26'
        with Label35() as fn_455:
            ft_456: 'FieldType' = field_def_453.field_type
            if isinstance39(ft_456, StringField):
                return_217 = SqlString(val_454)
                fn_455.break_()
            if isinstance39(ft_456, IntField):
                t_3281 = string_to_int32_5807(val_454)
                return_217 = SqlInt32(t_3281)
                fn_455.break_()
            if isinstance39(ft_456, Int64Field):
                t_3284 = string_to_int64_5808(val_454)
                return_217 = SqlInt64(t_3284)
                fn_455.break_()
            if isinstance39(ft_456, FloatField):
                t_3287 = string_to_float64_5809(val_454)
                return_217 = SqlFloat64(t_3287)
                fn_455.break_()
            if isinstance39(ft_456, BoolField):
                return_217 = this_121.parse_bool_sql_part_449(val_454)
                fn_455.break_()
            if isinstance39(ft_456, DateField):
                t_3292 = date_from_iso_string_5810(val_454)
                return_217 = SqlDate(t_3292)
                fn_455.break_()
            raise RuntimeError30()
        return return_217
    def to_insert_sql(this_122) -> 'SqlFragment':
        t_5583: 'int31'
        t_5588: 'str27'
        t_5589: 'bool33'
        t_5594: 'int31'
        t_5596: 'str27'
        t_5600: 'str27'
        t_5615: 'int31'
        t_3245: 'bool33'
        t_3253: 'FieldDef'
        t_3258: 'SqlPart'
        if not this_122.is_valid_394:
            raise RuntimeError30()
        i_459: 'int31' = 0
        while True:
            t_5583 = len_5803(this_122.table_def_390.fields)
            if not i_459 < t_5583:
                break
            f_460: 'FieldDef' = list_get_5811(this_122.table_def_390.fields, i_459)
            if not f_460.nullable:
                t_5588 = f_460.name.sql_value
                t_5589 = mapped_has_5800(this_122.changes_392, t_5588)
                t_3245 = not t_5589
            else:
                t_3245 = False
            if t_3245:
                raise RuntimeError30()
            i_459 = int_add_5812(i_459, 1)
        pairs_461: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_5813(this_122.changes_392)
        if len_5803(pairs_461) == 0:
            raise RuntimeError30()
        col_names_462: 'MutableSequence36[str27]' = list_5799()
        val_parts_463: 'MutableSequence36[SqlPart]' = list_5799()
        i_464: 'int31' = 0
        while True:
            t_5594 = len_5803(pairs_461)
            if not i_464 < t_5594:
                break
            pair_465: 'Pair25[str27, str27]' = list_get_5811(pairs_461, i_464)
            t_5596 = pair_465.key
            t_3253 = this_122.table_def_390.field(t_5596)
            fd_466: 'FieldDef' = t_3253
            col_names_462.append(fd_466.name.sql_value)
            t_5600 = pair_465.value
            t_3258 = this_122.value_to_sql_part_452(fd_466, t_5600)
            val_parts_463.append(t_3258)
            i_464 = int_add_5812(i_464, 1)
        b_467: 'SqlBuilder' = SqlBuilder()
        b_467.append_safe('INSERT INTO ')
        b_467.append_safe(this_122.table_def_390.table_name.sql_value)
        b_467.append_safe(' (')
        t_5608: 'Sequence29[str27]' = tuple_5802(col_names_462)
        def fn_5581(c_468: 'str27') -> 'str27':
            return c_468
        b_467.append_safe(list_join_5814(t_5608, ', ', fn_5581))
        b_467.append_safe(') VALUES (')
        b_467.append_part(list_get_5811(val_parts_463, 0))
        j_469: 'int31' = 1
        while True:
            t_5615 = len_5803(val_parts_463)
            if not j_469 < t_5615:
                break
            b_467.append_safe(', ')
            b_467.append_part(list_get_5811(val_parts_463, j_469))
            j_469 = int_add_5812(j_469, 1)
        b_467.append_safe(')')
        return b_467.accumulated
    def to_update_sql(this_123, id_471: 'int31') -> 'SqlFragment':
        t_5568: 'int31'
        t_5571: 'str27'
        t_5576: 'str27'
        t_3226: 'FieldDef'
        t_3232: 'SqlPart'
        if not this_123.is_valid_394:
            raise RuntimeError30()
        pairs_473: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_5813(this_123.changes_392)
        if len_5803(pairs_473) == 0:
            raise RuntimeError30()
        b_474: 'SqlBuilder' = SqlBuilder()
        b_474.append_safe('UPDATE ')
        b_474.append_safe(this_123.table_def_390.table_name.sql_value)
        b_474.append_safe(' SET ')
        i_475: 'int31' = 0
        while True:
            t_5568 = len_5803(pairs_473)
            if not i_475 < t_5568:
                break
            if i_475 > 0:
                b_474.append_safe(', ')
            pair_476: 'Pair25[str27, str27]' = list_get_5811(pairs_473, i_475)
            t_5571 = pair_476.key
            t_3226 = this_123.table_def_390.field(t_5571)
            fd_477: 'FieldDef' = t_3226
            b_474.append_safe(fd_477.name.sql_value)
            b_474.append_safe(' = ')
            t_5576 = pair_476.value
            t_3232 = this_123.value_to_sql_part_452(fd_477, t_5576)
            b_474.append_part(t_3232)
            i_475 = int_add_5812(i_475, 1)
        b_474.append_safe(' WHERE id = ')
        b_474.append_int32(id_471)
        return b_474.accumulated
    def __init__(this_200, table_def_479: 'TableDef', params_480: 'MappingProxyType32[str27, str27]', changes_481: 'MappingProxyType32[str27, str27]', errors_482: 'Sequence29[ChangesetError]', is_valid_483: 'bool33') -> None:
        this_200.table_def_390 = table_def_479
        this_200.params_391 = params_480
        this_200.changes_392 = changes_481
        this_200.errors_393 = errors_482
        this_200.is_valid_394 = is_valid_483
class JoinType(metaclass = ABCMeta28):
    def keyword(this_124) -> 'str27':
        raise RuntimeError30()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_125) -> 'str27':
        return 'INNER JOIN'
    def __init__(this_225) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_126) -> 'str27':
        return 'LEFT JOIN'
    def __init__(this_228) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_127) -> 'str27':
        return 'RIGHT JOIN'
    def __init__(this_231) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_128) -> 'str27':
        return 'FULL OUTER JOIN'
    def __init__(this_234) -> None:
        pass
class JoinClause:
    join_type_592: 'JoinType'
    table_593: 'SafeIdentifier'
    on_condition_594: 'SqlFragment'
    __slots__ = ('join_type_592', 'table_593', 'on_condition_594')
    def __init__(this_237, join_type_596: 'JoinType', table_597: 'SafeIdentifier', on_condition_598: 'SqlFragment') -> None:
        this_237.join_type_592 = join_type_596
        this_237.table_593 = table_597
        this_237.on_condition_594 = on_condition_598
    @property
    def join_type(this_1044) -> 'JoinType':
        return this_1044.join_type_592
    @property
    def table(this_1047) -> 'SafeIdentifier':
        return this_1047.table_593
    @property
    def on_condition(this_1050) -> 'SqlFragment':
        return this_1050.on_condition_594
class OrderClause:
    field_599: 'SafeIdentifier'
    ascending_600: 'bool33'
    __slots__ = ('field_599', 'ascending_600')
    def __init__(this_239, field_602: 'SafeIdentifier', ascending_603: 'bool33') -> None:
        this_239.field_599 = field_602
        this_239.ascending_600 = ascending_603
    @property
    def field(this_1053) -> 'SafeIdentifier':
        return this_1053.field_599
    @property
    def ascending(this_1056) -> 'bool33':
        return this_1056.ascending_600
class Query:
    table_name_604: 'SafeIdentifier'
    conditions_605: 'Sequence29[SqlFragment]'
    selected_fields_606: 'Sequence29[SafeIdentifier]'
    order_clauses_607: 'Sequence29[OrderClause]'
    limit_val_608: 'Union40[int31, None]'
    offset_val_609: 'Union40[int31, None]'
    join_clauses_610: 'Sequence29[JoinClause]'
    __slots__ = ('table_name_604', 'conditions_605', 'selected_fields_606', 'order_clauses_607', 'limit_val_608', 'offset_val_609', 'join_clauses_610')
    def where(this_129, condition_612: 'SqlFragment') -> 'Query':
        nb_614: 'MutableSequence36[SqlFragment]' = list_5799(this_129.conditions_605)
        nb_614.append(condition_612)
        return Query(this_129.table_name_604, tuple_5802(nb_614), this_129.selected_fields_606, this_129.order_clauses_607, this_129.limit_val_608, this_129.offset_val_609, this_129.join_clauses_610)
    def select(this_130, fields_616: 'Sequence29[SafeIdentifier]') -> 'Query':
        return Query(this_130.table_name_604, this_130.conditions_605, fields_616, this_130.order_clauses_607, this_130.limit_val_608, this_130.offset_val_609, this_130.join_clauses_610)
    def order_by(this_131, field_619: 'SafeIdentifier', ascending_620: 'bool33') -> 'Query':
        nb_622: 'MutableSequence36[OrderClause]' = list_5799(this_131.order_clauses_607)
        nb_622.append(OrderClause(field_619, ascending_620))
        return Query(this_131.table_name_604, this_131.conditions_605, this_131.selected_fields_606, tuple_5802(nb_622), this_131.limit_val_608, this_131.offset_val_609, this_131.join_clauses_610)
    def limit(this_132, n_624: 'int31') -> 'Query':
        if n_624 < 0:
            raise RuntimeError30()
        return Query(this_132.table_name_604, this_132.conditions_605, this_132.selected_fields_606, this_132.order_clauses_607, n_624, this_132.offset_val_609, this_132.join_clauses_610)
    def offset(this_133, n_627: 'int31') -> 'Query':
        if n_627 < 0:
            raise RuntimeError30()
        return Query(this_133.table_name_604, this_133.conditions_605, this_133.selected_fields_606, this_133.order_clauses_607, this_133.limit_val_608, n_627, this_133.join_clauses_610)
    def join(this_134, join_type_630: 'JoinType', table_631: 'SafeIdentifier', on_condition_632: 'SqlFragment') -> 'Query':
        nb_634: 'MutableSequence36[JoinClause]' = list_5799(this_134.join_clauses_610)
        nb_634.append(JoinClause(join_type_630, table_631, on_condition_632))
        return Query(this_134.table_name_604, this_134.conditions_605, this_134.selected_fields_606, this_134.order_clauses_607, this_134.limit_val_608, this_134.offset_val_609, tuple_5802(nb_634))
    def inner_join(this_135, table_636: 'SafeIdentifier', on_condition_637: 'SqlFragment') -> 'Query':
        t_5152: 'InnerJoin' = InnerJoin()
        return this_135.join(t_5152, table_636, on_condition_637)
    def left_join(this_136, table_640: 'SafeIdentifier', on_condition_641: 'SqlFragment') -> 'Query':
        t_5150: 'LeftJoin' = LeftJoin()
        return this_136.join(t_5150, table_640, on_condition_641)
    def right_join(this_137, table_644: 'SafeIdentifier', on_condition_645: 'SqlFragment') -> 'Query':
        t_5148: 'RightJoin' = RightJoin()
        return this_137.join(t_5148, table_644, on_condition_645)
    def full_join(this_138, table_648: 'SafeIdentifier', on_condition_649: 'SqlFragment') -> 'Query':
        t_5146: 'FullJoin' = FullJoin()
        return this_138.join(t_5146, table_648, on_condition_649)
    def to_sql(this_139) -> 'SqlFragment':
        t_5133: 'int31'
        b_653: 'SqlBuilder' = SqlBuilder()
        b_653.append_safe('SELECT ')
        if not this_139.selected_fields_606:
            b_653.append_safe('*')
        else:
            def fn_5116(f_654: 'SafeIdentifier') -> 'str27':
                return f_654.sql_value
            b_653.append_safe(list_join_5814(this_139.selected_fields_606, ', ', fn_5116))
        b_653.append_safe(' FROM ')
        b_653.append_safe(this_139.table_name_604.sql_value)
        def fn_5115(jc_655: 'JoinClause') -> 'None':
            b_653.append_safe(' ')
            t_5104: 'str27' = jc_655.join_type.keyword()
            b_653.append_safe(t_5104)
            b_653.append_safe(' ')
            t_5108: 'str27' = jc_655.table.sql_value
            b_653.append_safe(t_5108)
            b_653.append_safe(' ON ')
            t_5111: 'SqlFragment' = jc_655.on_condition
            b_653.append_fragment(t_5111)
        list_for_each_5797(this_139.join_clauses_610, fn_5115)
        if not (not this_139.conditions_605):
            b_653.append_safe(' WHERE ')
            b_653.append_fragment(list_get_5811(this_139.conditions_605, 0))
            i_656: 'int31' = 1
            while True:
                t_5133 = len_5803(this_139.conditions_605)
                if not i_656 < t_5133:
                    break
                b_653.append_safe(' AND ')
                b_653.append_fragment(list_get_5811(this_139.conditions_605, i_656))
                i_656 = int_add_5812(i_656, 1)
        if not (not this_139.order_clauses_607):
            b_653.append_safe(' ORDER BY ')
            first_657: 'bool33' = True
            def fn_5114(oc_658: 'OrderClause') -> 'None':
                nonlocal first_657
                t_2812: 'str27'
                if not first_657:
                    b_653.append_safe(', ')
                first_657 = False
                t_5098: 'str27' = oc_658.field.sql_value
                b_653.append_safe(t_5098)
                if oc_658.ascending:
                    t_2812 = ' ASC'
                else:
                    t_2812 = ' DESC'
                b_653.append_safe(t_2812)
            list_for_each_5797(this_139.order_clauses_607, fn_5114)
        lv_659: 'Union40[int31, None]' = this_139.limit_val_608
        if not lv_659 is None:
            lv_1257: 'int31' = lv_659
            b_653.append_safe(' LIMIT ')
            b_653.append_int32(lv_1257)
        ov_660: 'Union40[int31, None]' = this_139.offset_val_609
        if not ov_660 is None:
            ov_1258: 'int31' = ov_660
            b_653.append_safe(' OFFSET ')
            b_653.append_int32(ov_1258)
        return b_653.accumulated
    def safe_to_sql(this_140, default_limit_662: 'int31') -> 'SqlFragment':
        return_260: 'SqlFragment'
        t_2805: 'Query'
        if default_limit_662 < 0:
            raise RuntimeError30()
        if not this_140.limit_val_608 is None:
            return_260 = this_140.to_sql()
        else:
            t_2805 = this_140.limit(default_limit_662)
            return_260 = t_2805.to_sql()
        return return_260
    def __init__(this_241, table_name_665: 'SafeIdentifier', conditions_666: 'Sequence29[SqlFragment]', selected_fields_667: 'Sequence29[SafeIdentifier]', order_clauses_668: 'Sequence29[OrderClause]', limit_val_669: 'Union40[int31, None]', offset_val_670: 'Union40[int31, None]', join_clauses_671: 'Sequence29[JoinClause]') -> None:
        this_241.table_name_604 = table_name_665
        this_241.conditions_605 = conditions_666
        this_241.selected_fields_606 = selected_fields_667
        this_241.order_clauses_607 = order_clauses_668
        this_241.limit_val_608 = limit_val_669
        this_241.offset_val_609 = offset_val_670
        this_241.join_clauses_610 = join_clauses_671
    @property
    def table_name(this_1059) -> 'SafeIdentifier':
        return this_1059.table_name_604
    @property
    def conditions(this_1062) -> 'Sequence29[SqlFragment]':
        return this_1062.conditions_605
    @property
    def selected_fields(this_1065) -> 'Sequence29[SafeIdentifier]':
        return this_1065.selected_fields_606
    @property
    def order_clauses(this_1068) -> 'Sequence29[OrderClause]':
        return this_1068.order_clauses_607
    @property
    def limit_val(this_1071) -> 'Union40[int31, None]':
        return this_1071.limit_val_608
    @property
    def offset_val(this_1074) -> 'Union40[int31, None]':
        return this_1074.offset_val_609
    @property
    def join_clauses(this_1077) -> 'Sequence29[JoinClause]':
        return this_1077.join_clauses_610
class SafeIdentifier(metaclass = ABCMeta28):
    pass
class ValidatedIdentifier_142(SafeIdentifier):
    value_738: 'str27'
    __slots__ = ('value_738',)
    @property
    def sql_value(this_143) -> 'str27':
        return this_143.value_738
    def __init__(this_267, value_742: 'str27') -> None:
        this_267.value_738 = value_742
class FieldType(metaclass = ABCMeta28):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_273) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_275) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_277) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_279) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_281) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_283) -> None:
        pass
class FieldDef:
    name_756: 'SafeIdentifier'
    field_type_757: 'FieldType'
    nullable_758: 'bool33'
    __slots__ = ('name_756', 'field_type_757', 'nullable_758')
    def __init__(this_285, name_760: 'SafeIdentifier', field_type_761: 'FieldType', nullable_762: 'bool33') -> None:
        this_285.name_756 = name_760
        this_285.field_type_757 = field_type_761
        this_285.nullable_758 = nullable_762
    @property
    def name(this_982) -> 'SafeIdentifier':
        return this_982.name_756
    @property
    def field_type(this_985) -> 'FieldType':
        return this_985.field_type_757
    @property
    def nullable(this_988) -> 'bool33':
        return this_988.nullable_758
class TableDef:
    table_name_763: 'SafeIdentifier'
    fields_764: 'Sequence29[FieldDef]'
    __slots__ = ('table_name_763', 'fields_764')
    def field(this_144, name_766: 'str27') -> 'FieldDef':
        return_290: 'FieldDef'
        with Label35() as fn_767:
            this_3570: 'Sequence29[FieldDef]' = this_144.fields_764
            n_3571: 'int31' = len_5803(this_3570)
            i_3572: 'int31' = 0
            while i_3572 < n_3571:
                el_3573: 'FieldDef' = list_get_5811(this_3570, i_3572)
                i_3572 = int_add_5812(i_3572, 1)
                f_768: 'FieldDef' = el_3573
                if f_768.name.sql_value == name_766:
                    return_290 = f_768
                    fn_767.break_()
            raise RuntimeError30()
        return return_290
    def __init__(this_287, table_name_770: 'SafeIdentifier', fields_771: 'Sequence29[FieldDef]') -> None:
        this_287.table_name_763 = table_name_770
        this_287.fields_764 = fields_771
    @property
    def table_name(this_991) -> 'SafeIdentifier':
        return this_991.table_name_763
    @property
    def fields(this_994) -> 'Sequence29[FieldDef]':
        return this_994.fields_764
T_163 = TypeVar42('T_163', bound = Any41)
class SqlBuilder:
    buffer_791: 'MutableSequence36[SqlPart]'
    __slots__ = ('buffer_791',)
    def append_safe(this_145, sql_source_793: 'str27') -> 'None':
        t_5758: 'SqlSource' = SqlSource(sql_source_793)
        this_145.buffer_791.append(t_5758)
    def append_fragment(this_146, fragment_796: 'SqlFragment') -> 'None':
        t_5756: 'Sequence29[SqlPart]' = fragment_796.parts
        list_builder_add_all_5815(this_146.buffer_791, t_5756)
    def append_part(this_147, part_799: 'SqlPart') -> 'None':
        this_147.buffer_791.append(part_799)
    def append_part_list(this_148, values_802: 'Sequence29[SqlPart]') -> 'None':
        def fn_5752(x_804: 'SqlPart') -> 'None':
            this_148.append_part(x_804)
        this_148.append_list_847(values_802, fn_5752)
    def append_boolean(this_149, value_806: 'bool33') -> 'None':
        t_5749: 'SqlBoolean' = SqlBoolean(value_806)
        this_149.buffer_791.append(t_5749)
    def append_boolean_list(this_150, values_809: 'Sequence29[bool33]') -> 'None':
        def fn_5746(x_811: 'bool33') -> 'None':
            this_150.append_boolean(x_811)
        this_150.append_list_847(values_809, fn_5746)
    def append_date(this_151, value_813: 'date26') -> 'None':
        t_5743: 'SqlDate' = SqlDate(value_813)
        this_151.buffer_791.append(t_5743)
    def append_date_list(this_152, values_816: 'Sequence29[date26]') -> 'None':
        def fn_5740(x_818: 'date26') -> 'None':
            this_152.append_date(x_818)
        this_152.append_list_847(values_816, fn_5740)
    def append_float64(this_153, value_820: 'float38') -> 'None':
        t_5737: 'SqlFloat64' = SqlFloat64(value_820)
        this_153.buffer_791.append(t_5737)
    def append_float64_list(this_154, values_823: 'Sequence29[float38]') -> 'None':
        def fn_5734(x_825: 'float38') -> 'None':
            this_154.append_float64(x_825)
        this_154.append_list_847(values_823, fn_5734)
    def append_int32(this_155, value_827: 'int31') -> 'None':
        t_5731: 'SqlInt32' = SqlInt32(value_827)
        this_155.buffer_791.append(t_5731)
    def append_int32_list(this_156, values_830: 'Sequence29[int31]') -> 'None':
        def fn_5728(x_832: 'int31') -> 'None':
            this_156.append_int32(x_832)
        this_156.append_list_847(values_830, fn_5728)
    def append_int64(this_157, value_834: 'int64_23') -> 'None':
        t_5725: 'SqlInt64' = SqlInt64(value_834)
        this_157.buffer_791.append(t_5725)
    def append_int64_list(this_158, values_837: 'Sequence29[int64_23]') -> 'None':
        def fn_5722(x_839: 'int64_23') -> 'None':
            this_158.append_int64(x_839)
        this_158.append_list_847(values_837, fn_5722)
    def append_string(this_159, value_841: 'str27') -> 'None':
        t_5719: 'SqlString' = SqlString(value_841)
        this_159.buffer_791.append(t_5719)
    def append_string_list(this_160, values_844: 'Sequence29[str27]') -> 'None':
        def fn_5716(x_846: 'str27') -> 'None':
            this_160.append_string(x_846)
        this_160.append_list_847(values_844, fn_5716)
    def append_list_847(this_161, values_848: 'Sequence29[T_163]', append_value_849: 'Callable43[[T_163], None]') -> 'None':
        t_5711: 'int31'
        t_5713: 'T_163'
        i_851: 'int31' = 0
        while True:
            t_5711 = len_5803(values_848)
            if not i_851 < t_5711:
                break
            if i_851 > 0:
                this_161.append_safe(', ')
            t_5713 = list_get_5811(values_848, i_851)
            append_value_849(t_5713)
            i_851 = int_add_5812(i_851, 1)
    @property
    def accumulated(this_162) -> 'SqlFragment':
        return SqlFragment(tuple_5802(this_162.buffer_791))
    def __init__(this_292) -> None:
        t_5708: 'MutableSequence36[SqlPart]' = list_5799()
        this_292.buffer_791 = t_5708
class SqlFragment:
    parts_858: 'Sequence29[SqlPart]'
    __slots__ = ('parts_858',)
    def to_source(this_167) -> 'SqlSource':
        return SqlSource(this_167.to_string())
    def to_string(this_168) -> 'str27':
        t_5782: 'int31'
        builder_863: 'list3[str27]' = ['']
        i_864: 'int31' = 0
        while True:
            t_5782 = len_5803(this_168.parts_858)
            if not i_864 < t_5782:
                break
            list_get_5811(this_168.parts_858, i_864).format_to(builder_863)
            i_864 = int_add_5812(i_864, 1)
        return ''.join(builder_863)
    def __init__(this_313, parts_866: 'Sequence29[SqlPart]') -> None:
        this_313.parts_858 = parts_866
    @property
    def parts(this_1000) -> 'Sequence29[SqlPart]':
        return this_1000.parts_858
class SqlPart(metaclass = ABCMeta28):
    def format_to(this_169, builder_868: 'list3[str27]') -> 'None':
        raise RuntimeError30()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_870: 'str27'
    __slots__ = ('source_870',)
    def format_to(this_170, builder_872: 'list3[str27]') -> 'None':
        builder_872.append(this_170.source_870)
    def __init__(this_319, source_875: 'str27') -> None:
        this_319.source_870 = source_875
    @property
    def source(this_997) -> 'str27':
        return this_997.source_870
class SqlBoolean(SqlPart):
    value_876: 'bool33'
    __slots__ = ('value_876',)
    def format_to(this_171, builder_878: 'list3[str27]') -> 'None':
        t_3437: 'str27'
        if this_171.value_876:
            t_3437 = 'TRUE'
        else:
            t_3437 = 'FALSE'
        builder_878.append(t_3437)
    def __init__(this_322, value_881: 'bool33') -> None:
        this_322.value_876 = value_881
    @property
    def value(this_1003) -> 'bool33':
        return this_1003.value_876
class SqlDate(SqlPart):
    value_882: 'date26'
    __slots__ = ('value_882',)
    def format_to(this_172, builder_884: 'list3[str27]') -> 'None':
        builder_884.append("'")
        t_5763: 'str27' = date_to_string_5819(this_172.value_882)
        def fn_5761(c_886: 'int31') -> 'None':
            if c_886 == 39:
                builder_884.append("''")
            else:
                builder_884.append(string_from_code_point44(c_886))
        string_for_each_5821(t_5763, fn_5761)
        builder_884.append("'")
    def __init__(this_325, value_888: 'date26') -> None:
        this_325.value_882 = value_888
    @property
    def value(this_1018) -> 'date26':
        return this_1018.value_882
class SqlFloat64(SqlPart):
    value_889: 'float38'
    __slots__ = ('value_889',)
    def format_to(this_173, builder_891: 'list3[str27]') -> 'None':
        t_3426: 'bool33'
        t_3427: 'bool33'
        s_893: 'str27' = float64_to_string_5822(this_173.value_889)
        if s_893 == 'NaN':
            t_3427 = True
        else:
            if s_893 == 'Infinity':
                t_3426 = True
            else:
                t_3426 = s_893 == '-Infinity'
            t_3427 = t_3426
        if t_3427:
            builder_891.append('NULL')
        else:
            builder_891.append(s_893)
    def __init__(this_328, value_895: 'float38') -> None:
        this_328.value_889 = value_895
    @property
    def value(this_1015) -> 'float38':
        return this_1015.value_889
class SqlInt32(SqlPart):
    value_896: 'int31'
    __slots__ = ('value_896',)
    def format_to(this_174, builder_898: 'list3[str27]') -> 'None':
        t_5772: 'str27' = int_to_string_5806(this_174.value_896)
        builder_898.append(t_5772)
    def __init__(this_331, value_901: 'int31') -> None:
        this_331.value_896 = value_901
    @property
    def value(this_1009) -> 'int31':
        return this_1009.value_896
class SqlInt64(SqlPart):
    value_902: 'int64_23'
    __slots__ = ('value_902',)
    def format_to(this_175, builder_904: 'list3[str27]') -> 'None':
        t_5770: 'str27' = int_to_string_5806(this_175.value_902)
        builder_904.append(t_5770)
    def __init__(this_334, value_907: 'int64_23') -> None:
        this_334.value_902 = value_907
    @property
    def value(this_1012) -> 'int64_23':
        return this_1012.value_902
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_908: 'str27'
    __slots__ = ('value_908',)
    def format_to(this_176, builder_910: 'list3[str27]') -> 'None':
        builder_910.append("'")
        def fn_5775(c_912: 'int31') -> 'None':
            if c_912 == 39:
                builder_910.append("''")
            else:
                builder_910.append(string_from_code_point44(c_912))
        string_for_each_5821(this_176.value_908, fn_5775)
        builder_910.append("'")
    def __init__(this_337, value_914: 'str27') -> None:
        this_337.value_908 = value_914
    @property
    def value(this_1006) -> 'str27':
        return this_1006.value_908
def changeset(table_def_484: 'TableDef', params_485: 'MappingProxyType32[str27, str27]') -> 'Changeset':
    t_5558: 'MappingProxyType32[str27, str27]' = map_constructor_5823(())
    return ChangesetImpl_108(table_def_484, params_485, t_5558, (), True)
def is_ident_start_345(c_743: 'int31') -> 'bool33':
    return_270: 'bool33'
    t_3200: 'bool33'
    t_3201: 'bool33'
    if c_743 >= 97:
        t_3200 = c_743 <= 122
    else:
        t_3200 = False
    if t_3200:
        return_270 = True
    else:
        if c_743 >= 65:
            t_3201 = c_743 <= 90
        else:
            t_3201 = False
        if t_3201:
            return_270 = True
        else:
            return_270 = c_743 == 95
    return return_270
def is_ident_part_346(c_745: 'int31') -> 'bool33':
    return_271: 'bool33'
    if is_ident_start_345(c_745):
        return_271 = True
    elif c_745 >= 48:
        return_271 = c_745 <= 57
    else:
        return_271 = False
    return return_271
def safe_identifier(name_747: 'str27') -> 'SafeIdentifier':
    t_5556: 'int31'
    if not name_747:
        raise RuntimeError30()
    idx_749: 'int31' = 0
    if not is_ident_start_345(string_get_5824(name_747, idx_749)):
        raise RuntimeError30()
    t_5553: 'int31' = string_next_5825(name_747, idx_749)
    idx_749 = t_5553
    while True:
        if not len6(name_747) > idx_749:
            break
        if not is_ident_part_346(string_get_5824(name_747, idx_749)):
            raise RuntimeError30()
        t_5556 = string_next_5825(name_747, idx_749)
        idx_749 = t_5556
    return ValidatedIdentifier_142(name_747)
def delete_sql(table_def_574: 'TableDef', id_575: 'int31') -> 'SqlFragment':
    b_577: 'SqlBuilder' = SqlBuilder()
    b_577.append_safe('DELETE FROM ')
    b_577.append_safe(table_def_574.table_name.sql_value)
    b_577.append_safe(' WHERE id = ')
    b_577.append_int32(id_575)
    return b_577.accumulated
def from_(table_name_672: 'SafeIdentifier') -> 'Query':
    return Query(table_name_672, (), (), (), None, None, ())
def col(table_674: 'SafeIdentifier', column_675: 'SafeIdentifier') -> 'SqlFragment':
    b_677: 'SqlBuilder' = SqlBuilder()
    b_677.append_safe(table_674.sql_value)
    b_677.append_safe('.')
    b_677.append_safe(column_675.sql_value)
    return b_677.accumulated
