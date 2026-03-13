from builtins import str as str27, RuntimeError as RuntimeError30, int as int31, bool as bool33, Exception as Exception37, float as float38, isinstance as isinstance39, list as list3, len as len6, tuple as tuple5
from abc import ABCMeta as ABCMeta28
from typing import Sequence as Sequence29, Dict as Dict34, MutableSequence as MutableSequence36, Union as Union40, Any as Any41, TypeVar as TypeVar42, Callable as Callable43
from types import MappingProxyType as MappingProxyType32
from temper_core import Label as Label35, Pair as Pair25, string_from_code_point as string_from_code_point44, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, date_from_iso_string as date_from_iso_string13, list_get as list_get14, int_add as int_add15, mapped_to_list as mapped_to_list16, list_join as list_join17, list_builder_add_all as list_builder_add_all18, date_to_string as date_to_string19, string_for_each as string_for_each20, float64_to_string as float64_to_string21, map_constructor as map_constructor22, string_get as string_get23, string_next as string_next24
from datetime import date as date26
map_builder_set_10933 = map_builder_set0
list_for_each_10934 = list_for_each1
mapped_to_map_10935 = mapped_to_map2
list_10936 = list3
mapped_has_10937 = mapped_has4
tuple_10939 = tuple5
len_10940 = len6
string_count_between_10941 = string_count_between7
str_cat_10942 = str_cat8
int_to_string_10943 = int_to_string9
string_to_int32_10944 = string_to_int3210
string_to_int64_10945 = string_to_int6411
string_to_float64_10946 = string_to_float6412
date_from_iso_string_10947 = date_from_iso_string13
list_get_10948 = list_get14
int_add_10949 = int_add15
mapped_to_list_10950 = mapped_to_list16
list_join_10951 = list_join17
list_builder_add_all_10952 = list_builder_add_all18
date_to_string_10956 = date_to_string19
string_for_each_10958 = string_for_each20
float64_to_string_10959 = float64_to_string21
map_constructor_10960 = map_constructor22
string_get_10961 = string_get23
string_next_10962 = string_next24
pair_10964 = Pair25
date_10967 = date26
class ChangesetError:
    field_510: 'str27'
    message_511: 'str27'
    __slots__ = ('field_510', 'message_511')
    def __init__(this_273, field_513: 'str27', message_514: 'str27') -> None:
        this_273.field_510 = field_513
        this_273.message_511 = message_514
    @property
    def field(this_1502) -> 'str27':
        return this_1502.field_510
    @property
    def message(this_1505) -> 'str27':
        return this_1505.message_511
