from builtins import str as str27, RuntimeError as RuntimeError30, int as int31, bool as bool33, Exception as Exception37, float as float38, isinstance as isinstance39, list as list3, len as len6, tuple as tuple5
from abc import ABCMeta as ABCMeta28
from typing import Sequence as Sequence29, Dict as Dict34, MutableSequence as MutableSequence36, Union as Union40, Any as Any41, TypeVar as TypeVar42, Callable as Callable43
from types import MappingProxyType as MappingProxyType32
from temper_core import Label as Label35, Pair as Pair25, string_from_code_point as string_from_code_point44, map_builder_set as map_builder_set0, list_for_each as list_for_each1, mapped_to_map as mapped_to_map2, mapped_has as mapped_has4, string_count_between as string_count_between7, str_cat as str_cat8, int_to_string as int_to_string9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, date_from_iso_string as date_from_iso_string13, list_get as list_get14, int_add as int_add15, mapped_to_list as mapped_to_list16, list_join as list_join17, list_builder_add_all as list_builder_add_all18, date_to_string as date_to_string19, string_for_each as string_for_each20, float64_to_string as float64_to_string21, map_constructor as map_constructor22, string_get as string_get23, string_next as string_next24
from datetime import date as date26
map_builder_set_11459 = map_builder_set0
list_for_each_11460 = list_for_each1
mapped_to_map_11461 = mapped_to_map2
list_11462 = list3
mapped_has_11463 = mapped_has4
tuple_11465 = tuple5
len_11466 = len6
string_count_between_11467 = string_count_between7
str_cat_11468 = str_cat8
int_to_string_11469 = int_to_string9
string_to_int32_11470 = string_to_int3210
string_to_int64_11471 = string_to_int6411
string_to_float64_11472 = string_to_float6412
date_from_iso_string_11473 = date_from_iso_string13
list_get_11474 = list_get14
int_add_11475 = int_add15
mapped_to_list_11476 = mapped_to_list16
list_join_11477 = list_join17
list_builder_add_all_11478 = list_builder_add_all18
date_to_string_11482 = date_to_string19
string_for_each_11484 = string_for_each20
float64_to_string_11485 = float64_to_string21
map_constructor_11486 = map_constructor22
string_get_11487 = string_get23
string_next_11488 = string_next24
pair_11490 = Pair25
date_11493 = date26
class ChangesetError:
    field_551: 'str27'
    message_552: 'str27'
    __slots__ = ('field_551', 'message_552')
    def __init__(this_291, field_554: 'str27', message_555: 'str27') -> None:
        this_291.field_551 = field_554
        this_291.message_552 = message_555
    @property
    def field(this_1601) -> 'str27':
        return this_1601.field_551
    @property
    def message(this_1604) -> 'str27':
        return this_1604.message_552
