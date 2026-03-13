from builtins import str as str27, RuntimeError as RuntimeError30, int as int31, bool as bool33, Exception as Exception37, float as float38, isinstance as isinstance39, list as list3, len as len6, tuple as tuple5
from abc import ABCMeta as ABCMeta28
from typing import Sequence as Sequence29, Dict as Dict34, MutableSequence as MutableSequence36, Union as Union40, Any as Any41, TypeVar as TypeVar42, Callable as Callable43
from types import MappingProxyType as MappingProxyType32
from temper_core import Label as Label35, Pair as Pair25, string_from_code_point as string_from_code_point44, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, date_from_iso_string as date_from_iso_string13, list_get as list_get14, int_add as int_add15, mapped_to_list as mapped_to_list16, list_join as list_join17, list_builder_add_all as list_builder_add_all18, date_to_string as date_to_string19, string_for_each as string_for_each20, float64_to_string as float64_to_string21, map_constructor as map_constructor22, string_get as string_get23, string_next as string_next24
from datetime import date as date26
map_builder_set_9679 = map_builder_set0
list_for_each_9680 = list_for_each1
mapped_to_map_9681 = mapped_to_map2
list_9682 = list3
mapped_has_9683 = mapped_has4
tuple_9685 = tuple5
len_9686 = len6
string_count_between_9687 = string_count_between7
str_cat_9688 = str_cat8
int_to_string_9689 = int_to_string9
string_to_int32_9690 = string_to_int3210
string_to_int64_9691 = string_to_int6411
string_to_float64_9692 = string_to_float6412
date_from_iso_string_9693 = date_from_iso_string13
list_get_9694 = list_get14
int_add_9695 = int_add15
mapped_to_list_9696 = mapped_to_list16
list_join_9697 = list_join17
list_builder_add_all_9698 = list_builder_add_all18
date_to_string_9702 = date_to_string19
string_for_each_9704 = string_for_each20
float64_to_string_9705 = float64_to_string21
map_constructor_9706 = map_constructor22
string_get_9707 = string_get23
string_next_9708 = string_next24
pair_9710 = Pair25
date_9713 = date26
class ChangesetError:
    field_466: 'str27'
    message_467: 'str27'
    __slots__ = ('field_466', 'message_467')
    def __init__(this_251, field_469: 'str27', message_470: 'str27') -> None:
        this_251.field_466 = field_469
        this_251.message_467 = message_470
    @property
    def field(this_1360) -> 'str27':
        return this_1360.field_466
    @property
    def message(this_1363) -> 'str27':
        return this_1363.message_467