class Changeset(metaclass = ABCMeta28):
    def cast(this_165, allowed_fields_524: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_required(this_166, fields_527: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_length(this_167, field_530: 'SafeIdentifier', min_531: 'int31', max_532: 'int31') -> 'Changeset':
        raise RuntimeError30()
    def validate_int(this_168, field_535: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_int64(this_169, field_538: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_float(this_170, field_541: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_bool(this_171, field_544: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def to_insert_sql(this_172) -> 'SqlFragment':
        raise RuntimeError30()
    def to_update_sql(this_173, id_549: 'int31') -> 'SqlFragment':
        raise RuntimeError30()
class ChangesetImpl_174(Changeset):
    table_def_551: 'TableDef'
    params_552: 'MappingProxyType32[str27, str27]'
    changes_553: 'MappingProxyType32[str27, str27]'
    errors_554: 'Sequence29[ChangesetError]'
    is_valid_555: 'bool33'
    __slots__ = ('table_def_551', 'params_552', 'changes_553', 'errors_554', 'is_valid_555')
    @property
    def table_def(this_175) -> 'TableDef':
        return this_175.table_def_551
    @property
    def changes(this_176) -> 'MappingProxyType32[str27, str27]':
        return this_176.changes_553
    @property
    def errors(this_177) -> 'Sequence29[ChangesetError]':
        return this_177.errors_554
    @property
    def is_valid(this_178) -> 'bool33':
        return this_178.is_valid_555
    def cast(this_179, allowed_fields_565: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        mb_567: 'Dict34[str27, str27]' = {}
        def fn_10837(f_568: 'SafeIdentifier') -> 'None':
            t_10835: 'str27'
            t_10832: 'str27' = f_568.sql_value
            val_569: 'str27' = this_179.params_552.get(t_10832, '')
            if not (not val_569):
                t_10835 = f_568.sql_value
                map_builder_set_10933(mb_567, t_10835, val_569)
        list_for_each_10934(allowed_fields_565, fn_10837)
        return ChangesetImpl_174(this_179.table_def_551, this_179.params_552, mapped_to_map_10935(mb_567), this_179.errors_554, this_179.is_valid_555)
    def validate_required(this_180, fields_571: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        return_306: 'Changeset'
        t_10830: 'Sequence29[ChangesetError]'
        t_6226: 'TableDef'
        t_6227: 'MappingProxyType32[str27, str27]'
        t_6228: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_572:
            if not this_180.is_valid_555:
                return_306 = this_180
                fn_572.break_()
            eb_573: 'MutableSequence36[ChangesetError]' = list_10936(this_180.errors_554)
            valid_574: 'bool33' = True
            def fn_10826(f_575: 'SafeIdentifier') -> 'None':
                nonlocal valid_574
                t_10824: 'ChangesetError'
                t_10821: 'str27' = f_575.sql_value
                if not mapped_has_10937(this_180.changes_553, t_10821):
                    t_10824 = ChangesetError(f_575.sql_value, 'is required')
                    eb_573.append(t_10824)
                    valid_574 = False
            list_for_each_10934(fields_571, fn_10826)
            t_6226 = this_180.table_def_551
            t_6227 = this_180.params_552
            t_6228 = this_180.changes_553
            t_10830 = tuple_10939(eb_573)
            return_306 = ChangesetImpl_174(t_6226, t_6227, t_6228, t_10830, valid_574)
        return return_306
    def validate_length(this_181, field_577: 'SafeIdentifier', min_578: 'int31', max_579: 'int31') -> 'Changeset':
        return_307: 'Changeset'
        t_10808: 'str27'
        t_10819: 'Sequence29[ChangesetError]'
        t_6209: 'bool33'
        t_6215: 'TableDef'
        t_6216: 'MappingProxyType32[str27, str27]'
        t_6217: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_580:
            if not this_181.is_valid_555:
                return_307 = this_181
                fn_580.break_()
            t_10808 = field_577.sql_value
            val_581: 'str27' = this_181.changes_553.get(t_10808, '')
            len_582: 'int31' = string_count_between_10941(val_581, 0, len_10940(val_581))
            if len_582 < min_578:
                t_6209 = True
            else:
                t_6209 = len_582 > max_579
            if t_6209:
                msg_583: 'str27' = str_cat_10942('must be between ', int_to_string_10943(min_578), ' and ', int_to_string_10943(max_579), ' characters')
                eb_584: 'MutableSequence36[ChangesetError]' = list_10936(this_181.errors_554)
                eb_584.append(ChangesetError(field_577.sql_value, msg_583))
                t_6215 = this_181.table_def_551
                t_6216 = this_181.params_552
                t_6217 = this_181.changes_553
                t_10819 = tuple_10939(eb_584)
                return_307 = ChangesetImpl_174(t_6215, t_6216, t_6217, t_10819, False)
                fn_580.break_()
            return_307 = this_181
        return return_307
    def validate_int(this_182, field_586: 'SafeIdentifier') -> 'Changeset':
        return_308: 'Changeset'
        t_10799: 'str27'
        t_10806: 'Sequence29[ChangesetError]'
        t_6200: 'TableDef'
        t_6201: 'MappingProxyType32[str27, str27]'
        t_6202: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_587:
            if not this_182.is_valid_555:
                return_308 = this_182
                fn_587.break_()
            t_10799 = field_586.sql_value
            val_588: 'str27' = this_182.changes_553.get(t_10799, '')
            if not val_588:
                return_308 = this_182
                fn_587.break_()
            parse_ok_589: 'bool33'
            try:
                string_to_int32_10944(val_588)
                parse_ok_589 = True
            except Exception37:
                parse_ok_589 = False
            if not parse_ok_589:
                eb_590: 'MutableSequence36[ChangesetError]' = list_10936(this_182.errors_554)
                eb_590.append(ChangesetError(field_586.sql_value, 'must be an integer'))
                t_6200 = this_182.table_def_551
                t_6201 = this_182.params_552
                t_6202 = this_182.changes_553
                t_10806 = tuple_10939(eb_590)
                return_308 = ChangesetImpl_174(t_6200, t_6201, t_6202, t_10806, False)
                fn_587.break_()
            return_308 = this_182
        return return_308
    def validate_int64(this_183, field_592: 'SafeIdentifier') -> 'Changeset':
        return_309: 'Changeset'
        t_10790: 'str27'
        t_10797: 'Sequence29[ChangesetError]'
        t_6187: 'TableDef'
        t_6188: 'MappingProxyType32[str27, str27]'
        t_6189: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_593:
            if not this_183.is_valid_555:
                return_309 = this_183
                fn_593.break_()
            t_10790 = field_592.sql_value
            val_594: 'str27' = this_183.changes_553.get(t_10790, '')
            if not val_594:
                return_309 = this_183
                fn_593.break_()
            parse_ok_595: 'bool33'
            try:
                string_to_int64_10945(val_594)
                parse_ok_595 = True
            except Exception37:
                parse_ok_595 = False
            if not parse_ok_595:
                eb_596: 'MutableSequence36[ChangesetError]' = list_10936(this_183.errors_554)
                eb_596.append(ChangesetError(field_592.sql_value, 'must be a 64-bit integer'))
                t_6187 = this_183.table_def_551
                t_6188 = this_183.params_552
                t_6189 = this_183.changes_553
                t_10797 = tuple_10939(eb_596)
                return_309 = ChangesetImpl_174(t_6187, t_6188, t_6189, t_10797, False)
                fn_593.break_()
            return_309 = this_183
        return return_309
    def validate_float(this_184, field_598: 'SafeIdentifier') -> 'Changeset':
        return_310: 'Changeset'
        t_10781: 'str27'
        t_10788: 'Sequence29[ChangesetError]'
        t_6174: 'TableDef'
        t_6175: 'MappingProxyType32[str27, str27]'
        t_6176: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_599:
            if not this_184.is_valid_555:
                return_310 = this_184
                fn_599.break_()
            t_10781 = field_598.sql_value
            val_600: 'str27' = this_184.changes_553.get(t_10781, '')
            if not val_600:
                return_310 = this_184
                fn_599.break_()
            parse_ok_601: 'bool33'
            try:
                string_to_float64_10946(val_600)
                parse_ok_601 = True
            except Exception37:
                parse_ok_601 = False
            if not parse_ok_601:
                eb_602: 'MutableSequence36[ChangesetError]' = list_10936(this_184.errors_554)
                eb_602.append(ChangesetError(field_598.sql_value, 'must be a number'))
                t_6174 = this_184.table_def_551
                t_6175 = this_184.params_552
                t_6176 = this_184.changes_553
                t_10788 = tuple_10939(eb_602)
                return_310 = ChangesetImpl_174(t_6174, t_6175, t_6176, t_10788, False)
                fn_599.break_()
            return_310 = this_184
        return return_310
    def validate_bool(this_185, field_604: 'SafeIdentifier') -> 'Changeset':
        return_311: 'Changeset'
        t_10772: 'str27'
        t_10779: 'Sequence29[ChangesetError]'
        t_6149: 'bool33'
        t_6150: 'bool33'
        t_6152: 'bool33'
        t_6153: 'bool33'
        t_6155: 'bool33'
        t_6161: 'TableDef'
        t_6162: 'MappingProxyType32[str27, str27]'
        t_6163: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_605:
            if not this_185.is_valid_555:
                return_311 = this_185
                fn_605.break_()
            t_10772 = field_604.sql_value
            val_606: 'str27' = this_185.changes_553.get(t_10772, '')
            if not val_606:
                return_311 = this_185
                fn_605.break_()
            is_true_607: 'bool33'
            if val_606 == 'true':
                is_true_607 = True
            else:
                if val_606 == '1':
                    t_6150 = True
                else:
                    if val_606 == 'yes':
                        t_6149 = True
                    else:
                        t_6149 = val_606 == 'on'
                    t_6150 = t_6149
                is_true_607 = t_6150
            is_false_608: 'bool33'
            if val_606 == 'false':
                is_false_608 = True
            else:
                if val_606 == '0':
                    t_6153 = True
                else:
                    if val_606 == 'no':
                        t_6152 = True
                    else:
                        t_6152 = val_606 == 'off'
                    t_6153 = t_6152
                is_false_608 = t_6153
            if not is_true_607:
                t_6155 = not is_false_608
            else:
                t_6155 = False
            if t_6155:
                eb_609: 'MutableSequence36[ChangesetError]' = list_10936(this_185.errors_554)
                eb_609.append(ChangesetError(field_604.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_6161 = this_185.table_def_551
                t_6162 = this_185.params_552
                t_6163 = this_185.changes_553
                t_10779 = tuple_10939(eb_609)
                return_311 = ChangesetImpl_174(t_6161, t_6162, t_6163, t_10779, False)
                fn_605.break_()
            return_311 = this_185
        return return_311
    def parse_bool_sql_part_610(this_186, val_611: 'str27') -> 'SqlBoolean':
        return_312: 'SqlBoolean'
        t_6138: 'bool33'
        t_6139: 'bool33'
        t_6140: 'bool33'
        t_6142: 'bool33'
        t_6143: 'bool33'
        t_6144: 'bool33'
        with Label35() as fn_612:
            if val_611 == 'true':
                t_6140 = True
            else:
                if val_611 == '1':
                    t_6139 = True
                else:
                    if val_611 == 'yes':
                        t_6138 = True
                    else:
                        t_6138 = val_611 == 'on'
                    t_6139 = t_6138
                t_6140 = t_6139
            if t_6140:
                return_312 = SqlBoolean(True)
                fn_612.break_()
            if val_611 == 'false':
                t_6144 = True
            else:
                if val_611 == '0':
                    t_6143 = True
                else:
                    if val_611 == 'no':
                        t_6142 = True
                    else:
                        t_6142 = val_611 == 'off'
                    t_6143 = t_6142
                t_6144 = t_6143
            if t_6144:
                return_312 = SqlBoolean(False)
                fn_612.break_()
            raise RuntimeError30()
        return return_312
    def value_to_sql_part_613(this_187, field_def_614: 'FieldDef', val_615: 'str27') -> 'SqlPart':
        return_313: 'SqlPart'
        t_6125: 'int31'
        t_6128: 'int64_23'
        t_6131: 'float38'
        t_6136: 'date26'
        with Label35() as fn_616:
            ft_617: 'FieldType' = field_def_614.field_type
            if isinstance39(ft_617, StringField):
                return_313 = SqlString(val_615)
                fn_616.break_()
            if isinstance39(ft_617, IntField):
                t_6125 = string_to_int32_10944(val_615)
                return_313 = SqlInt32(t_6125)
                fn_616.break_()
            if isinstance39(ft_617, Int64Field):
                t_6128 = string_to_int64_10945(val_615)
                return_313 = SqlInt64(t_6128)
                fn_616.break_()
            if isinstance39(ft_617, FloatField):
                t_6131 = string_to_float64_10946(val_615)
                return_313 = SqlFloat64(t_6131)
                fn_616.break_()
            if isinstance39(ft_617, BoolField):
                return_313 = this_187.parse_bool_sql_part_610(val_615)
                fn_616.break_()
            if isinstance39(ft_617, DateField):
                t_6136 = date_from_iso_string_10947(val_615)
                return_313 = SqlDate(t_6136)
                fn_616.break_()
            raise RuntimeError30()
        return return_313
    def to_insert_sql(this_188) -> 'SqlFragment':
        t_10720: 'int31'
        t_10725: 'str27'
        t_10726: 'bool33'
        t_10731: 'int31'
        t_10733: 'str27'
        t_10737: 'str27'
        t_10752: 'int31'
        t_6089: 'bool33'
        t_6097: 'FieldDef'
        t_6102: 'SqlPart'
        if not this_188.is_valid_555:
            raise RuntimeError30()
        i_620: 'int31' = 0
        while True:
            t_10720 = len_10940(this_188.table_def_551.fields)
            if not i_620 < t_10720:
                break
            f_621: 'FieldDef' = list_get_10948(this_188.table_def_551.fields, i_620)
            if not f_621.nullable:
                t_10725 = f_621.name.sql_value
                t_10726 = mapped_has_10937(this_188.changes_553, t_10725)
                t_6089 = not t_10726
            else:
                t_6089 = False
            if t_6089:
                raise RuntimeError30()
            i_620 = int_add_10949(i_620, 1)
        pairs_622: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_10950(this_188.changes_553)
        if len_10940(pairs_622) == 0:
            raise RuntimeError30()
        col_names_623: 'MutableSequence36[str27]' = list_10936()
        val_parts_624: 'MutableSequence36[SqlPart]' = list_10936()
        i_625: 'int31' = 0
        while True:
            t_10731 = len_10940(pairs_622)
            if not i_625 < t_10731:
                break
            pair_626: 'Pair25[str27, str27]' = list_get_10948(pairs_622, i_625)
            t_10733 = pair_626.key
            t_6097 = this_188.table_def_551.field(t_10733)
            fd_627: 'FieldDef' = t_6097
            col_names_623.append(fd_627.name.sql_value)
            t_10737 = pair_626.value
            t_6102 = this_188.value_to_sql_part_613(fd_627, t_10737)
            val_parts_624.append(t_6102)
            i_625 = int_add_10949(i_625, 1)
        b_628: 'SqlBuilder' = SqlBuilder()
        b_628.append_safe('INSERT INTO ')
        b_628.append_safe(this_188.table_def_551.table_name.sql_value)
        b_628.append_safe(' (')
        t_10745: 'Sequence29[str27]' = tuple_10939(col_names_623)
        def fn_10718(c_629: 'str27') -> 'str27':
            return c_629
        b_628.append_safe(list_join_10951(t_10745, ', ', fn_10718))
        b_628.append_safe(') VALUES (')
        b_628.append_part(list_get_10948(val_parts_624, 0))
        j_630: 'int31' = 1
        while True:
            t_10752 = len_10940(val_parts_624)
            if not j_630 < t_10752:
                break
            b_628.append_safe(', ')
            b_628.append_part(list_get_10948(val_parts_624, j_630))
            j_630 = int_add_10949(j_630, 1)
        b_628.append_safe(')')
        return b_628.accumulated
    def to_update_sql(this_189, id_632: 'int31') -> 'SqlFragment':
        t_10705: 'int31'
        t_10708: 'str27'
        t_10713: 'str27'
        t_6070: 'FieldDef'
        t_6076: 'SqlPart'
        if not this_189.is_valid_555:
            raise RuntimeError30()
        pairs_634: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_10950(this_189.changes_553)
        if len_10940(pairs_634) == 0:
            raise RuntimeError30()
        b_635: 'SqlBuilder' = SqlBuilder()
        b_635.append_safe('UPDATE ')
        b_635.append_safe(this_189.table_def_551.table_name.sql_value)
        b_635.append_safe(' SET ')
        i_636: 'int31' = 0
        while True:
            t_10705 = len_10940(pairs_634)
            if not i_636 < t_10705:
                break
            if i_636 > 0:
                b_635.append_safe(', ')
            pair_637: 'Pair25[str27, str27]' = list_get_10948(pairs_634, i_636)
            t_10708 = pair_637.key
            t_6070 = this_189.table_def_551.field(t_10708)
            fd_638: 'FieldDef' = t_6070
            b_635.append_safe(fd_638.name.sql_value)
            b_635.append_safe(' = ')
            t_10713 = pair_637.value
            t_6076 = this_189.value_to_sql_part_613(fd_638, t_10713)
            b_635.append_part(t_6076)
            i_636 = int_add_10949(i_636, 1)
        b_635.append_safe(' WHERE id = ')
        b_635.append_int32(id_632)
        return b_635.accumulated
    def __init__(this_296, table_def_640: 'TableDef', params_641: 'MappingProxyType32[str27, str27]', changes_642: 'MappingProxyType32[str27, str27]', errors_643: 'Sequence29[ChangesetError]', is_valid_644: 'bool33') -> None:
        this_296.table_def_551 = table_def_640
        this_296.params_552 = params_641
        this_296.changes_553 = changes_642
        this_296.errors_554 = errors_643
        this_296.is_valid_555 = is_valid_644
class JoinType(metaclass = ABCMeta28):
    def keyword(this_190) -> 'str27':
        raise RuntimeError30()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_191) -> 'str27':
        return 'INNER JOIN'
    def __init__(this_321) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_192) -> 'str27':
        return 'LEFT JOIN'
    def __init__(this_324) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_193) -> 'str27':
        return 'RIGHT JOIN'
    def __init__(this_327) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_194) -> 'str27':
        return 'FULL OUTER JOIN'
    def __init__(this_330) -> None:
        pass
class JoinClause:
    join_type_753: 'JoinType'
    table_754: 'SafeIdentifier'
    on_condition_755: 'SqlFragment'
    __slots__ = ('join_type_753', 'table_754', 'on_condition_755')
    def __init__(this_333, join_type_757: 'JoinType', table_758: 'SafeIdentifier', on_condition_759: 'SqlFragment') -> None:
        this_333.join_type_753 = join_type_757
        this_333.table_754 = table_758
        this_333.on_condition_755 = on_condition_759
    @property
    def join_type(this_1570) -> 'JoinType':
        return this_1570.join_type_753
    @property
    def table(this_1573) -> 'SafeIdentifier':
        return this_1573.table_754
    @property
    def on_condition(this_1576) -> 'SqlFragment':
        return this_1576.on_condition_755
class OrderClause:
    field_760: 'SafeIdentifier'
    ascending_761: 'bool33'
    __slots__ = ('field_760', 'ascending_761')
    def __init__(this_335, field_763: 'SafeIdentifier', ascending_764: 'bool33') -> None:
        this_335.field_760 = field_763
        this_335.ascending_761 = ascending_764
    @property
    def field(this_1579) -> 'SafeIdentifier':
        return this_1579.field_760
    @property
    def ascending(this_1582) -> 'bool33':
        return this_1582.ascending_761
class WhereClause(metaclass = ABCMeta28):
    def keyword(this_196) -> 'str27':
        raise RuntimeError30()
class AndCondition(WhereClause):
    condition_769: 'SqlFragment'
    __slots__ = ('condition_769',)
    @property
    def condition(this_197) -> 'SqlFragment':
        return this_197.condition_769
    def keyword(this_198) -> 'str27':
        return 'AND'
    def __init__(this_341, condition_775: 'SqlFragment') -> None:
        this_341.condition_769 = condition_775
class OrCondition(WhereClause):
    condition_776: 'SqlFragment'
    __slots__ = ('condition_776',)
    @property
    def condition(this_199) -> 'SqlFragment':
        return this_199.condition_776
    def keyword(this_200) -> 'str27':
        return 'OR'
    def __init__(this_346, condition_782: 'SqlFragment') -> None:
        this_346.condition_776 = condition_782
class Query:
    table_name_783: 'SafeIdentifier'
    conditions_784: 'Sequence29[WhereClause]'
    selected_fields_785: 'Sequence29[SafeIdentifier]'
    order_clauses_786: 'Sequence29[OrderClause]'
    limit_val_787: 'Union40[int31, None]'
    offset_val_788: 'Union40[int31, None]'
    join_clauses_789: 'Sequence29[JoinClause]'
    group_by_fields_790: 'Sequence29[SafeIdentifier]'
    having_conditions_791: 'Sequence29[WhereClause]'
    is_distinct_792: 'bool33'
    select_exprs_793: 'Sequence29[SqlFragment]'
    __slots__ = ('table_name_783', 'conditions_784', 'selected_fields_785', 'order_clauses_786', 'limit_val_787', 'offset_val_788', 'join_clauses_789', 'group_by_fields_790', 'having_conditions_791', 'is_distinct_792', 'select_exprs_793')
    def where(this_201, condition_795: 'SqlFragment') -> 'Query':
        nb_797: 'MutableSequence36[WhereClause]' = list_10936(this_201.conditions_784)
        nb_797.append(AndCondition(condition_795))
        return Query(this_201.table_name_783, tuple_10939(nb_797), this_201.selected_fields_785, this_201.order_clauses_786, this_201.limit_val_787, this_201.offset_val_788, this_201.join_clauses_789, this_201.group_by_fields_790, this_201.having_conditions_791, this_201.is_distinct_792, this_201.select_exprs_793)
    def or_where(this_202, condition_799: 'SqlFragment') -> 'Query':
        nb_801: 'MutableSequence36[WhereClause]' = list_10936(this_202.conditions_784)
        nb_801.append(OrCondition(condition_799))
        return Query(this_202.table_name_783, tuple_10939(nb_801), this_202.selected_fields_785, this_202.order_clauses_786, this_202.limit_val_787, this_202.offset_val_788, this_202.join_clauses_789, this_202.group_by_fields_790, this_202.having_conditions_791, this_202.is_distinct_792, this_202.select_exprs_793)
    def where_null(this_203, field_803: 'SafeIdentifier') -> 'Query':
        b_805: 'SqlBuilder' = SqlBuilder()
        b_805.append_safe(field_803.sql_value)
        b_805.append_safe(' IS NULL')
        t_10304: 'SqlFragment' = b_805.accumulated
        return this_203.where(t_10304)
    def where_not_null(this_204, field_807: 'SafeIdentifier') -> 'Query':
        b_809: 'SqlBuilder' = SqlBuilder()
        b_809.append_safe(field_807.sql_value)
        b_809.append_safe(' IS NOT NULL')
        t_10298: 'SqlFragment' = b_809.accumulated
        return this_204.where(t_10298)
    def where_in(this_205, field_811: 'SafeIdentifier', values_812: 'Sequence29[SqlPart]') -> 'Query':
        return_365: 'Query'
        t_10279: 'SqlFragment'
        t_10287: 'int31'
        t_10292: 'SqlFragment'
        with Label35() as fn_813:
            if not values_812:
                b_814: 'SqlBuilder' = SqlBuilder()
                b_814.append_safe('1 = 0')
                t_10279 = b_814.accumulated
                return_365 = this_205.where(t_10279)
                fn_813.break_()
            b_815: 'SqlBuilder' = SqlBuilder()
            b_815.append_safe(field_811.sql_value)
            b_815.append_safe(' IN (')
            b_815.append_part(list_get_10948(values_812, 0))
            i_816: 'int31' = 1
            while True:
                t_10287 = len_10940(values_812)
                if not i_816 < t_10287:
                    break
                b_815.append_safe(', ')
                b_815.append_part(list_get_10948(values_812, i_816))
                i_816 = int_add_10949(i_816, 1)
            b_815.append_safe(')')
            t_10292 = b_815.accumulated
            return_365 = this_205.where(t_10292)
        return return_365
    def where_in_subquery(this_206, field_818: 'SafeIdentifier', sub_819: 'Query') -> 'Query':
        b_821: 'SqlBuilder' = SqlBuilder()
        b_821.append_safe(field_818.sql_value)
        b_821.append_safe(' IN (')
        b_821.append_fragment(sub_819.to_sql())
        b_821.append_safe(')')
        t_10274: 'SqlFragment' = b_821.accumulated
        return this_206.where(t_10274)
    def where_not(this_207, condition_823: 'SqlFragment') -> 'Query':
        b_825: 'SqlBuilder' = SqlBuilder()
        b_825.append_safe('NOT (')
        b_825.append_fragment(condition_823)
        b_825.append_safe(')')
        t_10265: 'SqlFragment' = b_825.accumulated
        return this_207.where(t_10265)
    def where_between(this_208, field_827: 'SafeIdentifier', low_828: 'SqlPart', high_829: 'SqlPart') -> 'Query':
        b_831: 'SqlBuilder' = SqlBuilder()
        b_831.append_safe(field_827.sql_value)
        b_831.append_safe(' BETWEEN ')
        b_831.append_part(low_828)
        b_831.append_safe(' AND ')
        b_831.append_part(high_829)
        t_10259: 'SqlFragment' = b_831.accumulated
        return this_208.where(t_10259)
    def where_like(this_209, field_833: 'SafeIdentifier', pattern_834: 'str27') -> 'Query':
        b_836: 'SqlBuilder' = SqlBuilder()
        b_836.append_safe(field_833.sql_value)
        b_836.append_safe(' LIKE ')
        b_836.append_string(pattern_834)
        t_10250: 'SqlFragment' = b_836.accumulated
        return this_209.where(t_10250)
    def where_i_like(this_210, field_838: 'SafeIdentifier', pattern_839: 'str27') -> 'Query':
        b_841: 'SqlBuilder' = SqlBuilder()
        b_841.append_safe(field_838.sql_value)
        b_841.append_safe(' ILIKE ')
        b_841.append_string(pattern_839)
        t_10243: 'SqlFragment' = b_841.accumulated
        return this_210.where(t_10243)
    def select(this_211, fields_843: 'Sequence29[SafeIdentifier]') -> 'Query':
        return Query(this_211.table_name_783, this_211.conditions_784, fields_843, this_211.order_clauses_786, this_211.limit_val_787, this_211.offset_val_788, this_211.join_clauses_789, this_211.group_by_fields_790, this_211.having_conditions_791, this_211.is_distinct_792, this_211.select_exprs_793)
    def select_expr(this_212, exprs_846: 'Sequence29[SqlFragment]') -> 'Query':
        return Query(this_212.table_name_783, this_212.conditions_784, this_212.selected_fields_785, this_212.order_clauses_786, this_212.limit_val_787, this_212.offset_val_788, this_212.join_clauses_789, this_212.group_by_fields_790, this_212.having_conditions_791, this_212.is_distinct_792, exprs_846)
    def order_by(this_213, field_849: 'SafeIdentifier', ascending_850: 'bool33') -> 'Query':
        nb_852: 'MutableSequence36[OrderClause]' = list_10936(this_213.order_clauses_786)
        nb_852.append(OrderClause(field_849, ascending_850))
        return Query(this_213.table_name_783, this_213.conditions_784, this_213.selected_fields_785, tuple_10939(nb_852), this_213.limit_val_787, this_213.offset_val_788, this_213.join_clauses_789, this_213.group_by_fields_790, this_213.having_conditions_791, this_213.is_distinct_792, this_213.select_exprs_793)
    def limit(this_214, n_854: 'int31') -> 'Query':
        if n_854 < 0:
            raise RuntimeError30()
        return Query(this_214.table_name_783, this_214.conditions_784, this_214.selected_fields_785, this_214.order_clauses_786, n_854, this_214.offset_val_788, this_214.join_clauses_789, this_214.group_by_fields_790, this_214.having_conditions_791, this_214.is_distinct_792, this_214.select_exprs_793)
    def offset(this_215, n_857: 'int31') -> 'Query':
        if n_857 < 0:
            raise RuntimeError30()
        return Query(this_215.table_name_783, this_215.conditions_784, this_215.selected_fields_785, this_215.order_clauses_786, this_215.limit_val_787, n_857, this_215.join_clauses_789, this_215.group_by_fields_790, this_215.having_conditions_791, this_215.is_distinct_792, this_215.select_exprs_793)
    def join(this_216, join_type_860: 'JoinType', table_861: 'SafeIdentifier', on_condition_862: 'SqlFragment') -> 'Query':
        nb_864: 'MutableSequence36[JoinClause]' = list_10936(this_216.join_clauses_789)
        nb_864.append(JoinClause(join_type_860, table_861, on_condition_862))
        return Query(this_216.table_name_783, this_216.conditions_784, this_216.selected_fields_785, this_216.order_clauses_786, this_216.limit_val_787, this_216.offset_val_788, tuple_10939(nb_864), this_216.group_by_fields_790, this_216.having_conditions_791, this_216.is_distinct_792, this_216.select_exprs_793)
    def inner_join(this_217, table_866: 'SafeIdentifier', on_condition_867: 'SqlFragment') -> 'Query':
        t_10213: 'InnerJoin' = InnerJoin()
        return this_217.join(t_10213, table_866, on_condition_867)
    def left_join(this_218, table_870: 'SafeIdentifier', on_condition_871: 'SqlFragment') -> 'Query':
        t_10211: 'LeftJoin' = LeftJoin()
        return this_218.join(t_10211, table_870, on_condition_871)
    def right_join(this_219, table_874: 'SafeIdentifier', on_condition_875: 'SqlFragment') -> 'Query':
        t_10209: 'RightJoin' = RightJoin()
        return this_219.join(t_10209, table_874, on_condition_875)
    def full_join(this_220, table_878: 'SafeIdentifier', on_condition_879: 'SqlFragment') -> 'Query':
        t_10207: 'FullJoin' = FullJoin()
        return this_220.join(t_10207, table_878, on_condition_879)
    def group_by(this_221, field_882: 'SafeIdentifier') -> 'Query':
        nb_884: 'MutableSequence36[SafeIdentifier]' = list_10936(this_221.group_by_fields_790)
        nb_884.append(field_882)
        return Query(this_221.table_name_783, this_221.conditions_784, this_221.selected_fields_785, this_221.order_clauses_786, this_221.limit_val_787, this_221.offset_val_788, this_221.join_clauses_789, tuple_10939(nb_884), this_221.having_conditions_791, this_221.is_distinct_792, this_221.select_exprs_793)
    def having(this_222, condition_886: 'SqlFragment') -> 'Query':
        nb_888: 'MutableSequence36[WhereClause]' = list_10936(this_222.having_conditions_791)
        nb_888.append(AndCondition(condition_886))
        return Query(this_222.table_name_783, this_222.conditions_784, this_222.selected_fields_785, this_222.order_clauses_786, this_222.limit_val_787, this_222.offset_val_788, this_222.join_clauses_789, this_222.group_by_fields_790, tuple_10939(nb_888), this_222.is_distinct_792, this_222.select_exprs_793)
    def or_having(this_223, condition_890: 'SqlFragment') -> 'Query':
        nb_892: 'MutableSequence36[WhereClause]' = list_10936(this_223.having_conditions_791)
        nb_892.append(OrCondition(condition_890))
        return Query(this_223.table_name_783, this_223.conditions_784, this_223.selected_fields_785, this_223.order_clauses_786, this_223.limit_val_787, this_223.offset_val_788, this_223.join_clauses_789, this_223.group_by_fields_790, tuple_10939(nb_892), this_223.is_distinct_792, this_223.select_exprs_793)
    def distinct(this_224) -> 'Query':
        return Query(this_224.table_name_783, this_224.conditions_784, this_224.selected_fields_785, this_224.order_clauses_786, this_224.limit_val_787, this_224.offset_val_788, this_224.join_clauses_789, this_224.group_by_fields_790, this_224.having_conditions_791, True, this_224.select_exprs_793)
    def to_sql(this_225) -> 'SqlFragment':
        t_10113: 'int31'
        t_10132: 'int31'
        t_10151: 'int31'
        b_897: 'SqlBuilder' = SqlBuilder()
        if this_225.is_distinct_792:
            b_897.append_safe('SELECT DISTINCT ')
        else:
            b_897.append_safe('SELECT ')
        if not (not this_225.select_exprs_793):
            b_897.append_fragment(list_get_10948(this_225.select_exprs_793, 0))
            i_898: 'int31' = 1
            while True:
                t_10113 = len_10940(this_225.select_exprs_793)
                if not i_898 < t_10113:
                    break
                b_897.append_safe(', ')
                b_897.append_fragment(list_get_10948(this_225.select_exprs_793, i_898))
                i_898 = int_add_10949(i_898, 1)
        elif not this_225.selected_fields_785:
            b_897.append_safe('*')
        else:
            def fn_10106(f_899: 'SafeIdentifier') -> 'str27':
                return f_899.sql_value
            b_897.append_safe(list_join_10951(this_225.selected_fields_785, ', ', fn_10106))
        b_897.append_safe(' FROM ')
        b_897.append_safe(this_225.table_name_783.sql_value)
        def fn_10105(jc_900: 'JoinClause') -> 'None':
            b_897.append_safe(' ')
            t_10093: 'str27' = jc_900.join_type.keyword()
            b_897.append_safe(t_10093)
            b_897.append_safe(' ')
            t_10097: 'str27' = jc_900.table.sql_value
            b_897.append_safe(t_10097)
            b_897.append_safe(' ON ')
            t_10100: 'SqlFragment' = jc_900.on_condition
            b_897.append_fragment(t_10100)
        list_for_each_10934(this_225.join_clauses_789, fn_10105)
        if not (not this_225.conditions_784):
            b_897.append_safe(' WHERE ')
            b_897.append_fragment(list_get_10948(this_225.conditions_784, 0).condition)
            i_901: 'int31' = 1
            while True:
                t_10132 = len_10940(this_225.conditions_784)
                if not i_901 < t_10132:
                    break
                b_897.append_safe(' ')
                b_897.append_safe(list_get_10948(this_225.conditions_784, i_901).keyword())
                b_897.append_safe(' ')
                b_897.append_fragment(list_get_10948(this_225.conditions_784, i_901).condition)
                i_901 = int_add_10949(i_901, 1)
        if not (not this_225.group_by_fields_790):
            b_897.append_safe(' GROUP BY ')
            def fn_10104(f_902: 'SafeIdentifier') -> 'str27':
                return f_902.sql_value
            b_897.append_safe(list_join_10951(this_225.group_by_fields_790, ', ', fn_10104))
        if not (not this_225.having_conditions_791):
            b_897.append_safe(' HAVING ')
            b_897.append_fragment(list_get_10948(this_225.having_conditions_791, 0).condition)
            i_903: 'int31' = 1
            while True:
                t_10151 = len_10940(this_225.having_conditions_791)
                if not i_903 < t_10151:
                    break
                b_897.append_safe(' ')
                b_897.append_safe(list_get_10948(this_225.having_conditions_791, i_903).keyword())
                b_897.append_safe(' ')
                b_897.append_fragment(list_get_10948(this_225.having_conditions_791, i_903).condition)
                i_903 = int_add_10949(i_903, 1)
        if not (not this_225.order_clauses_786):
            b_897.append_safe(' ORDER BY ')
            first_904: 'bool33' = True
            def fn_10103(oc_905: 'OrderClause') -> 'None':
                nonlocal first_904
                t_5515: 'str27'
                if not first_904:
                    b_897.append_safe(', ')
                first_904 = False
                t_10086: 'str27' = oc_905.field.sql_value
                b_897.append_safe(t_10086)
                if oc_905.ascending:
                    t_5515 = ' ASC'
                else:
                    t_5515 = ' DESC'
                b_897.append_safe(t_5515)
            list_for_each_10934(this_225.order_clauses_786, fn_10103)
        lv_906: 'Union40[int31, None]' = this_225.limit_val_787
        if not lv_906 is None:
            lv_1952: 'int31' = lv_906
            b_897.append_safe(' LIMIT ')
            b_897.append_int32(lv_1952)
        ov_907: 'Union40[int31, None]' = this_225.offset_val_788
        if not ov_907 is None:
            ov_1953: 'int31' = ov_907
            b_897.append_safe(' OFFSET ')
            b_897.append_int32(ov_1953)
        return b_897.accumulated
    def count_sql(this_226) -> 'SqlFragment':
        t_10055: 'int31'
        t_10074: 'int31'
        b_910: 'SqlBuilder' = SqlBuilder()
        b_910.append_safe('SELECT COUNT(*) FROM ')
        b_910.append_safe(this_226.table_name_783.sql_value)
        def fn_10043(jc_911: 'JoinClause') -> 'None':
            b_910.append_safe(' ')
            t_10033: 'str27' = jc_911.join_type.keyword()
            b_910.append_safe(t_10033)
            b_910.append_safe(' ')
            t_10037: 'str27' = jc_911.table.sql_value
            b_910.append_safe(t_10037)
            b_910.append_safe(' ON ')
            t_10040: 'SqlFragment' = jc_911.on_condition
            b_910.append_fragment(t_10040)
        list_for_each_10934(this_226.join_clauses_789, fn_10043)
        if not (not this_226.conditions_784):
            b_910.append_safe(' WHERE ')
            b_910.append_fragment(list_get_10948(this_226.conditions_784, 0).condition)
            i_912: 'int31' = 1
            while True:
                t_10055 = len_10940(this_226.conditions_784)
                if not i_912 < t_10055:
                    break
                b_910.append_safe(' ')
                b_910.append_safe(list_get_10948(this_226.conditions_784, i_912).keyword())
                b_910.append_safe(' ')
                b_910.append_fragment(list_get_10948(this_226.conditions_784, i_912).condition)
                i_912 = int_add_10949(i_912, 1)
        if not (not this_226.group_by_fields_790):
            b_910.append_safe(' GROUP BY ')
            def fn_10042(f_913: 'SafeIdentifier') -> 'str27':
                return f_913.sql_value
            b_910.append_safe(list_join_10951(this_226.group_by_fields_790, ', ', fn_10042))
        if not (not this_226.having_conditions_791):
            b_910.append_safe(' HAVING ')
            b_910.append_fragment(list_get_10948(this_226.having_conditions_791, 0).condition)
            i_914: 'int31' = 1
            while True:
                t_10074 = len_10940(this_226.having_conditions_791)
                if not i_914 < t_10074:
                    break
                b_910.append_safe(' ')
                b_910.append_safe(list_get_10948(this_226.having_conditions_791, i_914).keyword())
                b_910.append_safe(' ')
                b_910.append_fragment(list_get_10948(this_226.having_conditions_791, i_914).condition)
                i_914 = int_add_10949(i_914, 1)
        return b_910.accumulated
    def safe_to_sql(this_227, default_limit_916: 'int31') -> 'SqlFragment':
        return_387: 'SqlFragment'
        t_5464: 'Query'
        if default_limit_916 < 0:
            raise RuntimeError30()
        if not this_227.limit_val_787 is None:
            return_387 = this_227.to_sql()
        else:
            t_5464 = this_227.limit(default_limit_916)
            return_387 = t_5464.to_sql()
        return return_387
    def __init__(this_350, table_name_919: 'SafeIdentifier', conditions_920: 'Sequence29[WhereClause]', selected_fields_921: 'Sequence29[SafeIdentifier]', order_clauses_922: 'Sequence29[OrderClause]', limit_val_923: 'Union40[int31, None]', offset_val_924: 'Union40[int31, None]', join_clauses_925: 'Sequence29[JoinClause]', group_by_fields_926: 'Sequence29[SafeIdentifier]', having_conditions_927: 'Sequence29[WhereClause]', is_distinct_928: 'bool33', select_exprs_929: 'Sequence29[SqlFragment]') -> None:
        this_350.table_name_783 = table_name_919
        this_350.conditions_784 = conditions_920
        this_350.selected_fields_785 = selected_fields_921
        this_350.order_clauses_786 = order_clauses_922
        this_350.limit_val_787 = limit_val_923
        this_350.offset_val_788 = offset_val_924
        this_350.join_clauses_789 = join_clauses_925
        this_350.group_by_fields_790 = group_by_fields_926
        this_350.having_conditions_791 = having_conditions_927
        this_350.is_distinct_792 = is_distinct_928
        this_350.select_exprs_793 = select_exprs_929
    @property
    def table_name(this_1585) -> 'SafeIdentifier':
        return this_1585.table_name_783
    @property
    def conditions(this_1588) -> 'Sequence29[WhereClause]':
        return this_1588.conditions_784
    @property
    def selected_fields(this_1591) -> 'Sequence29[SafeIdentifier]':
        return this_1591.selected_fields_785
    @property
    def order_clauses(this_1594) -> 'Sequence29[OrderClause]':
        return this_1594.order_clauses_786
    @property
    def limit_val(this_1597) -> 'Union40[int31, None]':
        return this_1597.limit_val_787
    @property
    def offset_val(this_1600) -> 'Union40[int31, None]':
        return this_1600.offset_val_788
    @property
    def join_clauses(this_1603) -> 'Sequence29[JoinClause]':
        return this_1603.join_clauses_789
    @property
    def group_by_fields(this_1606) -> 'Sequence29[SafeIdentifier]':
        return this_1606.group_by_fields_790
    @property
    def having_conditions(this_1609) -> 'Sequence29[WhereClause]':
        return this_1609.having_conditions_791
    @property
    def is_distinct(this_1612) -> 'bool33':
        return this_1612.is_distinct_792
    @property
    def select_exprs(this_1615) -> 'Sequence29[SqlFragment]':
        return this_1615.select_exprs_793
class SetClause:
    field_976: 'SafeIdentifier'
    value_977: 'SqlPart'
    __slots__ = ('field_976', 'value_977')
    def __init__(this_402, field_979: 'SafeIdentifier', value_980: 'SqlPart') -> None:
        this_402.field_976 = field_979
        this_402.value_977 = value_980
    @property
    def field(this_1618) -> 'SafeIdentifier':
        return this_1618.field_976
    @property
    def value(this_1621) -> 'SqlPart':
        return this_1621.value_977
class UpdateQuery:
    table_name_981: 'SafeIdentifier'
    set_clauses_982: 'Sequence29[SetClause]'
    conditions_983: 'Sequence29[WhereClause]'
    limit_val_984: 'Union40[int31, None]'
    __slots__ = ('table_name_981', 'set_clauses_982', 'conditions_983', 'limit_val_984')
    def set(this_228, field_986: 'SafeIdentifier', value_987: 'SqlPart') -> 'UpdateQuery':
        nb_989: 'MutableSequence36[SetClause]' = list_10936(this_228.set_clauses_982)
        nb_989.append(SetClause(field_986, value_987))
        return UpdateQuery(this_228.table_name_981, tuple_10939(nb_989), this_228.conditions_983, this_228.limit_val_984)
    def where(this_229, condition_991: 'SqlFragment') -> 'UpdateQuery':
        nb_993: 'MutableSequence36[WhereClause]' = list_10936(this_229.conditions_983)
        nb_993.append(AndCondition(condition_991))
        return UpdateQuery(this_229.table_name_981, this_229.set_clauses_982, tuple_10939(nb_993), this_229.limit_val_984)
    def or_where(this_230, condition_995: 'SqlFragment') -> 'UpdateQuery':
        nb_997: 'MutableSequence36[WhereClause]' = list_10936(this_230.conditions_983)
        nb_997.append(OrCondition(condition_995))
        return UpdateQuery(this_230.table_name_981, this_230.set_clauses_982, tuple_10939(nb_997), this_230.limit_val_984)
    def limit(this_231, n_999: 'int31') -> 'UpdateQuery':
        if n_999 < 0:
            raise RuntimeError30()
        return UpdateQuery(this_231.table_name_981, this_231.set_clauses_982, this_231.conditions_983, n_999)
    def to_sql(this_232) -> 'SqlFragment':
        t_9890: 'int31'
        t_9904: 'int31'
        if not this_232.conditions_983:
            raise RuntimeError30()
        if not this_232.set_clauses_982:
            raise RuntimeError30()
        b_1003: 'SqlBuilder' = SqlBuilder()
        b_1003.append_safe('UPDATE ')
        b_1003.append_safe(this_232.table_name_981.sql_value)
        b_1003.append_safe(' SET ')
        b_1003.append_safe(list_get_10948(this_232.set_clauses_982, 0).field.sql_value)
        b_1003.append_safe(' = ')
        b_1003.append_part(list_get_10948(this_232.set_clauses_982, 0).value)
        i_1004: 'int31' = 1
        while True:
            t_9890 = len_10940(this_232.set_clauses_982)
            if not i_1004 < t_9890:
                break
            b_1003.append_safe(', ')
            b_1003.append_safe(list_get_10948(this_232.set_clauses_982, i_1004).field.sql_value)
            b_1003.append_safe(' = ')
            b_1003.append_part(list_get_10948(this_232.set_clauses_982, i_1004).value)
            i_1004 = int_add_10949(i_1004, 1)
        b_1003.append_safe(' WHERE ')
        b_1003.append_fragment(list_get_10948(this_232.conditions_983, 0).condition)
        i_1005: 'int31' = 1
        while True:
            t_9904 = len_10940(this_232.conditions_983)
            if not i_1005 < t_9904:
                break
            b_1003.append_safe(' ')
            b_1003.append_safe(list_get_10948(this_232.conditions_983, i_1005).keyword())
            b_1003.append_safe(' ')
            b_1003.append_fragment(list_get_10948(this_232.conditions_983, i_1005).condition)
            i_1005 = int_add_10949(i_1005, 1)
        lv_1006: 'Union40[int31, None]' = this_232.limit_val_984
        if not lv_1006 is None:
            lv_1954: 'int31' = lv_1006
            b_1003.append_safe(' LIMIT ')
            b_1003.append_int32(lv_1954)
        return b_1003.accumulated
    def __init__(this_404, table_name_1008: 'SafeIdentifier', set_clauses_1009: 'Sequence29[SetClause]', conditions_1010: 'Sequence29[WhereClause]', limit_val_1011: 'Union40[int31, None]') -> None:
        this_404.table_name_981 = table_name_1008
        this_404.set_clauses_982 = set_clauses_1009
        this_404.conditions_983 = conditions_1010
        this_404.limit_val_984 = limit_val_1011
    @property
    def table_name(this_1624) -> 'SafeIdentifier':
        return this_1624.table_name_981
    @property
    def set_clauses(this_1627) -> 'Sequence29[SetClause]':
        return this_1627.set_clauses_982
    @property
    def conditions(this_1630) -> 'Sequence29[WhereClause]':
        return this_1630.conditions_983
    @property
    def limit_val(this_1633) -> 'Union40[int31, None]':
        return this_1633.limit_val_984
class DeleteQuery:
    table_name_1012: 'SafeIdentifier'
    conditions_1013: 'Sequence29[WhereClause]'
    limit_val_1014: 'Union40[int31, None]'
    __slots__ = ('table_name_1012', 'conditions_1013', 'limit_val_1014')
    def where(this_233, condition_1016: 'SqlFragment') -> 'DeleteQuery':
        nb_1018: 'MutableSequence36[WhereClause]' = list_10936(this_233.conditions_1013)
        nb_1018.append(AndCondition(condition_1016))
        return DeleteQuery(this_233.table_name_1012, tuple_10939(nb_1018), this_233.limit_val_1014)
    def or_where(this_234, condition_1020: 'SqlFragment') -> 'DeleteQuery':
        nb_1022: 'MutableSequence36[WhereClause]' = list_10936(this_234.conditions_1013)
        nb_1022.append(OrCondition(condition_1020))
        return DeleteQuery(this_234.table_name_1012, tuple_10939(nb_1022), this_234.limit_val_1014)
    def limit(this_235, n_1024: 'int31') -> 'DeleteQuery':
        if n_1024 < 0:
            raise RuntimeError30()
        return DeleteQuery(this_235.table_name_1012, this_235.conditions_1013, n_1024)
    def to_sql(this_236) -> 'SqlFragment':
        t_9850: 'int31'
        if not this_236.conditions_1013:
            raise RuntimeError30()
        b_1028: 'SqlBuilder' = SqlBuilder()
        b_1028.append_safe('DELETE FROM ')
        b_1028.append_safe(this_236.table_name_1012.sql_value)
        b_1028.append_safe(' WHERE ')
        b_1028.append_fragment(list_get_10948(this_236.conditions_1013, 0).condition)
        i_1029: 'int31' = 1
        while True:
            t_9850 = len_10940(this_236.conditions_1013)
            if not i_1029 < t_9850:
                break
            b_1028.append_safe(' ')
            b_1028.append_safe(list_get_10948(this_236.conditions_1013, i_1029).keyword())
            b_1028.append_safe(' ')
            b_1028.append_fragment(list_get_10948(this_236.conditions_1013, i_1029).condition)
            i_1029 = int_add_10949(i_1029, 1)
        lv_1030: 'Union40[int31, None]' = this_236.limit_val_1014
        if not lv_1030 is None:
            lv_1955: 'int31' = lv_1030
            b_1028.append_safe(' LIMIT ')
            b_1028.append_int32(lv_1955)
        return b_1028.accumulated
    def __init__(this_414, table_name_1032: 'SafeIdentifier', conditions_1033: 'Sequence29[WhereClause]', limit_val_1034: 'Union40[int31, None]') -> None:
        this_414.table_name_1012 = table_name_1032
        this_414.conditions_1013 = conditions_1033
        this_414.limit_val_1014 = limit_val_1034
    @property
    def table_name(this_1636) -> 'SafeIdentifier':
        return this_1636.table_name_1012
    @property
    def conditions(this_1639) -> 'Sequence29[WhereClause]':
        return this_1639.conditions_1013
    @property
    def limit_val(this_1642) -> 'Union40[int31, None]':
        return this_1642.limit_val_1014
class SafeIdentifier(metaclass = ABCMeta28):
    pass
class ValidatedIdentifier_238(SafeIdentifier):
    value_1249: 'str27'
    __slots__ = ('value_1249',)
    @property
    def sql_value(this_239) -> 'str27':
        return this_239.value_1249
    def __init__(this_428, value_1253: 'str27') -> None:
        this_428.value_1249 = value_1253
class FieldType(metaclass = ABCMeta28):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_434) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_436) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_438) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_440) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_442) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_444) -> None:
        pass