class Changeset(metaclass = ABCMeta28):
    def cast(this_173, allowed_fields_565: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_required(this_174, fields_568: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError30()
    def validate_length(this_175, field_571: 'SafeIdentifier', min_572: 'int31', max_573: 'int31') -> 'Changeset':
        raise RuntimeError30()
    def validate_int(this_176, field_576: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_int64(this_177, field_579: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_float(this_178, field_582: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def validate_bool(this_179, field_585: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError30()
    def to_insert_sql(this_180) -> 'SqlFragment':
        raise RuntimeError30()
    def to_update_sql(this_181, id_590: 'int31') -> 'SqlFragment':
        raise RuntimeError30()
class ChangesetImpl_182(Changeset):
    table_def_592: 'TableDef'
    params_593: 'MappingProxyType32[str27, str27]'
    changes_594: 'MappingProxyType32[str27, str27]'
    errors_595: 'Sequence29[ChangesetError]'
    is_valid_596: 'bool33'
    __slots__ = ('table_def_592', 'params_593', 'changes_594', 'errors_595', 'is_valid_596')
    @property
    def table_def(this_183) -> 'TableDef':
        return this_183.table_def_592
    @property
    def changes(this_184) -> 'MappingProxyType32[str27, str27]':
        return this_184.changes_594
    @property
    def errors(this_185) -> 'Sequence29[ChangesetError]':
        return this_185.errors_595
    @property
    def is_valid(this_186) -> 'bool33':
        return this_186.is_valid_596
    def cast(this_187, allowed_fields_606: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        mb_608: 'Dict34[str27, str27]' = {}
        def fn_11363(f_609: 'SafeIdentifier') -> 'None':
            t_11361: 'str27'
            t_11358: 'str27' = f_609.sql_value
            val_610: 'str27' = this_187.params_593.get(t_11358, '')
            if not (not val_610):
                t_11361 = f_609.sql_value
                map_builder_set_11459(mb_608, t_11361, val_610)
        list_for_each_11460(allowed_fields_606, fn_11363)
        return ChangesetImpl_182(this_187.table_def_592, this_187.params_593, mapped_to_map_11461(mb_608), this_187.errors_595, this_187.is_valid_596)
    def validate_required(this_188, fields_612: 'Sequence29[SafeIdentifier]') -> 'Changeset':
        return_324: 'Changeset'
        t_11356: 'Sequence29[ChangesetError]'
        t_6537: 'TableDef'
        t_6538: 'MappingProxyType32[str27, str27]'
        t_6539: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_613:
            if not this_188.is_valid_596:
                return_324 = this_188
                fn_613.break_()
            eb_614: 'MutableSequence36[ChangesetError]' = list_11462(this_188.errors_595)
            valid_615: 'bool33' = True
            def fn_11352(f_616: 'SafeIdentifier') -> 'None':
                nonlocal valid_615
                t_11350: 'ChangesetError'
                t_11347: 'str27' = f_616.sql_value
                if not mapped_has_11463(this_188.changes_594, t_11347):
                    t_11350 = ChangesetError(f_616.sql_value, 'is required')
                    eb_614.append(t_11350)
                    valid_615 = False
            list_for_each_11460(fields_612, fn_11352)
            t_6537 = this_188.table_def_592
            t_6538 = this_188.params_593
            t_6539 = this_188.changes_594
            t_11356 = tuple_11465(eb_614)
            return_324 = ChangesetImpl_182(t_6537, t_6538, t_6539, t_11356, valid_615)
        return return_324
    def validate_length(this_189, field_618: 'SafeIdentifier', min_619: 'int31', max_620: 'int31') -> 'Changeset':
        return_325: 'Changeset'
        t_11334: 'str27'
        t_11345: 'Sequence29[ChangesetError]'
        t_6520: 'bool33'
        t_6526: 'TableDef'
        t_6527: 'MappingProxyType32[str27, str27]'
        t_6528: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_621:
            if not this_189.is_valid_596:
                return_325 = this_189
                fn_621.break_()
            t_11334 = field_618.sql_value
            val_622: 'str27' = this_189.changes_594.get(t_11334, '')
            len_623: 'int31' = string_count_between_11467(val_622, 0, len_11466(val_622))
            if len_623 < min_619:
                t_6520 = True
            else:
                t_6520 = len_623 > max_620
            if t_6520:
                msg_624: 'str27' = str_cat_11468('must be between ', int_to_string_11469(min_619), ' and ', int_to_string_11469(max_620), ' characters')
                eb_625: 'MutableSequence36[ChangesetError]' = list_11462(this_189.errors_595)
                eb_625.append(ChangesetError(field_618.sql_value, msg_624))
                t_6526 = this_189.table_def_592
                t_6527 = this_189.params_593
                t_6528 = this_189.changes_594
                t_11345 = tuple_11465(eb_625)
                return_325 = ChangesetImpl_182(t_6526, t_6527, t_6528, t_11345, False)
                fn_621.break_()
            return_325 = this_189
        return return_325
    def validate_int(this_190, field_627: 'SafeIdentifier') -> 'Changeset':
        return_326: 'Changeset'
        t_11325: 'str27'
        t_11332: 'Sequence29[ChangesetError]'
        t_6511: 'TableDef'
        t_6512: 'MappingProxyType32[str27, str27]'
        t_6513: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_628:
            if not this_190.is_valid_596:
                return_326 = this_190
                fn_628.break_()
            t_11325 = field_627.sql_value
            val_629: 'str27' = this_190.changes_594.get(t_11325, '')
            if not val_629:
                return_326 = this_190
                fn_628.break_()
            parse_ok_630: 'bool33'
            try:
                string_to_int32_11470(val_629)
                parse_ok_630 = True
            except Exception37:
                parse_ok_630 = False
            if not parse_ok_630:
                eb_631: 'MutableSequence36[ChangesetError]' = list_11462(this_190.errors_595)
                eb_631.append(ChangesetError(field_627.sql_value, 'must be an integer'))
                t_6511 = this_190.table_def_592
                t_6512 = this_190.params_593
                t_6513 = this_190.changes_594
                t_11332 = tuple_11465(eb_631)
                return_326 = ChangesetImpl_182(t_6511, t_6512, t_6513, t_11332, False)
                fn_628.break_()
            return_326 = this_190
        return return_326
    def validate_int64(this_191, field_633: 'SafeIdentifier') -> 'Changeset':
        return_327: 'Changeset'
        t_11316: 'str27'
        t_11323: 'Sequence29[ChangesetError]'
        t_6498: 'TableDef'
        t_6499: 'MappingProxyType32[str27, str27]'
        t_6500: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_634:
            if not this_191.is_valid_596:
                return_327 = this_191
                fn_634.break_()
            t_11316 = field_633.sql_value
            val_635: 'str27' = this_191.changes_594.get(t_11316, '')
            if not val_635:
                return_327 = this_191
                fn_634.break_()
            parse_ok_636: 'bool33'
            try:
                string_to_int64_11471(val_635)
                parse_ok_636 = True
            except Exception37:
                parse_ok_636 = False
            if not parse_ok_636:
                eb_637: 'MutableSequence36[ChangesetError]' = list_11462(this_191.errors_595)
                eb_637.append(ChangesetError(field_633.sql_value, 'must be a 64-bit integer'))
                t_6498 = this_191.table_def_592
                t_6499 = this_191.params_593
                t_6500 = this_191.changes_594
                t_11323 = tuple_11465(eb_637)
                return_327 = ChangesetImpl_182(t_6498, t_6499, t_6500, t_11323, False)
                fn_634.break_()
            return_327 = this_191
        return return_327
    def validate_float(this_192, field_639: 'SafeIdentifier') -> 'Changeset':
        return_328: 'Changeset'
        t_11307: 'str27'
        t_11314: 'Sequence29[ChangesetError]'
        t_6485: 'TableDef'
        t_6486: 'MappingProxyType32[str27, str27]'
        t_6487: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_640:
            if not this_192.is_valid_596:
                return_328 = this_192
                fn_640.break_()
            t_11307 = field_639.sql_value
            val_641: 'str27' = this_192.changes_594.get(t_11307, '')
            if not val_641:
                return_328 = this_192
                fn_640.break_()
            parse_ok_642: 'bool33'
            try:
                string_to_float64_11472(val_641)
                parse_ok_642 = True
            except Exception37:
                parse_ok_642 = False
            if not parse_ok_642:
                eb_643: 'MutableSequence36[ChangesetError]' = list_11462(this_192.errors_595)
                eb_643.append(ChangesetError(field_639.sql_value, 'must be a number'))
                t_6485 = this_192.table_def_592
                t_6486 = this_192.params_593
                t_6487 = this_192.changes_594
                t_11314 = tuple_11465(eb_643)
                return_328 = ChangesetImpl_182(t_6485, t_6486, t_6487, t_11314, False)
                fn_640.break_()
            return_328 = this_192
        return return_328
    def validate_bool(this_193, field_645: 'SafeIdentifier') -> 'Changeset':
        return_329: 'Changeset'
        t_11298: 'str27'
        t_11305: 'Sequence29[ChangesetError]'
        t_6460: 'bool33'
        t_6461: 'bool33'
        t_6463: 'bool33'
        t_6464: 'bool33'
        t_6466: 'bool33'
        t_6472: 'TableDef'
        t_6473: 'MappingProxyType32[str27, str27]'
        t_6474: 'MappingProxyType32[str27, str27]'
        with Label35() as fn_646:
            if not this_193.is_valid_596:
                return_329 = this_193
                fn_646.break_()
            t_11298 = field_645.sql_value
            val_647: 'str27' = this_193.changes_594.get(t_11298, '')
            if not val_647:
                return_329 = this_193
                fn_646.break_()
            is_true_648: 'bool33'
            if val_647 == 'true':
                is_true_648 = True
            else:
                if val_647 == '1':
                    t_6461 = True
                else:
                    if val_647 == 'yes':
                        t_6460 = True
                    else:
                        t_6460 = val_647 == 'on'
                    t_6461 = t_6460
                is_true_648 = t_6461
            is_false_649: 'bool33'
            if val_647 == 'false':
                is_false_649 = True
            else:
                if val_647 == '0':
                    t_6464 = True
                else:
                    if val_647 == 'no':
                        t_6463 = True
                    else:
                        t_6463 = val_647 == 'off'
                    t_6464 = t_6463
                is_false_649 = t_6464
            if not is_true_648:
                t_6466 = not is_false_649
            else:
                t_6466 = False
            if t_6466:
                eb_650: 'MutableSequence36[ChangesetError]' = list_11462(this_193.errors_595)
                eb_650.append(ChangesetError(field_645.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)'))
                t_6472 = this_193.table_def_592
                t_6473 = this_193.params_593
                t_6474 = this_193.changes_594
                t_11305 = tuple_11465(eb_650)
                return_329 = ChangesetImpl_182(t_6472, t_6473, t_6474, t_11305, False)
                fn_646.break_()
            return_329 = this_193
        return return_329
    def parse_bool_sql_part_651(this_194, val_652: 'str27') -> 'SqlBoolean':
        return_330: 'SqlBoolean'
        t_6449: 'bool33'
        t_6450: 'bool33'
        t_6451: 'bool33'
        t_6453: 'bool33'
        t_6454: 'bool33'
        t_6455: 'bool33'
        with Label35() as fn_653:
            if val_652 == 'true':
                t_6451 = True
            else:
                if val_652 == '1':
                    t_6450 = True
                else:
                    if val_652 == 'yes':
                        t_6449 = True
                    else:
                        t_6449 = val_652 == 'on'
                    t_6450 = t_6449
                t_6451 = t_6450
            if t_6451:
                return_330 = SqlBoolean(True)
                fn_653.break_()
            if val_652 == 'false':
                t_6455 = True
            else:
                if val_652 == '0':
                    t_6454 = True
                else:
                    if val_652 == 'no':
                        t_6453 = True
                    else:
                        t_6453 = val_652 == 'off'
                    t_6454 = t_6453
                t_6455 = t_6454
            if t_6455:
                return_330 = SqlBoolean(False)
                fn_653.break_()
            raise RuntimeError30()
        return return_330
    def value_to_sql_part_654(this_195, field_def_655: 'FieldDef', val_656: 'str27') -> 'SqlPart':
        return_331: 'SqlPart'
        t_6436: 'int31'
        t_6439: 'int64_23'
        t_6442: 'float38'
        t_6447: 'date26'
        with Label35() as fn_657:
            ft_658: 'FieldType' = field_def_655.field_type
            if isinstance39(ft_658, StringField):
                return_331 = SqlString(val_656)
                fn_657.break_()
            if isinstance39(ft_658, IntField):
                t_6436 = string_to_int32_11470(val_656)
                return_331 = SqlInt32(t_6436)
                fn_657.break_()
            if isinstance39(ft_658, Int64Field):
                t_6439 = string_to_int64_11471(val_656)
                return_331 = SqlInt64(t_6439)
                fn_657.break_()
            if isinstance39(ft_658, FloatField):
                t_6442 = string_to_float64_11472(val_656)
                return_331 = SqlFloat64(t_6442)
                fn_657.break_()
            if isinstance39(ft_658, BoolField):
                return_331 = this_195.parse_bool_sql_part_651(val_656)
                fn_657.break_()
            if isinstance39(ft_658, DateField):
                t_6447 = date_from_iso_string_11473(val_656)
                return_331 = SqlDate(t_6447)
                fn_657.break_()
            raise RuntimeError30()
        return return_331
    def to_insert_sql(this_196) -> 'SqlFragment':
        t_11246: 'int31'
        t_11251: 'str27'
        t_11252: 'bool33'
        t_11257: 'int31'
        t_11259: 'str27'
        t_11263: 'str27'
        t_11278: 'int31'
        t_6400: 'bool33'
        t_6408: 'FieldDef'
        t_6413: 'SqlPart'
        if not this_196.is_valid_596:
            raise RuntimeError30()
        i_661: 'int31' = 0
        while True:
            t_11246 = len_11466(this_196.table_def_592.fields)
            if not i_661 < t_11246:
                break
            f_662: 'FieldDef' = list_get_11474(this_196.table_def_592.fields, i_661)
            if not f_662.nullable:
                t_11251 = f_662.name.sql_value
                t_11252 = mapped_has_11463(this_196.changes_594, t_11251)
                t_6400 = not t_11252
            else:
                t_6400 = False
            if t_6400:
                raise RuntimeError30()
            i_661 = int_add_11475(i_661, 1)
        pairs_663: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_11476(this_196.changes_594)
        if len_11466(pairs_663) == 0:
            raise RuntimeError30()
        col_names_664: 'MutableSequence36[str27]' = list_11462()
        val_parts_665: 'MutableSequence36[SqlPart]' = list_11462()
        i_666: 'int31' = 0
        while True:
            t_11257 = len_11466(pairs_663)
            if not i_666 < t_11257:
                break
            pair_667: 'Pair25[str27, str27]' = list_get_11474(pairs_663, i_666)
            t_11259 = pair_667.key
            t_6408 = this_196.table_def_592.field(t_11259)
            fd_668: 'FieldDef' = t_6408
            col_names_664.append(fd_668.name.sql_value)
            t_11263 = pair_667.value
            t_6413 = this_196.value_to_sql_part_654(fd_668, t_11263)
            val_parts_665.append(t_6413)
            i_666 = int_add_11475(i_666, 1)
        b_669: 'SqlBuilder' = SqlBuilder()
        b_669.append_safe('INSERT INTO ')
        b_669.append_safe(this_196.table_def_592.table_name.sql_value)
        b_669.append_safe(' (')
        t_11271: 'Sequence29[str27]' = tuple_11465(col_names_664)
        def fn_11244(c_670: 'str27') -> 'str27':
            return c_670
        b_669.append_safe(list_join_11477(t_11271, ', ', fn_11244))
        b_669.append_safe(') VALUES (')
        b_669.append_part(list_get_11474(val_parts_665, 0))
        j_671: 'int31' = 1
        while True:
            t_11278 = len_11466(val_parts_665)
            if not j_671 < t_11278:
                break
            b_669.append_safe(', ')
            b_669.append_part(list_get_11474(val_parts_665, j_671))
            j_671 = int_add_11475(j_671, 1)
        b_669.append_safe(')')
        return b_669.accumulated
    def to_update_sql(this_197, id_673: 'int31') -> 'SqlFragment':
        t_11231: 'int31'
        t_11234: 'str27'
        t_11239: 'str27'
        t_6381: 'FieldDef'
        t_6387: 'SqlPart'
        if not this_197.is_valid_596:
            raise RuntimeError30()
        pairs_675: 'Sequence29[(Pair25[str27, str27])]' = mapped_to_list_11476(this_197.changes_594)
        if len_11466(pairs_675) == 0:
            raise RuntimeError30()
        b_676: 'SqlBuilder' = SqlBuilder()
        b_676.append_safe('UPDATE ')
        b_676.append_safe(this_197.table_def_592.table_name.sql_value)
        b_676.append_safe(' SET ')
        i_677: 'int31' = 0
        while True:
            t_11231 = len_11466(pairs_675)
            if not i_677 < t_11231:
                break
            if i_677 > 0:
                b_676.append_safe(', ')
            pair_678: 'Pair25[str27, str27]' = list_get_11474(pairs_675, i_677)
            t_11234 = pair_678.key
            t_6381 = this_197.table_def_592.field(t_11234)
            fd_679: 'FieldDef' = t_6381
            b_676.append_safe(fd_679.name.sql_value)
            b_676.append_safe(' = ')
            t_11239 = pair_678.value
            t_6387 = this_197.value_to_sql_part_654(fd_679, t_11239)
            b_676.append_part(t_6387)
            i_677 = int_add_11475(i_677, 1)
        b_676.append_safe(' WHERE id = ')
        b_676.append_int32(id_673)
        return b_676.accumulated
    def __init__(this_314, table_def_681: 'TableDef', params_682: 'MappingProxyType32[str27, str27]', changes_683: 'MappingProxyType32[str27, str27]', errors_684: 'Sequence29[ChangesetError]', is_valid_685: 'bool33') -> None:
        this_314.table_def_592 = table_def_681
        this_314.params_593 = params_682
        this_314.changes_594 = changes_683
        this_314.errors_595 = errors_684
        this_314.is_valid_596 = is_valid_685
class JoinType(metaclass = ABCMeta28):
    def keyword(this_198) -> 'str27':
        raise RuntimeError30()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_199) -> 'str27':
        return 'INNER JOIN'
    def __init__(this_339) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_200) -> 'str27':
        return 'LEFT JOIN'
    def __init__(this_342) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_201) -> 'str27':
        return 'RIGHT JOIN'
    def __init__(this_345) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_202) -> 'str27':
        return 'FULL OUTER JOIN'
    def __init__(this_348) -> None:
        pass
class CrossJoin(JoinType):
    __slots__ = ()
    def keyword(this_203) -> 'str27':
        return 'CROSS JOIN'
    def __init__(this_351) -> None:
        pass
class JoinClause:
    join_type_797: 'JoinType'
    table_798: 'SafeIdentifier'
    on_condition_799: 'Union40[SqlFragment, None]'
    __slots__ = ('join_type_797', 'table_798', 'on_condition_799')
    def __init__(this_354, join_type_801: 'JoinType', table_802: 'SafeIdentifier', on_condition_803: 'Union40[SqlFragment, None]') -> None:
        this_354.join_type_797 = join_type_801
        this_354.table_798 = table_802
        this_354.on_condition_799 = on_condition_803
    @property
    def join_type(this_1669) -> 'JoinType':
        return this_1669.join_type_797
    @property
    def table(this_1672) -> 'SafeIdentifier':
        return this_1672.table_798
    @property
    def on_condition(this_1675) -> 'Union40[SqlFragment, None]':
        return this_1675.on_condition_799
class NullsPosition(metaclass = ABCMeta28):
    def keyword(this_204) -> 'str27':
        raise RuntimeError30()
class NullsFirst(NullsPosition):
    __slots__ = ()
    def keyword(this_205) -> 'str27':
        return ' NULLS FIRST'
    def __init__(this_358) -> None:
        pass
class NullsLast(NullsPosition):
    __slots__ = ()
    def keyword(this_206) -> 'str27':
        return ' NULLS LAST'
    def __init__(this_361) -> None:
        pass
class OrderClause:
    field_812: 'SafeIdentifier'
    ascending_813: 'bool33'
    nulls_pos_814: 'Union40[NullsPosition, None]'
    __slots__ = ('field_812', 'ascending_813', 'nulls_pos_814')
    def __init__(this_364, field_816: 'SafeIdentifier', ascending_817: 'bool33', nulls_pos_818: 'Union40[NullsPosition, None]') -> None:
        this_364.field_812 = field_816
        this_364.ascending_813 = ascending_817
        this_364.nulls_pos_814 = nulls_pos_818
    @property
    def field(this_1678) -> 'SafeIdentifier':
        return this_1678.field_812
    @property
    def ascending(this_1681) -> 'bool33':
        return this_1681.ascending_813
    @property
    def nulls_pos(this_1684) -> 'Union40[NullsPosition, None]':
        return this_1684.nulls_pos_814
class LockMode(metaclass = ABCMeta28):
    def keyword(this_207) -> 'str27':
        raise RuntimeError30()
class ForUpdate(LockMode):
    __slots__ = ()
    def keyword(this_208) -> 'str27':
        return ' FOR UPDATE'
    def __init__(this_368) -> None:
        pass
class ForShare(LockMode):
    __slots__ = ()
    def keyword(this_209) -> 'str27':
        return ' FOR SHARE'
    def __init__(this_371) -> None:
        pass
class WhereClause(metaclass = ABCMeta28):
    def keyword(this_211) -> 'str27':
        raise RuntimeError30()
class AndCondition(WhereClause):
    condition_831: 'SqlFragment'
    __slots__ = ('condition_831',)
    @property
    def condition(this_212) -> 'SqlFragment':
        return this_212.condition_831
    def keyword(this_213) -> 'str27':
        return 'AND'
    def __init__(this_378, condition_837: 'SqlFragment') -> None:
        this_378.condition_831 = condition_837
class OrCondition(WhereClause):
    condition_838: 'SqlFragment'
    __slots__ = ('condition_838',)
    @property
    def condition(this_214) -> 'SqlFragment':
        return this_214.condition_838
    def keyword(this_215) -> 'str27':
        return 'OR'
    def __init__(this_383, condition_844: 'SqlFragment') -> None:
        this_383.condition_838 = condition_844
class Query:
    table_name_845: 'SafeIdentifier'
    conditions_846: 'Sequence29[WhereClause]'
    selected_fields_847: 'Sequence29[SafeIdentifier]'
    order_clauses_848: 'Sequence29[OrderClause]'
    limit_val_849: 'Union40[int31, None]'
    offset_val_850: 'Union40[int31, None]'
    join_clauses_851: 'Sequence29[JoinClause]'
    group_by_fields_852: 'Sequence29[SafeIdentifier]'
    having_conditions_853: 'Sequence29[WhereClause]'
    is_distinct_854: 'bool33'
    select_exprs_855: 'Sequence29[SqlFragment]'
    lock_mode_856: 'Union40[LockMode, None]'
    __slots__ = ('table_name_845', 'conditions_846', 'selected_fields_847', 'order_clauses_848', 'limit_val_849', 'offset_val_850', 'join_clauses_851', 'group_by_fields_852', 'having_conditions_853', 'is_distinct_854', 'select_exprs_855', 'lock_mode_856')
    def where(this_216, condition_858: 'SqlFragment') -> 'Query':
        nb_860: 'MutableSequence36[WhereClause]' = list_11462(this_216.conditions_846)
        nb_860.append(AndCondition(condition_858))
        return Query(this_216.table_name_845, tuple_11465(nb_860), this_216.selected_fields_847, this_216.order_clauses_848, this_216.limit_val_849, this_216.offset_val_850, this_216.join_clauses_851, this_216.group_by_fields_852, this_216.having_conditions_853, this_216.is_distinct_854, this_216.select_exprs_855, this_216.lock_mode_856)
    def or_where(this_217, condition_862: 'SqlFragment') -> 'Query':
        nb_864: 'MutableSequence36[WhereClause]' = list_11462(this_217.conditions_846)
        nb_864.append(OrCondition(condition_862))
        return Query(this_217.table_name_845, tuple_11465(nb_864), this_217.selected_fields_847, this_217.order_clauses_848, this_217.limit_val_849, this_217.offset_val_850, this_217.join_clauses_851, this_217.group_by_fields_852, this_217.having_conditions_853, this_217.is_distinct_854, this_217.select_exprs_855, this_217.lock_mode_856)
    def where_null(this_218, field_866: 'SafeIdentifier') -> 'Query':
        b_868: 'SqlBuilder' = SqlBuilder()
        b_868.append_safe(field_866.sql_value)
        b_868.append_safe(' IS NULL')
        t_10830: 'SqlFragment' = b_868.accumulated
        return this_218.where(t_10830)
    def where_not_null(this_219, field_870: 'SafeIdentifier') -> 'Query':
        b_872: 'SqlBuilder' = SqlBuilder()
        b_872.append_safe(field_870.sql_value)
        b_872.append_safe(' IS NOT NULL')
        t_10824: 'SqlFragment' = b_872.accumulated
        return this_219.where(t_10824)
    def where_in(this_220, field_874: 'SafeIdentifier', values_875: 'Sequence29[SqlPart]') -> 'Query':
        return_403: 'Query'
        t_10805: 'SqlFragment'
        t_10813: 'int31'
        t_10818: 'SqlFragment'
        with Label35() as fn_876:
            if not values_875:
                b_877: 'SqlBuilder' = SqlBuilder()
                b_877.append_safe('1 = 0')
                t_10805 = b_877.accumulated
                return_403 = this_220.where(t_10805)
                fn_876.break_()
            b_878: 'SqlBuilder' = SqlBuilder()
            b_878.append_safe(field_874.sql_value)
            b_878.append_safe(' IN (')
            b_878.append_part(list_get_11474(values_875, 0))
            i_879: 'int31' = 1
            while True:
                t_10813 = len_11466(values_875)
                if not i_879 < t_10813:
                    break
                b_878.append_safe(', ')
                b_878.append_part(list_get_11474(values_875, i_879))
                i_879 = int_add_11475(i_879, 1)
            b_878.append_safe(')')
            t_10818 = b_878.accumulated
            return_403 = this_220.where(t_10818)
        return return_403
    def where_in_subquery(this_221, field_881: 'SafeIdentifier', sub_882: 'Query') -> 'Query':
        b_884: 'SqlBuilder' = SqlBuilder()
        b_884.append_safe(field_881.sql_value)
        b_884.append_safe(' IN (')
        b_884.append_fragment(sub_882.to_sql())
        b_884.append_safe(')')
        t_10800: 'SqlFragment' = b_884.accumulated
        return this_221.where(t_10800)
    def where_not(this_222, condition_886: 'SqlFragment') -> 'Query':
        b_888: 'SqlBuilder' = SqlBuilder()
        b_888.append_safe('NOT (')
        b_888.append_fragment(condition_886)
        b_888.append_safe(')')
        t_10791: 'SqlFragment' = b_888.accumulated
        return this_222.where(t_10791)
    def where_between(this_223, field_890: 'SafeIdentifier', low_891: 'SqlPart', high_892: 'SqlPart') -> 'Query':
        b_894: 'SqlBuilder' = SqlBuilder()
        b_894.append_safe(field_890.sql_value)
        b_894.append_safe(' BETWEEN ')
        b_894.append_part(low_891)
        b_894.append_safe(' AND ')
        b_894.append_part(high_892)
        t_10785: 'SqlFragment' = b_894.accumulated
        return this_223.where(t_10785)
    def where_like(this_224, field_896: 'SafeIdentifier', pattern_897: 'str27') -> 'Query':
        b_899: 'SqlBuilder' = SqlBuilder()
        b_899.append_safe(field_896.sql_value)
        b_899.append_safe(' LIKE ')
        b_899.append_string(pattern_897)
        t_10776: 'SqlFragment' = b_899.accumulated
        return this_224.where(t_10776)
    def where_i_like(this_225, field_901: 'SafeIdentifier', pattern_902: 'str27') -> 'Query':
        b_904: 'SqlBuilder' = SqlBuilder()
        b_904.append_safe(field_901.sql_value)
        b_904.append_safe(' ILIKE ')
        b_904.append_string(pattern_902)
        t_10769: 'SqlFragment' = b_904.accumulated
        return this_225.where(t_10769)
    def select(this_226, fields_906: 'Sequence29[SafeIdentifier]') -> 'Query':
        return Query(this_226.table_name_845, this_226.conditions_846, fields_906, this_226.order_clauses_848, this_226.limit_val_849, this_226.offset_val_850, this_226.join_clauses_851, this_226.group_by_fields_852, this_226.having_conditions_853, this_226.is_distinct_854, this_226.select_exprs_855, this_226.lock_mode_856)
    def select_expr(this_227, exprs_909: 'Sequence29[SqlFragment]') -> 'Query':
        return Query(this_227.table_name_845, this_227.conditions_846, this_227.selected_fields_847, this_227.order_clauses_848, this_227.limit_val_849, this_227.offset_val_850, this_227.join_clauses_851, this_227.group_by_fields_852, this_227.having_conditions_853, this_227.is_distinct_854, exprs_909, this_227.lock_mode_856)
    def order_by(this_228, field_912: 'SafeIdentifier', ascending_913: 'bool33') -> 'Query':
        nb_915: 'MutableSequence36[OrderClause]' = list_11462(this_228.order_clauses_848)
        nb_915.append(OrderClause(field_912, ascending_913, None))
        return Query(this_228.table_name_845, this_228.conditions_846, this_228.selected_fields_847, tuple_11465(nb_915), this_228.limit_val_849, this_228.offset_val_850, this_228.join_clauses_851, this_228.group_by_fields_852, this_228.having_conditions_853, this_228.is_distinct_854, this_228.select_exprs_855, this_228.lock_mode_856)
    def order_by_nulls(this_229, field_917: 'SafeIdentifier', ascending_918: 'bool33', nulls_919: 'NullsPosition') -> 'Query':
        nb_921: 'MutableSequence36[OrderClause]' = list_11462(this_229.order_clauses_848)
        nb_921.append(OrderClause(field_917, ascending_918, nulls_919))
        return Query(this_229.table_name_845, this_229.conditions_846, this_229.selected_fields_847, tuple_11465(nb_921), this_229.limit_val_849, this_229.offset_val_850, this_229.join_clauses_851, this_229.group_by_fields_852, this_229.having_conditions_853, this_229.is_distinct_854, this_229.select_exprs_855, this_229.lock_mode_856)
    def limit(this_230, n_923: 'int31') -> 'Query':
        if n_923 < 0:
            raise RuntimeError30()
        return Query(this_230.table_name_845, this_230.conditions_846, this_230.selected_fields_847, this_230.order_clauses_848, n_923, this_230.offset_val_850, this_230.join_clauses_851, this_230.group_by_fields_852, this_230.having_conditions_853, this_230.is_distinct_854, this_230.select_exprs_855, this_230.lock_mode_856)
    def offset(this_231, n_926: 'int31') -> 'Query':
        if n_926 < 0:
            raise RuntimeError30()
        return Query(this_231.table_name_845, this_231.conditions_846, this_231.selected_fields_847, this_231.order_clauses_848, this_231.limit_val_849, n_926, this_231.join_clauses_851, this_231.group_by_fields_852, this_231.having_conditions_853, this_231.is_distinct_854, this_231.select_exprs_855, this_231.lock_mode_856)
    def join(this_232, join_type_929: 'JoinType', table_930: 'SafeIdentifier', on_condition_931: 'SqlFragment') -> 'Query':
        nb_933: 'MutableSequence36[JoinClause]' = list_11462(this_232.join_clauses_851)
        nb_933.append(JoinClause(join_type_929, table_930, on_condition_931))
        return Query(this_232.table_name_845, this_232.conditions_846, this_232.selected_fields_847, this_232.order_clauses_848, this_232.limit_val_849, this_232.offset_val_850, tuple_11465(nb_933), this_232.group_by_fields_852, this_232.having_conditions_853, this_232.is_distinct_854, this_232.select_exprs_855, this_232.lock_mode_856)
    def inner_join(this_233, table_935: 'SafeIdentifier', on_condition_936: 'SqlFragment') -> 'Query':
        t_10731: 'InnerJoin' = InnerJoin()
        return this_233.join(t_10731, table_935, on_condition_936)
    def left_join(this_234, table_939: 'SafeIdentifier', on_condition_940: 'SqlFragment') -> 'Query':
        t_10729: 'LeftJoin' = LeftJoin()
        return this_234.join(t_10729, table_939, on_condition_940)
    def right_join(this_235, table_943: 'SafeIdentifier', on_condition_944: 'SqlFragment') -> 'Query':
        t_10727: 'RightJoin' = RightJoin()
        return this_235.join(t_10727, table_943, on_condition_944)
    def full_join(this_236, table_947: 'SafeIdentifier', on_condition_948: 'SqlFragment') -> 'Query':
        t_10725: 'FullJoin' = FullJoin()
        return this_236.join(t_10725, table_947, on_condition_948)
    def cross_join(this_237, table_951: 'SafeIdentifier') -> 'Query':
        nb_953: 'MutableSequence36[JoinClause]' = list_11462(this_237.join_clauses_851)
        nb_953.append(JoinClause(CrossJoin(), table_951, None))
        return Query(this_237.table_name_845, this_237.conditions_846, this_237.selected_fields_847, this_237.order_clauses_848, this_237.limit_val_849, this_237.offset_val_850, tuple_11465(nb_953), this_237.group_by_fields_852, this_237.having_conditions_853, this_237.is_distinct_854, this_237.select_exprs_855, this_237.lock_mode_856)
    def group_by(this_238, field_955: 'SafeIdentifier') -> 'Query':
        nb_957: 'MutableSequence36[SafeIdentifier]' = list_11462(this_238.group_by_fields_852)
        nb_957.append(field_955)
        return Query(this_238.table_name_845, this_238.conditions_846, this_238.selected_fields_847, this_238.order_clauses_848, this_238.limit_val_849, this_238.offset_val_850, this_238.join_clauses_851, tuple_11465(nb_957), this_238.having_conditions_853, this_238.is_distinct_854, this_238.select_exprs_855, this_238.lock_mode_856)
    def having(this_239, condition_959: 'SqlFragment') -> 'Query':
        nb_961: 'MutableSequence36[WhereClause]' = list_11462(this_239.having_conditions_853)
        nb_961.append(AndCondition(condition_959))
        return Query(this_239.table_name_845, this_239.conditions_846, this_239.selected_fields_847, this_239.order_clauses_848, this_239.limit_val_849, this_239.offset_val_850, this_239.join_clauses_851, this_239.group_by_fields_852, tuple_11465(nb_961), this_239.is_distinct_854, this_239.select_exprs_855, this_239.lock_mode_856)
    def or_having(this_240, condition_963: 'SqlFragment') -> 'Query':
        nb_965: 'MutableSequence36[WhereClause]' = list_11462(this_240.having_conditions_853)
        nb_965.append(OrCondition(condition_963))
        return Query(this_240.table_name_845, this_240.conditions_846, this_240.selected_fields_847, this_240.order_clauses_848, this_240.limit_val_849, this_240.offset_val_850, this_240.join_clauses_851, this_240.group_by_fields_852, tuple_11465(nb_965), this_240.is_distinct_854, this_240.select_exprs_855, this_240.lock_mode_856)
    def distinct(this_241) -> 'Query':
        return Query(this_241.table_name_845, this_241.conditions_846, this_241.selected_fields_847, this_241.order_clauses_848, this_241.limit_val_849, this_241.offset_val_850, this_241.join_clauses_851, this_241.group_by_fields_852, this_241.having_conditions_853, True, this_241.select_exprs_855, this_241.lock_mode_856)
    def lock(this_242, mode_969: 'LockMode') -> 'Query':
        return Query(this_242.table_name_845, this_242.conditions_846, this_242.selected_fields_847, this_242.order_clauses_848, this_242.limit_val_849, this_242.offset_val_850, this_242.join_clauses_851, this_242.group_by_fields_852, this_242.having_conditions_853, this_242.is_distinct_854, this_242.select_exprs_855, mode_969)
    def to_sql(this_243) -> 'SqlFragment':
        t_10616: 'int31'
        t_10635: 'int31'
        t_10654: 'int31'
        b_973: 'SqlBuilder' = SqlBuilder()
        if this_243.is_distinct_854:
            b_973.append_safe('SELECT DISTINCT ')
        else:
            b_973.append_safe('SELECT ')
        if not (not this_243.select_exprs_855):
            b_973.append_fragment(list_get_11474(this_243.select_exprs_855, 0))
            i_974: 'int31' = 1
            while True:
                t_10616 = len_11466(this_243.select_exprs_855)
                if not i_974 < t_10616:
                    break
                b_973.append_safe(', ')
                b_973.append_fragment(list_get_11474(this_243.select_exprs_855, i_974))
                i_974 = int_add_11475(i_974, 1)
        elif not this_243.selected_fields_847:
            b_973.append_safe('*')
        else:
            def fn_10609(f_975: 'SafeIdentifier') -> 'str27':
                return f_975.sql_value
            b_973.append_safe(list_join_11477(this_243.selected_fields_847, ', ', fn_10609))
        b_973.append_safe(' FROM ')
        b_973.append_safe(this_243.table_name_845.sql_value)
        def fn_10608(jc_976: 'JoinClause') -> 'None':
            b_973.append_safe(' ')
            t_10596: 'str27' = jc_976.join_type.keyword()
            b_973.append_safe(t_10596)
            b_973.append_safe(' ')
            t_10600: 'str27' = jc_976.table.sql_value
            b_973.append_safe(t_10600)
            oc_977: 'Union40[SqlFragment, None]' = jc_976.on_condition
            if not oc_977 is None:
                oc_2069: 'SqlFragment' = oc_977
                b_973.append_safe(' ON ')
                b_973.append_fragment(oc_2069)
        list_for_each_11460(this_243.join_clauses_851, fn_10608)
        if not (not this_243.conditions_846):
            b_973.append_safe(' WHERE ')
            b_973.append_fragment(list_get_11474(this_243.conditions_846, 0).condition)
            i_978: 'int31' = 1
            while True:
                t_10635 = len_11466(this_243.conditions_846)
                if not i_978 < t_10635:
                    break
                b_973.append_safe(' ')
                b_973.append_safe(list_get_11474(this_243.conditions_846, i_978).keyword())
                b_973.append_safe(' ')
                b_973.append_fragment(list_get_11474(this_243.conditions_846, i_978).condition)
                i_978 = int_add_11475(i_978, 1)
        if not (not this_243.group_by_fields_852):
            b_973.append_safe(' GROUP BY ')
            def fn_10607(f_979: 'SafeIdentifier') -> 'str27':
                return f_979.sql_value
            b_973.append_safe(list_join_11477(this_243.group_by_fields_852, ', ', fn_10607))
        if not (not this_243.having_conditions_853):
            b_973.append_safe(' HAVING ')
            b_973.append_fragment(list_get_11474(this_243.having_conditions_853, 0).condition)
            i_980: 'int31' = 1
            while True:
                t_10654 = len_11466(this_243.having_conditions_853)
                if not i_980 < t_10654:
                    break
                b_973.append_safe(' ')
                b_973.append_safe(list_get_11474(this_243.having_conditions_853, i_980).keyword())
                b_973.append_safe(' ')
                b_973.append_fragment(list_get_11474(this_243.having_conditions_853, i_980).condition)
                i_980 = int_add_11475(i_980, 1)
        if not (not this_243.order_clauses_848):
            b_973.append_safe(' ORDER BY ')
            first_981: 'bool33' = True
            def fn_10606(orc_982: 'OrderClause') -> 'None':
                nonlocal first_981
                t_10591: 'str27'
                t_5801: 'str27'
                if not first_981:
                    b_973.append_safe(', ')
                first_981 = False
                t_10586: 'str27' = orc_982.field.sql_value
                b_973.append_safe(t_10586)
                if orc_982.ascending:
                    t_5801 = ' ASC'
                else:
                    t_5801 = ' DESC'
                b_973.append_safe(t_5801)
                np_983: 'Union40[NullsPosition, None]' = orc_982.nulls_pos
                if not np_983 is None:
                    t_10591 = np_983.keyword()
                    b_973.append_safe(t_10591)
            list_for_each_11460(this_243.order_clauses_848, fn_10606)
        lv_984: 'Union40[int31, None]' = this_243.limit_val_849
        if not lv_984 is None:
            lv_2071: 'int31' = lv_984
            b_973.append_safe(' LIMIT ')
            b_973.append_int32(lv_2071)
        ov_985: 'Union40[int31, None]' = this_243.offset_val_850
        if not ov_985 is None:
            ov_2072: 'int31' = ov_985
            b_973.append_safe(' OFFSET ')
            b_973.append_int32(ov_2072)
        lm_986: 'Union40[LockMode, None]' = this_243.lock_mode_856
        if not lm_986 is None:
            b_973.append_safe(lm_986.keyword())
        return b_973.accumulated
    def count_sql(this_244) -> 'SqlFragment':
        t_10555: 'int31'
        t_10574: 'int31'
        b_989: 'SqlBuilder' = SqlBuilder()
        b_989.append_safe('SELECT COUNT(*) FROM ')
        b_989.append_safe(this_244.table_name_845.sql_value)
        def fn_10543(jc_990: 'JoinClause') -> 'None':
            b_989.append_safe(' ')
            t_10533: 'str27' = jc_990.join_type.keyword()
            b_989.append_safe(t_10533)
            b_989.append_safe(' ')
            t_10537: 'str27' = jc_990.table.sql_value
            b_989.append_safe(t_10537)
            oc2_991: 'Union40[SqlFragment, None]' = jc_990.on_condition
            if not oc2_991 is None:
                oc2_2074: 'SqlFragment' = oc2_991
                b_989.append_safe(' ON ')
                b_989.append_fragment(oc2_2074)
        list_for_each_11460(this_244.join_clauses_851, fn_10543)
        if not (not this_244.conditions_846):
            b_989.append_safe(' WHERE ')
            b_989.append_fragment(list_get_11474(this_244.conditions_846, 0).condition)
            i_992: 'int31' = 1
            while True:
                t_10555 = len_11466(this_244.conditions_846)
                if not i_992 < t_10555:
                    break
                b_989.append_safe(' ')
                b_989.append_safe(list_get_11474(this_244.conditions_846, i_992).keyword())
                b_989.append_safe(' ')
                b_989.append_fragment(list_get_11474(this_244.conditions_846, i_992).condition)
                i_992 = int_add_11475(i_992, 1)
        if not (not this_244.group_by_fields_852):
            b_989.append_safe(' GROUP BY ')
            def fn_10542(f_993: 'SafeIdentifier') -> 'str27':
                return f_993.sql_value
            b_989.append_safe(list_join_11477(this_244.group_by_fields_852, ', ', fn_10542))
        if not (not this_244.having_conditions_853):
            b_989.append_safe(' HAVING ')
            b_989.append_fragment(list_get_11474(this_244.having_conditions_853, 0).condition)
            i_994: 'int31' = 1
            while True:
                t_10574 = len_11466(this_244.having_conditions_853)
                if not i_994 < t_10574:
                    break
                b_989.append_safe(' ')
                b_989.append_safe(list_get_11474(this_244.having_conditions_853, i_994).keyword())
                b_989.append_safe(' ')
                b_989.append_fragment(list_get_11474(this_244.having_conditions_853, i_994).condition)
                i_994 = int_add_11475(i_994, 1)
        return b_989.accumulated
    def safe_to_sql(this_245, default_limit_996: 'int31') -> 'SqlFragment':
        return_428: 'SqlFragment'
        t_5751: 'Query'
        if default_limit_996 < 0:
            raise RuntimeError30()
        if not this_245.limit_val_849 is None:
            return_428 = this_245.to_sql()
        else:
            t_5751 = this_245.limit(default_limit_996)
            return_428 = t_5751.to_sql()
        return return_428
    def __init__(this_387, table_name_999: 'SafeIdentifier', conditions_1000: 'Sequence29[WhereClause]', selected_fields_1001: 'Sequence29[SafeIdentifier]', order_clauses_1002: 'Sequence29[OrderClause]', limit_val_1003: 'Union40[int31, None]', offset_val_1004: 'Union40[int31, None]', join_clauses_1005: 'Sequence29[JoinClause]', group_by_fields_1006: 'Sequence29[SafeIdentifier]', having_conditions_1007: 'Sequence29[WhereClause]', is_distinct_1008: 'bool33', select_exprs_1009: 'Sequence29[SqlFragment]', lock_mode_1010: 'Union40[LockMode, None]') -> None:
        this_387.table_name_845 = table_name_999
        this_387.conditions_846 = conditions_1000
        this_387.selected_fields_847 = selected_fields_1001
        this_387.order_clauses_848 = order_clauses_1002
        this_387.limit_val_849 = limit_val_1003
        this_387.offset_val_850 = offset_val_1004
        this_387.join_clauses_851 = join_clauses_1005
        this_387.group_by_fields_852 = group_by_fields_1006
        this_387.having_conditions_853 = having_conditions_1007
        this_387.is_distinct_854 = is_distinct_1008
        this_387.select_exprs_855 = select_exprs_1009
        this_387.lock_mode_856 = lock_mode_1010
    @property
    def table_name(this_1687) -> 'SafeIdentifier':
        return this_1687.table_name_845
    @property
    def conditions(this_1690) -> 'Sequence29[WhereClause]':
        return this_1690.conditions_846
    @property
    def selected_fields(this_1693) -> 'Sequence29[SafeIdentifier]':
        return this_1693.selected_fields_847
    @property
    def order_clauses(this_1696) -> 'Sequence29[OrderClause]':
        return this_1696.order_clauses_848
    @property
    def limit_val(this_1699) -> 'Union40[int31, None]':
        return this_1699.limit_val_849
    @property
    def offset_val(this_1702) -> 'Union40[int31, None]':
        return this_1702.offset_val_850
    @property
    def join_clauses(this_1705) -> 'Sequence29[JoinClause]':
        return this_1705.join_clauses_851
    @property
    def group_by_fields(this_1708) -> 'Sequence29[SafeIdentifier]':
        return this_1708.group_by_fields_852
    @property
    def having_conditions(this_1711) -> 'Sequence29[WhereClause]':
        return this_1711.having_conditions_853
    @property
    def is_distinct(this_1714) -> 'bool33':
        return this_1714.is_distinct_854
    @property
    def select_exprs(this_1717) -> 'Sequence29[SqlFragment]':
        return this_1717.select_exprs_855
    @property
    def lock_mode(this_1720) -> 'Union40[LockMode, None]':
        return this_1720.lock_mode_856
class SetClause:
    field_1057: 'SafeIdentifier'
    value_1058: 'SqlPart'
    __slots__ = ('field_1057', 'value_1058')
    def __init__(this_443, field_1060: 'SafeIdentifier', value_1061: 'SqlPart') -> None:
        this_443.field_1057 = field_1060
        this_443.value_1058 = value_1061
    @property
    def field(this_1723) -> 'SafeIdentifier':
        return this_1723.field_1057
    @property
    def value(this_1726) -> 'SqlPart':
        return this_1726.value_1058
class UpdateQuery:
    table_name_1062: 'SafeIdentifier'
    set_clauses_1063: 'Sequence29[SetClause]'
    conditions_1064: 'Sequence29[WhereClause]'
    limit_val_1065: 'Union40[int31, None]'
    __slots__ = ('table_name_1062', 'set_clauses_1063', 'conditions_1064', 'limit_val_1065')
    def set(this_246, field_1067: 'SafeIdentifier', value_1068: 'SqlPart') -> 'UpdateQuery':
        nb_1070: 'MutableSequence36[SetClause]' = list_11462(this_246.set_clauses_1063)
        nb_1070.append(SetClause(field_1067, value_1068))
        return UpdateQuery(this_246.table_name_1062, tuple_11465(nb_1070), this_246.conditions_1064, this_246.limit_val_1065)
    def where(this_247, condition_1072: 'SqlFragment') -> 'UpdateQuery':
        nb_1074: 'MutableSequence36[WhereClause]' = list_11462(this_247.conditions_1064)
        nb_1074.append(AndCondition(condition_1072))
        return UpdateQuery(this_247.table_name_1062, this_247.set_clauses_1063, tuple_11465(nb_1074), this_247.limit_val_1065)
    def or_where(this_248, condition_1076: 'SqlFragment') -> 'UpdateQuery':
        nb_1078: 'MutableSequence36[WhereClause]' = list_11462(this_248.conditions_1064)
        nb_1078.append(OrCondition(condition_1076))
        return UpdateQuery(this_248.table_name_1062, this_248.set_clauses_1063, tuple_11465(nb_1078), this_248.limit_val_1065)
    def limit(this_249, n_1080: 'int31') -> 'UpdateQuery':
        if n_1080 < 0:
            raise RuntimeError30()
        return UpdateQuery(this_249.table_name_1062, this_249.set_clauses_1063, this_249.conditions_1064, n_1080)
    def to_sql(this_250) -> 'SqlFragment':
        t_10390: 'int31'
        t_10404: 'int31'
        if not this_250.conditions_1064:
            raise RuntimeError30()
        if not this_250.set_clauses_1063:
            raise RuntimeError30()
        b_1084: 'SqlBuilder' = SqlBuilder()
        b_1084.append_safe('UPDATE ')
        b_1084.append_safe(this_250.table_name_1062.sql_value)
        b_1084.append_safe(' SET ')
        b_1084.append_safe(list_get_11474(this_250.set_clauses_1063, 0).field.sql_value)
        b_1084.append_safe(' = ')
        b_1084.append_part(list_get_11474(this_250.set_clauses_1063, 0).value)
        i_1085: 'int31' = 1
        while True:
            t_10390 = len_11466(this_250.set_clauses_1063)
            if not i_1085 < t_10390:
                break
            b_1084.append_safe(', ')
            b_1084.append_safe(list_get_11474(this_250.set_clauses_1063, i_1085).field.sql_value)
            b_1084.append_safe(' = ')
            b_1084.append_part(list_get_11474(this_250.set_clauses_1063, i_1085).value)
            i_1085 = int_add_11475(i_1085, 1)
        b_1084.append_safe(' WHERE ')
        b_1084.append_fragment(list_get_11474(this_250.conditions_1064, 0).condition)
        i_1086: 'int31' = 1
        while True:
            t_10404 = len_11466(this_250.conditions_1064)
            if not i_1086 < t_10404:
                break
            b_1084.append_safe(' ')
            b_1084.append_safe(list_get_11474(this_250.conditions_1064, i_1086).keyword())
            b_1084.append_safe(' ')
            b_1084.append_fragment(list_get_11474(this_250.conditions_1064, i_1086).condition)
            i_1086 = int_add_11475(i_1086, 1)
        lv_1087: 'Union40[int31, None]' = this_250.limit_val_1065
        if not lv_1087 is None:
            lv_2075: 'int31' = lv_1087
            b_1084.append_safe(' LIMIT ')
            b_1084.append_int32(lv_2075)
        return b_1084.accumulated
    def __init__(this_445, table_name_1089: 'SafeIdentifier', set_clauses_1090: 'Sequence29[SetClause]', conditions_1091: 'Sequence29[WhereClause]', limit_val_1092: 'Union40[int31, None]') -> None:
        this_445.table_name_1062 = table_name_1089
        this_445.set_clauses_1063 = set_clauses_1090
        this_445.conditions_1064 = conditions_1091
        this_445.limit_val_1065 = limit_val_1092
    @property
    def table_name(this_1729) -> 'SafeIdentifier':
        return this_1729.table_name_1062
    @property
    def set_clauses(this_1732) -> 'Sequence29[SetClause]':
        return this_1732.set_clauses_1063
    @property
    def conditions(this_1735) -> 'Sequence29[WhereClause]':
        return this_1735.conditions_1064
    @property
    def limit_val(this_1738) -> 'Union40[int31, None]':
        return this_1738.limit_val_1065
class DeleteQuery:
    table_name_1093: 'SafeIdentifier'
    conditions_1094: 'Sequence29[WhereClause]'
    limit_val_1095: 'Union40[int31, None]'
    __slots__ = ('table_name_1093', 'conditions_1094', 'limit_val_1095')
    def where(this_251, condition_1097: 'SqlFragment') -> 'DeleteQuery':
        nb_1099: 'MutableSequence36[WhereClause]' = list_11462(this_251.conditions_1094)
        nb_1099.append(AndCondition(condition_1097))
        return DeleteQuery(this_251.table_name_1093, tuple_11465(nb_1099), this_251.limit_val_1095)
    def or_where(this_252, condition_1101: 'SqlFragment') -> 'DeleteQuery':
        nb_1103: 'MutableSequence36[WhereClause]' = list_11462(this_252.conditions_1094)
        nb_1103.append(OrCondition(condition_1101))
        return DeleteQuery(this_252.table_name_1093, tuple_11465(nb_1103), this_252.limit_val_1095)
    def limit(this_253, n_1105: 'int31') -> 'DeleteQuery':
        if n_1105 < 0:
            raise RuntimeError30()
        return DeleteQuery(this_253.table_name_1093, this_253.conditions_1094, n_1105)
    def to_sql(this_254) -> 'SqlFragment':
        t_10350: 'int31'
        if not this_254.conditions_1094:
            raise RuntimeError30()
        b_1109: 'SqlBuilder' = SqlBuilder()
        b_1109.append_safe('DELETE FROM ')
        b_1109.append_safe(this_254.table_name_1093.sql_value)
        b_1109.append_safe(' WHERE ')
        b_1109.append_fragment(list_get_11474(this_254.conditions_1094, 0).condition)
        i_1110: 'int31' = 1
        while True:
            t_10350 = len_11466(this_254.conditions_1094)
            if not i_1110 < t_10350:
                break
            b_1109.append_safe(' ')
            b_1109.append_safe(list_get_11474(this_254.conditions_1094, i_1110).keyword())
            b_1109.append_safe(' ')
            b_1109.append_fragment(list_get_11474(this_254.conditions_1094, i_1110).condition)
            i_1110 = int_add_11475(i_1110, 1)
        lv_1111: 'Union40[int31, None]' = this_254.limit_val_1095
        if not lv_1111 is None:
            lv_2076: 'int31' = lv_1111
            b_1109.append_safe(' LIMIT ')
            b_1109.append_int32(lv_2076)
        return b_1109.accumulated
    def __init__(this_455, table_name_1113: 'SafeIdentifier', conditions_1114: 'Sequence29[WhereClause]', limit_val_1115: 'Union40[int31, None]') -> None:
        this_455.table_name_1093 = table_name_1113
        this_455.conditions_1094 = conditions_1114
        this_455.limit_val_1095 = limit_val_1115
    @property
    def table_name(this_1741) -> 'SafeIdentifier':
        return this_1741.table_name_1093
    @property
    def conditions(this_1744) -> 'Sequence29[WhereClause]':
        return this_1744.conditions_1094
    @property
    def limit_val(this_1747) -> 'Union40[int31, None]':
        return this_1747.limit_val_1095
class SafeIdentifier(metaclass = ABCMeta28):
    pass
class ValidatedIdentifier_256(SafeIdentifier):
    value_1346: 'str27'
    __slots__ = ('value_1346',)
    @property
    def sql_value(this_257) -> 'str27':
        return this_257.value_1346
    def __init__(this_469, value_1350: 'str27') -> None:
        this_469.value_1346 = value_1350
class FieldType(metaclass = ABCMeta28):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_475) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_477) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_479) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_481) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_483) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_485) -> None:
        pass