class Changeset(metaclass = ABCMeta28):
    def cast(this_152, allowed_fields_480: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_required(this_153, fields_483: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_length(this_154, field_486: 'SafeIdentifier', min_487: 'int31', max_488: 'int31') -> 'Changeset':
        raise RuntimeError30()
    def validate_int(this_155, field_491: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_int64(this_156, field_494: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_float(this_157, field_497: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_bool(this_158, field_500: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def to_insert_sql(this_159) -> 'SqlFragment':
        raise RuntimeError30()
    def to_update_sql(this_160, id_505: 'int31') -> 'SqlFragment':
        raise RuntimeError30()
class ChangesetImpl_161(Changeset):
    table_def_507: 'TableDef'
    params_508: 'MappingProxyType32[str27, str27]'
    changes_509: 'MappingProxyType32[str27, str27]'
    errors_510: 'Sequence29[ChangesetError]'
    is_valid_511: 'bool33'
    __slots__ = ('table_def_507', 'params_508', 'changes_509', 'errors_510', 'is_valid_511')
    @property
    def table_def(this_162) -> 'TableDef':
        return this_162.table_def_507
    @property
    def changes(this_163) -> 'MappingProxyType32[str27, str27]':
        return this_163.changes_509
    @property
    def errors(this_164) -> 'Sequence29[ChangesetError]':
        return this_164.errors_510
    @property
    def is_valid(this_165) -> 'bool33':
        return this_165.is_valid_511
    def cast(this_166, allowed_fields_521: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        mb_523: 'Dict34[str27, str27]' = {}
        def fn_9583(f_524: 'SafeIdentifier') -> 'None':
            t_9581: 'str27'
            t_9578: 'str27' = f_524.sql_value
            val_525: 'str27' = this_166.params_508.get(t_9578, '')
            if not (not val_525):
                t_9581 = f_524.sql_value
                map_builder_set_9679(mb_523, t_9581, val_525)
        list_for_each_9680(allowed_fields_521, fn_9583)
        return ChangesetImpl_161(this_166.table_def_507, this_166.params_508, mapped_to_map_9681(mb_523), this_166.errors_510, this_166.is_valid_511)
    def validate_required(this_167, fields_527: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        return_284: 'Changeset'
        t_9576: 'Sequence29[ChangesetError]'
        t_5480: 'TableDef'
        t_5481: 'MappingProxyType32[str27, str27]'
        t_5482: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_528:
            if not this_167.is_valid_511:
                return_284 = this_167
                fn_528.break_()
            eb_529: 'MutableSequence36[ChangesetError]' = list_9682(this_167.errors_510)
            valid_530: 'bool33' = True
            def fn_9572(f_531: 'SafeIdentifier') -> 'None':
                nonlocal valid_530
                t_9570: 'ChangesetError'
                t_9567: 'str27' = f_531.sql_value
                if not mapped_has_9683(this_167.changes_509, t_9567):
                    t_9570 = ChangesetError(f_531.sql_value, 'is required')
                    eb_529.append(t_9570)
                    valid_530 = False
            list_for_each_9680(fields_527, fn_9572)
            t_5480 = this_167.table_def_507
            t_5481 = this_167.params_508
            t_5482 = this_167.changes_509
            t_9576 = tuple_9685(eb_529)
            return_284 = ChangesetImpl_161(t_5480, t_5481, t_5482, t_9576, valid_530)
        return return_284
    def validate_length(this_168, field_533: 'SafeIdentifier', min_534: 'int31', max_535: 'int31') -> 'Changeset':
        return_285: 'Changeset'
        t_9554: 'str27'
        t_9565: 'Sequence29[ChangesetError]'
        t_5463: 'bool33'
        t_5469: 'TableDef'
        t_5470: 'MappingProxyType32[str27, str27]'
        t_5471: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_536:
            if not this_168.is_valid_511:
                return_285 = this_168
                fn_536.break_()
            t_9554 = field_533.sql_value
            val_537: 'str27' = this_168.changes_509.get(t_9554, '')
            len_538: 'int31' = string_count_between_9687(val_537, 0, len_9686(val_537))
            if len_538 < min_534:
                t_5463 = True
            else:
                t_5463 = len_538 > max_535
            if t_5463:
                msg_539: 'str27' = str_cat_9688('must be between ', int_to_string_9689(min_534), ' and ', int_to_string_9689(max_535), ' characters')
                eb_540: 'MutableSequence36[ChangesetError]' = list_9682(this_168.errors_510)
                eb_540.append(ChangesetError(field_533.sql_value, msg_539))
                t_5469 = this_168.table_def_507
                t_5470 = this_168.params_508
                t_5471 = this_168.changes_509
                t_9565 = tuple_9685(eb_540)
                return_285 = ChangesetImpl_161(t_5469, t_5470, t_5471, t_9565, False)
                fn_536.break_()
            return_285 = this_168
        return return_285
    def validate_int(this_169, field_542: 'SafeIdentifier') -> 'Changeset':
        return_286: 'Changeset'
        t_9545: 'str27'
        t_9552: 'Sequence29[ChangesetError]'
        t_5454: 'TableDef'
        t_5455: 'MappingProxyType32[str27, str27]'
        t_5456: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_543:
            if not this_169.is_valid_511:
                return_286 = this_169
                fn_543.break_()
            t_9545 = field_542.sql_value
            val_544: 'str27' = this_169.changes_509.get(t_9545, '')
            if not val_544:
                return_286 = this_169
                fn_543.break_()
            parse_ok_545: 'bool33'
            try:
                string_to_int32_9690(val_544)
                parse_ok_545 = True
            except Exception37:
                parse_ok_545 = False
            if not parse_ok_545:
                eb_546: 'MutableSequence36[ChangesetError]' = list_9682(this_169.errors_510)
                eb_546.append(ChangesetError(field_542.sql_value, 'must be an integer'))
                t_5454 = this_169.table_def_507
                t_5455 = this_169.params_508
                t_5456 = this_169.changes_509
                t_9552 = tuple_9685(eb_546)
                return_286 = ChangesetImpl_161(t_5454, t_5455, t_5456, t_9552, False)
                fn_543.break_()
            return_286 = this_169
        return return_286
    def validate_int64(this_170, field_548: 'SafeIdentifier') -> 'Changeset':
        return_287: 'Changeset'
        t_9536: 'str27'
        t_9543: 'Sequence29[ChangesetError]'
        t_5441: 'TableDef'
        t_5442: 'MappingProxyType32[str27, str27]'
        t_5443: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_549:
            if not this_170.is_valid_511:
                return_287 = this_170
                fn_549.break_()
            t_9536 = field_548.sql_value
            val_550: 'str27' = this_170.changes_509.get(t_9536, '')
            if not val_550:
                return_287 = this_170
                fn_549.break_()
            parse_ok_551: 'bool33'
            try:
                string_to_int64_9691(val_550)
                parse_ok_551 = True
            except Exception37:
                parse_ok_551 = False
            if not parse_ok_551:
                eb_552: 'MutableSequence36[ChangesetError]' = list_9682(this_170.errors_510)
                eb_552.append(ChangesetError(field_548.sql_value, 'must be a 64-bit integer'))
                t_5441 = this_170.table_def_507
                t_5442 = this_170.params_508
                t_5443 = this_170.changes_509
                t_9543 = tuple_9685(eb_552)
                return_287 = ChangesetImpl_161(t_5441, t_5442, t_5443, t_9543, False)
                fn_549.break_()
            return_287 = this_170
        return return_287
    def validate_float(this_171, field_554: 'SafeIdentifier') -> 'Changeset':
        return_288: 'Changeset'
        t_9527: 'str27'
        t_9534: 'Sequence29[ChangesetError]'
        t_5428: 'TableDef'
        t_5429: 'MappingProxyType32[str27, str27]'
        t_5430: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_555:
            if not this_171.is_valid_511:
                return_288 = this_171
                fn_555.break_()
            t_9527 = field_554.sql_value
            val_556: 'str27' = this_171.changes_509.get(t_9527, '')
            if not val_556:
                return_288 = this_171
                fn_555.break_()
            parse_ok_557: 'bool33'
            try:
                string_to_float64_9692(val_556)
                parse_ok_557 = True
            except Exception37:
                parse_ok_557 = False
            if not parse_ok_557:
                eb_558: 'MutableSequence36[ChangesetError]' = list_9682(this_171.errors_510)
                eb_558.append(ChangesetError(field_554.sql_value, 'must be a number'))
                t_5428 = this_171.table_def_507
                t_5429 = this_171.params_508
                t_5430 = this_171.changes_509
                t_9534 = tuple_9685(eb_558)
                return_288 = ChangesetImpl_161(t_5428, t_5429, t_5430, t_9534, False)
                fn_555.break_()
            return_288 = this_171
        return return_288
    def validate_bool(this_172, field_560: 'SafeIdentifier') -> 'Changeset':
        return_289: 'Changeset'
        t_9518: 'str27'
        t_9525: 'Sequence29[ChangesetError]'
        t_5403: 'bool33'
        t_5404: 'bool33'
        t_5406: 'bool33'
        t_5407: 'bool33'
        t_5409: 'bool33'
        t_5415: 'TableDef'
        t_5416: 'MappingProxyType32[str27, str27]'
        t_5417: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_561:
            if not this_172.is_valid_511:
                return_289 = this_172
                fn_561.break_()
            t_9518 = field_560.sql_value
            val_562: 'str27' = this_172.changes_509.get(t_9518, '')
            if not val_562:
                return_289 = this_172
                fn_561.break_()
            is_true_563: 'bool33'
            if val_562 == 'true':
                is_true_563 = True
            else:
                if val_562 == '1':
                    t_5404 = True
                else:
                    if val_562 == 'yes':
                        t_5403 = True
                    else:
                        t_5403 = val_562 == 'on'
                    t_5404 = t_5403
                is_true_563 = t_5404
            is_false_564: 'bool33'
            if val_562 == 'false':
                is_false_564 = True
            else:
                if val_562 == '0':
                    t_5407 = True
                else:
                    if val_562 == 'no':
                        t_5406 = True
                    else:
                        t_5406 = val_562 == 'off'
                    t_5407 = t_5406
                is_false_564 = t_5407
            if not is_true_563:
                t_5409 = not is_false_564
            else:
                t_5409 = False
            if t_5409:
                eb_565: 'MutableSequence36[ChangesetError]' = list_9682(this_172.errors_510)
                eb_565.append(ChangesetError(field_560.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_5415 = this_172.table_def_507
                t_5416 = this_172.params_508
                t_5417 = this_172.changes_509
                t_9525 = tuple_9685(eb_565)
                return_289 = ChangesetImpl_161(t_5415, t_5416, t_5417, t_9525, False)
                fn_561.break_()
            return_289 = this_172
        return return_289
    def parse_bool_sql_part_566(this_173, val_567: 'str27') -> 'SqlBoolean':
        return_290: 'SqlBoolean'
        t_5392: 'bool33'
        t_5393: 'bool33'
        t_5394: 'bool33'
        t_5396: 'bool33'
        t_5397: 'bool33'
        t_5398: 'bool33'
        with Label35() as fn_568:
            if val_567 == 'true':
                t_5394 = True
            else:
                if val_567 == '1':
                    t_5393 = True
                else:
                    if val_567 == 'yes':
                        t_5392 = True
                    else:
                        t_5392 = val_567 == 'on'
                    t_5393 = t_5392
                t_5394 = t_5393
            if t_5394:
                return_290 = SqlBoolean(True)
                fn_568.break_()
            if val_567 == 'false':
                t_5398 = True
            else:
                if val_567 == '0':
                    t_5397 = True
                else:
                    if val_567 == 'no':
                        t_5396 = True
                    else:
                        t_5396 = val_567 == 'off'
                    t_5397 = t_5396
                t_5398 = t_5397
            if t_5398:
                return_290 = SqlBoolean(False)
                fn_568.break_()
            raise RuntimeError30()
        return return_290
    def value_to_sql_part_569(this_174, field_def_570: 'FieldDef', val_571: 'str27') -> 'SqlPart':
        return_291: 'SqlPart'
        t_5379: 'int31'
        t_5382: 'int64_23'
        t_5385: 'float38'
        t_5390: 'date26'
        with Label35() as fn_572:
            ft_573: 'FieldType' = field_def_570.field_type
            if isinstance39(ft_573, StringField):
                return_291 = SqlString(val_571)
                fn_572.break_()
            if isinstance39(ft_573, IntField):
                t_5379 = string_to_int32_9690(val_571)
                return_291 = SqlInt32(t_5379)
                fn_572.break_()
            if isinstance39(ft_573, Int64Field):
                t_5382 = string_to_int64_9691(val_571)
                return_291 = SqlInt64(t_5382)
                fn_572.break_()
            if isinstance39(ft_573, FloatField):
                t_5385 = string_to_float64_9692(val_571)
                return_291 = SqlFloat64(t_5385)
                fn_572.break_()
            if isinstance39(ft_573, BoolField):
                return_291 = this_174.parse_bool_sql_part_566(val_571)
                fn_572.break_()
            if isinstance39(ft_573, DateField):
                t_5390 = date_from_iso_string_9693(val_571)
                return_291 = SqlDate(t_5390)
                fn_572.break_()
            raise RuntimeError30()
        return return_291
    def to_insert_sql(this_175) -> 'SqlFragment':
        t_9466: 'int31'
        t_9471: 'str27'
        t_9472: 'bool33'
        t_9477: 'int31'
        t_9479: 'str27'
        t_9483: 'str27'
        t_9498: 'int31'
        t_5343: 'bool33'
        t_5351: 'FieldDef'
        t_5356: 'SqlPart'
        if not this_175.is_valid_511:
            raise RuntimeError30()
        i_576: 'int31' = 0
        while True:
            t_9466 = len_9686(this_175.table_def_507.fields)
            if not i_576 < t_9466:
                break
            f_577: 'FieldDef' = list_get_9694(this_175.table_def_507.fields, i_576)
            if not f_577.nullable:
                t_9471 = f_577.name.sql_value
                t_9472 = mapped_has_9683(this_175.changes_509, t_9471)
                t_5343 = not t_9472
            else:
                t_5343 = False
            if t_5343:
                raise RuntimeError30()
            i_576 = int_add_9695(i_576, 1)
        pairs_578: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_9696(this_175.changes_509)
        if len_9686(pairs_578) == 0:
            raise RuntimeError30()
        col_names_579: 'MutableSequence36[str27]' = list_9682()
        val_parts_580: 'MutableSequence36[SqlPart]' = list_9682()
        i_581: 'int31' = 0
        while True:
            t_9477 = len_9686(pairs_578)
            if not i_581 < t_9477:
                break
            pair_582: 'Pair25[str27, str27]' = list_get_9694(pairs_578, i_581)
            t_9479 = pair_582.key
            t_5351 = this_175.table_def_507.field(t_9479)
            fd_583: 'FieldDef' = t_5351
            col_names_579.append(fd_583.name.sql_value)
            t_9483 = pair_582.value
            t_5356 = this_175.value_to_sql_part_569(fd_583, t_9483)
            val_parts_580.append(t_5356)
            i_581 = int_add_9695(i_581, 1)
        b_584: 'SqlBuilder' = SqlBuilder()
        b_584.append_safe('INSERT INTO ')
        b_584.append_safe(this_175.table_def_507.table_name.sql_value)
        b_584.append_safe(' (')
        t_9491: 'Sequence29[str27]' = tuple_9685(col_names_579)
        def fn_9464(c_585: 'str27') -> 'str27':
            return c_585
        b_584.append_safe(list_join_9697(t_9491, ', ', fn_9464))
        b_584.append_safe(') VALUES (')
        b_584.append_part(list_get_9694(val_parts_580, 0))
        j_586: 'int31' = 1
        while True:
            t_9498 = len_9686(val_parts_580)
            if not j_586 < t_9498:
                break
            b_584.append_safe(', ')
            b_584.append_part(list_get_9694(val_parts_580, j_586))
            j_586 = int_add_9695(j_586, 1)
        b_584.append_safe(')')
        return b_584.accumulated
    def to_update_sql(this_176, id_588: 'int31') -> 'SqlFragment':
        t_9451: 'int31'
        t_9454: 'str27'
        t_9459: 'str27'
        t_5324: 'FieldDef'
        t_5330: 'SqlPart'
        if not this_176.is_valid_511:
            raise RuntimeError30()
        pairs_590: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_9696(this_176.changes_509)
        if len_9686(pairs_590) == 0:
            raise RuntimeError30()
        b_591: 'SqlBuilder' = SqlBuilder()
        b_591.append_safe('UPDATE ')
        b_591.append_safe(this_176.table_def_507.table_name.sql_value)
        b_591.append_safe(' SET ')
        i_592: 'int31' = 0
        while True:
            t_9451 = len_9686(pairs_590)
            if not i_592 < t_9451:
                break
            if i_592 > 0:
                b_591.append_safe(', ')
            pair_593: 'Pair25[str27, str27]' = list_get_9694(pairs_590, i_592)
            t_9454 = pair_593.key
            t_5324 = this_176.table_def_507.field(t_9454)
            fd_594: 'FieldDef' = t_5324
            b_591.append_safe(fd_594.name.sql_value)
            b_591.append_safe(' = ')
            t_9459 = pair_593.value
            t_5330 = this_176.value_to_sql_part_569(fd_594, t_9459)
            b_591.append_part(t_5330)
            i_592 = int_add_9695(i_592, 1)
        b_591.append_safe(' WHERE id = ')
        b_591.append_int32(id_588)
        return b_591.accumulated
    def __init__(this_274, table_def_596: 'TableDef', params_597: 'MappingProxyType32[str27, str27]', changes_598: 'MappingProxyType32[str27, str27]', errors_599: 'Sequence29[ChangesetError]', is_valid_600: 'bool33') -> None:
        this_274.table_def_507 = table_def_596
        this_274.params_508 = params_597
        this_274.changes_509 = changes_598
        this_274.errors_510 = errors_599
        this_274.is_valid_511 = is_valid_600
class JoinType(metaclass = ABCMeta28):
    def keyword(this_177) -> 'str27':
        raise RuntimeError30()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_178) -> 'str27':
        return 'INNER JOIN'
    def __init__(this_299) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_179) -> 'str27':
        return 'LEFT JOIN'
    def __init__(this_302) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_180) -> 'str27':
        return 'RIGHT JOIN'
    def __init__(this_305) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_181) -> 'str27':
        return 'FULL OUTER JOIN'
    def __init__(this_308) -> None:
        pass
class JoinClause:
    join_type_709: 'JoinType'
    table_710: 'SafeIdentifier'
    on_condition_711: 'SqlFragment'
    __slots__ = ('join_type_709', 'table_710', 'on_condition_711')
    def __init__(this_311, join_type_713: 'JoinType', table_714: 'SafeIdentifier', on_condition_715: 'SqlFragment') -> None:
        this_311.join_type_709 = join_type_713
        this_311.table_710 = table_714
        this_311.on_condition_711 = on_condition_715
    @property
    def join_type(this_1428) -> 'JoinType':
        return this_1428.join_type_709
    @property
    def table(this_1431) -> 'SafeIdentifier':
        return this_1431.table_710
    @property
    def on_condition(this_1434) -> 'SqlFragment':
        return this_1434.on_condition_711
class OrderClause:
    field_716: 'SafeIdentifier'
    ascending_717: 'bool33'
    __slots__ = ('field_716', 'ascending_717')
    def __init__(this_313, field_719: 'SafeIdentifier', ascending_720: 'bool33') -> None:
        this_313.field_716 = field_719
        this_313.ascending_717 = ascending_720
    @property
    def field(this_1437) -> 'SafeIdentifier':
        return this_1437.field_716
    @property
    def ascending(this_1440) -> 'bool33':
        return this_1440.ascending_717
class WhereClause(metaclass = ABCMeta28):
    def keyword(this_183) -> 'str27':
        raise RuntimeError30()
class AndCondition(WhereClause):
    condition_725: 'SqlFragment'
    __slots__ = ('condition_725',)
    @property
    def condition(this_184) -> 'SqlFragment':
        return this_184.condition_725
    def keyword(this_185) -> 'str27':
        return 'AND'
    def __init__(this_319, condition_731: 'SqlFragment') -> None:
        this_319.condition_725 = condition_731
class OrCondition(WhereClause):
    condition_732: 'SqlFragment'
    __slots__ = ('condition_732',)
    @property
    def condition(this_186) -> 'SqlFragment':
        return this_186.condition_732
    def keyword(this_187) -> 'str27':
        return 'OR'
    def __init__(this_324, condition_738: 'SqlFragment') -> None:
        this_324.condition_732 = condition_738
class Query:
    table_name_739: 'SafeIdentifier'
    conditions_740: 'Sequence29[WhereClause]'
    selected_fields_741: 'Sequence29[SafeIdentifier]'
    order_clauses_742: 'Sequence29[OrderClause]'
    limit_val_743: 'Union40[int31, None]'
    offset_val_744: 'Union40[int31, None]'
    join_clauses_745: 'Sequence29[JoinClause]'
    group_by_fields_746: 'Sequence29[SafeIdentifier]'
    having_conditions_747: 'Sequence29[WhereClause]'
    is_distinct_748: 'bool33'
    select_exprs_749: 'Sequence29[SqlFragment]'
    __slots__ = ('table_name_739', 'conditions_740', 'selected_fields_741', 'order_clauses_742', 'limit_val_743', 'offset_val_744', 'join_clauses_745', 'group_by_fields_746', 'having_conditions_747', 'is_distinct_748', 'select_exprs_749')
    def where(this_188, condition_751: 'SqlFragment') -> 'Query':
        nb_753: 'MutableSequence36[WhereClause]' = list_9682(this_188.conditions_740)
        nb_753.append(AndCondition(condition_751))
        return Query(this_188.table_name_739, tuple_9685(nb_753), this_188.selected_fields_741, this_188.order_clauses_742, this_188.limit_val_743, this_188.offset_val_744, this_188.join_clauses_745, this_188.group_by_fields_746, this_188.having_conditions_747, this_188.is_distinct_748, this_188.select_exprs_749)
    def or_where(this_189, condition_755: 'SqlFragment') -> 'Query':
        nb_757: 'MutableSequence36[WhereClause]' = list_9682(this_189.conditions_740)
        nb_757.append(OrCondition(condition_755))
        return Query(this_189.table_name_739, tuple_9685(nb_757), this_189.selected_fields_741, this_189.order_clauses_742, this_189.limit_val_743, this_189.offset_val_744, this_189.join_clauses_745, this_189.group_by_fields_746, this_189.having_conditions_747, this_189.is_distinct_748, this_189.select_exprs_749)
    def where_null(this_190, field_759: 'SafeIdentifier') -> 'Query':
        b_761: 'SqlBuilder' = SqlBuilder()
        b_761.append_safe(field_759.sql_value)
        b_761.append_safe(' IS NULL')
        t_9050: 'SqlFragment' = b_761.accumulated
        return this_190.where(t_9050)
    def where_not_null(this_191, field_763: 'SafeIdentifier') -> 'Query':
        b_765: 'SqlBuilder' = SqlBuilder()
        b_765.append_safe(field_763.sql_value)
        b_765.append_safe(' IS NOT NULL')
        t_9044: 'SqlFragment' = b_765.accumulated
        return this_191.where(t_9044)
    def where_in(this_192, field_767: 'SafeIdentifier', values_768: 'Sequence29[SqlPart]') -> 'Query':
        return_343: 'Query'
        t_9025: 'SqlFragment'
        t_9033: 'int31'
        t_9038: 'SqlFragment'
        with Label35() as fn_769:
            if not values_768:
                b_770: 'SqlBuilder' = SqlBuilder()
                b_770.append_safe('1 = 0')
                t_9025 = b_770.accumulated
                return_343 = this_192.where(t_9025)
                fn_769.break_()
            b_771: 'SqlBuilder' = SqlBuilder()
            b_771.append_safe(field_767.sql_value)
            b_771.append_safe(' IN (')
            b_771.append_part(list_get_9694(values_768, 0))
            i_772: 'int31' = 1
            while True:
                t_9033 = len_9686(values_768)
                if not i_772 < t_9033:
                    break
                b_771.append_safe(', ')
                b_771.append_part(list_get_9694(values_768, i_772))
                i_772 = int_add_9695(i_772, 1)
            b_771.append_safe(')')
            t_9038 = b_771.accumulated
            return_343 = this_192.where(t_9038)
        return return_343
    def where_in_subquery(this_193, field_774: 'SafeIdentifier', sub_775: 'Query') -> 'Query':
        b_777: 'SqlBuilder' = SqlBuilder()
        b_777.append_safe(field_774.sql_value)
        b_777.append_safe(' IN (')
        b_777.append_fragment(sub_775.to_sql())
        b_777.append_safe(')')
        t_9020: 'SqlFragment' = b_777.accumulated
        return this_193.where(t_9020)
    def where_not(this_194, condition_779: 'SqlFragment') -> 'Query':
        b_781: 'SqlBuilder' = SqlBuilder()
        b_781.append_safe('NOT (')
        b_781.append_fragment(condition_779)
        b_781.append_safe(')')
        t_9011: 'SqlFragment' = b_781.accumulated
        return this_194.where(t_9011)
    def where_between(this_195, field_783: 'SafeIdentifier', low_784: 'SqlPart', high_785: 'SqlPart') -> 'Query':
        b_787: 'SqlBuilder' = SqlBuilder()
        b_787.append_safe(field_783.sql_value)
        b_787.append_safe(' BETWEEN ')
        b_787.append_part(low_784)
        b_787.append_safe(' AND ')
        b_787.append_part(high_785)
        t_9005: 'SqlFragment' = b_787.accumulated
        return this_195.where(t_9005)
    def where_like(this_196, field_789: 'SafeIdentifier', pattern_790: 'str27') -> 'Query':
        b_792: 'SqlBuilder' = SqlBuilder()
        b_792.append_safe(field_789.sql_value)
        b_792.append_safe(' LIKE ')
        b_792.append_string(pattern_790)
        t_8996: 'SqlFragment' = b_792.accumulated
        return this_196.where(t_8996)
    def where_i_like(this_197, field_794: 'SafeIdentifier', pattern_795: 'str27') -> 'Query':
        b_797: 'SqlBuilder' = SqlBuilder()
        b_797.append_safe(field_794.sql_value)
        b_797.append_safe(' ILIKE ')
        b_797.append_string(pattern_795)
        t_8989: 'SqlFragment' = b_797.accumulated
        return this_197.where(t_8989)
    def select(this_198, fields_799: 'Sequence29[SafeIdentifier]') -> 'Query':
        return Query(this_198.table_name_739, this_198.conditions_740, fields_799, this_198.order_clauses_742, this_198.limit_val_743, this_198.offset_val_744, this_198.join_clauses_745, this_198.group_by_fields_746, this_198.having_conditions_747, this_198.is_distinct_748, this_198.select_exprs_749)
    def select_expr(this_199, exprs_802: 'Sequence29[SqlFragment]') -> 'Query':
        return Query(this_199.table_name_739, this_199.conditions_740, this_199.selected_fields_741, this_199.order_clauses_742, this_199.limit_val_743, this_199.offset_val_744, this_199.join_clauses_745, this_199.group_by_fields_746, this_199.having_conditions_747, this_199.is_distinct_748, exprs_802)
    def order_by(this_200, field_805: 'SafeIdentifier', ascending_806: 'bool33') -> 'Query':
        nb_808: 'MutableSequence36[OrderClause]' = list_9682(this_200.order_clauses_742)
        nb_808.append(OrderClause(field_805, ascending_806))
        return Query(this_200.table_name_739, this_200.conditions_740, this_200.selected_fields_741, tuple_9685(nb_808), this_200.limit_val_743, this_200.offset_val_744, this_200.join_clauses_745, this_200.group_by_fields_746, this_200.having_conditions_747, this_200.is_distinct_748, this_200.select_exprs_749)
    def limit(this_201, n_810: 'int31') -> 'Query':
        if n_810 < 0:
            raise RuntimeError30()
        return Query(this_201.table_name_739, this_201.conditions_740, this_201.selected_fields_741, this_201.order_clauses_742, n_810, this_201.offset_val_744, this_201.join_clauses_745, this_201.group_by_fields_746, this_201.having_conditions_747, this_201.is_distinct_748, this_201.select_exprs_749)
    def offset(this_202, n_813: 'int31') -> 'Query':
        if n_813 < 0:
            raise RuntimeError30()
        return Query(this_202.table_name_739, this_202.conditions_740, this_202.selected_fields_741, this_202.order_clauses_742, this_202.limit_val_743, n_813, this_202.join_clauses_745, this_202.group_by_fields_746, this_202.having_conditions_747, this_202.is_distinct_748, this_202.select_exprs_749)
    def join(this_203, join_type_816: 'JoinType', table_817: 'SafeIdentifier', on_condition_818: 'SqlFragment') -> 'Query':
        nb_820: 'MutableSequence36[JoinClause]' = list_9682(this_203.join_clauses_745)
        nb_820.append(JoinClause(join_type_816, table_817, on_condition_818))
        return Query(this_203.table_name_739, this_203.conditions_740, this_203.selected_fields_741, this_203.order_clauses_742, this_203.limit_val_743, this_203.offset_val_744, tuple_9685(nb_820), this_203.group_by_fields_746, this_203.having_conditions_747, this_203.is_distinct_748, this_203.select_exprs_749)
    def inner_join(this_204, table_822: 'SafeIdentifier', on_condition_823: 'SqlFragment') -> 'Query':
        t_8959: 'InnerJoin' = InnerJoin()
        return this_204.join(t_8959, table_822, on_condition_823)
    def left_join(this_205, table_826: 'SafeIdentifier', on_condition_827: 'SqlFragment') -> 'Query':
        t_8957: 'LeftJoin' = LeftJoin()
        return this_205.join(t_8957, table_826, on_condition_827)
    def right_join(this_206, table_830: 'SafeIdentifier', on_condition_831: 'SqlFragment') -> 'Query':
        t_8955: 'RightJoin' = RightJoin()
        return this_206.join(t_8955, table_830, on_condition_831)
    def full_join(this_207, table_834: 'SafeIdentifier', on_condition_835: 'SqlFragment') -> 'Query':
        t_8953: 'FullJoin' = FullJoin()
        return this_207.join(t_8953, table_834, on_condition_835)
    def group_by(this_208, field_838: 'SafeIdentifier') -> 'Query':
        nb_840: 'MutableSequence36[SafeIdentifier]' = list_9682(this_208.group_by_fields_746)
        nb_840.append(field_838)
        return Query(this_208.table_name_739, this_208.conditions_740, this_208.selected_fields_741, this_208.order_clauses_742, this_208.limit_val_743, this_208.offset_val_744, this_208.join_clauses_745, tuple_9685(nb_840), this_208.having_conditions_747, this_208.is_distinct_748, this_208.select_exprs_749)
    def having(this_209, condition_842: 'SqlFragment') -> 'Query':
        nb_844: 'MutableSequence36[WhereClause]' = list_9682(this_209.having_conditions_747)
        nb_844.append(AndCondition(condition_842))
        return Query(this_209.table_name_739, this_209.conditions_740, this_209.selected_fields_741, this_209.order_clauses_742, this_209.limit_val_743, this_209.offset_val_744, this_209.join_clauses_745, this_209.group_by_fields_746, tuple_9685(nb_844), this_209.is_distinct_748, this_209.select_exprs_749)
    def or_having(this_210, condition_846: 'SqlFragment') -> 'Query':
        nb_848: 'MutableSequence36[WhereClause]' = list_9682(this_210.having_conditions_747)
        nb_848.append(OrCondition(condition_846))
        return Query(this_210.table_name_739, this_210.conditions_740, this_210.selected_fields_741, this_210.order_clauses_742, this_210.limit_val_743, this_210.offset_val_744, this_210.join_clauses_745, this_210.group_by_fields_746, tuple_9685(nb_848), this_210.is_distinct_748, this_210.select_exprs_749)
    def distinct(this_211) -> 'Query':
        return Query(this_211.table_name_739, this_211.conditions_740, this_211.selected_fields_741, this_211.order_clauses_742, this_211.limit_val_743, this_211.offset_val_744, this_211.join_clauses_745, this_211.group_by_fields_746, this_211.having_conditions_747, True, this_211.select_exprs_749)
    def to_sql(this_212) -> 'SqlFragment':
        t_8859: 'int31'
        t_8878: 'int31'
        t_8897: 'int31'
        b_853: 'SqlBuilder' = SqlBuilder()
        if this_212.is_distinct_748:
            b_853.append_safe('SELECT DISTINCT ')
        else:
            b_853.append_safe('SELECT ')
        if not (not this_212.select_exprs_749):
            b_853.append_fragment(list_get_9694(this_212.select_exprs_749, 0))
            i_854: 'int31' = 1
            while True:
                t_8859 = len_9686(this_212.select_exprs_749)
                if not i_854 < t_8859:
                    break
                b_853.append_safe(', ')
                b_853.append_fragment(list_get_9694(this_212.select_exprs_749, i_854))
                i_854 = int_add_9695(i_854, 1)
        elif not this_212.selected_fields_741:
            b_853.append_safe('*')
        else:
            def fn_8852(f_855: 'SafeIdentifier') -> 'str27':
                return f_855.sql_value
            b_853.append_safe(list_join_9697(this_212.selected_fields_741, ', ', fn_8852))
        b_853.append_safe(' FROM ')
        b_853.append_safe(this_212.table_name_739.sql_value)
        def fn_8851(jc_856: 'JoinClause') -> 'None':
            b_853.append_safe(' ')
            t_8839: 'str27' = jc_856.join_type.keyword()
            b_853.append_safe(t_8839)
            b_853.append_safe(' ')
            t_8843: 'str27' = jc_856.table.sql_value
            b_853.append_safe(t_8843)
            b_853.append_safe(' ON ')
            t_8846: 'SqlFragment' = jc_856.on_condition
            b_853.append_fragment(t_8846)
        list_for_each_9680(this_212.join_clauses_745, fn_8851)
        if not (not this_212.conditions_740):
            b_853.append_safe(' WHERE ')
            b_853.append_fragment(list_get_9694(this_212.conditions_740, 0).condition)
            i_857: 'int31' = 1
            while True:
                t_8878 = len_9686(this_212.conditions_740)
                if not i_857 < t_8878:
                    break
                b_853.append_safe(' ')
                b_853.append_safe(list_get_9694(this_212.conditions_740, i_857).keyword())
                b_853.append_safe(' ')
                b_853.append_fragment(list_get_9694(this_212.conditions_740, i_857).condition)
                i_857 = int_add_9695(i_857, 1)
        if not (not this_212.group_by_fields_746):
            b_853.append_safe(' GROUP BY ')
            def fn_8850(f_858: 'SafeIdentifier') -> 'str27':
                return f_858.sql_value
            b_853.append_safe(list_join_9697(this_212.group_by_fields_746, ', ', fn_8850))
        if not (not this_212.having_conditions_747):
            b_853.append_safe(' HAVING ')
            b_853.append_fragment(list_get_9694(this_212.having_conditions_747, 0).condition)
            i_859: 'int31' = 1
            while True:
                t_8897 = len_9686(this_212.having_conditions_747)
                if not i_859 < t_8897:
                    break
                b_853.append_safe(' ')
                b_853.append_safe(list_get_9694(this_212.having_conditions_747, i_859).keyword())
                b_853.append_safe(' ')
                b_853.append_fragment(list_get_9694(this_212.having_conditions_747, i_859).condition)
                i_859 = int_add_9695(i_859, 1)
        if not (not this_212.order_clauses_742):
            b_853.append_safe(' ORDER BY ')
            first_860: 'bool33' = True
            def fn_8849(oc_861: 'OrderClause') -> 'None':
                nonlocal first_860
                t_4769: 'str27'
                if not first_860:
                    b_853.append_safe(', ')
                first_860 = False
                t_8832: 'str27' = oc_861.field.sql_value
                b_853.append_safe(t_8832)
                if oc_861.ascending:
                    t_4769 = ' ASC'
                else:
                    t_4769 = ' DESC'
                b_853.append_safe(t_4769)
            list_for_each_9680(this_212.order_clauses_742, fn_8849)
        lv_862: 'Union40[int31, None]' = this_212.limit_val_743
        if not lv_862 is None:
            lv_1742: 'int31' = lv_862
            b_853.append_safe(' LIMIT ')
            b_853.append_int32(lv_1742)
        ov_863: 'Union40[int31, None]' = this_212.offset_val_744
        if not ov_863 is None:
            ov_1743: 'int31' = ov_863
            b_853.append_safe(' OFFSET ')
            b_853.append_int32(ov_1743)
        return b_853.accumulated
    def count_sql(this_213) -> 'SqlFragment':
        t_8801: 'int31'
        t_8820: 'int31'
        b_866: 'SqlBuilder' = SqlBuilder()
        b_866.append_safe('SELECT COUNT(*) FROM ')
        b_866.append_safe(this_213.table_name_739.sql_value)
        def fn_8789(jc_867: 'JoinClause') -> 'None':
            b_866.append_safe(' ')
            t_8779: 'str27' = jc_867.join_type.keyword()
            b_866.append_safe(t_8779)
            b_866.append_safe(' ')
            t_8783: 'str27' = jc_867.table.sql_value
            b_866.append_safe(t_8783)
            b_866.append_safe(' ON ')
            t_8786: 'SqlFragment' = jc_867.on_condition
            b_866.append_fragment(t_8786)
        list_for_each_9680(this_213.join_clauses_745, fn_8789)
        if not (not this_213.conditions_740):
            b_866.append_safe(' WHERE ')
            b_866.append_fragment(list_get_9694(this_213.conditions_740, 0).condition)
            i_868: 'int31' = 1
            while True:
                t_8801 = len_9686(this_213.conditions_740)
                if not i_868 < t_8801:
                    break
                b_866.append_safe(' ')
                b_866.append_safe(list_get_9694(this_213.conditions_740, i_868).keyword())
                b_866.append_safe(' ')
                b_866.append_fragment(list_get_9694(this_213.conditions_740, i_868).condition)
                i_868 = int_add_9695(i_868, 1)
        if not (not this_213.group_by_fields_746):
            b_866.append_safe(' GROUP BY ')
            def fn_8788(f_869: 'SafeIdentifier') -> 'str27':
                return f_869.sql_value
            b_866.append_safe(list_join_9697(this_213.group_by_fields_746, ', ', fn_8788))
        if not (not this_213.having_conditions_747):
            b_866.append_safe(' HAVING ')
            b_866.append_fragment(list_get_9694(this_213.having_conditions_747, 0).condition)
            i_870: 'int31' = 1
            while True:
                t_8820 = len_9686(this_213.having_conditions_747)
                if not i_870 < t_8820:
                    break
                b_866.append_safe(' ')
                b_866.append_safe(list_get_9694(this_213.having_conditions_747, i_870).keyword())
                b_866.append_safe(' ')
                b_866.append_fragment(list_get_9694(this_213.having_conditions_747, i_870).condition)
                i_870 = int_add_9695(i_870, 1)
        return b_866.accumulated
    def safe_to_sql(this_214, default_limit_872: 'int31') -> 'SqlFragment':
        return_365: 'SqlFragment'
        t_4718: 'Query'
        if default_limit_872 < 0:
            raise RuntimeError30()
        if not this_214.limit_val_743 is None:
            return_365 = this_214.to_sql()
        else:
            t_4718 = this_214.limit(default_limit_872)
            return_365 = t_4718.to_sql()
        return return_365
    def __init__(this_328, table_name_875: 'SafeIdentifier', conditions_876: 'Sequence29[WhereClause]', selected_fields_877: 'Sequence29[SafeIdentifier]', order_clauses_878: 'Sequence29[OrderClause]', limit_val_879: 'Union40[int31, None]', offset_val_880: 'Union40[int31, None]', join_clauses_881: 'Sequence29[JoinClause]', group_by_fields_882: 'Sequence29[SafeIdentifier]', having_conditions_883: 'Sequence29[WhereClause]', is_distinct_884: 'bool33', select_exprs_885: 'Sequence29[SqlFragment]') -> None:
        this_328.table_name_739 = table_name_875
        this_328.conditions_740 = conditions_876
        this_328.selected_fields_741 = selected_fields_877
        this_328.order_clauses_742 = order_clauses_878
        this_328.limit_val_743 = limit_val_879
        this_328.offset_val_744 = offset_val_880
        this_328.join_clauses_745 = join_clauses_881
        this_328.group_by_fields_746 = group_by_fields_882
        this_328.having_conditions_747 = having_conditions_883
        this_328.is_distinct_748 = is_distinct_884
        this_328.select_exprs_749 = select_exprs_885
    @property
    def table_name(this_1443) -> 'SafeIdentifier':
        return this_1443.table_name_739
    @property
    def conditions(this_1446) -> 'Sequence29[WhereClause]':
        return this_1446.conditions_740
    @property
    def selected_fields(this_1449) -> 'Sequence29[SafeIdentifier]':
        return this_1449.selected_fields_741
    @property
    def order_clauses(this_1452) -> 'Sequence29[OrderClause]':
        return this_1452.order_clauses_742
    @property
    def limit_val(this_1455) -> 'Union40[int31, None]':
        return this_1455.limit_val_743
    @property
    def offset_val(this_1458) -> 'Union40[int31, None]':
        return this_1458.offset_val_744
    @property
    def join_clauses(this_1461) -> 'Sequence29[JoinClause]':
        return this_1461.join_clauses_745
    @property
    def group_by_fields(this_1464) -> 'Sequence29[SafeIdentifier]':
        return this_1464.group_by_fields_746
    @property
    def having_conditions(this_1467) -> 'Sequence29[WhereClause]':
        return this_1467.having_conditions_747
    @property
    def is_distinct(this_1470) -> 'bool33':
        return this_1470.is_distinct_748
    @property
    def select_exprs(this_1473) -> 'Sequence29[SqlFragment]':
        return this_1473.select_exprs_749
class SafeIdentifier(metaclass = ABCMeta28):
    pass
class ValidatedIdentifier_216(SafeIdentifier):
    value_1116: 'str27'
    __slots__ = ('value_1116',)
    @property
    def sql_value(this_217) -> 'str27':
        return this_217.value_1116
    def __init__(this_384, value_1120: 'str27') -> None:
        this_384.value_1116 = value_1120
class FieldType(metaclass = ABCMeta28):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_390) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_392) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_394) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_396) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_398) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_400) -> None:
        pass