class FieldDef:
    name_1267: 'SafeIdentifier'
    field_type_1268: 'FieldType'
    nullable_1269: 'bool33'
    __slots__ = ('name_1267', 'field_type_1268', 'nullable_1269')
    def __init__(this_446, name_1271: 'SafeIdentifier', field_type_1272: 'FieldType', nullable_1273: 'bool33') -> None:
        this_446.name_1267 = name_1271
        this_446.field_type_1268 = field_type_1272
        this_446.nullable_1269 = nullable_1273
    @property
    def name(this_1508) -> 'SafeIdentifier':
        return this_1508.name_1267
    @property
    def field_type(this_1511) -> 'FieldType':
        return this_1511.field_type_1268
    @property
    def nullable(this_1514) -> 'bool33':
        return this_1514.nullable_1269
class TableDef:
    table_name_1274: 'SafeIdentifier'
    fields_1275: 'Sequence29[FieldDef]'
    __slots__ = ('table_name_1274', 'fields_1275')
    def field(this_240, name_1277: 'str27') -> 'FieldDef':
        return_451: 'FieldDef'
        with Label35() as fn_1278:
            this_6482: 'Sequence29[FieldDef]' = this_240.fields_1275
            n_6483: 'int31' = len_10940(this_6482)
            i_6484: 'int31' = 0
            while i_6484 < n_6483:
                el_6485: 'FieldDef' = list_get_10948(this_6482, i_6484)
                i_6484 = int_add_10949(i_6484, 1)
                f_1279: 'FieldDef' = el_6485
                if f_1279.name.sql_value == name_1277:
                    return_451 = f_1279
                    fn_1278.break_()
            raise RuntimeError30()
        return return_451
    def __init__(this_448, table_name_1281: 'SafeIdentifier', fields_1282: 'Sequence29[FieldDef]') -> None:
        this_448.table_name_1274 = table_name_1281
        this_448.fields_1275 = fields_1282
    @property
    def table_name(this_1517) -> 'SafeIdentifier':
        return this_1517.table_name_1274
    @property
    def fields(this_1520) -> 'Sequence29[FieldDef]':
        return this_1520.fields_1275