class FieldDef:
    name_1364: 'SafeIdentifier'
    field_type_1365: 'FieldType'
    nullable_1366: 'bool33'
    __slots__ = ('name_1364', 'field_type_1365', 'nullable_1366')
    def __init__(this_487, name_1368: 'SafeIdentifier', field_type_1369: 'FieldType', nullable_1370: 'bool33') -> None:
        this_487.name_1364 = name_1368
        this_487.field_type_1365 = field_type_1369
        this_487.nullable_1366 = nullable_1370
    @property
    def name(this_1607) -> 'SafeIdentifier':
        return this_1607.name_1364
    @property
    def field_type(this_1610) -> 'FieldType':
        return this_1610.field_type_1365
    @property
    def nullable(this_1613) -> 'bool33':
        return this_1613.nullable_1366
class TableDef:
    table_name_1371: 'SafeIdentifier'
    fields_1372: 'Sequence29[FieldDef]'
    __slots__ = ('table_name_1371', 'fields_1372')
    def field(this_258, name_1374: 'str27') -> 'FieldDef':
        return_492: 'FieldDef'
        with Label35() as fn_1375:
            this_6801: 'Sequence29[FieldDef]' = this_258.fields_1372
            n_6802: 'int31' = len_11466(this_6801)
            i_6803: 'int31' = 0
            while i_6803 < n_6802:
                el_6804: 'FieldDef' = list_get_11474(this_6801, i_6803)
                i_6803 = int_add_11475(i_6803, 1)
                f_1376: 'FieldDef' = el_6804
                if f_1376.name.sql_value == name_1374:
                    return_492 = f_1376
                    fn_1375.break_()
            raise RuntimeError30()
        return return_492
    def __init__(this_489, table_name_1378: 'SafeIdentifier', fields_1379: 'Sequence29[FieldDef]') -> None:
        this_489.table_name_1371 = table_name_1378
        this_489.fields_1372 = fields_1379
    @property
    def table_name(this_1616) -> 'SafeIdentifier':
        return this_1616.table_name_1371
    @property
    def fields(this_1619) -> 'Sequence29[FieldDef]':
        return this_1619.fields_1372
