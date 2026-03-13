from builtins import str as str27, RuntimeError as RuntimeError30, int as int31, bool as bool33, Exception as Exception37, float as float38, isinstance as isinstance39, list as list3, len as len6, tuple as tuple5
from abc import ABCMeta as ABCMeta28
from typing import Sequence as Sequence29, Dict as Dict34, MutableSequence as MutableSequence36, Union as Union40, Any as Any41, TypeVar as TypeVar42, Callable as Callable43
from types import MappingProxyType as MappingProxyType32
from temper_core import Label as Label35, Pair as Pair25, string_from_code_point as string_from_code_point44, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, date_from_iso_string as date_from_iso_string13, list_get as list_get14, int_add as int_add15, mapped_to_list as mapped_to_list16, list_join as list_join17, list_builder_add_all as list_builder_add_all18, date_to_string as date_to_string19, string_for_each as string_for_each20, float64_to_string as float64_to_string21, map_constructor as map_constructor22, string_get as string_get23, string_next as string_next24
from datetime import date as date26
map_builder_set_8805 = map_builder_set0
list_for_each_8806 = list_for_each1
mapped_to_map_8807 = mapped_to_map2
list_8808 = list3
mapped_has_8809 = mapped_has4
tuple_8811 = tuple5
len_8812 = len6
string_count_between_8813 = string_count_between7
str_cat_8814 = str_cat8
int_to_string_8815 = int_to_string9
string_to_int32_8816 = string_to_int3210
string_to_int64_8817 = string_to_int6411
string_to_float64_8818 = string_to_float6412
date_from_iso_string_8819 = date_from_iso_string13
list_get_8820 = list_get14
int_add_8821 = int_add15
mapped_to_list_8822 = mapped_to_list16
list_join_8823 = list_join17
list_builder_add_all_8824 = list_builder_add_all18
date_to_string_8828 = date_to_string19
string_for_each_8830 = string_for_each20
float64_to_string_8831 = float64_to_string21
map_constructor_8832 = map_constructor22
string_get_8833 = string_get23
string_next_8834 = string_next24
pair_8836 = Pair25
date_8839 = date26
class ChangesetError:
    field_448: 'str27'
    message_449: 'str27'
    __slots__ = ('field_448', 'message_449')
    def __init__(this_240, field_451: 'str27', message_452: 'str27') -> None:
        this_240.field_448 = field_451
        this_240.message_449 = message_452
    @property
    def field(this_1276) -> 'str27':
        return this_1276.field_448
    @property
    def message(this_1279) -> 'str27':
        return this_1279.message_449