class FieldDef:
    name_1134: 'SafeIdentifier'
    field_type_1135: 'FieldType'
    nullable_1136: 'bool33'
    __slots__ = ('name_1134', 'field_type_1135', 'nullable_1136')
    def __init__(this_402, name_1138: 'SafeIdentifier', field_type_1139: 'FieldType', nullable_1140: 'bool33') -> None:
        this_402.name_1134 = name_1138
        this_402.field_type_1135 = field_type_1139
        this_402.nullable_1136 = nullable_1140
    @property
    def name(this_1366) -> 'SafeIdentifier':
        return this_1366.name_1134
    @property
    def field_type(this_1369) -> 'FieldType':
        return this_1369.field_type_1135
    @property
    def nullable(this_1372) -> 'bool33':
        return this_1372.nullable_1136
class TableDef:
    table_name_1141: 'SafeIdentifier'
    fields_1142: 'Sequence29[FieldDef]'
    __slots__ = ('table_name_1141', 'fields_1142')
    def field(this_218, name_1144: 'str27') -> 'FieldDef':
        return_407: 'FieldDef'
        with Label35() as fn_1145:
            this_5723: 'Sequence29[FieldDef]' = this_218.fields_1142
            n_5724: 'int31' = len_9686(this_5723)
            i_5725: 'int31' = 0
            while i_5725 < n_5724:
                el_5726: 'FieldDef' = list_get_9694(this_5723, i_5725)
                i_5725 = int_add_9695(i_5725, 1)
                f_1146: 'FieldDef' = el_5726
                if f_1146.name.sql_value == name_1144:
                    return_407 = f_1146
                    fn_1145.break_()
            raise RuntimeError30()
        return return_407
    def __init__(this_404, table_name_1148: 'SafeIdentifier', fields_1149: 'Sequence29[FieldDef]') -> None:
        this_404.table_name_1141 = table_name_1148
        this_404.fields_1142 = fields_1149
    @property
    def table_name(this_1375) -> 'SafeIdentifier':
        return this_1375.table_name_1141
    @property
    def fields(this_1378) -> 'Sequence29[FieldDef]':
        return this_1378.fields_1142