T_277 = TypeVar42('T_277', bound = Any41)
class SqlBuilder:
    buffer_1399: 'MutableSequence36[SqlPart]'
    __slots__ = ('buffer_1399',)
    def append_safe(this_259, sql_source_1401: 'str27') -> 'None':
        t_11421: 'SqlSource' = SqlSource(sql_source_1401)
        this_259.buffer_1399.append(t_11421)
    def append_fragment(this_260, fragment_1404: 'SqlFragment') -> 'None':
        t_11419: 'Sequence29[SqlPart]' = fragment_1404.parts
        list_builder_add_all_11478(this_260.buffer_1399, t_11419)
    def append_part(this_261, part_1407: 'SqlPart') -> 'None':
        this_261.buffer_1399.append(part_1407)
    def append_part_list(this_262, values_1410: 'Sequence29[SqlPart]') -> 'None':
        def fn_11415(x_1412: 'SqlPart') -> 'None':
            this_262.append_part(x_1412)
        this_262.append_list_1455(values_1410, fn_11415)
    def append_boolean(this_263, value_1414: 'bool33') -> 'None':
        t_11412: 'SqlBoolean' = SqlBoolean(value_1414)
        this_263.buffer_1399.append(t_11412)
    def append_boolean_list(this_264, values_1417: 'Sequence29[bool33]') -> 'None':
        def fn_11409(x_1419: 'bool33') -> 'None':
            this_264.append_boolean(x_1419)
        this_264.append_list_1455(values_1417, fn_11409)
    def append_date(this_265, value_1421: 'date26') -> 'None':
        t_11406: 'SqlDate' = SqlDate(value_1421)
        this_265.buffer_1399.append(t_11406)
    def append_date_list(this_266, values_1424: 'Sequence29[date26]') -> 'None':
        def fn_11403(x_1426: 'date26') -> 'None':
            this_266.append_date(x_1426)
        this_266.append_list_1455(values_1424, fn_11403)
    def append_float64(this_267, value_1428: 'float38') -> 'None':
        t_11400: 'SqlFloat64' = SqlFloat64(value_1428)
        this_267.buffer_1399.append(t_11400)
    def append_float64_list(this_268, values_1431: 'Sequence29[float38]') -> 'None':
        def fn_11397(x_1433: 'float38') -> 'None':
            this_268.append_float64(x_1433)
        this_268.append_list_1455(values_1431, fn_11397)
    def append_int32(this_269, value_1435: 'int31') -> 'None':
        t_11394: 'SqlInt32' = SqlInt32(value_1435)
        this_269.buffer_1399.append(t_11394)
    def append_int32_list(this_270, values_1438: 'Sequence29[int31]') -> 'None':
        def fn_11391(x_1440: 'int31') -> 'None':
            this_270.append_int32(x_1440)
        this_270.append_list_1455(values_1438, fn_11391)
    def append_int64(this_271, value_1442: 'int64_23') -> 'None':
        t_11388: 'SqlInt64' = SqlInt64(value_1442)
        this_271.buffer_1399.append(t_11388)
    def append_int64_list(this_272, values_1445: 'Sequence29[int64_23]') -> 'None':
        def fn_11385(x_1447: 'int64_23') -> 'None':
            this_272.append_int64(x_1447)
        this_272.append_list_1455(values_1445, fn_11385)
    def append_string(this_273, value_1449: 'str27') -> 'None':
        t_11382: 'SqlString' = SqlString(value_1449)
        this_273.buffer_1399.append(t_11382)
    def append_string_list(this_274, values_1452: 'Sequence29[str27]') -> 'None':
        def fn_11379(x_1454: 'str27') -> 'None':
            this_274.append_string(x_1454)
        this_274.append_list_1455(values_1452, fn_11379)
    def append_list_1455(this_275, values_1456: 'Sequence29[T_277]', append_value_1457: 'Callable43[[T_277], None]') -> 'None':
        t_11374: 'int31'
        t_11376: 'T_277'
        i_1459: 'int31' = 0
        while True:
            t_11374 = len_11466(values_1456)
            if not i_1459 < t_11374:
                break
            if i_1459 > 0:
                this_275.append_safe(', ')
            t_11376 = list_get_11474(values_1456, i_1459)
            append_value_1457(t_11376)
            i_1459 = int_add_11475(i_1459, 1)
    @property
    def accumulated(this_276) -> 'SqlFragment':
        return SqlFragment(tuple_11465(this_276.buffer_1399))
    def __init__(this_494) -> None:
        t_11371: 'MutableSequence36[SqlPart]' = list_11462()
        this_494.buffer_1399 = t_11371