class Changeset(metaclass = ABCMeta28):
    def cast(this_142, allowed_fields_462: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_required(this_143, fields_465: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_length(this_144, field_468: 'SafeIdentifier', min_469: 'int31', max_470: 'int31') -> 'Changeset':
        raise RuntimeError30()
    def validate_int(this_145, field_473: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_int64(this_146, field_476: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_float(this_147, field_479: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_bool(this_148, field_482: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def to_insert_sql(this_149) -> 'SqlFragment':
        raise RuntimeError30()
    def to_update_sql(this_150, id_487: 'int31') -> 'SqlFragment':
        raise RuntimeError30()
class ChangesetImpl_151(Changeset):
    table_def_489: 'TableDef'
    params_490: 'MappingProxyType32[str27, str27]'
    changes_491: 'MappingProxyType32[str27, str27]'
    errors_492: 'Sequence29[ChangesetError]'
    is_valid_493: 'bool33'
    __slots__ = ('table_def_489', 'params_490', 'changes_491', 'errors_492', 'is_valid_493')
    @property
    def table_def(this_152) -> 'TableDef':
        return this_152.table_def_489
    @property
    def changes(this_153) -> 'MappingProxyType32[str27, str27]':
        return this_153.changes_491
    @property
    def errors(this_154) -> 'Sequence29[ChangesetError]':
        return this_154.errors_492
    @property
    def is_valid(this_155) -> 'bool33':
        return this_155.is_valid_493
    def cast(this_156, allowed_fields_503: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        mb_505: 'Dict34[str27, str27]' = {}
        def fn_8709(f_506: 'SafeIdentifier') -> 'None':
            t_8707: 'str27'
            t_8704: 'str27' = f_506.sql_value
            val_507: 'str27' = this_156.params_490.get(t_8704, '')
            if not (not val_507):
                t_8707 = f_506.sql_value
                map_builder_set_8805(mb_505, t_8707, val_507)
        list_for_each_8806(allowed_fields_503, fn_8709)
        return ChangesetImpl_151(this_156.table_def_489, this_156.params_490, mapped_to_map_8807(mb_505), this_156.errors_492, this_156.is_valid_493)
    def validate_required(this_157, fields_509: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        return_273: 'Changeset'
        t_8702: 'Sequence29[ChangesetError]'
        t_5006: 'TableDef'
        t_5007: 'MappingProxyType32[str27, str27]'
        t_5008: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_510:
            if not this_157.is_valid_493:
                return_273 = this_157
                fn_510.break_()
            eb_511: 'MutableSequence36[ChangesetError]' = list_8808(this_157.errors_492)
            valid_512: 'bool33' = True
            def fn_8698(f_513: 'SafeIdentifier') -> 'None':
                nonlocal valid_512
                t_8696: 'ChangesetError'
                t_8693: 'str27' = f_513.sql_value
                if not mapped_has_8809(this_157.changes_491, t_8693):
                    t_8696 = ChangesetError(f_513.sql_value, 'is required')
                    eb_511.append(t_8696)
                    valid_512 = False
            list_for_each_8806(fields_509, fn_8698)
            t_5006 = this_157.table_def_489
            t_5007 = this_157.params_490
            t_5008 = this_157.changes_491
            t_8702 = tuple_8811(eb_511)
            return_273 = ChangesetImpl_151(t_5006, t_5007, t_5008, t_8702, valid_512)
        return return_273
    def validate_length(this_158, field_515: 'SafeIdentifier', min_516: 'int31', max_517: 'int31') -> 'Changeset':
        return_274: 'Changeset'
        t_8680: 'str27'
        t_8691: 'Sequence29[ChangesetError]'
        t_4989: 'bool33'
        t_4995: 'TableDef'
        t_4996: 'MappingProxyType32[str27, str27]'
        t_4997: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_518:
            if not this_158.is_valid_493:
                return_274 = this_158
                fn_518.break_()
            t_8680 = field_515.sql_value
            val_519: 'str27' = this_158.changes_491.get(t_8680, '')
            len_520: 'int31' = string_count_between_8813(val_519, 0, len_8812(val_519))
            if len_520 < min_516:
                t_4989 = True
            else:
                t_4989 = len_520 > max_517
            if t_4989:
                msg_521: 'str27' = str_cat_8814('must be between ', int_to_string_8815(min_516), ' and ', int_to_string_8815(max_517), ' characters')
                eb_522: 'MutableSequence36[ChangesetError]' = list_8808(this_158.errors_492)
                eb_522.append(ChangesetError(field_515.sql_value, msg_521))
                t_4995 = this_158.table_def_489
                t_4996 = this_158.params_490
                t_4997 = this_158.changes_491
                t_8691 = tuple_8811(eb_522)
                return_274 = ChangesetImpl_151(t_4995, t_4996, t_4997, t_8691, False)
                fn_518.break_()
            return_274 = this_158
        return return_274
    def validate_int(this_159, field_524: 'SafeIdentifier') -> 'Changeset':
        return_275: 'Changeset'
        t_8671: 'str27'
        t_8678: 'Sequence29[ChangesetError]'
        t_4980: 'TableDef'
        t_4981: 'MappingProxyType32[str27, str27]'
        t_4982: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_525:
            if not this_159.is_valid_493:
                return_275 = this_159
                fn_525.break_()
            t_8671 = field_524.sql_value
            val_526: 'str27' = this_159.changes_491.get(t_8671, '')
            if not val_526:
                return_275 = this_159
                fn_525.break_()
            parse_ok_527: 'bool33'
            try:
                string_to_int32_8816(val_526)
                parse_ok_527 = True
            except Exception37:
                parse_ok_527 = False
            if not parse_ok_527:
                eb_528: 'MutableSequence36[ChangesetError]' = list_8808(this_159.errors_492)
                eb_528.append(ChangesetError(field_524.sql_value, 'must be an integer'))
                t_4980 = this_159.table_def_489
                t_4981 = this_159.params_490
                t_4982 = this_159.changes_491
                t_8678 = tuple_8811(eb_528)
                return_275 = ChangesetImpl_151(t_4980, t_4981, t_4982, t_8678, False)
                fn_525.break_()
            return_275 = this_159
        return return_275
    def validate_int64(this_160, field_530: 'SafeIdentifier') -> 'Changeset':
        return_276: 'Changeset'
        t_8662: 'str27'
        t_8669: 'Sequence29[ChangesetError]'
        t_4967: 'TableDef'
        t_4968: 'MappingProxyType32[str27, str27]'
        t_4969: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_531:
            if not this_160.is_valid_493:
                return_276 = this_160
                fn_531.break_()
            t_8662 = field_530.sql_value
            val_532: 'str27' = this_160.changes_491.get(t_8662, '')
            if not val_532:
                return_276 = this_160
                fn_531.break_()
            parse_ok_533: 'bool33'
            try:
                string_to_int64_8817(val_532)
                parse_ok_533 = True
            except Exception37:
                parse_ok_533 = False
            if not parse_ok_533:
                eb_534: 'MutableSequence36[ChangesetError]' = list_8808(this_160.errors_492)
                eb_534.append(ChangesetError(field_530.sql_value, 'must be a 64-bit integer'))
                t_4967 = this_160.table_def_489
                t_4968 = this_160.params_490
                t_4969 = this_160.changes_491
                t_8669 = tuple_8811(eb_534)
                return_276 = ChangesetImpl_151(t_4967, t_4968, t_4969, t_8669, False)
                fn_531.break_()
            return_276 = this_160
        return return_276
    def validate_float(this_161, field_536: 'SafeIdentifier') -> 'Changeset':
        return_277: 'Changeset'
        t_8653: 'str27'
        t_8660: 'Sequence29[ChangesetError]'
        t_4954: 'TableDef'
        t_4955: 'MappingProxyType32[str27, str27]'
        t_4956: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_537:
            if not this_161.is_valid_493:
                return_277 = this_161
                fn_537.break_()
            t_8653 = field_536.sql_value
            val_538: 'str27' = this_161.changes_491.get(t_8653, '')
            if not val_538:
                return_277 = this_161
                fn_537.break_()
            parse_ok_539: 'bool33'
            try:
                string_to_float64_8818(val_538)
                parse_ok_539 = True
            except Exception37:
                parse_ok_539 = False
            if not parse_ok_539:
                eb_540: 'MutableSequence36[ChangesetError]' = list_8808(this_161.errors_492)
                eb_540.append(ChangesetError(field_536.sql_value, 'must be a number'))
                t_4954 = this_161.table_def_489
                t_4955 = this_161.params_490
                t_4956 = this_161.changes_491
                t_8660 = tuple_8811(eb_540)
                return_277 = ChangesetImpl_151(t_4954, t_4955, t_4956, t_8660, False)
                fn_537.break_()
            return_277 = this_161
        return return_277
    def validate_bool(this_162, field_542: 'SafeIdentifier') -> 'Changeset':
        return_278: 'Changeset'
        t_8644: 'str27'
        t_8651: 'Sequence29[ChangesetError]'
        t_4929: 'bool33'
        t_4930: 'bool33'
        t_4932: 'bool33'
        t_4933: 'bool33'
        t_4935: 'bool33'
        t_4941: 'TableDef'
        t_4942: 'MappingProxyType32[str27, str27]'
        t_4943: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_543:
            if not this_162.is_valid_493:
                return_278 = this_162
                fn_543.break_()
            t_8644 = field_542.sql_value
            val_544: 'str27' = this_162.changes_491.get(t_8644, '')
            if not val_544:
                return_278 = this_162
                fn_543.break_()
            is_true_545: 'bool33'
            if val_544 == 'true':
                is_true_545 = True
            else:
                if val_544 == '1':
                    t_4930 = True
                else:
                    if val_544 == 'yes':
                        t_4929 = True
                    else:
                        t_4929 = val_544 == 'on'
                    t_4930 = t_4929
                is_true_545 = t_4930
            is_false_546: 'bool33'
            if val_544 == 'false':
                is_false_546 = True
            else:
                if val_544 == '0':
                    t_4933 = True
                else:
                    if val_544 == 'no':
                        t_4932 = True
                    else:
                        t_4932 = val_544 == 'off'
                    t_4933 = t_4932
                is_false_546 = t_4933
            if not is_true_545:
                t_4935 = not is_false_546
            else:
                t_4935 = False
            if t_4935:
                eb_547: 'MutableSequence36[ChangesetError]' = list_8808(this_162.errors_492)
                eb_547.append(ChangesetError(field_542.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_4941 = this_162.table_def_489
                t_4942 = this_162.params_490
                t_4943 = this_162.changes_491
                t_8651 = tuple_8811(eb_547)
                return_278 = ChangesetImpl_151(t_4941, t_4942, t_4943, t_8651, False)
                fn_543.break_()
            return_278 = this_162
        return return_278
    def parse_bool_sql_part_548(this_163, val_549: 'str27') -> 'SqlBoolean':
        return_279: 'SqlBoolean'
        t_4918: 'bool33'
        t_4919: 'bool33'
        t_4920: 'bool33'
        t_4922: 'bool33'
        t_4923: 'bool33'
        t_4924: 'bool33'
        with Label35() as fn_550:
            if val_549 == 'true':
                t_4920 = True
            else:
                if val_549 == '1':
                    t_4919 = True
                else:
                    if val_549 == 'yes':
                        t_4918 = True
                    else:
                        t_4918 = val_549 == 'on'
                    t_4919 = t_4918
                t_4920 = t_4919
            if t_4920:
                return_279 = SqlBoolean(True)
                fn_550.break_()
            if val_549 == 'false':
                t_4924 = True
            else:
                if val_549 == '0':
                    t_4923 = True
                else:
                    if val_549 == 'no':
                        t_4922 = True
                    else:
                        t_4922 = val_549 == 'off'
                    t_4923 = t_4922
                t_4924 = t_4923
            if t_4924:
                return_279 = SqlBoolean(False)
                fn_550.break_()
            raise RuntimeError30()
        return return_279
    def value_to_sql_part_551(this_164, field_def_552: 'FieldDef', val_553: 'str27') -> 'SqlPart':
        return_280: 'SqlPart'
        t_4905: 'int31'
        t_4908: 'int64_23'
        t_4911: 'float38'
        t_4916: 'date26'
        with Label35() as fn_554:
            ft_555: 'FieldType' = field_def_552.field_type
            if isinstance39(ft_555, StringField):
                return_280 = SqlString(val_553)
                fn_554.break_()
            if isinstance39(ft_555, IntField):
                t_4905 = string_to_int32_8816(val_553)
                return_280 = SqlInt32(t_4905)
                fn_554.break_()
            if isinstance39(ft_555, Int64Field):
                t_4908 = string_to_int64_8817(val_553)
                return_280 = SqlInt64(t_4908)
                fn_554.break_()
            if isinstance39(ft_555, FloatField):
                t_4911 = string_to_float64_8818(val_553)
                return_280 = SqlFloat64(t_4911)
                fn_554.break_()
            if isinstance39(ft_555, BoolField):
                return_280 = this_164.parse_bool_sql_part_548(val_553)
                fn_554.break_()
            if isinstance39(ft_555, DateField):
                t_4916 = date_from_iso_string_8819(val_553)
                return_280 = SqlDate(t_4916)
                fn_554.break_()
            raise RuntimeError30()
        return return_280
    def to_insert_sql(this_165) -> 'SqlFragment':
        t_8592: 'int31'
        t_8597: 'str27'
        t_8598: 'bool33'
        t_8603: 'int31'
        t_8605: 'str27'
        t_8609: 'str27'
        t_8624: 'int31'
        t_4869: 'bool33'
        t_4877: 'FieldDef'
        t_4882: 'SqlPart'
        if not this_165.is_valid_493:
            raise RuntimeError30()
        i_558: 'int31' = 0
        while True:
            t_8592 = len_8812(this_165.table_def_489.fields)
            if not i_558 < t_8592:
                break
            f_559: 'FieldDef' = list_get_8820(this_165.table_def_489.fields, i_558)
            if not f_559.nullable:
                t_8597 = f_559.name.sql_value
                t_8598 = mapped_has_8809(this_165.changes_491, t_8597)
                t_4869 = not t_8598
            else:
                t_4869 = False
            if t_4869:
                raise RuntimeError30()
            i_558 = int_add_8821(i_558, 1)
        pairs_560: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_8822(this_165.changes_491)
        if len_8812(pairs_560) == 0:
            raise RuntimeError30()
        col_names_561: 'MutableSequence36[str27]' = list_8808()
        val_parts_562: 'MutableSequence36[SqlPart]' = list_8808()
        i_563: 'int31' = 0
        while True:
            t_8603 = len_8812(pairs_560)
            if not i_563 < t_8603:
                break
            pair_564: 'Pair25[str27, str27]' = list_get_8820(pairs_560, i_563)
            t_8605 = pair_564.key
            t_4877 = this_165.table_def_489.field(t_8605)
            fd_565: 'FieldDef' = t_4877
            col_names_561.append(fd_565.name.sql_value)
            t_8609 = pair_564.value
            t_4882 = this_165.value_to_sql_part_551(fd_565, t_8609)
            val_parts_562.append(t_4882)
            i_563 = int_add_8821(i_563, 1)
        b_566: 'SqlBuilder' = SqlBuilder()
        b_566.append_safe('INSERT INTO ')
        b_566.append_safe(this_165.table_def_489.table_name.sql_value)
        b_566.append_safe(' (')
        t_8617: 'Sequence29[str27]' = tuple_8811(col_names_561)
        def fn_8590(c_567: 'str27') -> 'str27':
            return c_567
        b_566.append_safe(list_join_8823(t_8617, ', ', fn_8590))
        b_566.append_safe(') VALUES (')
        b_566.append_part(list_get_8820(val_parts_562, 0))
        j_568: 'int31' = 1
        while True:
            t_8624 = len_8812(val_parts_562)
            if not j_568 < t_8624:
                break
            b_566.append_safe(', ')
            b_566.append_part(list_get_8820(val_parts_562, j_568))
            j_568 = int_add_8821(j_568, 1)
        b_566.append_safe(')')
        return b_566.accumulated
    def to_update_sql(this_166, id_570: 'int31') -> 'SqlFragment':
        t_8577: 'int31'
        t_8580: 'str27'
        t_8585: 'str27'
        t_4850: 'FieldDef'
        t_4856: 'SqlPart'
        if not this_166.is_valid_493:
            raise RuntimeError30()
        pairs_572: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_8822(this_166.changes_491)
        if len_8812(pairs_572) == 0:
            raise RuntimeError30()
        b_573: 'SqlBuilder' = SqlBuilder()
        b_573.append_safe('UPDATE ')
        b_573.append_safe(this_166.table_def_489.table_name.sql_value)
        b_573.append_safe(' SET ')
        i_574: 'int31' = 0
        while True:
            t_8577 = len_8812(pairs_572)
            if not i_574 < t_8577:
                break
            if i_574 > 0:
                b_573.append_safe(', ')
            pair_575: 'Pair25[str27, str27]' = list_get_8820(pairs_572, i_574)
            t_8580 = pair_575.key
            t_4850 = this_166.table_def_489.field(t_8580)
            fd_576: 'FieldDef' = t_4850
            b_573.append_safe(fd_576.name.sql_value)
            b_573.append_safe(' = ')
            t_8585 = pair_575.value
            t_4856 = this_166.value_to_sql_part_551(fd_576, t_8585)
            b_573.append_part(t_4856)
            i_574 = int_add_8821(i_574, 1)
        b_573.append_safe(' WHERE id = ')
        b_573.append_int32(id_570)
        return b_573.accumulated
    def __init__(this_263, table_def_578: 'TableDef', params_579: 'MappingProxyType32[str27, str27]', changes_580: 'MappingProxyType32[str27, str27]', errors_581: 'Sequence29[ChangesetError]', is_valid_582: 'bool33') -> None:
        this_263.table_def_489 = table_def_578
        this_263.params_490 = params_579
        this_263.changes_491 = changes_580
        this_263.errors_492 = errors_581
        this_263.is_valid_493 = is_valid_582
class JoinType(metaclass = ABCMeta28):
    def keyword(this_167) -> 'str27':
        raise RuntimeError30()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_168) -> 'str27':
        return 'INNER JOIN'
    def __init__(this_288) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_169) -> 'str27':
        return 'LEFT JOIN'
    def __init__(this_291) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_170) -> 'str27':
        return 'RIGHT JOIN'
    def __init__(this_294) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_171) -> 'str27':
        return 'FULL OUTER JOIN'
    def __init__(this_297) -> None:
        pass
class JoinClause:
    join_type_691: 'JoinType'
    table_692: 'SafeIdentifier'
    on_condition_693: 'SqlFragment'
    __slots__ = ('join_type_691', 'table_692', 'on_condition_693')
    def __init__(this_300, join_type_695: 'JoinType', table_696: 'SafeIdentifier', on_condition_697: 'SqlFragment') -> None:
        this_300.join_type_691 = join_type_695
        this_300.table_692 = table_696
        this_300.on_condition_693 = on_condition_697
    @property
    def join_type(this_1344) -> 'JoinType':
        return this_1344.join_type_691
    @property
    def table(this_1347) -> 'SafeIdentifier':
        return this_1347.table_692
    @property
    def on_condition(this_1350) -> 'SqlFragment':
        return this_1350.on_condition_693
class OrderClause:
    field_698: 'SafeIdentifier'
    ascending_699: 'bool33'
    __slots__ = ('field_698', 'ascending_699')
    def __init__(this_302, field_701: 'SafeIdentifier', ascending_702: 'bool33') -> None:
        this_302.field_698 = field_701
        this_302.ascending_699 = ascending_702
    @property
    def field(this_1353) -> 'SafeIdentifier':
        return this_1353.field_698
    @property
    def ascending(this_1356) -> 'bool33':
        return this_1356.ascending_699
class WhereClause(metaclass = ABCMeta28):
    def keyword(this_173) -> 'str27':
        raise RuntimeError30()
class AndCondition(WhereClause):
    condition_707: 'SqlFragment'
    __slots__ = ('condition_707',)
    @property
    def condition(this_174) -> 'SqlFragment':
        return this_174.condition_707
    def keyword(this_175) -> 'str27':
        return 'AND'
    def __init__(this_308, condition_713: 'SqlFragment') -> None:
        this_308.condition_707 = condition_713
class OrCondition(WhereClause):
    condition_714: 'SqlFragment'
    __slots__ = ('condition_714',)
    @property
    def condition(this_176) -> 'SqlFragment':
        return this_176.condition_714
    def keyword(this_177) -> 'str27':
        return 'OR'
    def __init__(this_313, condition_720: 'SqlFragment') -> None:
        this_313.condition_714 = condition_720
class Query:
    table_name_721: 'SafeIdentifier'
    conditions_722: 'Sequence29[WhereClause]'
    selected_fields_723: 'Sequence29[SafeIdentifier]'
    order_clauses_724: 'Sequence29[OrderClause]'
    limit_val_725: 'Union40[int31, None]'
    offset_val_726: 'Union40[int31, None]'
    join_clauses_727: 'Sequence29[JoinClause]'
    group_by_fields_728: 'Sequence29[SafeIdentifier]'
    having_conditions_729: 'Sequence29[WhereClause]'
    is_distinct_730: 'bool33'
    select_exprs_731: 'Sequence29[SqlFragment]'
    __slots__ = ('table_name_721', 'conditions_722', 'selected_fields_723', 'order_clauses_724', 'limit_val_725', 'offset_val_726', 'join_clauses_727', 'group_by_fields_728', 'having_conditions_729', 'is_distinct_730', 'select_exprs_731')
    def where(this_178, condition_733: 'SqlFragment') -> 'Query':
        nb_735: 'MutableSequence36[WhereClause]' = list_8808(this_178.conditions_722)
        nb_735.append(AndCondition(condition_733))
        return Query(this_178.table_name_721, tuple_8811(nb_735), this_178.selected_fields_723, this_178.order_clauses_724, this_178.limit_val_725, this_178.offset_val_726, this_178.join_clauses_727, this_178.group_by_fields_728, this_178.having_conditions_729, this_178.is_distinct_730, this_178.select_exprs_731)
    def or_where(this_179, condition_737: 'SqlFragment') -> 'Query':
        nb_739: 'MutableSequence36[WhereClause]' = list_8808(this_179.conditions_722)
        nb_739.append(OrCondition(condition_737))
        return Query(this_179.table_name_721, tuple_8811(nb_739), this_179.selected_fields_723, this_179.order_clauses_724, this_179.limit_val_725, this_179.offset_val_726, this_179.join_clauses_727, this_179.group_by_fields_728, this_179.having_conditions_729, this_179.is_distinct_730, this_179.select_exprs_731)
    def where_null(this_180, field_741: 'SafeIdentifier') -> 'Query':
        b_743: 'SqlBuilder' = SqlBuilder()
        b_743.append_safe(field_741.sql_value)
        b_743.append_safe(' IS NULL')
        t_8176: 'SqlFragment' = b_743.accumulated
        return this_180.where(t_8176)
    def where_not_null(this_181, field_745: 'SafeIdentifier') -> 'Query':
        b_747: 'SqlBuilder' = SqlBuilder()
        b_747.append_safe(field_745.sql_value)
        b_747.append_safe(' IS NOT NULL')
        t_8170: 'SqlFragment' = b_747.accumulated
        return this_181.where(t_8170)
    def where_in(this_182, field_749: 'SafeIdentifier', values_750: 'Sequence29[SqlPart]') -> 'Query':
        return_332: 'Query'
        t_8151: 'SqlFragment'
        t_8159: 'int31'
        t_8164: 'SqlFragment'
        with Label35() as fn_751:
            if not values_750:
                b_752: 'SqlBuilder' = SqlBuilder()
                b_752.append_safe('1 = 0')
                t_8151 = b_752.accumulated
                return_332 = this_182.where(t_8151)
                fn_751.break_()
            b_753: 'SqlBuilder' = SqlBuilder()
            b_753.append_safe(field_749.sql_value)
            b_753.append_safe(' IN (')
            b_753.append_part(list_get_8820(values_750, 0))
            i_754: 'int31' = 1
            while True:
                t_8159 = len_8812(values_750)
                if not i_754 < t_8159:
                    break
                b_753.append_safe(', ')
                b_753.append_part(list_get_8820(values_750, i_754))
                i_754 = int_add_8821(i_754, 1)
            b_753.append_safe(')')
            t_8164 = b_753.accumulated
            return_332 = this_182.where(t_8164)
        return return_332
    def where_not(this_183, condition_756: 'SqlFragment') -> 'Query':
        b_758: 'SqlBuilder' = SqlBuilder()
        b_758.append_safe('NOT (')
        b_758.append_fragment(condition_756)
        b_758.append_safe(')')
        t_8146: 'SqlFragment' = b_758.accumulated
        return this_183.where(t_8146)
    def where_between(this_184, field_760: 'SafeIdentifier', low_761: 'SqlPart', high_762: 'SqlPart') -> 'Query':
        b_764: 'SqlBuilder' = SqlBuilder()
        b_764.append_safe(field_760.sql_value)
        b_764.append_safe(' BETWEEN ')
        b_764.append_part(low_761)
        b_764.append_safe(' AND ')
        b_764.append_part(high_762)
        t_8140: 'SqlFragment' = b_764.accumulated
        return this_184.where(t_8140)
    def where_like(this_185, field_766: 'SafeIdentifier', pattern_767: 'str27') -> 'Query':
        b_769: 'SqlBuilder' = SqlBuilder()
        b_769.append_safe(field_766.sql_value)
        b_769.append_safe(' LIKE ')
        b_769.append_string(pattern_767)
        t_8131: 'SqlFragment' = b_769.accumulated
        return this_185.where(t_8131)
    def where_i_like(this_186, field_771: 'SafeIdentifier', pattern_772: 'str27') -> 'Query':
        b_774: 'SqlBuilder' = SqlBuilder()
        b_774.append_safe(field_771.sql_value)
        b_774.append_safe(' ILIKE ')
        b_774.append_string(pattern_772)
        t_8124: 'SqlFragment' = b_774.accumulated
        return this_186.where(t_8124)
    def select(this_187, fields_776: 'Sequence29[SafeIdentifier]') -> 'Query':
        return Query(this_187.table_name_721, this_187.conditions_722, fields_776, this_187.order_clauses_724, this_187.limit_val_725, this_187.offset_val_726, this_187.join_clauses_727, this_187.group_by_fields_728, this_187.having_conditions_729, this_187.is_distinct_730, this_187.select_exprs_731)
    def select_expr(this_188, exprs_779: 'Sequence29[SqlFragment]') -> 'Query':
        return Query(this_188.table_name_721, this_188.conditions_722, this_188.selected_fields_723, this_188.order_clauses_724, this_188.limit_val_725, this_188.offset_val_726, this_188.join_clauses_727, this_188.group_by_fields_728, this_188.having_conditions_729, this_188.is_distinct_730, exprs_779)
    def order_by(this_189, field_782: 'SafeIdentifier', ascending_783: 'bool33') -> 'Query':
        nb_785: 'MutableSequence36[OrderClause]' = list_8808(this_189.order_clauses_724)
        nb_785.append(OrderClause(field_782, ascending_783))
        return Query(this_189.table_name_721, this_189.conditions_722, this_189.selected_fields_723, tuple_8811(nb_785), this_189.limit_val_725, this_189.offset_val_726, this_189.join_clauses_727, this_189.group_by_fields_728, this_189.having_conditions_729, this_189.is_distinct_730, this_189.select_exprs_731)
    def limit(this_190, n_787: 'int31') -> 'Query':
        if n_787 < 0:
            raise RuntimeError30()
        return Query(this_190.table_name_721, this_190.conditions_722, this_190.selected_fields_723, this_190.order_clauses_724, n_787, this_190.offset_val_726, this_190.join_clauses_727, this_190.group_by_fields_728, this_190.having_conditions_729, this_190.is_distinct_730, this_190.select_exprs_731)
    def offset(this_191, n_790: 'int31') -> 'Query':
        if n_790 < 0:
            raise RuntimeError30()
        return Query(this_191.table_name_721, this_191.conditions_722, this_191.selected_fields_723, this_191.order_clauses_724, this_191.limit_val_725, n_790, this_191.join_clauses_727, this_191.group_by_fields_728, this_191.having_conditions_729, this_191.is_distinct_730, this_191.select_exprs_731)
    def join(this_192, join_type_793: 'JoinType', table_794: 'SafeIdentifier', on_condition_795: 'SqlFragment') -> 'Query':
        nb_797: 'MutableSequence36[JoinClause]' = list_8808(this_192.join_clauses_727)
        nb_797.append(JoinClause(join_type_793, table_794, on_condition_795))
        return Query(this_192.table_name_721, this_192.conditions_722, this_192.selected_fields_723, this_192.order_clauses_724, this_192.limit_val_725, this_192.offset_val_726, tuple_8811(nb_797), this_192.group_by_fields_728, this_192.having_conditions_729, this_192.is_distinct_730, this_192.select_exprs_731)
    def inner_join(this_193, table_799: 'SafeIdentifier', on_condition_800: 'SqlFragment') -> 'Query':
        t_8094: 'InnerJoin' = InnerJoin()
        return this_193.join(t_8094, table_799, on_condition_800)
    def left_join(this_194, table_803: 'SafeIdentifier', on_condition_804: 'SqlFragment') -> 'Query':
        t_8092: 'LeftJoin' = LeftJoin()
        return this_194.join(t_8092, table_803, on_condition_804)
    def right_join(this_195, table_807: 'SafeIdentifier', on_condition_808: 'SqlFragment') -> 'Query':
        t_8090: 'RightJoin' = RightJoin()
        return this_195.join(t_8090, table_807, on_condition_808)
    def full_join(this_196, table_811: 'SafeIdentifier', on_condition_812: 'SqlFragment') -> 'Query':
        t_8088: 'FullJoin' = FullJoin()
        return this_196.join(t_8088, table_811, on_condition_812)
    def group_by(this_197, field_815: 'SafeIdentifier') -> 'Query':
        nb_817: 'MutableSequence36[SafeIdentifier]' = list_8808(this_197.group_by_fields_728)
        nb_817.append(field_815)
        return Query(this_197.table_name_721, this_197.conditions_722, this_197.selected_fields_723, this_197.order_clauses_724, this_197.limit_val_725, this_197.offset_val_726, this_197.join_clauses_727, tuple_8811(nb_817), this_197.having_conditions_729, this_197.is_distinct_730, this_197.select_exprs_731)
    def having(this_198, condition_819: 'SqlFragment') -> 'Query':
        nb_821: 'MutableSequence36[WhereClause]' = list_8808(this_198.having_conditions_729)
        nb_821.append(AndCondition(condition_819))
        return Query(this_198.table_name_721, this_198.conditions_722, this_198.selected_fields_723, this_198.order_clauses_724, this_198.limit_val_725, this_198.offset_val_726, this_198.join_clauses_727, this_198.group_by_fields_728, tuple_8811(nb_821), this_198.is_distinct_730, this_198.select_exprs_731)
    def or_having(this_199, condition_823: 'SqlFragment') -> 'Query':
        nb_825: 'MutableSequence36[WhereClause]' = list_8808(this_199.having_conditions_729)
        nb_825.append(OrCondition(condition_823))
        return Query(this_199.table_name_721, this_199.conditions_722, this_199.selected_fields_723, this_199.order_clauses_724, this_199.limit_val_725, this_199.offset_val_726, this_199.join_clauses_727, this_199.group_by_fields_728, tuple_8811(nb_825), this_199.is_distinct_730, this_199.select_exprs_731)
    def distinct(this_200) -> 'Query':
        return Query(this_200.table_name_721, this_200.conditions_722, this_200.selected_fields_723, this_200.order_clauses_724, this_200.limit_val_725, this_200.offset_val_726, this_200.join_clauses_727, this_200.group_by_fields_728, this_200.having_conditions_729, True, this_200.select_exprs_731)
    def to_sql(this_201) -> 'SqlFragment':
        t_7994: 'int31'
        t_8013: 'int31'
        t_8032: 'int31'
        b_830: 'SqlBuilder' = SqlBuilder()
        if this_201.is_distinct_730:
            b_830.append_safe('SELECT DISTINCT ')
        else:
            b_830.append_safe('SELECT ')
        if not (not this_201.select_exprs_731):
            b_830.append_fragment(list_get_8820(this_201.select_exprs_731, 0))
            i_831: 'int31' = 1
            while True:
                t_7994 = len_8812(this_201.select_exprs_731)
                if not i_831 < t_7994:
                    break
                b_830.append_safe(', ')
                b_830.append_fragment(list_get_8820(this_201.select_exprs_731, i_831))
                i_831 = int_add_8821(i_831, 1)
        elif not this_201.selected_fields_723:
            b_830.append_safe('*')
        else:
            def fn_7987(f_832: 'SafeIdentifier') -> 'str27':
                return f_832.sql_value
            b_830.append_safe(list_join_8823(this_201.selected_fields_723, ', ', fn_7987))
        b_830.append_safe(' FROM ')
        b_830.append_safe(this_201.table_name_721.sql_value)
        def fn_7986(jc_833: 'JoinClause') -> 'None':
            b_830.append_safe(' ')
            t_7974: 'str27' = jc_833.join_type.keyword()
            b_830.append_safe(t_7974)
            b_830.append_safe(' ')
            t_7978: 'str27' = jc_833.table.sql_value
            b_830.append_safe(t_7978)
            b_830.append_safe(' ON ')
            t_7981: 'SqlFragment' = jc_833.on_condition
            b_830.append_fragment(t_7981)
        list_for_each_8806(this_201.join_clauses_727, fn_7986)
        if not (not this_201.conditions_722):
            b_830.append_safe(' WHERE ')
            b_830.append_fragment(list_get_8820(this_201.conditions_722, 0).condition)
            i_834: 'int31' = 1
            while True:
                t_8013 = len_8812(this_201.conditions_722)
                if not i_834 < t_8013:
                    break
                b_830.append_safe(' ')
                b_830.append_safe(list_get_8820(this_201.conditions_722, i_834).keyword())
                b_830.append_safe(' ')
                b_830.append_fragment(list_get_8820(this_201.conditions_722, i_834).condition)
                i_834 = int_add_8821(i_834, 1)
        if not (not this_201.group_by_fields_728):
            b_830.append_safe(' GROUP BY ')
            def fn_7985(f_835: 'SafeIdentifier') -> 'str27':
                return f_835.sql_value
            b_830.append_safe(list_join_8823(this_201.group_by_fields_728, ', ', fn_7985))
        if not (not this_201.having_conditions_729):
            b_830.append_safe(' HAVING ')
            b_830.append_fragment(list_get_8820(this_201.having_conditions_729, 0).condition)
            i_836: 'int31' = 1
            while True:
                t_8032 = len_8812(this_201.having_conditions_729)
                if not i_836 < t_8032:
                    break
                b_830.append_safe(' ')
                b_830.append_safe(list_get_8820(this_201.having_conditions_729, i_836).keyword())
                b_830.append_safe(' ')
                b_830.append_fragment(list_get_8820(this_201.having_conditions_729, i_836).condition)
                i_836 = int_add_8821(i_836, 1)
        if not (not this_201.order_clauses_724):
            b_830.append_safe(' ORDER BY ')
            first_837: 'bool33' = True
            def fn_7984(oc_838: 'OrderClause') -> 'None':
                nonlocal first_837
                t_4304: 'str27'
                if not first_837:
                    b_830.append_safe(', ')
                first_837 = False
                t_7967: 'str27' = oc_838.field.sql_value
                b_830.append_safe(t_7967)
                if oc_838.ascending:
                    t_4304 = ' ASC'
                else:
                    t_4304 = ' DESC'
                b_830.append_safe(t_4304)
            list_for_each_8806(this_201.order_clauses_724, fn_7984)
        lv_839: 'Union40[int31, None]' = this_201.limit_val_725
        if not lv_839 is None:
            lv_1638: 'int31' = lv_839
            b_830.append_safe(' LIMIT ')
            b_830.append_int32(lv_1638)
        ov_840: 'Union40[int31, None]' = this_201.offset_val_726
        if not ov_840 is None:
            ov_1639: 'int31' = ov_840
            b_830.append_safe(' OFFSET ')
            b_830.append_int32(ov_1639)
        return b_830.accumulated
    def count_sql(this_202) -> 'SqlFragment':
        t_7936: 'int31'
        t_7955: 'int31'
        b_843: 'SqlBuilder' = SqlBuilder()
        b_843.append_safe('SELECT COUNT(*) FROM ')
        b_843.append_safe(this_202.table_name_721.sql_value)
        def fn_7924(jc_844: 'JoinClause') -> 'None':
            b_843.append_safe(' ')
            t_7914: 'str27' = jc_844.join_type.keyword()
            b_843.append_safe(t_7914)
            b_843.append_safe(' ')
            t_7918: 'str27' = jc_844.table.sql_value
            b_843.append_safe(t_7918)
            b_843.append_safe(' ON ')
            t_7921: 'SqlFragment' = jc_844.on_condition
            b_843.append_fragment(t_7921)
        list_for_each_8806(this_202.join_clauses_727, fn_7924)
        if not (not this_202.conditions_722):
            b_843.append_safe(' WHERE ')
            b_843.append_fragment(list_get_8820(this_202.conditions_722, 0).condition)
            i_845: 'int31' = 1
            while True:
                t_7936 = len_8812(this_202.conditions_722)
                if not i_845 < t_7936:
                    break
                b_843.append_safe(' ')
                b_843.append_safe(list_get_8820(this_202.conditions_722, i_845).keyword())
                b_843.append_safe(' ')
                b_843.append_fragment(list_get_8820(this_202.conditions_722, i_845).condition)
                i_845 = int_add_8821(i_845, 1)
        if not (not this_202.group_by_fields_728):
            b_843.append_safe(' GROUP BY ')
            def fn_7923(f_846: 'SafeIdentifier') -> 'str27':
                return f_846.sql_value
            b_843.append_safe(list_join_8823(this_202.group_by_fields_728, ', ', fn_7923))
        if not (not this_202.having_conditions_729):
            b_843.append_safe(' HAVING ')
            b_843.append_fragment(list_get_8820(this_202.having_conditions_729, 0).condition)
            i_847: 'int31' = 1
            while True:
                t_7955 = len_8812(this_202.having_conditions_729)
                if not i_847 < t_7955:
                    break
                b_843.append_safe(' ')
                b_843.append_safe(list_get_8820(this_202.having_conditions_729, i_847).keyword())
                b_843.append_safe(' ')
                b_843.append_fragment(list_get_8820(this_202.having_conditions_729, i_847).condition)
                i_847 = int_add_8821(i_847, 1)
        return b_843.accumulated
    def safe_to_sql(this_203, default_limit_849: 'int31') -> 'SqlFragment':
        return_353: 'SqlFragment'
        t_4253: 'Query'
        if default_limit_849 < 0:
            raise RuntimeError30()
        if not this_203.limit_val_725 is None:
            return_353 = this_203.to_sql()
        else:
            t_4253 = this_203.limit(default_limit_849)
            return_353 = t_4253.to_sql()
        return return_353
    def __init__(this_317, table_name_852: 'SafeIdentifier', conditions_853: 'Sequence29[WhereClause]', selected_fields_854: 'Sequence29[SafeIdentifier]', order_clauses_855: 'Sequence29[OrderClause]', limit_val_856: 'Union40[int31, None]', offset_val_857: 'Union40[int31, None]', join_clauses_858: 'Sequence29[JoinClause]', group_by_fields_859: 'Sequence29[SafeIdentifier]', having_conditions_860: 'Sequence29[WhereClause]', is_distinct_861: 'bool33', select_exprs_862: 'Sequence29[SqlFragment]') -> None:
        this_317.table_name_721 = table_name_852
        this_317.conditions_722 = conditions_853
        this_317.selected_fields_723 = selected_fields_854
        this_317.order_clauses_724 = order_clauses_855
        this_317.limit_val_725 = limit_val_856
        this_317.offset_val_726 = offset_val_857
        this_317.join_clauses_727 = join_clauses_858
        this_317.group_by_fields_728 = group_by_fields_859
        this_317.having_conditions_729 = having_conditions_860
        this_317.is_distinct_730 = is_distinct_861
        this_317.select_exprs_731 = select_exprs_862
    @property
    def table_name(this_1359) -> 'SafeIdentifier':
        return this_1359.table_name_721
    @property
    def conditions(this_1362) -> 'Sequence29[WhereClause]':
        return this_1362.conditions_722
    @property
    def selected_fields(this_1365) -> 'Sequence29[SafeIdentifier]':
        return this_1365.selected_fields_723
    @property
    def order_clauses(this_1368) -> 'Sequence29[OrderClause]':
        return this_1368.order_clauses_724
    @property
    def limit_val(this_1371) -> 'Union40[int31, None]':
        return this_1371.limit_val_725
    @property
    def offset_val(this_1374) -> 'Union40[int31, None]':
        return this_1374.offset_val_726
    @property
    def join_clauses(this_1377) -> 'Sequence29[JoinClause]':
        return this_1377.join_clauses_727
    @property
    def group_by_fields(this_1380) -> 'Sequence29[SafeIdentifier]':
        return this_1380.group_by_fields_728
    @property
    def having_conditions(this_1383) -> 'Sequence29[WhereClause]':
        return this_1383.having_conditions_729
    @property
    def is_distinct(this_1386) -> 'bool33':
        return this_1386.is_distinct_730
    @property
    def select_exprs(this_1389) -> 'Sequence29[SqlFragment]':
        return this_1389.select_exprs_731
class SafeIdentifier(metaclass = ABCMeta28):
    pass
class ValidatedIdentifier_205(SafeIdentifier):
    value_1032: 'str27'
    __slots__ = ('value_1032',)
    @property
    def sql_value(this_206) -> 'str27':
        return this_206.value_1032
    def __init__(this_366, value_1036: 'str27') -> None:
        this_366.value_1032 = value_1036
class FieldType(metaclass = ABCMeta28):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_372) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_374) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_376) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_378) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_380) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_382) -> None:
        pass