T_237 = TypeVar42('T_237', bound = Any41)
class SqlBuilder:
    buffer_1169: 'MutableSequence36[SqlPart]'
    __slots__ = ('buffer_1169',)
    def append_safe(this_219, sql_source_1171: 'str27') -> 'None':
        t_9641: 'SqlSource' = SqlSource(sql_source_1171)
        this_219.buffer_1169.append(t_9641)
    def append_fragment(this_220, fragment_1174: 'SqlFragment') -> 'None':
        t_9639: 'Sequence29[SqlPart]' = fragment_1174.parts
        list_builder_add_all_9698(this_220.buffer_1169, t_9639)
    def append_part(this_221, part_1177: 'SqlPart') -> 'None':
        this_221.buffer_1169.append(part_1177)
    def append_part_list(this_222, values_1180: 'Sequence29[SqlPart]') -> 'None':
        def fn_9635(x_1182: 'SqlPart') -> 'None':
            this_222.append_part(x_1182)
        this_222.append_list_1225(values_1180, fn_9635)
    def append_boolean(this_223, value_1184: 'bool33') -> 'None':
        t_9632: 'SqlBoolean' = SqlBoolean(value_1184)
        this_223.buffer_1169.append(t_9632)
    def append_boolean_list(this_224, values_1187: 'Sequence29[bool33]') -> 'None':
        def fn_9629(x_1189: 'bool33') -> 'None':
            this_224.append_boolean(x_1189)
        this_224.append_list_1225(values_1187, fn_9629)
    def append_date(this_225, value_1191: 'date26') -> 'None':
        t_9626: 'SqlDate' = SqlDate(value_1191)
        this_225.buffer_1169.append(t_9626)
    def append_date_list(this_226, values_1194: 'Sequence29[date26]') -> 'None':
        def fn_9623(x_1196: 'date26') -> 'None':
            this_226.append_date(x_1196)
        this_226.append_list_1225(values_1194, fn_9623)
    def append_float64(this_227, value_1198: 'float38') -> 'None':
        t_9620: 'SqlFloat64' = SqlFloat64(value_1198)
        this_227.buffer_1169.append(t_9620)
    def append_float64_list(this_228, values_1201: 'Sequence29[float38]') -> 'None':
        def fn_9617(x_1203: 'float38') -> 'None':
            this_228.append_float64(x_1203)
        this_228.append_list_1225(values_1201, fn_9617)
    def append_int32(this_229, value_1205: 'int31') -> 'None':
        t_9614: 'SqlInt32' = SqlInt32(value_1205)
        this_229.buffer_1169.append(t_9614)
    def append_int32_list(this_230, values_1208: 'Sequence29[int31]') -> 'None':
        def fn_9611(x_1210: 'int31') -> 'None':
            this_230.append_int32(x_1210)
        this_230.append_list_1225(values_1208, fn_9611)
    def append_int64(this_231, value_1212: 'int64_23') -> 'None':
        t_9608: 'SqlInt64' = SqlInt64(value_1212)
        this_231.buffer_1169.append(t_9608)
    def append_int64_list(this_232, values_1215: 'Sequence29[int64_23]') -> 'None':
        def fn_9605(x_1217: 'int64_23') -> 'None':
            this_232.append_int64(x_1217)
        this_232.append_list_1225(values_1215, fn_9605)
    def append_string(this_233, value_1219: 'str27') -> 'None':
        t_9602: 'SqlString' = SqlString(value_1219)
        this_233.buffer_1169.append(t_9602)
    def append_string_list(this_234, values_1222: 'Sequence29[str27]') -> 'None':
        def fn_9599(x_1224: 'str27') -> 'None':
            this_234.append_string(x_1224)
        this_234.append_list_1225(values_1222, fn_9599)
    def append_list_1225(this_235, values_1226: 'Sequence29[T_237]', append_value_1227: 'Callable43[[T_237], None]') -> 'None':
        t_9594: 'int31'
        t_9596: 'T_237'
        i_1229: 'int31' = 0
        while True:
            t_9594 = len_9686(values_1226)
            if not i_1229 < t_9594:
                break
            if i_1229 > 0:
                this_235.append_safe(', ')
            t_9596 = list_get_9694(values_1226, i_1229)
            append_value_1227(t_9596)
            i_1229 = int_add_9695(i_1229, 1)
    @property
    def accumulated(this_236) -> 'SqlFragment':
        return SqlFragment(tuple_9685(this_236.buffer_1169))
    def __init__(this_409) -> None:
        t_9591: 'MutableSequence36[SqlPart]' = list_9682()
        this_409.buffer_1169 = t_9591