class SqlFragment:
    parts_1466: 'Sequence29[SqlPart]'
    __slots__ = ('parts_1466',)
    def to_source(this_281) -> 'SqlSource':
        return SqlSource(this_281.to_string())
    def to_string(this_282) -> 'str27':
        t_11445: 'int31'
        builder_1471: 'list3[str27]' = ['']
        i_1472: 'int31' = 0
        while True:
            t_11445 = len_11466(this_282.parts_1466)
            if not i_1472 < t_11445:
                break
            list_get_11474(this_282.parts_1466, i_1472).format_to(builder_1471)
            i_1472 = int_add_11475(i_1472, 1)
        return ''.join(builder_1471)
    def __init__(this_515, parts_1474: 'Sequence29[SqlPart]') -> None:
        this_515.parts_1466 = parts_1474
    @property
    def parts(this_1625) -> 'Sequence29[SqlPart]':
        return this_1625.parts_1466
class SqlPart(metaclass = ABCMeta28):
    def format_to(this_283, builder_1476: 'list3[str27]') -> 'None':
        raise RuntimeError30()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_1478: 'str27'
    __slots__ = ('source_1478',)
    def format_to(this_284, builder_1480: 'list3[str27]') -> 'None':
        builder_1480.append(this_284.source_1478)
    def __init__(this_521, source_1483: 'str27') -> None:
        this_521.source_1478 = source_1483
    @property
    def source(this_1622) -> 'str27':
        return this_1622.source_1478
