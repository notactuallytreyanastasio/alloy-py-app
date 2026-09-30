from builtins import str as str29, float as float31, RuntimeError as RuntimeError34, int as int35, bool as bool37, Exception as Exception41, len as len2, isinstance as isinstance42, list as list0, tuple as tuple1
from typing import Union as Union30, Sequence as Sequence33, MutableSequence as MutableSequence38, Dict as Dict39, Any as Any43, TypeVar as TypeVar44, Callable as Callable45
from abc import ABCMeta as ABCMeta32
from types import MappingProxyType as MappingProxyType36
from temper_core import Label as Label40, Pair as Pair27, string_from_code_point as string_from_code_point46, list_get as list_get3, int_add as int_add4, map_builder_set as map_builder_set5, mapped_to_map as mapped_to_map6, mapped_has as mapped_has7, string_count_between as string_count_between8, str_cat as str_cat9, int_to_string as int_to_string10, string_to_int32 as string_to_int3211, string_to_int64 as string_to_int6412, string_to_float64 as string_to_float6413, mapped_to_list as mapped_to_list14, float_cmp as float_cmp15, float64_to_string as float64_to_string16, float_eq as float_eq17, require_string_index as require_string_index18, int_sub as int_sub19, string_next as string_next20, string_get as string_get21, date_from_iso_string as date_from_iso_string22, list_join as list_join23, list_builder_add_all as list_builder_add_all24, date_to_string as date_to_string25, map_constructor as map_constructor26
from datetime import date as date28
_list_4170 = list0
_tuple_4172 = tuple1
_len_4174 = len2
_list_get_4175 = list_get3
_int_add_4176 = int_add4
_map_builder_set_4179 = map_builder_set5
_mapped_to_map_4180 = mapped_to_map6
_mapped_has_4181 = mapped_has7
_string_count_between_4182 = string_count_between8
_str_cat_4183 = str_cat9
_int_to_string_4184 = int_to_string10
_string_to_int32_4185 = string_to_int3211
_string_to_int64_4186 = string_to_int6412
_string_to_float64_4187 = string_to_float6413
_mapped_to_list_4188 = mapped_to_list14
_float_cmp_4189 = float_cmp15
_float64_to_string_4190 = float64_to_string16
_float_eq_4191 = float_eq17
_require_string_index_4194 = require_string_index18
_int_sub_4195 = int_sub19
_string_next_4196 = string_next20
_string_get_4198 = string_get21
_date_from_iso_string_4199 = date_from_iso_string22
_list_join_4200 = list_join23
_list_builder_add_all_4201 = list_builder_add_all24
_date_to_string_4205 = date_to_string25
_map_constructor_4207 = map_constructor26
_pair_4208 = Pair27
_date_4209 = date28
class ChangesetError:
    _field_748: 'str29'
    _message_749: 'str29'
    __slots__ = ('_field_748', '_message_749')
    def __init__(this, /, field: 'str29', message: 'str29') -> None:
        this._field_748 = field
        this._message_749 = message
    @property
    def field(this_2301, /) -> 'str29':
        return this_2301._field_748
    @property
    def message(this_2304, /) -> 'str29':
        return this_2304._message_749
class NumberValidationOpts:
    _greater_than_753: 'Union30[float31, None]'
    _less_than_754: 'Union30[float31, None]'
    _greater_than_or_equal_755: 'Union30[float31, None]'
    _less_than_or_equal_756: 'Union30[float31, None]'
    _equal_to_757: 'Union30[float31, None]'
    __slots__ = ('_greater_than_753', '_less_than_754', '_greater_than_or_equal_755', '_less_than_or_equal_756', '_equal_to_757')
    def __init__(this_430, /, greater_than: 'Union30[float31, None]', less_than: 'Union30[float31, None]', greater_than_or_equal: 'Union30[float31, None]', less_than_or_equal: 'Union30[float31, None]', equal_to: 'Union30[float31, None]') -> None:
        this_430._greater_than_753 = greater_than
        this_430._less_than_754 = less_than
        this_430._greater_than_or_equal_755 = greater_than_or_equal
        this_430._less_than_or_equal_756 = less_than_or_equal
        this_430._equal_to_757 = equal_to
    @property
    def greater_than(this_2307, /) -> 'Union30[float31, None]':
        return this_2307._greater_than_753
    @property
    def less_than(this_2310, /) -> 'Union30[float31, None]':
        return this_2310._less_than_754
    @property
    def greater_than_or_equal(this_2313, /) -> 'Union30[float31, None]':
        return this_2313._greater_than_or_equal_755
    @property
    def less_than_or_equal(this_2316, /) -> 'Union30[float31, None]':
        return this_2316._less_than_or_equal_756
    @property
    def equal_to(this_2319, /) -> 'Union30[float31, None]':
        return this_2319._equal_to_757