T_259 = TypeVar42('T_259', bound = Any41)
class SqlBuilder:
    buffer_1302: 'MutableSequence36[SqlPart]'
    __slots__ = ('buffer_1302',)
    def append_safe(this_241, sql_source_1304: 'str27') -> 'None':
        t_10895: 'SqlSource' = SqlSource(sql_source_1304)
        this_241.buffer_1302.append(t_10895)
    def append_fragment(this_242, fragment_1307: 'SqlFragment') -> 'None':
        t_10893: 'Sequence29[SqlPart]' = fragment_1307.parts
        list_builder_add_all_10952(this_242.buffer_1302, t_10893)
    def append_part(this_243, part_1310: 'SqlPart') -> 'None':
        this_243.buffer_1302.append(part_1310)
    def append_part_list(this_244, values_1313: 'Sequence29[SqlPart]') -> 'None':
        def fn_10889(x_1315: 'SqlPart') -> 'None':
            this_244.append_part(x_1315)
        this_244.append_list_1358(values_1313, fn_10889)
    def append_boolean(this_245, value_1317: 'bool33') -> 'None':
        t_10886: 'SqlBoolean' = SqlBoolean(value_1317)
        this_245.buffer_1302.append(t_10886)
    def append_boolean_list(this_246, values_1320: 'Sequence29[bool33]') -> 'None':
        def fn_10883(x_1322: 'bool33') -> 'None':
            this_246.append_boolean(x_1322)
        this_246.append_list_1358(values_1320, fn_10883)
    def append_date(this_247, value_1324: 'date26') -> 'None':
        t_10880: 'SqlDate' = SqlDate(value_1324)
        this_247.buffer_1302.append(t_10880)
    def append_date_list(this_248, values_1327: 'Sequence29[date26]') -> 'None':
        def fn_10877(x_1329: 'date26') -> 'None':
            this_248.append_date(x_1329)
        this_248.append_list_1358(values_1327, fn_10877)
    def append_float64(this_249, value_1331: 'float38') -> 'None':
        t_10874: 'SqlFloat64' = SqlFloat64(value_1331)
        this_249.buffer_1302.append(t_10874)
    def append_float64_list(this_250, values_1334: 'Sequence29[float38]') -> 'None':
        def fn_10871(x_1336: 'float38') -> 'None':
            this_250.append_float64(x_1336)
        this_250.append_list_1358(values_1334, fn_10871)
    def append_int32(this_251, value_1338: 'int31') -> 'None':
        t_10868: 'SqlInt32' = SqlInt32(value_1338)
        this_251.buffer_1302.append(t_10868)
    def append_int32_list(this_252, values_1341: 'Sequence29[int31]') -> 'None':
        def fn_10865(x_1343: 'int31') -> 'None':
            this_252.append_int32(x_1343)
        this_252.append_list_1358(values_1341, fn_10865)
    def append_int64(this_253, value_1345: 'int64_23') -> 'None':
        t_10862: 'SqlInt64' = SqlInt64(value_1345)
        this_253.buffer_1302.append(t_10862)
    def append_int64_list(this_254, values_1348: 'Sequence29[int64_23]') -> 'None':
        def fn_10859(x_1350: 'int64_23') -> 'None':
            this_254.append_int64(x_1350)
        this_254.append_list_1358(values_1348, fn_10859)
    def append_string(this_255, value_1352: 'str27') -> 'None':
        t_10856: 'SqlString' = SqlString(value_1352)
        this_255.buffer_1302.append(t_10856)
    def append_string_list(this_256, values_1355: 'Sequence29[str27]') -> 'None':
        def fn_10853(x_1357: 'str27') -> 'None':
            this_256.append_string(x_1357)
        this_256.append_list_1358(values_1355, fn_10853)
    def append_list_1358(this_257, values_1359: 'Sequence29[T_259]', append_value_1360: 'Callable43[[T_259], None]') -> 'None':
        t_10848: 'int31'
        t_10850: 'T_259'
        i_1362: 'int31' = 0
        while True:
            t_10848 = len_10940(values_1359)
            if not i_1362 < t_10848:
                break
            if i_1362 > 0:
                this_257.append_safe(', ')
            t_10850 = list_get_10948(values_1359, i_1362)
            append_value_1360(t_10850)
            i_1362 = int_add_10949(i_1362, 1)
    @property
    def accumulated(this_258) -> 'SqlFragment':
        return SqlFragment(tuple_10939(this_258.buffer_1302))
    def __init__(this_453) -> None:
        t_10845: 'MutableSequence36[SqlPart]' = list_10936()
        this_453.buffer_1302 = t_10845