class SqlBoolean(SqlPart):
    value_1484: 'bool33'
    __slots__ = ('value_1484',)
    def format_to(this_285, builder_1486: 'list3[str27]') -> 'None':
        t_6592: 'str27'
        if this_285.value_1484:
            t_6592 = 'TRUE'
        else:
            t_6592 = 'FALSE'
        builder_1486.append(t_6592)
    def __init__(this_524, value_1489: 'bool33') -> None:
        this_524.value_1484 = value_1489
    @property
    def value(this_1628) -> 'bool33':
        return this_1628.value_1484
class SqlDate(SqlPart):
    value_1490: 'date26'
    __slots__ = ('value_1490',)
    def format_to(this_286, builder_1492: 'list3[str27]') -> 'None':
        builder_1492.append("'")
        t_11426: 'str27' = date_to_string_11482(this_286.value_1490)
        def fn_11424(c_1494: 'int31') -> 'None':
            if c_1494 == 39:
                builder_1492.append("''")
            else:
                builder_1492.append(string_from_code_point44(c_1494))
        string_for_each_11484(t_11426, fn_11424)
        builder_1492.append("'")
    def __init__(this_527, value_1496: 'date26') -> None:
        this_527.value_1490 = value_1496
    @property
    def value(this_1643) -> 'date26':
        return this_1643.value_1490
