from builtins import str as str34, float as float36, RuntimeError as RuntimeError39, int as int40, bool as bool42, Exception as Exception46, len as len6, isinstance as isinstance47, list as list0, tuple as tuple1
from typing import Union as Union35, Sequence as Sequence38, MutableSequence as MutableSequence43, Dict as Dict44, Any as Any48, TypeVar as TypeVar49, Callable as Callable50
from abc import ABCMeta as ABCMeta37
from types import MappingProxyType as MappingProxyType41
from temper_core import Label as Label45, Pair as Pair32, string_from_code_point as string_from_code_point51, map_builder_set as map_builder_set2, list_for_each as list_for_each3, mapped_to_map as mapped_to_map4, mapped_has as mapped_has5, string_count_between as string_count_between7, int_to_string as int_to_string8, str_cat as str_cat9, string_to_int32 as string_to_int3210, string_to_int64 as string_to_int6411, string_to_float64 as string_to_float6412, mapped_to_list as mapped_to_list13, list_get as list_get14, int_add as int_add15, float_gt as float_gt16, float64_to_string as float64_to_string17, float_lt as float_lt18, float_gt_eq as float_gt_eq19, float_lt_eq as float_lt_eq20, float_eq as float_eq21, require_string_index as require_string_index22, int_sub as int_sub23, string_next as string_next24, string_get as string_get25, date_from_iso_string as date_from_iso_string26, list_join as list_join27, list_builder_add_all as list_builder_add_all28, date_to_string as date_to_string29, string_for_each as string_for_each30, map_constructor as map_constructor31
from datetime import date as date33
list_17379 = list0
tuple_17381 = tuple1
map_builder_set_17385 = map_builder_set2
list_for_each_17386 = list_for_each3
mapped_to_map_17387 = mapped_to_map4
mapped_has_17388 = mapped_has5
len_17389 = len6
string_count_between_17390 = string_count_between7
int_to_string_17391 = int_to_string8
str_cat_17392 = str_cat9
string_to_int32_17393 = string_to_int3210
string_to_int64_17394 = string_to_int6411
string_to_float64_17395 = string_to_float6412
mapped_to_list_17396 = mapped_to_list13
list_get_17397 = list_get14
int_add_17398 = int_add15
float_gt_17399 = float_gt16
float64_to_string_17400 = float64_to_string17
float_lt_17401 = float_lt18
float_gt_eq_17402 = float_gt_eq19
float_lt_eq_17403 = float_lt_eq20
float_eq_17404 = float_eq21
require_string_index_17407 = require_string_index22
int_sub_17408 = int_sub23
string_next_17409 = string_next24
string_get_17411 = string_get25
date_from_iso_string_17412 = date_from_iso_string26
list_join_17413 = list_join27
list_builder_add_all_17414 = list_builder_add_all28
date_to_string_17418 = date_to_string29
string_for_each_17420 = string_for_each30
map_constructor_17421 = map_constructor31
pair_17422 = Pair32
date_17423 = date33
class ChangesetError:
    field_714: 'str34'
    message_715: 'str34'
    __slots__ = ('field_714', 'message_715')
    def __init__(this_409, field_717: 'str34', message_718: 'str34') -> None:
        this_409.field_714 = field_717
        this_409.message_715 = message_718
    @property
    def field(this_2204) -> 'str34':
        return this_2204.field_714
    @property
    def message(this_2207) -> 'str34':
        return this_2207.message_715
class NumberValidationOpts:
    greater_than_719: 'Union35[float36, None]'
    less_than_720: 'Union35[float36, None]'
    greater_than_or_equal_721: 'Union35[float36, None]'
    less_than_or_equal_722: 'Union35[float36, None]'
    equal_to_723: 'Union35[float36, None]'
    __slots__ = ('greater_than_719', 'less_than_720', 'greater_than_or_equal_721', 'less_than_or_equal_722', 'equal_to_723')
    def __init__(this_411, greater_than_725: 'Union35[float36, None]', less_than_726: 'Union35[float36, None]', greater_than_or_equal_727: 'Union35[float36, None]', less_than_or_equal_728: 'Union35[float36, None]', equal_to_729: 'Union35[float36, None]') -> None:
        this_411.greater_than_719 = greater_than_725
        this_411.less_than_720 = less_than_726
        this_411.greater_than_or_equal_721 = greater_than_or_equal_727
        this_411.less_than_or_equal_722 = less_than_or_equal_728
        this_411.equal_to_723 = equal_to_729
    @property
    def greater_than(this_2210) -> 'Union35[float36, None]':
        return this_2210.greater_than_719
    @property
    def less_than(this_2213) -> 'Union35[float36, None]':
        return this_2213.less_than_720
    @property
    def greater_than_or_equal(this_2216) -> 'Union35[float36, None]':
        return this_2216.greater_than_or_equal_721
    @property
    def less_than_or_equal(this_2219) -> 'Union35[float36, None]':
        return this_2219.less_than_or_equal_722
    @property
    def equal_to(this_2222) -> 'Union35[float36, None]':
        return this_2222.equal_to_723