class SqlFragment:
    parts_1369: 'Sequence29[SqlPart]'
    __slots__ = ('parts_1369',)
    def to_source(this_263) -> 'SqlSource':
        return SqlSource(this_263.to_string())
    def to_string(this_264) -> 'str27':
        t_10919: 'int31'
        builder_1374: 'list3[str27]' = ['']
        i_1375: 'int31' = 0
        while True:
            t_10919 = len_10940(this_264.parts_1369)
            if not i_1375 < t_10919:
                break
            list_get_10948(this_264.parts_1369, i_1375).format_to(builder_1374)
            i_1375 = int_add_10949(i_1375, 1)
        return ''.join(builder_1374)
    def __init__(this_474, parts_1377: 'Sequence29[SqlPart]') -> None:
        this_474.parts_1369 = parts_1377
    @property
    def parts(this_1526) -> 'Sequence29[SqlPart]':
        return this_1526.parts_1369
class SqlPart(metaclass = ABCMeta28):
    def format_to(this_265, builder_1379: 'list3[str27]') -> 'None':
        raise RuntimeError30()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_1381: 'str27'
    __slots__ = ('source_1381',)
    def format_to(this_266, builder_1383: 'list3[str27]') -> 'None':
        builder_1383.append(this_266.source_1381)
    def __init__(this_480, source_1386: 'str27') -> None:
        this_480.source_1381 = source_1386
    @property
    def source(this_1523) -> 'str27':
        return this_1523.source_1381