class SqlFloat64(SqlPart):
    value_1497: 'float38'
    __slots__ = ('value_1497',)
    def format_to(this_287, builder_1499: 'list3[str27]') -> 'None':
        t_6581: 'bool33'
        t_6582: 'bool33'
        s_1501: 'str27' = float64_to_string_11485(this_287.value_1497)
        if s_1501 == 'NaN':
            t_6582 = True
        else:
            if s_1501 == 'Infinity':
                t_6581 = True
            else:
                t_6581 = s_1501 == '-Infinity'
            t_6582 = t_6581
        if t_6582:
            builder_1499.append('NULL')
        else:
            builder_1499.append(s_1501)
    def __init__(this_530, value_1503: 'float38') -> None:
        this_530.value_1497 = value_1503
    @property
    def value(this_1640) -> 'float38':
        return this_1640.value_1497
class SqlInt32(SqlPart):
    value_1504: 'int31'
    __slots__ = ('value_1504',)
    def format_to(this_288, builder_1506: 'list3[str27]') -> 'None':
        t_11435: 'str27' = int_to_string_11469(this_288.value_1504)
        builder_1506.append(t_11435)
    def __init__(this_533, value_1509: 'int31') -> None:
        this_533.value_1504 = value_1509
    @property
    def value(this_1634) -> 'int31':
        return this_1634.value_1504