class Changeset(metaclass = ABCMeta32):
    def cast(this_243, allowed_fields_773: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_required(this_244, fields_776: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_length(this_245, field_779: 'SafeIdentifier', min_780: 'int35', max_781: 'int35', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_int(this_246, field_784: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_int64(this_247, field_787: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_float(this_248, field_790: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_bool(this_249, field_793: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def put_change(this_250, field_796: 'SafeIdentifier', value_797: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def get_change(this_251, field_800: 'SafeIdentifier', /) -> 'str29':
        raise RuntimeError34()
    def delete_change(this_252, field_803: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_inclusion(this_253, field_806: 'SafeIdentifier', allowed_807: 'Sequence33[str29]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_exclusion(this_254, field_810: 'SafeIdentifier', disallowed_811: 'Sequence33[str29]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_number(this_255, field_814: 'SafeIdentifier', opts_815: 'NumberValidationOpts', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_acceptance(this_256, field_818: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_confirmation(this_257, field_821: 'SafeIdentifier', confirmation_field_822: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_contains(this_258, field_825: 'SafeIdentifier', substring_826: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_starts_with(this_259, field_829: 'SafeIdentifier', prefix_830: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_ends_with(this_260, field_833: 'SafeIdentifier', suffix_834: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def to_insert_sql(this_261, /) -> 'SqlFragment':
        raise RuntimeError34()
    def to_update_sql(this_262, id_839: 'int35', /) -> 'SqlFragment':
        raise RuntimeError34()
class _ChangesetImpl(Changeset):
    _table_def_841: 'TableDef'
    _params_842: 'MappingProxyType36[str29, str29]'
    _changes_843: 'MappingProxyType36[str29, str29]'
    _errors_844: 'Sequence33[ChangesetError]'
    _is_valid_845: 'bool37'
    __slots__ = ('_table_def_841', '_params_842', '_changes_843', '_errors_844', '_is_valid_845')
    @property
    def table_def(this_264, /) -> 'TableDef':
        return this_264._table_def_841
    @property
    def changes(this_265, /) -> 'MappingProxyType36[str29, str29]':
        return this_265._changes_843
    @property
    def errors(this_266, /) -> 'Sequence33[ChangesetError]':
        return this_266._errors_844
    @property
    def is_valid(this_267, /) -> 'bool37':
        return this_267._is_valid_845
    def _add_error_854(this_268, field_855: 'str29', message_856: 'str29', /) -> 'Changeset':
        eb_858: 'MutableSequence38[ChangesetError]' = _list_4170(this_268._errors_844)
        eb_858.append(ChangesetError(field_855, message_856))
        return _ChangesetImpl(this_268._table_def_841, this_268._params_842, this_268._changes_843, _tuple_4172(eb_858), False)
    def cast(this_269, allowed_fields_860: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        mb_862: 'Dict39[str29, str29]' = {}
        this_3777: 'Sequence33[SafeIdentifier]' = allowed_fields_860
        n_3779: 'int35' = _len_4174(this_3777)
        i_3780: 'int35' = 0
        while i_3780 < n_3779:
            el_3781: 'SafeIdentifier' = _list_get_4175(this_3777, i_3780)
            i_3780 = _int_add_4176(i_3780, 1)
            f_863: 'SafeIdentifier' = el_3781
            val_864: 'str29' = this_269._params_842.get(f_863.sql_value, '')
            if not (not val_864):
                _map_builder_set_4179(mb_862, f_863.sql_value, val_864)
        return _ChangesetImpl(this_269._table_def_841, this_269._params_842, _mapped_to_map_4180(mb_862), this_269._errors_844, this_269._is_valid_845)
    def validate_required(this_270, fields_866: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        return_480: 'Changeset'
        with Label40() as fn_867:
            if not this_270._is_valid_845:
                return_480 = this_270
                fn_867.break_()
            eb_868: 'MutableSequence38[ChangesetError]' = _list_4170(this_270._errors_844)
            valid_869: 'bool37' = True
            this_3782: 'Sequence33[SafeIdentifier]' = fields_866
            n_3784: 'int35' = _len_4174(this_3782)
            i_3785: 'int35' = 0
            while i_3785 < n_3784:
                el_3786: 'SafeIdentifier' = _list_get_4175(this_3782, i_3785)
                i_3785 = _int_add_4176(i_3785, 1)
                f_870: 'SafeIdentifier' = el_3786
                if not _mapped_has_4181(this_270._changes_843, f_870.sql_value):
                    eb_868.append(ChangesetError(f_870.sql_value, 'is required'))
                    valid_869 = False
            return _ChangesetImpl(this_270._table_def_841, this_270._params_842, this_270._changes_843, _tuple_4172(eb_868), valid_869)
        return return_480
    def validate_length(this_271, field_872: 'SafeIdentifier', min_873: 'int35', max_874: 'int35', /) -> 'Changeset':
        return_481: 'Changeset'
        with Label40() as fn_875:
            if not this_271._is_valid_845:
                return_481 = this_271
                fn_875.break_()
            val_876: 'str29' = this_271._changes_843.get(field_872.sql_value, '')
            len_877: 'int35' = _string_count_between_4182(val_876, 0, _len_4174(val_876))
            t_3755: 'bool37'
            if len_877 < min_873:
                t_3755 = True
            else:
                t_3755 = len_877 > max_874
            if t_3755:
                return_481 = this_271._add_error_854(field_872.sql_value, _str_cat_4183('must be between ', _int_to_string_4184(min_873), ' and ', _int_to_string_4184(max_874), ' characters'))
                fn_875.break_()
            return this_271
        return return_481
    def validate_int(this_272, field_879: 'SafeIdentifier', /) -> 'Changeset':
        return_482: 'Changeset'
        with Label40() as fn_880:
            if not this_272._is_valid_845:
                return_482 = this_272
                fn_880.break_()
            val_881: 'str29' = this_272._changes_843.get(field_879.sql_value, '')
            if not val_881:
                return_482 = this_272
                fn_880.break_()
            parse_ok_882: 'bool37'
            try:
                _string_to_int32_4185(val_881)
                parse_ok_882 = True
            except Exception41:
                parse_ok_882 = False
            if not parse_ok_882:
                return_482 = this_272._add_error_854(field_879.sql_value, 'must be an integer')
                fn_880.break_()
            return this_272
        return return_482
    def validate_int64(this_273, field_884: 'SafeIdentifier', /) -> 'Changeset':
        return_483: 'Changeset'
        with Label40() as fn_885:
            if not this_273._is_valid_845:
                return_483 = this_273
                fn_885.break_()
            val_886: 'str29' = this_273._changes_843.get(field_884.sql_value, '')
            if not val_886:
                return_483 = this_273
                fn_885.break_()
            parse_ok_887: 'bool37'
            try:
                _string_to_int64_4186(val_886)
                parse_ok_887 = True
            except Exception41:
                parse_ok_887 = False
            if not parse_ok_887:
                return_483 = this_273._add_error_854(field_884.sql_value, 'must be a 64-bit integer')
                fn_885.break_()
            return this_273
        return return_483
    def validate_float(this_274, field_889: 'SafeIdentifier', /) -> 'Changeset':
        return_484: 'Changeset'
        with Label40() as fn_890:
            if not this_274._is_valid_845:
                return_484 = this_274
                fn_890.break_()
            val_891: 'str29' = this_274._changes_843.get(field_889.sql_value, '')
            if not val_891:
                return_484 = this_274
                fn_890.break_()
            parse_ok_892: 'bool37'
            try:
                _string_to_float64_4187(val_891)
                parse_ok_892 = True
            except Exception41:
                parse_ok_892 = False
            if not parse_ok_892:
                return_484 = this_274._add_error_854(field_889.sql_value, 'must be a number')
                fn_890.break_()
            return this_274
        return return_484
    def validate_bool(this_275, field_894: 'SafeIdentifier', /) -> 'Changeset':
        return_485: 'Changeset'
        with Label40() as fn_895:
            if not this_275._is_valid_845:
                return_485 = this_275
                fn_895.break_()
            val_896: 'str29' = this_275._changes_843.get(field_894.sql_value, '')
            if not val_896:
                return_485 = this_275
                fn_895.break_()
            is_true_897: 'bool37'
            if val_896 == 'true':
                is_true_897 = True
            elif val_896 == '1':
                is_true_897 = True
            elif val_896 == 'yes':
                is_true_897 = True
            else:
                is_true_897 = val_896 == 'on'
            is_false_898: 'bool37'
            if val_896 == 'false':
                is_false_898 = True
            elif val_896 == '0':
                is_false_898 = True
            elif val_896 == 'no':
                is_false_898 = True
            else:
                is_false_898 = val_896 == 'off'
            t_3750: 'bool37'
            if not is_true_897:
                t_3750 = not is_false_898
            else:
                t_3750 = False
            if t_3750:
                return_485 = this_275._add_error_854(field_894.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)')
                fn_895.break_()
            return this_275
        return return_485
    def put_change(this_276, field_900: 'SafeIdentifier', value_901: 'str29', /) -> 'Changeset':
        mb_903: 'Dict39[str29, str29]' = {}
        pairs_904: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4188(this_276._changes_843)
        i_905: 'int35' = 0
        while i_905 < _len_4174(pairs_904):
            _map_builder_set_4179(mb_903, _list_get_4175(pairs_904, i_905).key, _list_get_4175(pairs_904, i_905).value)
            i_905 = _int_add_4176(i_905, 1)
        _map_builder_set_4179(mb_903, field_900.sql_value, value_901)
        return _ChangesetImpl(this_276._table_def_841, this_276._params_842, _mapped_to_map_4180(mb_903), this_276._errors_844, this_276._is_valid_845)
    def get_change(this_277, field_907: 'SafeIdentifier', /) -> 'str29':
        if not _mapped_has_4181(this_277._changes_843, field_907.sql_value):
            raise RuntimeError34()
        return this_277._changes_843.get(field_907.sql_value, '')
    def delete_change(this_278, field_910: 'SafeIdentifier', /) -> 'Changeset':
        mb_912: 'Dict39[str29, str29]' = {}
        pairs_913: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4188(this_278._changes_843)
        i_914: 'int35' = 0
        while i_914 < _len_4174(pairs_913):
            if not _list_get_4175(pairs_913, i_914).key == field_910.sql_value:
                _map_builder_set_4179(mb_912, _list_get_4175(pairs_913, i_914).key, _list_get_4175(pairs_913, i_914).value)
            i_914 = _int_add_4176(i_914, 1)
        return _ChangesetImpl(this_278._table_def_841, this_278._params_842, _mapped_to_map_4180(mb_912), this_278._errors_844, this_278._is_valid_845)
    def validate_inclusion(this_279, field_916: 'SafeIdentifier', allowed_917: 'Sequence33[str29]', /) -> 'Changeset':
        return_489: 'Changeset'
        with Label40() as fn_918:
            if not this_279._is_valid_845:
                return_489 = this_279
                fn_918.break_()
            if not _mapped_has_4181(this_279._changes_843, field_916.sql_value):
                return_489 = this_279
                fn_918.break_()
            val_919: 'str29' = this_279._changes_843.get(field_916.sql_value, '')
            found_920: 'bool37' = False
            this_3787: 'Sequence33[str29]' = allowed_917
            n_3789: 'int35' = _len_4174(this_3787)
            i_3790: 'int35' = 0
            while i_3790 < n_3789:
                el_3791: 'str29' = _list_get_4175(this_3787, i_3790)
                i_3790 = _int_add_4176(i_3790, 1)
                a_921: 'str29' = el_3791
                if a_921 == val_919:
                    found_920 = True
            if not found_920:
                return_489 = this_279._add_error_854(field_916.sql_value, 'is not included in the list')
                fn_918.break_()
            return this_279
        return return_489
    def validate_exclusion(this_280, field_923: 'SafeIdentifier', disallowed_924: 'Sequence33[str29]', /) -> 'Changeset':
        return_490: 'Changeset'
        with Label40() as fn_925:
            if not this_280._is_valid_845:
                return_490 = this_280
                fn_925.break_()
            if not _mapped_has_4181(this_280._changes_843, field_923.sql_value):
                return_490 = this_280
                fn_925.break_()
            val_926: 'str29' = this_280._changes_843.get(field_923.sql_value, '')
            found_927: 'bool37' = False
            this_3792: 'Sequence33[str29]' = disallowed_924
            n_3794: 'int35' = _len_4174(this_3792)
            i_3795: 'int35' = 0
            while i_3795 < n_3794:
                el_3796: 'str29' = _list_get_4175(this_3792, i_3795)
                i_3795 = _int_add_4176(i_3795, 1)
                d_928: 'str29' = el_3796
                if d_928 == val_926:
                    found_927 = True
            if found_927:
                return_490 = this_280._add_error_854(field_923.sql_value, 'is reserved')
                fn_925.break_()
            return this_280
        return return_490
    def validate_number(this_281, field_930: 'SafeIdentifier', opts_931: 'NumberValidationOpts', /) -> 'Changeset':
        return_491: 'Changeset'
        with Label40() as fn_932:
            if not this_281._is_valid_845:
                return_491 = this_281
                fn_932.break_()
            if not _mapped_has_4181(this_281._changes_843, field_930.sql_value):
                return_491 = this_281
                fn_932.break_()
            val_933: 'str29' = this_281._changes_843.get(field_930.sql_value, '')
            parse_ok_934: 'bool37'
            try:
                _string_to_float64_4187(val_933)
                parse_ok_934 = True
            except Exception41:
                parse_ok_934 = False
            if not parse_ok_934:
                return_491 = this_281._add_error_854(field_930.sql_value, 'must be a number')
                fn_932.break_()
            num_935: 'float31'
            try:
                num_935 = _string_to_float64_4187(val_933)
            except Exception41:
                num_935 = 0.0
            gt_936: 'Union30[float31, None]' = opts_931.greater_than
            if not gt_936 is None:
                gt_2947: 'float31' = gt_936
                if not _float_cmp_4189(num_935, gt_2947) > 0:
                    return_491 = this_281._add_error_854(field_930.sql_value, _str_cat_4183('must be greater than ', _float64_to_string_4190(gt_2947)))
                    fn_932.break_()
            lt_937: 'Union30[float31, None]' = opts_931.less_than
            if not lt_937 is None:
                lt_2948: 'float31' = lt_937
                if not _float_cmp_4189(num_935, lt_2948) < 0:
                    return_491 = this_281._add_error_854(field_930.sql_value, _str_cat_4183('must be less than ', _float64_to_string_4190(lt_2948)))
                    fn_932.break_()
            gte_938: 'Union30[float31, None]' = opts_931.greater_than_or_equal
            if not gte_938 is None:
                gte_2949: 'float31' = gte_938
                if not _float_cmp_4189(num_935, gte_2949) >= 0:
                    return_491 = this_281._add_error_854(field_930.sql_value, _str_cat_4183('must be greater than or equal to ', _float64_to_string_4190(gte_2949)))
                    fn_932.break_()
            lte_939: 'Union30[float31, None]' = opts_931.less_than_or_equal
            if not lte_939 is None:
                lte_2950: 'float31' = lte_939
                if not _float_cmp_4189(num_935, lte_2950) <= 0:
                    return_491 = this_281._add_error_854(field_930.sql_value, _str_cat_4183('must be less than or equal to ', _float64_to_string_4190(lte_2950)))
                    fn_932.break_()
            eq_940: 'Union30[float31, None]' = opts_931.equal_to
            if not eq_940 is None:
                eq_2951: 'float31' = eq_940
                if not _float_eq_4191(num_935, eq_2951):
                    return_491 = this_281._add_error_854(field_930.sql_value, _str_cat_4183('must be equal to ', _float64_to_string_4190(eq_2951)))
                    fn_932.break_()
            return this_281
        return return_491
    def validate_acceptance(this_282, field_942: 'SafeIdentifier', /) -> 'Changeset':
        return_492: 'Changeset'
        with Label40() as fn_943:
            if not this_282._is_valid_845:
                return_492 = this_282
                fn_943.break_()
            if not _mapped_has_4181(this_282._changes_843, field_942.sql_value):
                return_492 = this_282
                fn_943.break_()
            val_944: 'str29' = this_282._changes_843.get(field_942.sql_value, '')
            accepted_945: 'bool37'
            if val_944 == 'true':
                accepted_945 = True
            elif val_944 == '1':
                accepted_945 = True
            elif val_944 == 'yes':
                accepted_945 = True
            else:
                accepted_945 = val_944 == 'on'
            if not accepted_945:
                return_492 = this_282._add_error_854(field_942.sql_value, 'must be accepted')
                fn_943.break_()
            return this_282
        return return_492
    def validate_confirmation(this_283, field_947: 'SafeIdentifier', confirmation_field_948: 'SafeIdentifier', /) -> 'Changeset':
        return_493: 'Changeset'
        with Label40() as fn_949:
            if not this_283._is_valid_845:
                return_493 = this_283
                fn_949.break_()
            if not _mapped_has_4181(this_283._changes_843, field_947.sql_value):
                return_493 = this_283
                fn_949.break_()
            val_950: 'str29' = this_283._changes_843.get(field_947.sql_value, '')
            conf_951: 'str29' = this_283._changes_843.get(confirmation_field_948.sql_value, '')
            if not val_950 == conf_951:
                return_493 = this_283._add_error_854(confirmation_field_948.sql_value, 'does not match')
                fn_949.break_()
            return this_283
        return return_493
    def validate_contains(this_284, field_953: 'SafeIdentifier', substring_954: 'str29', /) -> 'Changeset':
        return_494: 'Changeset'
        with Label40() as fn_955:
            if not this_284._is_valid_845:
                return_494 = this_284
                fn_955.break_()
            if not _mapped_has_4181(this_284._changes_843, field_953.sql_value):
                return_494 = this_284
                fn_955.break_()
            val_956: 'str29' = this_284._changes_843.get(field_953.sql_value, '')
            if not val_956.find(substring_954) >= 0:
                return_494 = this_284._add_error_854(field_953.sql_value, 'must contain the given substring')
                fn_955.break_()
            return this_284
        return return_494
    def validate_starts_with(this_285, field_958: 'SafeIdentifier', prefix_959: 'str29', /) -> 'Changeset':
        return_495: 'Changeset'
        with Label40() as fn_960:
            if not this_285._is_valid_845:
                return_495 = this_285
                fn_960.break_()
            if not _mapped_has_4181(this_285._changes_843, field_958.sql_value):
                return_495 = this_285
                fn_960.break_()
            val_961: 'str29' = this_285._changes_843.get(field_958.sql_value, '')
            idx_962: 'int35' = val_961.find(prefix_959)
            starts_963: 'bool37'
            if idx_962 >= 0:
                starts_963 = _string_count_between_4182(val_961, 0, _require_string_index_4194(idx_962)) == 0
            else:
                starts_963 = False
            if not starts_963:
                return_495 = this_285._add_error_854(field_958.sql_value, 'must start with the given prefix')
                fn_960.break_()
            return this_285
        return return_495
    def validate_ends_with(this_286, field_965: 'SafeIdentifier', suffix_966: 'str29', /) -> 'Changeset':
        return_496: 'Changeset'
        with Label40() as fn_967:
            if not this_286._is_valid_845:
                return_496 = this_286
                fn_967.break_()
            if not _mapped_has_4181(this_286._changes_843, field_965.sql_value):
                return_496 = this_286
                fn_967.break_()
            val_968: 'str29' = this_286._changes_843.get(field_965.sql_value, '')
            val_len_969: 'int35' = _string_count_between_4182(val_968, 0, _len_4174(val_968))
            suffix_len_970: 'int35' = _string_count_between_4182(suffix_966, 0, _len_4174(suffix_966))
            if val_len_969 < suffix_len_970:
                return_496 = this_286._add_error_854(field_965.sql_value, 'must end with the given suffix')
                fn_967.break_()
            skip_count_971: 'int35' = _int_sub_4195(val_len_969, suffix_len_970)
            str_idx_972: 'int35' = 0
            i_973: 'int35' = 0
            while i_973 < skip_count_971:
                str_idx_972 = _string_next_4196(val_968, str_idx_972)
                i_973 = _int_add_4176(i_973, 1)
            suf_idx_974: 'int35' = 0
            matches_975: 'bool37' = True
            while True:
                t_3725: 'bool37'
                if matches_975:
                    t_3725 = len2(suffix_966) > suf_idx_974
                else:
                    t_3725 = False
                if not t_3725:
                    break
                if not len2(val_968) > str_idx_972:
                    matches_975 = False
                elif not _string_get_4198(val_968, str_idx_972) == _string_get_4198(suffix_966, suf_idx_974):
                    matches_975 = False
                else:
                    str_idx_972 = _string_next_4196(val_968, str_idx_972)
                    suf_idx_974 = _string_next_4196(suffix_966, suf_idx_974)
            if not matches_975:
                return_496 = this_286._add_error_854(field_965.sql_value, 'must end with the given suffix')
                fn_967.break_()
            return this_286
        return return_496
    def _parse_bool_sql_part_976(this_287, val_977: 'str29', /) -> 'SqlBoolean':
        return_497: 'SqlBoolean'
        with Label40() as fn_978:
            t_3717: 'bool37'
            if val_977 == 'true':
                t_3717 = True
            elif val_977 == '1':
                t_3717 = True
            elif val_977 == 'yes':
                t_3717 = True
            else:
                t_3717 = val_977 == 'on'
            if t_3717:
                return_497 = SqlBoolean(True)
                fn_978.break_()
            t_3721: 'bool37'
            if val_977 == 'false':
                t_3721 = True
            elif val_977 == '0':
                t_3721 = True
            elif val_977 == 'no':
                t_3721 = True
            else:
                t_3721 = val_977 == 'off'
            if t_3721:
                return_497 = SqlBoolean(False)
                fn_978.break_()
            raise RuntimeError34()
        return return_497
    def _value_to_sql_part_979(this_288, field_def_980: 'FieldDef', val_981: 'str29', /) -> 'SqlPart':
        return_498: 'SqlPart'
        with Label40() as fn_982:
            ft_983: 'FieldType' = field_def_980.field_type
            if isinstance42(ft_983, StringField):
                return_498 = SqlString(val_981)
                fn_982.break_()
            if isinstance42(ft_983, IntField):
                t_3848: 'int35' = _string_to_int32_4185(val_981)
                return_498 = SqlInt32(t_3848)
                fn_982.break_()
            if isinstance42(ft_983, Int64Field):
                t_3849: '_int64' = _string_to_int64_4186(val_981)
                return_498 = SqlInt64(t_3849)
                fn_982.break_()
            if isinstance42(ft_983, FloatField):
                t_3850: 'float31' = _string_to_float64_4187(val_981)
                return_498 = SqlFloat64(t_3850)
                fn_982.break_()
            if isinstance42(ft_983, BoolField):
                return_498 = this_288._parse_bool_sql_part_976(val_981)
                fn_982.break_()
            if isinstance42(ft_983, DateField):
                t_3851: 'date28' = _date_from_iso_string_4199(val_981)
                return_498 = SqlDate(t_3851)
                fn_982.break_()
            raise RuntimeError34()
        return return_498
    def to_insert_sql(this_289, /) -> 'SqlFragment':
        if not this_289._is_valid_845:
            raise RuntimeError34()
        i_986: 'int35' = 0
        while i_986 < _len_4174(this_289._table_def_841.fields):
            with Label40() as continue_4166:
                f_987: 'FieldDef' = _list_get_4175(this_289._table_def_841.fields, i_986)
                if f_987.virtual:
                    continue_4166.break_()
                dv_988: 'Union30[SqlPart, None]' = f_987.default_value
                t_3702: 'bool37'
                if not f_987.nullable:
                    if not _mapped_has_4181(this_289._changes_843, f_987.name.sql_value):
                        t_3702 = dv_988 is None
                    else:
                        t_3702 = False
                else:
                    t_3702 = False
                if t_3702:
                    raise RuntimeError34()
            i_986 = _int_add_4176(i_986, 1)
        col_names_989: 'MutableSequence38[str29]' = _list_4170()
        val_parts_990: 'MutableSequence38[SqlPart]' = _list_4170()
        pairs_991: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4188(this_289._changes_843)
        i_992: 'int35' = 0
        while i_992 < _len_4174(pairs_991):
            with Label40() as continue_4167:
                pair_993: 'Pair27[str29, str29]' = _list_get_4175(pairs_991, i_992)
                fd_994: 'FieldDef' = this_289._table_def_841.field(pair_993.key)
                if fd_994.virtual:
                    continue_4167.break_()
                col_names_989.append(fd_994.name.sql_value)
                t_3847: 'SqlPart' = this_289._value_to_sql_part_979(fd_994, pair_993.value)
                val_parts_990.append(t_3847)
            i_992 = _int_add_4176(i_992, 1)
        i_995: 'int35' = 0
        while i_995 < _len_4174(this_289._table_def_841.fields):
            with Label40() as continue_4168:
                f_996: 'FieldDef' = _list_get_4175(this_289._table_def_841.fields, i_995)
                if f_996.virtual:
                    continue_4168.break_()
                dv_997: 'Union30[SqlPart, None]' = f_996.default_value
                if not dv_997 is None:
                    dv_2959: 'SqlPart' = dv_997
                    if not _mapped_has_4181(this_289._changes_843, f_996.name.sql_value):
                        col_names_989.append(f_996.name.sql_value)
                        val_parts_990.append(dv_2959)
            i_995 = _int_add_4176(i_995, 1)
        if _len_4174(val_parts_990) == 0:
            raise RuntimeError34()
        b_998: 'SqlBuilder' = SqlBuilder()
        b_998.append_safe('INSERT INTO ')
        b_998.append_safe(this_289._table_def_841.table_name.sql_value)
        b_998.append_safe(' (')
        def fn_4158(c_999: 'str29', /) -> 'str29':
            return c_999
        b_998.append_safe(_list_join_4200(_tuple_4172(col_names_989), ', ', fn_4158))
        b_998.append_safe(') VALUES (')
        b_998.append_part(_list_get_4175(val_parts_990, 0))
        j_1000: 'int35' = 1
        while j_1000 < _len_4174(val_parts_990):
            b_998.append_safe(', ')
            b_998.append_part(_list_get_4175(val_parts_990, j_1000))
            j_1000 = _int_add_4176(j_1000, 1)
        b_998.append_safe(')')
        return b_998.accumulated
    def to_update_sql(this_290, id_1002: 'int35', /) -> 'SqlFragment':
        if not this_290._is_valid_845:
            raise RuntimeError34()
        pairs_1004: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4188(this_290._changes_843)
        if _len_4174(pairs_1004) == 0:
            raise RuntimeError34()
        b_1005: 'SqlBuilder' = SqlBuilder()
        b_1005.append_safe('UPDATE ')
        b_1005.append_safe(this_290._table_def_841.table_name.sql_value)
        b_1005.append_safe(' SET ')
        set_count_1006: 'int35' = 0
        i_1007: 'int35' = 0
        while i_1007 < _len_4174(pairs_1004):
            with Label40() as continue_4169:
                pair_1008: 'Pair27[str29, str29]' = _list_get_4175(pairs_1004, i_1007)
                fd_1009: 'FieldDef' = this_290._table_def_841.field(pair_1008.key)
                if fd_1009.virtual:
                    continue_4169.break_()
                if set_count_1006 > 0:
                    b_1005.append_safe(', ')
                b_1005.append_safe(fd_1009.name.sql_value)
                b_1005.append_safe(' = ')
                t_3846: 'SqlPart' = this_290._value_to_sql_part_979(fd_1009, pair_1008.value)
                b_1005.append_part(t_3846)
                set_count_1006 = _int_add_4176(set_count_1006, 1)
            i_1007 = _int_add_4176(i_1007, 1)
        if set_count_1006 == 0:
            raise RuntimeError34()
        b_1005.append_safe(' WHERE ')
        b_1005.append_safe(this_290._table_def_841.pk_name())
        b_1005.append_safe(' = ')
        b_1005.append_int32(id_1002)
        return b_1005.accumulated
    def __init__(this_469, /, table_def: 'TableDef', params: 'MappingProxyType36[str29, str29]', changes: 'MappingProxyType36[str29, str29]', errors: 'Sequence33[ChangesetError]', is_valid: 'bool37') -> None:
        this_469._table_def_841 = table_def
        this_469._params_842 = params
        this_469._changes_843 = changes
        this_469._errors_844 = errors
        this_469._is_valid_845 = is_valid
class JoinType(metaclass = ABCMeta32):
    def keyword(this_311, /) -> 'str29':
        raise RuntimeError34()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_312, /) -> 'str29':
        return 'INNER JOIN'
    def __init__(this_506, /) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_313, /) -> 'str29':
        return 'LEFT JOIN'
    def __init__(this_509, /) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_314, /) -> 'str29':
        return 'RIGHT JOIN'
    def __init__(this_512, /) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_315, /) -> 'str29':
        return 'FULL OUTER JOIN'
    def __init__(this_515, /) -> None:
        pass
class CrossJoin(JoinType):
    __slots__ = ()
    def keyword(this_316, /) -> 'str29':
        return 'CROSS JOIN'
    def __init__(this_518, /) -> None:
        pass
class JoinClause:
    _join_type_1356: 'JoinType'
    _table_1357: 'SafeIdentifier'
    _on_condition_1358: 'Union30[SqlFragment, None]'
    __slots__ = ('_join_type_1356', '_table_1357', '_on_condition_1358')
    def __init__(this_521, /, join_type: 'JoinType', table: 'SafeIdentifier', on_condition: 'Union30[SqlFragment, None]') -> None:
        this_521._join_type_1356 = join_type
        this_521._table_1357 = table
        this_521._on_condition_1358 = on_condition
    @property
    def join_type(this_2464, /) -> 'JoinType':
        return this_2464._join_type_1356
    @property
    def table(this_2467, /) -> 'SafeIdentifier':
        return this_2467._table_1357
    @property
    def on_condition(this_2470, /) -> 'Union30[SqlFragment, None]':
        return this_2470._on_condition_1358
class NullsPosition(metaclass = ABCMeta32):
    def keyword(this_317, /) -> 'str29':
        raise RuntimeError34()
class NullsFirst(NullsPosition):
    __slots__ = ()
    def keyword(this_318, /) -> 'str29':
        return ' NULLS FIRST'
    def __init__(this_525, /) -> None:
        pass
class NullsLast(NullsPosition):
    __slots__ = ()
    def keyword(this_319, /) -> 'str29':
        return ' NULLS LAST'
    def __init__(this_528, /) -> None:
        pass
class OrderClause:
    _field_1371: 'SafeIdentifier'
    _ascending_1372: 'bool37'
    _nulls_pos_1373: 'Union30[NullsPosition, None]'
    __slots__ = ('_field_1371', '_ascending_1372', '_nulls_pos_1373')
    def __init__(this_531, /, field_1375: 'SafeIdentifier', ascending: 'bool37', nulls_pos: 'Union30[NullsPosition, None]') -> None:
        this_531._field_1371 = field_1375
        this_531._ascending_1372 = ascending
        this_531._nulls_pos_1373 = nulls_pos
    @property
    def field(this_2473, /) -> 'SafeIdentifier':
        return this_2473._field_1371
    @property
    def ascending(this_2476, /) -> 'bool37':
        return this_2476._ascending_1372
    @property
    def nulls_pos(this_2479, /) -> 'Union30[NullsPosition, None]':
        return this_2479._nulls_pos_1373
class LockMode(metaclass = ABCMeta32):
    def keyword(this_320, /) -> 'str29':
        raise RuntimeError34()
class ForUpdate(LockMode):
    __slots__ = ()
    def keyword(this_321, /) -> 'str29':
        return ' FOR UPDATE'
    def __init__(this_535, /) -> None:
        pass
class ForShare(LockMode):
    __slots__ = ()
    def keyword(this_322, /) -> 'str29':
        return ' FOR SHARE'
    def __init__(this_538, /) -> None:
        pass
class WhereClause(metaclass = ABCMeta32):
    def keyword(this_324, /) -> 'str29':
        raise RuntimeError34()
class AndCondition(WhereClause):
    _condition_1390: 'SqlFragment'
    __slots__ = ('_condition_1390',)
    @property
    def condition(this_325, /) -> 'SqlFragment':
        return this_325._condition_1390
    def keyword(this_326, /) -> 'str29':
        return 'AND'
    def __init__(this_545, /, condition: 'SqlFragment') -> None:
        this_545._condition_1390 = condition
class OrCondition(WhereClause):
    _condition_1397: 'SqlFragment'
    __slots__ = ('_condition_1397',)
    @property
    def condition(this_327, /) -> 'SqlFragment':
        return this_327._condition_1397
    def keyword(this_328, /) -> 'str29':
        return 'OR'
    def __init__(this_550, /, condition_1403: 'SqlFragment') -> None:
        this_550._condition_1397 = condition_1403
class Query:
    _table_name_1421: 'SafeIdentifier'
    _conditions_1422: 'Sequence33[WhereClause]'
    _selected_fields_1423: 'Sequence33[SafeIdentifier]'
    _order_clauses_1424: 'Sequence33[OrderClause]'
    _limit_val_1425: 'Union30[int35, None]'
    _offset_val_1426: 'Union30[int35, None]'
    _join_clauses_1427: 'Sequence33[JoinClause]'
    _group_by_fields_1428: 'Sequence33[SafeIdentifier]'
    _having_conditions_1429: 'Sequence33[WhereClause]'
    _is_distinct_1430: 'bool37'
    _select_exprs_1431: 'Sequence33[SqlFragment]'
    _lock_mode_1432: 'Union30[LockMode, None]'
    __slots__ = ('_table_name_1421', '_conditions_1422', '_selected_fields_1423', '_order_clauses_1424', '_limit_val_1425', '_offset_val_1426', '_join_clauses_1427', '_group_by_fields_1428', '_having_conditions_1429', '_is_distinct_1430', '_select_exprs_1431', '_lock_mode_1432')
    def where(this_329, condition_1434: 'SqlFragment', /) -> 'Query':
        nb_1436: 'MutableSequence38[WhereClause]' = _list_4170(this_329._conditions_1422)
        nb_1436.append(AndCondition(condition_1434))
        return Query(this_329._table_name_1421, _tuple_4172(nb_1436), this_329._selected_fields_1423, this_329._order_clauses_1424, this_329._limit_val_1425, this_329._offset_val_1426, this_329._join_clauses_1427, this_329._group_by_fields_1428, this_329._having_conditions_1429, this_329._is_distinct_1430, this_329._select_exprs_1431, this_329._lock_mode_1432)
    def or_where(this_330, condition_1438: 'SqlFragment', /) -> 'Query':
        nb_1440: 'MutableSequence38[WhereClause]' = _list_4170(this_330._conditions_1422)
        nb_1440.append(OrCondition(condition_1438))
        return Query(this_330._table_name_1421, _tuple_4172(nb_1440), this_330._selected_fields_1423, this_330._order_clauses_1424, this_330._limit_val_1425, this_330._offset_val_1426, this_330._join_clauses_1427, this_330._group_by_fields_1428, this_330._having_conditions_1429, this_330._is_distinct_1430, this_330._select_exprs_1431, this_330._lock_mode_1432)
    def where_null(this_331, field_1442: 'SafeIdentifier', /) -> 'Query':
        b_1444: 'SqlBuilder' = SqlBuilder()
        b_1444.append_safe(field_1442.sql_value)
        b_1444.append_safe(' IS NULL')
        return this_331.where(b_1444.accumulated)
    def where_not_null(this_332, field_1446: 'SafeIdentifier', /) -> 'Query':
        b_1448: 'SqlBuilder' = SqlBuilder()
        b_1448.append_safe(field_1446.sql_value)
        b_1448.append_safe(' IS NOT NULL')
        return this_332.where(b_1448.accumulated)
    def where_in(this_333, field_1450: 'SafeIdentifier', values_1451: 'Sequence33[SqlPart]', /) -> 'Query':
        return_574: 'Query'
        with Label40() as fn_1452:
            if not values_1451:
                b_1453: 'SqlBuilder' = SqlBuilder()
                b_1453.append_safe('1 = 0')
                return_574 = this_333.where(b_1453.accumulated)
                fn_1452.break_()
            b_1454: 'SqlBuilder' = SqlBuilder()
            b_1454.append_safe(field_1450.sql_value)
            b_1454.append_safe(' IN (')
            b_1454.append_part(_list_get_4175(values_1451, 0))
            i_1455: 'int35' = 1
            while i_1455 < _len_4174(values_1451):
                b_1454.append_safe(', ')
                b_1454.append_part(_list_get_4175(values_1451, i_1455))
                i_1455 = _int_add_4176(i_1455, 1)
            b_1454.append_safe(')')
            return this_333.where(b_1454.accumulated)
        return return_574
    def where_in_subquery(this_334, field_1457: 'SafeIdentifier', sub_1458: 'Query', /) -> 'Query':
        b_1460: 'SqlBuilder' = SqlBuilder()
        b_1460.append_safe(field_1457.sql_value)
        b_1460.append_safe(' IN (')
        b_1460.append_fragment(sub_1458.to_sql())
        b_1460.append_safe(')')
        return this_334.where(b_1460.accumulated)
    def where_not(this_335, condition_1462: 'SqlFragment', /) -> 'Query':
        b_1464: 'SqlBuilder' = SqlBuilder()
        b_1464.append_safe('NOT (')
        b_1464.append_fragment(condition_1462)
        b_1464.append_safe(')')
        return this_335.where(b_1464.accumulated)
    def where_between(this_336, field_1466: 'SafeIdentifier', low_1467: 'SqlPart', high_1468: 'SqlPart', /) -> 'Query':
        b_1470: 'SqlBuilder' = SqlBuilder()
        b_1470.append_safe(field_1466.sql_value)
        b_1470.append_safe(' BETWEEN ')
        b_1470.append_part(low_1467)
        b_1470.append_safe(' AND ')
        b_1470.append_part(high_1468)
        return this_336.where(b_1470.accumulated)
    def where_like(this_337, field_1472: 'SafeIdentifier', pattern_1473: 'str29', /) -> 'Query':
        b_1475: 'SqlBuilder' = SqlBuilder()
        b_1475.append_safe(field_1472.sql_value)
        b_1475.append_safe(' LIKE ')
        b_1475.append_string(pattern_1473)
        return this_337.where(b_1475.accumulated)
    def where_i_like(this_338, field_1477: 'SafeIdentifier', pattern_1478: 'str29', /) -> 'Query':
        b_1480: 'SqlBuilder' = SqlBuilder()
        b_1480.append_safe(field_1477.sql_value)
        b_1480.append_safe(' ILIKE ')
        b_1480.append_string(pattern_1478)
        return this_338.where(b_1480.accumulated)
    def select(this_339, fields_1482: 'Sequence33[SafeIdentifier]', /) -> 'Query':
        return Query(this_339._table_name_1421, this_339._conditions_1422, fields_1482, this_339._order_clauses_1424, this_339._limit_val_1425, this_339._offset_val_1426, this_339._join_clauses_1427, this_339._group_by_fields_1428, this_339._having_conditions_1429, this_339._is_distinct_1430, this_339._select_exprs_1431, this_339._lock_mode_1432)
    def select_expr(this_340, exprs_1485: 'Sequence33[SqlFragment]', /) -> 'Query':
        return Query(this_340._table_name_1421, this_340._conditions_1422, this_340._selected_fields_1423, this_340._order_clauses_1424, this_340._limit_val_1425, this_340._offset_val_1426, this_340._join_clauses_1427, this_340._group_by_fields_1428, this_340._having_conditions_1429, this_340._is_distinct_1430, exprs_1485, this_340._lock_mode_1432)
    def order_by(this_341, field_1488: 'SafeIdentifier', ascending_1489: 'bool37', /) -> 'Query':
        nb_1491: 'MutableSequence38[OrderClause]' = _list_4170(this_341._order_clauses_1424)
        nb_1491.append(OrderClause(field_1488, ascending_1489, None))
        return Query(this_341._table_name_1421, this_341._conditions_1422, this_341._selected_fields_1423, _tuple_4172(nb_1491), this_341._limit_val_1425, this_341._offset_val_1426, this_341._join_clauses_1427, this_341._group_by_fields_1428, this_341._having_conditions_1429, this_341._is_distinct_1430, this_341._select_exprs_1431, this_341._lock_mode_1432)
    def order_by_nulls(this_342, field_1493: 'SafeIdentifier', ascending_1494: 'bool37', nulls_1495: 'NullsPosition', /) -> 'Query':
        nb_1497: 'MutableSequence38[OrderClause]' = _list_4170(this_342._order_clauses_1424)
        nb_1497.append(OrderClause(field_1493, ascending_1494, nulls_1495))
        return Query(this_342._table_name_1421, this_342._conditions_1422, this_342._selected_fields_1423, _tuple_4172(nb_1497), this_342._limit_val_1425, this_342._offset_val_1426, this_342._join_clauses_1427, this_342._group_by_fields_1428, this_342._having_conditions_1429, this_342._is_distinct_1430, this_342._select_exprs_1431, this_342._lock_mode_1432)
    def limit(this_343, n_1499: 'int35', /) -> 'Query':
        if n_1499 < 0:
            raise RuntimeError34()
        return Query(this_343._table_name_1421, this_343._conditions_1422, this_343._selected_fields_1423, this_343._order_clauses_1424, n_1499, this_343._offset_val_1426, this_343._join_clauses_1427, this_343._group_by_fields_1428, this_343._having_conditions_1429, this_343._is_distinct_1430, this_343._select_exprs_1431, this_343._lock_mode_1432)
    def offset(this_344, n_1502: 'int35', /) -> 'Query':
        if n_1502 < 0:
            raise RuntimeError34()
        return Query(this_344._table_name_1421, this_344._conditions_1422, this_344._selected_fields_1423, this_344._order_clauses_1424, this_344._limit_val_1425, n_1502, this_344._join_clauses_1427, this_344._group_by_fields_1428, this_344._having_conditions_1429, this_344._is_distinct_1430, this_344._select_exprs_1431, this_344._lock_mode_1432)
    def join(this_345, join_type_1505: 'JoinType', table_1506: 'SafeIdentifier', on_condition_1507: 'SqlFragment', /) -> 'Query':
        nb_1509: 'MutableSequence38[JoinClause]' = _list_4170(this_345._join_clauses_1427)
        nb_1509.append(JoinClause(join_type_1505, table_1506, on_condition_1507))
        return Query(this_345._table_name_1421, this_345._conditions_1422, this_345._selected_fields_1423, this_345._order_clauses_1424, this_345._limit_val_1425, this_345._offset_val_1426, _tuple_4172(nb_1509), this_345._group_by_fields_1428, this_345._having_conditions_1429, this_345._is_distinct_1430, this_345._select_exprs_1431, this_345._lock_mode_1432)
    def inner_join(this_346, table_1511: 'SafeIdentifier', on_condition_1512: 'SqlFragment', /) -> 'Query':
        return this_346.join(InnerJoin(), table_1511, on_condition_1512)
    def left_join(this_347, table_1515: 'SafeIdentifier', on_condition_1516: 'SqlFragment', /) -> 'Query':
        return this_347.join(LeftJoin(), table_1515, on_condition_1516)
    def right_join(this_348, table_1519: 'SafeIdentifier', on_condition_1520: 'SqlFragment', /) -> 'Query':
        return this_348.join(RightJoin(), table_1519, on_condition_1520)
    def full_join(this_349, table_1523: 'SafeIdentifier', on_condition_1524: 'SqlFragment', /) -> 'Query':
        return this_349.join(FullJoin(), table_1523, on_condition_1524)
    def cross_join(this_350, table_1527: 'SafeIdentifier', /) -> 'Query':
        nb_1529: 'MutableSequence38[JoinClause]' = _list_4170(this_350._join_clauses_1427)
        nb_1529.append(JoinClause(CrossJoin(), table_1527, None))
        return Query(this_350._table_name_1421, this_350._conditions_1422, this_350._selected_fields_1423, this_350._order_clauses_1424, this_350._limit_val_1425, this_350._offset_val_1426, _tuple_4172(nb_1529), this_350._group_by_fields_1428, this_350._having_conditions_1429, this_350._is_distinct_1430, this_350._select_exprs_1431, this_350._lock_mode_1432)
    def group_by(this_351, field_1531: 'SafeIdentifier', /) -> 'Query':
        nb_1533: 'MutableSequence38[SafeIdentifier]' = _list_4170(this_351._group_by_fields_1428)
        nb_1533.append(field_1531)
        return Query(this_351._table_name_1421, this_351._conditions_1422, this_351._selected_fields_1423, this_351._order_clauses_1424, this_351._limit_val_1425, this_351._offset_val_1426, this_351._join_clauses_1427, _tuple_4172(nb_1533), this_351._having_conditions_1429, this_351._is_distinct_1430, this_351._select_exprs_1431, this_351._lock_mode_1432)
    def having(this_352, condition_1535: 'SqlFragment', /) -> 'Query':
        nb_1537: 'MutableSequence38[WhereClause]' = _list_4170(this_352._having_conditions_1429)
        nb_1537.append(AndCondition(condition_1535))
        return Query(this_352._table_name_1421, this_352._conditions_1422, this_352._selected_fields_1423, this_352._order_clauses_1424, this_352._limit_val_1425, this_352._offset_val_1426, this_352._join_clauses_1427, this_352._group_by_fields_1428, _tuple_4172(nb_1537), this_352._is_distinct_1430, this_352._select_exprs_1431, this_352._lock_mode_1432)
    def or_having(this_353, condition_1539: 'SqlFragment', /) -> 'Query':
        nb_1541: 'MutableSequence38[WhereClause]' = _list_4170(this_353._having_conditions_1429)
        nb_1541.append(OrCondition(condition_1539))
        return Query(this_353._table_name_1421, this_353._conditions_1422, this_353._selected_fields_1423, this_353._order_clauses_1424, this_353._limit_val_1425, this_353._offset_val_1426, this_353._join_clauses_1427, this_353._group_by_fields_1428, _tuple_4172(nb_1541), this_353._is_distinct_1430, this_353._select_exprs_1431, this_353._lock_mode_1432)
    def distinct(this_354, /) -> 'Query':
        return Query(this_354._table_name_1421, this_354._conditions_1422, this_354._selected_fields_1423, this_354._order_clauses_1424, this_354._limit_val_1425, this_354._offset_val_1426, this_354._join_clauses_1427, this_354._group_by_fields_1428, this_354._having_conditions_1429, True, this_354._select_exprs_1431, this_354._lock_mode_1432)
    def lock(this_355, mode_1545: 'LockMode', /) -> 'Query':
        return Query(this_355._table_name_1421, this_355._conditions_1422, this_355._selected_fields_1423, this_355._order_clauses_1424, this_355._limit_val_1425, this_355._offset_val_1426, this_355._join_clauses_1427, this_355._group_by_fields_1428, this_355._having_conditions_1429, this_355._is_distinct_1430, this_355._select_exprs_1431, mode_1545)
    def to_sql(this_356, /) -> 'SqlFragment':
        b_1549: 'SqlBuilder' = SqlBuilder()
        if this_356._is_distinct_1430:
            b_1549.append_safe('SELECT DISTINCT ')
        else:
            b_1549.append_safe('SELECT ')
        if not (not this_356._select_exprs_1431):
            b_1549.append_fragment(_list_get_4175(this_356._select_exprs_1431, 0))
            i_1550: 'int35' = 1
            while i_1550 < _len_4174(this_356._select_exprs_1431):
                b_1549.append_safe(', ')
                b_1549.append_fragment(_list_get_4175(this_356._select_exprs_1431, i_1550))
                i_1550 = _int_add_4176(i_1550, 1)
        elif not this_356._selected_fields_1423:
            b_1549.append_safe('*')
        else:
            def fn_4030(f_1551: 'SafeIdentifier', /) -> 'str29':
                return f_1551.sql_value
            b_1549.append_safe(_list_join_4200(this_356._selected_fields_1423, ', ', fn_4030))
        b_1549.append_safe(' FROM ')
        b_1549.append_safe(this_356._table_name_1421.sql_value)
        _render_joins(b_1549, this_356._join_clauses_1427)
        _render_where(b_1549, this_356._conditions_1422)
        _render_group_by(b_1549, this_356._group_by_fields_1428)
        _render_having(b_1549, this_356._having_conditions_1429)
        if not (not this_356._order_clauses_1424):
            b_1549.append_safe(' ORDER BY ')
            first_1552: 'bool37' = True
            this_3827: 'Sequence33[OrderClause]' = this_356._order_clauses_1424
            n_3829: 'int35' = _len_4174(this_3827)
            i_3830: 'int35' = 0
            while i_3830 < n_3829:
                el_3831: 'OrderClause' = _list_get_4175(this_3827, i_3830)
                i_3830 = _int_add_4176(i_3830, 1)
                orc_1553: 'OrderClause' = el_3831
                t_3597: 'str29'
                if not first_1552:
                    b_1549.append_safe(', ')
                first_1552 = False
                b_1549.append_safe(orc_1553.field.sql_value)
                if orc_1553.ascending:
                    t_3597 = ' ASC'
                else:
                    t_3597 = ' DESC'
                b_1549.append_safe(t_3597)
                np_1554: 'Union30[NullsPosition, None]' = orc_1553.nulls_pos
                if not np_1554 is None:
                    b_1549.append_safe(np_1554.keyword())
        lv_1555: 'Union30[int35, None]' = this_356._limit_val_1425
        if not lv_1555 is None:
            lv_2962: 'int35' = lv_1555
            b_1549.append_safe(' LIMIT ')
            b_1549.append_int32(lv_2962)
        ov_1556: 'Union30[int35, None]' = this_356._offset_val_1426
        if not ov_1556 is None:
            ov_2963: 'int35' = ov_1556
            b_1549.append_safe(' OFFSET ')
            b_1549.append_int32(ov_2963)
        lm_1557: 'Union30[LockMode, None]' = this_356._lock_mode_1432
        if not lm_1557 is None:
            b_1549.append_safe(lm_1557.keyword())
        return b_1549.accumulated
    def count_sql(this_357, /) -> 'SqlFragment':
        b_1560: 'SqlBuilder' = SqlBuilder()
        b_1560.append_safe('SELECT COUNT(*) FROM ')
        b_1560.append_safe(this_357._table_name_1421.sql_value)
        _render_joins(b_1560, this_357._join_clauses_1427)
        _render_where(b_1560, this_357._conditions_1422)
        _render_group_by(b_1560, this_357._group_by_fields_1428)
        _render_having(b_1560, this_357._having_conditions_1429)
        return b_1560.accumulated
    def safe_to_sql(this_358, default_limit_1562: 'int35', /) -> 'SqlFragment':
        if default_limit_1562 < 0:
            raise RuntimeError34()
        if not this_358._limit_val_1425 is None:
            return this_358.to_sql()
        else:
            t_3843: 'Query' = this_358.limit(default_limit_1562)
            return t_3843.to_sql()
    def __init__(this_558, /, table_name: 'SafeIdentifier', conditions: 'Sequence33[WhereClause]', selected_fields: 'Sequence33[SafeIdentifier]', order_clauses: 'Sequence33[OrderClause]', limit_val: 'Union30[int35, None]', offset_val: 'Union30[int35, None]', join_clauses: 'Sequence33[JoinClause]', group_by_fields: 'Sequence33[SafeIdentifier]', having_conditions: 'Sequence33[WhereClause]', is_distinct: 'bool37', select_exprs: 'Sequence33[SqlFragment]', lock_mode: 'Union30[LockMode, None]') -> None:
        this_558._table_name_1421 = table_name
        this_558._conditions_1422 = conditions
        this_558._selected_fields_1423 = selected_fields
        this_558._order_clauses_1424 = order_clauses
        this_558._limit_val_1425 = limit_val
        this_558._offset_val_1426 = offset_val
        this_558._join_clauses_1427 = join_clauses
        this_558._group_by_fields_1428 = group_by_fields
        this_558._having_conditions_1429 = having_conditions
        this_558._is_distinct_1430 = is_distinct
        this_558._select_exprs_1431 = select_exprs
        this_558._lock_mode_1432 = lock_mode
    @property
    def table_name(this_2482, /) -> 'SafeIdentifier':
        return this_2482._table_name_1421
    @property
    def conditions(this_2485, /) -> 'Sequence33[WhereClause]':
        return this_2485._conditions_1422
    @property
    def selected_fields(this_2488, /) -> 'Sequence33[SafeIdentifier]':
        return this_2488._selected_fields_1423
    @property
    def order_clauses(this_2491, /) -> 'Sequence33[OrderClause]':
        return this_2491._order_clauses_1424
    @property
    def limit_val(this_2494, /) -> 'Union30[int35, None]':
        return this_2494._limit_val_1425
    @property
    def offset_val(this_2497, /) -> 'Union30[int35, None]':
        return this_2497._offset_val_1426
    @property
    def join_clauses(this_2500, /) -> 'Sequence33[JoinClause]':
        return this_2500._join_clauses_1427
    @property
    def group_by_fields(this_2503, /) -> 'Sequence33[SafeIdentifier]':
        return this_2503._group_by_fields_1428
    @property
    def having_conditions(this_2506, /) -> 'Sequence33[WhereClause]':
        return this_2506._having_conditions_1429
    @property
    def is_distinct(this_2509, /) -> 'bool37':
        return this_2509._is_distinct_1430
    @property
    def select_exprs(this_2512, /) -> 'Sequence33[SqlFragment]':
        return this_2512._select_exprs_1431
    @property
    def lock_mode(this_2515, /) -> 'Union30[LockMode, None]':
        return this_2515._lock_mode_1432
class SetClause:
    _field_1623: 'SafeIdentifier'
    _value_1624: 'SqlPart'
    __slots__ = ('_field_1623', '_value_1624')
    def __init__(this_614, /, field_1626: 'SafeIdentifier', value: 'SqlPart') -> None:
        this_614._field_1623 = field_1626
        this_614._value_1624 = value
    @property
    def field(this_2518, /) -> 'SafeIdentifier':
        return this_2518._field_1623
    @property
    def value(this_2521, /) -> 'SqlPart':
        return this_2521._value_1624
class UpdateQuery:
    _table_name_1628: 'SafeIdentifier'
    _set_clauses_1629: 'Sequence33[SetClause]'
    _conditions_1630: 'Sequence33[WhereClause]'
    _limit_val_1631: 'Union30[int35, None]'
    __slots__ = ('_table_name_1628', '_set_clauses_1629', '_conditions_1630', '_limit_val_1631')
    def set(this_359, field_1633: 'SafeIdentifier', value_1634: 'SqlPart', /) -> 'UpdateQuery':
        nb_1636: 'MutableSequence38[SetClause]' = _list_4170(this_359._set_clauses_1629)
        nb_1636.append(SetClause(field_1633, value_1634))
        return UpdateQuery(this_359._table_name_1628, _tuple_4172(nb_1636), this_359._conditions_1630, this_359._limit_val_1631)
    def where(this_360, condition_1638: 'SqlFragment', /) -> 'UpdateQuery':
        nb_1640: 'MutableSequence38[WhereClause]' = _list_4170(this_360._conditions_1630)
        nb_1640.append(AndCondition(condition_1638))
        return UpdateQuery(this_360._table_name_1628, this_360._set_clauses_1629, _tuple_4172(nb_1640), this_360._limit_val_1631)
    def or_where(this_361, condition_1642: 'SqlFragment', /) -> 'UpdateQuery':
        nb_1644: 'MutableSequence38[WhereClause]' = _list_4170(this_361._conditions_1630)
        nb_1644.append(OrCondition(condition_1642))
        return UpdateQuery(this_361._table_name_1628, this_361._set_clauses_1629, _tuple_4172(nb_1644), this_361._limit_val_1631)
    def limit(this_362, n_1646: 'int35', /) -> 'UpdateQuery':
        if n_1646 < 0:
            raise RuntimeError34()
        return UpdateQuery(this_362._table_name_1628, this_362._set_clauses_1629, this_362._conditions_1630, n_1646)
    def to_sql(this_363, /) -> 'SqlFragment':
        if not this_363._conditions_1630:
            raise RuntimeError34()
        if not this_363._set_clauses_1629:
            raise RuntimeError34()
        b_1650: 'SqlBuilder' = SqlBuilder()
        b_1650.append_safe('UPDATE ')
        b_1650.append_safe(this_363._table_name_1628.sql_value)
        b_1650.append_safe(' SET ')
        b_1650.append_safe(_list_get_4175(this_363._set_clauses_1629, 0).field.sql_value)
        b_1650.append_safe(' = ')
        b_1650.append_part(_list_get_4175(this_363._set_clauses_1629, 0).value)
        i_1651: 'int35' = 1
        while i_1651 < _len_4174(this_363._set_clauses_1629):
            b_1650.append_safe(', ')
            b_1650.append_safe(_list_get_4175(this_363._set_clauses_1629, i_1651).field.sql_value)
            b_1650.append_safe(' = ')
            b_1650.append_part(_list_get_4175(this_363._set_clauses_1629, i_1651).value)
            i_1651 = _int_add_4176(i_1651, 1)
        _render_where(b_1650, this_363._conditions_1630)
        lv_1652: 'Union30[int35, None]' = this_363._limit_val_1631
        if not lv_1652 is None:
            lv_2965: 'int35' = lv_1652
            b_1650.append_safe(' LIMIT ')
            b_1650.append_int32(lv_2965)
        return b_1650.accumulated
    def __init__(this_616, /, table_name_1654: 'SafeIdentifier', set_clauses: 'Sequence33[SetClause]', conditions_1656: 'Sequence33[WhereClause]', limit_val_1657: 'Union30[int35, None]') -> None:
        this_616._table_name_1628 = table_name_1654
        this_616._set_clauses_1629 = set_clauses
        this_616._conditions_1630 = conditions_1656
        this_616._limit_val_1631 = limit_val_1657
    @property
    def table_name(this_2524, /) -> 'SafeIdentifier':
        return this_2524._table_name_1628
    @property
    def set_clauses(this_2527, /) -> 'Sequence33[SetClause]':
        return this_2527._set_clauses_1629
    @property
    def conditions(this_2530, /) -> 'Sequence33[WhereClause]':
        return this_2530._conditions_1630
    @property
    def limit_val(this_2533, /) -> 'Union30[int35, None]':
        return this_2533._limit_val_1631
class DeleteQuery:
    _table_name_1658: 'SafeIdentifier'
    _conditions_1659: 'Sequence33[WhereClause]'
    _limit_val_1660: 'Union30[int35, None]'
    __slots__ = ('_table_name_1658', '_conditions_1659', '_limit_val_1660')
    def where(this_364, condition_1662: 'SqlFragment', /) -> 'DeleteQuery':
        nb_1664: 'MutableSequence38[WhereClause]' = _list_4170(this_364._conditions_1659)
        nb_1664.append(AndCondition(condition_1662))
        return DeleteQuery(this_364._table_name_1658, _tuple_4172(nb_1664), this_364._limit_val_1660)
    def or_where(this_365, condition_1666: 'SqlFragment', /) -> 'DeleteQuery':
        nb_1668: 'MutableSequence38[WhereClause]' = _list_4170(this_365._conditions_1659)
        nb_1668.append(OrCondition(condition_1666))
        return DeleteQuery(this_365._table_name_1658, _tuple_4172(nb_1668), this_365._limit_val_1660)
    def limit(this_366, n_1670: 'int35', /) -> 'DeleteQuery':
        if n_1670 < 0:
            raise RuntimeError34()
        return DeleteQuery(this_366._table_name_1658, this_366._conditions_1659, n_1670)
    def to_sql(this_367, /) -> 'SqlFragment':
        if not this_367._conditions_1659:
            raise RuntimeError34()
        b_1674: 'SqlBuilder' = SqlBuilder()
        b_1674.append_safe('DELETE FROM ')
        b_1674.append_safe(this_367._table_name_1658.sql_value)
        _render_where(b_1674, this_367._conditions_1659)
        lv_1675: 'Union30[int35, None]' = this_367._limit_val_1660
        if not lv_1675 is None:
            lv_2966: 'int35' = lv_1675
            b_1674.append_safe(' LIMIT ')
            b_1674.append_int32(lv_2966)
        return b_1674.accumulated
    def __init__(this_626, /, table_name_1677: 'SafeIdentifier', conditions_1678: 'Sequence33[WhereClause]', limit_val_1679: 'Union30[int35, None]') -> None:
        this_626._table_name_1658 = table_name_1677
        this_626._conditions_1659 = conditions_1678
        this_626._limit_val_1660 = limit_val_1679
    @property
    def table_name(this_2536, /) -> 'SafeIdentifier':
        return this_2536._table_name_1658
    @property
    def conditions(this_2539, /) -> 'Sequence33[WhereClause]':
        return this_2539._conditions_1659
    @property
    def limit_val(this_2542, /) -> 'Union30[int35, None]':
        return this_2542._limit_val_1660
class SafeIdentifier(metaclass = ABCMeta32):
    pass
class _ValidatedIdentifier(SafeIdentifier):
    _value_1935: 'str29'
    __slots__ = ('_value_1935',)
    @property
    def sql_value(this_370, /) -> 'str29':
        return this_370._value_1935
    def __init__(this_640, /, value_1939: 'str29') -> None:
        this_640._value_1935 = value_1939
class FieldType(metaclass = ABCMeta32):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_646, /) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_648, /) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_650, /) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_652, /) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_654, /) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_656, /) -> None:
        pass
class FieldDef:
    _name_1953: 'SafeIdentifier'
    _field_type_1954: 'FieldType'
    _nullable_1955: 'bool37'
    _default_value_1956: 'Union30[SqlPart, None]'
    _virtual_1957: 'bool37'
    __slots__ = ('_name_1953', '_field_type_1954', '_nullable_1955', '_default_value_1956', '_virtual_1957')
    def __init__(this_658, /, name: 'SafeIdentifier', field_type: 'FieldType', nullable: 'bool37', default_value: 'Union30[SqlPart, None]', virtual: 'bool37') -> None:
        this_658._name_1953 = name
        this_658._field_type_1954 = field_type
        this_658._nullable_1955 = nullable
        this_658._default_value_1956 = default_value
        this_658._virtual_1957 = virtual
    @property
    def name(this_2322, /) -> 'SafeIdentifier':
        return this_2322._name_1953
    @property
    def field_type(this_2325, /) -> 'FieldType':
        return this_2325._field_type_1954
    @property
    def nullable(this_2328, /) -> 'bool37':
        return this_2328._nullable_1955
    @property
    def default_value(this_2331, /) -> 'Union30[SqlPart, None]':
        return this_2331._default_value_1956
    @property
    def virtual(this_2334, /) -> 'bool37':
        return this_2334._virtual_1957
class TableDef:
    _table_name_1964: 'SafeIdentifier'
    _fields_1965: 'Sequence33[FieldDef]'
    _primary_key_1966: 'Union30[SafeIdentifier, None]'
    __slots__ = ('_table_name_1964', '_fields_1965', '_primary_key_1966')
    def field(this_377, name_1968: 'str29', /) -> 'FieldDef':
        return_665: 'FieldDef'
        with Label40() as fn_1969:
            this_3764: 'Sequence33[FieldDef]' = this_377._fields_1965
            n_3766: 'int35' = _len_4174(this_3764)
            i_3767: 'int35' = 0
            while i_3767 < n_3766:
                el_3768: 'FieldDef' = _list_get_4175(this_3764, i_3767)
                i_3767 = _int_add_4176(i_3767, 1)
                f_1970: 'FieldDef' = el_3768
                if f_1970.name.sql_value == name_1968:
                    return_665 = f_1970
                    fn_1969.break_()
            raise RuntimeError34()
        return return_665
    def pk_name(this_378, /) -> 'str29':
        return_666: 'str29'
        with Label40() as fn_1972:
            pk_1973: 'Union30[SafeIdentifier, None]' = this_378._primary_key_1966
            if not pk_1973 is None:
                return_666 = pk_1973.sql_value
                fn_1972.break_()
            return 'id'
        return return_666
    def __init__(this_661, /, table_name_1975: 'SafeIdentifier', fields: 'Sequence33[FieldDef]', primary_key: 'Union30[SafeIdentifier, None]') -> None:
        this_661._table_name_1964 = table_name_1975
        this_661._fields_1965 = fields
        this_661._primary_key_1966 = primary_key
    @property
    def table_name(this_2337, /) -> 'SafeIdentifier':
        return this_2337._table_name_1964
    @property
    def fields(this_2340, /) -> 'Sequence33[FieldDef]':
        return this_2340._fields_1965
    @property
    def primary_key(this_2343, /) -> 'Union30[SafeIdentifier, None]':
        return this_2343._primary_key_1966
T_397 = TypeVar44('T_397', bound = Any43)
class SqlBuilder:
    _buffer_2018: 'MutableSequence38[SqlPart]'
    __slots__ = ('_buffer_2018',)
    def append_safe(this_379, sql_source_2020: 'str29', /) -> 'None':
        this_379._buffer_2018.append(SqlSource(sql_source_2020))
    def append_fragment(this_380, fragment_2023: 'SqlFragment', /) -> 'None':
        _list_builder_add_all_4201(this_380._buffer_2018, fragment_2023.parts)
    def append_part(this_381, part_2026: 'SqlPart', /) -> 'None':
        this_381._buffer_2018.append(part_2026)
    def append_part_list(this_382, values_2029: 'Sequence33[SqlPart]', /) -> 'None':
        def fn_4165(x_2031: 'SqlPart', /) -> 'None':
            this_382.append_part(x_2031)
        this_382._append_list_2074(values_2029, fn_4165)
    def append_boolean(this_383, value_2033: 'bool37', /) -> 'None':
        this_383._buffer_2018.append(SqlBoolean(value_2033))
    def append_boolean_list(this_384, values_2036: 'Sequence33[bool37]', /) -> 'None':
        def fn_4164(x_2038: 'bool37', /) -> 'None':
            this_384.append_boolean(x_2038)
        this_384._append_list_2074(values_2036, fn_4164)
    def append_date(this_385, value_2040: 'date28', /) -> 'None':
        this_385._buffer_2018.append(SqlDate(value_2040))
    def append_date_list(this_386, values_2043: 'Sequence33[date28]', /) -> 'None':
        def fn_4163(x_2045: 'date28', /) -> 'None':
            this_386.append_date(x_2045)
        this_386._append_list_2074(values_2043, fn_4163)
    def append_float64(this_387, value_2047: 'float31', /) -> 'None':
        this_387._buffer_2018.append(SqlFloat64(value_2047))
    def append_float64_list(this_388, values_2050: 'Sequence33[float31]', /) -> 'None':
        def fn_4162(x_2052: 'float31', /) -> 'None':
            this_388.append_float64(x_2052)
        this_388._append_list_2074(values_2050, fn_4162)
    def append_int32(this_389, value_2054: 'int35', /) -> 'None':
        this_389._buffer_2018.append(SqlInt32(value_2054))
    def append_int32_list(this_390, values_2057: 'Sequence33[int35]', /) -> 'None':
        def fn_4161(x_2059: 'int35', /) -> 'None':
            this_390.append_int32(x_2059)
        this_390._append_list_2074(values_2057, fn_4161)
    def append_int64(this_391, value_2061: '_int64', /) -> 'None':
        this_391._buffer_2018.append(SqlInt64(value_2061))
    def append_int64_list(this_392, values_2064: 'Sequence33[_int64]', /) -> 'None':
        def fn_4160(x_2066: '_int64', /) -> 'None':
            this_392.append_int64(x_2066)
        this_392._append_list_2074(values_2064, fn_4160)
    def append_string(this_393, value_2068: 'str29', /) -> 'None':
        this_393._buffer_2018.append(SqlString(value_2068))
    def append_string_list(this_394, values_2071: 'Sequence33[str29]', /) -> 'None':
        def fn_4159(x_2073: 'str29', /) -> 'None':
            this_394.append_string(x_2073)
        this_394._append_list_2074(values_2071, fn_4159)
    def _append_list_2074(this_395, values_2075: 'Sequence33[T_397]', append_value_2076: 'Callable45[[T_397], None]', /) -> 'None':
        i_2078: 'int35' = 0
        while i_2078 < _len_4174(values_2075):
            if i_2078 > 0:
                this_395.append_safe(', ')
            append_value_2076(_list_get_4175(values_2075, i_2078))
            i_2078 = _int_add_4176(i_2078, 1)
    @property
    def accumulated(this_396, /) -> 'SqlFragment':
        return SqlFragment(_tuple_4172(this_396._buffer_2018))
    def __init__(this_669, /) -> None:
        t_2249: 'MutableSequence38[SqlPart]' = _list_4170()
        this_669._buffer_2018 = t_2249
class SqlFragment:
    _parts_2085: 'Sequence33[SqlPart]'
    __slots__ = ('_parts_2085',)
    def to_source(this_401, /) -> 'SqlSource':
        return SqlSource(this_401.to_string())
    def to_string(this_402, /) -> 'str29':
        builder_2090: 'list0[str29]' = ['']
        i_2091: 'int35' = 0
        while i_2091 < _len_4174(this_402._parts_2085):
            _list_get_4175(this_402._parts_2085, i_2091).format_to(builder_2090)
            i_2091 = _int_add_4176(i_2091, 1)
        return ''.join(builder_2090)
    def to_parameterized(this_403, /) -> 'ParameterizedSql':
        text_2094: 'list0[str29]' = ['']
        params_2095: 'MutableSequence38[str29]' = _list_4170()
        i_2096: 'int35' = 0
        while i_2096 < _len_4174(this_403._parts_2085):
            _list_get_4175(this_403._parts_2085, i_2096).format_parameterized(text_2094, params_2095)
            i_2096 = _int_add_4176(i_2096, 1)
        return ParameterizedSql(''.join(text_2094), _tuple_4172(params_2095))
    def __init__(this_690, /, parts: 'Sequence33[SqlPart]') -> None:
        this_690._parts_2085 = parts
    @property
    def parts(this_2355, /) -> 'Sequence33[SqlPart]':
        return this_2355._parts_2085
class ParameterizedSql:
    _text_2099: 'str29'
    _params_2100: 'Sequence33[str29]'
    __slots__ = ('_text_2099', '_params_2100')
    def __init__(this_696, /, text: 'str29', params_2103: 'Sequence33[str29]') -> None:
        this_696._text_2099 = text
        this_696._params_2100 = params_2103
    @property
    def text(this_2349, /) -> 'str29':
        return this_2349._text_2099
    @property
    def params(this_2352, /) -> 'Sequence33[str29]':
        return this_2352._params_2100
class SqlPart(metaclass = ABCMeta32):
    def format_to(this_404, builder_2109: 'list0[str29]', /) -> 'None':
        raise RuntimeError34()
    def format_parameterized(this_405, text_2112: 'list0[str29]', params_2113: 'MutableSequence38[str29]', /) -> 'None':
        raise RuntimeError34()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    _source_2115: 'str29'
    __slots__ = ('_source_2115',)
    def format_to(this_406, builder_2117: 'list0[str29]', /) -> 'None':
        builder_2117.append(this_406._source_2115)
    def format_parameterized(this_407, text_2120: 'list0[str29]', params_2121: 'MutableSequence38[str29]', /) -> 'None':
        text_2120.append(this_407._source_2115)
    def __init__(this_702, /, source: 'str29') -> None:
        this_702._source_2115 = source
    @property
    def source(this_2346, /) -> 'str29':
        return this_2346._source_2115
class SqlBoolean(SqlPart):
    _value_2125: 'bool37'
    __slots__ = ('_value_2125',)
    def format_to(this_408, builder_2127: 'list0[str29]', /) -> 'None':
        t_3763: 'str29'
        if this_408._value_2125:
            t_3763 = 'TRUE'
        else:
            t_3763 = 'FALSE'
        builder_2127.append(t_3763)
    def format_parameterized(this_409, text_2130: 'list0[str29]', params_2131: 'MutableSequence38[str29]', /) -> 'None':
        this_409.format_to(text_2130)
    def __init__(this_706, /, value_2134: 'bool37') -> None:
        this_706._value_2125 = value_2134
    @property
    def value(this_2358, /) -> 'bool37':
        return this_2358._value_2125
class SqlDate(SqlPart):
    _value_2135: 'date28'
    __slots__ = ('_value_2135',)
    def format_to(this_410, builder_2137: 'list0[str29]', /) -> 'None':
        builder_2137.append("'")
        this_3773: 'str29' = _date_to_string_4205(this_410._value_2135)
        index_3775: 'int35' = 0
        while len2(this_3773) > index_3775:
            code_point_3776: 'int35' = _string_get_4198(this_3773, index_3775)
            c_2139: 'int35' = code_point_3776
            if c_2139 == 39:
                builder_2137.append("''")
            else:
                builder_2137.append(string_from_code_point46(c_2139))
            index_3775 = _string_next_4196(this_3773, index_3775)
        builder_2137.append("'")
    def format_parameterized(this_411, text_2141: 'list0[str29]', params_2142: 'MutableSequence38[str29]', /) -> 'None':
        _placeholder(text_2141, params_2142, _date_to_string_4205(this_411._value_2135))
    def __init__(this_710, /, value_2145: 'date28') -> None:
        this_710._value_2135 = value_2145
    @property
    def value(this_2373, /) -> 'date28':
        return this_2373._value_2135
class SqlFloat64(SqlPart):
    _value_2146: 'float31'
    __slots__ = ('_value_2146',)
    def format_to(this_412, builder_2148: 'list0[str29]', /) -> 'None':
        s_2150: 'str29' = _float64_to_string_4190(this_412._value_2146)
        t_3760: 'bool37'
        if s_2150 == 'NaN':
            t_3760 = True
        elif s_2150 == 'Infinity':
            t_3760 = True
        else:
            t_3760 = s_2150 == '-Infinity'
        if t_3760:
            builder_2148.append('NULL')
        else:
            builder_2148.append(s_2150)
    def format_parameterized(this_413, text_2152: 'list0[str29]', params_2153: 'MutableSequence38[str29]', /) -> 'None':
        s_2155: 'str29' = _float64_to_string_4190(this_413._value_2146)
        t_3757: 'bool37'
        if s_2155 == 'NaN':
            t_3757 = True
        elif s_2155 == 'Infinity':
            t_3757 = True
        else:
            t_3757 = s_2155 == '-Infinity'
        if t_3757:
            text_2152.append('NULL')
        else:
            _placeholder(text_2152, params_2153, s_2155)
    def __init__(this_714, /, value_2157: 'float31') -> None:
        this_714._value_2146 = value_2157
    @property
    def value(this_2370, /) -> 'float31':
        return this_2370._value_2146
class SqlInt32(SqlPart):
    _value_2158: 'int35'
    __slots__ = ('_value_2158',)
    def format_to(this_418, builder_2160: 'list0[str29]', /) -> 'None':
        builder_2160.append(_int_to_string_4184(this_418._value_2158))
    def format_parameterized(this_419, text_2163: 'list0[str29]', params_2164: 'MutableSequence38[str29]', /) -> 'None':
        _placeholder(text_2163, params_2164, _int_to_string_4184(this_419._value_2158))
    def __init__(this_718, /, value_2167: 'int35') -> None:
        this_718._value_2158 = value_2167
    @property
    def value(this_2364, /) -> 'int35':
        return this_2364._value_2158
class SqlInt64(SqlPart):
    _value_2168: '_int64'
    __slots__ = ('_value_2168',)
    def format_to(this_420, builder_2170: 'list0[str29]', /) -> 'None':
        builder_2170.append(_int_to_string_4184(this_420._value_2168))
    def format_parameterized(this_421, text_2173: 'list0[str29]', params_2174: 'MutableSequence38[str29]', /) -> 'None':
        _placeholder(text_2173, params_2174, _int_to_string_4184(this_421._value_2168))
    def __init__(this_722, /, value_2177: '_int64') -> None:
        this_722._value_2168 = value_2177
    @property
    def value(this_2367, /) -> '_int64':
        return this_2367._value_2168
class SqlDefault(SqlPart):
    '`SqlDefault` renders the literal SQL keyword `DEFAULT`, used for columns\nwith server-side default values (e.g., `NOW()` for timestamps).'
    __slots__ = ()
    def format_to(this_422, builder_2179: 'list0[str29]', /) -> 'None':
        builder_2179.append('DEFAULT')
    def format_parameterized(this_423, text_2182: 'list0[str29]', params_2183: 'MutableSequence38[str29]', /) -> 'None':
        this_423.format_to(text_2182)
    def __init__(this_726, /) -> None:
        pass
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    _value_2186: 'str29'
    __slots__ = ('_value_2186',)
    def format_to(this_424, builder_2188: 'list0[str29]', /) -> 'None':
        builder_2188.append("'")
        this_3769: 'str29' = this_424._value_2186
        index_3771: 'int35' = 0
        while len2(this_3769) > index_3771:
            code_point_3772: 'int35' = _string_get_4198(this_3769, index_3771)
            c_2190: 'int35' = code_point_3772
            if c_2190 == 39:
                builder_2188.append("''")
            else:
                builder_2188.append(string_from_code_point46(c_2190))
            index_3771 = _string_next_4196(this_3769, index_3771)
        builder_2188.append("'")
    def format_parameterized(this_425, text_2192: 'list0[str29]', params_2193: 'MutableSequence38[str29]', /) -> 'None':
        _placeholder(text_2192, params_2193, this_425._value_2186)
    def __init__(this_730, /, value_2196: 'str29') -> None:
        this_730._value_2186 = value_2196
    @property
    def value(this_2361, /) -> 'str29':
        return this_2361._value_2186
def _placeholder(text_2104: 'list0[str29]', params_2105: 'MutableSequence38[str29]', value_2106: 'str29', /) -> 'None':
    params_2105.append(value_2106)
    text_2104.append('$')
    text_2104.append(_int_to_string_4184(_len_4174(params_2105)))
def changeset(table_def_1016: 'TableDef', params_1017: 'MappingProxyType36[str29, str29]', /) -> 'Changeset':
    return _ChangesetImpl(table_def_1016, params_1017, _map_constructor_4207(()), (), True)
def _is_ident_start(c_1940: 'int35', /) -> 'bool37':
    t_3698: 'bool37'
    if c_1940 >= 97:
        t_3698 = c_1940 <= 122
    else:
        t_3698 = False
    if t_3698:
        return True
    else:
        t_3700: 'bool37'
        if c_1940 >= 65:
            t_3700 = c_1940 <= 90
        else:
            t_3700 = False
        if t_3700:
            return True
        else:
            return c_1940 == 95
def _is_ident_part(c_1942: 'int35', /) -> 'bool37':
    if _is_ident_start(c_1942):
        return True
    elif c_1942 >= 48:
        return c_1942 <= 57
    else:
        return False
def safe_identifier(name_1944: 'str29', /) -> 'SafeIdentifier':
    if not name_1944:
        raise RuntimeError34()
    idx_1946: 'int35' = 0
    if not _is_ident_start(_string_get_4198(name_1944, idx_1946)):
        raise RuntimeError34()
    idx_1946 = _string_next_4196(name_1944, idx_1946)
    while len2(name_1944) > idx_1946:
        if not _is_ident_part(_string_get_4198(name_1944, idx_1946)):
            raise RuntimeError34()
        idx_1946 = _string_next_4196(name_1944, idx_1946)
    return _ValidatedIdentifier(name_1944)
def timestamps() -> 'Sequence33[FieldDef]':
    t_3844: 'SafeIdentifier' = safe_identifier('inserted_at')
    t_3845: 'SafeIdentifier' = safe_identifier('updated_at')
    return (FieldDef(t_3844, DateField(), True, SqlDefault(), False), FieldDef(t_3845, DateField(), True, SqlDefault(), False))
def delete_sql(table_def_1335: 'TableDef', id_1336: 'int35', /) -> 'SqlFragment':
    b_1338: 'SqlBuilder' = SqlBuilder()
    b_1338.append_safe('DELETE FROM ')
    b_1338.append_safe(table_def_1335.table_name.sql_value)
    b_1338.append_safe(' WHERE ')
    b_1338.append_safe(table_def_1335.pk_name())
    b_1338.append_safe(' = ')
    b_1338.append_int32(id_1336)
    return b_1338.accumulated
def _render_where(b_1404: 'SqlBuilder', conditions_1405: 'Sequence33[WhereClause]', /) -> 'None':
    if not (not conditions_1405):
        b_1404.append_safe(' WHERE ')
        b_1404.append_fragment(_list_get_4175(conditions_1405, 0).condition)
        i_1407: 'int35' = 1
        while i_1407 < _len_4174(conditions_1405):
            b_1404.append_safe(' ')
            b_1404.append_safe(_list_get_4175(conditions_1405, i_1407).keyword())
            b_1404.append_safe(' ')
            b_1404.append_fragment(_list_get_4175(conditions_1405, i_1407).condition)
            i_1407 = _int_add_4176(i_1407, 1)
def _render_joins(b_1408: 'SqlBuilder', join_clauses_1409: 'Sequence33[JoinClause]', /) -> 'None':
    this_3822: 'Sequence33[JoinClause]' = join_clauses_1409
    n_3824: 'int35' = _len_4174(this_3822)
    i_3825: 'int35' = 0
    while i_3825 < n_3824:
        el_3826: 'JoinClause' = _list_get_4175(this_3822, i_3825)
        i_3825 = _int_add_4176(i_3825, 1)
        jc_1411: 'JoinClause' = el_3826
        b_1408.append_safe(' ')
        b_1408.append_safe(jc_1411.join_type.keyword())
        b_1408.append_safe(' ')
        b_1408.append_safe(jc_1411.table.sql_value)
        oc_1412: 'Union30[SqlFragment, None]' = jc_1411.on_condition
        if not oc_1412 is None:
            oc_2960: 'SqlFragment' = oc_1412
            b_1408.append_safe(' ON ')
            b_1408.append_fragment(oc_2960)
def _render_group_by(b_1413: 'SqlBuilder', group_by_fields_1414: 'Sequence33[SafeIdentifier]', /) -> 'None':
    if not (not group_by_fields_1414):
        b_1413.append_safe(' GROUP BY ')
        def fn_4031(f_1416: 'SafeIdentifier', /) -> 'str29':
            return f_1416.sql_value
        b_1413.append_safe(_list_join_4200(group_by_fields_1414, ', ', fn_4031))
def _render_having(b_1417: 'SqlBuilder', having_conditions_1418: 'Sequence33[WhereClause]', /) -> 'None':
    if not (not having_conditions_1418):
        b_1417.append_safe(' HAVING ')
        b_1417.append_fragment(_list_get_4175(having_conditions_1418, 0).condition)
        i_1420: 'int35' = 1
        while i_1420 < _len_4174(having_conditions_1418):
            b_1417.append_safe(' ')
            b_1417.append_safe(_list_get_4175(having_conditions_1418, i_1420).keyword())
            b_1417.append_safe(' ')
            b_1417.append_fragment(_list_get_4175(having_conditions_1418, i_1420).condition)
            i_1420 = _int_add_4176(i_1420, 1)
def from_(table_name_1577: 'SafeIdentifier', /) -> 'Query':
    return Query(table_name_1577, (), (), (), None, None, (), (), (), False, (), None)
def col(table_1579: 'SafeIdentifier', column_1580: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1582: 'SqlBuilder' = SqlBuilder()
    b_1582.append_safe(table_1579.sql_value)
    b_1582.append_safe('.')
    b_1582.append_safe(column_1580.sql_value)
    return b_1582.accumulated
def count_all() -> 'SqlFragment':
    b_1584: 'SqlBuilder' = SqlBuilder()
    b_1584.append_safe('COUNT(*)')
    return b_1584.accumulated
def count_col(field_1585: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1587: 'SqlBuilder' = SqlBuilder()
    b_1587.append_safe('COUNT(')
    b_1587.append_safe(field_1585.sql_value)
    b_1587.append_safe(')')
    return b_1587.accumulated
def sum_col(field_1588: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1590: 'SqlBuilder' = SqlBuilder()
    b_1590.append_safe('SUM(')
    b_1590.append_safe(field_1588.sql_value)
    b_1590.append_safe(')')
    return b_1590.accumulated
def avg_col(field_1591: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1593: 'SqlBuilder' = SqlBuilder()
    b_1593.append_safe('AVG(')
    b_1593.append_safe(field_1591.sql_value)
    b_1593.append_safe(')')
    return b_1593.accumulated
def min_col(field_1594: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1596: 'SqlBuilder' = SqlBuilder()
    b_1596.append_safe('MIN(')
    b_1596.append_safe(field_1594.sql_value)
    b_1596.append_safe(')')
    return b_1596.accumulated
def max_col(field_1597: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1599: 'SqlBuilder' = SqlBuilder()
    b_1599.append_safe('MAX(')
    b_1599.append_safe(field_1597.sql_value)
    b_1599.append_safe(')')
    return b_1599.accumulated
def union_sql(a_1600: 'Query', b_1601: 'Query', /) -> 'SqlFragment':
    sb_1603: 'SqlBuilder' = SqlBuilder()
    sb_1603.append_safe('(')
    sb_1603.append_fragment(a_1600.to_sql())
    sb_1603.append_safe(') UNION (')
    sb_1603.append_fragment(b_1601.to_sql())
    sb_1603.append_safe(')')
    return sb_1603.accumulated
def union_all_sql(a_1604: 'Query', b_1605: 'Query', /) -> 'SqlFragment':
    sb_1607: 'SqlBuilder' = SqlBuilder()
    sb_1607.append_safe('(')
    sb_1607.append_fragment(a_1604.to_sql())
    sb_1607.append_safe(') UNION ALL (')
    sb_1607.append_fragment(b_1605.to_sql())
    sb_1607.append_safe(')')
    return sb_1607.accumulated
def intersect_sql(a_1608: 'Query', b_1609: 'Query', /) -> 'SqlFragment':
    sb_1611: 'SqlBuilder' = SqlBuilder()
    sb_1611.append_safe('(')
    sb_1611.append_fragment(a_1608.to_sql())
    sb_1611.append_safe(') INTERSECT (')
    sb_1611.append_fragment(b_1609.to_sql())
    sb_1611.append_safe(')')
    return sb_1611.accumulated
def except_sql(a_1612: 'Query', b_1613: 'Query', /) -> 'SqlFragment':
    sb_1615: 'SqlBuilder' = SqlBuilder()
    sb_1615.append_safe('(')
    sb_1615.append_fragment(a_1612.to_sql())
    sb_1615.append_safe(') EXCEPT (')
    sb_1615.append_fragment(b_1613.to_sql())
    sb_1615.append_safe(')')
    return sb_1615.accumulated
def subquery(q_1616: 'Query', alias_1617: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1619: 'SqlBuilder' = SqlBuilder()
    b_1619.append_safe('(')
    b_1619.append_fragment(q_1616.to_sql())
    b_1619.append_safe(') AS ')
    b_1619.append_safe(alias_1617.sql_value)
    return b_1619.accumulated
def exists_sql(q_1620: 'Query', /) -> 'SqlFragment':
    b_1622: 'SqlBuilder' = SqlBuilder()
    b_1622.append_safe('EXISTS (')
    b_1622.append_fragment(q_1620.to_sql())
    b_1622.append_safe(')')
    return b_1622.accumulated
def update(table_name_1680: 'SafeIdentifier', /) -> 'UpdateQuery':
    return UpdateQuery(table_name_1680, (), (), None)
def delete_from(table_name_1682: 'SafeIdentifier', /) -> 'DeleteQuery':
    return DeleteQuery(table_name_1682, (), None)