class SqlBoolean(SqlPart):
    value_1387: 'bool33'
    __slots__ = ('value_1387',)
    def format_to(this_267, builder_1389: 'list3[str27]') -> 'None':
        t_6281: 'str27'
        if this_267.value_1387:
            t_6281 = 'TRUE'
        else:
            t_6281 = 'FALSE'
        builder_1389.append(t_6281)
    def __init__(this_483, value_1392: 'bool33') -> None:
        this_483.value_1387 = value_1392
    @property
    def value(this_1529) -> 'bool33':
        return this_1529.value_1387
class SqlDate(SqlPart):
    value_1393: 'date26'
    __slots__ = ('value_1393',)
    def format_to(this_268, builder_1395: 'list3[str27]') -> 'None':
        builder_1395.append("'")
        t_10900: 'str27' = date_to_string_10956(this_268.value_1393)
        def fn_10898(c_1397: 'int31') -> 'None':
            if c_1397 == 39:
                builder_1395.append("''")
            else:
                builder_1395.append(string_from_code_point44(c_1397))
        string_for_each_10958(t_10900, fn_10898)
        builder_1395.append("'")
    def __init__(this_486, value_1399: 'date26') -> None:
        this_486.value_1393 = value_1399
    @property
    def value(this_1544) -> 'date26':
        return this_1544.value_1393