class FieldDef:
    name_1050: 'SafeIdentifier'
    field_type_1051: 'FieldType'
    nullable_1052: 'bool33'
    __slots__ = ('name_1050', 'field_type_1051', 'nullable_1052')
    def __init__(this_384, name_1054: 'SafeIdentifier', field_type_1055: 'FieldType', nullable_1056: 'bool33') -> None:
        this_384.name_1050 = name_1054
        this_384.field_type_1051 = field_type_1055
        this_384.nullable_1052 = nullable_1056
    @property
    def name(this_1282) -> 'SafeIdentifier':
        return this_1282.name_1050
    @property
    def field_type(this_1285) -> 'FieldType':
        return this_1285.field_type_1051
    @property
    def nullable(this_1288) -> 'bool33':
        return this_1288.nullable_1052
class TableDef:
    table_name_1057: 'SafeIdentifier'
    fields_1058: 'Sequence29[FieldDef]'
    __slots__ = ('table_name_1057', 'fields_1058')
    def field(this_207, name_1060: 'str27') -> 'FieldDef':
        return_389: 'FieldDef'
        with Label35() as fn_1061:
            this_5239: 'Sequence29[FieldDef]' = this_207.fields_1058
            n_5240: 'int31' = len_8812(this_5239)
            i_5241: 'int31' = 0
            while i_5241 < n_5240:
                el_5242: 'FieldDef' = list_get_8820(this_5239, i_5241)
                i_5241 = int_add_8821(i_5241, 1)
                f_1062: 'FieldDef' = el_5242
                if f_1062.name.sql_value == name_1060:
                    return_389 = f_1062
                    fn_1061.break_()
            raise RuntimeError30()
        return return_389
    def __init__(this_386, table_name_1064: 'SafeIdentifier', fields_1065: 'Sequence29[FieldDef]') -> None:
        this_386.table_name_1057 = table_name_1064
        this_386.fields_1058 = fields_1065
    @property
    def table_name(this_1291) -> 'SafeIdentifier':
        return this_1291.table_name_1057
    @property
    def fields(this_1294) -> 'Sequence29[FieldDef]':
        return this_1294.fields_1058
