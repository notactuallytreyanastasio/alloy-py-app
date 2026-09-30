from builtins import str as str29, float as float31, RuntimeError as RuntimeError34, int as int35, bool as bool37, Exception as Exception41, len as len2, isinstance as isinstance42, list as list0, tuple as tuple1
from typing import Union as Union30, Sequence as Sequence33, MutableSequence as MutableSequence38, Dict as Dict39, Any as Any43, TypeVar as TypeVar44, Callable as Callable45
from abc import ABCMeta as ABCMeta32
from types import MappingProxyType as MappingProxyType36
from temper_core import Label as Label40, Pair as Pair27, string_from_code_point as string_from_code_point46, list_get as list_get3, int_add as int_add4, map_builder_set as map_builder_set5, mapped_to_map as mapped_to_map6, mapped_has as mapped_has7, string_count_between as string_count_between8, str_cat as str_cat9, int_to_string as int_to_string10, string_to_int32 as string_to_int3211, string_to_int64 as string_to_int6412, string_to_float64 as string_to_float6413, mapped_to_list as mapped_to_list14, float_cmp as float_cmp15, float64_to_string as float64_to_string16, float_eq as float_eq17, require_string_index as require_string_index18, int_sub as int_sub19, string_next as string_next20, string_get as string_get21, date_from_iso_string as date_from_iso_string22, list_join as list_join23, list_builder_add_all as list_builder_add_all24, date_to_string as date_to_string25, map_constructor as map_constructor26
from datetime import date as date28
_list_4018 = list0
_tuple_4020 = tuple1
_len_4022 = len2
_list_get_4023 = list_get3
_int_add_4024 = int_add4
_map_builder_set_4027 = map_builder_set5
_mapped_to_map_4028 = mapped_to_map6
_mapped_has_4029 = mapped_has7
_string_count_between_4030 = string_count_between8
_str_cat_4031 = str_cat9
_int_to_string_4032 = int_to_string10
_string_to_int32_4033 = string_to_int3211
_string_to_int64_4034 = string_to_int6412
_string_to_float64_4035 = string_to_float6413
_mapped_to_list_4036 = mapped_to_list14
_float_cmp_4037 = float_cmp15
_float64_to_string_4038 = float64_to_string16
_float_eq_4039 = float_eq17
_require_string_index_4042 = require_string_index18
_int_sub_4043 = int_sub19
_string_next_4044 = string_next20
_string_get_4046 = string_get21
_date_from_iso_string_4047 = date_from_iso_string22
_list_join_4048 = list_join23
_list_builder_add_all_4049 = list_builder_add_all24
_date_to_string_4053 = date_to_string25
_map_constructor_4055 = map_constructor26
_pair_4056 = Pair27
_date_4057 = date28
class ChangesetError:
    _field_714: 'str29'
    _message_715: 'str29'
    __slots__ = ('_field_714', '_message_715')
    def __init__(this, /, field: 'str29', message: 'str29') -> None:
        this._field_714 = field
        this._message_715 = message
    @property
    def field(this_2204, /) -> 'str29':
        return this_2204._field_714
    @property
    def message(this_2207, /) -> 'str29':
        return this_2207._message_715
class NumberValidationOpts:
    _greater_than_719: 'Union30[float31, None]'
    _less_than_720: 'Union30[float31, None]'
    _greater_than_or_equal_721: 'Union30[float31, None]'
    _less_than_or_equal_722: 'Union30[float31, None]'
    _equal_to_723: 'Union30[float31, None]'
    __slots__ = ('_greater_than_719', '_less_than_720', '_greater_than_or_equal_721', '_less_than_or_equal_722', '_equal_to_723')
    def __init__(this_411, /, greater_than: 'Union30[float31, None]', less_than: 'Union30[float31, None]', greater_than_or_equal: 'Union30[float31, None]', less_than_or_equal: 'Union30[float31, None]', equal_to: 'Union30[float31, None]') -> None:
        this_411._greater_than_719 = greater_than
        this_411._less_than_720 = less_than
        this_411._greater_than_or_equal_721 = greater_than_or_equal
        this_411._less_than_or_equal_722 = less_than_or_equal
        this_411._equal_to_723 = equal_to
    @property
    def greater_than(this_2210, /) -> 'Union30[float31, None]':
        return this_2210._greater_than_719
    @property
    def less_than(this_2213, /) -> 'Union30[float31, None]':
        return this_2213._less_than_720
    @property
    def greater_than_or_equal(this_2216, /) -> 'Union30[float31, None]':
        return this_2216._greater_than_or_equal_721
    @property
    def less_than_or_equal(this_2219, /) -> 'Union30[float31, None]':
        return this_2219._less_than_or_equal_722
    @property
    def equal_to(this_2222, /) -> 'Union30[float31, None]':
        return this_2222._equal_to_723