class SqlInt64(SqlPart):
    value_1510: 'int64_23'
    __slots__ = ('value_1510',)
    def format_to(this_289, builder_1512: 'list3[str27]') -> 'None':
        t_11433: 'str27' = int_to_string_11469(this_289.value_1510)
        builder_1512.append(t_11433)
    def __init__(this_536, value_1515: 'int64_23') -> None:
        this_536.value_1510 = value_1515
    @property
    def value(this_1637) -> 'int64_23':
        return this_1637.value_1510
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_1516: 'str27'
    __slots__ = ('value_1516',)
    def format_to(this_290, builder_1518: 'list3[str27]') -> 'None':
        builder_1518.append("'")
        def fn_11438(c_1520: 'int31') -> 'None':
            if c_1520 == 39:
                builder_1518.append("''")
            else:
                builder_1518.append(string_from_code_point44(c_1520))
        string_for_each_11484(this_290.value_1516, fn_11438)
        builder_1518.append("'")
    def __init__(this_539, value_1522: 'str27') -> None:
        this_539.value_1516 = value_1522
    @property
    def value(this_1631) -> 'str27':
        return this_1631.value_1516
def changeset(table_def_686: 'TableDef', params_687: 'MappingProxyType32[str27, str27]') -> 'Changeset':
    t_11221: 'MappingProxyType32[str27, str27]' = map_constructor_11486(())
    return ChangesetImpl_182(table_def_686, params_687, t_11221, (), True)
def is_ident_start_547(c_1351: 'int31') -> 'bool33':
    return_472: 'bool33'
    t_6355: 'bool33'
    t_6356: 'bool33'
    if c_1351 >= 97:
        t_6355 = c_1351 <= 122
    else:
        t_6355 = False
    if t_6355:
        return_472 = True
    else:
        if c_1351 >= 65:
            t_6356 = c_1351 <= 90
        else:
            t_6356 = False
        if t_6356:
            return_472 = True
        else:
            return_472 = c_1351 == 95
    return return_472
def is_ident_part_548(c_1353: 'int31') -> 'bool33':
    return_473: 'bool33'
    if is_ident_start_547(c_1353):
        return_473 = True
    elif c_1353 >= 48:
        return_473 = c_1353 <= 57
    else:
        return_473 = False
    return return_473
def safe_identifier(name_1355: 'str27') -> 'SafeIdentifier':
    t_11219: 'int31'
    if not name_1355:
        raise RuntimeError30()
    idx_1357: 'int31' = 0
    if not is_ident_start_547(string_get_11487(name_1355, idx_1357)):
        raise RuntimeError30()
    t_11216: 'int31' = string_next_11488(name_1355, idx_1357)
    idx_1357 = t_11216
    while True:
        if not len6(name_1355) > idx_1357:
            break
        if not is_ident_part_548(string_get_11487(name_1355, idx_1357)):
            raise RuntimeError30()
        t_11219 = string_next_11488(name_1355, idx_1357)
        idx_1357 = t_11219
    return ValidatedIdentifier_256(name_1355)
def delete_sql(table_def_776: 'TableDef', id_777: 'int31') -> 'SqlFragment':
    b_779: 'SqlBuilder' = SqlBuilder()
    b_779.append_safe('DELETE FROM ')
    b_779.append_safe(table_def_776.table_name.sql_value)
    b_779.append_safe(' WHERE id = ')
    b_779.append_int32(id_777)
    return b_779.accumulated
def from_(table_name_1011: 'SafeIdentifier') -> 'Query':
    return Query(table_name_1011, (), (), (), None, None, (), (), (), False, (), None)
def col(table_1013: 'SafeIdentifier', column_1014: 'SafeIdentifier') -> 'SqlFragment':
    b_1016: 'SqlBuilder' = SqlBuilder()
    b_1016.append_safe(table_1013.sql_value)
    b_1016.append_safe('.')
    b_1016.append_safe(column_1014.sql_value)
    return b_1016.accumulated
def count_all() -> 'SqlFragment':
    b_1018: 'SqlBuilder' = SqlBuilder()
    b_1018.append_safe('COUNT(*)')
    return b_1018.accumulated
def count_col(field_1019: 'SafeIdentifier') -> 'SqlFragment':
    b_1021: 'SqlBuilder' = SqlBuilder()
    b_1021.append_safe('COUNT(')
    b_1021.append_safe(field_1019.sql_value)
    b_1021.append_safe(')')
    return b_1021.accumulated
def sum_col(field_1022: 'SafeIdentifier') -> 'SqlFragment':
    b_1024: 'SqlBuilder' = SqlBuilder()
    b_1024.append_safe('SUM(')
    b_1024.append_safe(field_1022.sql_value)
    b_1024.append_safe(')')
    return b_1024.accumulated
def avg_col(field_1025: 'SafeIdentifier') -> 'SqlFragment':
    b_1027: 'SqlBuilder' = SqlBuilder()
    b_1027.append_safe('AVG(')
    b_1027.append_safe(field_1025.sql_value)
    b_1027.append_safe(')')
    return b_1027.accumulated
def min_col(field_1028: 'SafeIdentifier') -> 'SqlFragment':
    b_1030: 'SqlBuilder' = SqlBuilder()
    b_1030.append_safe('MIN(')
    b_1030.append_safe(field_1028.sql_value)
    b_1030.append_safe(')')
    return b_1030.accumulated
def max_col(field_1031: 'SafeIdentifier') -> 'SqlFragment':
    b_1033: 'SqlBuilder' = SqlBuilder()
    b_1033.append_safe('MAX(')
    b_1033.append_safe(field_1031.sql_value)
    b_1033.append_safe(')')
    return b_1033.accumulated
def union_sql(a_1034: 'Query', b_1035: 'Query') -> 'SqlFragment':
    sb_1037: 'SqlBuilder' = SqlBuilder()
    sb_1037.append_safe('(')
    sb_1037.append_fragment(a_1034.to_sql())
    sb_1037.append_safe(') UNION (')
    sb_1037.append_fragment(b_1035.to_sql())
    sb_1037.append_safe(')')
    return sb_1037.accumulated
def union_all_sql(a_1038: 'Query', b_1039: 'Query') -> 'SqlFragment':
    sb_1041: 'SqlBuilder' = SqlBuilder()
    sb_1041.append_safe('(')
    sb_1041.append_fragment(a_1038.to_sql())
    sb_1041.append_safe(') UNION ALL (')
    sb_1041.append_fragment(b_1039.to_sql())
    sb_1041.append_safe(')')
    return sb_1041.accumulated
def intersect_sql(a_1042: 'Query', b_1043: 'Query') -> 'SqlFragment':
    sb_1045: 'SqlBuilder' = SqlBuilder()
    sb_1045.append_safe('(')
    sb_1045.append_fragment(a_1042.to_sql())
    sb_1045.append_safe(') INTERSECT (')
    sb_1045.append_fragment(b_1043.to_sql())
    sb_1045.append_safe(')')
    return sb_1045.accumulated
def except_sql(a_1046: 'Query', b_1047: 'Query') -> 'SqlFragment':
    sb_1049: 'SqlBuilder' = SqlBuilder()
    sb_1049.append_safe('(')
    sb_1049.append_fragment(a_1046.to_sql())
    sb_1049.append_safe(') EXCEPT (')
    sb_1049.append_fragment(b_1047.to_sql())
    sb_1049.append_safe(')')
    return sb_1049.accumulated
def subquery(q_1050: 'Query', alias_1051: 'SafeIdentifier') -> 'SqlFragment':
    b_1053: 'SqlBuilder' = SqlBuilder()
    b_1053.append_safe('(')
    b_1053.append_fragment(q_1050.to_sql())
    b_1053.append_safe(') AS ')
    b_1053.append_safe(alias_1051.sql_value)
    return b_1053.accumulated
def exists_sql(q_1054: 'Query') -> 'SqlFragment':
    b_1056: 'SqlBuilder' = SqlBuilder()
    b_1056.append_safe('EXISTS (')
    b_1056.append_fragment(q_1054.to_sql())
    b_1056.append_safe(')')
    return b_1056.accumulated
def update(table_name_1116: 'SafeIdentifier') -> 'UpdateQuery':
    return UpdateQuery(table_name_1116, (), (), None)
def delete_from(table_name_1118: 'SafeIdentifier') -> 'DeleteQuery':
    return DeleteQuery(table_name_1118, (), None)