T_226 = TypeVar42('T_226', bound = Any41)
class SqlBuilder:
    buffer_1085: 'MutableSequence36[SqlPart]'
    __slots__ = ('buffer_1085',)
    def append_safe(this_208, sql_source_1087: 'str27') -> 'None':
        t_8767: 'SqlSource' = SqlSource(sql_source_1087)
        this_208.buffer_1085.append(t_8767)
    def append_fragment(this_209, fragment_1090: 'SqlFragment') -> 'None':
        t_8765: 'Sequence29[SqlPart]' = fragment_1090.parts
        list_builder_add_all_8824(this_209.buffer_1085, t_8765)
    def append_part(this_210, part_1093: 'SqlPart') -> 'None':
        this_210.buffer_1085.append(part_1093)
    def append_part_list(this_211, values_1096: 'Sequence29[SqlPart]') -> 'None':
        def fn_8761(x_1098: 'SqlPart') -> 'None':
            this_211.append_part(x_1098)
        this_211.append_list_1141(values_1096, fn_8761)
    def append_boolean(this_212, value_1100: 'bool33') -> 'None':
        t_8758: 'SqlBoolean' = SqlBoolean(value_1100)
        this_212.buffer_1085.append(t_8758)
    def append_boolean_list(this_213, values_1103: 'Sequence29[bool33]') -> 'None':
        def fn_8755(x_1105: 'bool33') -> 'None':
            this_213.append_boolean(x_1105)
        this_213.append_list_1141(values_1103, fn_8755)
    def append_date(this_214, value_1107: 'date26') -> 'None':
        t_8752: 'SqlDate' = SqlDate(value_1107)
        this_214.buffer_1085.append(t_8752)
    def append_date_list(this_215, values_1110: 'Sequence29[date26]') -> 'None':
        def fn_8749(x_1112: 'date26') -> 'None':
            this_215.append_date(x_1112)
        this_215.append_list_1141(values_1110, fn_8749)
    def append_float64(this_216, value_1114: 'float38') -> 'None':
        t_8746: 'SqlFloat64' = SqlFloat64(value_1114)
        this_216.buffer_1085.append(t_8746)
    def append_float64_list(this_217, values_1117: 'Sequence29[float38]') -> 'None':
        def fn_8743(x_1119: 'float38') -> 'None':
            this_217.append_float64(x_1119)
        this_217.append_list_1141(values_1117, fn_8743)
    def append_int32(this_218, value_1121: 'int31') -> 'None':
        t_8740: 'SqlInt32' = SqlInt32(value_1121)
        this_218.buffer_1085.append(t_8740)
    def append_int32_list(this_219, values_1124: 'Sequence29[int31]') -> 'None':
        def fn_8737(x_1126: 'int31') -> 'None':
            this_219.append_int32(x_1126)
        this_219.append_list_1141(values_1124, fn_8737)
    def append_int64(this_220, value_1128: 'int64_23') -> 'None':
        t_8734: 'SqlInt64' = SqlInt64(value_1128)
        this_220.buffer_1085.append(t_8734)
    def append_int64_list(this_221, values_1131: 'Sequence29[int64_23]') -> 'None':
        def fn_8731(x_1133: 'int64_23') -> 'None':
            this_221.append_int64(x_1133)
        this_221.append_list_1141(values_1131, fn_8731)
    def append_string(this_222, value_1135: 'str27') -> 'None':
        t_8728: 'SqlString' = SqlString(value_1135)
        this_222.buffer_1085.append(t_8728)
    def append_string_list(this_223, values_1138: 'Sequence29[str27]') -> 'None':
        def fn_8725(x_1140: 'str27') -> 'None':
            this_223.append_string(x_1140)
        this_223.append_list_1141(values_1138, fn_8725)
    def append_list_1141(this_224, values_1142: 'Sequence29[T_226]', append_value_1143: 'Callable43[[T_226], None]') -> 'None':
        t_8720: 'int31'
        t_8722: 'T_226'
        i_1145: 'int31' = 0
        while True:
            t_8720 = len_8812(values_1142)
            if not i_1145 < t_8720:
                break
            if i_1145 > 0:
                this_224.append_safe(', ')
            t_8722 = list_get_8820(values_1142, i_1145)
            append_value_1143(t_8722)
            i_1145 = int_add_8821(i_1145, 1)
    @property
    def accumulated(this_225) -> 'SqlFragment':
        return SqlFragment(tuple_8811(this_225.buffer_1085))
    def __init__(this_391) -> None:
        t_8717: 'MutableSequence36[SqlPart]' = list_8808()
        this_391.buffer_1085 = t_8717