class Changeset(metaclass = ABCMeta32):
    def cast(this_238, allowed_fields_739: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_required(this_239, fields_742: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_length(this_240, field_745: 'SafeIdentifier', min_746: 'int35', max_747: 'int35', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_int(this_241, field_750: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_int64(this_242, field_753: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_float(this_243, field_756: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_bool(this_244, field_759: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def put_change(this_245, field_762: 'SafeIdentifier', value_763: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def get_change(this_246, field_766: 'SafeIdentifier', /) -> 'str29':
        raise RuntimeError34()
    def delete_change(this_247, field_769: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_inclusion(this_248, field_772: 'SafeIdentifier', allowed_773: 'Sequence33[str29]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_exclusion(this_249, field_776: 'SafeIdentifier', disallowed_777: 'Sequence33[str29]', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_number(this_250, field_780: 'SafeIdentifier', opts_781: 'NumberValidationOpts', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_acceptance(this_251, field_784: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_confirmation(this_252, field_787: 'SafeIdentifier', confirmation_field_788: 'SafeIdentifier', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_contains(this_253, field_791: 'SafeIdentifier', substring_792: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_starts_with(this_254, field_795: 'SafeIdentifier', prefix_796: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def validate_ends_with(this_255, field_799: 'SafeIdentifier', suffix_800: 'str29', /) -> 'Changeset':
        raise RuntimeError34()
    def to_insert_sql(this_256, /) -> 'SqlFragment':
        raise RuntimeError34()
    def to_update_sql(this_257, id_805: 'int35', /) -> 'SqlFragment':
        raise RuntimeError34()
class _ChangesetImpl(Changeset):
    _table_def_807: 'TableDef'
    _params_808: 'MappingProxyType36[str29, str29]'
    _changes_809: 'MappingProxyType36[str29, str29]'
    _errors_810: 'Sequence33[ChangesetError]'
    _is_valid_811: 'bool37'
    __slots__ = ('_table_def_807', '_params_808', '_changes_809', '_errors_810', '_is_valid_811')
    @property
    def table_def(this_259, /) -> 'TableDef':
        return this_259._table_def_807
    @property
    def changes(this_260, /) -> 'MappingProxyType36[str29, str29]':
        return this_260._changes_809
    @property
    def errors(this_261, /) -> 'Sequence33[ChangesetError]':
        return this_261._errors_810
    @property
    def is_valid(this_262, /) -> 'bool37':
        return this_262._is_valid_811
    def _add_error_820(this_263, field_821: 'str29', message_822: 'str29', /) -> 'Changeset':
        eb_824: 'MutableSequence38[ChangesetError]' = _list_4018(this_263._errors_810)
        eb_824.append(ChangesetError(field_821, message_822))
        return _ChangesetImpl(this_263._table_def_807, this_263._params_808, this_263._changes_809, _tuple_4020(eb_824), False)
    def cast(this_264, allowed_fields_826: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        mb_828: 'Dict39[str29, str29]' = {}
        this_3636: 'Sequence33[SafeIdentifier]' = allowed_fields_826
        n_3638: 'int35' = _len_4022(this_3636)
        i_3639: 'int35' = 0
        while i_3639 < n_3638:
            el_3640: 'SafeIdentifier' = _list_get_4023(this_3636, i_3639)
            i_3639 = _int_add_4024(i_3639, 1)
            f_829: 'SafeIdentifier' = el_3640
            val_830: 'str29' = this_264._params_808.get(f_829.sql_value, '')
            if not (not val_830):
                _map_builder_set_4027(mb_828, f_829.sql_value, val_830)
        return _ChangesetImpl(this_264._table_def_807, this_264._params_808, _mapped_to_map_4028(mb_828), this_264._errors_810, this_264._is_valid_811)
    def validate_required(this_265, fields_832: 'Sequence33[SafeIdentifier]', /) -> 'Changeset':
        return_461: 'Changeset'
        with Label40() as fn_833:
            if not this_265._is_valid_811:
                return_461 = this_265
                fn_833.break_()
            eb_834: 'MutableSequence38[ChangesetError]' = _list_4018(this_265._errors_810)
            valid_835: 'bool37' = True
            this_3641: 'Sequence33[SafeIdentifier]' = fields_832
            n_3643: 'int35' = _len_4022(this_3641)
            i_3644: 'int35' = 0
            while i_3644 < n_3643:
                el_3645: 'SafeIdentifier' = _list_get_4023(this_3641, i_3644)
                i_3644 = _int_add_4024(i_3644, 1)
                f_836: 'SafeIdentifier' = el_3645
                if not _mapped_has_4029(this_265._changes_809, f_836.sql_value):
                    eb_834.append(ChangesetError(f_836.sql_value, 'is required'))
                    valid_835 = False
            return _ChangesetImpl(this_265._table_def_807, this_265._params_808, this_265._changes_809, _tuple_4020(eb_834), valid_835)
        return return_461
    def validate_length(this_266, field_838: 'SafeIdentifier', min_839: 'int35', max_840: 'int35', /) -> 'Changeset':
        return_462: 'Changeset'
        with Label40() as fn_841:
            if not this_266._is_valid_811:
                return_462 = this_266
                fn_841.break_()
            val_842: 'str29' = this_266._changes_809.get(field_838.sql_value, '')
            len_843: 'int35' = _string_count_between_4030(val_842, 0, _len_4022(val_842))
            t_3617: 'bool37'
            if len_843 < min_839:
                t_3617 = True
            else:
                t_3617 = len_843 > max_840
            if t_3617:
                return_462 = this_266._add_error_820(field_838.sql_value, _str_cat_4031('must be between ', _int_to_string_4032(min_839), ' and ', _int_to_string_4032(max_840), ' characters'))
                fn_841.break_()
            return this_266
        return return_462
    def validate_int(this_267, field_845: 'SafeIdentifier', /) -> 'Changeset':
        return_463: 'Changeset'
        with Label40() as fn_846:
            if not this_267._is_valid_811:
                return_463 = this_267
                fn_846.break_()
            val_847: 'str29' = this_267._changes_809.get(field_845.sql_value, '')
            if not val_847:
                return_463 = this_267
                fn_846.break_()
            parse_ok_848: 'bool37'
            try:
                _string_to_int32_4033(val_847)
                parse_ok_848 = True
            except Exception41:
                parse_ok_848 = False
            if not parse_ok_848:
                return_463 = this_267._add_error_820(field_845.sql_value, 'must be an integer')
                fn_846.break_()
            return this_267
        return return_463
    def validate_int64(this_268, field_850: 'SafeIdentifier', /) -> 'Changeset':
        return_464: 'Changeset'
        with Label40() as fn_851:
            if not this_268._is_valid_811:
                return_464 = this_268
                fn_851.break_()
            val_852: 'str29' = this_268._changes_809.get(field_850.sql_value, '')
            if not val_852:
                return_464 = this_268
                fn_851.break_()
            parse_ok_853: 'bool37'
            try:
                _string_to_int64_4034(val_852)
                parse_ok_853 = True
            except Exception41:
                parse_ok_853 = False
            if not parse_ok_853:
                return_464 = this_268._add_error_820(field_850.sql_value, 'must be a 64-bit integer')
                fn_851.break_()
            return this_268
        return return_464
    def validate_float(this_269, field_855: 'SafeIdentifier', /) -> 'Changeset':
        return_465: 'Changeset'
        with Label40() as fn_856:
            if not this_269._is_valid_811:
                return_465 = this_269
                fn_856.break_()
            val_857: 'str29' = this_269._changes_809.get(field_855.sql_value, '')
            if not val_857:
                return_465 = this_269
                fn_856.break_()
            parse_ok_858: 'bool37'
            try:
                _string_to_float64_4035(val_857)
                parse_ok_858 = True
            except Exception41:
                parse_ok_858 = False
            if not parse_ok_858:
                return_465 = this_269._add_error_820(field_855.sql_value, 'must be a number')
                fn_856.break_()
            return this_269
        return return_465
    def validate_bool(this_270, field_860: 'SafeIdentifier', /) -> 'Changeset':
        return_466: 'Changeset'
        with Label40() as fn_861:
            if not this_270._is_valid_811:
                return_466 = this_270
                fn_861.break_()
            val_862: 'str29' = this_270._changes_809.get(field_860.sql_value, '')
            if not val_862:
                return_466 = this_270
                fn_861.break_()
            is_true_863: 'bool37'
            if val_862 == 'true':
                is_true_863 = True
            elif val_862 == '1':
                is_true_863 = True
            elif val_862 == 'yes':
                is_true_863 = True
            else:
                is_true_863 = val_862 == 'on'
            is_false_864: 'bool37'
            if val_862 == 'false':
                is_false_864 = True
            elif val_862 == '0':
                is_false_864 = True
            elif val_862 == 'no':
                is_false_864 = True
            else:
                is_false_864 = val_862 == 'off'
            t_3612: 'bool37'
            if not is_true_863:
                t_3612 = not is_false_864
            else:
                t_3612 = False
            if t_3612:
                return_466 = this_270._add_error_820(field_860.sql_value, 'must be a boolean (true/false/1/0/yes/no/on/off)')
                fn_861.break_()
            return this_270
        return return_466
    def put_change(this_271, field_866: 'SafeIdentifier', value_867: 'str29', /) -> 'Changeset':
        mb_869: 'Dict39[str29, str29]' = {}
        pairs_870: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4036(this_271._changes_809)
        i_871: 'int35' = 0
        while i_871 < _len_4022(pairs_870):
            _map_builder_set_4027(mb_869, _list_get_4023(pairs_870, i_871).key, _list_get_4023(pairs_870, i_871).value)
            i_871 = _int_add_4024(i_871, 1)
        _map_builder_set_4027(mb_869, field_866.sql_value, value_867)
        return _ChangesetImpl(this_271._table_def_807, this_271._params_808, _mapped_to_map_4028(mb_869), this_271._errors_810, this_271._is_valid_811)
    def get_change(this_272, field_873: 'SafeIdentifier', /) -> 'str29':
        if not _mapped_has_4029(this_272._changes_809, field_873.sql_value):
            raise RuntimeError34()
        return this_272._changes_809.get(field_873.sql_value, '')
    def delete_change(this_273, field_876: 'SafeIdentifier', /) -> 'Changeset':
        mb_878: 'Dict39[str29, str29]' = {}
        pairs_879: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4036(this_273._changes_809)
        i_880: 'int35' = 0
        while i_880 < _len_4022(pairs_879):
            if not _list_get_4023(pairs_879, i_880).key == field_876.sql_value:
                _map_builder_set_4027(mb_878, _list_get_4023(pairs_879, i_880).key, _list_get_4023(pairs_879, i_880).value)
            i_880 = _int_add_4024(i_880, 1)
        return _ChangesetImpl(this_273._table_def_807, this_273._params_808, _mapped_to_map_4028(mb_878), this_273._errors_810, this_273._is_valid_811)
    def validate_inclusion(this_274, field_882: 'SafeIdentifier', allowed_883: 'Sequence33[str29]', /) -> 'Changeset':
        return_470: 'Changeset'
        with Label40() as fn_884:
            if not this_274._is_valid_811:
                return_470 = this_274
                fn_884.break_()
            if not _mapped_has_4029(this_274._changes_809, field_882.sql_value):
                return_470 = this_274
                fn_884.break_()
            val_885: 'str29' = this_274._changes_809.get(field_882.sql_value, '')
            found_886: 'bool37' = False
            this_3646: 'Sequence33[str29]' = allowed_883
            n_3648: 'int35' = _len_4022(this_3646)
            i_3649: 'int35' = 0
            while i_3649 < n_3648:
                el_3650: 'str29' = _list_get_4023(this_3646, i_3649)
                i_3649 = _int_add_4024(i_3649, 1)
                a_887: 'str29' = el_3650
                if a_887 == val_885:
                    found_886 = True
            if not found_886:
                return_470 = this_274._add_error_820(field_882.sql_value, 'is not included in the list')
                fn_884.break_()
            return this_274
        return return_470
    def validate_exclusion(this_275, field_889: 'SafeIdentifier', disallowed_890: 'Sequence33[str29]', /) -> 'Changeset':
        return_471: 'Changeset'
        with Label40() as fn_891:
            if not this_275._is_valid_811:
                return_471 = this_275
                fn_891.break_()
            if not _mapped_has_4029(this_275._changes_809, field_889.sql_value):
                return_471 = this_275
                fn_891.break_()
            val_892: 'str29' = this_275._changes_809.get(field_889.sql_value, '')
            found_893: 'bool37' = False
            this_3651: 'Sequence33[str29]' = disallowed_890
            n_3653: 'int35' = _len_4022(this_3651)
            i_3654: 'int35' = 0
            while i_3654 < n_3653:
                el_3655: 'str29' = _list_get_4023(this_3651, i_3654)
                i_3654 = _int_add_4024(i_3654, 1)
                d_894: 'str29' = el_3655
                if d_894 == val_892:
                    found_893 = True
            if found_893:
                return_471 = this_275._add_error_820(field_889.sql_value, 'is reserved')
                fn_891.break_()
            return this_275
        return return_471
    def validate_number(this_276, field_896: 'SafeIdentifier', opts_897: 'NumberValidationOpts', /) -> 'Changeset':
        return_472: 'Changeset'
        with Label40() as fn_898:
            if not this_276._is_valid_811:
                return_472 = this_276
                fn_898.break_()
            if not _mapped_has_4029(this_276._changes_809, field_896.sql_value):
                return_472 = this_276
                fn_898.break_()
            val_899: 'str29' = this_276._changes_809.get(field_896.sql_value, '')
            parse_ok_900: 'bool37'
            try:
                _string_to_float64_4035(val_899)
                parse_ok_900 = True
            except Exception41:
                parse_ok_900 = False
            if not parse_ok_900:
                return_472 = this_276._add_error_820(field_896.sql_value, 'must be a number')
                fn_898.break_()
            num_901: 'float31'
            try:
                num_901 = _string_to_float64_4035(val_899)
            except Exception41:
                num_901 = 0.0
            gt_902: 'Union30[float31, None]' = opts_897.greater_than
            if not gt_902 is None:
                gt_2831: 'float31' = gt_902
                if not _float_cmp_4037(num_901, gt_2831) > 0:
                    return_472 = this_276._add_error_820(field_896.sql_value, _str_cat_4031('must be greater than ', _float64_to_string_4038(gt_2831)))
                    fn_898.break_()
            lt_903: 'Union30[float31, None]' = opts_897.less_than
            if not lt_903 is None:
                lt_2832: 'float31' = lt_903
                if not _float_cmp_4037(num_901, lt_2832) < 0:
                    return_472 = this_276._add_error_820(field_896.sql_value, _str_cat_4031('must be less than ', _float64_to_string_4038(lt_2832)))
                    fn_898.break_()
            gte_904: 'Union30[float31, None]' = opts_897.greater_than_or_equal
            if not gte_904 is None:
                gte_2833: 'float31' = gte_904
                if not _float_cmp_4037(num_901, gte_2833) >= 0:
                    return_472 = this_276._add_error_820(field_896.sql_value, _str_cat_4031('must be greater than or equal to ', _float64_to_string_4038(gte_2833)))
                    fn_898.break_()
            lte_905: 'Union30[float31, None]' = opts_897.less_than_or_equal
            if not lte_905 is None:
                lte_2834: 'float31' = lte_905
                if not _float_cmp_4037(num_901, lte_2834) <= 0:
                    return_472 = this_276._add_error_820(field_896.sql_value, _str_cat_4031('must be less than or equal to ', _float64_to_string_4038(lte_2834)))
                    fn_898.break_()
            eq_906: 'Union30[float31, None]' = opts_897.equal_to
            if not eq_906 is None:
                eq_2835: 'float31' = eq_906
                if not _float_eq_4039(num_901, eq_2835):
                    return_472 = this_276._add_error_820(field_896.sql_value, _str_cat_4031('must be equal to ', _float64_to_string_4038(eq_2835)))
                    fn_898.break_()
            return this_276
        return return_472
    def validate_acceptance(this_277, field_908: 'SafeIdentifier', /) -> 'Changeset':
        return_473: 'Changeset'
        with Label40() as fn_909:
            if not this_277._is_valid_811:
                return_473 = this_277
                fn_909.break_()
            if not _mapped_has_4029(this_277._changes_809, field_908.sql_value):
                return_473 = this_277
                fn_909.break_()
            val_910: 'str29' = this_277._changes_809.get(field_908.sql_value, '')
            accepted_911: 'bool37'
            if val_910 == 'true':
                accepted_911 = True
            elif val_910 == '1':
                accepted_911 = True
            elif val_910 == 'yes':
                accepted_911 = True
            else:
                accepted_911 = val_910 == 'on'
            if not accepted_911:
                return_473 = this_277._add_error_820(field_908.sql_value, 'must be accepted')
                fn_909.break_()
            return this_277
        return return_473
    def validate_confirmation(this_278, field_913: 'SafeIdentifier', confirmation_field_914: 'SafeIdentifier', /) -> 'Changeset':
        return_474: 'Changeset'
        with Label40() as fn_915:
            if not this_278._is_valid_811:
                return_474 = this_278
                fn_915.break_()
            if not _mapped_has_4029(this_278._changes_809, field_913.sql_value):
                return_474 = this_278
                fn_915.break_()
            val_916: 'str29' = this_278._changes_809.get(field_913.sql_value, '')
            conf_917: 'str29' = this_278._changes_809.get(confirmation_field_914.sql_value, '')
            if not val_916 == conf_917:
                return_474 = this_278._add_error_820(confirmation_field_914.sql_value, 'does not match')
                fn_915.break_()
            return this_278
        return return_474
    def validate_contains(this_279, field_919: 'SafeIdentifier', substring_920: 'str29', /) -> 'Changeset':
        return_475: 'Changeset'
        with Label40() as fn_921:
            if not this_279._is_valid_811:
                return_475 = this_279
                fn_921.break_()
            if not _mapped_has_4029(this_279._changes_809, field_919.sql_value):
                return_475 = this_279
                fn_921.break_()
            val_922: 'str29' = this_279._changes_809.get(field_919.sql_value, '')
            if not val_922.find(substring_920) >= 0:
                return_475 = this_279._add_error_820(field_919.sql_value, 'must contain the given substring')
                fn_921.break_()
            return this_279
        return return_475
    def validate_starts_with(this_280, field_924: 'SafeIdentifier', prefix_925: 'str29', /) -> 'Changeset':
        return_476: 'Changeset'
        with Label40() as fn_926:
            if not this_280._is_valid_811:
                return_476 = this_280
                fn_926.break_()
            if not _mapped_has_4029(this_280._changes_809, field_924.sql_value):
                return_476 = this_280
                fn_926.break_()
            val_927: 'str29' = this_280._changes_809.get(field_924.sql_value, '')
            idx_928: 'int35' = val_927.find(prefix_925)
            starts_929: 'bool37'
            if idx_928 >= 0:
                starts_929 = _string_count_between_4030(val_927, 0, _require_string_index_4042(idx_928)) == 0
            else:
                starts_929 = False
            if not starts_929:
                return_476 = this_280._add_error_820(field_924.sql_value, 'must start with the given prefix')
                fn_926.break_()
            return this_280
        return return_476
    def validate_ends_with(this_281, field_931: 'SafeIdentifier', suffix_932: 'str29', /) -> 'Changeset':
        return_477: 'Changeset'
        with Label40() as fn_933:
            if not this_281._is_valid_811:
                return_477 = this_281
                fn_933.break_()
            if not _mapped_has_4029(this_281._changes_809, field_931.sql_value):
                return_477 = this_281
                fn_933.break_()
            val_934: 'str29' = this_281._changes_809.get(field_931.sql_value, '')
            val_len_935: 'int35' = _string_count_between_4030(val_934, 0, _len_4022(val_934))
            suffix_len_936: 'int35' = _string_count_between_4030(suffix_932, 0, _len_4022(suffix_932))
            if val_len_935 < suffix_len_936:
                return_477 = this_281._add_error_820(field_931.sql_value, 'must end with the given suffix')
                fn_933.break_()
            skip_count_937: 'int35' = _int_sub_4043(val_len_935, suffix_len_936)
            str_idx_938: 'int35' = 0
            i_939: 'int35' = 0
            while i_939 < skip_count_937:
                str_idx_938 = _string_next_4044(val_934, str_idx_938)
                i_939 = _int_add_4024(i_939, 1)
            suf_idx_940: 'int35' = 0
            matches_941: 'bool37' = True
            while True:
                t_3587: 'bool37'
                if matches_941:
                    t_3587 = len2(suffix_932) > suf_idx_940
                else:
                    t_3587 = False
                if not t_3587:
                    break
                if not len2(val_934) > str_idx_938:
                    matches_941 = False
                elif not _string_get_4046(val_934, str_idx_938) == _string_get_4046(suffix_932, suf_idx_940):
                    matches_941 = False
                else:
                    str_idx_938 = _string_next_4044(val_934, str_idx_938)
                    suf_idx_940 = _string_next_4044(suffix_932, suf_idx_940)
            if not matches_941:
                return_477 = this_281._add_error_820(field_931.sql_value, 'must end with the given suffix')
                fn_933.break_()
            return this_281
        return return_477
    def _parse_bool_sql_part_942(this_282, val_943: 'str29', /) -> 'SqlBoolean':
        return_478: 'SqlBoolean'
        with Label40() as fn_944:
            t_3579: 'bool37'
            if val_943 == 'true':
                t_3579 = True
            elif val_943 == '1':
                t_3579 = True
            elif val_943 == 'yes':
                t_3579 = True
            else:
                t_3579 = val_943 == 'on'
            if t_3579:
                return_478 = SqlBoolean(True)
                fn_944.break_()
            t_3583: 'bool37'
            if val_943 == 'false':
                t_3583 = True
            elif val_943 == '0':
                t_3583 = True
            elif val_943 == 'no':
                t_3583 = True
            else:
                t_3583 = val_943 == 'off'
            if t_3583:
                return_478 = SqlBoolean(False)
                fn_944.break_()
            raise RuntimeError34()
        return return_478
    def _value_to_sql_part_945(this_283, field_def_946: 'FieldDef', val_947: 'str29', /) -> 'SqlPart':
        return_479: 'SqlPart'
        with Label40() as fn_948:
            ft_949: 'FieldType' = field_def_946.field_type
            if isinstance42(ft_949, StringField):
                return_479 = SqlString(val_947)
                fn_948.break_()
            if isinstance42(ft_949, IntField):
                t_3707: 'int35' = _string_to_int32_4033(val_947)
                return_479 = SqlInt32(t_3707)
                fn_948.break_()
            if isinstance42(ft_949, Int64Field):
                t_3708: '_int64' = _string_to_int64_4034(val_947)
                return_479 = SqlInt64(t_3708)
                fn_948.break_()
            if isinstance42(ft_949, FloatField):
                t_3709: 'float31' = _string_to_float64_4035(val_947)
                return_479 = SqlFloat64(t_3709)
                fn_948.break_()
            if isinstance42(ft_949, BoolField):
                return_479 = this_283._parse_bool_sql_part_942(val_947)
                fn_948.break_()
            if isinstance42(ft_949, DateField):
                t_3710: 'date28' = _date_from_iso_string_4047(val_947)
                return_479 = SqlDate(t_3710)
                fn_948.break_()
            raise RuntimeError34()
        return return_479
    def to_insert_sql(this_284, /) -> 'SqlFragment':
        if not this_284._is_valid_811:
            raise RuntimeError34()
        i_952: 'int35' = 0
        while i_952 < _len_4022(this_284._table_def_807.fields):
            with Label40() as continue_4014:
                f_953: 'FieldDef' = _list_get_4023(this_284._table_def_807.fields, i_952)
                if f_953.virtual:
                    continue_4014.break_()
                dv_954: 'Union30[SqlPart, None]' = f_953.default_value
                t_3564: 'bool37'
                if not f_953.nullable:
                    if not _mapped_has_4029(this_284._changes_809, f_953.name.sql_value):
                        t_3564 = dv_954 is None
                    else:
                        t_3564 = False
                else:
                    t_3564 = False
                if t_3564:
                    raise RuntimeError34()
            i_952 = _int_add_4024(i_952, 1)
        col_names_955: 'MutableSequence38[str29]' = _list_4018()
        val_parts_956: 'MutableSequence38[SqlPart]' = _list_4018()
        pairs_957: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4036(this_284._changes_809)
        i_958: 'int35' = 0
        while i_958 < _len_4022(pairs_957):
            with Label40() as continue_4015:
                pair_959: 'Pair27[str29, str29]' = _list_get_4023(pairs_957, i_958)
                fd_960: 'FieldDef' = this_284._table_def_807.field(pair_959.key)
                if fd_960.virtual:
                    continue_4015.break_()
                col_names_955.append(fd_960.name.sql_value)
                t_3706: 'SqlPart' = this_284._value_to_sql_part_945(fd_960, pair_959.value)
                val_parts_956.append(t_3706)
            i_958 = _int_add_4024(i_958, 1)
        i_961: 'int35' = 0
        while i_961 < _len_4022(this_284._table_def_807.fields):
            with Label40() as continue_4016:
                f_962: 'FieldDef' = _list_get_4023(this_284._table_def_807.fields, i_961)
                if f_962.virtual:
                    continue_4016.break_()
                dv_963: 'Union30[SqlPart, None]' = f_962.default_value
                if not dv_963 is None:
                    dv_2843: 'SqlPart' = dv_963
                    if not _mapped_has_4029(this_284._changes_809, f_962.name.sql_value):
                        col_names_955.append(f_962.name.sql_value)
                        val_parts_956.append(dv_2843)
            i_961 = _int_add_4024(i_961, 1)
        if _len_4022(val_parts_956) == 0:
            raise RuntimeError34()
        b_964: 'SqlBuilder' = SqlBuilder()
        b_964.append_safe('INSERT INTO ')
        b_964.append_safe(this_284._table_def_807.table_name.sql_value)
        b_964.append_safe(' (')
        def fn_4006(c_965: 'str29', /) -> 'str29':
            return c_965
        b_964.append_safe(_list_join_4048(_tuple_4020(col_names_955), ', ', fn_4006))
        b_964.append_safe(') VALUES (')
        b_964.append_part(_list_get_4023(val_parts_956, 0))
        j_966: 'int35' = 1
        while j_966 < _len_4022(val_parts_956):
            b_964.append_safe(', ')
            b_964.append_part(_list_get_4023(val_parts_956, j_966))
            j_966 = _int_add_4024(j_966, 1)
        b_964.append_safe(')')
        return b_964.accumulated
    def to_update_sql(this_285, id_968: 'int35', /) -> 'SqlFragment':
        if not this_285._is_valid_811:
            raise RuntimeError34()
        pairs_970: 'Sequence33[(Pair27[str29, str29])]' = _mapped_to_list_4036(this_285._changes_809)
        if _len_4022(pairs_970) == 0:
            raise RuntimeError34()
        b_971: 'SqlBuilder' = SqlBuilder()
        b_971.append_safe('UPDATE ')
        b_971.append_safe(this_285._table_def_807.table_name.sql_value)
        b_971.append_safe(' SET ')
        set_count_972: 'int35' = 0
        i_973: 'int35' = 0
        while i_973 < _len_4022(pairs_970):
            with Label40() as continue_4017:
                pair_974: 'Pair27[str29, str29]' = _list_get_4023(pairs_970, i_973)
                fd_975: 'FieldDef' = this_285._table_def_807.field(pair_974.key)
                if fd_975.virtual:
                    continue_4017.break_()
                if set_count_972 > 0:
                    b_971.append_safe(', ')
                b_971.append_safe(fd_975.name.sql_value)
                b_971.append_safe(' = ')
                t_3705: 'SqlPart' = this_285._value_to_sql_part_945(fd_975, pair_974.value)
                b_971.append_part(t_3705)
                set_count_972 = _int_add_4024(set_count_972, 1)
            i_973 = _int_add_4024(i_973, 1)
        if set_count_972 == 0:
            raise RuntimeError34()
        b_971.append_safe(' WHERE ')
        b_971.append_safe(this_285._table_def_807.pk_name())
        b_971.append_safe(' = ')
        b_971.append_int32(id_968)
        return b_971.accumulated
    def __init__(this_450, /, table_def: 'TableDef', params: 'MappingProxyType36[str29, str29]', changes: 'MappingProxyType36[str29, str29]', errors: 'Sequence33[ChangesetError]', is_valid: 'bool37') -> None:
        this_450._table_def_807 = table_def
        this_450._params_808 = params
        this_450._changes_809 = changes
        this_450._errors_810 = errors
        this_450._is_valid_811 = is_valid
class JoinType(metaclass = ABCMeta32):
    def keyword(this_306, /) -> 'str29':
        raise RuntimeError34()
class InnerJoin(JoinType):
    __slots__ = ()
    def keyword(this_307, /) -> 'str29':
        return 'INNER JOIN'
    def __init__(this_487, /) -> None:
        pass
class LeftJoin(JoinType):
    __slots__ = ()
    def keyword(this_308, /) -> 'str29':
        return 'LEFT JOIN'
    def __init__(this_490, /) -> None:
        pass
class RightJoin(JoinType):
    __slots__ = ()
    def keyword(this_309, /) -> 'str29':
        return 'RIGHT JOIN'
    def __init__(this_493, /) -> None:
        pass
class FullJoin(JoinType):
    __slots__ = ()
    def keyword(this_310, /) -> 'str29':
        return 'FULL OUTER JOIN'
    def __init__(this_496, /) -> None:
        pass
class CrossJoin(JoinType):
    __slots__ = ()
    def keyword(this_311, /) -> 'str29':
        return 'CROSS JOIN'
    def __init__(this_499, /) -> None:
        pass
class JoinClause:
    _join_type_1322: 'JoinType'
    _table_1323: 'SafeIdentifier'
    _on_condition_1324: 'Union30[SqlFragment, None]'
    __slots__ = ('_join_type_1322', '_table_1323', '_on_condition_1324')
    def __init__(this_502, /, join_type: 'JoinType', table: 'SafeIdentifier', on_condition: 'Union30[SqlFragment, None]') -> None:
        this_502._join_type_1322 = join_type
        this_502._table_1323 = table
        this_502._on_condition_1324 = on_condition
    @property
    def join_type(this_2361, /) -> 'JoinType':
        return this_2361._join_type_1322
    @property
    def table(this_2364, /) -> 'SafeIdentifier':
        return this_2364._table_1323
    @property
    def on_condition(this_2367, /) -> 'Union30[SqlFragment, None]':
        return this_2367._on_condition_1324
class NullsPosition(metaclass = ABCMeta32):
    def keyword(this_312, /) -> 'str29':
        raise RuntimeError34()
class NullsFirst(NullsPosition):
    __slots__ = ()
    def keyword(this_313, /) -> 'str29':
        return ' NULLS FIRST'
    def __init__(this_506, /) -> None:
        pass
class NullsLast(NullsPosition):
    __slots__ = ()
    def keyword(this_314, /) -> 'str29':
        return ' NULLS LAST'
    def __init__(this_509, /) -> None:
        pass
class OrderClause:
    _field_1337: 'SafeIdentifier'
    _ascending_1338: 'bool37'
    _nulls_pos_1339: 'Union30[NullsPosition, None]'
    __slots__ = ('_field_1337', '_ascending_1338', '_nulls_pos_1339')
    def __init__(this_512, /, field_1341: 'SafeIdentifier', ascending: 'bool37', nulls_pos: 'Union30[NullsPosition, None]') -> None:
        this_512._field_1337 = field_1341
        this_512._ascending_1338 = ascending
        this_512._nulls_pos_1339 = nulls_pos
    @property
    def field(this_2370, /) -> 'SafeIdentifier':
        return this_2370._field_1337
    @property
    def ascending(this_2373, /) -> 'bool37':
        return this_2373._ascending_1338
    @property
    def nulls_pos(this_2376, /) -> 'Union30[NullsPosition, None]':
        return this_2376._nulls_pos_1339
class LockMode(metaclass = ABCMeta32):
    def keyword(this_315, /) -> 'str29':
        raise RuntimeError34()
class ForUpdate(LockMode):
    __slots__ = ()
    def keyword(this_316, /) -> 'str29':
        return ' FOR UPDATE'
    def __init__(this_516, /) -> None:
        pass
class ForShare(LockMode):
    __slots__ = ()
    def keyword(this_317, /) -> 'str29':
        return ' FOR SHARE'
    def __init__(this_519, /) -> None:
        pass
class WhereClause(metaclass = ABCMeta32):
    def keyword(this_319, /) -> 'str29':
        raise RuntimeError34()
class AndCondition(WhereClause):
    _condition_1356: 'SqlFragment'
    __slots__ = ('_condition_1356',)
    @property
    def condition(this_320, /) -> 'SqlFragment':
        return this_320._condition_1356
    def keyword(this_321, /) -> 'str29':
        return 'AND'
    def __init__(this_526, /, condition: 'SqlFragment') -> None:
        this_526._condition_1356 = condition
class OrCondition(WhereClause):
    _condition_1363: 'SqlFragment'
    __slots__ = ('_condition_1363',)
    @property
    def condition(this_322, /) -> 'SqlFragment':
        return this_322._condition_1363
    def keyword(this_323, /) -> 'str29':
        return 'OR'
    def __init__(this_531, /, condition_1369: 'SqlFragment') -> None:
        this_531._condition_1363 = condition_1369
class Query:
    _table_name_1387: 'SafeIdentifier'
    _conditions_1388: 'Sequence33[WhereClause]'
    _selected_fields_1389: 'Sequence33[SafeIdentifier]'
    _order_clauses_1390: 'Sequence33[OrderClause]'
    _limit_val_1391: 'Union30[int35, None]'
    _offset_val_1392: 'Union30[int35, None]'
    _join_clauses_1393: 'Sequence33[JoinClause]'
    _group_by_fields_1394: 'Sequence33[SafeIdentifier]'
    _having_conditions_1395: 'Sequence33[WhereClause]'
    _is_distinct_1396: 'bool37'
    _select_exprs_1397: 'Sequence33[SqlFragment]'
    _lock_mode_1398: 'Union30[LockMode, None]'
    __slots__ = ('_table_name_1387', '_conditions_1388', '_selected_fields_1389', '_order_clauses_1390', '_limit_val_1391', '_offset_val_1392', '_join_clauses_1393', '_group_by_fields_1394', '_having_conditions_1395', '_is_distinct_1396', '_select_exprs_1397', '_lock_mode_1398')
    def where(this_324, condition_1400: 'SqlFragment', /) -> 'Query':
        nb_1402: 'MutableSequence38[WhereClause]' = _list_4018(this_324._conditions_1388)
        nb_1402.append(AndCondition(condition_1400))
        return Query(this_324._table_name_1387, _tuple_4020(nb_1402), this_324._selected_fields_1389, this_324._order_clauses_1390, this_324._limit_val_1391, this_324._offset_val_1392, this_324._join_clauses_1393, this_324._group_by_fields_1394, this_324._having_conditions_1395, this_324._is_distinct_1396, this_324._select_exprs_1397, this_324._lock_mode_1398)
    def or_where(this_325, condition_1404: 'SqlFragment', /) -> 'Query':
        nb_1406: 'MutableSequence38[WhereClause]' = _list_4018(this_325._conditions_1388)
        nb_1406.append(OrCondition(condition_1404))
        return Query(this_325._table_name_1387, _tuple_4020(nb_1406), this_325._selected_fields_1389, this_325._order_clauses_1390, this_325._limit_val_1391, this_325._offset_val_1392, this_325._join_clauses_1393, this_325._group_by_fields_1394, this_325._having_conditions_1395, this_325._is_distinct_1396, this_325._select_exprs_1397, this_325._lock_mode_1398)
    def where_null(this_326, field_1408: 'SafeIdentifier', /) -> 'Query':
        b_1410: 'SqlBuilder' = SqlBuilder()
        b_1410.append_safe(field_1408.sql_value)
        b_1410.append_safe(' IS NULL')
        return this_326.where(b_1410.accumulated)
    def where_not_null(this_327, field_1412: 'SafeIdentifier', /) -> 'Query':
        b_1414: 'SqlBuilder' = SqlBuilder()
        b_1414.append_safe(field_1412.sql_value)
        b_1414.append_safe(' IS NOT NULL')
        return this_327.where(b_1414.accumulated)
    def where_in(this_328, field_1416: 'SafeIdentifier', values_1417: 'Sequence33[SqlPart]', /) -> 'Query':
        return_555: 'Query'
        with Label40() as fn_1418:
            if not values_1417:
                b_1419: 'SqlBuilder' = SqlBuilder()
                b_1419.append_safe('1 = 0')
                return_555 = this_328.where(b_1419.accumulated)
                fn_1418.break_()
            b_1420: 'SqlBuilder' = SqlBuilder()
            b_1420.append_safe(field_1416.sql_value)
            b_1420.append_safe(' IN (')
            b_1420.append_part(_list_get_4023(values_1417, 0))
            i_1421: 'int35' = 1
            while i_1421 < _len_4022(values_1417):
                b_1420.append_safe(', ')
                b_1420.append_part(_list_get_4023(values_1417, i_1421))
                i_1421 = _int_add_4024(i_1421, 1)
            b_1420.append_safe(')')
            return this_328.where(b_1420.accumulated)
        return return_555
    def where_in_subquery(this_329, field_1423: 'SafeIdentifier', sub_1424: 'Query', /) -> 'Query':
        b_1426: 'SqlBuilder' = SqlBuilder()
        b_1426.append_safe(field_1423.sql_value)
        b_1426.append_safe(' IN (')
        b_1426.append_fragment(sub_1424.to_sql())
        b_1426.append_safe(')')
        return this_329.where(b_1426.accumulated)
    def where_not(this_330, condition_1428: 'SqlFragment', /) -> 'Query':
        b_1430: 'SqlBuilder' = SqlBuilder()
        b_1430.append_safe('NOT (')
        b_1430.append_fragment(condition_1428)
        b_1430.append_safe(')')
        return this_330.where(b_1430.accumulated)
    def where_between(this_331, field_1432: 'SafeIdentifier', low_1433: 'SqlPart', high_1434: 'SqlPart', /) -> 'Query':
        b_1436: 'SqlBuilder' = SqlBuilder()
        b_1436.append_safe(field_1432.sql_value)
        b_1436.append_safe(' BETWEEN ')
        b_1436.append_part(low_1433)
        b_1436.append_safe(' AND ')
        b_1436.append_part(high_1434)
        return this_331.where(b_1436.accumulated)
    def where_like(this_332, field_1438: 'SafeIdentifier', pattern_1439: 'str29', /) -> 'Query':
        b_1441: 'SqlBuilder' = SqlBuilder()
        b_1441.append_safe(field_1438.sql_value)
        b_1441.append_safe(' LIKE ')
        b_1441.append_string(pattern_1439)
        return this_332.where(b_1441.accumulated)
    def where_i_like(this_333, field_1443: 'SafeIdentifier', pattern_1444: 'str29', /) -> 'Query':
        b_1446: 'SqlBuilder' = SqlBuilder()
        b_1446.append_safe(field_1443.sql_value)
        b_1446.append_safe(' ILIKE ')
        b_1446.append_string(pattern_1444)
        return this_333.where(b_1446.accumulated)
    def select(this_334, fields_1448: 'Sequence33[SafeIdentifier]', /) -> 'Query':
        return Query(this_334._table_name_1387, this_334._conditions_1388, fields_1448, this_334._order_clauses_1390, this_334._limit_val_1391, this_334._offset_val_1392, this_334._join_clauses_1393, this_334._group_by_fields_1394, this_334._having_conditions_1395, this_334._is_distinct_1396, this_334._select_exprs_1397, this_334._lock_mode_1398)
    def select_expr(this_335, exprs_1451: 'Sequence33[SqlFragment]', /) -> 'Query':
        return Query(this_335._table_name_1387, this_335._conditions_1388, this_335._selected_fields_1389, this_335._order_clauses_1390, this_335._limit_val_1391, this_335._offset_val_1392, this_335._join_clauses_1393, this_335._group_by_fields_1394, this_335._having_conditions_1395, this_335._is_distinct_1396, exprs_1451, this_335._lock_mode_1398)
    def order_by(this_336, field_1454: 'SafeIdentifier', ascending_1455: 'bool37', /) -> 'Query':
        nb_1457: 'MutableSequence38[OrderClause]' = _list_4018(this_336._order_clauses_1390)
        nb_1457.append(OrderClause(field_1454, ascending_1455, None))
        return Query(this_336._table_name_1387, this_336._conditions_1388, this_336._selected_fields_1389, _tuple_4020(nb_1457), this_336._limit_val_1391, this_336._offset_val_1392, this_336._join_clauses_1393, this_336._group_by_fields_1394, this_336._having_conditions_1395, this_336._is_distinct_1396, this_336._select_exprs_1397, this_336._lock_mode_1398)
    def order_by_nulls(this_337, field_1459: 'SafeIdentifier', ascending_1460: 'bool37', nulls_1461: 'NullsPosition', /) -> 'Query':
        nb_1463: 'MutableSequence38[OrderClause]' = _list_4018(this_337._order_clauses_1390)
        nb_1463.append(OrderClause(field_1459, ascending_1460, nulls_1461))
        return Query(this_337._table_name_1387, this_337._conditions_1388, this_337._selected_fields_1389, _tuple_4020(nb_1463), this_337._limit_val_1391, this_337._offset_val_1392, this_337._join_clauses_1393, this_337._group_by_fields_1394, this_337._having_conditions_1395, this_337._is_distinct_1396, this_337._select_exprs_1397, this_337._lock_mode_1398)
    def limit(this_338, n_1465: 'int35', /) -> 'Query':
        if n_1465 < 0:
            raise RuntimeError34()
        return Query(this_338._table_name_1387, this_338._conditions_1388, this_338._selected_fields_1389, this_338._order_clauses_1390, n_1465, this_338._offset_val_1392, this_338._join_clauses_1393, this_338._group_by_fields_1394, this_338._having_conditions_1395, this_338._is_distinct_1396, this_338._select_exprs_1397, this_338._lock_mode_1398)
    def offset(this_339, n_1468: 'int35', /) -> 'Query':
        if n_1468 < 0:
            raise RuntimeError34()
        return Query(this_339._table_name_1387, this_339._conditions_1388, this_339._selected_fields_1389, this_339._order_clauses_1390, this_339._limit_val_1391, n_1468, this_339._join_clauses_1393, this_339._group_by_fields_1394, this_339._having_conditions_1395, this_339._is_distinct_1396, this_339._select_exprs_1397, this_339._lock_mode_1398)
    def join(this_340, join_type_1471: 'JoinType', table_1472: 'SafeIdentifier', on_condition_1473: 'SqlFragment', /) -> 'Query':
        nb_1475: 'MutableSequence38[JoinClause]' = _list_4018(this_340._join_clauses_1393)
        nb_1475.append(JoinClause(join_type_1471, table_1472, on_condition_1473))
        return Query(this_340._table_name_1387, this_340._conditions_1388, this_340._selected_fields_1389, this_340._order_clauses_1390, this_340._limit_val_1391, this_340._offset_val_1392, _tuple_4020(nb_1475), this_340._group_by_fields_1394, this_340._having_conditions_1395, this_340._is_distinct_1396, this_340._select_exprs_1397, this_340._lock_mode_1398)
    def inner_join(this_341, table_1477: 'SafeIdentifier', on_condition_1478: 'SqlFragment', /) -> 'Query':
        return this_341.join(InnerJoin(), table_1477, on_condition_1478)
    def left_join(this_342, table_1481: 'SafeIdentifier', on_condition_1482: 'SqlFragment', /) -> 'Query':
        return this_342.join(LeftJoin(), table_1481, on_condition_1482)
    def right_join(this_343, table_1485: 'SafeIdentifier', on_condition_1486: 'SqlFragment', /) -> 'Query':
        return this_343.join(RightJoin(), table_1485, on_condition_1486)
    def full_join(this_344, table_1489: 'SafeIdentifier', on_condition_1490: 'SqlFragment', /) -> 'Query':
        return this_344.join(FullJoin(), table_1489, on_condition_1490)
    def cross_join(this_345, table_1493: 'SafeIdentifier', /) -> 'Query':
        nb_1495: 'MutableSequence38[JoinClause]' = _list_4018(this_345._join_clauses_1393)
        nb_1495.append(JoinClause(CrossJoin(), table_1493, None))
        return Query(this_345._table_name_1387, this_345._conditions_1388, this_345._selected_fields_1389, this_345._order_clauses_1390, this_345._limit_val_1391, this_345._offset_val_1392, _tuple_4020(nb_1495), this_345._group_by_fields_1394, this_345._having_conditions_1395, this_345._is_distinct_1396, this_345._select_exprs_1397, this_345._lock_mode_1398)
    def group_by(this_346, field_1497: 'SafeIdentifier', /) -> 'Query':
        nb_1499: 'MutableSequence38[SafeIdentifier]' = _list_4018(this_346._group_by_fields_1394)
        nb_1499.append(field_1497)
        return Query(this_346._table_name_1387, this_346._conditions_1388, this_346._selected_fields_1389, this_346._order_clauses_1390, this_346._limit_val_1391, this_346._offset_val_1392, this_346._join_clauses_1393, _tuple_4020(nb_1499), this_346._having_conditions_1395, this_346._is_distinct_1396, this_346._select_exprs_1397, this_346._lock_mode_1398)
    def having(this_347, condition_1501: 'SqlFragment', /) -> 'Query':
        nb_1503: 'MutableSequence38[WhereClause]' = _list_4018(this_347._having_conditions_1395)
        nb_1503.append(AndCondition(condition_1501))
        return Query(this_347._table_name_1387, this_347._conditions_1388, this_347._selected_fields_1389, this_347._order_clauses_1390, this_347._limit_val_1391, this_347._offset_val_1392, this_347._join_clauses_1393, this_347._group_by_fields_1394, _tuple_4020(nb_1503), this_347._is_distinct_1396, this_347._select_exprs_1397, this_347._lock_mode_1398)
    def or_having(this_348, condition_1505: 'SqlFragment', /) -> 'Query':
        nb_1507: 'MutableSequence38[WhereClause]' = _list_4018(this_348._having_conditions_1395)
        nb_1507.append(OrCondition(condition_1505))
        return Query(this_348._table_name_1387, this_348._conditions_1388, this_348._selected_fields_1389, this_348._order_clauses_1390, this_348._limit_val_1391, this_348._offset_val_1392, this_348._join_clauses_1393, this_348._group_by_fields_1394, _tuple_4020(nb_1507), this_348._is_distinct_1396, this_348._select_exprs_1397, this_348._lock_mode_1398)
    def distinct(this_349, /) -> 'Query':
        return Query(this_349._table_name_1387, this_349._conditions_1388, this_349._selected_fields_1389, this_349._order_clauses_1390, this_349._limit_val_1391, this_349._offset_val_1392, this_349._join_clauses_1393, this_349._group_by_fields_1394, this_349._having_conditions_1395, True, this_349._select_exprs_1397, this_349._lock_mode_1398)
    def lock(this_350, mode_1511: 'LockMode', /) -> 'Query':
        return Query(this_350._table_name_1387, this_350._conditions_1388, this_350._selected_fields_1389, this_350._order_clauses_1390, this_350._limit_val_1391, this_350._offset_val_1392, this_350._join_clauses_1393, this_350._group_by_fields_1394, this_350._having_conditions_1395, this_350._is_distinct_1396, this_350._select_exprs_1397, mode_1511)
    def to_sql(this_351, /) -> 'SqlFragment':
        b_1515: 'SqlBuilder' = SqlBuilder()
        if this_351._is_distinct_1396:
            b_1515.append_safe('SELECT DISTINCT ')
        else:
            b_1515.append_safe('SELECT ')
        if not (not this_351._select_exprs_1397):
            b_1515.append_fragment(_list_get_4023(this_351._select_exprs_1397, 0))
            i_1516: 'int35' = 1
            while i_1516 < _len_4022(this_351._select_exprs_1397):
                b_1515.append_safe(', ')
                b_1515.append_fragment(_list_get_4023(this_351._select_exprs_1397, i_1516))
                i_1516 = _int_add_4024(i_1516, 1)
        elif not this_351._selected_fields_1389:
            b_1515.append_safe('*')
        else:
            def fn_3878(f_1517: 'SafeIdentifier', /) -> 'str29':
                return f_1517.sql_value
            b_1515.append_safe(_list_join_4048(this_351._selected_fields_1389, ', ', fn_3878))
        b_1515.append_safe(' FROM ')
        b_1515.append_safe(this_351._table_name_1387.sql_value)
        _render_joins(b_1515, this_351._join_clauses_1393)
        _render_where(b_1515, this_351._conditions_1388)
        _render_group_by(b_1515, this_351._group_by_fields_1394)
        _render_having(b_1515, this_351._having_conditions_1395)
        if not (not this_351._order_clauses_1390):
            b_1515.append_safe(' ORDER BY ')
            first_1518: 'bool37' = True
            this_3686: 'Sequence33[OrderClause]' = this_351._order_clauses_1390
            n_3688: 'int35' = _len_4022(this_3686)
            i_3689: 'int35' = 0
            while i_3689 < n_3688:
                el_3690: 'OrderClause' = _list_get_4023(this_3686, i_3689)
                i_3689 = _int_add_4024(i_3689, 1)
                orc_1519: 'OrderClause' = el_3690
                t_3459: 'str29'
                if not first_1518:
                    b_1515.append_safe(', ')
                first_1518 = False
                b_1515.append_safe(orc_1519.field.sql_value)
                if orc_1519.ascending:
                    t_3459 = ' ASC'
                else:
                    t_3459 = ' DESC'
                b_1515.append_safe(t_3459)
                np_1520: 'Union30[NullsPosition, None]' = orc_1519.nulls_pos
                if not np_1520 is None:
                    b_1515.append_safe(np_1520.keyword())
        lv_1521: 'Union30[int35, None]' = this_351._limit_val_1391
        if not lv_1521 is None:
            lv_2846: 'int35' = lv_1521
            b_1515.append_safe(' LIMIT ')
            b_1515.append_int32(lv_2846)
        ov_1522: 'Union30[int35, None]' = this_351._offset_val_1392
        if not ov_1522 is None:
            ov_2847: 'int35' = ov_1522
            b_1515.append_safe(' OFFSET ')
            b_1515.append_int32(ov_2847)
        lm_1523: 'Union30[LockMode, None]' = this_351._lock_mode_1398
        if not lm_1523 is None:
            b_1515.append_safe(lm_1523.keyword())
        return b_1515.accumulated
    def count_sql(this_352, /) -> 'SqlFragment':
        b_1526: 'SqlBuilder' = SqlBuilder()
        b_1526.append_safe('SELECT COUNT(*) FROM ')
        b_1526.append_safe(this_352._table_name_1387.sql_value)
        _render_joins(b_1526, this_352._join_clauses_1393)
        _render_where(b_1526, this_352._conditions_1388)
        _render_group_by(b_1526, this_352._group_by_fields_1394)
        _render_having(b_1526, this_352._having_conditions_1395)
        return b_1526.accumulated
    def safe_to_sql(this_353, default_limit_1528: 'int35', /) -> 'SqlFragment':
        if default_limit_1528 < 0:
            raise RuntimeError34()
        if not this_353._limit_val_1391 is None:
            return this_353.to_sql()
        else:
            t_3702: 'Query' = this_353.limit(default_limit_1528)
            return t_3702.to_sql()
    def __init__(this_539, /, table_name: 'SafeIdentifier', conditions: 'Sequence33[WhereClause]', selected_fields: 'Sequence33[SafeIdentifier]', order_clauses: 'Sequence33[OrderClause]', limit_val: 'Union30[int35, None]', offset_val: 'Union30[int35, None]', join_clauses: 'Sequence33[JoinClause]', group_by_fields: 'Sequence33[SafeIdentifier]', having_conditions: 'Sequence33[WhereClause]', is_distinct: 'bool37', select_exprs: 'Sequence33[SqlFragment]', lock_mode: 'Union30[LockMode, None]') -> None:
        this_539._table_name_1387 = table_name
        this_539._conditions_1388 = conditions
        this_539._selected_fields_1389 = selected_fields
        this_539._order_clauses_1390 = order_clauses
        this_539._limit_val_1391 = limit_val
        this_539._offset_val_1392 = offset_val
        this_539._join_clauses_1393 = join_clauses
        this_539._group_by_fields_1394 = group_by_fields
        this_539._having_conditions_1395 = having_conditions
        this_539._is_distinct_1396 = is_distinct
        this_539._select_exprs_1397 = select_exprs
        this_539._lock_mode_1398 = lock_mode
    @property
    def table_name(this_2379, /) -> 'SafeIdentifier':
        return this_2379._table_name_1387
    @property
    def conditions(this_2382, /) -> 'Sequence33[WhereClause]':
        return this_2382._conditions_1388
    @property
    def selected_fields(this_2385, /) -> 'Sequence33[SafeIdentifier]':
        return this_2385._selected_fields_1389
    @property
    def order_clauses(this_2388, /) -> 'Sequence33[OrderClause]':
        return this_2388._order_clauses_1390
    @property
    def limit_val(this_2391, /) -> 'Union30[int35, None]':
        return this_2391._limit_val_1391
    @property
    def offset_val(this_2394, /) -> 'Union30[int35, None]':
        return this_2394._offset_val_1392
    @property
    def join_clauses(this_2397, /) -> 'Sequence33[JoinClause]':
        return this_2397._join_clauses_1393
    @property
    def group_by_fields(this_2400, /) -> 'Sequence33[SafeIdentifier]':
        return this_2400._group_by_fields_1394
    @property
    def having_conditions(this_2403, /) -> 'Sequence33[WhereClause]':
        return this_2403._having_conditions_1395
    @property
    def is_distinct(this_2406, /) -> 'bool37':
        return this_2406._is_distinct_1396
    @property
    def select_exprs(this_2409, /) -> 'Sequence33[SqlFragment]':
        return this_2409._select_exprs_1397
    @property
    def lock_mode(this_2412, /) -> 'Union30[LockMode, None]':
        return this_2412._lock_mode_1398
class SetClause:
    _field_1589: 'SafeIdentifier'
    _value_1590: 'SqlPart'
    __slots__ = ('_field_1589', '_value_1590')
    def __init__(this_595, /, field_1592: 'SafeIdentifier', value: 'SqlPart') -> None:
        this_595._field_1589 = field_1592
        this_595._value_1590 = value
    @property
    def field(this_2415, /) -> 'SafeIdentifier':
        return this_2415._field_1589
    @property
    def value(this_2418, /) -> 'SqlPart':
        return this_2418._value_1590
class UpdateQuery:
    _table_name_1594: 'SafeIdentifier'
    _set_clauses_1595: 'Sequence33[SetClause]'
    _conditions_1596: 'Sequence33[WhereClause]'
    _limit_val_1597: 'Union30[int35, None]'
    __slots__ = ('_table_name_1594', '_set_clauses_1595', '_conditions_1596', '_limit_val_1597')
    def set(this_354, field_1599: 'SafeIdentifier', value_1600: 'SqlPart', /) -> 'UpdateQuery':
        nb_1602: 'MutableSequence38[SetClause]' = _list_4018(this_354._set_clauses_1595)
        nb_1602.append(SetClause(field_1599, value_1600))
        return UpdateQuery(this_354._table_name_1594, _tuple_4020(nb_1602), this_354._conditions_1596, this_354._limit_val_1597)
    def where(this_355, condition_1604: 'SqlFragment', /) -> 'UpdateQuery':
        nb_1606: 'MutableSequence38[WhereClause]' = _list_4018(this_355._conditions_1596)
        nb_1606.append(AndCondition(condition_1604))
        return UpdateQuery(this_355._table_name_1594, this_355._set_clauses_1595, _tuple_4020(nb_1606), this_355._limit_val_1597)
    def or_where(this_356, condition_1608: 'SqlFragment', /) -> 'UpdateQuery':
        nb_1610: 'MutableSequence38[WhereClause]' = _list_4018(this_356._conditions_1596)
        nb_1610.append(OrCondition(condition_1608))
        return UpdateQuery(this_356._table_name_1594, this_356._set_clauses_1595, _tuple_4020(nb_1610), this_356._limit_val_1597)
    def limit(this_357, n_1612: 'int35', /) -> 'UpdateQuery':
        if n_1612 < 0:
            raise RuntimeError34()
        return UpdateQuery(this_357._table_name_1594, this_357._set_clauses_1595, this_357._conditions_1596, n_1612)
    def to_sql(this_358, /) -> 'SqlFragment':
        if not this_358._conditions_1596:
            raise RuntimeError34()
        if not this_358._set_clauses_1595:
            raise RuntimeError34()
        b_1616: 'SqlBuilder' = SqlBuilder()
        b_1616.append_safe('UPDATE ')
        b_1616.append_safe(this_358._table_name_1594.sql_value)
        b_1616.append_safe(' SET ')
        b_1616.append_safe(_list_get_4023(this_358._set_clauses_1595, 0).field.sql_value)
        b_1616.append_safe(' = ')
        b_1616.append_part(_list_get_4023(this_358._set_clauses_1595, 0).value)
        i_1617: 'int35' = 1
        while i_1617 < _len_4022(this_358._set_clauses_1595):
            b_1616.append_safe(', ')
            b_1616.append_safe(_list_get_4023(this_358._set_clauses_1595, i_1617).field.sql_value)
            b_1616.append_safe(' = ')
            b_1616.append_part(_list_get_4023(this_358._set_clauses_1595, i_1617).value)
            i_1617 = _int_add_4024(i_1617, 1)
        _render_where(b_1616, this_358._conditions_1596)
        lv_1618: 'Union30[int35, None]' = this_358._limit_val_1597
        if not lv_1618 is None:
            lv_2849: 'int35' = lv_1618
            b_1616.append_safe(' LIMIT ')
            b_1616.append_int32(lv_2849)
        return b_1616.accumulated
    def __init__(this_597, /, table_name_1620: 'SafeIdentifier', set_clauses: 'Sequence33[SetClause]', conditions_1622: 'Sequence33[WhereClause]', limit_val_1623: 'Union30[int35, None]') -> None:
        this_597._table_name_1594 = table_name_1620
        this_597._set_clauses_1595 = set_clauses
        this_597._conditions_1596 = conditions_1622
        this_597._limit_val_1597 = limit_val_1623
    @property
    def table_name(this_2421, /) -> 'SafeIdentifier':
        return this_2421._table_name_1594
    @property
    def set_clauses(this_2424, /) -> 'Sequence33[SetClause]':
        return this_2424._set_clauses_1595
    @property
    def conditions(this_2427, /) -> 'Sequence33[WhereClause]':
        return this_2427._conditions_1596
    @property
    def limit_val(this_2430, /) -> 'Union30[int35, None]':
        return this_2430._limit_val_1597
class DeleteQuery:
    _table_name_1624: 'SafeIdentifier'
    _conditions_1625: 'Sequence33[WhereClause]'
    _limit_val_1626: 'Union30[int35, None]'
    __slots__ = ('_table_name_1624', '_conditions_1625', '_limit_val_1626')
    def where(this_359, condition_1628: 'SqlFragment', /) -> 'DeleteQuery':
        nb_1630: 'MutableSequence38[WhereClause]' = _list_4018(this_359._conditions_1625)
        nb_1630.append(AndCondition(condition_1628))
        return DeleteQuery(this_359._table_name_1624, _tuple_4020(nb_1630), this_359._limit_val_1626)
    def or_where(this_360, condition_1632: 'SqlFragment', /) -> 'DeleteQuery':
        nb_1634: 'MutableSequence38[WhereClause]' = _list_4018(this_360._conditions_1625)
        nb_1634.append(OrCondition(condition_1632))
        return DeleteQuery(this_360._table_name_1624, _tuple_4020(nb_1634), this_360._limit_val_1626)
    def limit(this_361, n_1636: 'int35', /) -> 'DeleteQuery':
        if n_1636 < 0:
            raise RuntimeError34()
        return DeleteQuery(this_361._table_name_1624, this_361._conditions_1625, n_1636)
    def to_sql(this_362, /) -> 'SqlFragment':
        if not this_362._conditions_1625:
            raise RuntimeError34()
        b_1640: 'SqlBuilder' = SqlBuilder()
        b_1640.append_safe('DELETE FROM ')
        b_1640.append_safe(this_362._table_name_1624.sql_value)
        _render_where(b_1640, this_362._conditions_1625)
        lv_1641: 'Union30[int35, None]' = this_362._limit_val_1626
        if not lv_1641 is None:
            lv_2850: 'int35' = lv_1641
            b_1640.append_safe(' LIMIT ')
            b_1640.append_int32(lv_2850)
        return b_1640.accumulated
    def __init__(this_607, /, table_name_1643: 'SafeIdentifier', conditions_1644: 'Sequence33[WhereClause]', limit_val_1645: 'Union30[int35, None]') -> None:
        this_607._table_name_1624 = table_name_1643
        this_607._conditions_1625 = conditions_1644
        this_607._limit_val_1626 = limit_val_1645
    @property
    def table_name(this_2433, /) -> 'SafeIdentifier':
        return this_2433._table_name_1624
    @property
    def conditions(this_2436, /) -> 'Sequence33[WhereClause]':
        return this_2436._conditions_1625
    @property
    def limit_val(this_2439, /) -> 'Union30[int35, None]':
        return this_2439._limit_val_1626
class SafeIdentifier(metaclass = ABCMeta32):
    pass
class _ValidatedIdentifier(SafeIdentifier):
    _value_1901: 'str29'
    __slots__ = ('_value_1901',)
    @property
    def sql_value(this_365, /) -> 'str29':
        return this_365._value_1901
    def __init__(this_621, /, value_1905: 'str29') -> None:
        this_621._value_1901 = value_1905
class FieldType(metaclass = ABCMeta32):
    pass
class StringField(FieldType):
    __slots__ = ()
    def __init__(this_627, /) -> None:
        pass
class IntField(FieldType):
    __slots__ = ()
    def __init__(this_629, /) -> None:
        pass
class Int64Field(FieldType):
    __slots__ = ()
    def __init__(this_631, /) -> None:
        pass
class FloatField(FieldType):
    __slots__ = ()
    def __init__(this_633, /) -> None:
        pass
class BoolField(FieldType):
    __slots__ = ()
    def __init__(this_635, /) -> None:
        pass
class DateField(FieldType):
    __slots__ = ()
    def __init__(this_637, /) -> None:
        pass
class FieldDef:
    _name_1919: 'SafeIdentifier'
    _field_type_1920: 'FieldType'
    _nullable_1921: 'bool37'
    _default_value_1922: 'Union30[SqlPart, None]'
    _virtual_1923: 'bool37'
    __slots__ = ('_name_1919', '_field_type_1920', '_nullable_1921', '_default_value_1922', '_virtual_1923')
    def __init__(this_639, /, name: 'SafeIdentifier', field_type: 'FieldType', nullable: 'bool37', default_value: 'Union30[SqlPart, None]', virtual: 'bool37') -> None:
        this_639._name_1919 = name
        this_639._field_type_1920 = field_type
        this_639._nullable_1921 = nullable
        this_639._default_value_1922 = default_value
        this_639._virtual_1923 = virtual
    @property
    def name(this_2225, /) -> 'SafeIdentifier':
        return this_2225._name_1919
    @property
    def field_type(this_2228, /) -> 'FieldType':
        return this_2228._field_type_1920
    @property
    def nullable(this_2231, /) -> 'bool37':
        return this_2231._nullable_1921
    @property
    def default_value(this_2234, /) -> 'Union30[SqlPart, None]':
        return this_2234._default_value_1922
    @property
    def virtual(this_2237, /) -> 'bool37':
        return this_2237._virtual_1923
class TableDef:
    _table_name_1930: 'SafeIdentifier'
    _fields_1931: 'Sequence33[FieldDef]'
    _primary_key_1932: 'Union30[SafeIdentifier, None]'
    __slots__ = ('_table_name_1930', '_fields_1931', '_primary_key_1932')
    def field(this_372, name_1934: 'str29', /) -> 'FieldDef':
        return_646: 'FieldDef'
        with Label40() as fn_1935:
            this_3623: 'Sequence33[FieldDef]' = this_372._fields_1931
            n_3625: 'int35' = _len_4022(this_3623)
            i_3626: 'int35' = 0
            while i_3626 < n_3625:
                el_3627: 'FieldDef' = _list_get_4023(this_3623, i_3626)
                i_3626 = _int_add_4024(i_3626, 1)
                f_1936: 'FieldDef' = el_3627
                if f_1936.name.sql_value == name_1934:
                    return_646 = f_1936
                    fn_1935.break_()
            raise RuntimeError34()
        return return_646
    def pk_name(this_373, /) -> 'str29':
        return_647: 'str29'
        with Label40() as fn_1938:
            pk_1939: 'Union30[SafeIdentifier, None]' = this_373._primary_key_1932
            if not pk_1939 is None:
                return_647 = pk_1939.sql_value
                fn_1938.break_()
            return 'id'
        return return_647
    def __init__(this_642, /, table_name_1941: 'SafeIdentifier', fields: 'Sequence33[FieldDef]', primary_key: 'Union30[SafeIdentifier, None]') -> None:
        this_642._table_name_1930 = table_name_1941
        this_642._fields_1931 = fields
        this_642._primary_key_1932 = primary_key
    @property
    def table_name(this_2240, /) -> 'SafeIdentifier':
        return this_2240._table_name_1930
    @property
    def fields(this_2243, /) -> 'Sequence33[FieldDef]':
        return this_2243._fields_1931
    @property
    def primary_key(this_2246, /) -> 'Union30[SafeIdentifier, None]':
        return this_2246._primary_key_1932
T_392 = TypeVar44('T_392', bound = Any43)
class SqlBuilder:
    _buffer_1984: 'MutableSequence38[SqlPart]'
    __slots__ = ('_buffer_1984',)
    def append_safe(this_374, sql_source_1986: 'str29', /) -> 'None':
        this_374._buffer_1984.append(SqlSource(sql_source_1986))
    def append_fragment(this_375, fragment_1989: 'SqlFragment', /) -> 'None':
        _list_builder_add_all_4049(this_375._buffer_1984, fragment_1989.parts)
    def append_part(this_376, part_1992: 'SqlPart', /) -> 'None':
        this_376._buffer_1984.append(part_1992)
    def append_part_list(this_377, values_1995: 'Sequence33[SqlPart]', /) -> 'None':
        def fn_4013(x_1997: 'SqlPart', /) -> 'None':
            this_377.append_part(x_1997)
        this_377._append_list_2040(values_1995, fn_4013)
    def append_boolean(this_378, value_1999: 'bool37', /) -> 'None':
        this_378._buffer_1984.append(SqlBoolean(value_1999))
    def append_boolean_list(this_379, values_2002: 'Sequence33[bool37]', /) -> 'None':
        def fn_4012(x_2004: 'bool37', /) -> 'None':
            this_379.append_boolean(x_2004)
        this_379._append_list_2040(values_2002, fn_4012)
    def append_date(this_380, value_2006: 'date28', /) -> 'None':
        this_380._buffer_1984.append(SqlDate(value_2006))
    def append_date_list(this_381, values_2009: 'Sequence33[date28]', /) -> 'None':
        def fn_4011(x_2011: 'date28', /) -> 'None':
            this_381.append_date(x_2011)
        this_381._append_list_2040(values_2009, fn_4011)
    def append_float64(this_382, value_2013: 'float31', /) -> 'None':
        this_382._buffer_1984.append(SqlFloat64(value_2013))
    def append_float64_list(this_383, values_2016: 'Sequence33[float31]', /) -> 'None':
        def fn_4010(x_2018: 'float31', /) -> 'None':
            this_383.append_float64(x_2018)
        this_383._append_list_2040(values_2016, fn_4010)
    def append_int32(this_384, value_2020: 'int35', /) -> 'None':
        this_384._buffer_1984.append(SqlInt32(value_2020))
    def append_int32_list(this_385, values_2023: 'Sequence33[int35]', /) -> 'None':
        def fn_4009(x_2025: 'int35', /) -> 'None':
            this_385.append_int32(x_2025)
        this_385._append_list_2040(values_2023, fn_4009)
    def append_int64(this_386, value_2027: '_int64', /) -> 'None':
        this_386._buffer_1984.append(SqlInt64(value_2027))
    def append_int64_list(this_387, values_2030: 'Sequence33[_int64]', /) -> 'None':
        def fn_4008(x_2032: '_int64', /) -> 'None':
            this_387.append_int64(x_2032)
        this_387._append_list_2040(values_2030, fn_4008)
    def append_string(this_388, value_2034: 'str29', /) -> 'None':
        this_388._buffer_1984.append(SqlString(value_2034))
    def append_string_list(this_389, values_2037: 'Sequence33[str29]', /) -> 'None':
        def fn_4007(x_2039: 'str29', /) -> 'None':
            this_389.append_string(x_2039)
        this_389._append_list_2040(values_2037, fn_4007)
    def _append_list_2040(this_390, values_2041: 'Sequence33[T_392]', append_value_2042: 'Callable45[[T_392], None]', /) -> 'None':
        i_2044: 'int35' = 0
        while i_2044 < _len_4022(values_2041):
            if i_2044 > 0:
                this_390.append_safe(', ')
            append_value_2042(_list_get_4023(values_2041, i_2044))
            i_2044 = _int_add_4024(i_2044, 1)
    @property
    def accumulated(this_391, /) -> 'SqlFragment':
        return SqlFragment(_tuple_4020(this_391._buffer_1984))
    def __init__(this_650, /) -> None:
        t_2152: 'MutableSequence38[SqlPart]' = _list_4018()
        this_650._buffer_1984 = t_2152
class SqlFragment:
    _parts_2051: 'Sequence33[SqlPart]'
    __slots__ = ('_parts_2051',)
    def to_source(this_396, /) -> 'SqlSource':
        return SqlSource(this_396.to_string())
    def to_string(this_397, /) -> 'str29':
        builder_2056: 'list0[str29]' = ['']
        i_2057: 'int35' = 0
        while i_2057 < _len_4022(this_397._parts_2051):
            _list_get_4023(this_397._parts_2051, i_2057).format_to(builder_2056)
            i_2057 = _int_add_4024(i_2057, 1)
        return ''.join(builder_2056)
    def __init__(this_671, /, parts: 'Sequence33[SqlPart]') -> None:
        this_671._parts_2051 = parts
    @property
    def parts(this_2252, /) -> 'Sequence33[SqlPart]':
        return this_2252._parts_2051
class SqlPart(metaclass = ABCMeta32):
    def format_to(this_398, builder_2061: 'list0[str29]', /) -> 'None':
        raise RuntimeError34()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped."
    _source_2063: 'str29'
    __slots__ = ('_source_2063',)
    def format_to(this_399, builder_2065: 'list0[str29]', /) -> 'None':
        builder_2065.append(this_399._source_2063)
    def __init__(this_677, /, source: 'str29') -> None:
        this_677._source_2063 = source
    @property
    def source(this_2249, /) -> 'str29':
        return this_2249._source_2063
class SqlBoolean(SqlPart):
    _value_2069: 'bool37'
    __slots__ = ('_value_2069',)
    def format_to(this_400, builder_2071: 'list0[str29]', /) -> 'None':
        t_3622: 'str29'
        if this_400._value_2069:
            t_3622 = 'TRUE'
        else:
            t_3622 = 'FALSE'
        builder_2071.append(t_3622)
    def __init__(this_680, /, value_2074: 'bool37') -> None:
        this_680._value_2069 = value_2074
    @property
    def value(this_2255, /) -> 'bool37':
        return this_2255._value_2069
class SqlDate(SqlPart):
    _value_2075: 'date28'
    __slots__ = ('_value_2075',)
    def format_to(this_401, builder_2077: 'list0[str29]', /) -> 'None':
        builder_2077.append("'")
        this_3632: 'str29' = _date_to_string_4053(this_401._value_2075)
        index_3634: 'int35' = 0
        while len2(this_3632) > index_3634:
            code_point_3635: 'int35' = _string_get_4046(this_3632, index_3634)
            c_2079: 'int35' = code_point_3635
            if c_2079 == 39:
                builder_2077.append("''")
            else:
                builder_2077.append(string_from_code_point46(c_2079))
            index_3634 = _string_next_4044(this_3632, index_3634)
        builder_2077.append("'")
    def __init__(this_683, /, value_2081: 'date28') -> None:
        this_683._value_2075 = value_2081
    @property
    def value(this_2270, /) -> 'date28':
        return this_2270._value_2075
class SqlFloat64(SqlPart):
    _value_2082: 'float31'
    __slots__ = ('_value_2082',)
    def format_to(this_402, builder_2084: 'list0[str29]', /) -> 'None':
        s_2086: 'str29' = _float64_to_string_4038(this_402._value_2082)
        t_3619: 'bool37'
        if s_2086 == 'NaN':
            t_3619 = True
        elif s_2086 == 'Infinity':
            t_3619 = True
        else:
            t_3619 = s_2086 == '-Infinity'
        if t_3619:
            builder_2084.append('NULL')
        else:
            builder_2084.append(s_2086)
    def __init__(this_686, /, value_2088: 'float31') -> None:
        this_686._value_2082 = value_2088
    @property
    def value(this_2267, /) -> 'float31':
        return this_2267._value_2082
class SqlInt32(SqlPart):
    _value_2089: 'int35'
    __slots__ = ('_value_2089',)
    def format_to(this_405, builder_2091: 'list0[str29]', /) -> 'None':
        builder_2091.append(_int_to_string_4032(this_405._value_2089))
    def __init__(this_689, /, value_2094: 'int35') -> None:
        this_689._value_2089 = value_2094
    @property
    def value(this_2261, /) -> 'int35':
        return this_2261._value_2089
class SqlInt64(SqlPart):
    _value_2095: '_int64'
    __slots__ = ('_value_2095',)
    def format_to(this_406, builder_2097: 'list0[str29]', /) -> 'None':
        builder_2097.append(_int_to_string_4032(this_406._value_2095))
    def __init__(this_692, /, value_2100: '_int64') -> None:
        this_692._value_2095 = value_2100
    @property
    def value(this_2264, /) -> '_int64':
        return this_2264._value_2095
class SqlDefault(SqlPart):
    '`SqlDefault` renders the literal SQL keyword `DEFAULT`, used for columns\nwith server-side default values (e.g., `NOW()` for timestamps).'
    __slots__ = ()
    def format_to(this_407, builder_2102: 'list0[str29]', /) -> 'None':
        builder_2102.append('DEFAULT')
    def __init__(this_695, /) -> None:
        pass
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    _value_2105: 'str29'
    __slots__ = ('_value_2105',)
    def format_to(this_408, builder_2107: 'list0[str29]', /) -> 'None':
        builder_2107.append("'")
        this_3628: 'str29' = this_408._value_2105
        index_3630: 'int35' = 0
        while len2(this_3628) > index_3630:
            code_point_3631: 'int35' = _string_get_4046(this_3628, index_3630)
            c_2109: 'int35' = code_point_3631
            if c_2109 == 39:
                builder_2107.append("''")
            else:
                builder_2107.append(string_from_code_point46(c_2109))
            index_3630 = _string_next_4044(this_3628, index_3630)
        builder_2107.append("'")
    def __init__(this_698, /, value_2111: 'str29') -> None:
        this_698._value_2105 = value_2111
    @property
    def value(this_2258, /) -> 'str29':
        return this_2258._value_2105
def changeset(table_def_982: 'TableDef', params_983: 'MappingProxyType36[str29, str29]', /) -> 'Changeset':
    return _ChangesetImpl(table_def_982, params_983, _map_constructor_4055(()), (), True)
def _is_ident_start(c_1906: 'int35', /) -> 'bool37':
    t_3560: 'bool37'
    if c_1906 >= 97:
        t_3560 = c_1906 <= 122
    else:
        t_3560 = False
    if t_3560:
        return True
    else:
        t_3562: 'bool37'
        if c_1906 >= 65:
            t_3562 = c_1906 <= 90
        else:
            t_3562 = False
        if t_3562:
            return True
        else:
            return c_1906 == 95
def _is_ident_part(c_1908: 'int35', /) -> 'bool37':
    if _is_ident_start(c_1908):
        return True
    elif c_1908 >= 48:
        return c_1908 <= 57
    else:
        return False
def safe_identifier(name_1910: 'str29', /) -> 'SafeIdentifier':
    if not name_1910:
        raise RuntimeError34()
    idx_1912: 'int35' = 0
    if not _is_ident_start(_string_get_4046(name_1910, idx_1912)):
        raise RuntimeError34()
    idx_1912 = _string_next_4044(name_1910, idx_1912)
    while len2(name_1910) > idx_1912:
        if not _is_ident_part(_string_get_4046(name_1910, idx_1912)):
            raise RuntimeError34()
        idx_1912 = _string_next_4044(name_1910, idx_1912)
    return _ValidatedIdentifier(name_1910)
def timestamps() -> 'Sequence33[FieldDef]':
    t_3703: 'SafeIdentifier' = safe_identifier('inserted_at')
    t_3704: 'SafeIdentifier' = safe_identifier('updated_at')
    return (FieldDef(t_3703, DateField(), True, SqlDefault(), False), FieldDef(t_3704, DateField(), True, SqlDefault(), False))
def delete_sql(table_def_1301: 'TableDef', id_1302: 'int35', /) -> 'SqlFragment':
    b_1304: 'SqlBuilder' = SqlBuilder()
    b_1304.append_safe('DELETE FROM ')
    b_1304.append_safe(table_def_1301.table_name.sql_value)
    b_1304.append_safe(' WHERE ')
    b_1304.append_safe(table_def_1301.pk_name())
    b_1304.append_safe(' = ')
    b_1304.append_int32(id_1302)
    return b_1304.accumulated
def _render_where(b_1370: 'SqlBuilder', conditions_1371: 'Sequence33[WhereClause]', /) -> 'None':
    if not (not conditions_1371):
        b_1370.append_safe(' WHERE ')
        b_1370.append_fragment(_list_get_4023(conditions_1371, 0).condition)
        i_1373: 'int35' = 1
        while i_1373 < _len_4022(conditions_1371):
            b_1370.append_safe(' ')
            b_1370.append_safe(_list_get_4023(conditions_1371, i_1373).keyword())
            b_1370.append_safe(' ')
            b_1370.append_fragment(_list_get_4023(conditions_1371, i_1373).condition)
            i_1373 = _int_add_4024(i_1373, 1)
def _render_joins(b_1374: 'SqlBuilder', join_clauses_1375: 'Sequence33[JoinClause]', /) -> 'None':
    this_3681: 'Sequence33[JoinClause]' = join_clauses_1375
    n_3683: 'int35' = _len_4022(this_3681)
    i_3684: 'int35' = 0
    while i_3684 < n_3683:
        el_3685: 'JoinClause' = _list_get_4023(this_3681, i_3684)
        i_3684 = _int_add_4024(i_3684, 1)
        jc_1377: 'JoinClause' = el_3685
        b_1374.append_safe(' ')
        b_1374.append_safe(jc_1377.join_type.keyword())
        b_1374.append_safe(' ')
        b_1374.append_safe(jc_1377.table.sql_value)
        oc_1378: 'Union30[SqlFragment, None]' = jc_1377.on_condition
        if not oc_1378 is None:
            oc_2844: 'SqlFragment' = oc_1378
            b_1374.append_safe(' ON ')
            b_1374.append_fragment(oc_2844)
def _render_group_by(b_1379: 'SqlBuilder', group_by_fields_1380: 'Sequence33[SafeIdentifier]', /) -> 'None':
    if not (not group_by_fields_1380):
        b_1379.append_safe(' GROUP BY ')
        def fn_3879(f_1382: 'SafeIdentifier', /) -> 'str29':
            return f_1382.sql_value
        b_1379.append_safe(_list_join_4048(group_by_fields_1380, ', ', fn_3879))
def _render_having(b_1383: 'SqlBuilder', having_conditions_1384: 'Sequence33[WhereClause]', /) -> 'None':
    if not (not having_conditions_1384):
        b_1383.append_safe(' HAVING ')
        b_1383.append_fragment(_list_get_4023(having_conditions_1384, 0).condition)
        i_1386: 'int35' = 1
        while i_1386 < _len_4022(having_conditions_1384):
            b_1383.append_safe(' ')
            b_1383.append_safe(_list_get_4023(having_conditions_1384, i_1386).keyword())
            b_1383.append_safe(' ')
            b_1383.append_fragment(_list_get_4023(having_conditions_1384, i_1386).condition)
            i_1386 = _int_add_4024(i_1386, 1)
def from_(table_name_1543: 'SafeIdentifier', /) -> 'Query':
    return Query(table_name_1543, (), (), (), None, None, (), (), (), False, (), None)
def col(table_1545: 'SafeIdentifier', column_1546: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1548: 'SqlBuilder' = SqlBuilder()
    b_1548.append_safe(table_1545.sql_value)
    b_1548.append_safe('.')
    b_1548.append_safe(column_1546.sql_value)
    return b_1548.accumulated
def count_all() -> 'SqlFragment':
    b_1550: 'SqlBuilder' = SqlBuilder()
    b_1550.append_safe('COUNT(*)')
    return b_1550.accumulated
def count_col(field_1551: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1553: 'SqlBuilder' = SqlBuilder()
    b_1553.append_safe('COUNT(')
    b_1553.append_safe(field_1551.sql_value)
    b_1553.append_safe(')')
    return b_1553.accumulated
def sum_col(field_1554: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1556: 'SqlBuilder' = SqlBuilder()
    b_1556.append_safe('SUM(')
    b_1556.append_safe(field_1554.sql_value)
    b_1556.append_safe(')')
    return b_1556.accumulated
def avg_col(field_1557: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1559: 'SqlBuilder' = SqlBuilder()
    b_1559.append_safe('AVG(')
    b_1559.append_safe(field_1557.sql_value)
    b_1559.append_safe(')')
    return b_1559.accumulated
def min_col(field_1560: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1562: 'SqlBuilder' = SqlBuilder()
    b_1562.append_safe('MIN(')
    b_1562.append_safe(field_1560.sql_value)
    b_1562.append_safe(')')
    return b_1562.accumulated
def max_col(field_1563: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1565: 'SqlBuilder' = SqlBuilder()
    b_1565.append_safe('MAX(')
    b_1565.append_safe(field_1563.sql_value)
    b_1565.append_safe(')')
    return b_1565.accumulated
def union_sql(a_1566: 'Query', b_1567: 'Query', /) -> 'SqlFragment':
    sb_1569: 'SqlBuilder' = SqlBuilder()
    sb_1569.append_safe('(')
    sb_1569.append_fragment(a_1566.to_sql())
    sb_1569.append_safe(') UNION (')
    sb_1569.append_fragment(b_1567.to_sql())
    sb_1569.append_safe(')')
    return sb_1569.accumulated
def union_all_sql(a_1570: 'Query', b_1571: 'Query', /) -> 'SqlFragment':
    sb_1573: 'SqlBuilder' = SqlBuilder()
    sb_1573.append_safe('(')
    sb_1573.append_fragment(a_1570.to_sql())
    sb_1573.append_safe(') UNION ALL (')
    sb_1573.append_fragment(b_1571.to_sql())
    sb_1573.append_safe(')')
    return sb_1573.accumulated
def intersect_sql(a_1574: 'Query', b_1575: 'Query', /) -> 'SqlFragment':
    sb_1577: 'SqlBuilder' = SqlBuilder()
    sb_1577.append_safe('(')
    sb_1577.append_fragment(a_1574.to_sql())
    sb_1577.append_safe(') INTERSECT (')
    sb_1577.append_fragment(b_1575.to_sql())
    sb_1577.append_safe(')')
    return sb_1577.accumulated
def except_sql(a_1578: 'Query', b_1579: 'Query', /) -> 'SqlFragment':
    sb_1581: 'SqlBuilder' = SqlBuilder()
    sb_1581.append_safe('(')
    sb_1581.append_fragment(a_1578.to_sql())
    sb_1581.append_safe(') EXCEPT (')
    sb_1581.append_fragment(b_1579.to_sql())
    sb_1581.append_safe(')')
    return sb_1581.accumulated
def subquery(q_1582: 'Query', alias_1583: 'SafeIdentifier', /) -> 'SqlFragment':
    b_1585: 'SqlBuilder' = SqlBuilder()
    b_1585.append_safe('(')
    b_1585.append_fragment(q_1582.to_sql())
    b_1585.append_safe(') AS ')
    b_1585.append_safe(alias_1583.sql_value)
    return b_1585.accumulated
def exists_sql(q_1586: 'Query', /) -> 'SqlFragment':
    b_1588: 'SqlBuilder' = SqlBuilder()
    b_1588.append_safe('EXISTS (')
    b_1588.append_fragment(q_1586.to_sql())
    b_1588.append_safe(')')
    return b_1588.accumulated
def update(table_name_1646: 'SafeIdentifier', /) -> 'UpdateQuery':
    return UpdateQuery(table_name_1646, (), (), None)
def delete_from(table_name_1648: 'SafeIdentifier', /) -> 'DeleteQuery':
    return DeleteQuery(table_name_1648, (), None)