class SqlFragment:
    parts_1236: 'Sequence29[SqlPart]'
    __slots__ = ('parts_1236',)
    def to_source(this_241) -> 'SqlSource':
        return SqlSource(this_241.to_string())
    def to_string(this_242) -> 'str27':
        t_9665: 'int31'
        builder_1241: 'list3[str27]' = ['']
        i_1242: 'int31' = 0
        while True:
            t_9665 = len_9686(this_242.parts_1236)
            if not i_1242 < t_9665:
                break
            list_get_9694(this_242.parts_1236, i_1242).format_to(builder_1241)
            i_1242 = int_add_9695(i_1242, 1)
        return ''.join(builder_1241)
    def __init__(this_430, parts_1244: 'Sequence29[SqlPart]') -> None:
        this_430.parts_1236 = parts_1244
    @property
    def parts(this_1384) -> 'Sequence29[SqlPart]':
        return this_1384.parts_1236
class SqlPart(metaclass = ABCMeta28):
    def format_to(this_243, builder_1246: 'list3[str27]') -> 'None':
        raise RuntimeError30()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_1248: 'str27'
    __slots__ = ('source_1248',)
    def format_to(this_244, builder_1250: 'list3[str27]') -> 'None':
        builder_1250.append(this_244.source_1248)
    def __init__(this_436, source_1253: 'str27') -> None:
        this_436.source_1248 = source_1253
    @property
    def source(this_1381) -> 'str27':
        return this_1381.source_1248