class SqlFragment:
    parts_1152: 'Sequence29[SqlPart]'
    __slots__ = ('parts_1152',)
    def to_source(this_230) -> 'SqlSource':
        return SqlSource(this_230.to_string())
    def to_string(this_231) -> 'str27':
        t_8791: 'int31'
        builder_1157: 'list3[str27]' = ['']
        i_1158: 'int31' = 0
        while True:
            t_8791 = len_8812(this_231.parts_1152)
            if not i_1158 < t_8791:
                break
            list_get_8820(this_231.parts_1152, i_1158).format_to(builder_1157)
            i_1158 = int_add_8821(i_1158, 1)
        return ''.join(builder_1157)
    def __init__(this_412, parts_1160: 'Sequence29[SqlPart]') -> None:
        this_412.parts_1152 = parts_1160
    @property
    def parts(this_1300) -> 'Sequence29[SqlPart]':
        return this_1300.parts_1152
class SqlPart(metaclass = ABCMeta28):
    def format_to(this_232, builder_1162: 'list3[str27]') -> 'None':
        raise RuntimeError30()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_1164: 'str27'
    __slots__ = ('source_1164',)
    def format_to(this_233, builder_1166: 'list3[str27]') -> 'None':
        builder_1166.append(this_233.source_1164)
    def __init__(this_418, source_1169: 'str27') -> None:
        this_418.source_1164 = source_1169
    @property
    def source(this_1297) -> 'str27':
        return this_1297.source_1164