class Changeset(metaclass = ABCMeta37):
    def cast(this_266, allowed_fields_739: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError39()
    def validate_required(this_267, fields_742: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        raise RuntimeError39()
    def validate_length(this_268, field_745: 'SafeIdentifier', min_746: 'int40', max_747: 'int40') -> 'Changeset':
        raise RuntimeError39()
    def validate_int(this_269, field_750: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_int64(this_270, field_753: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_float(this_271, field_756: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_bool(this_272, field_759: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def put_change(this_273, field_762: 'SafeIdentifier', value_763: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def get_change(this_274, field_766: 'SafeIdentifier') -> 'str34':
        raise RuntimeError39()
    def delete_change(this_275, field_769: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_inclusion(this_276, field_772: 'SafeIdentifier', allowed_773: 'Sequence38[str34]') -> 'Changeset':
        raise RuntimeError39()
    def validate_exclusion(this_277, field_776: 'SafeIdentifier', disallowed_777: 'Sequence38[str34]') -> 'Changeset':
        raise RuntimeError39()
    def validate_number(this_278, field_780: 'SafeIdentifier', opts_781: 'NumberValidationOpts') -> 'Changeset':
        raise RuntimeError39()
    def validate_acceptance(this_279, field_784: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_confirmation(this_280, field_787: 'SafeIdentifier', confirmation_field_788: 'SafeIdentifier') -> 'Changeset':
        raise RuntimeError39()
    def validate_contains(this_281, field_791: 'SafeIdentifier', substring_792: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def validate_starts_with(this_282, field_795: 'SafeIdentifier', prefix_796: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def validate_ends_with(this_283, field_799: 'SafeIdentifier', suffix_800: 'str34') -> 'Changeset':
        raise RuntimeError39()
    def to_insert_sql(this_284) -> 'SqlFragment':
        raise RuntimeError39()
    def to_update_sql(this_285, id_805: 'int40') -> 'SqlFragment':
        raise RuntimeError39()
class ChangesetImpl_286(Changeset):
    table_def_807: 'TableDef'
    params_808: 'MappingProxyType41[str34, str34]'
    changes_809: 'MappingProxyType41[str34, str34]'
    errors_810: 'Sequence38[ChangesetError]'
    is_valid_811: 'bool42'
    __slots__ = ('table_def_807', 'params_808', 'changes_809', 'errors_810', 'is_valid_811')
    @property
    def table_def(this_287) -> 'TableDef':
        return this_287.table_def_807
    @property
    def changes(this_288) -> 'MappingProxyType41[str34, str34]':
        return this_288.changes_809
    @property
    def errors(this_289) -> 'Sequence38[ChangesetError]':
        return this_289.errors_810
    @property
    def is_valid(this_290) -> 'bool42':
        return this_290.is_valid_811
    def add_error_820(this_291, field_821: 'str34', message_822: 'str34') -> 'Changeset':
        eb_824: 'MutableSequence43[ChangesetError]' = list_17379(this_291.errors_810)
        eb_824.append(ChangesetError(field_821, message_822))
        return ChangesetImpl_286(this_291.table_def_807, this_291.params_808, this_291.changes_809, tuple_17381(eb_824), False)
    def cast(this_292, allowed_fields_826: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        mb_828: 'Dict44[str34, str34]' = {}
        def fn_17273(f_829: 'SafeIdentifier') -> 'None':
            t_17271: 'str34'
            t_17268: 'str34' = f_829.sql_value
            val_830: 'str34' = this_292.params_808.get(t_17268, '')
            if not (not val_830):
                t_17271 = f_829.sql_value
                map_builder_set_17385(mb_828, t_17271, val_830)
        list_for_each_17386(allowed_fields_826, fn_17273)
        return ChangesetImpl_286(this_292.table_def_807, this_292.params_808, mapped_to_map_17387(mb_828), this_292.errors_810, this_292.is_valid_811)
    def validate_required(this_293, fields_832: 'Sequence38[SafeIdentifier]') -> 'Changeset':
        return_461: 'Changeset'
        t_17266: 'Sequence38[ChangesetError]'
        t_9729: 'TableDef'
        t_9730: 'MappingProxyType41[str34, str34]'
        t_9731: 'MappingProxyType41[str34, str34]'
        with Label45() as fn_833:
            if not this_293.is_valid_811:
                return_461 = this_293
                fn_833.break_()
            eb_834: 'MutableSequence43[ChangesetError]' = list_17379(this_293.errors_810)
            valid_835: 'bool42' = True
            def fn_17262(f_836: 'SafeIdentifier') -> 'None':
                nonlocal valid_835
                t_17260: 'ChangesetError'
                t_17257: 'str34' = f_836.sql_value
                if not mapped_has_17388(this_293.changes_809, t_17257):
                    t_17260 = ChangesetError(f_836.sql_value, 'is required')
                    eb_834.append(t_17260)
                    valid_835 = False
            list_for_each_17386(fields_832, fn_17262)
            t_9729 = this_293.table_def_807
            t_9730 = this_293.params_808
            t_9731 = this_293.changes_809
            t_17266 = tuple_17381(eb_834)
            return_461 = ChangesetImpl_286(t_9729, t_9730, t_9731, t_17266, valid_835)
        return return_461
    def validate_length(this_294, field_838: 'SafeIdentifier', min_839: 'int40', max_840: 'int40') -> 'Changeset':
        return_462: 'Changeset'
        t_17248: 'str34'
        t_17253: 'str34'
        t_17254: 'str34'
        t_17255: 'str34'
        t_9719: 'bool42'
        with Label45() as fn_841:
            if not this_294.is_valid_811:
                return_462 = this_294
                fn_841.break_()
            t_17248 = field_838.sql_value
            val_842: 'str34' = this_294.changes_809.get(t_17248, '')
            len_843: 'int40' = string_count_between_17390(val_842, 0, len_17389(val_842))
            if len_843 < min_839:
                t_9719 = True
            else:
                t_9719 = len_843 > max_840
            if t_9719:
                t_17253 = field_838.sql_value
                t_17254 = int_to_string_17391(min_839)
                t_17255 = int_to_string_17391(max_840)
                return_462 = this_294.add_error_820(t_17253, str_cat_17392('must be between ', t_17254, ' and ', t_17255, ' characters'))
                fn_841.break_()
            return_462 = this_294
        return return_462
    def validate_int(this_295, field_845: 'SafeIdentifier') -> 'Changeset':
        return_463: 'Changeset'
        t_17243: 'str34'
        t_17246: 'str34'
        with Label45() as fn_846:
            if not this_295.is_valid_811:
                return_463 = this_295
                fn_846.break_()
            t_17243 = field_845.sql_value
            val_847: 'str34' = this_295.changes_809.get(t_17243, '')
            if not val_847:
                return_463 = this_295
                fn_846.break_()
            parse_ok_848: 'bool42'
            try:
                string_to_int32_17393(val_847)
                parse_ok_848 = True
            except Exception46:
                parse_ok_848 = False
            if not parse_ok_848:
                t_17246 = field_845.sql_value
                return_463 = this_295.add_error_820(t_17246, 'must be an integer')
                fn_846.break_()
            return_463 = this_295
        return return_463
    def validate_int64(this_296, field_850: 'SafeIdentifier') -> 'Changeset':
        return_464: 'Changeset'
        t_17238: 'str34'
        t_17241: 'str34'
        with Label45() as fn_851:
            if not this_296.is_valid_811:
                return_464 = this_296
                fn_851.break_()
            t_17238 = field_850.sql_value
            val_852: 'str34' = this_296.changes_809.get(t_17238, '')
            if not val_852:
                return_464 = this_296
                fn_851.break_()
            parse_ok_853: 'bool42'
            try:
                string_to_int64_17394(val_852)
                parse_ok_853 = True
            except Exception46:
                parse_ok_853 = False
            if not parse_ok_853:
                t_17241 = field_850.sql_value
                return_464 = this_296.add_error_820(t_17241, 'must be a 64-bit integer')
                fn_851.break_()
            return_464 = this_296
        return return_464
    def validate_float(this_297, field_855: 'SafeIdentifier') -> 'Changeset':
        return_465: 'Changeset'
        t_17233: 'str34'
        t_17236: 'str34'
        with Label45() as fn_856:
            if not this_297.is_valid_811:
                return_465 = this_297
                fn_856.break_()
            t_17233 = field_855.sql_value
            val_857: 'str34' = this_297.changes_809.get(t_17233, '')
            if not val_857:
                return_465 = this_297
                fn_856.break_()
            parse_ok_858: 'bool42'
            try:
                string_to_float64_17395(val_857)
                parse_ok_858 = True
            except Exception46:
                parse_ok_858 = False
            if not parse_ok_858:
                t_17236 = field_855.sql_value
                return_465 = this_297.add_error_820(t_17236, 'must be a number')
                fn_856.break_()
            return_465 = this_297
        return return_465
    def validate_bool(this_298, field_860: 'SafeIdentifier') -> 'Changeset':
        return_466: 'Changeset'
        t_17228: 'str34'
        t_17231: 'str34'
        t_9687: 'bool42'
        t_9688: 'bool42'
        t_9690: 'bool42'
        t_9691: 'bool42'
        t_9693: 'bool42'
        with Label45() as fn_861:
            if not this_298.is_valid_811:
                return_466 = this_298
                fn_861.break_()
            t_17228 = field_860.sql_value
            val_862: 'str34' = this_298.changes_809.get(t_17228, '')
            if not val_862:
                return_466 = this_298
                fn_861.break_()
            is_true_863: 'bool42'
            if val_862 == 'true':
                is_true_863 = True
            else:
                if val_862 == '1':
                    t_9688 = True
                else:
                    if val_862 == 'yes':
                        t_9687 = True
                    else:
                        t_9687 = val_862 == 'on'
                    t_9688 = t_9687
                is_true_863 = t_9688
            is_false_864: 'bool42'
            if val_862 == 'false':
                is_false_864 = True
            else:
                if val_862 == '0':
                    t_9691 = True
                else:
                    if val_862 == 'no':
                        t_9690 = True
                    else:
                        t_9690 = val_862 == 'off'
                    t_9691 = t_9690
                is_false_864 = t_9691
            if not is_true_863:
                t_9693 = not is_false_864
            else:
                t_9693 = False
            if t_9693:
                t_17231 = field_860.sql_value
                return_466 = this_298.add_error_820(t_17231, 'must be a boolean (true/false/1/0/yes/no/on/off)')
                fn_861.break_()
            return_466 = this_298
        return return_466
    def put_change(this_299, field_866: 'SafeIdentifier', value_867: 'str34') -> 'Changeset':
        t_17216: 'int40'
        mb_869: 'Dict44[str34, str34]' = {}
        pairs_870: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_17396(this_299.changes_809)
        i_871: 'int40' = 0
        while True:
            t_17216 = len_17389(pairs_870)
            if not i_871 < t_17216:
                break
            map_builder_set_17385(mb_869, list_get_17397(pairs_870, i_871).key, list_get_17397(pairs_870, i_871).value)
            i_871 = int_add_17398(i_871, 1)
        map_builder_set_17385(mb_869, field_866.sql_value, value_867)
        return ChangesetImpl_286(this_299.table_def_807, this_299.params_808, mapped_to_map_17387(mb_869), this_299.errors_810, this_299.is_valid_811)
    def get_change(this_300, field_873: 'SafeIdentifier') -> 'str34':
        t_17210: 'str34' = field_873.sql_value
        if not mapped_has_17388(this_300.changes_809, t_17210):
            raise RuntimeError39()
        t_17212: 'str34' = field_873.sql_value
        return this_300.changes_809.get(t_17212, '')
    def delete_change(this_301, field_876: 'SafeIdentifier') -> 'Changeset':
        t_17197: 'int40'
        mb_878: 'Dict44[str34, str34]' = {}
        pairs_879: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_17396(this_301.changes_809)
        i_880: 'int40' = 0
        while True:
            t_17197 = len_17389(pairs_879)
            if not i_880 < t_17197:
                break
            if list_get_17397(pairs_879, i_880).key != field_876.sql_value:
                map_builder_set_17385(mb_878, list_get_17397(pairs_879, i_880).key, list_get_17397(pairs_879, i_880).value)
            i_880 = int_add_17398(i_880, 1)
        return ChangesetImpl_286(this_301.table_def_807, this_301.params_808, mapped_to_map_17387(mb_878), this_301.errors_810, this_301.is_valid_811)
    def validate_inclusion(this_302, field_882: 'SafeIdentifier', allowed_883: 'Sequence38[str34]') -> 'Changeset':
        return_470: 'Changeset'
        t_17187: 'str34'
        t_17189: 'str34'
        t_17193: 'str34'
        with Label45() as fn_884:
            if not this_302.is_valid_811:
                return_470 = this_302
                fn_884.break_()
            t_17187 = field_882.sql_value
            if not mapped_has_17388(this_302.changes_809, t_17187):
                return_470 = this_302
                fn_884.break_()
            t_17189 = field_882.sql_value
            val_885: 'str34' = this_302.changes_809.get(t_17189, '')
            found_886: 'bool42' = False
            def fn_17186(a_887: 'str34') -> 'None':
                nonlocal found_886
                if a_887 == val_885:
                    found_886 = True
            list_for_each_17386(allowed_883, fn_17186)
            if not found_886:
                t_17193 = field_882.sql_value
                return_470 = this_302.add_error_820(t_17193, 'is not included in the list')
                fn_884.break_()
            return_470 = this_302
        return return_470
    def validate_exclusion(this_303, field_889: 'SafeIdentifier', disallowed_890: 'Sequence38[str34]') -> 'Changeset':
        return_471: 'Changeset'
        t_17178: 'str34'
        t_17180: 'str34'
        t_17184: 'str34'
        with Label45() as fn_891:
            if not this_303.is_valid_811:
                return_471 = this_303
                fn_891.break_()
            t_17178 = field_889.sql_value
            if not mapped_has_17388(this_303.changes_809, t_17178):
                return_471 = this_303
                fn_891.break_()
            t_17180 = field_889.sql_value
            val_892: 'str34' = this_303.changes_809.get(t_17180, '')
            found_893: 'bool42' = False
            def fn_17177(d_894: 'str34') -> 'None':
                nonlocal found_893
                if d_894 == val_892:
                    found_893 = True
            list_for_each_17386(disallowed_890, fn_17177)
            if found_893:
                t_17184 = field_889.sql_value
                return_471 = this_303.add_error_820(t_17184, 'is reserved')
                fn_891.break_()
            return_471 = this_303
        return return_471
    def validate_number(this_304, field_896: 'SafeIdentifier', opts_897: 'NumberValidationOpts') -> 'Changeset':
        return_472: 'Changeset'
        t_17151: 'str34'
        t_17153: 'str34'
        t_17155: 'str34'
        t_17158: 'str34'
        t_17159: 'str34'
        t_17162: 'str34'
        t_17163: 'str34'
        t_17166: 'str34'
        t_17167: 'str34'
        t_17170: 'str34'
        t_17171: 'str34'
        t_17174: 'str34'
        t_17175: 'str34'
        t_9621: 'float36'
        with Label45() as fn_898:
            if not this_304.is_valid_811:
                return_472 = this_304
                fn_898.break_()
            t_17151 = field_896.sql_value
            if not mapped_has_17388(this_304.changes_809, t_17151):
                return_472 = this_304
                fn_898.break_()
            t_17153 = field_896.sql_value
            val_899: 'str34' = this_304.changes_809.get(t_17153, '')
            parse_ok_900: 'bool42'
            try:
                string_to_float64_17395(val_899)
                parse_ok_900 = True
            except Exception46:
                parse_ok_900 = False
            if not parse_ok_900:
                t_17155 = field_896.sql_value
                return_472 = this_304.add_error_820(t_17155, 'must be a number')
                fn_898.break_()
            num_901: 'float36'
            try:
                t_9621 = string_to_float64_17395(val_899)
                num_901 = t_9621
            except Exception46:
                num_901 = 0.0
            gt_902: 'Union35[float36, None]' = opts_897.greater_than
            if not gt_902 is None:
                gt_2831: 'float36' = gt_902
                if not float_gt_17399(num_901, gt_2831):
                    t_17158 = field_896.sql_value
                    t_17159 = float64_to_string_17400(gt_2831)
                    return_472 = this_304.add_error_820(t_17158, str_cat_17392('must be greater than ', t_17159))
                    fn_898.break_()
            lt_903: 'Union35[float36, None]' = opts_897.less_than
            if not lt_903 is None:
                lt_2832: 'float36' = lt_903
                if not float_lt_17401(num_901, lt_2832):
                    t_17162 = field_896.sql_value
                    t_17163 = float64_to_string_17400(lt_2832)
                    return_472 = this_304.add_error_820(t_17162, str_cat_17392('must be less than ', t_17163))
                    fn_898.break_()
            gte_904: 'Union35[float36, None]' = opts_897.greater_than_or_equal
            if not gte_904 is None:
                gte_2833: 'float36' = gte_904
                if not float_gt_eq_17402(num_901, gte_2833):
                    t_17166 = field_896.sql_value
                    t_17167 = float64_to_string_17400(gte_2833)
                    return_472 = this_304.add_error_820(t_17166, str_cat_17392('must be greater than or equal to ', t_17167))
                    fn_898.break_()
            lte_905: 'Union35[float36, None]' = opts_897.less_than_or_equal
            if not lte_905 is None:
                lte_2834: 'float36' = lte_905
                if not float_lt_eq_17403(num_901, lte_2834):
                    t_17170 = field_896.sql_value
                    t_17171 = float64_to_string_17400(lte_2834)
                    return_472 = this_304.add_error_820(t_17170, str_cat_17392('must be less than or equal to ', t_17171))
                    fn_898.break_()
            eq_906: 'Union35[float36, None]' = opts_897.equal_to
            if not eq_906 is None:
                eq_2835: 'float36' = eq_906
                if not float_eq_17404(num_901, eq_2835):
                    t_17174 = field_896.sql_value
                    t_17175 = float64_to_string_17400(eq_2835)
                    return_472 = this_304.add_error_820(t_17174, str_cat_17392('must be equal to ', t_17175))
                    fn_898.break_()
            return_472 = this_304
        return return_472
    def validate_acceptance(this_305, field_908: 'SafeIdentifier') -> 'Changeset':
        return_473: 'Changeset'
        t_17145: 'str34'
        t_17147: 'str34'
        t_17149: 'str34'
        t_9609: 'bool42'
        t_9610: 'bool42'
        with Label45() as fn_909:
            if not this_305.is_valid_811:
                return_473 = this_305
                fn_909.break_()
            t_17145 = field_908.sql_value
            if not mapped_has_17388(this_305.changes_809, t_17145):
                return_473 = this_305
                fn_909.break_()
            t_17147 = field_908.sql_value
            val_910: 'str34' = this_305.changes_809.get(t_17147, '')
            accepted_911: 'bool42'
            if val_910 == 'true':
                accepted_911 = True
            else:
                if val_910 == '1':
                    t_9610 = True
                else:
                    if val_910 == 'yes':
                        t_9609 = True
                    else:
                        t_9609 = val_910 == 'on'
                    t_9610 = t_9609
                accepted_911 = t_9610
            if not accepted_911:
                t_17149 = field_908.sql_value
                return_473 = this_305.add_error_820(t_17149, 'must be accepted')
                fn_909.break_()
            return_473 = this_305
        return return_473
    def validate_confirmation(this_306, field_913: 'SafeIdentifier', confirmation_field_914: 'SafeIdentifier') -> 'Changeset':
        return_474: 'Changeset'
        t_17137: 'str34'
        t_17139: 'str34'
        t_17141: 'str34'
        t_17143: 'str34'
        with Label45() as fn_915:
            if not this_306.is_valid_811:
                return_474 = this_306
                fn_915.break_()
            t_17137 = field_913.sql_value
            if not mapped_has_17388(this_306.changes_809, t_17137):
                return_474 = this_306
                fn_915.break_()
            t_17139 = field_913.sql_value
            val_916: 'str34' = this_306.changes_809.get(t_17139, '')
            t_17141 = confirmation_field_914.sql_value
            conf_917: 'str34' = this_306.changes_809.get(t_17141, '')
            if val_916 != conf_917:
                t_17143 = confirmation_field_914.sql_value
                return_474 = this_306.add_error_820(t_17143, 'does not match')
                fn_915.break_()
            return_474 = this_306
        return return_474
    def validate_contains(this_307, field_919: 'SafeIdentifier', substring_920: 'str34') -> 'Changeset':
        return_475: 'Changeset'
        t_17129: 'str34'
        t_17131: 'str34'
        t_17135: 'str34'
        with Label45() as fn_921:
            if not this_307.is_valid_811:
                return_475 = this_307
                fn_921.break_()
            t_17129 = field_919.sql_value
            if not mapped_has_17388(this_307.changes_809, t_17129):
                return_475 = this_307
                fn_921.break_()
            t_17131 = field_919.sql_value
            val_922: 'str34' = this_307.changes_809.get(t_17131, '')
            if not val_922.find(substring_920) >= 0:
                t_17135 = field_919.sql_value
                return_475 = this_307.add_error_820(t_17135, 'must contain the given substring')
                fn_921.break_()
            return_475 = this_307
        return return_475
    def validate_starts_with(this_308, field_924: 'SafeIdentifier', prefix_925: 'str34') -> 'Changeset':
        return_476: 'Changeset'
        t_17120: 'str34'
        t_17122: 'str34'
        t_17126: 'int40'
        t_17127: 'str34'
        with Label45() as fn_926:
            if not this_308.is_valid_811:
                return_476 = this_308
                fn_926.break_()
            t_17120 = field_924.sql_value
            if not mapped_has_17388(this_308.changes_809, t_17120):
                return_476 = this_308
                fn_926.break_()
            t_17122 = field_924.sql_value
            val_927: 'str34' = this_308.changes_809.get(t_17122, '')
            idx_928: 'int40' = val_927.find(prefix_925)
            starts_929: 'bool42'
            if idx_928 >= 0:
                t_17126 = string_count_between_17390(val_927, 0, require_string_index_17407(idx_928))
                starts_929 = t_17126 == 0
            else:
                starts_929 = False
            if not starts_929:
                t_17127 = field_924.sql_value
                return_476 = this_308.add_error_820(t_17127, 'must start with the given prefix')
                fn_926.break_()
            return_476 = this_308
        return return_476
    def validate_ends_with(this_309, field_931: 'SafeIdentifier', suffix_932: 'str34') -> 'Changeset':
        return_477: 'Changeset'
        t_17100: 'str34'
        t_17102: 'str34'
        t_17107: 'int40'
        t_17109: 'str34'
        t_17111: 'int40'
        t_17112: 'bool42'
        t_17116: 'int40'
        t_17117: 'int40'
        t_17118: 'str34'
        t_9569: 'bool42'
        with Label45() as fn_933:
            if not this_309.is_valid_811:
                return_477 = this_309
                fn_933.break_()
            t_17100 = field_931.sql_value
            if not mapped_has_17388(this_309.changes_809, t_17100):
                return_477 = this_309
                fn_933.break_()
            t_17102 = field_931.sql_value
            val_934: 'str34' = this_309.changes_809.get(t_17102, '')
            val_len_935: 'int40' = string_count_between_17390(val_934, 0, len_17389(val_934))
            t_17107 = len_17389(suffix_932)
            suffix_len_936: 'int40' = string_count_between_17390(suffix_932, 0, t_17107)
            if val_len_935 < suffix_len_936:
                t_17109 = field_931.sql_value
                return_477 = this_309.add_error_820(t_17109, 'must end with the given suffix')
                fn_933.break_()
            skip_count_937: 'int40' = int_sub_17408(val_len_935, suffix_len_936)
            str_idx_938: 'int40' = 0
            i_939: 'int40' = 0
            while i_939 < skip_count_937:
                t_17111 = string_next_17409(val_934, str_idx_938)
                str_idx_938 = t_17111
                i_939 = int_add_17398(i_939, 1)
            suf_idx_940: 'int40' = 0
            matches_941: 'bool42' = True
            while True:
                if matches_941:
                    t_17112 = len6(suffix_932) > suf_idx_940
                    t_9569 = t_17112
                else:
                    t_9569 = False
                if not t_9569:
                    break
                if not len6(val_934) > str_idx_938:
                    matches_941 = False
                elif string_get_17411(val_934, str_idx_938) != string_get_17411(suffix_932, suf_idx_940):
                    matches_941 = False
                else:
                    t_17116 = string_next_17409(val_934, str_idx_938)
                    str_idx_938 = t_17116
                    t_17117 = string_next_17409(suffix_932, suf_idx_940)
                    suf_idx_940 = t_17117
            if not matches_941:
                t_17118 = field_931.sql_value
                return_477 = this_309.add_error_820(t_17118, 'must end with the given suffix')
                fn_933.break_()
            return_477 = this_309
        return return_477
    def parse_bool_sql_part_942(this_310, val_943: 'str34') -> 'SqlBoolean':
        return_478: 'SqlBoolean'
        t_9547: 'bool42'
        t_9548: 'bool42'
        t_9549: 'bool42'
        t_9551: 'bool42'
        t_9552: 'bool42'
        t_9553: 'bool42'
        with Label45() as fn_944:
            if val_943 == 'true':
                t_9549 = True
            else:
                if val_943 == '1':
                    t_9548 = True
                else:
                    if val_943 == 'yes':
                        t_9547 = True
                    else:
                        t_9547 = val_943 == 'on'
                    t_9548 = t_9547
                t_9549 = t_9548
            if t_9549:
                return_478 = SqlBoolean(True)
                fn_944.break_()
            if val_943 == 'false':
                t_9553 = True
            else:
                if val_943 == '0':
                    t_9552 = True
                else:
                    if val_943 == 'no':
                        t_9551 = True
                    else:
                        t_9551 = val_943 == 'off'
                    t_9552 = t_9551
                t_9553 = t_9552
            if t_9553:
                return_478 = SqlBoolean(False)
                fn_944.break_()
            raise RuntimeError39()
        return return_478
    def value_to_sql_part_945(this_311, field_def_946: 'FieldDef', val_947: 'str34') -> 'SqlPart':
        return_479: 'SqlPart'
        t_9534: 'int40'
        t_9537: 'int64_23'
        t_9540: 'float36'
        t_9545: 'date33'
        with Label45() as fn_948:
            ft_949: 'FieldType' = field_def_946.field_type
            if isinstance47(ft_949, StringField):
                return_479 = SqlString(val_947)
                fn_948.break_()
            if isinstance47(ft_949, IntField):
                t_9534 = string_to_int32_17393(val_947)
                return_479 = SqlInt32(t_9534)
                fn_948.break_()
            if isinstance47(ft_949, Int64Field):
                t_9537 = string_to_int64_17394(val_947)
                return_479 = SqlInt64(t_9537)
                fn_948.break_()
            if isinstance47(ft_949, FloatField):
                t_9540 = string_to_float64_17395(val_947)
                return_479 = SqlFloat64(t_9540)
                fn_948.break_()
            if isinstance47(ft_949, BoolField):
                return_479 = this_311.parse_bool_sql_part_942(val_947)
                fn_948.break_()
            if isinstance47(ft_949, DateField):
                t_9545 = date_from_iso_string_17412(val_947)
                return_479 = SqlDate(t_9545)
                fn_948.break_()
            raise RuntimeError39()
        return return_479
    def to_insert_sql(this_312) -> 'SqlFragment':
        t_17032: 'int40'
        t_17039: 'str34'
        t_17044: 'int40'
        t_17046: 'str34'
        t_17051: 'str34'
        t_17054: 'int40'
        t_17060: 'str34'
        t_17080: 'int40'
        t_9484: 'bool42'
        t_9485: 'bool42'
        t_9492: 'FieldDef'
        t_9498: 'SqlPart'
        if not this_312.is_valid_811:
            raise RuntimeError39()
        i_952: 'int40' = 0
        while True:
            with Label45() as continue_17375:
                t_17032 = len_17389(this_312.table_def_807.fields)
                if not i_952 < t_17032:
                    break
                f_953: 'FieldDef' = list_get_17397(this_312.table_def_807.fields, i_952)
                if f_953.virtual:
                    continue_17375.break_()
                dv_954: 'Union35[SqlPart, None]' = f_953.default_value
                if not f_953.nullable:
                    t_17039 = f_953.name.sql_value
                    if not mapped_has_17388(this_312.changes_809, t_17039):
                        t_9484 = dv_954 is None
                    else:
                        t_9484 = False
                    t_9485 = t_9484
                else:
                    t_9485 = False
                if t_9485:
                    raise RuntimeError39()
            i_952 = int_add_17398(i_952, 1)
        col_names_955: 'MutableSequence43[str34]' = list_17379()
        val_parts_956: 'MutableSequence43[SqlPart]' = list_17379()
        pairs_957: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_17396(this_312.changes_809)
        i_958: 'int40' = 0
        while True:
            with Label45() as continue_17376:
                t_17044 = len_17389(pairs_957)
                if not i_958 < t_17044:
                    break
                pair_959: 'Pair32[str34, str34]' = list_get_17397(pairs_957, i_958)
                t_17046 = pair_959.key
                t_9492 = this_312.table_def_807.field(t_17046)
                fd_960: 'FieldDef' = t_9492
                if fd_960.virtual:
                    continue_17376.break_()
                col_names_955.append(fd_960.name.sql_value)
                t_17051 = pair_959.value
                t_9498 = this_312.value_to_sql_part_945(fd_960, t_17051)
                val_parts_956.append(t_9498)
            i_958 = int_add_17398(i_958, 1)
        i_961: 'int40' = 0
        while True:
            with Label45() as continue_17377:
                t_17054 = len_17389(this_312.table_def_807.fields)
                if not i_961 < t_17054:
                    break
                f_962: 'FieldDef' = list_get_17397(this_312.table_def_807.fields, i_961)
                if f_962.virtual:
                    continue_17377.break_()
                dv_963: 'Union35[SqlPart, None]' = f_962.default_value
                if not dv_963 is None:
                    dv_2843: 'SqlPart' = dv_963
                    t_17060 = f_962.name.sql_value
                    if not mapped_has_17388(this_312.changes_809, t_17060):
                        col_names_955.append(f_962.name.sql_value)
                        val_parts_956.append(dv_2843)
            i_961 = int_add_17398(i_961, 1)
        if len_17389(val_parts_956) == 0:
            raise RuntimeError39()
        b_964: 'SqlBuilder' = SqlBuilder()
        b_964.append_safe('INSERT INTO ')
        b_964.append_safe(this_312.table_def_807.table_name.sql_value)
        b_964.append_safe(' (')
        t_17073: 'Sequence38[str34]' = tuple_17381(col_names_955)
        def fn_17030(c_965: 'str34') -> 'str34':
            return c_965
        b_964.append_safe(list_join_17413(t_17073, ', ', fn_17030))
        b_964.append_safe(') VALUES (')
        b_964.append_part(list_get_17397(val_parts_956, 0))
        j_966: 'int40' = 1
        while True:
            t_17080 = len_17389(val_parts_956)
            if not j_966 < t_17080:
                break
            b_964.append_safe(', ')
            b_964.append_part(list_get_17397(val_parts_956, j_966))
            j_966 = int_add_17398(j_966, 1)
        b_964.append_safe(')')
        return b_964.accumulated
    def to_update_sql(this_313, id_968: 'int40') -> 'SqlFragment':
        t_17013: 'int40'
        t_17015: 'str34'
        t_17022: 'str34'
        t_9459: 'FieldDef'
        t_9466: 'SqlPart'
        if not this_313.is_valid_811:
            raise RuntimeError39()
        pairs_970: 'Sequence38[(Pair32[str34, str34])]' = mapped_to_list_17396(this_313.changes_809)
        if len_17389(pairs_970) == 0:
            raise RuntimeError39()
        b_971: 'SqlBuilder' = SqlBuilder()
        b_971.append_safe('UPDATE ')
        b_971.append_safe(this_313.table_def_807.table_name.sql_value)
        b_971.append_safe(' SET ')
        set_count_972: 'int40' = 0
        i_973: 'int40' = 0
        while True:
            with Label45() as continue_17378:
                t_17013 = len_17389(pairs_970)
                if not i_973 < t_17013:
                    break
                pair_974: 'Pair32[str34, str34]' = list_get_17397(pairs_970, i_973)
                t_17015 = pair_974.key
                t_9459 = this_313.table_def_807.field(t_17015)
                fd_975: 'FieldDef' = t_9459
                if fd_975.virtual:
                    continue_17378.break_()
                if set_count_972 > 0:
                    b_971.append_safe(', ')
                b_971.append_safe(fd_975.name.sql_value)
                b_971.append_safe(' = ')
                t_17022 = pair_974.value
                t_9466 = this_313.value_to_sql_part_945(fd_975, t_17022)
                b_971.append_part(t_9466)
                set_count_972 = int_add_17398(set_count_972, 1)
            i_973 = int_add_17398(i_973, 1)
        if set_count_972 == 0:
            raise RuntimeError39()
        b_971.append_safe(' WHERE ')
        b_971.append_safe(this_313.table_def_807.pk_name())
        b_971.append_safe(' = ')
        b_971.append_int32(id_968)
        return b_971.accumulated
    def __init__(this_450, table_def_977: 'TableDef', params_978: 'MappingProxyType41[str34, str34]', changes_979: 'MappingProxyType41[str34, str34]', errors_980: 'Sequence38[ChangesetError]', is_valid_981: 'bool42') -> None:
        this_450.table_def_807 = table_def_977
        this_450.params_808 = params_978
        this_450.changes_809 = changes_979
        this_450.errors_810 = errors_980
        this_450.is_valid_811 = is_valid_981
class JoinType(metaclass = ABCMeta37):
    def keyword(this_314) -> 'str34':
        raise RuntimeError39()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_315) -> 'str34':
        return 'INNER JOIN'
    def __init__(this_487) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_316) -> 'str34':
        return 'LEFT JOIN'
    def __init__(this_490) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_317) -> 'str34':
        return 'RIGHT JOIN'
    def __init__(this_493) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_318) -> 'str34':
        return 'FULL OUTER JOIN'
    def __init__(this_496) -> None:
        pass
class CrossJoin(JoinType):
    __slots__ = ()
    def keyword(this_319) -> 'str34':
        return 'CROSS JOIN'
    def __init__(this_499) -> None:
        pass
class JoinClause:
    join_type_1322: 'JoinType'
    table_1323: 'SafeIdentifier'
    on_condition_1324: 'Union35[SqlFragment, None]'
    __slots__ = ('join_type_1322', 'table_1323', 'on_condition_1324')
    def __init__(this_502, join_type_1326: 'JoinType', table_1327: 'SafeIdentifier', on_condition_1328: 'Union35[SqlFragment, None]') -> None:
        this_502.join_type_1322 = join_type_1326
        this_502.table_1323 = table_1327
        this_502.on_condition_1324 = on_condition_1328
    @property
    def join_type(this_2361) -> 'JoinType':
        return this_2361.join_type_1322
    @property
    def table(this_2364) -> 'SafeIdentifier':
        return this_2364.table_1323
    @property
    def on_condition(this_2367) -> 'Union35[SqlFragment, None]':
        return this_2367.on_condition_1324
class NullsPosition(metaclass = ABCMeta37):
    def keyword(this_320) -> 'str34':
        raise RuntimeError39()
class NullsFirst(NullsPosition):
    __slots__ = ()
    def keyword(this_321) -> 'str34':
        return ' NULLS FIRST'
    def __init__(this_506) -> None:
        pass
class NullsLast(NullsPosition):
    __slots__ = ()
    def keyword(this_322) -> 'str34':
        return ' NULLS LAST'
    def __init__(this_509) -> None:
        pass
class OrderClause:
    field_1337: 'SafeIdentifier'
    ascending_1338: 'bool42'
    nulls_pos_1339: 'Union35[NullsPosition, None]'
    __slots__ = ('field_1337', 'ascending_1338', 'nulls_pos_1339')
    def __init__(this_512, field_1341: 'SafeIdentifier', ascending_1342: 'bool42', nulls_pos_1343: 'Union35[NullsPosition, None]') -> None:
        this_512.field_1337 = field_1341
        this_512.ascending_1338 = ascending_1342
        this_512.nulls_pos_1339 = nulls_pos_1343
    @property
    def field(this_2370) -> 'SafeIdentifier':
        return this_2370.field_1337
    @property
    def ascending(this_2373) -> 'bool42':
        return this_2373.ascending_1338
    @property
    def nulls_pos(this_2376) -> 'Union35[NullsPosition, None]':
        return this_2376.nulls_pos_1339
class LockMode(metaclass = ABCMeta37):
    def keyword(this_323) -> 'str34':
        raise RuntimeError39()
class ForUpdate(LockMode):
    __slots__ = ()
    def keyword(this_324) -> 'str34':
        return ' FOR UPDATE'
    def __init__(this_516) -> None:
        pass
class ForShare(LockMode):
    __slots__ = ()
    def keyword(this_325) -> 'str34':
        return ' FOR SHARE'
    def __init__(this_519) -> None:
        pass
class WhereClause(metaclass = ABCMeta37):
    def keyword(this_327) -> 'str34':
        raise RuntimeError39()
class AndCondition(WhereClause):
    condition_1356: 'SqlFragment'
    __slots__ = ('condition_1356',)
    @property
    def condition(this_328) -> 'SqlFragment':
        return this_328.condition_1356
    def keyword(this_329) -> 'str34':
        return 'AND'
    def __init__(this_526, condition_1362: 'SqlFragment') -> None:
        this_526.condition_1356 = condition_1362
class OrCondition(WhereClause):
    condition_1363: 'SqlFragment'
    __slots__ = ('condition_1363',)
    @property
    def condition(this_330) -> 'SqlFragment':
        return this_330.condition_1363
    def keyword(this_331) -> 'str34':
        return 'OR'
    def __init__(this_531, condition_1369: 'SqlFragment') -> None:
        this_531.condition_1363 = condition_1369
class Query:
    table_name_1387: 'SafeIdentifier'
    conditions_1388: 'Sequence38[WhereClause]'
    selected_fields_1389: 'Sequence38[SafeIdentifier]'
    order_clauses_1390: 'Sequence38[OrderClause]'
    limit_val_1391: 'Union35[int40, None]'
    offset_val_1392: 'Union35[int40, None]'
    join_clauses_1393: 'Sequence38[JoinClause]'
    group_by_fields_1394: 'Sequence38[SafeIdentifier]'
    having_conditions_1395: 'Sequence38[WhereClause]'
    is_distinct_1396: 'bool42'
    select_exprs_1397: 'Sequence38[SqlFragment]'
    lock_mode_1398: 'Union35[LockMode, None]'
    __slots__ = ('table_name_1387', 'conditions_1388', 'selected_fields_1389', 'order_clauses_1390', 'limit_val_1391', 'offset_val_1392', 'join_clauses_1393', 'group_by_fields_1394', 'having_conditions_1395', 'is_distinct_1396', 'select_exprs_1397', 'lock_mode_1398')
    def where(this_332, condition_1400: 'SqlFragment') -> 'Query':
        nb_1402: 'MutableSequence43[WhereClause]' = list_17379(this_332.conditions_1388)
        nb_1402.append(AndCondition(condition_1400))
        return Query(this_332.table_name_1387, tuple_17381(nb_1402), this_332.selected_fields_1389, this_332.order_clauses_1390, this_332.limit_val_1391, this_332.offset_val_1392, this_332.join_clauses_1393, this_332.group_by_fields_1394, this_332.having_conditions_1395, this_332.is_distinct_1396, this_332.select_exprs_1397, this_332.lock_mode_1398)
    def or_where(this_333, condition_1404: 'SqlFragment') -> 'Query':
        nb_1406: 'MutableSequence43[WhereClause]' = list_17379(this_333.conditions_1388)
        nb_1406.append(OrCondition(condition_1404))
        return Query(this_333.table_name_1387, tuple_17381(nb_1406), this_333.selected_fields_1389, this_333.order_clauses_1390, this_333.limit_val_1391, this_333.offset_val_1392, this_333.join_clauses_1393, this_333.group_by_fields_1394, this_333.having_conditions_1395, this_333.is_distinct_1396, this_333.select_exprs_1397, this_333.lock_mode_1398)
    def where_null(this_334, field_1408: 'SafeIdentifier') -> 'Query':
        b_1410: 'SqlBuilder' = SqlBuilder()
        b_1410.append_safe(field_1408.sql_value)
        b_1410.append_safe(' IS NULL')
        t_15470: 'SqlFragment' = b_1410.accumulated
        return this_334.where(t_15470)
    def where_not_null(this_335, field_1412: 'SafeIdentifier') -> 'Query':
        b_1414: 'SqlBuilder' = SqlBuilder()
        b_1414.append_safe(field_1412.sql_value)
        b_1414.append_safe(' IS NOT NULL')
        t_15464: 'SqlFragment' = b_1414.accumulated
        return this_335.where(t_15464)
    def where_in(this_336, field_1416: 'SafeIdentifier', values_1417: 'Sequence38[SqlPart]') -> 'Query':
        return_555: 'Query'
        t_15445: 'SqlFragment'
        t_15453: 'int40'
        t_15458: 'SqlFragment'
        with Label45() as fn_1418:
            if not values_1417:
                b_1419: 'SqlBuilder' = SqlBuilder()
                b_1419.append_safe('1 = 0')
                t_15445 = b_1419.accumulated
                return_555 = this_336.where(t_15445)
                fn_1418.break_()
            b_1420: 'SqlBuilder' = SqlBuilder()
            b_1420.append_safe(field_1416.sql_value)
            b_1420.append_safe(' IN (')
            b_1420.append_part(list_get_17397(values_1417, 0))
            i_1421: 'int40' = 1
            while True:
                t_15453 = len_17389(values_1417)
                if not i_1421 < t_15453:
                    break
                b_1420.append_safe(', ')
                b_1420.append_part(list_get_17397(values_1417, i_1421))
                i_1421 = int_add_17398(i_1421, 1)
            b_1420.append_safe(')')
            t_15458 = b_1420.accumulated
            return_555 = this_336.where(t_15458)
        return return_555
    def where_in_subquery(this_337, field_1423: 'SafeIdentifier', sub_1424: 'Query') -> 'Query':
        b_1426: 'SqlBuilder' = SqlBuilder()
        b_1426.append_safe(field_1423.sql_value)
        b_1426.append_safe(' IN (')
        b_1426.append_fragment(sub_1424.to_sql())
        b_1426.append_safe(')')
        t_15440: 'SqlFragment' = b_1426.accumulated
        return this_337.where(t_15440)
    def where_not(this_338, condition_1428: 'SqlFragment') -> 'Query':
        b_1430: 'SqlBuilder' = SqlBuilder()
        b_1430.append_safe('NOT (')
        b_1430.append_fragment(condition_1428)
        b_1430.append_safe(')')
        t_15431: 'SqlFragment' = b_1430.accumulated
        return this_338.where(t_15431)
    def where_between(this_339, field_1432: 'SafeIdentifier', low_1433: 'SqlPart', high_1434: 'SqlPart') -> 'Query':
        b_1436: 'SqlBuilder' = SqlBuilder()
        b_1436.append_safe(field_1432.sql_value)
        b_1436.append_safe(' BETWEEN ')
        b_1436.append_part(low_1433)
        b_1436.append_safe(' AND ')
        b_1436.append_part(high_1434)
        t_15425: 'SqlFragment' = b_1436.accumulated
        return this_339.where(t_15425)
    def where_like(this_340, field_1438: 'SafeIdentifier', pattern_1439: 'str34') -> 'Query':
        b_1441: 'SqlBuilder' = SqlBuilder()
        b_1441.append_safe(field_1438.sql_value)
        b_1441.append_safe(' LIKE ')
        b_1441.append_string(pattern_1439)
        t_15416: 'SqlFragment' = b_1441.accumulated
        return this_340.where(t_15416)
    def where_i_like(this_341, field_1443: 'SafeIdentifier', pattern_1444: 'str34') -> 'Query':
        b_1446: 'SqlBuilder' = SqlBuilder()
        b_1446.append_safe(field_1443.sql_value)
        b_1446.append_safe(' ILIKE ')
        b_1446.append_string(pattern_1444)
        t_15409: 'SqlFragment' = b_1446.accumulated
        return this_341.where(t_15409)
    def select(this_342, fields_1448: 'Sequence38[SafeIdentifier]') -> 'Query':
        return Query(this_342.table_name_1387, this_342.conditions_1388, fields_1448, this_342.order_clauses_1390, this_342.limit_val_1391, this_342.offset_val_1392, this_342.join_clauses_1393, this_342.group_by_fields_1394, this_342.having_conditions_1395, this_342.is_distinct_1396, this_342.select_exprs_1397, this_342.lock_mode_1398)
    def select_expr(this_343, exprs_1451: 'Sequence38[SqlFragment]') -> 'Query':
        return Query(this_343.table_name_1387, this_343.conditions_1388, this_343.selected_fields_1389, this_343.order_clauses_1390, this_343.limit_val_1391, this_343.offset_val_1392, this_343.join_clauses_1393, this_343.group_by_fields_1394, this_343.having_conditions_1395, this_343.is_distinct_1396, exprs_1451, this_343.lock_mode_1398)
    def order_by(this_344, field_1454: 'SafeIdentifier', ascending_1455: 'bool42') -> 'Query':
        nb_1457: 'MutableSequence43[OrderClause]' = list_17379(this_344.order_clauses_1390)
        nb_1457.append(OrderClause(field_1454, ascending_1455, None))
        return Query(this_344.table_name_1387, this_344.conditions_1388, this_344.selected_fields_1389, tuple_17381(nb_1457), this_344.limit_val_1391, this_344.offset_val_1392, this_344.join_clauses_1393, this_344.group_by_fields_1394, this_344.having_conditions_1395, this_344.is_distinct_1396, this_344.select_exprs_1397, this_344.lock_mode_1398)
    def order_by_nulls(this_345, field_1459: 'SafeIdentifier', ascending_1460: 'bool42', nulls_1461: 'NullsPosition') -> 'Query':
        nb_1463: 'MutableSequence43[OrderClause]' = list_17379(this_345.order_clauses_1390)
        nb_1463.append(OrderClause(field_1459, ascending_1460, nulls_1461))
        return Query(this_345.table_name_1387, this_345.conditions_1388, this_345.selected_fields_1389, tuple_17381(nb_1463), this_345.limit_val_1391, this_345.offset_val_1392, this_345.join_clauses_1393, this_345.group_by_fields_1394, this_345.having_conditions_1395, this_345.is_distinct_1396, this_345.select_exprs_1397, this_345.lock_mode_1398)
    def limit(this_346, n_1465: 'int40') -> 'Query':
        if n_1465 < 0:
            raise RuntimeError39()
        return Query(this_346.table_name_1387, this_346.conditions_1388, this_346.selected_fields_1389, this_346.order_clauses_1390, n_1465, this_346.offset_val_1392, this_346.join_clauses_1393, this_346.group_by_fields_1394, this_346.having_conditions_1395, this_346.is_distinct_1396, this_346.select_exprs_1397, this_346.lock_mode_1398)
    def offset(this_347, n_1468: 'int40') -> 'Query':
        if n_1468 < 0:
            raise RuntimeError39()
        return Query(this_347.table_name_1387, this_347.conditions_1388, this_347.selected_fields_1389, this_347.order_clauses_1390, this_347.limit_val_1391, n_1468, this_347.join_clauses_1393, this_347.group_by_fields_1394, this_347.having_conditions_1395, this_347.is_distinct_1396, this_347.select_exprs_1397, this_347.lock_mode_1398)
    def join(this_348, join_type_1471: 'JoinType', table_1472: 'SafeIdentifier', on_condition_1473: 'SqlFragment') -> 'Query':
        nb_1475: 'MutableSequence43[JoinClause]' = list_17379(this_348.join_clauses_1393)
        nb_1475.append(JoinClause(join_type_1471, table_1472, on_condition_1473))
        return Query(this_348.table_name_1387, this_348.conditions_1388, this_348.selected_fields_1389, this_348.order_clauses_1390, this_348.limit_val_1391, this_348.offset_val_1392, tuple_17381(nb_1475), this_348.group_by_fields_1394, this_348.having_conditions_1395, this_348.is_distinct_1396, this_348.select_exprs_1397, this_348.lock_mode_1398)
    def inner_join(this_349, table_1477: 'SafeIdentifier', on_condition_1478: 'SqlFragment') -> 'Query':
        t_15371: 'InnerJoin' = InnerJoin()
        return this_349.join(t_15371, table_1477, on_condition_1478)
    def left_join(this_350, table_1481: 'SafeIdentifier', on_condition_1482: 'SqlFragment') -> 'Query':
        t_15369: 'LeftJoin' = LeftJoin()
        return this_350.join(t_15369, table_1481, on_condition_1482)
    def right_join(this_351, table_1485: 'SafeIdentifier', on_condition_1486: 'SqlFragment') -> 'Query':
        t_15367: 'RightJoin' = RightJoin()
        return this_351.join(t_15367, table_1485, on_condition_1486)
    def full_join(this_352, table_1489: 'SafeIdentifier', on_condition_1490: 'SqlFragment') -> 'Query':
        t_15365: 'FullJoin' = FullJoin()
        return this_352.join(t_15365, table_1489, on_condition_1490)
    def cross_join(this_353, table_1493: 'SafeIdentifier') -> 'Query':
        nb_1495: 'MutableSequence43[JoinClause]' = list_17379(this_353.join_clauses_1393)
        nb_1495.append(JoinClause(CrossJoin(), table_1493, None))
        return Query(this_353.table_name_1387, this_353.conditions_1388, this_353.selected_fields_1389, this_353.order_clauses_1390, this_353.limit_val_1391, this_353.offset_val_1392, tuple_17381(nb_1495), this_353.group_by_fields_1394, this_353.having_conditions_1395, this_353.is_distinct_1396, this_353.select_exprs_1397, this_353.lock_mode_1398)
    def group_by(this_354, field_1497: 'SafeIdentifier') -> 'Query':
        nb_1499: 'MutableSequence43[SafeIdentifier]' = list_17379(this_354.group_by_fields_1394)
        nb_1499.append(field_1497)
        return Query(this_354.table_name_1387, this_354.conditions_1388, this_354.selected_fields_1389, this_354.order_clauses_1390, this_354.limit_val_1391, this_354.offset_val_1392, this_354.join_clauses_1393, tuple_17381(nb_1499), this_354.having_conditions_1395, this_354.is_distinct_1396, this_354.select_exprs_1397, this_354.lock_mode_1398)
    def having(this_355, condition_1501: 'SqlFragment') -> 'Query':
        nb_1503: 'MutableSequence43[WhereClause]' = list_17379(this_355.having_conditions_1395)
        nb_1503.append(AndCondition(condition_1501))
        return Query(this_355.table_name_1387, this_355.conditions_1388, this_355.selected_fields_1389, this_355.order_clauses_1390, this_355.limit_val_1391, this_355.offset_val_1392, this_355.join_clauses_1393, this_355.group_by_fields_1394, tuple_17381(nb_1503), this_355.is_distinct_1396, this_355.select_exprs_1397, this_355.lock_mode_1398)
    def or_having(this_356, condition_1505: 'SqlFragment') -> 'Query':
        nb_1507: 'MutableSequence43[WhereClause]' = list_17379(this_356.having_conditions_1395)
        nb_1507.append(OrCondition(condition_1505))
        return Query(this_356.table_name_1387, this_356.conditions_1388, this_356.selected_fields_1389, this_356.order_clauses_1390, this_356.limit_val_1391, this_356.offset_val_1392, this_356.join_clauses_1393, this_356.group_by_fields_1394, tuple_17381(nb_1507), this_356.is_distinct_1396, this_356.select_exprs_1397, this_356.lock_mode_1398)
    def distinct(this_357) -> 'Query':
        return Query(this_357.table_name_1387, this_357.conditions_1388, this_357.selected_fields_1389, this_357.order_clauses_1390, this_357.limit_val_1391, this_357.offset_val_1392, this_357.join_clauses_1393, this_357.group_by_fields_1394, this_357.having_conditions_1395, True, this_357.select_exprs_1397, this_357.lock_mode_1398)
    def lock(this_358, mode_1511: 'LockMode') -> 'Query':
        return Query(this_358.table_name_1387, this_358.conditions_1388, this_358.selected_fields_1389, this_358.order_clauses_1390, this_358.limit_val_1391, this_358.offset_val_1392, this_358.join_clauses_1393, this_358.group_by_fields_1394, this_358.having_conditions_1395, this_358.is_distinct_1396, this_358.select_exprs_1397, mode_1511)
    def to_sql(this_359) -> 'SqlFragment':
        t_15287: 'int40'
        b_1515: 'SqlBuilder' = SqlBuilder()
        if this_359.is_distinct_1396:
            b_1515.append_safe('SELECT DISTINCT ')
        else:
            b_1515.append_safe('SELECT ')
        if not (not this_359.select_exprs_1397):
            b_1515.append_fragment(list_get_17397(this_359.select_exprs_1397, 0))
            i_1516: 'int40' = 1
            while True:
                t_15287 = len_17389(this_359.select_exprs_1397)
                if not i_1516 < t_15287:
                    break
                b_1515.append_safe(', ')
                b_1515.append_fragment(list_get_17397(this_359.select_exprs_1397, i_1516))
                i_1516 = int_add_17398(i_1516, 1)
        elif not this_359.selected_fields_1389:
            b_1515.append_safe('*')
        else:
            def fn_15280(f_1517: 'SafeIdentifier') -> 'str34':
                return f_1517.sql_value
            b_1515.append_safe(list_join_17413(this_359.selected_fields_1389, ', ', fn_15280))
        b_1515.append_safe(' FROM ')
        b_1515.append_safe(this_359.table_name_1387.sql_value)
        render_joins_706(b_1515, this_359.join_clauses_1393)
        render_where_705(b_1515, this_359.conditions_1388)
        render_group_by_707(b_1515, this_359.group_by_fields_1394)
        render_having_708(b_1515, this_359.having_conditions_1395)
        if not (not this_359.order_clauses_1390):
            b_1515.append_safe(' ORDER BY ')
            first_1518: 'bool42' = True
            def fn_15279(orc_1519: 'OrderClause') -> 'None':
                nonlocal first_1518
                t_15276: 'str34'
                t_7962: 'str34'
                if not first_1518:
                    b_1515.append_safe(', ')
                first_1518 = False
                t_15271: 'str34' = orc_1519.field.sql_value
                b_1515.append_safe(t_15271)
                if orc_1519.ascending:
                    t_7962 = ' ASC'
                else:
                    t_7962 = ' DESC'
                b_1515.append_safe(t_7962)
                np_1520: 'Union35[NullsPosition, None]' = orc_1519.nulls_pos
                if not np_1520 is None:
                    t_15276 = np_1520.keyword()
                    b_1515.append_safe(t_15276)
            list_for_each_17386(this_359.order_clauses_1390, fn_15279)
        lv_1521: 'Union35[int40, None]' = this_359.limit_val_1391
        if not lv_1521 is None:
            lv_2846: 'int40' = lv_1521
            b_1515.append_safe(' LIMIT ')
            b_1515.append_int32(lv_2846)
        ov_1522: 'Union35[int40, None]' = this_359.offset_val_1392
        if not ov_1522 is None:
            ov_2847: 'int40' = ov_1522
            b_1515.append_safe(' OFFSET ')
            b_1515.append_int32(ov_2847)
        lm_1523: 'Union35[LockMode, None]' = this_359.lock_mode_1398
        if not lm_1523 is None:
            b_1515.append_safe(lm_1523.keyword())
        return b_1515.accumulated
    def count_sql(this_360) -> 'SqlFragment':
        b_1526: 'SqlBuilder' = SqlBuilder()
        b_1526.append_safe('SELECT COUNT(*) FROM ')
        b_1526.append_safe(this_360.table_name_1387.sql_value)
        render_joins_706(b_1526, this_360.join_clauses_1393)
        render_where_705(b_1526, this_360.conditions_1388)
        render_group_by_707(b_1526, this_360.group_by_fields_1394)
        render_having_708(b_1526, this_360.having_conditions_1395)
        return b_1526.accumulated
    def safe_to_sql(this_361, default_limit_1528: 'int40') -> 'SqlFragment':
        return_580: 'SqlFragment'
        t_7946: 'Query'
        if default_limit_1528 < 0:
            raise RuntimeError39()
        if not this_361.limit_val_1391 is None:
            return_580 = this_361.to_sql()
        else:
            t_7946 = this_361.limit(default_limit_1528)
            return_580 = t_7946.to_sql()
        return return_580
    def __init__(this_539, table_name_1531: 'SafeIdentifier', conditions_1532: 'Sequence38[WhereClause]', selected_fields_1533: 'Sequence38[SafeIdentifier]', order_clauses_1534: 'Sequence38[OrderClause]', limit_val_1535: 'Union35[int40, None]', offset_val_1536: 'Union35[int40, None]', join_clauses_1537: 'Sequence38[JoinClause]', group_by_fields_1538: 'Sequence38[SafeIdentifier]', having_conditions_1539: 'Sequence38[WhereClause]', is_distinct_1540: 'bool42', select_exprs_1541: 'Sequence38[SqlFragment]', lock_mode_1542: 'Union35[LockMode, None]') -> None:
        this_539.table_name_1387 = table_name_1531
        this_539.conditions_1388 = conditions_1532
        this_539.selected_fields_1389 = selected_fields_1533
        this_539.order_clauses_1390 = order_clauses_1534
        this_539.limit_val_1391 = limit_val_1535
        this_539.offset_val_1392 = offset_val_1536
        this_539.join_clauses_1393 = join_clauses_1537
        this_539.group_by_fields_1394 = group_by_fields_1538
        this_539.having_conditions_1395 = having_conditions_1539
        this_539.is_distinct_1396 = is_distinct_1540
        this_539.select_exprs_1397 = select_exprs_1541
        this_539.lock_mode_1398 = lock_mode_1542
    @property
    def table_name(this_2379) -> 'SafeIdentifier':
        return this_2379.table_name_1387
    @property
    def conditions(this_2382) -> 'Sequence38[WhereClause]':
        return this_2382.conditions_1388
    @property
    def selected_fields(this_2385) -> 'Sequence38[SafeIdentifier]':
        return this_2385.selected_fields_1389
    @property
    def order_clauses(this_2388) -> 'Sequence38[OrderClause]':
        return this_2388.order_clauses_1390
    @property
    def limit_val(this_2391) -> 'Union35[int40, None]':
        return this_2391.limit_val_1391
    @property
    def offset_val(this_2394) -> 'Union35[int40, None]':
        return this_2394.offset_val_1392
    @property
    def join_clauses(this_2397) -> 'Sequence38[JoinClause]':
        return this_2397.join_clauses_1393
    @property
    def group_by_fields(this_2400) -> 'Sequence38[SafeIdentifier]':
        return this_2400.group_by_fields_1394
    @property
    def having_conditions(this_2403) -> 'Sequence38[WhereClause]':
        return this_2403.having_conditions_1395
    @property
    def is_distinct(this_2406) -> 'bool42':
        return this_2406.is_distinct_1396
    @property
    def select_exprs(this_2409) -> 'Sequence38[SqlFragment]':
        return this_2409.select_exprs_1397
    @property
    def lock_mode(this_2412) -> 'Union35[LockMode, None]':
        return this_2412.lock_mode_1398
class SetClause:
    field_1589: 'SafeIdentifier'
    value_1590: 'SqlPart'
    __slots__ = ('field_1589', 'value_1590')
    def __init__(this_595, field_1592: 'SafeIdentifier', value_1593: 'SqlPart') -> None:
        this_595.field_1589 = field_1592
        this_595.value_1590 = value_1593
    @property
    def field(this_2415) -> 'SafeIdentifier':
        return this_2415.field_1589
    @property
    def value(this_2418) -> 'SqlPart':
        return this_2418.value_1590
class UpdateQuery:
    table_name_1594: 'SafeIdentifier'
    set_clauses_1595: 'Sequence38[SetClause]'
    conditions_1596: 'Sequence38[WhereClause]'
    limit_val_1597: 'Union35[int40, None]'
    __slots__ = ('table_name_1594', 'set_clauses_1595', 'conditions_1596', 'limit_val_1597')
    def set(this_362, field_1599: 'SafeIdentifier', value_1600: 'SqlPart') -> 'UpdateQuery':
        nb_1602: 'MutableSequence43[SetClause]' = list_17379(this_362.set_clauses_1595)
        nb_1602.append(SetClause(field_1599, value_1600))
        return UpdateQuery(this_362.table_name_1594, tuple_17381(nb_1602), this_362.conditions_1596, this_362.limit_val_1597)
    def where(this_363, condition_1604: 'SqlFragment') -> 'UpdateQuery':
        nb_1606: 'MutableSequence43[WhereClause]' = list_17379(this_363.conditions_1596)
        nb_1606.append(AndCondition(condition_1604))
        return UpdateQuery(this_363.table_name_1594, this_363.set_clauses_1595, tuple_17381(nb_1606), this_363.limit_val_1597)
    def or_where(this_364, condition_1608: 'SqlFragment') -> 'UpdateQuery':
        nb_1610: 'MutableSequence43[WhereClause]' = list_17379(this_364.conditions_1596)
        nb_1610.append(OrCondition(condition_1608))
        return UpdateQuery(this_364.table_name_1594, this_364.set_clauses_1595, tuple_17381(nb_1610), this_364.limit_val_1597)
    def limit(this_365, n_1612: 'int40') -> 'UpdateQuery':
        if n_1612 < 0:
            raise RuntimeError39()
        return UpdateQuery(this_365.table_name_1594, this_365.set_clauses_1595, this_365.conditions_1596, n_1612)
    def to_sql(this_366) -> 'SqlFragment':
        t_15132: 'int40'
        if not this_366.conditions_1596:
            raise RuntimeError39()
        if not this_366.set_clauses_1595:
            raise RuntimeError39()
        b_1616: 'SqlBuilder' = SqlBuilder()
        b_1616.append_safe('UPDATE ')
        b_1616.append_safe(this_366.table_name_1594.sql_value)
        b_1616.append_safe(' SET ')
        b_1616.append_safe(list_get_17397(this_366.set_clauses_1595, 0).field.sql_value)
        b_1616.append_safe(' = ')
        b_1616.append_part(list_get_17397(this_366.set_clauses_1595, 0).value)
        i_1617: 'int40' = 1
        while True:
            t_15132 = len_17389(this_366.set_clauses_1595)
            if not i_1617 < t_15132:
                break
            b_1616.append_safe(', ')
            b_1616.append_safe(list_get_17397(this_366.set_clauses_1595, i_1617).field.sql_value)
            b_1616.append_safe(' = ')
            b_1616.append_part(list_get_17397(this_366.set_clauses_1595, i_1617).value)
            i_1617 = int_add_17398(i_1617, 1)
        render_where_705(b_1616, this_366.conditions_1596)
        lv_1618: 'Union35[int40, None]' = this_366.limit_val_1597
        if not lv_1618 is None:
            lv_2849: 'int40' = lv_1618
            b_1616.append_safe(' LIMIT ')
            b_1616.append_int32(lv_2849)
        return b_1616.accumulated
    def __init__(this_597, table_name_1620: 'SafeIdentifier', set_clauses_1621: 'Sequence38[SetClause]', conditions_1622: 'Sequence38[WhereClause]', limit_val_1623: 'Union35[int40, None]') -> None:
        this_597.table_name_1594 = table_name_1620
        this_597.set_clauses_1595 = set_clauses_1621
        this_597.conditions_1596 = conditions_1622
        this_597.limit_val_1597 = limit_val_1623
    @property
    def table_name(this_2421) -> 'SafeIdentifier':
        return this_2421.table_name_1594
    @property
    def set_clauses(this_2424) -> 'Sequence38[SetClause]':
        return this_2424.set_clauses_1595
    @property
    def conditions(this_2427) -> 'Sequence38[WhereClause]':
        return this_2427.conditions_1596
    @property
    def limit_val(this_2430) -> 'Union35[int40, None]':
        return this_2430.limit_val_1597
class DeleteQuery:
    table_name_1624: 'SafeIdentifier'
    conditions_1625: 'Sequence38[WhereClause]'
    limit_val_1626: 'Union35[int40, None]'
    __slots__ = ('table_name_1624', 'conditions_1625', 'limit_val_1626')
    def where(this_367, condition_1628: 'SqlFragment') -> 'DeleteQuery':
        nb_1630: 'MutableSequence43[WhereClause]' = list_17379(this_367.conditions_1625)
        nb_1630.append(AndCondition(condition_1628))
        return DeleteQuery(this_367.table_name_1624, tuple_17381(nb_1630), this_367.limit_val_1626)
    def or_where(this_368, condition_1632: 'SqlFragment') -> 'DeleteQuery':
        nb_1634: 'MutableSequence43[WhereClause]' = list_17379(this_368.conditions_1625)
        nb_1634.append(OrCondition(condition_1632))
        return DeleteQuery(this_368.table_name_1624, tuple_17381(nb_1634), this_368.limit_val_1626)
    def limit(this_369, n_1636: 'int40') -> 'DeleteQuery':
        if n_1636 < 0:
            raise RuntimeError39()
        return DeleteQuery(this_369.table_name_1624, this_369.conditions_1625, n_1636)
    def to_sql(this_370) -> 'SqlFragment':
        if not this_370.conditions_1625:
            raise RuntimeError39()
        b_1640: 'SqlBuilder' = SqlBuilder()
        b_1640.append_safe('DELETE FROM ')
        b_1640.append_safe(this_370.table_name_1624.sql_value)
        render_where_705(b_1640, this_370.conditions_1625)
        lv_1641: 'Union35[int40, None]' = this_370.limit_val_1626
        if not lv_1641 is None:
            lv_2850: 'int40' = lv_1641
            b_1640.append_safe(' LIMIT ')
            b_1640.append_int32(lv_2850)
        return b_1640.accumulated
    def __init__(this_607, table_name_1643: 'SafeIdentifier', conditions_1644: 'Sequence38[WhereClause]', limit_val_1645: 'Union35[int40, None]') -> None:
        this_607.table_name_1624 = table_name_1643
        this_607.conditions_1625 = conditions_1644
        this_607.limit_val_1626 = limit_val_1645
    @property
    def table_name(this_2433) -> 'SafeIdentifier':
        return this_2433.table_name_1624
    @property
    def conditions(this_2436) -> 'Sequence38[WhereClause]':
        return this_2436.conditions_1625
    @property
    def limit_val(this_2439) -> 'Union35[int40, None]':
        return this_2439.limit_val_1626
class SafeIdentifier(metaclass = ABCMeta37):
    pass
class ValidatedIdentifier_372(SafeIdentifier):
    value_1901: 'str34'
    __slots__ = ('value_1901',)
    @property
    def sql_value(this_373) -> 'str34':
        return this_373.value_1901
    def __init__(this_621, value_1905: 'str34') -> None:
        this_621.value_1901 = value_1905
class FieldType(metaclass = ABCMeta37):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_627) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_629) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_631) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_633) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_635) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_637) -> None:
        pass
class FieldDef:
    name_1919: 'SafeIdentifier'
    field_type_1920: 'FieldType'
    nullable_1921: 'bool42'
    default_value_1922: 'Union35[SqlPart, None]'
    virtual_1923: 'bool42'
    __slots__ = ('name_1919', 'field_type_1920', 'nullable_1921', 'default_value_1922', 'virtual_1923')
    def __init__(this_639, name_1925: 'SafeIdentifier', field_type_1926: 'FieldType', nullable_1927: 'bool42', default_value_1928: 'Union35[SqlPart, None]', virtual_1929: 'bool42') -> None:
        this_639.name_1919 = name_1925
        this_639.field_type_1920 = field_type_1926
        this_639.nullable_1921 = nullable_1927
        this_639.default_value_1922 = default_value_1928
        this_639.virtual_1923 = virtual_1929
    @property
    def name(this_2225) -> 'SafeIdentifier':
        return this_2225.name_1919
    @property
    def field_type(this_2228) -> 'FieldType':
        return this_2228.field_type_1920
    @property
    def nullable(this_2231) -> 'bool42':
        return this_2231.nullable_1921
    @property
    def default_value(this_2234) -> 'Union35[SqlPart, None]':
        return this_2234.default_value_1922
    @property
    def virtual(this_2237) -> 'bool42':
        return this_2237.virtual_1923
class TableDef:
    table_name_1930: 'SafeIdentifier'
    fields_1931: 'Sequence38[FieldDef]'
    primary_key_1932: 'Union35[SafeIdentifier, None]'
    __slots__ = ('table_name_1930', 'fields_1931', 'primary_key_1932')
    def field(this_374, name_1934: 'str34') -> 'FieldDef':
        return_646: 'FieldDef'
        with Label45() as fn_1935:
            this_10148: 'Sequence38[FieldDef]' = this_374.fields_1931
            n_10149: 'int40' = len_17389(this_10148)
            i_10150: 'int40' = 0
            while i_10150 < n_10149:
                el_10151: 'FieldDef' = list_get_17397(this_10148, i_10150)
                i_10150 = int_add_17398(i_10150, 1)
                f_1936: 'FieldDef' = el_10151
                if f_1936.name.sql_value == name_1934:
                    return_646 = f_1936
                    fn_1935.break_()
            raise RuntimeError39()
        return return_646
    def pk_name(this_375) -> 'str34':
        return_647: 'str34'
        with Label45() as fn_1938:
            pk_1939: 'Union35[SafeIdentifier, None]' = this_375.primary_key_1932
            if not pk_1939 is None:
                pk_2830: 'SafeIdentifier' = pk_1939
                return_647 = pk_2830.sql_value
                fn_1938.break_()
            return_647 = 'id'
        return return_647
    def __init__(this_642, table_name_1941: 'SafeIdentifier', fields_1942: 'Sequence38[FieldDef]', primary_key_1943: 'Union35[SafeIdentifier, None]') -> None:
        this_642.table_name_1930 = table_name_1941
        this_642.fields_1931 = fields_1942
        this_642.primary_key_1932 = primary_key_1943
    @property
    def table_name(this_2240) -> 'SafeIdentifier':
        return this_2240.table_name_1930
    @property
    def fields(this_2243) -> 'Sequence38[FieldDef]':
        return this_2243.fields_1931
    @property
    def primary_key(this_2246) -> 'Union35[SafeIdentifier, None]':
        return this_2246.primary_key_1932
T_394 = TypeVar49('T_394', bound = Any48)
class SqlBuilder:
    buffer_1984: 'MutableSequence43[SqlPart]'
    __slots__ = ('buffer_1984',)
    def append_safe(this_376, sql_source_1986: 'str34') -> 'None':
        t_17339: 'SqlSource' = SqlSource(sql_source_1986)
        this_376.buffer_1984.append(t_17339)
    def append_fragment(this_377, fragment_1989: 'SqlFragment') -> 'None':
        t_17337: 'Sequence38[SqlPart]' = fragment_1989.parts
        list_builder_add_all_17414(this_377.buffer_1984, t_17337)
    def append_part(this_378, part_1992: 'SqlPart') -> 'None':
        this_378.buffer_1984.append(part_1992)
    def append_part_list(this_379, values_1995: 'Sequence38[SqlPart]') -> 'None':
        def fn_17333(x_1997: 'SqlPart') -> 'None':
            this_379.append_part(x_1997)
        this_379.append_list_2040(values_1995, fn_17333)
    def append_boolean(this_380, value_1999: 'bool42') -> 'None':
        t_17330: 'SqlBoolean' = SqlBoolean(value_1999)
        this_380.buffer_1984.append(t_17330)
    def append_boolean_list(this_381, values_2002: 'Sequence38[bool42]') -> 'None':
        def fn_17327(x_2004: 'bool42') -> 'None':
            this_381.append_boolean(x_2004)
        this_381.append_list_2040(values_2002, fn_17327)
    def append_date(this_382, value_2006: 'date33') -> 'None':
        t_17324: 'SqlDate' = SqlDate(value_2006)
        this_382.buffer_1984.append(t_17324)
    def append_date_list(this_383, values_2009: 'Sequence38[date33]') -> 'None':
        def fn_17321(x_2011: 'date33') -> 'None':
            this_383.append_date(x_2011)
        this_383.append_list_2040(values_2009, fn_17321)
    def append_float64(this_384, value_2013: 'float36') -> 'None':
        t_17318: 'SqlFloat64' = SqlFloat64(value_2013)
        this_384.buffer_1984.append(t_17318)
    def append_float64_list(this_385, values_2016: 'Sequence38[float36]') -> 'None':
        def fn_17315(x_2018: 'float36') -> 'None':
            this_385.append_float64(x_2018)
        this_385.append_list_2040(values_2016, fn_17315)
    def append_int32(this_386, value_2020: 'int40') -> 'None':
        t_17312: 'SqlInt32' = SqlInt32(value_2020)
        this_386.buffer_1984.append(t_17312)
    def append_int32_list(this_387, values_2023: 'Sequence38[int40]') -> 'None':
        def fn_17309(x_2025: 'int40') -> 'None':
            this_387.append_int32(x_2025)
        this_387.append_list_2040(values_2023, fn_17309)
    def append_int64(this_388, value_2027: 'int64_23') -> 'None':
        t_17306: 'SqlInt64' = SqlInt64(value_2027)
        this_388.buffer_1984.append(t_17306)
    def append_int64_list(this_389, values_2030: 'Sequence38[int64_23]') -> 'None':
        def fn_17303(x_2032: 'int64_23') -> 'None':
            this_389.append_int64(x_2032)
        this_389.append_list_2040(values_2030, fn_17303)
    def append_string(this_390, value_2034: 'str34') -> 'None':
        t_17300: 'SqlString' = SqlString(value_2034)
        this_390.buffer_1984.append(t_17300)
    def append_string_list(this_391, values_2037: 'Sequence38[str34]') -> 'None':
        def fn_17297(x_2039: 'str34') -> 'None':
            this_391.append_string(x_2039)
        this_391.append_list_2040(values_2037, fn_17297)
    def append_list_2040(this_392, values_2041: 'Sequence38[T_394]', append_value_2042: 'Callable50[[T_394], None]') -> 'None':
        t_17292: 'int40'
        t_17294: 'T_394'
        i_2044: 'int40' = 0
        while True:
            t_17292 = len_17389(values_2041)
            if not i_2044 < t_17292:
                break
            if i_2044 > 0:
                this_392.append_safe(', ')
            t_17294 = list_get_17397(values_2041, i_2044)
            append_value_2042(t_17294)
            i_2044 = int_add_17398(i_2044, 1)
    @property
    def accumulated(this_393) -> 'SqlFragment':
        return SqlFragment(tuple_17381(this_393.buffer_1984))
    def __init__(this_650) -> None:
        t_17289: 'MutableSequence43[SqlPart]' = list_17379()
        this_650.buffer_1984 = t_17289
class SqlFragment:
    parts_2051: 'Sequence38[SqlPart]'
    __slots__ = ('parts_2051',)
    def to_source(this_398) -> 'SqlSource':
        return SqlSource(this_398.to_string())
    def to_string(this_399) -> 'str34':
        t_17363: 'int40'
        builder_2056: 'list0[str34]' = ['']
        i_2057: 'int40' = 0
        while True:
            t_17363 = len_17389(this_399.parts_2051)
            if not i_2057 < t_17363:
                break
            list_get_17397(this_399.parts_2051, i_2057).format_to(builder_2056)
            i_2057 = int_add_17398(i_2057, 1)
        return ''.join(builder_2056)
    def __init__(this_671, parts_2059: 'Sequence38[SqlPart]') -> None:
        this_671.parts_2051 = parts_2059
    @property
    def parts(this_2252) -> 'Sequence38[SqlPart]':
        return this_2252.parts_2051
class SqlPart(metaclass = ABCMeta37):
    def format_to(this_400, builder_2061: 'list0[str34]') -> 'None':
        raise RuntimeError39()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    source_2063: 'str34'
    __slots__ = ('source_2063',)
    def format_to(this_401, builder_2065: 'list0[str34]') -> 'None':
        builder_2065.append(this_401.source_2063)
    def __init__(this_677, source_2068: 'str34') -> None:
        this_677.source_2063 = source_2068
    @property
    def source(this_2249) -> 'str34':
        return this_2249.source_2063
class SqlBoolean(SqlPart):
    value_2069: 'bool42'
    __slots__ = ('value_2069',)
    def format_to(this_402, builder_2071: 'list0[str34]') -> 'None':
        t_9792: 'str34'
        if this_402.value_2069:
            t_9792 = 'TRUE'
        else:
            t_9792 = 'FALSE'
        builder_2071.append(t_9792)
    def __init__(this_680, value_2074: 'bool42') -> None:
        this_680.value_2069 = value_2074
    @property
    def value(this_2255) -> 'bool42':
        return this_2255.value_2069
class SqlDate(SqlPart):
    value_2075: 'date33'
    __slots__ = ('value_2075',)
    def format_to(this_403, builder_2077: 'list0[str34]') -> 'None':
        builder_2077.append("'")
        t_17344: 'str34' = date_to_string_17418(this_403.value_2075)
        def fn_17342(c_2079: 'int40') -> 'None':
            if c_2079 == 39:
                builder_2077.append("''")
            else:
                builder_2077.append(string_from_code_point51(c_2079))
        string_for_each_17420(t_17344, fn_17342)
        builder_2077.append("'")
    def __init__(this_683, value_2081: 'date33') -> None:
        this_683.value_2075 = value_2081
    @property
    def value(this_2270) -> 'date33':
        return this_2270.value_2075
class SqlFloat64(SqlPart):
    value_2082: 'float36'
    __slots__ = ('value_2082',)
    def format_to(this_404, builder_2084: 'list0[str34]') -> 'None':
        t_9781: 'bool42'
        t_9782: 'bool42'
        s_2086: 'str34' = float64_to_string_17400(this_404.value_2082)
        if s_2086 == 'NaN':
            t_9782 = True
        else:
            if s_2086 == 'Infinity':
                t_9781 = True
            else:
                t_9781 = s_2086 == '-Infinity'
            t_9782 = t_9781
        if t_9782:
            builder_2084.append('NULL')
        else:
            builder_2084.append(s_2086)
    def __init__(this_686, value_2088: 'float36') -> None:
        this_686.value_2082 = value_2088
    @property
    def value(this_2267) -> 'float36':
        return this_2267.value_2082
class SqlInt32(SqlPart):
    value_2089: 'int40'
    __slots__ = ('value_2089',)
    def format_to(this_405, builder_2091: 'list0[str34]') -> 'None':
        t_17353: 'str34' = int_to_string_17391(this_405.value_2089)
        builder_2091.append(t_17353)
    def __init__(this_689, value_2094: 'int40') -> None:
        this_689.value_2089 = value_2094
    @property
    def value(this_2261) -> 'int40':
        return this_2261.value_2089
class SqlInt64(SqlPart):
    value_2095: 'int64_23'
    __slots__ = ('value_2095',)
    def format_to(this_406, builder_2097: 'list0[str34]') -> 'None':
        t_17351: 'str34' = int_to_string_17391(this_406.value_2095)
        builder_2097.append(t_17351)
    def __init__(this_692, value_2100: 'int64_23') -> None:
        this_692.value_2095 = value_2100
    @property
    def value(this_2264) -> 'int64_23':
        return this_2264.value_2095
class SqlDefault(SqlPart):
    '`SqlDefault` renders the literal SQL keyword `DEFAULT`, used for columns\nwith server-side default values (e.g., `NOW()` for timestamps).'
    __slots__ = ()
    def format_to(this_407, builder_2102: 'list0[str34]') -> 'None':
        builder_2102.append('DEFAULT')
    def __init__(this_695) -> None:
        pass
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_2105: 'str34'
    __slots__ = ('value_2105',)
    def format_to(this_408, builder_2107: 'list0[str34]') -> 'None':
        builder_2107.append("'")
        def fn_17356(c_2109: 'int40') -> 'None':
            if c_2109 == 39:
                builder_2107.append("''")
            else:
                builder_2107.append(string_from_code_point51(c_2109))
        string_for_each_17420(this_408.value_2105, fn_17356)
        builder_2107.append("'")
    def __init__(this_698, value_2111: 'str34') -> None:
        this_698.value_2105 = value_2111
    @property
    def value(this_2258) -> 'str34':
        return this_2258.value_2105
def changeset(table_def_982: 'TableDef', params_983: 'MappingProxyType41[str34, str34]') -> 'Changeset':
    t_17003: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
    return ChangesetImpl_286(table_def_982, params_983, t_17003, (), True)
def is_ident_start_710(c_1906: 'int40') -> 'bool42':
    return_624: 'bool42'
    t_9433: 'bool42'
    t_9434: 'bool42'
    if c_1906 >= 97:
        t_9433 = c_1906 <= 122
    else:
        t_9433 = False
    if t_9433:
        return_624 = True
    else:
        if c_1906 >= 65:
            t_9434 = c_1906 <= 90
        else:
            t_9434 = False
        if t_9434:
            return_624 = True
        else:
            return_624 = c_1906 == 95
    return return_624
def is_ident_part_711(c_1908: 'int40') -> 'bool42':
    return_625: 'bool42'
    if is_ident_start_710(c_1908):
        return_625 = True
    elif c_1908 >= 48:
        return_625 = c_1908 <= 57
    else:
        return_625 = False
    return return_625
def safe_identifier(name_1910: 'str34') -> 'SafeIdentifier':
    t_17001: 'int40'
    if not name_1910:
        raise RuntimeError39()
    idx_1912: 'int40' = 0
    if not is_ident_start_710(string_get_17411(name_1910, idx_1912)):
        raise RuntimeError39()
    t_16998: 'int40' = string_next_17409(name_1910, idx_1912)
    idx_1912 = t_16998
    while True:
        if not len6(name_1910) > idx_1912:
            break
        if not is_ident_part_711(string_get_17411(name_1910, idx_1912)):
            raise RuntimeError39()
        t_17001 = string_next_17409(name_1910, idx_1912)
        idx_1912 = t_17001
    return ValidatedIdentifier_372(name_1910)
def timestamps() -> 'Sequence38[FieldDef]':
    t_8692: 'SafeIdentifier'
    t_8692 = safe_identifier('inserted_at')
    t_16100: 'FieldDef' = FieldDef(t_8692, DateField(), True, SqlDefault(), False)
    t_8696: 'SafeIdentifier'
    t_8696 = safe_identifier('updated_at')
    return (t_16100, FieldDef(t_8696, DateField(), True, SqlDefault(), False))
def delete_sql(table_def_1301: 'TableDef', id_1302: 'int40') -> 'SqlFragment':
    b_1304: 'SqlBuilder' = SqlBuilder()
    b_1304.append_safe('DELETE FROM ')
    b_1304.append_safe(table_def_1301.table_name.sql_value)
    b_1304.append_safe(' WHERE ')
    b_1304.append_safe(table_def_1301.pk_name())
    b_1304.append_safe(' = ')
    b_1304.append_int32(id_1302)
    return b_1304.accumulated
def render_where_705(b_1370: 'SqlBuilder', conditions_1371: 'Sequence38[WhereClause]') -> 'None':
    t_15522: 'SqlFragment'
    t_15524: 'int40'
    t_15527: 'str34'
    t_15531: 'SqlFragment'
    if not (not conditions_1371):
        b_1370.append_safe(' WHERE ')
        t_15522 = list_get_17397(conditions_1371, 0).condition
        b_1370.append_fragment(t_15522)
        i_1373: 'int40' = 1
        while True:
            t_15524 = len_17389(conditions_1371)
            if not i_1373 < t_15524:
                break
            b_1370.append_safe(' ')
            t_15527 = list_get_17397(conditions_1371, i_1373).keyword()
            b_1370.append_safe(t_15527)
            b_1370.append_safe(' ')
            t_15531 = list_get_17397(conditions_1371, i_1373).condition
            b_1370.append_fragment(t_15531)
            i_1373 = int_add_17398(i_1373, 1)
def render_joins_706(b_1374: 'SqlBuilder', join_clauses_1375: 'Sequence38[JoinClause]') -> 'None':
    def fn_15516(jc_1377: 'JoinClause') -> 'None':
        b_1374.append_safe(' ')
        t_15507: 'str34' = jc_1377.join_type.keyword()
        b_1374.append_safe(t_15507)
        b_1374.append_safe(' ')
        t_15511: 'str34' = jc_1377.table.sql_value
        b_1374.append_safe(t_15511)
        oc_1378: 'Union35[SqlFragment, None]' = jc_1377.on_condition
        if not oc_1378 is None:
            oc_2844: 'SqlFragment' = oc_1378
            b_1374.append_safe(' ON ')
            b_1374.append_fragment(oc_2844)
    list_for_each_17386(join_clauses_1375, fn_15516)
def render_group_by_707(b_1379: 'SqlBuilder', group_by_fields_1380: 'Sequence38[SafeIdentifier]') -> 'None':
    t_15503: 'str34'
    if not (not group_by_fields_1380):
        b_1379.append_safe(' GROUP BY ')
        def fn_15499(f_1382: 'SafeIdentifier') -> 'str34':
            return f_1382.sql_value
        t_15503 = list_join_17413(group_by_fields_1380, ', ', fn_15499)
        b_1379.append_safe(t_15503)
def render_having_708(b_1383: 'SqlBuilder', having_conditions_1384: 'Sequence38[WhereClause]') -> 'None':
    t_15487: 'SqlFragment'
    t_15489: 'int40'
    t_15492: 'str34'
    t_15496: 'SqlFragment'
    if not (not having_conditions_1384):
        b_1383.append_safe(' HAVING ')
        t_15487 = list_get_17397(having_conditions_1384, 0).condition
        b_1383.append_fragment(t_15487)
        i_1386: 'int40' = 1
        while True:
            t_15489 = len_17389(having_conditions_1384)
            if not i_1386 < t_15489:
                break
            b_1383.append_safe(' ')
            t_15492 = list_get_17397(having_conditions_1384, i_1386).keyword()
            b_1383.append_safe(t_15492)
            b_1383.append_safe(' ')
            t_15496 = list_get_17397(having_conditions_1384, i_1386).condition
            b_1383.append_fragment(t_15496)
            i_1386 = int_add_17398(i_1386, 1)
def from_(table_name_1543: 'SafeIdentifier') -> 'Query':
    return Query(table_name_1543, (), (), (), None, None, (), (), (), False, (), None)
def col(table_1545: 'SafeIdentifier', column_1546: 'SafeIdentifier') -> 'SqlFragment':
    b_1548: 'SqlBuilder' = SqlBuilder()
    b_1548.append_safe(table_1545.sql_value)
    b_1548.append_safe('.')
    b_1548.append_safe(column_1546.sql_value)
    return b_1548.accumulated
def count_all() -> 'SqlFragment':
    b_1550: 'SqlBuilder' = SqlBuilder()
    b_1550.append_safe('COUNT(*)')
    return b_1550.accumulated
def count_col(field_1551: 'SafeIdentifier') -> 'SqlFragment':
    b_1553: 'SqlBuilder' = SqlBuilder()
    b_1553.append_safe('COUNT(')
    b_1553.append_safe(field_1551.sql_value)
    b_1553.append_safe(')')
    return b_1553.accumulated
def sum_col(field_1554: 'SafeIdentifier') -> 'SqlFragment':
    b_1556: 'SqlBuilder' = SqlBuilder()
    b_1556.append_safe('SUM(')
    b_1556.append_safe(field_1554.sql_value)
    b_1556.append_safe(')')
    return b_1556.accumulated
def avg_col(field_1557: 'SafeIdentifier') -> 'SqlFragment':
    b_1559: 'SqlBuilder' = SqlBuilder()
    b_1559.append_safe('AVG(')
    b_1559.append_safe(field_1557.sql_value)
    b_1559.append_safe(')')
    return b_1559.accumulated
def min_col(field_1560: 'SafeIdentifier') -> 'SqlFragment':
    b_1562: 'SqlBuilder' = SqlBuilder()
    b_1562.append_safe('MIN(')
    b_1562.append_safe(field_1560.sql_value)
    b_1562.append_safe(')')
    return b_1562.accumulated
def max_col(field_1563: 'SafeIdentifier') -> 'SqlFragment':
    b_1565: 'SqlBuilder' = SqlBuilder()
    b_1565.append_safe('MAX(')
    b_1565.append_safe(field_1563.sql_value)
    b_1565.append_safe(')')
    return b_1565.accumulated
def union_sql(a_1566: 'Query', b_1567: 'Query') -> 'SqlFragment':
    sb_1569: 'SqlBuilder' = SqlBuilder()
    sb_1569.append_safe('(')
    sb_1569.append_fragment(a_1566.to_sql())
    sb_1569.append_safe(') UNION (')
    sb_1569.append_fragment(b_1567.to_sql())
    sb_1569.append_safe(')')
    return sb_1569.accumulated
def union_all_sql(a_1570: 'Query', b_1571: 'Query') -> 'SqlFragment':
    sb_1573: 'SqlBuilder' = SqlBuilder()
    sb_1573.append_safe('(')
    sb_1573.append_fragment(a_1570.to_sql())
    sb_1573.append_safe(') UNION ALL (')
    sb_1573.append_fragment(b_1571.to_sql())
    sb_1573.append_safe(')')
    return sb_1573.accumulated
def intersect_sql(a_1574: 'Query', b_1575: 'Query') -> 'SqlFragment':
    sb_1577: 'SqlBuilder' = SqlBuilder()
    sb_1577.append_safe('(')
    sb_1577.append_fragment(a_1574.to_sql())
    sb_1577.append_safe(') INTERSECT (')
    sb_1577.append_fragment(b_1575.to_sql())
    sb_1577.append_safe(')')
    return sb_1577.accumulated
def except_sql(a_1578: 'Query', b_1579: 'Query') -> 'SqlFragment':
    sb_1581: 'SqlBuilder' = SqlBuilder()
    sb_1581.append_safe('(')
    sb_1581.append_fragment(a_1578.to_sql())
    sb_1581.append_safe(') EXCEPT (')
    sb_1581.append_fragment(b_1579.to_sql())
    sb_1581.append_safe(')')
    return sb_1581.accumulated
def subquery(q_1582: 'Query', alias_1583: 'SafeIdentifier') -> 'SqlFragment':
    b_1585: 'SqlBuilder' = SqlBuilder()
    b_1585.append_safe('(')
    b_1585.append_fragment(q_1582.to_sql())
    b_1585.append_safe(') AS ')
    b_1585.append_safe(alias_1583.sql_value)
    return b_1585.accumulated
def exists_sql(q_1586: 'Query') -> 'SqlFragment':
    b_1588: 'SqlBuilder' = SqlBuilder()
    b_1588.append_safe('EXISTS (')
    b_1588.append_fragment(q_1586.to_sql())
    b_1588.append_safe(')')
    return b_1588.accumulated
def update(table_name_1646: 'SafeIdentifier') -> 'UpdateQuery':
    return UpdateQuery(table_name_1646, (), (), None)
def delete_from(table_name_1648: 'SafeIdentifier') -> 'DeleteQuery':
    return DeleteQuery(table_name_1648, (), None)