class SqlBoolean(SqlPart):
    value_1254: 'bool33'
    __slots__ = ('value_1254',)
    def format_to(this_245, builder_1256: 'list3[str27]') -> 'None':
        t_5535: 'str27'
        if this_245.value_1254:
            t_5535 = 'TRUE'
        else:
            t_5535 = 'FALSE'
        builder_1256.append(t_5535)
    def __init__(this_439, value_1259: 'bool33') -> None:
        this_439.value_1254 = value_1259
    @property
    def value(this_1387) -> 'bool33':
        return this_1387.value_1254
class SqlDate(SqlPart):
    value_1260: 'date26'
    __slots__ = ('value_1260',)
    def format_to(this_246, builder_1262: 'list3[str27]') -> 'None':
        builder_1262.append("'")
        t_9646: 'str27' = date_to_string_9702(this_246.value_1260)
        def fn_9644(c_1264: 'int31') -> 'None':
            if c_1264 == 39:
                builder_1262.append("''")
            else:
                builder_1262.append(string_from_code_point44(c_1264))
        string_for_each_9704(t_9646, fn_9644)
        builder_1262.append("'")
    def __init__(this_442, value_1266: 'date26') -> None:
        this_442.value_1260 = value_1266
    @property
    def value(this_1402) -> 'date26':
        return this_1402.value_1260