class SqlBoolean(SqlPart):
    value_1170: 'bool33'
    __slots__ = ('value_1170',)
    def format_to(this_234, builder_1172: 'list3[str27]') -> 'None':
        t_5061: 'str27'
        if this_234.value_1170:
            t_5061 = 'TRUE'
        else:
            t_5061 = 'FALSE'
        builder_1172.append(t_5061)
    def __init__(this_421, value_1175: 'bool33') -> None:
        this_421.value_1170 = value_1175
    @property
    def value(this_1303) -> 'bool33':
        return this_1303.value_1170
class SqlDate(SqlPart):
    value_1176: 'date26'
    __slots__ = ('value_1176',)
    def format_to(this_235, builder_1178: 'list3[str27]') -> 'None':
        builder_1178.append("'")
        t_8772: 'str27' = date_to_string_8828(this_235.value_1176)
        def fn_8770(c_1180: 'int31') -> 'None':
            if c_1180 == 39:
                builder_1178.append("''")
            else:
                builder_1178.append(string_from_code_point44(c_1180))
        string_for_each_8830(t_8772, fn_8770)
        builder_1178.append("'")
    def __init__(this_424, value_1182: 'date26') -> None:
        this_424.value_1176 = value_1182
    @property
    def value(this_1318) -> 'date26':
        return this_1318.value_1176