class SqlFloat64(SqlPart):
    value_1400: 'float38'
    __slots__ = ('value_1400',)
    def format_to(this_269, builder_1402: 'list3[str27]') -> 'None':
        t_6270: 'bool33'
        t_6271: 'bool33'
        s_1404: 'str27' = float64_to_string_10959(this_269.value_1400)
        if s_1404 == 'NaN':
            t_6271 = True
        else:
            if s_1404 == 'Infinity':
                t_6270 = True
            else:
                t_6270 = s_1404 == '-Infinity'
            t_6271 = t_6270
        if t_6271:
            builder_1402.append('NULL')
        else:
            builder_1402.append(s_1404)
    def __init__(this_489, value_1406: 'float38') -> None:
        this_489.value_1400 = value_1406
    @property
    def value(this_1541) -> 'float38':
        return this_1541.value_1400
class SqlInt32(SqlPart):
    value_1407: 'int31'
    __slots__ = ('value_1407',)
    def format_to(this_270, builder_1409: 'list3[str27]') -> 'None':
        t_10909: 'str27' = int_to_string_10943(this_270.value_1407)
        builder_1409.append(t_10909)
    def __init__(this_492, value_1412: 'int31') -> None:
        this_492.value_1407 = value_1412
    @property
    def value(this_1535) -> 'int31':
        return this_1535.value_1407