class SqlFloat64(SqlPart):
    value_1267: 'float38'
    __slots__ = ('value_1267',)
    def format_to(this_247, builder_1269: 'list3[str27]') -> 'None':
        t_5524: 'bool33'
        t_5525: 'bool33'
        s_1271: 'str27' = float64_to_string_9705(this_247.value_1267)
        if s_1271 == 'NaN':
            t_5525 = True
        else:
            if s_1271 == 'Infinity':
                t_5524 = True
            else:
                t_5524 = s_1271 == '-Infinity'
            t_5525 = t_5524
        if t_5525:
            builder_1269.append('NULL')
        else:
            builder_1269.append(s_1271)
    def __init__(this_445, value_1273: 'float38') -> None:
        this_445.value_1267 = value_1273
    @property
    def value(this_1399) -> 'float38':
        return this_1399.value_1267
class SqlInt32(SqlPart):
    value_1274: 'int31'
    __slots__ = ('value_1274',)
    def format_to(this_248, builder_1276: 'list3[str27]') -> 'None':
        t_9655: 'str27' = int_to_string_9689(this_248.value_1274)
        builder_1276.append(t_9655)
    def __init__(this_448, value_1279: 'int31') -> None:
        this_448.value_1274 = value_1279
    @property
    def value(this_1393) -> 'int31':
        return this_1393.value_1274