class SqlFloat64(SqlPart):
    value_1183: 'float38'
    __slots__ = ('value_1183',)
    def format_to(this_236, builder_1185: 'list3[str27]') -> 'None':
        t_5050: 'bool33'
        t_5051: 'bool33'
        s_1187: 'str27' = float64_to_string_8831(this_236.value_1183)
        if s_1187 == 'NaN':
            t_5051 = True
        else:
            if s_1187 == 'Infinity':
                t_5050 = True
            else:
                t_5050 = s_1187 == '-Infinity'
            t_5051 = t_5050
        if t_5051:
            builder_1185.append('NULL')
        else:
            builder_1185.append(s_1187)
    def __init__(this_427, value_1189: 'float38') -> None:
        this_427.value_1183 = value_1189
    @property
    def value(this_1315) -> 'float38':
        return this_1315.value_1183
class SqlInt32(SqlPart):
    value_1190: 'int31'
    __slots__ = ('value_1190',)
    def format_to(this_237, builder_1192: 'list3[str27]') -> 'None':
        t_8781: 'str27' = int_to_string_8815(this_237.value_1190)
        builder_1192.append(t_8781)
    def __init__(this_430, value_1195: 'int31') -> None:
        this_430.value_1190 = value_1195
    @property
    def value(this_1309) -> 'int31':
        return this_1309.value_1190