class SqlInt64(SqlPart):
    value_1413: 'int64_23'
    __slots__ = ('value_1413',)
    def format_to(this_271, builder_1415: 'list3[str27]') -> 'None':
        t_10907: 'str27' = int_to_string_10943(this_271.value_1413)
        builder_1415.append(t_10907)
    def __init__(this_495, value_1418: 'int64_23') -> None:
        this_495.value_1413 = value_1418
    @property
    def value(this_1538) -> 'int64_23':
        return this_1538.value_1413
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_1419: 'str27'
    __slots__ = ('value_1419',)
    def format_to(this_272, builder_1421: 'list3[str27]') -> 'None':
        builder_1421.append("'")
        def fn_10912(c_1423: 'int31') -> 'None':
            if c_1423 == 39:
                builder_1421.append("''")
            else:
                builder_1421.append(string_from_code_point44(c_1423))
        string_for_each_10958(this_272.value_1419, fn_10912)
        builder_1421.append("'")
    def __init__(this_498, value_1425: 'str27') -> None:
        this_498.value_1419 = value_1425
    @property
    def value(this_1532) -> 'str27':
        return this_1532.value_1419
def changeset(table_def_645: 'TableDef', params_646: 'MappingProxyType32[str27, str27]') -> 'Changeset':
    t_10695: 'MappingProxyType32[str27, str27]' = map_constructor_10960(())
    return ChangesetImpl_174(table_def_645, params_646, t_10695, (), True)
def is_ident_start_506(c_1254: 'int31') -> 'bool33':
    return_431: 'bool33'
    t_6044: 'bool33'
    t_6045: 'bool33'
    if c_1254 >= 97:
        t_6044 = c_1254 <= 122
    else:
        t_6044 = False
    if t_6044:
        return_431 = True
    else:
        if c_1254 >= 65:
            t_6045 = c_1254 <= 90
        else:
            t_6045 = False
        if t_6045:
            return_431 = True
        else:
            return_431 = c_1254 == 95
    return return_431
def is_ident_part_507(c_1256: 'int31') -> 'bool33':
    return_432: 'bool33'
    if is_ident_start_506(c_1256):
        return_432 = True
    elif c_1256 >= 48:
        return_432 = c_1256 <= 57
    else:
        return_432 = False
    return return_432
def safe_identifier(name_1258: 'str27') -> 'SafeIdentifier':
    t_10693: 'int31'
    if not name_1258:
        raise RuntimeError30()
    idx_1260: 'int31' = 0
    if not is_ident_start_506(string_get_10961(name_1258, idx_1260)):
        raise RuntimeError30()
    t_10690: 'int31' = string_next_10962(name_1258, idx_1260)
    idx_1260 = t_10690
    while True:
        if not len6(name_1258) > idx_1260:
            break
        if not is_ident_part_507(string_get_10961(name_1258, idx_1260)):
            raise RuntimeError30()
        t_10693 = string_next_10962(name_1258, idx_1260)
        idx_1260 = t_10693
    return ValidatedIdentifier_238(name_1258)
def delete_sql(table_def_735: 'TableDef', id_736: 'int31') -> 'SqlFragment':
    b_738: 'SqlBuilder' = SqlBuilder()
    b_738.append_safe('DELETE FROM ')
    b_738.append_safe(table_def_735.table_name.sql_value)
    b_738.append_safe(' WHERE id = ')
    b_738.append_int32(id_736)
    return b_738.accumulated
def from_(table_name_930: 'SafeIdentifier') -> 'Query':
    return Query(table_name_930, (), (), (), None, None, (), (), (), False, ())
def col(table_932: 'SafeIdentifier', column_933: 'SafeIdentifier') -> 'SqlFragment':
    b_935: 'SqlBuilder' = SqlBuilder()
    b_935.append_safe(table_932.sql_value)
    b_935.append_safe('.')
    b_935.append_safe(column_933.sql_value)
    return b_935.accumulated
def count_all() -> 'SqlFragment':
    b_937: 'SqlBuilder' = SqlBuilder()
    b_937.append_safe('COUNT(*)')
    return b_937.accumulated
def count_col(field_938: 'SafeIdentifier') -> 'SqlFragment':
    b_940: 'SqlBuilder' = SqlBuilder()
    b_940.append_safe('COUNT(')
    b_940.append_safe(field_938.sql_value)
    b_940.append_safe(')')
    return b_940.accumulated
def sum_col(field_941: 'SafeIdentifier') -> 'SqlFragment':
    b_943: 'SqlBuilder' = SqlBuilder()
    b_943.append_safe('SUM(')
    b_943.append_safe(field_941.sql_value)
    b_943.append_safe(')')
    return b_943.accumulated
def avg_col(field_944: 'SafeIdentifier') -> 'SqlFragment':
    b_946: 'SqlBuilder' = SqlBuilder()
    b_946.append_safe('AVG(')
    b_946.append_safe(field_944.sql_value)
    b_946.append_safe(')')
    return b_946.accumulated
def min_col(field_947: 'SafeIdentifier') -> 'SqlFragment':
    b_949: 'SqlBuilder' = SqlBuilder()
    b_949.append_safe('MIN(')
    b_949.append_safe(field_947.sql_value)
    b_949.append_safe(')')
    return b_949.accumulated
def max_col(field_950: 'SafeIdentifier') -> 'SqlFragment':
    b_952: 'SqlBuilder' = SqlBuilder()
    b_952.append_safe('MAX(')
    b_952.append_safe(field_950.sql_value)
    b_952.append_safe(')')
    return b_952.accumulated
def union_sql(a_953: 'Query', b_954: 'Query') -> 'SqlFragment':
    sb_956: 'SqlBuilder' = SqlBuilder()
    sb_956.append_safe('(')
    sb_956.append_fragment(a_953.to_sql())
    sb_956.append_safe(') UNION (')
    sb_956.append_fragment(b_954.to_sql())
    sb_956.append_safe(')')
    return sb_956.accumulated
def union_all_sql(a_957: 'Query', b_958: 'Query') -> 'SqlFragment':
    sb_960: 'SqlBuilder' = SqlBuilder()
    sb_960.append_safe('(')
    sb_960.append_fragment(a_957.to_sql())
    sb_960.append_safe(') UNION ALL (')
    sb_960.append_fragment(b_958.to_sql())
    sb_960.append_safe(')')
    return sb_960.accumulated
def intersect_sql(a_961: 'Query', b_962: 'Query') -> 'SqlFragment':
    sb_964: 'SqlBuilder' = SqlBuilder()
    sb_964.append_safe('(')
    sb_964.append_fragment(a_961.to_sql())
    sb_964.append_safe(') INTERSECT (')
    sb_964.append_fragment(b_962.to_sql())
    sb_964.append_safe(')')
    return sb_964.accumulated
def except_sql(a_965: 'Query', b_966: 'Query') -> 'SqlFragment':
    sb_968: 'SqlBuilder' = SqlBuilder()
    sb_968.append_safe('(')
    sb_968.append_fragment(a_965.to_sql())
    sb_968.append_safe(') EXCEPT (')
    sb_968.append_fragment(b_966.to_sql())
    sb_968.append_safe(')')
    return sb_968.accumulated
def subquery(q_969: 'Query', alias_970: 'SafeIdentifier') -> 'SqlFragment':
    b_972: 'SqlBuilder' = SqlBuilder()
    b_972.append_safe('(')
    b_972.append_fragment(q_969.to_sql())
    b_972.append_safe(') AS ')
    b_972.append_safe(alias_970.sql_value)
    return b_972.accumulated
def exists_sql(q_973: 'Query') -> 'SqlFragment':
    b_975: 'SqlBuilder' = SqlBuilder()
    b_975.append_safe('EXISTS (')
    b_975.append_fragment(q_973.to_sql())
    b_975.append_safe(')')
    return b_975.accumulated
def update(table_name_1035: 'SafeIdentifier') -> 'UpdateQuery':
    return UpdateQuery(table_name_1035, (), (), None)
def delete_from(table_name_1037: 'SafeIdentifier') -> 'DeleteQuery':
    return DeleteQuery(table_name_1037, (), None)