class SqlInt64(SqlPart):
    value_1280: 'int64_23'
    __slots__ = ('value_1280',)
    def format_to(this_249, builder_1282: 'list3[str27]') -> 'None':
        t_9653: 'str27' = int_to_string_9689(this_249.value_1280)
        builder_1282.append(t_9653)
    def __init__(this_451, value_1285: 'int64_23') -> None:
        this_451.value_1280 = value_1285
    @property
    def value(this_1396) -> 'int64_23':
        return this_1396.value_1280
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_1286: 'str27'
    __slots__ = ('value_1286',)
    def format_to(this_250, builder_1288: 'list3[str27]') -> 'None':
        builder_1288.append("'")
        def fn_9658(c_1290: 'int31') -> 'None':
            if c_1290 == 39:
                builder_1288.append("''")
            else:
                builder_1288.append(string_from_code_point44(c_1290))
        string_for_each_9704(this_250.value_1286, fn_9658)
        builder_1288.append("'")
    def __init__(this_454, value_1292: 'str27') -> None:
        this_454.value_1286 = value_1292
    @property
    def value(this_1390) -> 'str27':
        return this_1390.value_1286
def changeset(table_def_601: 'TableDef', params_602: 'MappingProxyType32[str27, str27]') -> 'Changeset':
    t_9441: 'MappingProxyType32[str27, str27]' = map_constructor_9706(())
    return ChangesetImpl_161(table_def_601, params_602, t_9441, (), True)
def is_ident_start_462(c_1121: 'int31') -> 'bool33':
    return_387: 'bool33'
    t_5298: 'bool33'
    t_5299: 'bool33'
    if c_1121 >= 97:
        t_5298 = c_1121 <= 122
    else:
        t_5298 = False
    if t_5298:
        return_387 = True
    else:
        if c_1121 >= 65:
            t_5299 = c_1121 <= 90
        else:
            t_5299 = False
        if t_5299:
            return_387 = True
        else:
            return_387 = c_1121 == 95
    return return_387
def is_ident_part_463(c_1123: 'int31') -> 'bool33':
    return_388: 'bool33'
    if is_ident_start_462(c_1123):
        return_388 = True
    elif c_1123 >= 48:
        return_388 = c_1123 <= 57
    else:
        return_388 = False
    return return_388
def safe_identifier(name_1125: 'str27') -> 'SafeIdentifier':
    t_9439: 'int31'
    if not name_1125:
        raise RuntimeError30()
    idx_1127: 'int31' = 0
    if not is_ident_start_462(string_get_9707(name_1125, idx_1127)):
        raise RuntimeError30()
    t_9436: 'int31' = string_next_9708(name_1125, idx_1127)
    idx_1127 = t_9436
    while True:
        if not len6(name_1125) > idx_1127:
            break
        if not is_ident_part_463(string_get_9707(name_1125, idx_1127)):
            raise RuntimeError30()
        t_9439 = string_next_9708(name_1125, idx_1127)
        idx_1127 = t_9439
    return ValidatedIdentifier_216(name_1125)
def delete_sql(table_def_691: 'TableDef', id_692: 'int31') -> 'SqlFragment':
    b_694: 'SqlBuilder' = SqlBuilder()
    b_694.append_safe('DELETE FROM ')
    b_694.append_safe(table_def_691.table_name.sql_value)
    b_694.append_safe(' WHERE id = ')
    b_694.append_int32(id_692)
    return b_694.accumulated
def from_(table_name_886: 'SafeIdentifier') -> 'Query':
    return Query(table_name_886, (), (), (), None, None, (), (), (), False, ())
def col(table_888: 'SafeIdentifier', column_889: 'SafeIdentifier') -> 'SqlFragment':
    b_891: 'SqlBuilder' = SqlBuilder()
    b_891.append_safe(table_888.sql_value)
    b_891.append_safe('.')
    b_891.append_safe(column_889.sql_value)
    return b_891.accumulated
def count_all() -> 'SqlFragment':
    b_893: 'SqlBuilder' = SqlBuilder()
    b_893.append_safe('COUNT(*)')
    return b_893.accumulated
def count_col(field_894: 'SafeIdentifier') -> 'SqlFragment':
    b_896: 'SqlBuilder' = SqlBuilder()
    b_896.append_safe('COUNT(')
    b_896.append_safe(field_894.sql_value)
    b_896.append_safe(')')
    return b_896.accumulated
def sum_col(field_897: 'SafeIdentifier') -> 'SqlFragment':
    b_899: 'SqlBuilder' = SqlBuilder()
    b_899.append_safe('SUM(')
    b_899.append_safe(field_897.sql_value)
    b_899.append_safe(')')
    return b_899.accumulated
def avg_col(field_900: 'SafeIdentifier') -> 'SqlFragment':
    b_902: 'SqlBuilder' = SqlBuilder()
    b_902.append_safe('AVG(')
    b_902.append_safe(field_900.sql_value)
    b_902.append_safe(')')
    return b_902.accumulated
def min_col(field_903: 'SafeIdentifier') -> 'SqlFragment':
    b_905: 'SqlBuilder' = SqlBuilder()
    b_905.append_safe('MIN(')
    b_905.append_safe(field_903.sql_value)
    b_905.append_safe(')')
    return b_905.accumulated
def max_col(field_906: 'SafeIdentifier') -> 'SqlFragment':
    b_908: 'SqlBuilder' = SqlBuilder()
    b_908.append_safe('MAX(')
    b_908.append_safe(field_906.sql_value)
    b_908.append_safe(')')
    return b_908.accumulated
def union_sql(a_909: 'Query', b_910: 'Query') -> 'SqlFragment':
    sb_912: 'SqlBuilder' = SqlBuilder()
    sb_912.append_safe('(')
    sb_912.append_fragment(a_909.to_sql())
    sb_912.append_safe(') UNION (')
    sb_912.append_fragment(b_910.to_sql())
    sb_912.append_safe(')')
    return sb_912.accumulated
def union_all_sql(a_913: 'Query', b_914: 'Query') -> 'SqlFragment':
    sb_916: 'SqlBuilder' = SqlBuilder()
    sb_916.append_safe('(')
    sb_916.append_fragment(a_913.to_sql())
    sb_916.append_safe(') UNION ALL (')
    sb_916.append_fragment(b_914.to_sql())
    sb_916.append_safe(')')
    return sb_916.accumulated
def intersect_sql(a_917: 'Query', b_918: 'Query') -> 'SqlFragment':
    sb_920: 'SqlBuilder' = SqlBuilder()
    sb_920.append_safe('(')
    sb_920.append_fragment(a_917.to_sql())
    sb_920.append_safe(') INTERSECT (')
    sb_920.append_fragment(b_918.to_sql())
    sb_920.append_safe(')')
    return sb_920.accumulated
def except_sql(a_921: 'Query', b_922: 'Query') -> 'SqlFragment':
    sb_924: 'SqlBuilder' = SqlBuilder()
    sb_924.append_safe('(')
    sb_924.append_fragment(a_921.to_sql())
    sb_924.append_safe(') EXCEPT (')
    sb_924.append_fragment(b_922.to_sql())
    sb_924.append_safe(')')
    return sb_924.accumulated
def subquery(q_925: 'Query', alias_926: 'SafeIdentifier') -> 'SqlFragment':
    b_928: 'SqlBuilder' = SqlBuilder()
    b_928.append_safe('(')
    b_928.append_fragment(q_925.to_sql())
    b_928.append_safe(') AS ')
    b_928.append_safe(alias_926.sql_value)
    return b_928.accumulated
def exists_sql(q_929: 'Query') -> 'SqlFragment':
    b_931: 'SqlBuilder' = SqlBuilder()
    b_931.append_safe('EXISTS (')
    b_931.append_fragment(q_929.to_sql())
    b_931.append_safe(')')
    return b_931.accumulated