class SqlInt64(SqlPart):
    value_1196: 'int64_23'
    __slots__ = ('value_1196',)
    def format_to(this_238, builder_1198: 'list3[str27]') -> 'None':
        t_8779: 'str27' = int_to_string_8815(this_238.value_1196)
        builder_1198.append(t_8779)
    def __init__(this_433, value_1201: 'int64_23') -> None:
        this_433.value_1196 = value_1201
    @property
    def value(this_1312) -> 'int64_23':
        return this_1312.value_1196
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_1202: 'str27'
    __slots__ = ('value_1202',)
    def format_to(this_239, builder_1204: 'list3[str27]') -> 'None':
        builder_1204.append("'")
        def fn_8784(c_1206: 'int31') -> 'None':
            if c_1206 == 39:
                builder_1204.append("''")
            else:
                builder_1204.append(string_from_code_point44(c_1206))
        string_for_each_8830(this_239.value_1202, fn_8784)
        builder_1204.append("'")
    def __init__(this_436, value_1208: 'str27') -> None:
        this_436.value_1202 = value_1208
    @property
    def value(this_1306) -> 'str27':
        return this_1306.value_1202
def changeset(table_def_583: 'TableDef', params_584: 'MappingProxyType32[str27, str27]') -> 'Changeset':
    t_8567: 'MappingProxyType32[str27, str27]' = map_constructor_8832(())
    return ChangesetImpl_151(table_def_583, params_584, t_8567, (), True)
def is_ident_start_444(c_1037: 'int31') -> 'bool33':
    return_369: 'bool33'
    t_4824: 'bool33'
    t_4825: 'bool33'
    if c_1037 >= 97:
        t_4824 = c_1037 <= 122
    else:
        t_4824 = False
    if t_4824:
        return_369 = True
    else:
        if c_1037 >= 65:
            t_4825 = c_1037 <= 90
        else:
            t_4825 = False
        if t_4825:
            return_369 = True
        else:
            return_369 = c_1037 == 95
    return return_369
def is_ident_part_445(c_1039: 'int31') -> 'bool33':
    return_370: 'bool33'
    if is_ident_start_444(c_1039):
        return_370 = True
    elif c_1039 >= 48:
        return_370 = c_1039 <= 57
    else:
        return_370 = False
    return return_370
def safe_identifier(name_1041: 'str27') -> 'SafeIdentifier':
    t_8565: 'int31'
    if not name_1041:
        raise RuntimeError30()
    idx_1043: 'int31' = 0
    if not is_ident_start_444(string_get_8833(name_1041, idx_1043)):
        raise RuntimeError30()
    t_8562: 'int31' = string_next_8834(name_1041, idx_1043)
    idx_1043 = t_8562
    while True:
        if not len6(name_1041) > idx_1043:
            break
        if not is_ident_part_445(string_get_8833(name_1041, idx_1043)):
            raise RuntimeError30()
        t_8565 = string_next_8834(name_1041, idx_1043)
        idx_1043 = t_8565
    return ValidatedIdentifier_205(name_1041)
def delete_sql(table_def_673: 'TableDef', id_674: 'int31') -> 'SqlFragment':
    b_676: 'SqlBuilder' = SqlBuilder()
    b_676.append_safe('DELETE FROM ')
    b_676.append_safe(table_def_673.table_name.sql_value)
    b_676.append_safe(' WHERE id = ')
    b_676.append_int32(id_674)
    return b_676.accumulated
def from_(table_name_863: 'SafeIdentifier') -> 'Query':
    return Query(table_name_863, (), (), (), None, None, (), (), (), False, ())
def col(table_865: 'SafeIdentifier', column_866: 'SafeIdentifier') -> 'SqlFragment':
    b_868: 'SqlBuilder' = SqlBuilder()
    b_868.append_safe(table_865.sql_value)
    b_868.append_safe('.')
    b_868.append_safe(column_866.sql_value)
    return b_868.accumulated
def count_all() -> 'SqlFragment':
    b_870: 'SqlBuilder' = SqlBuilder()
    b_870.append_safe('COUNT(*)')
    return b_870.accumulated
def count_col(field_871: 'SafeIdentifier') -> 'SqlFragment':
    b_873: 'SqlBuilder' = SqlBuilder()
    b_873.append_safe('COUNT(')
    b_873.append_safe(field_871.sql_value)
    b_873.append_safe(')')
    return b_873.accumulated
def sum_col(field_874: 'SafeIdentifier') -> 'SqlFragment':
    b_876: 'SqlBuilder' = SqlBuilder()
    b_876.append_safe('SUM(')
    b_876.append_safe(field_874.sql_value)
    b_876.append_safe(')')
    return b_876.accumulated
def avg_col(field_877: 'SafeIdentifier') -> 'SqlFragment':
    b_879: 'SqlBuilder' = SqlBuilder()
    b_879.append_safe('AVG(')
    b_879.append_safe(field_877.sql_value)
    b_879.append_safe(')')
    return b_879.accumulated
def min_col(field_880: 'SafeIdentifier') -> 'SqlFragment':
    b_882: 'SqlBuilder' = SqlBuilder()
    b_882.append_safe('MIN(')
    b_882.append_safe(field_880.sql_value)
    b_882.append_safe(')')
    return b_882.accumulated
def max_col(field_883: 'SafeIdentifier') -> 'SqlFragment':
    b_885: 'SqlBuilder' = SqlBuilder()
    b_885.append_safe('MAX(')
    b_885.append_safe(field_883.sql_value)
    b_885.append_safe(')')
    return b_885.accumulated
