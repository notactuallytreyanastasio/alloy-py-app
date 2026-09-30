from temper_std.testing import Test
from builtins import str as str29, int as int35, bool as bool37, Exception as Exception41, float as float31
from unittest import TestCase as TestCase48
from types import MappingProxyType as MappingProxyType36
from typing import Sequence as Sequence33, MutableSequence as MutableSequence38
from datetime import date as date28
from math import nan as nan259, inf as inf261
from orm.src import safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, _map_constructor_4055, _pair_4056, changeset, Changeset, _mapped_has_4029, _len_4022, _list_get_4023, _int_add_4024, _str_cat_4031, SqlFragment, NumberValidationOpts, SqlDefault, timestamps, _list_4018, _tuple_4020, delete_sql, _int_to_string_4032, Int64Field, DateField, from_, Query, SqlBuilder, SafeIdentifier, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, update, UpdateQuery, SqlBoolean, delete_from, DeleteQuery, NullsFirst, NullsLast, ForUpdate, ForShare, _date_4057, SqlPart
def _csid(name_985: 'str29', /) -> 'SafeIdentifier':
    return safe_identifier(name_985)
def _user_table() -> 'TableDef':
    return TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('email'), StringField(), False, None, False), FieldDef(_csid('age'), IntField(), True, None, False), FieldDef(_csid('score'), FloatField(), True, None, False), FieldDef(_csid('active'), BoolField(), True, None, False)), None)
class TestCase47(TestCase48):
    def test___castWhitelistsAllowedFields__2272(self) -> None:
        'cast whitelists allowed fields'
        test_12: Test = Test()
        try:
            params_989: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('email', 'alice@example.com'), _pair_4056('admin', 'true')))
            cs_990: 'Changeset' = changeset(_user_table(), params_989).cast((_csid('name'), _csid('email')))
            def fn_4005() -> 'str29':
                return 'name should be in changes'
            test_12.assert_(_mapped_has_4029(cs_990.changes, 'name'), fn_4005)
            def fn_4004() -> 'str29':
                return 'email should be in changes'
            test_12.assert_(_mapped_has_4029(cs_990.changes, 'email'), fn_4004)
            def fn_4003() -> 'str29':
                return 'admin must be dropped (not in whitelist)'
            test_12.assert_(not _mapped_has_4029(cs_990.changes, 'admin'), fn_4003)
            def fn_4002() -> 'str29':
                return 'should still be valid'
            test_12.assert_(cs_990.is_valid, fn_4002)
        finally:
            test_12.soft_fail_to_hard()
class TestCase49(TestCase48):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__2273(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_13: Test = Test()
        try:
            params_992: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('email', 'alice@example.com')))
            cs_993: 'Changeset' = changeset(_user_table(), params_992).cast((_csid('name'),)).cast((_csid('email'),))
            def fn_4001() -> 'str29':
                return 'name must be excluded by second cast'
            test_13.assert_(not _mapped_has_4029(cs_993.changes, 'name'), fn_4001)
            def fn_4000() -> 'str29':
                return 'email should be present'
            test_13.assert_(_mapped_has_4029(cs_993.changes, 'email'), fn_4000)
        finally:
            test_13.soft_fail_to_hard()
class TestCase50(TestCase48):
    def test___castIgnoresEmptyStringValues__2274(self) -> None:
        'cast ignores empty string values'
        test_14: Test = Test()
        try:
            params_995: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', ''), _pair_4056('email', 'bob@example.com')))
            cs_996: 'Changeset' = changeset(_user_table(), params_995).cast((_csid('name'), _csid('email')))
            def fn_3999() -> 'str29':
                return 'empty name should not be in changes'
            test_14.assert_(not _mapped_has_4029(cs_996.changes, 'name'), fn_3999)
            def fn_3998() -> 'str29':
                return 'email should be in changes'
            test_14.assert_(_mapped_has_4029(cs_996.changes, 'email'), fn_3998)
        finally:
            test_14.soft_fail_to_hard()
class TestCase51(TestCase48):
    def test___validateRequiredPassesWhenFieldPresent__2275(self) -> None:
        'validateRequired passes when field present'
        test_15: Test = Test()
        try:
            params_998: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_999: 'Changeset' = changeset(_user_table(), params_998).cast((_csid('name'),)).validate_required((_csid('name'),))
            def fn_3997() -> 'str29':
                return 'should be valid'
            test_15.assert_(cs_999.is_valid, fn_3997)
            def fn_3996() -> 'str29':
                return 'no errors expected'
            test_15.assert_(_len_4022(cs_999.errors) == 0, fn_3996)
        finally:
            test_15.soft_fail_to_hard()
class TestCase52(TestCase48):
    def test___validateRequiredFailsWhenFieldMissing__2276(self) -> None:
        'validateRequired fails when field missing'
        test_16: Test = Test()
        try:
            params_1001: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1002: 'Changeset' = changeset(_user_table(), params_1001).cast((_csid('name'),)).validate_required((_csid('name'),))
            def fn_3995() -> 'str29':
                return 'should be invalid'
            test_16.assert_(not cs_1002.is_valid, fn_3995)
            def fn_3994() -> 'str29':
                return 'should have one error'
            test_16.assert_(_len_4022(cs_1002.errors) == 1, fn_3994)
            def fn_3993() -> 'str29':
                return 'error should name the field'
            test_16.assert_(_list_get_4023(cs_1002.errors, 0).field == 'name', fn_3993)
        finally:
            test_16.soft_fail_to_hard()
class TestCase53(TestCase48):
    def test___validateLengthPassesWithinRange__2277(self) -> None:
        'validateLength passes within range'
        test_17: Test = Test()
        try:
            params_1004: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1005: 'Changeset' = changeset(_user_table(), params_1004).cast((_csid('name'),)).validate_length(_csid('name'), 2, 50)
            def fn_3992() -> 'str29':
                return 'should be valid'
            test_17.assert_(cs_1005.is_valid, fn_3992)
        finally:
            test_17.soft_fail_to_hard()
class TestCase54(TestCase48):
    def test___validateLengthFailsWhenTooShort__2278(self) -> None:
        'validateLength fails when too short'
        test_18: Test = Test()
        try:
            params_1007: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'A'),))
            cs_1008: 'Changeset' = changeset(_user_table(), params_1007).cast((_csid('name'),)).validate_length(_csid('name'), 2, 50)
            def fn_3991() -> 'str29':
                return 'should be invalid'
            test_18.assert_(not cs_1008.is_valid, fn_3991)
        finally:
            test_18.soft_fail_to_hard()
class TestCase55(TestCase48):
    def test___validateLengthFailsWhenTooLong__2279(self) -> None:
        'validateLength fails when too long'
        test_19: Test = Test()
        try:
            params_1010: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            cs_1011: 'Changeset' = changeset(_user_table(), params_1010).cast((_csid('name'),)).validate_length(_csid('name'), 2, 10)
            def fn_3990() -> 'str29':
                return 'should be invalid'
            test_19.assert_(not cs_1011.is_valid, fn_3990)
        finally:
            test_19.soft_fail_to_hard()
class TestCase56(TestCase48):
    def test___validateIntPassesForValidInteger__2280(self) -> None:
        'validateInt passes for valid integer'
        test_20: Test = Test()
        try:
            params_1013: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '30'),))
            cs_1014: 'Changeset' = changeset(_user_table(), params_1013).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_3989() -> 'str29':
                return 'should be valid'
            test_20.assert_(cs_1014.is_valid, fn_3989)
        finally:
            test_20.soft_fail_to_hard()
class TestCase57(TestCase48):
    def test___validateIntFailsForNonInteger__2281(self) -> None:
        'validateInt fails for non-integer'
        test_21: Test = Test()
        try:
            params_1016: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', 'not-a-number'),))
            cs_1017: 'Changeset' = changeset(_user_table(), params_1016).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_3988() -> 'str29':
                return 'should be invalid'
            test_21.assert_(not cs_1017.is_valid, fn_3988)
        finally:
            test_21.soft_fail_to_hard()
class TestCase58(TestCase48):
    def test___validateFloatPassesForValidFloat__2282(self) -> None:
        'validateFloat passes for valid float'
        test_22: Test = Test()
        try:
            params_1019: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '9.5'),))
            cs_1020: 'Changeset' = changeset(_user_table(), params_1019).cast((_csid('score'),)).validate_float(_csid('score'))
            def fn_3987() -> 'str29':
                return 'should be valid'
            test_22.assert_(cs_1020.is_valid, fn_3987)
        finally:
            test_22.soft_fail_to_hard()
class TestCase59(TestCase48):
    def test___validateInt64_passesForValid64_bitInteger__2283(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_23: Test = Test()
        try:
            params_1022: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '9999999999'),))
            cs_1023: 'Changeset' = changeset(_user_table(), params_1022).cast((_csid('age'),)).validate_int64(_csid('age'))
            def fn_3986() -> 'str29':
                return 'should be valid'
            test_23.assert_(cs_1023.is_valid, fn_3986)
        finally:
            test_23.soft_fail_to_hard()
class TestCase60(TestCase48):
    def test___validateInt64_failsForNonInteger__2284(self) -> None:
        'validateInt64 fails for non-integer'
        test_24: Test = Test()
        try:
            params_1025: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', 'not-a-number'),))
            cs_1026: 'Changeset' = changeset(_user_table(), params_1025).cast((_csid('age'),)).validate_int64(_csid('age'))
            def fn_3985() -> 'str29':
                return 'should be invalid'
            test_24.assert_(not cs_1026.is_valid, fn_3985)
        finally:
            test_24.soft_fail_to_hard()
class TestCase61(TestCase48):
    def test___validateBoolAcceptsTrue1_yesOn__2285(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_25: Test = Test()
        try:
            this_3656: 'Sequence33[str29]' = ('true', '1', 'yes', 'on')
            n_3658: 'int35' = _len_4022(this_3656)
            i_3659: 'int35' = 0
            while i_3659 < n_3658:
                el_3660: 'str29' = _list_get_4023(this_3656, i_3659)
                i_3659 = _int_add_4024(i_3659, 1)
                v_1028: 'str29' = el_3660
                params_1029: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('active', v_1028),))
                cs_1030: 'Changeset' = changeset(_user_table(), params_1029).cast((_csid('active'),)).validate_bool(_csid('active'))
                def fn_3984() -> 'str29':
                    return _str_cat_4031('should accept: ', v_1028)
                test_25.assert_(cs_1030.is_valid, fn_3984)
        finally:
            test_25.soft_fail_to_hard()
class TestCase62(TestCase48):
    def test___validateBoolAcceptsFalse0_noOff__2286(self) -> None:
        'validateBool accepts false/0/no/off'
        test_26: Test = Test()
        try:
            this_3661: 'Sequence33[str29]' = ('false', '0', 'no', 'off')
            n_3663: 'int35' = _len_4022(this_3661)
            i_3664: 'int35' = 0
            while i_3664 < n_3663:
                el_3665: 'str29' = _list_get_4023(this_3661, i_3664)
                i_3664 = _int_add_4024(i_3664, 1)
                v_1032: 'str29' = el_3665
                params_1033: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('active', v_1032),))
                cs_1034: 'Changeset' = changeset(_user_table(), params_1033).cast((_csid('active'),)).validate_bool(_csid('active'))
                def fn_3983() -> 'str29':
                    return _str_cat_4031('should accept: ', v_1032)
                test_26.assert_(cs_1034.is_valid, fn_3983)
        finally:
            test_26.soft_fail_to_hard()
class TestCase63(TestCase48):
    def test___validateBoolRejectsAmbiguousValues__2287(self) -> None:
        'validateBool rejects ambiguous values'
        test_27: Test = Test()
        try:
            this_3666: 'Sequence33[str29]' = ('TRUE', 'Yes', 'maybe', '2', 'enabled')
            n_3668: 'int35' = _len_4022(this_3666)
            i_3669: 'int35' = 0
            while i_3669 < n_3668:
                el_3670: 'str29' = _list_get_4023(this_3666, i_3669)
                i_3669 = _int_add_4024(i_3669, 1)
                v_1036: 'str29' = el_3670
                params_1037: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('active', v_1036),))
                cs_1038: 'Changeset' = changeset(_user_table(), params_1037).cast((_csid('active'),)).validate_bool(_csid('active'))
                def fn_3982() -> 'str29':
                    return _str_cat_4031('should reject ambiguous: ', v_1036)
                test_27.assert_(not cs_1038.is_valid, fn_3982)
        finally:
            test_27.soft_fail_to_hard()
class TestCase64(TestCase48):
    def test___toInsertSqlEscapesBobbyTables__2288(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_28: Test = Test()
        try:
            params_1040: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', "Robert'); DROP TABLE users;--"), _pair_4056('email', 'bobby@evil.com')))
            cs_1041: 'Changeset' = changeset(_user_table(), params_1040).cast((_csid('name'), _csid('email'))).validate_required((_csid('name'), _csid('email')))
            sql_frag_1042: 'SqlFragment' = cs_1041.to_insert_sql()
            s_1043: 'str29' = sql_frag_1042.to_string()
            t_3558: 'bool37' = s_1043.find("''") >= 0
            def fn_3981() -> 'str29':
                return _str_cat_4031('single quote must be doubled: ', s_1043)
            test_28.assert_(t_3558, fn_3981)
        finally:
            test_28.soft_fail_to_hard()
class TestCase65(TestCase48):
    def test___toInsertSqlProducesCorrectSqlForStringField__2289(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_29: Test = Test()
        try:
            params_1045: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('email', 'a@example.com')))
            cs_1046: 'Changeset' = changeset(_user_table(), params_1045).cast((_csid('name'), _csid('email'))).validate_required((_csid('name'), _csid('email')))
            sql_frag_1047: 'SqlFragment' = cs_1046.to_insert_sql()
            s_1048: 'str29' = sql_frag_1047.to_string()
            t_3552: 'bool37' = s_1048.find('INSERT INTO users') >= 0
            def fn_3980() -> 'str29':
                return _str_cat_4031('has INSERT INTO: ', s_1048)
            test_29.assert_(t_3552, fn_3980)
            t_3554: 'bool37' = s_1048.find("'Alice'") >= 0
            def fn_3979() -> 'str29':
                return _str_cat_4031('has quoted name: ', s_1048)
            test_29.assert_(t_3554, fn_3979)
        finally:
            test_29.soft_fail_to_hard()
class TestCase66(TestCase48):
    def test___toInsertSqlProducesCorrectSqlForIntField__2290(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_30: Test = Test()
        try:
            params_1050: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Bob'), _pair_4056('email', 'b@example.com'), _pair_4056('age', '25')))
            cs_1051: 'Changeset' = changeset(_user_table(), params_1050).cast((_csid('name'), _csid('email'), _csid('age'))).validate_required((_csid('name'), _csid('email')))
            sql_frag_1052: 'SqlFragment' = cs_1051.to_insert_sql()
            s_1053: 'str29' = sql_frag_1052.to_string()
            t_3547: 'bool37' = s_1053.find('25') >= 0
            def fn_3978() -> 'str29':
                return _str_cat_4031('age rendered unquoted: ', s_1053)
            test_30.assert_(t_3547, fn_3978)
        finally:
            test_30.soft_fail_to_hard()
class TestCase67(TestCase48):
    def test___toInsertSqlBubblesOnInvalidChangeset__2291(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_31: Test = Test()
        try:
            params_1055: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1056: 'Changeset' = changeset(_user_table(), params_1055).cast((_csid('name'),)).validate_required((_csid('name'),))
            did_bubble_1057: 'bool37'
            try:
                cs_1056.to_insert_sql()
                did_bubble_1057 = False
            except Exception41:
                did_bubble_1057 = True
            def fn_3977() -> 'str29':
                return 'invalid changeset should bubble'
            test_31.assert_(did_bubble_1057, fn_3977)
        finally:
            test_31.soft_fail_to_hard()
class TestCase68(TestCase48):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__2292(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_32: Test = Test()
        try:
            strict_table_1059: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False), FieldDef(_csid('body'), StringField(), True, None, False)), None)
            params_1060: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('body', 'hello'),))
            cs_1061: 'Changeset' = changeset(strict_table_1059, params_1060).cast((_csid('body'),))
            def fn_3976() -> 'str29':
                return 'changeset should appear valid (no explicit validation run)'
            test_32.assert_(cs_1061.is_valid, fn_3976)
            did_bubble_1062: 'bool37'
            try:
                cs_1061.to_insert_sql()
                did_bubble_1062 = False
            except Exception41:
                did_bubble_1062 = True
            def fn_3975() -> 'str29':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_32.assert_(did_bubble_1062, fn_3975)
        finally:
            test_32.soft_fail_to_hard()
class TestCase69(TestCase48):
    def test___toUpdateSqlProducesCorrectSql__2293(self) -> None:
        'toUpdateSql produces correct SQL'
        test_33: Test = Test()
        try:
            params_1064: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Bob'),))
            cs_1065: 'Changeset' = changeset(_user_table(), params_1064).cast((_csid('name'),)).validate_required((_csid('name'),))
            sql_frag_1066: 'SqlFragment' = cs_1065.to_update_sql(42)
            s_1067: 'str29' = sql_frag_1066.to_string()
            def fn_3974() -> 'str29':
                return _str_cat_4031('got: ', s_1067)
            test_33.assert_(s_1067 == "UPDATE users SET name = 'Bob' WHERE id = 42", fn_3974)
        finally:
            test_33.soft_fail_to_hard()
class TestCase70(TestCase48):
    def test___toUpdateSqlBubblesOnInvalidChangeset__2294(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_34: Test = Test()
        try:
            params_1069: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1070: 'Changeset' = changeset(_user_table(), params_1069).cast((_csid('name'),)).validate_required((_csid('name'),))
            did_bubble_1071: 'bool37'
            try:
                cs_1070.to_update_sql(1)
                did_bubble_1071 = False
            except Exception41:
                did_bubble_1071 = True
            def fn_3973() -> 'str29':
                return 'invalid changeset should bubble'
            test_34.assert_(did_bubble_1071, fn_3973)
        finally:
            test_34.soft_fail_to_hard()
class TestCase71(TestCase48):
    def test___putChangeAddsANewField__2295(self) -> None:
        'putChange adds a new field'
        test_35: Test = Test()
        try:
            params_1073: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1074: 'Changeset' = changeset(_user_table(), params_1073).cast((_csid('name'),)).put_change(_csid('email'), 'alice@example.com')
            def fn_3972() -> 'str29':
                return 'email should be in changes'
            test_35.assert_(_mapped_has_4029(cs_1074.changes, 'email'), fn_3972)
            def fn_3971() -> 'str29':
                return 'email value'
            test_35.assert_(cs_1074.changes.get('email', '') == 'alice@example.com', fn_3971)
        finally:
            test_35.soft_fail_to_hard()
class TestCase72(TestCase48):
    def test___putChangeOverwritesExistingField__2296(self) -> None:
        'putChange overwrites existing field'
        test_36: Test = Test()
        try:
            params_1076: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1077: 'Changeset' = changeset(_user_table(), params_1076).cast((_csid('name'),)).put_change(_csid('name'), 'Bob')
            def fn_3970() -> 'str29':
                return 'name should be overwritten'
            test_36.assert_(cs_1077.changes.get('name', '') == 'Bob', fn_3970)
        finally:
            test_36.soft_fail_to_hard()
class TestCase73(TestCase48):
    def test___putChangeValueAppearsInToInsertSql__2297(self) -> None:
        'putChange value appears in toInsertSql'
        test_37: Test = Test()
        try:
            params_1079: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('email', 'a@example.com')))
            cs_1080: 'Changeset' = changeset(_user_table(), params_1079).cast((_csid('name'), _csid('email'))).put_change(_csid('name'), 'Bob')
            t_3538: 'SqlFragment' = cs_1080.to_insert_sql()
            s_1081: 'str29' = t_3538.to_string()
            t_3539: 'bool37' = s_1081.find("'Bob'") >= 0
            def fn_3969() -> 'str29':
                return _str_cat_4031('should use putChange value: ', s_1081)
            test_37.assert_(t_3539, fn_3969)
        finally:
            test_37.soft_fail_to_hard()
class TestCase74(TestCase48):
    def test___getChangeReturnsValueForExistingField__2298(self) -> None:
        'getChange returns value for existing field'
        test_38: Test = Test()
        try:
            params_1083: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1084: 'Changeset' = changeset(_user_table(), params_1083).cast((_csid('name'),))
            val_1085: 'str29' = cs_1084.get_change(_csid('name'))
            def fn_3968() -> 'str29':
                return 'should return Alice'
            test_38.assert_(val_1085 == 'Alice', fn_3968)
        finally:
            test_38.soft_fail_to_hard()
class TestCase75(TestCase48):
    def test___getChangeBubblesOnMissingField__2299(self) -> None:
        'getChange bubbles on missing field'
        test_39: Test = Test()
        try:
            params_1087: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1088: 'Changeset' = changeset(_user_table(), params_1087).cast((_csid('name'),))
            did_bubble_1089: 'bool37'
            try:
                cs_1088.get_change(_csid('email'))
                did_bubble_1089 = False
            except Exception41:
                did_bubble_1089 = True
            def fn_3967() -> 'str29':
                return 'should bubble for missing field'
            test_39.assert_(did_bubble_1089, fn_3967)
        finally:
            test_39.soft_fail_to_hard()
class TestCase76(TestCase48):
    def test___deleteChangeRemovesField__2300(self) -> None:
        'deleteChange removes field'
        test_40: Test = Test()
        try:
            params_1091: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('email', 'a@example.com')))
            cs_1092: 'Changeset' = changeset(_user_table(), params_1091).cast((_csid('name'), _csid('email'))).delete_change(_csid('email'))
            def fn_3966() -> 'str29':
                return 'email should be removed'
            test_40.assert_(not _mapped_has_4029(cs_1092.changes, 'email'), fn_3966)
            def fn_3965() -> 'str29':
                return 'name should remain'
            test_40.assert_(_mapped_has_4029(cs_1092.changes, 'name'), fn_3965)
        finally:
            test_40.soft_fail_to_hard()
class TestCase77(TestCase48):
    def test___deleteChangeOnNonexistentFieldIsNoOp__2301(self) -> None:
        'deleteChange on nonexistent field is no-op'
        test_41: Test = Test()
        try:
            params_1094: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1095: 'Changeset' = changeset(_user_table(), params_1094).cast((_csid('name'),)).delete_change(_csid('email'))
            def fn_3964() -> 'str29':
                return 'name should still be present'
            test_41.assert_(_mapped_has_4029(cs_1095.changes, 'name'), fn_3964)
            def fn_3963() -> 'str29':
                return 'should still be valid'
            test_41.assert_(cs_1095.is_valid, fn_3963)
        finally:
            test_41.soft_fail_to_hard()
class TestCase78(TestCase48):
    def test___validateInclusionPassesWhenValueInList__2302(self) -> None:
        'validateInclusion passes when value in list'
        test_42: Test = Test()
        try:
            params_1097: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'admin'),))
            cs_1098: 'Changeset' = changeset(_user_table(), params_1097).cast((_csid('name'),)).validate_inclusion(_csid('name'), ('admin', 'user', 'guest'))
            def fn_3962() -> 'str29':
                return 'should be valid'
            test_42.assert_(cs_1098.is_valid, fn_3962)
        finally:
            test_42.soft_fail_to_hard()
class TestCase79(TestCase48):
    def test___validateInclusionFailsWhenValueNotInList__2303(self) -> None:
        'validateInclusion fails when value not in list'
        test_43: Test = Test()
        try:
            params_1100: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'hacker'),))
            cs_1101: 'Changeset' = changeset(_user_table(), params_1100).cast((_csid('name'),)).validate_inclusion(_csid('name'), ('admin', 'user', 'guest'))
            def fn_3961() -> 'str29':
                return 'should be invalid'
            test_43.assert_(not cs_1101.is_valid, fn_3961)
            def fn_3960() -> 'str29':
                return 'error on name'
            test_43.assert_(_list_get_4023(cs_1101.errors, 0).field == 'name', fn_3960)
        finally:
            test_43.soft_fail_to_hard()
class TestCase80(TestCase48):
    def test___validateInclusionSkipsWhenFieldNotInChanges__2304(self) -> None:
        'validateInclusion skips when field not in changes'
        test_44: Test = Test()
        try:
            params_1103: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1104: 'Changeset' = changeset(_user_table(), params_1103).cast((_csid('name'),)).validate_inclusion(_csid('name'), ('admin', 'user'))
            def fn_3959() -> 'str29':
                return 'should be valid when field absent'
            test_44.assert_(cs_1104.is_valid, fn_3959)
        finally:
            test_44.soft_fail_to_hard()
class TestCase81(TestCase48):
    def test___validateExclusionPassesWhenValueNotInList__2305(self) -> None:
        'validateExclusion passes when value not in list'
        test_45: Test = Test()
        try:
            params_1106: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1107: 'Changeset' = changeset(_user_table(), params_1106).cast((_csid('name'),)).validate_exclusion(_csid('name'), ('root', 'admin', 'superuser'))
            def fn_3958() -> 'str29':
                return 'should be valid'
            test_45.assert_(cs_1107.is_valid, fn_3958)
        finally:
            test_45.soft_fail_to_hard()
class TestCase82(TestCase48):
    def test___validateExclusionFailsWhenValueInList__2306(self) -> None:
        'validateExclusion fails when value in list'
        test_46: Test = Test()
        try:
            params_1109: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'admin'),))
            cs_1110: 'Changeset' = changeset(_user_table(), params_1109).cast((_csid('name'),)).validate_exclusion(_csid('name'), ('root', 'admin', 'superuser'))
            def fn_3957() -> 'str29':
                return 'should be invalid'
            test_46.assert_(not cs_1110.is_valid, fn_3957)
            def fn_3956() -> 'str29':
                return 'error on name'
            test_46.assert_(_list_get_4023(cs_1110.errors, 0).field == 'name', fn_3956)
        finally:
            test_46.soft_fail_to_hard()
class TestCase83(TestCase48):
    def test___validateExclusionSkipsWhenFieldNotInChanges__2307(self) -> None:
        'validateExclusion skips when field not in changes'
        test_47: Test = Test()
        try:
            params_1112: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1113: 'Changeset' = changeset(_user_table(), params_1112).cast((_csid('name'),)).validate_exclusion(_csid('name'), ('root', 'admin'))
            def fn_3955() -> 'str29':
                return 'should be valid when field absent'
            test_47.assert_(cs_1113.is_valid, fn_3955)
        finally:
            test_47.soft_fail_to_hard()
class TestCase84(TestCase48):
    def test___validateNumberGreaterThanPasses__2308(self) -> None:
        'validateNumber greaterThan passes'
        test_48: Test = Test()
        try:
            params_1115: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '25'),))
            cs_1116: 'Changeset' = changeset(_user_table(), params_1115).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(18.0, None, None, None, None))
            def fn_3954() -> 'str29':
                return '25 > 18 should pass'
            test_48.assert_(cs_1116.is_valid, fn_3954)
        finally:
            test_48.soft_fail_to_hard()
class TestCase85(TestCase48):
    def test___validateNumberGreaterThanFails__2309(self) -> None:
        'validateNumber greaterThan fails'
        test_49: Test = Test()
        try:
            params_1118: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '15'),))
            cs_1119: 'Changeset' = changeset(_user_table(), params_1118).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(18.0, None, None, None, None))
            def fn_3953() -> 'str29':
                return '15 > 18 should fail'
            test_49.assert_(not cs_1119.is_valid, fn_3953)
        finally:
            test_49.soft_fail_to_hard()
class TestCase86(TestCase48):
    def test___validateNumberLessThanPasses__2310(self) -> None:
        'validateNumber lessThan passes'
        test_50: Test = Test()
        try:
            params_1121: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '8.5'),))
            cs_1122: 'Changeset' = changeset(_user_table(), params_1121).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, 10.0, None, None, None))
            def fn_3952() -> 'str29':
                return '8.5 < 10 should pass'
            test_50.assert_(cs_1122.is_valid, fn_3952)
        finally:
            test_50.soft_fail_to_hard()
class TestCase87(TestCase48):
    def test___validateNumberLessThanFails__2311(self) -> None:
        'validateNumber lessThan fails'
        test_51: Test = Test()
        try:
            params_1124: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '12.0'),))
            cs_1125: 'Changeset' = changeset(_user_table(), params_1124).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, 10.0, None, None, None))
            def fn_3951() -> 'str29':
                return '12 < 10 should fail'
            test_51.assert_(not cs_1125.is_valid, fn_3951)
        finally:
            test_51.soft_fail_to_hard()
class TestCase88(TestCase48):
    def test___validateNumberGreaterThanOrEqualBoundary__2312(self) -> None:
        'validateNumber greaterThanOrEqual boundary'
        test_52: Test = Test()
        try:
            params_1127: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '18'),))
            cs_1128: 'Changeset' = changeset(_user_table(), params_1127).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(None, None, 18.0, None, None))
            def fn_3950() -> 'str29':
                return '18 >= 18 should pass'
            test_52.assert_(cs_1128.is_valid, fn_3950)
        finally:
            test_52.soft_fail_to_hard()
class TestCase89(TestCase48):
    def test___validateNumberCombinedOptions__2313(self) -> None:
        'validateNumber combined options'
        test_53: Test = Test()
        try:
            params_1130: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '5.0'),))
            cs_1131: 'Changeset' = changeset(_user_table(), params_1130).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(0.0, 10.0, None, None, None))
            def fn_3949() -> 'str29':
                return '5 > 0 and < 10 should pass'
            test_53.assert_(cs_1131.is_valid, fn_3949)
        finally:
            test_53.soft_fail_to_hard()
class TestCase90(TestCase48):
    def test___validateNumberNonNumericValue__2314(self) -> None:
        'validateNumber non-numeric value'
        test_54: Test = Test()
        try:
            params_1133: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', 'abc'),))
            cs_1134: 'Changeset' = changeset(_user_table(), params_1133).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(0.0, None, None, None, None))
            def fn_3948() -> 'str29':
                return 'non-numeric should fail'
            test_54.assert_(not cs_1134.is_valid, fn_3948)
            def fn_3947() -> 'str29':
                return 'correct error message'
            test_54.assert_(_list_get_4023(cs_1134.errors, 0).message == 'must be a number', fn_3947)
        finally:
            test_54.soft_fail_to_hard()
class TestCase91(TestCase48):
    def test___validateNumberSkipsWhenFieldNotInChanges__2315(self) -> None:
        'validateNumber skips when field not in changes'
        test_55: Test = Test()
        try:
            params_1136: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1137: 'Changeset' = changeset(_user_table(), params_1136).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(0.0, None, None, None, None))
            def fn_3946() -> 'str29':
                return 'should be valid when field absent'
            test_55.assert_(cs_1137.is_valid, fn_3946)
        finally:
            test_55.soft_fail_to_hard()
class TestCase92(TestCase48):
    def test___validateAcceptancePassesForTrueValues__2316(self) -> None:
        'validateAcceptance passes for true values'
        test_56: Test = Test()
        try:
            this_3671: 'Sequence33[str29]' = ('true', '1', 'yes', 'on')
            n_3673: 'int35' = _len_4022(this_3671)
            i_3674: 'int35' = 0
            while i_3674 < n_3673:
                el_3675: 'str29' = _list_get_4023(this_3671, i_3674)
                i_3674 = _int_add_4024(i_3674, 1)
                v_1139: 'str29' = el_3675
                params_1140: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('active', v_1139),))
                cs_1141: 'Changeset' = changeset(_user_table(), params_1140).cast((_csid('active'),)).validate_acceptance(_csid('active'))
                def fn_3945() -> 'str29':
                    return _str_cat_4031('should accept: ', v_1139)
                test_56.assert_(cs_1141.is_valid, fn_3945)
        finally:
            test_56.soft_fail_to_hard()
class TestCase93(TestCase48):
    def test___validateAcceptanceFailsForNonTrueValues__2317(self) -> None:
        'validateAcceptance fails for non-true values'
        test_57: Test = Test()
        try:
            params_1143: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('active', 'false'),))
            cs_1144: 'Changeset' = changeset(_user_table(), params_1143).cast((_csid('active'),)).validate_acceptance(_csid('active'))
            def fn_3944() -> 'str29':
                return 'false should not be accepted'
            test_57.assert_(not cs_1144.is_valid, fn_3944)
            def fn_3943() -> 'str29':
                return 'correct message'
            test_57.assert_(_list_get_4023(cs_1144.errors, 0).message == 'must be accepted', fn_3943)
        finally:
            test_57.soft_fail_to_hard()
class TestCase94(TestCase48):
    def test___validateConfirmationPassesWhenFieldsMatch__2318(self) -> None:
        'validateConfirmation passes when fields match'
        test_58: Test = Test()
        try:
            tbl_1146: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('password'), StringField(), False, None, False), FieldDef(_csid('password_confirmation'), StringField(), True, None, False)), None)
            params_1147: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('password', 'secret123'), _pair_4056('password_confirmation', 'secret123')))
            cs_1148: 'Changeset' = changeset(tbl_1146, params_1147).cast((_csid('password'), _csid('password_confirmation'))).validate_confirmation(_csid('password'), _csid('password_confirmation'))
            def fn_3942() -> 'str29':
                return 'matching fields should pass'
            test_58.assert_(cs_1148.is_valid, fn_3942)
        finally:
            test_58.soft_fail_to_hard()
class TestCase95(TestCase48):
    def test___validateConfirmationFailsWhenFieldsDiffer__2319(self) -> None:
        'validateConfirmation fails when fields differ'
        test_59: Test = Test()
        try:
            tbl_1150: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('password'), StringField(), False, None, False), FieldDef(_csid('password_confirmation'), StringField(), True, None, False)), None)
            params_1151: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('password', 'secret123'), _pair_4056('password_confirmation', 'wrong456')))
            cs_1152: 'Changeset' = changeset(tbl_1150, params_1151).cast((_csid('password'), _csid('password_confirmation'))).validate_confirmation(_csid('password'), _csid('password_confirmation'))
            def fn_3941() -> 'str29':
                return 'mismatched fields should fail'
            test_59.assert_(not cs_1152.is_valid, fn_3941)
            def fn_3940() -> 'str29':
                return 'error on confirmation field'
            test_59.assert_(_list_get_4023(cs_1152.errors, 0).field == 'password_confirmation', fn_3940)
        finally:
            test_59.soft_fail_to_hard()
class TestCase96(TestCase48):
    def test___validateConfirmationFailsWhenConfirmationMissing__2320(self) -> None:
        'validateConfirmation fails when confirmation missing'
        test_60: Test = Test()
        try:
            tbl_1154: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('password'), StringField(), False, None, False), FieldDef(_csid('password_confirmation'), StringField(), True, None, False)), None)
            params_1155: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('password', 'secret123'),))
            cs_1156: 'Changeset' = changeset(tbl_1154, params_1155).cast((_csid('password'),)).validate_confirmation(_csid('password'), _csid('password_confirmation'))
            def fn_3939() -> 'str29':
                return 'missing confirmation should fail'
            test_60.assert_(not cs_1156.is_valid, fn_3939)
        finally:
            test_60.soft_fail_to_hard()
class TestCase97(TestCase48):
    def test___validateContainsPassesWhenSubstringFound__2321(self) -> None:
        'validateContains passes when substring found'
        test_61: Test = Test()
        try:
            params_1158: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('email', 'alice@example.com'),))
            cs_1159: 'Changeset' = changeset(_user_table(), params_1158).cast((_csid('email'),)).validate_contains(_csid('email'), '@')
            def fn_3938() -> 'str29':
                return 'should pass when @ present'
            test_61.assert_(cs_1159.is_valid, fn_3938)
        finally:
            test_61.soft_fail_to_hard()
class TestCase98(TestCase48):
    def test___validateContainsFailsWhenSubstringNotFound__2322(self) -> None:
        'validateContains fails when substring not found'
        test_62: Test = Test()
        try:
            params_1161: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('email', 'alice-example.com'),))
            cs_1162: 'Changeset' = changeset(_user_table(), params_1161).cast((_csid('email'),)).validate_contains(_csid('email'), '@')
            def fn_3937() -> 'str29':
                return 'should fail when @ absent'
            test_62.assert_(not cs_1162.is_valid, fn_3937)
        finally:
            test_62.soft_fail_to_hard()
class TestCase99(TestCase48):
    def test___validateContainsSkipsWhenFieldNotInChanges__2323(self) -> None:
        'validateContains skips when field not in changes'
        test_63: Test = Test()
        try:
            params_1164: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1165: 'Changeset' = changeset(_user_table(), params_1164).cast((_csid('email'),)).validate_contains(_csid('email'), '@')
            def fn_3936() -> 'str29':
                return 'should be valid when field absent'
            test_63.assert_(cs_1165.is_valid, fn_3936)
        finally:
            test_63.soft_fail_to_hard()
class TestCase100(TestCase48):
    def test___validateStartsWithPasses__2324(self) -> None:
        'validateStartsWith passes'
        test_64: Test = Test()
        try:
            params_1167: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Dr. Smith'),))
            cs_1168: 'Changeset' = changeset(_user_table(), params_1167).cast((_csid('name'),)).validate_starts_with(_csid('name'), 'Dr.')
            def fn_3935() -> 'str29':
                return 'should pass for Dr. prefix'
            test_64.assert_(cs_1168.is_valid, fn_3935)
        finally:
            test_64.soft_fail_to_hard()
class TestCase101(TestCase48):
    def test___validateStartsWithFails__2325(self) -> None:
        'validateStartsWith fails'
        test_65: Test = Test()
        try:
            params_1170: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Mr. Smith'),))
            cs_1171: 'Changeset' = changeset(_user_table(), params_1170).cast((_csid('name'),)).validate_starts_with(_csid('name'), 'Dr.')
            def fn_3934() -> 'str29':
                return 'should fail for Mr. prefix'
            test_65.assert_(not cs_1171.is_valid, fn_3934)
        finally:
            test_65.soft_fail_to_hard()
class TestCase102(TestCase48):
    def test___validateEndsWithPasses__2326(self) -> None:
        'validateEndsWith passes'
        test_66: Test = Test()
        try:
            params_1173: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('email', 'alice@example.com'),))
            cs_1174: 'Changeset' = changeset(_user_table(), params_1173).cast((_csid('email'),)).validate_ends_with(_csid('email'), '.com')
            def fn_3933() -> 'str29':
                return 'should pass for .com suffix'
            test_66.assert_(cs_1174.is_valid, fn_3933)
        finally:
            test_66.soft_fail_to_hard()
class TestCase103(TestCase48):
    def test___validateEndsWithFails__2327(self) -> None:
        'validateEndsWith fails'
        test_67: Test = Test()
        try:
            params_1176: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('email', 'alice@example.org'),))
            cs_1177: 'Changeset' = changeset(_user_table(), params_1176).cast((_csid('email'),)).validate_ends_with(_csid('email'), '.com')
            def fn_3932() -> 'str29':
                return 'should fail for .org when expecting .com'
            test_67.assert_(not cs_1177.is_valid, fn_3932)
        finally:
            test_67.soft_fail_to_hard()
class TestCase104(TestCase48):
    def test___validateEndsWithHandlesRepeatedSuffixCorrectly__2328(self) -> None:
        'validateEndsWith handles repeated suffix correctly'
        test_68: Test = Test()
        try:
            params_1179: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'abcabc'),))
            cs_1180: 'Changeset' = changeset(_user_table(), params_1179).cast((_csid('name'),)).validate_ends_with(_csid('name'), 'abc')
            def fn_3931() -> 'str29':
                return 'abcabc should end with abc'
            test_68.assert_(cs_1180.is_valid, fn_3931)
        finally:
            test_68.soft_fail_to_hard()
class TestCase105(TestCase48):
    def test___toInsertSqlUsesDefaultValueWhenFieldNotInChanges__2329(self) -> None:
        'toInsertSql uses default value when field not in changes'
        test_69: Test = Test()
        try:
            tbl_1182: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False), FieldDef(_csid('status'), StringField(), False, SqlDefault(), False)), None)
            params_1183: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('title', 'Hello'),))
            cs_1184: 'Changeset' = changeset(tbl_1182, params_1183).cast((_csid('title'),))
            t_3528: 'SqlFragment' = cs_1184.to_insert_sql()
            s_1185: 'str29' = t_3528.to_string()
            t_3529: 'bool37' = s_1185.find('INSERT INTO posts') >= 0
            def fn_3930() -> 'str29':
                return _str_cat_4031('has INSERT INTO: ', s_1185)
            test_69.assert_(t_3529, fn_3930)
            t_3531: 'bool37' = s_1185.find("'Hello'") >= 0
            def fn_3929() -> 'str29':
                return _str_cat_4031('has title value: ', s_1185)
            test_69.assert_(t_3531, fn_3929)
            t_3533: 'bool37' = s_1185.find('DEFAULT') >= 0
            def fn_3928() -> 'str29':
                return _str_cat_4031('status should use DEFAULT: ', s_1185)
            test_69.assert_(t_3533, fn_3928)
        finally:
            test_69.soft_fail_to_hard()
class TestCase106(TestCase48):
    def test___toInsertSqlChangeOverridesDefaultValue__2330(self) -> None:
        'toInsertSql change overrides default value'
        test_70: Test = Test()
        try:
            tbl_1187: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False), FieldDef(_csid('status'), StringField(), False, SqlDefault(), False)), None)
            params_1188: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('title', 'Hello'), _pair_4056('status', 'published')))
            cs_1189: 'Changeset' = changeset(tbl_1187, params_1188).cast((_csid('title'), _csid('status')))
            t_3522: 'SqlFragment' = cs_1189.to_insert_sql()
            s_1190: 'str29' = t_3522.to_string()
            t_3523: 'bool37' = s_1190.find("'published'") >= 0
            def fn_3927() -> 'str29':
                return _str_cat_4031('should use provided value: ', s_1190)
            test_70.assert_(t_3523, fn_3927)
        finally:
            test_70.soft_fail_to_hard()
class TestCase107(TestCase48):
    def test___toInsertSqlWithTimestampsUsesDefault__2331(self) -> None:
        'toInsertSql with timestamps uses DEFAULT'
        test_71: Test = Test()
        try:
            ts_1192: 'Sequence33[FieldDef]' = timestamps()
            fields_1193: 'MutableSequence38[FieldDef]' = _list_4018()
            fields_1193.append(FieldDef(_csid('title'), StringField(), False, None, False))
            this_3676: 'Sequence33[FieldDef]' = ts_1192
            n_3678: 'int35' = _len_4022(this_3676)
            i_3679: 'int35' = 0
            while i_3679 < n_3678:
                el_3680: 'FieldDef' = _list_get_4023(this_3676, i_3679)
                i_3679 = _int_add_4024(i_3679, 1)
                t_1194: 'FieldDef' = el_3680
                fields_1193.append(t_1194)
            tbl_1195: 'TableDef' = TableDef(_csid('articles'), _tuple_4020(fields_1193), None)
            params_1196: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('title', 'News'),))
            cs_1197: 'Changeset' = changeset(tbl_1195, params_1196).cast((_csid('title'),))
            t_3514: 'SqlFragment' = cs_1197.to_insert_sql()
            s_1198: 'str29' = t_3514.to_string()
            t_3515: 'bool37' = s_1198.find('inserted_at') >= 0
            def fn_3926() -> 'str29':
                return _str_cat_4031('should include inserted_at: ', s_1198)
            test_71.assert_(t_3515, fn_3926)
            t_3517: 'bool37' = s_1198.find('updated_at') >= 0
            def fn_3925() -> 'str29':
                return _str_cat_4031('should include updated_at: ', s_1198)
            test_71.assert_(t_3517, fn_3925)
            t_3519: 'bool37' = s_1198.find('DEFAULT') >= 0
            def fn_3924() -> 'str29':
                return _str_cat_4031('timestamps should use DEFAULT: ', s_1198)
            test_71.assert_(t_3519, fn_3924)
        finally:
            test_71.soft_fail_to_hard()
class TestCase108(TestCase48):
    def test___toInsertSqlSkipsVirtualFields__2332(self) -> None:
        'toInsertSql skips virtual fields'
        test_72: Test = Test()
        try:
            tbl_1200: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('full_name'), StringField(), True, None, True)), None)
            params_1201: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('full_name', 'Alice Smith')))
            cs_1202: 'Changeset' = changeset(tbl_1200, params_1201).cast((_csid('name'), _csid('full_name')))
            t_3505: 'SqlFragment' = cs_1202.to_insert_sql()
            s_1203: 'str29' = t_3505.to_string()
            t_3506: 'bool37' = s_1203.find("'Alice'") >= 0
            def fn_3923() -> 'str29':
                return _str_cat_4031('name should be included: ', s_1203)
            test_72.assert_(t_3506, fn_3923)
            t_3508: 'bool37' = s_1203.find('full_name') >= 0
            def fn_3922() -> 'str29':
                return _str_cat_4031('virtual field should be excluded: ', s_1203)
            test_72.assert_(not t_3508, fn_3922)
        finally:
            test_72.soft_fail_to_hard()
class TestCase109(TestCase48):
    def test___toInsertSqlAllowsMissingNonNullableVirtualField__2333(self) -> None:
        'toInsertSql allows missing non-nullable virtual field'
        test_73: Test = Test()
        try:
            tbl_1205: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('computed'), StringField(), False, None, True)), None)
            params_1206: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'),))
            cs_1207: 'Changeset' = changeset(tbl_1205, params_1206).cast((_csid('name'),))
            t_3500: 'SqlFragment' = cs_1207.to_insert_sql()
            s_1208: 'str29' = t_3500.to_string()
            t_3501: 'bool37' = s_1208.find("'Alice'") >= 0
            def fn_3921() -> 'str29':
                return _str_cat_4031('should succeed: ', s_1208)
            test_73.assert_(t_3501, fn_3921)
        finally:
            test_73.soft_fail_to_hard()
class TestCase110(TestCase48):
    def test___toUpdateSqlSkipsVirtualFields__2334(self) -> None:
        'toUpdateSql skips virtual fields'
        test_74: Test = Test()
        try:
            tbl_1210: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('display'), StringField(), True, None, True)), None)
            params_1211: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Bob'), _pair_4056('display', 'Bobby')))
            cs_1212: 'Changeset' = changeset(tbl_1210, params_1211).cast((_csid('name'), _csid('display')))
            t_3494: 'SqlFragment' = cs_1212.to_update_sql(1)
            s_1213: 'str29' = t_3494.to_string()
            t_3495: 'bool37' = s_1213.find("name = 'Bob'") >= 0
            def fn_3920() -> 'str29':
                return _str_cat_4031('name should be in SET: ', s_1213)
            test_74.assert_(t_3495, fn_3920)
            t_3497: 'bool37' = s_1213.find('display') >= 0
            def fn_3919() -> 'str29':
                return _str_cat_4031('virtual field excluded from UPDATE: ', s_1213)
            test_74.assert_(not t_3497, fn_3919)
        finally:
            test_74.soft_fail_to_hard()
class TestCase111(TestCase48):
    def test___toUpdateSqlUsesCustomPrimaryKey__2335(self) -> None:
        'toUpdateSql uses custom primary key'
        test_75: Test = Test()
        try:
            tbl_1215: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False),), _csid('post_id'))
            params_1216: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('title', 'Updated'),))
            cs_1217: 'Changeset' = changeset(tbl_1215, params_1216).cast((_csid('title'),))
            t_3491: 'SqlFragment' = cs_1217.to_update_sql(99)
            s_1218: 'str29' = t_3491.to_string()
            def fn_3918() -> 'str29':
                return _str_cat_4031('got: ', s_1218)
            test_75.assert_(s_1218 == "UPDATE posts SET title = 'Updated' WHERE post_id = 99", fn_3918)
        finally:
            test_75.soft_fail_to_hard()
class TestCase112(TestCase48):
    def test___deleteSqlUsesCustomPrimaryKey__2336(self) -> None:
        'deleteSql uses custom primary key'
        test_76: Test = Test()
        try:
            tbl_1220: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False),), _csid('post_id'))
            s_1221: 'str29' = delete_sql(tbl_1220, 42).to_string()
            def fn_3917() -> 'str29':
                return _str_cat_4031('got: ', s_1221)
            test_76.assert_(s_1221 == 'DELETE FROM posts WHERE post_id = 42', fn_3917)
        finally:
            test_76.soft_fail_to_hard()
class TestCase113(TestCase48):
    def test___deleteSqlUsesDefaultIdWhenPrimaryKeyNull__2337(self) -> None:
        'deleteSql uses default id when primaryKey null'
        test_77: Test = Test()
        try:
            tbl_1223: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False),), None)
            s_1224: 'str29' = delete_sql(tbl_1223, 7).to_string()
            def fn_3916() -> 'str29':
                return _str_cat_4031('got: ', s_1224)
            test_77.assert_(s_1224 == 'DELETE FROM users WHERE id = 7', fn_3916)
        finally:
            test_77.soft_fail_to_hard()
class TestCase114(TestCase48):
    def test___alreadyInvalidChangesetSkipsSubsequentValidators__2338(self) -> None:
        'already-invalid changeset skips subsequent validators'
        test_78: Test = Test()
        try:
            params_1226: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'A'), _pair_4056('email', 'alice@example.com')))
            cs_1227: 'Changeset' = changeset(_user_table(), params_1226).cast((_csid('name'), _csid('email'))).validate_length(_csid('name'), 3, 50).validate_required((_csid('name'), _csid('email'))).validate_contains(_csid('email'), '@')
            def fn_3915() -> 'str29':
                return 'should be invalid from validateLength'
            test_78.assert_(not cs_1227.is_valid, fn_3915)
            def fn_3914() -> 'str29':
                return _str_cat_4031('should have exactly 1 error, not accumulate: ', _int_to_string_4032(_len_4022(cs_1227.errors)))
            test_78.assert_(_len_4022(cs_1227.errors) == 1, fn_3914)
            def fn_3913() -> 'str29':
                return 'error should be on name'
            test_78.assert_(_list_get_4023(cs_1227.errors, 0).field == 'name', fn_3913)
        finally:
            test_78.soft_fail_to_hard()
class TestCase115(TestCase48):
    def test___validateNumberLessThanOrEqualPassesAtBoundary__2339(self) -> None:
        'validateNumber lessThanOrEqual passes at boundary'
        test_79: Test = Test()
        try:
            params_1229: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '10.0'),))
            cs_1230: 'Changeset' = changeset(_user_table(), params_1229).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, 10.0, None))
            def fn_3912() -> 'str29':
                return '10.0 <= 10.0 should pass'
            test_79.assert_(cs_1230.is_valid, fn_3912)
        finally:
            test_79.soft_fail_to_hard()
class TestCase116(TestCase48):
    def test___validateNumberLessThanOrEqualFailsAboveBoundary__2340(self) -> None:
        'validateNumber lessThanOrEqual fails above boundary'
        test_80: Test = Test()
        try:
            params_1232: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '10.1'),))
            cs_1233: 'Changeset' = changeset(_user_table(), params_1232).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, 10.0, None))
            def fn_3911() -> 'str29':
                return '10.1 <= 10.0 should fail'
            test_80.assert_(not cs_1233.is_valid, fn_3911)
            def fn_3910() -> 'str29':
                return 'correct message'
            test_80.assert_(_list_get_4023(cs_1233.errors, 0).message == 'must be less than or equal to 10.0', fn_3910)
        finally:
            test_80.soft_fail_to_hard()
class TestCase117(TestCase48):
    def test___validateNumberEqualToPassesWhenEqual__2341(self) -> None:
        'validateNumber equalTo passes when equal'
        test_81: Test = Test()
        try:
            params_1235: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '42.0'),))
            cs_1236: 'Changeset' = changeset(_user_table(), params_1235).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, None, 42.0))
            def fn_3909() -> 'str29':
                return '42.0 == 42.0 should pass'
            test_81.assert_(cs_1236.is_valid, fn_3909)
        finally:
            test_81.soft_fail_to_hard()
class TestCase118(TestCase48):
    def test___validateNumberEqualToFailsWhenNotEqual__2342(self) -> None:
        'validateNumber equalTo fails when not equal'
        test_82: Test = Test()
        try:
            params_1238: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '41.9'),))
            cs_1239: 'Changeset' = changeset(_user_table(), params_1238).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, None, 42.0))
            def fn_3908() -> 'str29':
                return '41.9 == 42.0 should fail'
            test_82.assert_(not cs_1239.is_valid, fn_3908)
            def fn_3907() -> 'str29':
                return 'correct message'
            test_82.assert_(_list_get_4023(cs_1239.errors, 0).message == 'must be equal to 42.0', fn_3907)
        finally:
            test_82.soft_fail_to_hard()
class TestCase119(TestCase48):
    def test___validateNumberGreaterThanFailsAtExactThreshold__2343(self) -> None:
        'validateNumber greaterThan fails at exact threshold'
        test_83: Test = Test()
        try:
            params_1241: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '18'),))
            cs_1242: 'Changeset' = changeset(_user_table(), params_1241).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(18.0, None, None, None, None))
            def fn_3906() -> 'str29':
                return '18 > 18 should fail (strict greater than)'
            test_83.assert_(not cs_1242.is_valid, fn_3906)
        finally:
            test_83.soft_fail_to_hard()
class TestCase120(TestCase48):
    def test___validateNumberLessThanFailsAtExactThreshold__2344(self) -> None:
        'validateNumber lessThan fails at exact threshold'
        test_84: Test = Test()
        try:
            params_1244: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', '10.0'),))
            cs_1245: 'Changeset' = changeset(_user_table(), params_1244).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, 10.0, None, None, None))
            def fn_3905() -> 'str29':
                return '10.0 < 10.0 should fail (strict less than)'
            test_84.assert_(not cs_1245.is_valid, fn_3905)
        finally:
            test_84.soft_fail_to_hard()
class TestCase121(TestCase48):
    def test___validateFloatFailsForNonFloatString__2345(self) -> None:
        'validateFloat fails for non-float string'
        test_85: Test = Test()
        try:
            params_1247: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('score', 'abc'),))
            cs_1248: 'Changeset' = changeset(_user_table(), params_1247).cast((_csid('score'),)).validate_float(_csid('score'))
            def fn_3904() -> 'str29':
                return 'abc should not parse as float'
            test_85.assert_(not cs_1248.is_valid, fn_3904)
            def fn_3903() -> 'str29':
                return 'correct message'
            test_85.assert_(_list_get_4023(cs_1248.errors, 0).message == 'must be a number', fn_3903)
        finally:
            test_85.soft_fail_to_hard()
class TestCase122(TestCase48):
    def test___toInsertSqlWithAllSixFieldTypes__2346(self) -> None:
        'toInsertSql with all six field types'
        test_86: Test = Test()
        try:
            tbl_1250: 'TableDef' = TableDef(_csid('records'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('count'), IntField(), False, None, False), FieldDef(_csid('big_id'), Int64Field(), False, None, False), FieldDef(_csid('rating'), FloatField(), False, None, False), FieldDef(_csid('active'), BoolField(), False, None, False), FieldDef(_csid('birthday'), DateField(), False, None, False)), None)
            params_1251: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('count', '42'), _pair_4056('big_id', '9999999999'), _pair_4056('rating', '3.14'), _pair_4056('active', 'true'), _pair_4056('birthday', '2000-01-15')))
            cs_1252: 'Changeset' = changeset(tbl_1250, params_1251).cast((_csid('name'), _csid('count'), _csid('big_id'), _csid('rating'), _csid('active'), _csid('birthday')))
            t_3478: 'SqlFragment' = cs_1252.to_insert_sql()
            s_1253: 'str29' = t_3478.to_string()
            t_3479: 'bool37' = s_1253.find("'Alice'") >= 0
            def fn_3902() -> 'str29':
                return _str_cat_4031('string field: ', s_1253)
            test_86.assert_(t_3479, fn_3902)
            t_3481: 'bool37' = s_1253.find('42') >= 0
            def fn_3901() -> 'str29':
                return _str_cat_4031('int field: ', s_1253)
            test_86.assert_(t_3481, fn_3901)
            t_3483: 'bool37' = s_1253.find('9999999999') >= 0
            def fn_3900() -> 'str29':
                return _str_cat_4031('int64 field: ', s_1253)
            test_86.assert_(t_3483, fn_3900)
            t_3485: 'bool37' = s_1253.find('3.14') >= 0
            def fn_3899() -> 'str29':
                return _str_cat_4031('float field: ', s_1253)
            test_86.assert_(t_3485, fn_3899)
            t_3487: 'bool37' = s_1253.find('TRUE') >= 0
            def fn_3898() -> 'str29':
                return _str_cat_4031('bool field: ', s_1253)
            test_86.assert_(t_3487, fn_3898)
            t_3489: 'bool37' = s_1253.find("'2000-01-15'") >= 0
            def fn_3897() -> 'str29':
                return _str_cat_4031('date field: ', s_1253)
            test_86.assert_(t_3489, fn_3897)
        finally:
            test_86.soft_fail_to_hard()
class TestCase123(TestCase48):
    def test___deleteChangeOnNonNullableFieldCausesToInsertSqlToBubble__2347(self) -> None:
        'deleteChange on non-nullable field causes toInsertSql to bubble'
        test_87: Test = Test()
        try:
            tbl_1255: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('email'), StringField(), False, None, False)), None)
            params_1256: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('email', 'a@b.com')))
            cs_1257: 'Changeset' = changeset(tbl_1255, params_1256).cast((_csid('name'), _csid('email'))).delete_change(_csid('email'))
            did_bubble_1258: 'bool37'
            try:
                cs_1257.to_insert_sql()
                did_bubble_1258 = False
            except Exception41:
                did_bubble_1258 = True
            def fn_3896() -> 'str29':
                return 'removing non-nullable field should make toInsertSql bubble'
            test_87.assert_(did_bubble_1258, fn_3896)
        finally:
            test_87.soft_fail_to_hard()
class TestCase124(TestCase48):
    def test___validateLengthPassesAtExactMin__2348(self) -> None:
        'validateLength passes at exact min'
        test_88: Test = Test()
        try:
            params_1260: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'abc'),))
            cs_1261: 'Changeset' = changeset(_user_table(), params_1260).cast((_csid('name'),)).validate_length(_csid('name'), 3, 10)
            def fn_3895() -> 'str29':
                return 'length 3 should pass for min 3'
            test_88.assert_(cs_1261.is_valid, fn_3895)
        finally:
            test_88.soft_fail_to_hard()
class TestCase125(TestCase48):
    def test___validateLengthPassesAtExactMax__2349(self) -> None:
        'validateLength passes at exact max'
        test_89: Test = Test()
        try:
            params_1263: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'abcdefghij'),))
            cs_1264: 'Changeset' = changeset(_user_table(), params_1263).cast((_csid('name'),)).validate_length(_csid('name'), 1, 10)
            def fn_3894() -> 'str29':
                return 'length 10 should pass for max 10'
            test_89.assert_(cs_1264.is_valid, fn_3894)
        finally:
            test_89.soft_fail_to_hard()
class TestCase126(TestCase48):
    def test___validateAcceptanceSkipsWhenFieldNotInChanges__2350(self) -> None:
        'validateAcceptance skips when field not in changes'
        test_90: Test = Test()
        try:
            params_1266: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1267: 'Changeset' = changeset(_user_table(), params_1266).cast((_csid('active'),)).validate_acceptance(_csid('active'))
            def fn_3893() -> 'str29':
                return 'should be valid when field absent'
            test_90.assert_(cs_1267.is_valid, fn_3893)
        finally:
            test_90.soft_fail_to_hard()
class TestCase127(TestCase48):
    def test___multipleValidatorsChainCorrectlyOnValidChangeset__2351(self) -> None:
        'multiple validators chain correctly on valid changeset'
        test_91: Test = Test()
        try:
            params_1269: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('email', 'alice@example.com'), _pair_4056('age', '25')))
            cs_1270: 'Changeset' = changeset(_user_table(), params_1269).cast((_csid('name'), _csid('email'), _csid('age'))).validate_required((_csid('name'), _csid('email'))).validate_length(_csid('name'), 2, 50).validate_contains(_csid('email'), '@').validate_int(_csid('age')).validate_number(_csid('age'), NumberValidationOpts(0.0, 150.0, None, None, None))
            def fn_3892() -> 'str29':
                return 'all validators should pass'
            test_91.assert_(cs_1270.is_valid, fn_3892)
            def fn_3891() -> 'str29':
                return 'no errors expected'
            test_91.assert_(_len_4022(cs_1270.errors) == 0, fn_3891)
        finally:
            test_91.soft_fail_to_hard()
class TestCase128(TestCase48):
    def test___toUpdateSqlWithMultipleNonVirtualFields__2352(self) -> None:
        'toUpdateSql with multiple non-virtual fields'
        test_92: Test = Test()
        try:
            tbl_1272: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('email'), StringField(), False, None, False)), None)
            params_1273: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Bob'), _pair_4056('email', 'bob@example.com')))
            cs_1274: 'Changeset' = changeset(tbl_1272, params_1273).cast((_csid('name'), _csid('email')))
            t_3464: 'SqlFragment' = cs_1274.to_update_sql(5)
            s_1275: 'str29' = t_3464.to_string()
            t_3465: 'bool37' = s_1275.find("name = 'Bob'") >= 0
            def fn_3890() -> 'str29':
                return _str_cat_4031('name in SET: ', s_1275)
            test_92.assert_(t_3465, fn_3890)
            t_3467: 'bool37' = s_1275.find("email = 'bob@example.com'") >= 0
            def fn_3889() -> 'str29':
                return _str_cat_4031('email in SET: ', s_1275)
            test_92.assert_(t_3467, fn_3889)
            t_3469: 'bool37' = s_1275.find('WHERE id = 5') >= 0
            def fn_3888() -> 'str29':
                return _str_cat_4031('WHERE clause: ', s_1275)
            test_92.assert_(t_3469, fn_3888)
        finally:
            test_92.soft_fail_to_hard()
class TestCase129(TestCase48):
    def test___toUpdateSqlBubblesWhenAllChangesAreVirtualFields__2353(self) -> None:
        'toUpdateSql bubbles when all changes are virtual fields'
        test_93: Test = Test()
        try:
            tbl_1277: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('computed'), StringField(), True, None, True)), None)
            params_1278: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'Alice'), _pair_4056('computed', 'derived')))
            cs_1279: 'Changeset' = changeset(tbl_1277, params_1278).cast((_csid('computed'),))
            did_bubble_1280: 'bool37'
            try:
                cs_1279.to_update_sql(1)
                did_bubble_1280 = False
            except Exception41:
                did_bubble_1280 = True
            def fn_3887() -> 'str29':
                return 'should bubble when all changes are virtual'
            test_93.assert_(did_bubble_1280, fn_3887)
        finally:
            test_93.soft_fail_to_hard()
class TestCase130(TestCase48):
    def test___putChangeSatisfiesSubsequentValidateRequired__2354(self) -> None:
        'putChange satisfies subsequent validateRequired'
        test_94: Test = Test()
        try:
            params_1282: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1283: 'Changeset' = changeset(_user_table(), params_1282).cast((_csid('name'),)).put_change(_csid('name'), 'Injected').validate_required((_csid('name'),))
            def fn_3886() -> 'str29':
                return 'putChange should satisfy required'
            test_94.assert_(cs_1283.is_valid, fn_3886)
        finally:
            test_94.soft_fail_to_hard()
class TestCase131(TestCase48):
    def test___validateStartsWithSkipsWhenFieldNotInChanges__2355(self) -> None:
        'validateStartsWith skips when field not in changes'
        test_95: Test = Test()
        try:
            params_1285: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1286: 'Changeset' = changeset(_user_table(), params_1285).cast((_csid('name'),)).validate_starts_with(_csid('name'), 'Dr.')
            def fn_3885() -> 'str29':
                return 'should be valid when field absent'
            test_95.assert_(cs_1286.is_valid, fn_3885)
        finally:
            test_95.soft_fail_to_hard()
class TestCase132(TestCase48):
    def test___validateEndsWithSkipsWhenFieldNotInChanges__2356(self) -> None:
        'validateEndsWith skips when field not in changes'
        test_96: Test = Test()
        try:
            params_1288: 'MappingProxyType36[str29, str29]' = _map_constructor_4055(())
            cs_1289: 'Changeset' = changeset(_user_table(), params_1288).cast((_csid('name'),)).validate_ends_with(_csid('name'), '.com')
            def fn_3884() -> 'str29':
                return 'should be valid when field absent'
            test_96.assert_(cs_1289.is_valid, fn_3884)
        finally:
            test_96.soft_fail_to_hard()
class TestCase133(TestCase48):
    def test___validateIntAcceptsZero__2357(self) -> None:
        'validateInt accepts zero'
        test_97: Test = Test()
        try:
            params_1291: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '0'),))
            cs_1292: 'Changeset' = changeset(_user_table(), params_1291).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_3883() -> 'str29':
                return '0 should be a valid int'
            test_97.assert_(cs_1292.is_valid, fn_3883)
        finally:
            test_97.soft_fail_to_hard()
class TestCase134(TestCase48):
    def test___validateIntAcceptsNegative__2358(self) -> None:
        'validateInt accepts negative'
        test_98: Test = Test()
        try:
            params_1294: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('age', '-5'),))
            cs_1295: 'Changeset' = changeset(_user_table(), params_1294).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_3882() -> 'str29':
                return '-5 should be a valid int'
            test_98.assert_(cs_1295.is_valid, fn_3882)
        finally:
            test_98.soft_fail_to_hard()
class TestCase135(TestCase48):
    def test___changesetImmutabilityValidatorsDoNotMutateBase__2359(self) -> None:
        'changeset immutability - validators do not mutate base'
        test_99: Test = Test()
        try:
            params_1297: 'MappingProxyType36[str29, str29]' = _map_constructor_4055((_pair_4056('name', 'A'), _pair_4056('email', 'alice@example.com')))
            base_1298: 'Changeset' = changeset(_user_table(), params_1297).cast((_csid('name'), _csid('email')))
            failed_1299: 'Changeset' = base_1298.validate_length(_csid('name'), 3, 50)
            passed_1300: 'Changeset' = base_1298.validate_required((_csid('name'), _csid('email')))
            def fn_3881() -> 'str29':
                return 'failed branch should be invalid'
            test_99.assert_(not failed_1299.is_valid, fn_3881)
            def fn_3880() -> 'str29':
                return 'passed branch should still be valid'
            test_99.assert_(passed_1300.is_valid, fn_3880)
        finally:
            test_99.soft_fail_to_hard()
def _sid(name_1650: 'str29', /) -> 'SafeIdentifier':
    return safe_identifier(name_1650)
class TestCase136(TestCase48):
    def test___bareFromProducesSelect__2441(self) -> None:
        'bare from produces SELECT *'
        test_100: Test = Test()
        try:
            q_1653: 'Query' = from_(_sid('users'))
            def fn_3877() -> 'str29':
                return 'bare query'
            test_100.assert_(q_1653.to_sql().to_string() == 'SELECT * FROM users', fn_3877)
        finally:
            test_100.soft_fail_to_hard()
class TestCase137(TestCase48):
    def test___selectRestrictsColumns__2442(self) -> None:
        'select restricts columns'
        test_101: Test = Test()
        try:
            q_1655: 'Query' = from_(_sid('users')).select((_sid('id'), _sid('name')))
            def fn_3876() -> 'str29':
                return 'select columns'
            test_101.assert_(q_1655.to_sql().to_string() == 'SELECT id, name FROM users', fn_3876)
        finally:
            test_101.soft_fail_to_hard()
class TestCase138(TestCase48):
    def test___whereAddsConditionWithIntValue__2443(self) -> None:
        'where adds condition with int value'
        test_102: Test = Test()
        try:
            t_3458: 'Query' = from_(_sid('users'))
            accumulator_2444: 'SqlBuilder' = SqlBuilder()
            accumulator_2444.append_safe('age > ')
            accumulator_2444.append_int32(18)
            q_1657: 'Query' = t_3458.where(accumulator_2444.accumulated)
            def fn_3875() -> 'str29':
                return 'where int'
            test_102.assert_(q_1657.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18', fn_3875)
        finally:
            test_102.soft_fail_to_hard()
class TestCase139(TestCase48):
    def test___whereAddsConditionWithBoolValue__2445(self) -> None:
        'where adds condition with bool value'
        test_103: Test = Test()
        try:
            t_3456: 'Query' = from_(_sid('users'))
            accumulator_2446: 'SqlBuilder' = SqlBuilder()
            accumulator_2446.append_safe('active = ')
            accumulator_2446.append_boolean(True)
            q_1659: 'Query' = t_3456.where(accumulator_2446.accumulated)
            def fn_3874() -> 'str29':
                return 'where bool'
            test_103.assert_(q_1659.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE', fn_3874)
        finally:
            test_103.soft_fail_to_hard()
class TestCase140(TestCase48):
    def test___chainedWhereUsesAnd__2447(self) -> None:
        'chained where uses AND'
        test_104: Test = Test()
        try:
            t_3452: 'Query' = from_(_sid('users'))
            accumulator_2448: 'SqlBuilder' = SqlBuilder()
            accumulator_2448.append_safe('age > ')
            accumulator_2448.append_int32(18)
            t_3454: 'Query' = t_3452.where(accumulator_2448.accumulated)
            accumulator_2449: 'SqlBuilder' = SqlBuilder()
            accumulator_2449.append_safe('active = ')
            accumulator_2449.append_boolean(True)
            q_1661: 'Query' = t_3454.where(accumulator_2449.accumulated)
            def fn_3873() -> 'str29':
                return 'chained where'
            test_104.assert_(q_1661.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE', fn_3873)
        finally:
            test_104.soft_fail_to_hard()
class TestCase141(TestCase48):
    def test___orderByAsc__2450(self) -> None:
        'orderBy ASC'
        test_105: Test = Test()
        try:
            q_1663: 'Query' = from_(_sid('users')).order_by(_sid('name'), True)
            def fn_3872() -> 'str29':
                return 'order asc'
            test_105.assert_(q_1663.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC', fn_3872)
        finally:
            test_105.soft_fail_to_hard()
class TestCase142(TestCase48):
    def test___orderByDesc__2451(self) -> None:
        'orderBy DESC'
        test_106: Test = Test()
        try:
            q_1665: 'Query' = from_(_sid('users')).order_by(_sid('created_at'), False)
            def fn_3871() -> 'str29':
                return 'order desc'
            test_106.assert_(q_1665.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC', fn_3871)
        finally:
            test_106.soft_fail_to_hard()
class TestCase143(TestCase48):
    def test___limitAndOffset__2452(self) -> None:
        'limit and offset'
        test_107: Test = Test()
        try:
            t_3701: 'Query' = from_(_sid('users')).limit(10)
            q_1667: 'Query' = t_3701.offset(20)
            def fn_3870() -> 'str29':
                return 'limit/offset'
            test_107.assert_(q_1667.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20', fn_3870)
        finally:
            test_107.soft_fail_to_hard()
class TestCase144(TestCase48):
    def test___limitBubblesOnNegative__2453(self) -> None:
        'limit bubbles on negative'
        test_108: Test = Test()
        try:
            did_bubble_1669: 'bool37'
            try:
                from_(_sid('users')).limit(-1)
                did_bubble_1669 = False
            except Exception41:
                did_bubble_1669 = True
            def fn_3869() -> 'str29':
                return 'negative limit should bubble'
            test_108.assert_(did_bubble_1669, fn_3869)
        finally:
            test_108.soft_fail_to_hard()
class TestCase145(TestCase48):
    def test___offsetBubblesOnNegative__2454(self) -> None:
        'offset bubbles on negative'
        test_109: Test = Test()
        try:
            did_bubble_1671: 'bool37'
            try:
                from_(_sid('users')).offset(-1)
                did_bubble_1671 = False
            except Exception41:
                did_bubble_1671 = True
            def fn_3868() -> 'str29':
                return 'negative offset should bubble'
            test_109.assert_(did_bubble_1671, fn_3868)
        finally:
            test_109.soft_fail_to_hard()
class TestCase146(TestCase48):
    def test___complexComposedQuery__2455(self) -> None:
        'complex composed query'
        test_110: Test = Test()
        try:
            min_age_1673: 'int35' = 21
            t_3444: 'Query' = from_(_sid('users')).select((_sid('id'), _sid('name'), _sid('email')))
            accumulator_2456: 'SqlBuilder' = SqlBuilder()
            accumulator_2456.append_safe('age >= ')
            accumulator_2456.append_int32(21)
            t_3446: 'Query' = t_3444.where(accumulator_2456.accumulated)
            accumulator_2457: 'SqlBuilder' = SqlBuilder()
            accumulator_2457.append_safe('active = ')
            accumulator_2457.append_boolean(True)
            t_3700: 'Query' = t_3446.where(accumulator_2457.accumulated).order_by(_sid('name'), True).limit(25)
            q_1674: 'Query' = t_3700.offset(0)
            def fn_3867() -> 'str29':
                return 'complex query'
            test_110.assert_(q_1674.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0', fn_3867)
        finally:
            test_110.soft_fail_to_hard()
class TestCase147(TestCase48):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__2458(self) -> None:
        'safeToSql applies default limit when none set'
        test_111: Test = Test()
        try:
            q_1676: 'Query' = from_(_sid('users'))
            t_3442: 'SqlFragment' = q_1676.safe_to_sql(100)
            s_1677: 'str29' = t_3442.to_string()
            def fn_3866() -> 'str29':
                return _str_cat_4031('should have limit: ', s_1677)
            test_111.assert_(s_1677 == 'SELECT * FROM users LIMIT 100', fn_3866)
        finally:
            test_111.soft_fail_to_hard()
class TestCase148(TestCase48):
    def test___safeToSqlRespectsExplicitLimit__2459(self) -> None:
        'safeToSql respects explicit limit'
        test_112: Test = Test()
        try:
            q_1679: 'Query' = from_(_sid('users')).limit(5)
            t_3441: 'SqlFragment' = q_1679.safe_to_sql(100)
            s_1680: 'str29' = t_3441.to_string()
            def fn_3865() -> 'str29':
                return _str_cat_4031('explicit limit preserved: ', s_1680)
            test_112.assert_(s_1680 == 'SELECT * FROM users LIMIT 5', fn_3865)
        finally:
            test_112.soft_fail_to_hard()
class TestCase149(TestCase48):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__2460(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_113: Test = Test()
        try:
            did_bubble_1682: 'bool37'
            try:
                from_(_sid('users')).safe_to_sql(-1)
                did_bubble_1682 = False
            except Exception41:
                did_bubble_1682 = True
            def fn_3864() -> 'str29':
                return 'negative defaultLimit should bubble'
            test_113.assert_(did_bubble_1682, fn_3864)
        finally:
            test_113.soft_fail_to_hard()
class TestCase150(TestCase48):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__2461(self) -> None:
        'where with injection attempt in string value is escaped'
        test_114: Test = Test()
        try:
            evil_1684: 'str29' = "'; DROP TABLE users; --"
            t_3434: 'Query' = from_(_sid('users'))
            accumulator_2462: 'SqlBuilder' = SqlBuilder()
            accumulator_2462.append_safe('name = ')
            accumulator_2462.append_string("'; DROP TABLE users; --")
            q_1685: 'Query' = t_3434.where(accumulator_2462.accumulated)
            s_1686: 'str29' = q_1685.to_sql().to_string()
            t_3435: 'bool37' = s_1686.find("''") >= 0
            def fn_3863() -> 'str29':
                return _str_cat_4031('quotes must be doubled: ', s_1686)
            test_114.assert_(t_3435, fn_3863)
            t_3437: 'bool37' = s_1686.find('SELECT * FROM users WHERE name =') >= 0
            def fn_3862() -> 'str29':
                return _str_cat_4031('structure intact: ', s_1686)
            test_114.assert_(t_3437, fn_3862)
        finally:
            test_114.soft_fail_to_hard()
class TestCase151(TestCase48):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__2463(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_115: Test = Test()
        try:
            attack_1688: 'str29' = 'users; DROP TABLE users; --'
            did_bubble_1689: 'bool37'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_1689 = False
            except Exception41:
                did_bubble_1689 = True
            def fn_3861() -> 'str29':
                return 'metacharacter-containing name must be rejected at construction'
            test_115.assert_(did_bubble_1689, fn_3861)
        finally:
            test_115.soft_fail_to_hard()
class TestCase152(TestCase48):
    def test___innerJoinProducesInnerJoin__2464(self) -> None:
        'innerJoin produces INNER JOIN'
        test_116: Test = Test()
        try:
            t_3428: 'Query' = from_(_sid('users'))
            t_3429: 'SafeIdentifier' = _sid('orders')
            accumulator_2465: 'SqlBuilder' = SqlBuilder()
            accumulator_2465.append_safe('users.id = orders.user_id')
            q_1691: 'Query' = t_3428.inner_join(t_3429, accumulator_2465.accumulated)
            def fn_3860() -> 'str29':
                return 'inner join'
            test_116.assert_(q_1691.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id', fn_3860)
        finally:
            test_116.soft_fail_to_hard()
class TestCase153(TestCase48):
    def test___leftJoinProducesLeftJoin__2466(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_117: Test = Test()
        try:
            t_3425: 'Query' = from_(_sid('users'))
            t_3426: 'SafeIdentifier' = _sid('profiles')
            accumulator_2467: 'SqlBuilder' = SqlBuilder()
            accumulator_2467.append_safe('users.id = profiles.user_id')
            q_1693: 'Query' = t_3425.left_join(t_3426, accumulator_2467.accumulated)
            def fn_3859() -> 'str29':
                return 'left join'
            test_117.assert_(q_1693.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id', fn_3859)
        finally:
            test_117.soft_fail_to_hard()
class TestCase154(TestCase48):
    def test___rightJoinProducesRightJoin__2468(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_118: Test = Test()
        try:
            t_3422: 'Query' = from_(_sid('orders'))
            t_3423: 'SafeIdentifier' = _sid('users')
            accumulator_2469: 'SqlBuilder' = SqlBuilder()
            accumulator_2469.append_safe('orders.user_id = users.id')
            q_1695: 'Query' = t_3422.right_join(t_3423, accumulator_2469.accumulated)
            def fn_3858() -> 'str29':
                return 'right join'
            test_118.assert_(q_1695.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id', fn_3858)
        finally:
            test_118.soft_fail_to_hard()
class TestCase155(TestCase48):
    def test___fullJoinProducesFullOuterJoin__2470(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_119: Test = Test()
        try:
            t_3419: 'Query' = from_(_sid('users'))
            t_3420: 'SafeIdentifier' = _sid('orders')
            accumulator_2471: 'SqlBuilder' = SqlBuilder()
            accumulator_2471.append_safe('users.id = orders.user_id')
            q_1697: 'Query' = t_3419.full_join(t_3420, accumulator_2471.accumulated)
            def fn_3857() -> 'str29':
                return 'full join'
            test_119.assert_(q_1697.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id', fn_3857)
        finally:
            test_119.soft_fail_to_hard()
class TestCase156(TestCase48):
    def test___chainedJoins__2472(self) -> None:
        'chained joins'
        test_120: Test = Test()
        try:
            t_3413: 'Query' = from_(_sid('users'))
            t_3414: 'SafeIdentifier' = _sid('orders')
            accumulator_2473: 'SqlBuilder' = SqlBuilder()
            accumulator_2473.append_safe('users.id = orders.user_id')
            t_3416: 'Query' = t_3413.inner_join(t_3414, accumulator_2473.accumulated)
            t_3417: 'SafeIdentifier' = _sid('profiles')
            accumulator_2474: 'SqlBuilder' = SqlBuilder()
            accumulator_2474.append_safe('users.id = profiles.user_id')
            q_1699: 'Query' = t_3416.left_join(t_3417, accumulator_2474.accumulated)
            def fn_3856() -> 'str29':
                return 'chained joins'
            test_120.assert_(q_1699.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id', fn_3856)
        finally:
            test_120.soft_fail_to_hard()
class TestCase157(TestCase48):
    def test___joinWithWhereAndOrderBy__2475(self) -> None:
        'join with where and orderBy'
        test_121: Test = Test()
        try:
            t_3407: 'Query' = from_(_sid('users'))
            t_3408: 'SafeIdentifier' = _sid('orders')
            accumulator_2476: 'SqlBuilder' = SqlBuilder()
            accumulator_2476.append_safe('users.id = orders.user_id')
            t_3410: 'Query' = t_3407.inner_join(t_3408, accumulator_2476.accumulated)
            accumulator_2477: 'SqlBuilder' = SqlBuilder()
            accumulator_2477.append_safe('orders.total > ')
            accumulator_2477.append_int32(100)
            q_1701: 'Query' = t_3410.where(accumulator_2477.accumulated).order_by(_sid('name'), True).limit(10)
            def fn_3855() -> 'str29':
                return 'join with where/order/limit'
            test_121.assert_(q_1701.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10', fn_3855)
        finally:
            test_121.soft_fail_to_hard()
class TestCase158(TestCase48):
    def test___colHelperProducesQualifiedReference__2478(self) -> None:
        'col helper produces qualified reference'
        test_122: Test = Test()
        try:
            c_1703: 'SqlFragment' = col(_sid('users'), _sid('id'))
            def fn_3854() -> 'str29':
                return 'col helper'
            test_122.assert_(c_1703.to_string() == 'users.id', fn_3854)
        finally:
            test_122.soft_fail_to_hard()
class TestCase159(TestCase48):
    def test___joinWithColHelper__2479(self) -> None:
        'join with col helper'
        test_123: Test = Test()
        try:
            on_cond_1705: 'SqlFragment' = col(_sid('users'), _sid('id'))
            b_1706: 'SqlBuilder' = SqlBuilder()
            b_1706.append_fragment(on_cond_1705)
            b_1706.append_safe(' = ')
            b_1706.append_fragment(col(_sid('orders'), _sid('user_id')))
            q_1707: 'Query' = from_(_sid('users')).inner_join(_sid('orders'), b_1706.accumulated)
            def fn_3853() -> 'str29':
                return 'join with col'
            test_123.assert_(q_1707.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id', fn_3853)
        finally:
            test_123.soft_fail_to_hard()
class TestCase160(TestCase48):
    def test___orWhereBasic__2480(self) -> None:
        'orWhere basic'
        test_124: Test = Test()
        try:
            t_3405: 'Query' = from_(_sid('users'))
            accumulator_2481: 'SqlBuilder' = SqlBuilder()
            accumulator_2481.append_safe('status = ')
            accumulator_2481.append_string('active')
            q_1709: 'Query' = t_3405.or_where(accumulator_2481.accumulated)
            def fn_3852() -> 'str29':
                return 'orWhere basic'
            test_124.assert_(q_1709.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'", fn_3852)
        finally:
            test_124.soft_fail_to_hard()
class TestCase161(TestCase48):
    def test___whereThenOrWhere__2482(self) -> None:
        'where then orWhere'
        test_125: Test = Test()
        try:
            t_3401: 'Query' = from_(_sid('users'))
            accumulator_2483: 'SqlBuilder' = SqlBuilder()
            accumulator_2483.append_safe('age > ')
            accumulator_2483.append_int32(18)
            t_3403: 'Query' = t_3401.where(accumulator_2483.accumulated)
            accumulator_2484: 'SqlBuilder' = SqlBuilder()
            accumulator_2484.append_safe('vip = ')
            accumulator_2484.append_boolean(True)
            q_1711: 'Query' = t_3403.or_where(accumulator_2484.accumulated)
            def fn_3851() -> 'str29':
                return 'where then orWhere'
            test_125.assert_(q_1711.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE', fn_3851)
        finally:
            test_125.soft_fail_to_hard()
class TestCase162(TestCase48):
    def test___multipleOrWhere__2485(self) -> None:
        'multiple orWhere'
        test_126: Test = Test()
        try:
            t_3395: 'Query' = from_(_sid('users'))
            accumulator_2486: 'SqlBuilder' = SqlBuilder()
            accumulator_2486.append_safe('active = ')
            accumulator_2486.append_boolean(True)
            t_3397: 'Query' = t_3395.where(accumulator_2486.accumulated)
            accumulator_2487: 'SqlBuilder' = SqlBuilder()
            accumulator_2487.append_safe('role = ')
            accumulator_2487.append_string('admin')
            t_3399: 'Query' = t_3397.or_where(accumulator_2487.accumulated)
            accumulator_2488: 'SqlBuilder' = SqlBuilder()
            accumulator_2488.append_safe('role = ')
            accumulator_2488.append_string('moderator')
            q_1713: 'Query' = t_3399.or_where(accumulator_2488.accumulated)
            def fn_3850() -> 'str29':
                return 'multiple orWhere'
            test_126.assert_(q_1713.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'", fn_3850)
        finally:
            test_126.soft_fail_to_hard()
class TestCase163(TestCase48):
    def test___mixedWhereAndOrWhere__2489(self) -> None:
        'mixed where and orWhere'
        test_127: Test = Test()
        try:
            t_3389: 'Query' = from_(_sid('users'))
            accumulator_2490: 'SqlBuilder' = SqlBuilder()
            accumulator_2490.append_safe('age > ')
            accumulator_2490.append_int32(18)
            t_3391: 'Query' = t_3389.where(accumulator_2490.accumulated)
            accumulator_2491: 'SqlBuilder' = SqlBuilder()
            accumulator_2491.append_safe('active = ')
            accumulator_2491.append_boolean(True)
            t_3393: 'Query' = t_3391.where(accumulator_2491.accumulated)
            accumulator_2492: 'SqlBuilder' = SqlBuilder()
            accumulator_2492.append_safe('vip = ')
            accumulator_2492.append_boolean(True)
            q_1715: 'Query' = t_3393.or_where(accumulator_2492.accumulated)
            def fn_3849() -> 'str29':
                return 'mixed where and orWhere'
            test_127.assert_(q_1715.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE', fn_3849)
        finally:
            test_127.soft_fail_to_hard()
class TestCase164(TestCase48):
    def test___whereNull__2493(self) -> None:
        'whereNull'
        test_128: Test = Test()
        try:
            q_1717: 'Query' = from_(_sid('users')).where_null(_sid('deleted_at'))
            def fn_3848() -> 'str29':
                return 'whereNull'
            test_128.assert_(q_1717.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL', fn_3848)
        finally:
            test_128.soft_fail_to_hard()
class TestCase165(TestCase48):
    def test___whereNotNull__2494(self) -> None:
        'whereNotNull'
        test_129: Test = Test()
        try:
            q_1719: 'Query' = from_(_sid('users')).where_not_null(_sid('email'))
            def fn_3847() -> 'str29':
                return 'whereNotNull'
            test_129.assert_(q_1719.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL', fn_3847)
        finally:
            test_129.soft_fail_to_hard()
class TestCase166(TestCase48):
    def test___whereNullChainedWithWhere__2495(self) -> None:
        'whereNull chained with where'
        test_130: Test = Test()
        try:
            t_3387: 'Query' = from_(_sid('users'))
            accumulator_2496: 'SqlBuilder' = SqlBuilder()
            accumulator_2496.append_safe('active = ')
            accumulator_2496.append_boolean(True)
            q_1721: 'Query' = t_3387.where(accumulator_2496.accumulated).where_null(_sid('deleted_at'))
            def fn_3846() -> 'str29':
                return 'whereNull chained'
            test_130.assert_(q_1721.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL', fn_3846)
        finally:
            test_130.soft_fail_to_hard()
class TestCase167(TestCase48):
    def test___whereNotNullChainedWithOrWhere__2497(self) -> None:
        'whereNotNull chained with orWhere'
        test_131: Test = Test()
        try:
            t_3385: 'Query' = from_(_sid('users')).where_null(_sid('deleted_at'))
            accumulator_2498: 'SqlBuilder' = SqlBuilder()
            accumulator_2498.append_safe('role = ')
            accumulator_2498.append_string('admin')
            q_1723: 'Query' = t_3385.or_where(accumulator_2498.accumulated)
            def fn_3845() -> 'str29':
                return 'whereNotNull with orWhere'
            test_131.assert_(q_1723.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'", fn_3845)
        finally:
            test_131.soft_fail_to_hard()
class TestCase168(TestCase48):
    def test___whereInWithIntValues__2499(self) -> None:
        'whereIn with int values'
        test_132: Test = Test()
        try:
            q_1725: 'Query' = from_(_sid('users')).where_in(_sid('id'), (SqlInt32(1), SqlInt32(2), SqlInt32(3)))
            def fn_3844() -> 'str29':
                return 'whereIn ints'
            test_132.assert_(q_1725.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)', fn_3844)
        finally:
            test_132.soft_fail_to_hard()
class TestCase169(TestCase48):
    def test___whereInWithStringValuesEscaping__2500(self) -> None:
        'whereIn with string values escaping'
        test_133: Test = Test()
        try:
            q_1727: 'Query' = from_(_sid('users')).where_in(_sid('name'), (SqlString('Alice'), SqlString("Bob's")))
            def fn_3843() -> 'str29':
                return 'whereIn strings'
            test_133.assert_(q_1727.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')", fn_3843)
        finally:
            test_133.soft_fail_to_hard()
class TestCase170(TestCase48):
    def test___whereInWithEmptyListProduces1_0__2501(self) -> None:
        'whereIn with empty list produces 1=0'
        test_134: Test = Test()
        try:
            q_1729: 'Query' = from_(_sid('users')).where_in(_sid('id'), ())
            def fn_3842() -> 'str29':
                return 'whereIn empty'
            test_134.assert_(q_1729.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0', fn_3842)
        finally:
            test_134.soft_fail_to_hard()
class TestCase171(TestCase48):
    def test___whereInChained__2502(self) -> None:
        'whereIn chained'
        test_135: Test = Test()
        try:
            t_3383: 'Query' = from_(_sid('users'))
            accumulator_2503: 'SqlBuilder' = SqlBuilder()
            accumulator_2503.append_safe('active = ')
            accumulator_2503.append_boolean(True)
            q_1731: 'Query' = t_3383.where(accumulator_2503.accumulated).where_in(_sid('role'), (SqlString('admin'), SqlString('user')))
            def fn_3841() -> 'str29':
                return 'whereIn chained'
            test_135.assert_(q_1731.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')", fn_3841)
        finally:
            test_135.soft_fail_to_hard()
class TestCase172(TestCase48):
    def test___whereInSingleElement__2504(self) -> None:
        'whereIn single element'
        test_136: Test = Test()
        try:
            q_1733: 'Query' = from_(_sid('users')).where_in(_sid('id'), (SqlInt32(42),))
            def fn_3840() -> 'str29':
                return 'whereIn single'
            test_136.assert_(q_1733.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)', fn_3840)
        finally:
            test_136.soft_fail_to_hard()
class TestCase173(TestCase48):
    def test___whereNotBasic__2505(self) -> None:
        'whereNot basic'
        test_137: Test = Test()
        try:
            t_3381: 'Query' = from_(_sid('users'))
            accumulator_2506: 'SqlBuilder' = SqlBuilder()
            accumulator_2506.append_safe('active = ')
            accumulator_2506.append_boolean(True)
            q_1735: 'Query' = t_3381.where_not(accumulator_2506.accumulated)
            def fn_3839() -> 'str29':
                return 'whereNot'
            test_137.assert_(q_1735.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)', fn_3839)
        finally:
            test_137.soft_fail_to_hard()
class TestCase174(TestCase48):
    def test___whereNotChained__2507(self) -> None:
        'whereNot chained'
        test_138: Test = Test()
        try:
            t_3377: 'Query' = from_(_sid('users'))
            accumulator_2508: 'SqlBuilder' = SqlBuilder()
            accumulator_2508.append_safe('age > ')
            accumulator_2508.append_int32(18)
            t_3379: 'Query' = t_3377.where(accumulator_2508.accumulated)
            accumulator_2509: 'SqlBuilder' = SqlBuilder()
            accumulator_2509.append_safe('banned = ')
            accumulator_2509.append_boolean(True)
            q_1737: 'Query' = t_3379.where_not(accumulator_2509.accumulated)
            def fn_3838() -> 'str29':
                return 'whereNot chained'
            test_138.assert_(q_1737.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)', fn_3838)
        finally:
            test_138.soft_fail_to_hard()
class TestCase175(TestCase48):
    def test___whereBetweenIntegers__2510(self) -> None:
        'whereBetween integers'
        test_139: Test = Test()
        try:
            q_1739: 'Query' = from_(_sid('users')).where_between(_sid('age'), SqlInt32(18), SqlInt32(65))
            def fn_3837() -> 'str29':
                return 'whereBetween ints'
            test_139.assert_(q_1739.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65', fn_3837)
        finally:
            test_139.soft_fail_to_hard()
class TestCase176(TestCase48):
    def test___whereBetweenChained__2511(self) -> None:
        'whereBetween chained'
        test_140: Test = Test()
        try:
            t_3375: 'Query' = from_(_sid('users'))
            accumulator_2512: 'SqlBuilder' = SqlBuilder()
            accumulator_2512.append_safe('active = ')
            accumulator_2512.append_boolean(True)
            q_1741: 'Query' = t_3375.where(accumulator_2512.accumulated).where_between(_sid('age'), SqlInt32(21), SqlInt32(30))
            def fn_3836() -> 'str29':
                return 'whereBetween chained'
            test_140.assert_(q_1741.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30', fn_3836)
        finally:
            test_140.soft_fail_to_hard()
class TestCase177(TestCase48):
    def test___whereLikeBasic__2513(self) -> None:
        'whereLike basic'
        test_141: Test = Test()
        try:
            q_1743: 'Query' = from_(_sid('users')).where_like(_sid('name'), 'John%')
            def fn_3835() -> 'str29':
                return 'whereLike'
            test_141.assert_(q_1743.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'", fn_3835)
        finally:
            test_141.soft_fail_to_hard()
class TestCase178(TestCase48):
    def test___whereIlikeBasic__2514(self) -> None:
        'whereILike basic'
        test_142: Test = Test()
        try:
            q_1745: 'Query' = from_(_sid('users')).where_i_like(_sid('email'), '%@gmail.com')
            def fn_3834() -> 'str29':
                return 'whereILike'
            test_142.assert_(q_1745.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'", fn_3834)
        finally:
            test_142.soft_fail_to_hard()
class TestCase179(TestCase48):
    def test___whereLikeWithInjectionAttempt__2515(self) -> None:
        'whereLike with injection attempt'
        test_143: Test = Test()
        try:
            q_1747: 'Query' = from_(_sid('users')).where_like(_sid('name'), "'; DROP TABLE users; --")
            s_1748: 'str29' = q_1747.to_sql().to_string()
            t_3370: 'bool37' = s_1748.find("''") >= 0
            def fn_3833() -> 'str29':
                return _str_cat_4031('like injection escaped: ', s_1748)
            test_143.assert_(t_3370, fn_3833)
            t_3372: 'bool37' = s_1748.find('LIKE') >= 0
            def fn_3832() -> 'str29':
                return _str_cat_4031('like structure intact: ', s_1748)
            test_143.assert_(t_3372, fn_3832)
        finally:
            test_143.soft_fail_to_hard()
class TestCase180(TestCase48):
    def test___whereLikeWildcardPatterns__2516(self) -> None:
        'whereLike wildcard patterns'
        test_144: Test = Test()
        try:
            q_1750: 'Query' = from_(_sid('users')).where_like(_sid('name'), '%son%')
            def fn_3831() -> 'str29':
                return 'whereLike wildcard'
            test_144.assert_(q_1750.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'", fn_3831)
        finally:
            test_144.soft_fail_to_hard()
class TestCase181(TestCase48):
    def test___countAllProducesCount__2517(self) -> None:
        'countAll produces COUNT(*)'
        test_145: Test = Test()
        try:
            f_1752: 'SqlFragment' = count_all()
            def fn_3830() -> 'str29':
                return 'countAll'
            test_145.assert_(f_1752.to_string() == 'COUNT(*)', fn_3830)
        finally:
            test_145.soft_fail_to_hard()
class TestCase182(TestCase48):
    def test___countColProducesCountField__2518(self) -> None:
        'countCol produces COUNT(field)'
        test_146: Test = Test()
        try:
            f_1754: 'SqlFragment' = count_col(_sid('id'))
            def fn_3829() -> 'str29':
                return 'countCol'
            test_146.assert_(f_1754.to_string() == 'COUNT(id)', fn_3829)
        finally:
            test_146.soft_fail_to_hard()
class TestCase183(TestCase48):
    def test___sumColProducesSumField__2519(self) -> None:
        'sumCol produces SUM(field)'
        test_147: Test = Test()
        try:
            f_1756: 'SqlFragment' = sum_col(_sid('amount'))
            def fn_3828() -> 'str29':
                return 'sumCol'
            test_147.assert_(f_1756.to_string() == 'SUM(amount)', fn_3828)
        finally:
            test_147.soft_fail_to_hard()
class TestCase184(TestCase48):
    def test___avgColProducesAvgField__2520(self) -> None:
        'avgCol produces AVG(field)'
        test_148: Test = Test()
        try:
            f_1758: 'SqlFragment' = avg_col(_sid('price'))
            def fn_3827() -> 'str29':
                return 'avgCol'
            test_148.assert_(f_1758.to_string() == 'AVG(price)', fn_3827)
        finally:
            test_148.soft_fail_to_hard()
class TestCase185(TestCase48):
    def test___minColProducesMinField__2521(self) -> None:
        'minCol produces MIN(field)'
        test_149: Test = Test()
        try:
            f_1760: 'SqlFragment' = min_col(_sid('created_at'))
            def fn_3826() -> 'str29':
                return 'minCol'
            test_149.assert_(f_1760.to_string() == 'MIN(created_at)', fn_3826)
        finally:
            test_149.soft_fail_to_hard()
class TestCase186(TestCase48):
    def test___maxColProducesMaxField__2522(self) -> None:
        'maxCol produces MAX(field)'
        test_150: Test = Test()
        try:
            f_1762: 'SqlFragment' = max_col(_sid('score'))
            def fn_3825() -> 'str29':
                return 'maxCol'
            test_150.assert_(f_1762.to_string() == 'MAX(score)', fn_3825)
        finally:
            test_150.soft_fail_to_hard()
class TestCase187(TestCase48):
    def test___selectExprWithAggregate__2523(self) -> None:
        'selectExpr with aggregate'
        test_151: Test = Test()
        try:
            q_1764: 'Query' = from_(_sid('orders')).select_expr((count_all(),))
            def fn_3824() -> 'str29':
                return 'selectExpr count'
            test_151.assert_(q_1764.to_sql().to_string() == 'SELECT COUNT(*) FROM orders', fn_3824)
        finally:
            test_151.soft_fail_to_hard()
class TestCase188(TestCase48):
    def test___selectExprWithMultipleExpressions__2524(self) -> None:
        'selectExpr with multiple expressions'
        test_152: Test = Test()
        try:
            name_frag_1766: 'SqlFragment' = col(_sid('users'), _sid('name'))
            q_1767: 'Query' = from_(_sid('users')).select_expr((name_frag_1766, count_all()))
            def fn_3823() -> 'str29':
                return 'selectExpr multi'
            test_152.assert_(q_1767.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users', fn_3823)
        finally:
            test_152.soft_fail_to_hard()
class TestCase189(TestCase48):
    def test___selectExprOverridesSelectedFields__2525(self) -> None:
        'selectExpr overrides selectedFields'
        test_153: Test = Test()
        try:
            q_1769: 'Query' = from_(_sid('users')).select((_sid('id'), _sid('name'))).select_expr((count_all(),))
            def fn_3822() -> 'str29':
                return 'selectExpr overrides select'
            test_153.assert_(q_1769.to_sql().to_string() == 'SELECT COUNT(*) FROM users', fn_3822)
        finally:
            test_153.soft_fail_to_hard()
class TestCase190(TestCase48):
    def test___groupBySingleField__2526(self) -> None:
        'groupBy single field'
        test_154: Test = Test()
        try:
            q_1771: 'Query' = from_(_sid('orders')).select_expr((col(_sid('orders'), _sid('status')), count_all())).group_by(_sid('status'))
            def fn_3821() -> 'str29':
                return 'groupBy single'
            test_154.assert_(q_1771.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status', fn_3821)
        finally:
            test_154.soft_fail_to_hard()
class TestCase191(TestCase48):
    def test___groupByMultipleFields__2527(self) -> None:
        'groupBy multiple fields'
        test_155: Test = Test()
        try:
            q_1773: 'Query' = from_(_sid('orders')).group_by(_sid('status')).group_by(_sid('category'))
            def fn_3820() -> 'str29':
                return 'groupBy multiple'
            test_155.assert_(q_1773.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category', fn_3820)
        finally:
            test_155.soft_fail_to_hard()
class TestCase192(TestCase48):
    def test___havingBasic__2528(self) -> None:
        'having basic'
        test_156: Test = Test()
        try:
            t_3367: 'Query' = from_(_sid('orders')).select_expr((col(_sid('orders'), _sid('status')), count_all())).group_by(_sid('status'))
            accumulator_2529: 'SqlBuilder' = SqlBuilder()
            accumulator_2529.append_safe('COUNT(*) > ')
            accumulator_2529.append_int32(5)
            q_1775: 'Query' = t_3367.having(accumulator_2529.accumulated)
            def fn_3819() -> 'str29':
                return 'having basic'
            test_156.assert_(q_1775.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5', fn_3819)
        finally:
            test_156.soft_fail_to_hard()
class TestCase193(TestCase48):
    def test___orHaving__2530(self) -> None:
        'orHaving'
        test_157: Test = Test()
        try:
            t_3363: 'Query' = from_(_sid('orders')).group_by(_sid('status'))
            accumulator_2531: 'SqlBuilder' = SqlBuilder()
            accumulator_2531.append_safe('COUNT(*) > ')
            accumulator_2531.append_int32(5)
            t_3365: 'Query' = t_3363.having(accumulator_2531.accumulated)
            accumulator_2532: 'SqlBuilder' = SqlBuilder()
            accumulator_2532.append_safe('SUM(total) > ')
            accumulator_2532.append_int32(1000)
            q_1777: 'Query' = t_3365.or_having(accumulator_2532.accumulated)
            def fn_3818() -> 'str29':
                return 'orHaving'
            test_157.assert_(q_1777.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000', fn_3818)
        finally:
            test_157.soft_fail_to_hard()
class TestCase194(TestCase48):
    def test___distinctBasic__2533(self) -> None:
        'distinct basic'
        test_158: Test = Test()
        try:
            q_1779: 'Query' = from_(_sid('users')).select((_sid('name'),)).distinct()
            def fn_3817() -> 'str29':
                return 'distinct'
            test_158.assert_(q_1779.to_sql().to_string() == 'SELECT DISTINCT name FROM users', fn_3817)
        finally:
            test_158.soft_fail_to_hard()
class TestCase195(TestCase48):
    def test___distinctWithWhere__2534(self) -> None:
        'distinct with where'
        test_159: Test = Test()
        try:
            t_3361: 'Query' = from_(_sid('users')).select((_sid('email'),))
            accumulator_2535: 'SqlBuilder' = SqlBuilder()
            accumulator_2535.append_safe('active = ')
            accumulator_2535.append_boolean(True)
            q_1781: 'Query' = t_3361.where(accumulator_2535.accumulated).distinct()
            def fn_3816() -> 'str29':
                return 'distinct with where'
            test_159.assert_(q_1781.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE', fn_3816)
        finally:
            test_159.soft_fail_to_hard()
class TestCase196(TestCase48):
    def test___countSqlBare__2536(self) -> None:
        'countSql bare'
        test_160: Test = Test()
        try:
            q_1783: 'Query' = from_(_sid('users'))
            def fn_3815() -> 'str29':
                return 'countSql bare'
            test_160.assert_(q_1783.count_sql().to_string() == 'SELECT COUNT(*) FROM users', fn_3815)
        finally:
            test_160.soft_fail_to_hard()
class TestCase197(TestCase48):
    def test___countSqlWithWhere__2537(self) -> None:
        'countSql with WHERE'
        test_161: Test = Test()
        try:
            t_3359: 'Query' = from_(_sid('users'))
            accumulator_2538: 'SqlBuilder' = SqlBuilder()
            accumulator_2538.append_safe('active = ')
            accumulator_2538.append_boolean(True)
            q_1785: 'Query' = t_3359.where(accumulator_2538.accumulated)
            def fn_3814() -> 'str29':
                return 'countSql with where'
            test_161.assert_(q_1785.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE', fn_3814)
        finally:
            test_161.soft_fail_to_hard()
class TestCase198(TestCase48):
    def test___countSqlWithJoin__2539(self) -> None:
        'countSql with JOIN'
        test_162: Test = Test()
        try:
            t_3354: 'Query' = from_(_sid('users'))
            t_3355: 'SafeIdentifier' = _sid('orders')
            accumulator_2540: 'SqlBuilder' = SqlBuilder()
            accumulator_2540.append_safe('users.id = orders.user_id')
            t_3357: 'Query' = t_3354.inner_join(t_3355, accumulator_2540.accumulated)
            accumulator_2541: 'SqlBuilder' = SqlBuilder()
            accumulator_2541.append_safe('orders.total > ')
            accumulator_2541.append_int32(100)
            q_1787: 'Query' = t_3357.where(accumulator_2541.accumulated)
            def fn_3813() -> 'str29':
                return 'countSql with join'
            test_162.assert_(q_1787.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100', fn_3813)
        finally:
            test_162.soft_fail_to_hard()
class TestCase199(TestCase48):
    def test___countSqlDropsOrderByLimitOffset__2542(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_163: Test = Test()
        try:
            t_3351: 'Query' = from_(_sid('users'))
            accumulator_2543: 'SqlBuilder' = SqlBuilder()
            accumulator_2543.append_safe('active = ')
            accumulator_2543.append_boolean(True)
            t_3699: 'Query' = t_3351.where(accumulator_2543.accumulated).order_by(_sid('name'), True).limit(10)
            q_1789: 'Query' = t_3699.offset(20)
            s_1790: 'str29' = q_1789.count_sql().to_string()
            def fn_3812() -> 'str29':
                return _str_cat_4031('countSql drops extras: ', s_1790)
            test_163.assert_(s_1790 == 'SELECT COUNT(*) FROM users WHERE active = TRUE', fn_3812)
        finally:
            test_163.soft_fail_to_hard()
class TestCase200(TestCase48):
    def test___fullAggregationQuery__2544(self) -> None:
        'full aggregation query'
        test_164: Test = Test()
        try:
            t_3344: 'Query' = from_(_sid('orders')).select_expr((col(_sid('orders'), _sid('status')), count_all(), sum_col(_sid('total'))))
            t_3345: 'SafeIdentifier' = _sid('users')
            accumulator_2545: 'SqlBuilder' = SqlBuilder()
            accumulator_2545.append_safe('orders.user_id = users.id')
            t_3347: 'Query' = t_3344.inner_join(t_3345, accumulator_2545.accumulated)
            accumulator_2546: 'SqlBuilder' = SqlBuilder()
            accumulator_2546.append_safe('users.active = ')
            accumulator_2546.append_boolean(True)
            t_3349: 'Query' = t_3347.where(accumulator_2546.accumulated).group_by(_sid('status'))
            accumulator_2547: 'SqlBuilder' = SqlBuilder()
            accumulator_2547.append_safe('COUNT(*) > ')
            accumulator_2547.append_int32(3)
            q_1792: 'Query' = t_3349.having(accumulator_2547.accumulated).order_by(_sid('status'), True)
            expected_1793: 'str29' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_3811() -> 'str29':
                return 'full aggregation'
            test_164.assert_(q_1792.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC', fn_3811)
        finally:
            test_164.soft_fail_to_hard()
class TestCase201(TestCase48):
    def test___unionSql__2548(self) -> None:
        'unionSql'
        test_165: Test = Test()
        try:
            t_3340: 'Query' = from_(_sid('users'))
            accumulator_2549: 'SqlBuilder' = SqlBuilder()
            accumulator_2549.append_safe('role = ')
            accumulator_2549.append_string('admin')
            a_1795: 'Query' = t_3340.where(accumulator_2549.accumulated)
            t_3342: 'Query' = from_(_sid('users'))
            accumulator_2550: 'SqlBuilder' = SqlBuilder()
            accumulator_2550.append_safe('role = ')
            accumulator_2550.append_string('moderator')
            b_1796: 'Query' = t_3342.where(accumulator_2550.accumulated)
            s_1797: 'str29' = union_sql(a_1795, b_1796).to_string()
            def fn_3810() -> 'str29':
                return _str_cat_4031('unionSql: ', s_1797)
            test_165.assert_(s_1797 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')", fn_3810)
        finally:
            test_165.soft_fail_to_hard()
class TestCase202(TestCase48):
    def test___unionAllSql__2551(self) -> None:
        'unionAllSql'
        test_166: Test = Test()
        try:
            a_1799: 'Query' = from_(_sid('users')).select((_sid('name'),))
            b_1800: 'Query' = from_(_sid('contacts')).select((_sid('name'),))
            s_1801: 'str29' = union_all_sql(a_1799, b_1800).to_string()
            def fn_3809() -> 'str29':
                return _str_cat_4031('unionAllSql: ', s_1801)
            test_166.assert_(s_1801 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)', fn_3809)
        finally:
            test_166.soft_fail_to_hard()
class TestCase203(TestCase48):
    def test___intersectSql__2552(self) -> None:
        'intersectSql'
        test_167: Test = Test()
        try:
            a_1803: 'Query' = from_(_sid('users')).select((_sid('email'),))
            b_1804: 'Query' = from_(_sid('subscribers')).select((_sid('email'),))
            s_1805: 'str29' = intersect_sql(a_1803, b_1804).to_string()
            def fn_3808() -> 'str29':
                return _str_cat_4031('intersectSql: ', s_1805)
            test_167.assert_(s_1805 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)', fn_3808)
        finally:
            test_167.soft_fail_to_hard()
class TestCase204(TestCase48):
    def test___exceptSql__2553(self) -> None:
        'exceptSql'
        test_168: Test = Test()
        try:
            a_1807: 'Query' = from_(_sid('users')).select((_sid('id'),))
            b_1808: 'Query' = from_(_sid('banned')).select((_sid('id'),))
            s_1809: 'str29' = except_sql(a_1807, b_1808).to_string()
            def fn_3807() -> 'str29':
                return _str_cat_4031('exceptSql: ', s_1809)
            test_168.assert_(s_1809 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)', fn_3807)
        finally:
            test_168.soft_fail_to_hard()
class TestCase205(TestCase48):
    def test___subqueryWithAlias__2554(self) -> None:
        'subquery with alias'
        test_169: Test = Test()
        try:
            t_3338: 'Query' = from_(_sid('orders')).select((_sid('user_id'),))
            accumulator_2555: 'SqlBuilder' = SqlBuilder()
            accumulator_2555.append_safe('total > ')
            accumulator_2555.append_int32(100)
            inner_1811: 'Query' = t_3338.where(accumulator_2555.accumulated)
            s_1812: 'str29' = subquery(inner_1811, _sid('big_orders')).to_string()
            def fn_3806() -> 'str29':
                return _str_cat_4031('subquery: ', s_1812)
            test_169.assert_(s_1812 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders', fn_3806)
        finally:
            test_169.soft_fail_to_hard()
class TestCase206(TestCase48):
    def test___existsSql__2556(self) -> None:
        'existsSql'
        test_170: Test = Test()
        try:
            t_3336: 'Query' = from_(_sid('orders'))
            accumulator_2557: 'SqlBuilder' = SqlBuilder()
            accumulator_2557.append_safe('orders.user_id = users.id')
            inner_1814: 'Query' = t_3336.where(accumulator_2557.accumulated)
            s_1815: 'str29' = exists_sql(inner_1814).to_string()
            def fn_3805() -> 'str29':
                return _str_cat_4031('existsSql: ', s_1815)
            test_170.assert_(s_1815 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)', fn_3805)
        finally:
            test_170.soft_fail_to_hard()
class TestCase207(TestCase48):
    def test___whereInSubquery__2558(self) -> None:
        'whereInSubquery'
        test_171: Test = Test()
        try:
            t_3334: 'Query' = from_(_sid('orders')).select((_sid('user_id'),))
            accumulator_2559: 'SqlBuilder' = SqlBuilder()
            accumulator_2559.append_safe('total > ')
            accumulator_2559.append_int32(1000)
            sub_1817: 'Query' = t_3334.where(accumulator_2559.accumulated)
            q_1818: 'Query' = from_(_sid('users')).where_in_subquery(_sid('id'), sub_1817)
            s_1819: 'str29' = q_1818.to_sql().to_string()
            def fn_3804() -> 'str29':
                return _str_cat_4031('whereInSubquery: ', s_1819)
            test_171.assert_(s_1819 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)', fn_3804)
        finally:
            test_171.soft_fail_to_hard()
class TestCase208(TestCase48):
    def test___setOperationWithWhereOnEachSide__2560(self) -> None:
        'set operation with WHERE on each side'
        test_172: Test = Test()
        try:
            t_3328: 'Query' = from_(_sid('users'))
            accumulator_2561: 'SqlBuilder' = SqlBuilder()
            accumulator_2561.append_safe('age > ')
            accumulator_2561.append_int32(18)
            t_3330: 'Query' = t_3328.where(accumulator_2561.accumulated)
            accumulator_2562: 'SqlBuilder' = SqlBuilder()
            accumulator_2562.append_safe('active = ')
            accumulator_2562.append_boolean(True)
            a_1821: 'Query' = t_3330.where(accumulator_2562.accumulated)
            t_3332: 'Query' = from_(_sid('users'))
            accumulator_2563: 'SqlBuilder' = SqlBuilder()
            accumulator_2563.append_safe('role = ')
            accumulator_2563.append_string('vip')
            b_1822: 'Query' = t_3332.where(accumulator_2563.accumulated)
            s_1823: 'str29' = union_sql(a_1821, b_1822).to_string()
            def fn_3803() -> 'str29':
                return _str_cat_4031('union with where: ', s_1823)
            test_172.assert_(s_1823 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')", fn_3803)
        finally:
            test_172.soft_fail_to_hard()
class TestCase209(TestCase48):
    def test___whereInSubqueryChainedWithWhere__2564(self) -> None:
        'whereInSubquery chained with where'
        test_173: Test = Test()
        try:
            sub_1825: 'Query' = from_(_sid('orders')).select((_sid('user_id'),))
            t_3326: 'Query' = from_(_sid('users'))
            accumulator_2565: 'SqlBuilder' = SqlBuilder()
            accumulator_2565.append_safe('active = ')
            accumulator_2565.append_boolean(True)
            q_1826: 'Query' = t_3326.where(accumulator_2565.accumulated).where_in_subquery(_sid('id'), sub_1825)
            s_1827: 'str29' = q_1826.to_sql().to_string()
            def fn_3802() -> 'str29':
                return _str_cat_4031('whereInSubquery chained: ', s_1827)
            test_173.assert_(s_1827 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)', fn_3802)
        finally:
            test_173.soft_fail_to_hard()
class TestCase210(TestCase48):
    def test___existsSqlUsedInWhere__2566(self) -> None:
        'existsSql used in where'
        test_174: Test = Test()
        try:
            t_3324: 'Query' = from_(_sid('orders'))
            accumulator_2567: 'SqlBuilder' = SqlBuilder()
            accumulator_2567.append_safe('orders.user_id = users.id')
            sub_1829: 'Query' = t_3324.where(accumulator_2567.accumulated)
            q_1830: 'Query' = from_(_sid('users')).where(exists_sql(sub_1829))
            s_1831: 'str29' = q_1830.to_sql().to_string()
            def fn_3801() -> 'str29':
                return _str_cat_4031('exists in where: ', s_1831)
            test_174.assert_(s_1831 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)', fn_3801)
        finally:
            test_174.soft_fail_to_hard()
class TestCase211(TestCase48):
    def test___updateQueryBasic__2568(self) -> None:
        'UpdateQuery basic'
        test_175: Test = Test()
        try:
            t_3321: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('Alice'))
            accumulator_2569: 'SqlBuilder' = SqlBuilder()
            accumulator_2569.append_safe('id = ')
            accumulator_2569.append_int32(1)
            q_1833: 'SqlFragment' = t_3321.where(accumulator_2569.accumulated).to_sql()
            def fn_3800() -> 'str29':
                return 'update basic'
            test_175.assert_(q_1833.to_string() == "UPDATE users SET name = 'Alice' WHERE id = 1", fn_3800)
        finally:
            test_175.soft_fail_to_hard()
class TestCase212(TestCase48):
    def test___updateQueryMultipleSet__2570(self) -> None:
        'UpdateQuery multiple SET'
        test_176: Test = Test()
        try:
            t_3318: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('Bob')).set(_sid('age'), SqlInt32(30))
            accumulator_2571: 'SqlBuilder' = SqlBuilder()
            accumulator_2571.append_safe('id = ')
            accumulator_2571.append_int32(2)
            q_1835: 'SqlFragment' = t_3318.where(accumulator_2571.accumulated).to_sql()
            def fn_3799() -> 'str29':
                return 'update multi set'
            test_176.assert_(q_1835.to_string() == "UPDATE users SET name = 'Bob', age = 30 WHERE id = 2", fn_3799)
        finally:
            test_176.soft_fail_to_hard()
class TestCase213(TestCase48):
    def test___updateQueryMultipleWhere__2572(self) -> None:
        'UpdateQuery multiple WHERE'
        test_177: Test = Test()
        try:
            t_3313: 'UpdateQuery' = update(_sid('users')).set(_sid('active'), SqlBoolean(False))
            accumulator_2573: 'SqlBuilder' = SqlBuilder()
            accumulator_2573.append_safe('age < ')
            accumulator_2573.append_int32(18)
            t_3315: 'UpdateQuery' = t_3313.where(accumulator_2573.accumulated)
            accumulator_2574: 'SqlBuilder' = SqlBuilder()
            accumulator_2574.append_safe('role = ')
            accumulator_2574.append_string('guest')
            q_1837: 'SqlFragment' = t_3315.where(accumulator_2574.accumulated).to_sql()
            def fn_3798() -> 'str29':
                return 'update multi where'
            test_177.assert_(q_1837.to_string() == "UPDATE users SET active = FALSE WHERE age < 18 AND role = 'guest'", fn_3798)
        finally:
            test_177.soft_fail_to_hard()
class TestCase214(TestCase48):
    def test___updateQueryOrWhere__2575(self) -> None:
        'UpdateQuery orWhere'
        test_178: Test = Test()
        try:
            t_3308: 'UpdateQuery' = update(_sid('users')).set(_sid('status'), SqlString('banned'))
            accumulator_2576: 'SqlBuilder' = SqlBuilder()
            accumulator_2576.append_safe('spam_count > ')
            accumulator_2576.append_int32(10)
            t_3310: 'UpdateQuery' = t_3308.where(accumulator_2576.accumulated)
            accumulator_2577: 'SqlBuilder' = SqlBuilder()
            accumulator_2577.append_safe('reported = ')
            accumulator_2577.append_boolean(True)
            q_1839: 'SqlFragment' = t_3310.or_where(accumulator_2577.accumulated).to_sql()
            def fn_3797() -> 'str29':
                return 'update orWhere'
            test_178.assert_(q_1839.to_string() == "UPDATE users SET status = 'banned' WHERE spam_count > 10 OR reported = TRUE", fn_3797)
        finally:
            test_178.soft_fail_to_hard()
class TestCase215(TestCase48):
    def test___updateQueryBubblesWithoutWhere__2578(self) -> None:
        'UpdateQuery bubbles without WHERE'
        test_179: Test = Test()
        try:
            did_bubble_1841: 'bool37'
            try:
                update(_sid('users')).set(_sid('x'), SqlInt32(1)).to_sql()
                did_bubble_1841 = False
            except Exception41:
                did_bubble_1841 = True
            def fn_3796() -> 'str29':
                return 'update without WHERE should bubble'
            test_179.assert_(did_bubble_1841, fn_3796)
        finally:
            test_179.soft_fail_to_hard()
class TestCase216(TestCase48):
    def test___updateQueryBubblesWithoutSet__2579(self) -> None:
        'UpdateQuery bubbles without SET'
        test_180: Test = Test()
        try:
            did_bubble_1843: 'bool37'
            try:
                t_3304: 'UpdateQuery' = update(_sid('users'))
                accumulator_2580: 'SqlBuilder' = SqlBuilder()
                accumulator_2580.append_safe('id = ')
                accumulator_2580.append_int32(1)
                t_3304.where(accumulator_2580.accumulated).to_sql()
                did_bubble_1843 = False
            except Exception41:
                did_bubble_1843 = True
            def fn_3795() -> 'str29':
                return 'update without SET should bubble'
            test_180.assert_(did_bubble_1843, fn_3795)
        finally:
            test_180.soft_fail_to_hard()
class TestCase217(TestCase48):
    def test___updateQueryWithLimit__2581(self) -> None:
        'UpdateQuery with limit'
        test_181: Test = Test()
        try:
            t_3301: 'UpdateQuery' = update(_sid('users')).set(_sid('active'), SqlBoolean(False))
            accumulator_2582: 'SqlBuilder' = SqlBuilder()
            accumulator_2582.append_safe('last_login < ')
            accumulator_2582.append_string('2024-01-01')
            t_3698: 'UpdateQuery' = t_3301.where(accumulator_2582.accumulated).limit(100)
            q_1845: 'SqlFragment' = t_3698.to_sql()
            def fn_3794() -> 'str29':
                return 'update limit'
            test_181.assert_(q_1845.to_string() == "UPDATE users SET active = FALSE WHERE last_login < '2024-01-01' LIMIT 100", fn_3794)
        finally:
            test_181.soft_fail_to_hard()
class TestCase218(TestCase48):
    def test___updateQueryEscaping__2583(self) -> None:
        'UpdateQuery escaping'
        test_182: Test = Test()
        try:
            t_3298: 'UpdateQuery' = update(_sid('users')).set(_sid('bio'), SqlString("It's a test"))
            accumulator_2584: 'SqlBuilder' = SqlBuilder()
            accumulator_2584.append_safe('id = ')
            accumulator_2584.append_int32(1)
            q_1847: 'SqlFragment' = t_3298.where(accumulator_2584.accumulated).to_sql()
            def fn_3793() -> 'str29':
                return 'update escaping'
            test_182.assert_(q_1847.to_string() == "UPDATE users SET bio = 'It''s a test' WHERE id = 1", fn_3793)
        finally:
            test_182.soft_fail_to_hard()
class TestCase219(TestCase48):
    def test___deleteQueryBasic__2585(self) -> None:
        'DeleteQuery basic'
        test_183: Test = Test()
        try:
            t_3295: 'DeleteQuery' = delete_from(_sid('users'))
            accumulator_2586: 'SqlBuilder' = SqlBuilder()
            accumulator_2586.append_safe('id = ')
            accumulator_2586.append_int32(1)
            q_1849: 'SqlFragment' = t_3295.where(accumulator_2586.accumulated).to_sql()
            def fn_3792() -> 'str29':
                return 'delete basic'
            test_183.assert_(q_1849.to_string() == 'DELETE FROM users WHERE id = 1', fn_3792)
        finally:
            test_183.soft_fail_to_hard()
class TestCase220(TestCase48):
    def test___deleteQueryMultipleWhere__2587(self) -> None:
        'DeleteQuery multiple WHERE'
        test_184: Test = Test()
        try:
            t_3290: 'DeleteQuery' = delete_from(_sid('logs'))
            accumulator_2588: 'SqlBuilder' = SqlBuilder()
            accumulator_2588.append_safe('created_at < ')
            accumulator_2588.append_string('2024-01-01')
            t_3292: 'DeleteQuery' = t_3290.where(accumulator_2588.accumulated)
            accumulator_2589: 'SqlBuilder' = SqlBuilder()
            accumulator_2589.append_safe('level = ')
            accumulator_2589.append_string('debug')
            q_1851: 'SqlFragment' = t_3292.where(accumulator_2589.accumulated).to_sql()
            def fn_3791() -> 'str29':
                return 'delete multi where'
            test_184.assert_(q_1851.to_string() == "DELETE FROM logs WHERE created_at < '2024-01-01' AND level = 'debug'", fn_3791)
        finally:
            test_184.soft_fail_to_hard()
class TestCase221(TestCase48):
    def test___deleteQueryBubblesWithoutWhere__2590(self) -> None:
        'DeleteQuery bubbles without WHERE'
        test_185: Test = Test()
        try:
            did_bubble_1853: 'bool37'
            try:
                delete_from(_sid('users')).to_sql()
                did_bubble_1853 = False
            except Exception41:
                did_bubble_1853 = True
            def fn_3790() -> 'str29':
                return 'delete without WHERE should bubble'
            test_185.assert_(did_bubble_1853, fn_3790)
        finally:
            test_185.soft_fail_to_hard()
class TestCase222(TestCase48):
    def test___deleteQueryOrWhere__2591(self) -> None:
        'DeleteQuery orWhere'
        test_186: Test = Test()
        try:
            t_3284: 'DeleteQuery' = delete_from(_sid('sessions'))
            accumulator_2592: 'SqlBuilder' = SqlBuilder()
            accumulator_2592.append_safe('expired = ')
            accumulator_2592.append_boolean(True)
            t_3286: 'DeleteQuery' = t_3284.where(accumulator_2592.accumulated)
            accumulator_2593: 'SqlBuilder' = SqlBuilder()
            accumulator_2593.append_safe('created_at < ')
            accumulator_2593.append_string('2023-01-01')
            q_1855: 'SqlFragment' = t_3286.or_where(accumulator_2593.accumulated).to_sql()
            def fn_3789() -> 'str29':
                return 'delete orWhere'
            test_186.assert_(q_1855.to_string() == "DELETE FROM sessions WHERE expired = TRUE OR created_at < '2023-01-01'", fn_3789)
        finally:
            test_186.soft_fail_to_hard()
class TestCase223(TestCase48):
    def test___deleteQueryWithLimit__2594(self) -> None:
        'DeleteQuery with limit'
        test_187: Test = Test()
        try:
            t_3281: 'DeleteQuery' = delete_from(_sid('logs'))
            accumulator_2595: 'SqlBuilder' = SqlBuilder()
            accumulator_2595.append_safe('level = ')
            accumulator_2595.append_string('debug')
            t_3697: 'DeleteQuery' = t_3281.where(accumulator_2595.accumulated).limit(1000)
            q_1857: 'SqlFragment' = t_3697.to_sql()
            def fn_3788() -> 'str29':
                return 'delete limit'
            test_187.assert_(q_1857.to_string() == "DELETE FROM logs WHERE level = 'debug' LIMIT 1000", fn_3788)
        finally:
            test_187.soft_fail_to_hard()
class TestCase224(TestCase48):
    def test___orderByNullsNullsFirst__2596(self) -> None:
        'orderByNulls NULLS FIRST'
        test_188: Test = Test()
        try:
            q_1859: 'Query' = from_(_sid('users')).order_by_nulls(_sid('email'), True, NullsFirst())
            def fn_3787() -> 'str29':
                return 'nulls first'
            test_188.assert_(q_1859.to_sql().to_string() == 'SELECT * FROM users ORDER BY email ASC NULLS FIRST', fn_3787)
        finally:
            test_188.soft_fail_to_hard()
class TestCase225(TestCase48):
    def test___orderByNullsNullsLast__2597(self) -> None:
        'orderByNulls NULLS LAST'
        test_189: Test = Test()
        try:
            q_1861: 'Query' = from_(_sid('users')).order_by_nulls(_sid('score'), False, NullsLast())
            def fn_3786() -> 'str29':
                return 'nulls last'
            test_189.assert_(q_1861.to_sql().to_string() == 'SELECT * FROM users ORDER BY score DESC NULLS LAST', fn_3786)
        finally:
            test_189.soft_fail_to_hard()
class TestCase226(TestCase48):
    def test___mixedOrderByAndOrderByNulls__2598(self) -> None:
        'mixed orderBy and orderByNulls'
        test_190: Test = Test()
        try:
            q_1863: 'Query' = from_(_sid('users')).order_by(_sid('name'), True).order_by_nulls(_sid('email'), True, NullsFirst())
            def fn_3785() -> 'str29':
                return 'mixed order'
            test_190.assert_(q_1863.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC, email ASC NULLS FIRST', fn_3785)
        finally:
            test_190.soft_fail_to_hard()
class TestCase227(TestCase48):
    def test___crossJoin__2599(self) -> None:
        'crossJoin'
        test_191: Test = Test()
        try:
            q_1865: 'Query' = from_(_sid('users')).cross_join(_sid('colors'))
            def fn_3784() -> 'str29':
                return 'cross join'
            test_191.assert_(q_1865.to_sql().to_string() == 'SELECT * FROM users CROSS JOIN colors', fn_3784)
        finally:
            test_191.soft_fail_to_hard()
class TestCase228(TestCase48):
    def test___crossJoinCombinedWithOtherJoins__2600(self) -> None:
        'crossJoin combined with other joins'
        test_192: Test = Test()
        try:
            t_3278: 'Query' = from_(_sid('users'))
            t_3279: 'SafeIdentifier' = _sid('orders')
            accumulator_2601: 'SqlBuilder' = SqlBuilder()
            accumulator_2601.append_safe('users.id = orders.user_id')
            q_1867: 'Query' = t_3278.inner_join(t_3279, accumulator_2601.accumulated).cross_join(_sid('colors'))
            def fn_3783() -> 'str29':
                return 'cross + inner join'
            test_192.assert_(q_1867.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id CROSS JOIN colors', fn_3783)
        finally:
            test_192.soft_fail_to_hard()
class TestCase229(TestCase48):
    def test___lockForUpdate__2602(self) -> None:
        'lock FOR UPDATE'
        test_193: Test = Test()
        try:
            t_3276: 'Query' = from_(_sid('users'))
            accumulator_2603: 'SqlBuilder' = SqlBuilder()
            accumulator_2603.append_safe('id = ')
            accumulator_2603.append_int32(1)
            q_1869: 'Query' = t_3276.where(accumulator_2603.accumulated).lock(ForUpdate())
            def fn_3782() -> 'str29':
                return 'for update'
            test_193.assert_(q_1869.to_sql().to_string() == 'SELECT * FROM users WHERE id = 1 FOR UPDATE', fn_3782)
        finally:
            test_193.soft_fail_to_hard()
class TestCase230(TestCase48):
    def test___lockForShare__2604(self) -> None:
        'lock FOR SHARE'
        test_194: Test = Test()
        try:
            q_1871: 'Query' = from_(_sid('users')).select((_sid('name'),)).lock(ForShare())
            def fn_3781() -> 'str29':
                return 'for share'
            test_194.assert_(q_1871.to_sql().to_string() == 'SELECT name FROM users FOR SHARE', fn_3781)
        finally:
            test_194.soft_fail_to_hard()
class TestCase231(TestCase48):
    def test___lockWithFullQuery__2605(self) -> None:
        'lock with full query'
        test_195: Test = Test()
        try:
            t_3273: 'Query' = from_(_sid('accounts'))
            accumulator_2606: 'SqlBuilder' = SqlBuilder()
            accumulator_2606.append_safe('id = ')
            accumulator_2606.append_int32(42)
            t_3696: 'Query' = t_3273.where(accumulator_2606.accumulated).limit(1)
            q_1873: 'Query' = t_3696.lock(ForUpdate())
            def fn_3780() -> 'str29':
                return 'lock full query'
            test_195.assert_(q_1873.to_sql().to_string() == 'SELECT * FROM accounts WHERE id = 42 LIMIT 1 FOR UPDATE', fn_3780)
        finally:
            test_195.soft_fail_to_hard()
class TestCase232(TestCase48):
    def test___queryBuilderImmutabilityTwoQueriesFromSameBase__2607(self) -> None:
        'query builder immutability - two queries from same base'
        test_196: Test = Test()
        try:
            t_3269: 'Query' = from_(_sid('users'))
            accumulator_2608: 'SqlBuilder' = SqlBuilder()
            accumulator_2608.append_safe('active = ')
            accumulator_2608.append_boolean(True)
            base_1875: 'Query' = t_3269.where(accumulator_2608.accumulated)
            q1_1876: 'Query' = base_1875.limit(10)
            q2_1877: 'Query' = base_1875.limit(20)
            def fn_3779() -> 'str29':
                return 'q1'
            test_196.assert_(q1_1876.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE LIMIT 10', fn_3779)
            def fn_3778() -> 'str29':
                return 'q2'
            test_196.assert_(q2_1877.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE LIMIT 20', fn_3778)
        finally:
            test_196.soft_fail_to_hard()
class TestCase233(TestCase48):
    def test___limitZeroProducesLimit0__2609(self) -> None:
        'limit zero produces LIMIT 0'
        test_197: Test = Test()
        try:
            q_1879: 'Query' = from_(_sid('users')).limit(0)
            def fn_3777() -> 'str29':
                return 'limit 0'
            test_197.assert_(q_1879.to_sql().to_string() == 'SELECT * FROM users LIMIT 0', fn_3777)
        finally:
            test_197.soft_fail_to_hard()
class TestCase234(TestCase48):
    def test___safeToSqlWithZeroDefaultLimit__2610(self) -> None:
        'safeToSql with zero defaultLimit'
        test_198: Test = Test()
        try:
            q_1881: 'Query' = from_(_sid('users'))
            s_1882: 'SqlFragment' = q_1881.safe_to_sql(0)
            def fn_3776() -> 'str29':
                return 'safeToSql 0'
            test_198.assert_(s_1882.to_string() == 'SELECT * FROM users LIMIT 0', fn_3776)
        finally:
            test_198.soft_fail_to_hard()
class TestCase235(TestCase48):
    def test___updateQueryLimitBubblesOnNegative__2611(self) -> None:
        'UpdateQuery limit bubbles on negative'
        test_199: Test = Test()
        try:
            did_bubble_1884: 'bool37'
            try:
                t_3264: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('x'))
                accumulator_2612: 'SqlBuilder' = SqlBuilder()
                accumulator_2612.append_safe('id = ')
                accumulator_2612.append_int32(1)
                t_3264.where(accumulator_2612.accumulated).limit(-1)
                did_bubble_1884 = False
            except Exception41:
                did_bubble_1884 = True
            def fn_3775() -> 'str29':
                return 'UpdateQuery negative limit should bubble'
            test_199.assert_(did_bubble_1884, fn_3775)
        finally:
            test_199.soft_fail_to_hard()
class TestCase236(TestCase48):
    def test___deleteQueryLimitBubblesOnNegative__2613(self) -> None:
        'DeleteQuery limit bubbles on negative'
        test_200: Test = Test()
        try:
            did_bubble_1886: 'bool37'
            try:
                t_3261: 'DeleteQuery' = delete_from(_sid('users'))
                accumulator_2614: 'SqlBuilder' = SqlBuilder()
                accumulator_2614.append_safe('id = ')
                accumulator_2614.append_int32(1)
                t_3261.where(accumulator_2614.accumulated).limit(-1)
                did_bubble_1886 = False
            except Exception41:
                did_bubble_1886 = True
            def fn_3774() -> 'str29':
                return 'DeleteQuery negative limit should bubble'
            test_200.assert_(did_bubble_1886, fn_3774)
        finally:
            test_200.soft_fail_to_hard()
class TestCase237(TestCase48):
    def test___updateQueryImmutabilityTwoFromSameBase__2615(self) -> None:
        'UpdateQuery immutability - two from same base'
        test_201: Test = Test()
        try:
            t_3251: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('Alice'))
            accumulator_2616: 'SqlBuilder' = SqlBuilder()
            accumulator_2616.append_safe('id = ')
            accumulator_2616.append_int32(1)
            base_1888: 'UpdateQuery' = t_3251.where(accumulator_2616.accumulated)
            q1_1889: 'UpdateQuery' = base_1888.set(_sid('age'), SqlInt32(25))
            q2_1890: 'UpdateQuery' = base_1888.set(_sid('age'), SqlInt32(30))
            t_3252: 'SqlFragment' = q1_1889.to_sql()
            s1_1891: 'str29' = t_3252.to_string()
            t_3253: 'SqlFragment' = q2_1890.to_sql()
            s2_1892: 'str29' = t_3253.to_string()
            t_3254: 'bool37' = s1_1891.find('25') >= 0
            def fn_3773() -> 'str29':
                return _str_cat_4031('q1 should have 25: ', s1_1891)
            test_201.assert_(t_3254, fn_3773)
            t_3256: 'bool37' = s2_1892.find('30') >= 0
            def fn_3772() -> 'str29':
                return _str_cat_4031('q2 should have 30: ', s2_1892)
            test_201.assert_(t_3256, fn_3772)
            t_3258: 'bool37' = s1_1891.find('30') >= 0
            def fn_3771() -> 'str29':
                return _str_cat_4031('q1 should NOT have 30: ', s1_1891)
            test_201.assert_(not t_3258, fn_3771)
        finally:
            test_201.soft_fail_to_hard()
class TestCase238(TestCase48):
    def test___deleteQueryImmutability__2617(self) -> None:
        'DeleteQuery immutability'
        test_202: Test = Test()
        try:
            t_3236: 'DeleteQuery' = delete_from(_sid('users'))
            accumulator_2618: 'SqlBuilder' = SqlBuilder()
            accumulator_2618.append_safe('active = ')
            accumulator_2618.append_boolean(False)
            base_1894: 'DeleteQuery' = t_3236.where(accumulator_2618.accumulated)
            accumulator_2619: 'SqlBuilder' = SqlBuilder()
            accumulator_2619.append_safe('age < ')
            accumulator_2619.append_int32(18)
            q1_1895: 'DeleteQuery' = base_1894.where(accumulator_2619.accumulated)
            accumulator_2620: 'SqlBuilder' = SqlBuilder()
            accumulator_2620.append_safe('age > ')
            accumulator_2620.append_int32(65)
            q2_1896: 'DeleteQuery' = base_1894.where(accumulator_2620.accumulated)
            t_3239: 'SqlFragment' = q1_1895.to_sql()
            s1_1897: 'str29' = t_3239.to_string()
            t_3240: 'SqlFragment' = q2_1896.to_sql()
            s2_1898: 'str29' = t_3240.to_string()
            t_3241: 'bool37' = s1_1897.find('age < 18') >= 0
            def fn_3770() -> 'str29':
                return _str_cat_4031('q1: ', s1_1897)
            test_202.assert_(t_3241, fn_3770)
            t_3243: 'bool37' = s2_1898.find('age > 65') >= 0
            def fn_3769() -> 'str29':
                return _str_cat_4031('q2: ', s2_1898)
            test_202.assert_(t_3243, fn_3769)
            t_3245: 'bool37' = s1_1897.find('age > 65') >= 0
            def fn_3768() -> 'str29':
                return _str_cat_4031('q1 should not have q2 condition: ', s1_1897)
            test_202.assert_(not t_3245, fn_3768)
        finally:
            test_202.soft_fail_to_hard()
class TestCase239(TestCase48):
    def test___safeIdentifierAcceptsValidNames__2621(self) -> None:
        'safeIdentifier accepts valid names'
        test_203: Test = Test()
        try:
            id_1946: 'SafeIdentifier' = safe_identifier('user_name')
            def fn_3767() -> 'str29':
                return 'value should round-trip'
            test_203.assert_(id_1946.sql_value == 'user_name', fn_3767)
        finally:
            test_203.soft_fail_to_hard()
class TestCase240(TestCase48):
    def test___safeIdentifierRejectsEmptyString__2622(self) -> None:
        'safeIdentifier rejects empty string'
        test_204: Test = Test()
        try:
            did_bubble_1948: 'bool37'
            try:
                safe_identifier('')
                did_bubble_1948 = False
            except Exception41:
                did_bubble_1948 = True
            def fn_3766() -> 'str29':
                return 'empty string should bubble'
            test_204.assert_(did_bubble_1948, fn_3766)
        finally:
            test_204.soft_fail_to_hard()
class TestCase241(TestCase48):
    def test___safeIdentifierRejectsLeadingDigit__2623(self) -> None:
        'safeIdentifier rejects leading digit'
        test_205: Test = Test()
        try:
            did_bubble_1950: 'bool37'
            try:
                safe_identifier('1col')
                did_bubble_1950 = False
            except Exception41:
                did_bubble_1950 = True
            def fn_3765() -> 'str29':
                return 'leading digit should bubble'
            test_205.assert_(did_bubble_1950, fn_3765)
        finally:
            test_205.soft_fail_to_hard()
class TestCase242(TestCase48):
    def test___safeIdentifierRejectsSqlMetacharacters__2624(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_206: Test = Test()
        try:
            cases_1952: 'Sequence33[str29]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            this_3691: 'Sequence33[str29]' = cases_1952
            n_3693: 'int35' = _len_4022(this_3691)
            i_3694: 'int35' = 0
            while i_3694 < n_3693:
                el_3695: 'str29' = _list_get_4023(this_3691, i_3694)
                i_3694 = _int_add_4024(i_3694, 1)
                c_1953: 'str29' = el_3695
                did_bubble_1954: 'bool37'
                try:
                    safe_identifier(c_1953)
                    did_bubble_1954 = False
                except Exception41:
                    did_bubble_1954 = True
                def fn_3764() -> 'str29':
                    return _str_cat_4031('should reject: ', c_1953)
                test_206.assert_(did_bubble_1954, fn_3764)
        finally:
            test_206.soft_fail_to_hard()
class TestCase243(TestCase48):
    def test___tableDefFieldLookupFound__2625(self) -> None:
        'TableDef field lookup - found'
        test_207: Test = Test()
        try:
            t_3224: 'SafeIdentifier' = safe_identifier('users')
            t_3225: 'SafeIdentifier' = safe_identifier('name')
            t_3226: 'SafeIdentifier' = safe_identifier('age')
            td_1956: 'TableDef' = TableDef(t_3224, (FieldDef(t_3225, StringField(), False, None, False), FieldDef(t_3226, IntField(), False, None, False)), None)
            f_1957: 'FieldDef' = td_1956.field('age')
            def fn_3763() -> 'str29':
                return 'should find age field'
            test_207.assert_(f_1957.name.sql_value == 'age', fn_3763)
        finally:
            test_207.soft_fail_to_hard()
class TestCase244(TestCase48):
    def test___tableDefFieldLookupNotFoundBubbles__2626(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_208: Test = Test()
        try:
            t_3221: 'SafeIdentifier' = safe_identifier('users')
            t_3222: 'SafeIdentifier' = safe_identifier('name')
            td_1959: 'TableDef' = TableDef(t_3221, (FieldDef(t_3222, StringField(), False, None, False),), None)
            did_bubble_1960: 'bool37'
            try:
                td_1959.field('nonexistent')
                did_bubble_1960 = False
            except Exception41:
                did_bubble_1960 = True
            def fn_3762() -> 'str29':
                return 'unknown field should bubble'
            test_208.assert_(did_bubble_1960, fn_3762)
        finally:
            test_208.soft_fail_to_hard()
class TestCase245(TestCase48):
    def test___fieldDefNullableFlag__2627(self) -> None:
        'FieldDef nullable flag'
        test_209: Test = Test()
        try:
            t_3219: 'SafeIdentifier' = safe_identifier('email')
            required_1962: 'FieldDef' = FieldDef(t_3219, StringField(), False, None, False)
            t_3220: 'SafeIdentifier' = safe_identifier('bio')
            optional_1963: 'FieldDef' = FieldDef(t_3220, StringField(), True, None, False)
            def fn_3761() -> 'str29':
                return 'required field should not be nullable'
            test_209.assert_(not required_1962.nullable, fn_3761)
            def fn_3760() -> 'str29':
                return 'optional field should be nullable'
            test_209.assert_(optional_1963.nullable, fn_3760)
        finally:
            test_209.soft_fail_to_hard()
class TestCase246(TestCase48):
    def test___pkNameDefaultsToIdWhenPrimaryKeyIsNull__2628(self) -> None:
        'pkName defaults to id when primaryKey is null'
        test_210: Test = Test()
        try:
            t_3217: 'SafeIdentifier' = safe_identifier('users')
            t_3218: 'SafeIdentifier' = safe_identifier('name')
            td_1965: 'TableDef' = TableDef(t_3217, (FieldDef(t_3218, StringField(), False, None, False),), None)
            def fn_3759() -> 'str29':
                return 'default pk should be id'
            test_210.assert_(td_1965.pk_name() == 'id', fn_3759)
        finally:
            test_210.soft_fail_to_hard()
class TestCase247(TestCase48):
    def test___pkNameReturnsCustomPrimaryKey__2629(self) -> None:
        'pkName returns custom primary key'
        test_211: Test = Test()
        try:
            t_3213: 'SafeIdentifier' = safe_identifier('users')
            t_3214: 'SafeIdentifier' = safe_identifier('user_id')
            t_3216: 'Sequence33[FieldDef]' = (FieldDef(t_3214, IntField(), False, None, False),)
            t_3215: 'SafeIdentifier' = safe_identifier('user_id')
            td_1967: 'TableDef' = TableDef(t_3213, t_3216, t_3215)
            def fn_3758() -> 'str29':
                return 'custom pk should be user_id'
            test_211.assert_(td_1967.pk_name() == 'user_id', fn_3758)
        finally:
            test_211.soft_fail_to_hard()
class TestCase248(TestCase48):
    def test___timestampsReturnsTwoDateFieldDefs__2630(self) -> None:
        'timestamps returns two DateField defs'
        test_212: Test = Test()
        try:
            ts_1969: 'Sequence33[FieldDef]' = timestamps()
            def fn_3757() -> 'str29':
                return 'should return 2 fields'
            test_212.assert_(_len_4022(ts_1969) == 2, fn_3757)
            def fn_3756() -> 'str29':
                return 'first should be inserted_at'
            test_212.assert_(_list_get_4023(ts_1969, 0).name.sql_value == 'inserted_at', fn_3756)
            def fn_3755() -> 'str29':
                return 'second should be updated_at'
            test_212.assert_(_list_get_4023(ts_1969, 1).name.sql_value == 'updated_at', fn_3755)
            def fn_3754() -> 'str29':
                return 'inserted_at should be nullable'
            test_212.assert_(_list_get_4023(ts_1969, 0).nullable, fn_3754)
            def fn_3753() -> 'str29':
                return 'updated_at should be nullable'
            test_212.assert_(_list_get_4023(ts_1969, 1).nullable, fn_3753)
            def fn_3752() -> 'str29':
                return 'inserted_at should have default'
            test_212.assert_(not _list_get_4023(ts_1969, 0).default_value is None, fn_3752)
            def fn_3751() -> 'str29':
                return 'updated_at should have default'
            test_212.assert_(not _list_get_4023(ts_1969, 1).default_value is None, fn_3751)
        finally:
            test_212.soft_fail_to_hard()
class TestCase249(TestCase48):
    def test___fieldDefDefaultValueField__2631(self) -> None:
        'FieldDef defaultValue field'
        test_213: Test = Test()
        try:
            t_3210: 'SafeIdentifier' = safe_identifier('status')
            with_default_1971: 'FieldDef' = FieldDef(t_3210, StringField(), False, SqlDefault(), False)
            t_3211: 'SafeIdentifier' = safe_identifier('name')
            without_default_1972: 'FieldDef' = FieldDef(t_3211, StringField(), False, None, False)
            def fn_3750() -> 'str29':
                return 'should have default'
            test_213.assert_(not with_default_1971.default_value is None, fn_3750)
            def fn_3749() -> 'str29':
                return 'should not have default'
            test_213.assert_(without_default_1972.default_value is None, fn_3749)
        finally:
            test_213.soft_fail_to_hard()
class TestCase250(TestCase48):
    def test___fieldDefVirtualFlag__2632(self) -> None:
        'FieldDef virtual flag'
        test_214: Test = Test()
        try:
            t_3208: 'SafeIdentifier' = safe_identifier('name')
            normal_1974: 'FieldDef' = FieldDef(t_3208, StringField(), False, None, False)
            t_3209: 'SafeIdentifier' = safe_identifier('full_name')
            virt_1975: 'FieldDef' = FieldDef(t_3209, StringField(), True, None, True)
            def fn_3748() -> 'str29':
                return 'normal field should not be virtual'
            test_214.assert_(not normal_1974.virtual, fn_3748)
            def fn_3747() -> 'str29':
                return 'virtual field should be virtual'
            test_214.assert_(virt_1975.virtual, fn_3747)
        finally:
            test_214.soft_fail_to_hard()
class TestCase251(TestCase48):
    def test___safeIdentifierAcceptsSingleCharacterNames__2633(self) -> None:
        'safeIdentifier accepts single character names'
        test_215: Test = Test()
        try:
            a_1977: 'SafeIdentifier' = safe_identifier('a')
            def fn_3746() -> 'str29':
                return 'single letter should work'
            test_215.assert_(a_1977.sql_value == 'a', fn_3746)
            u_1978: 'SafeIdentifier' = safe_identifier('_')
            def fn_3745() -> 'str29':
                return 'single underscore should work'
            test_215.assert_(u_1978.sql_value == '_', fn_3745)
        finally:
            test_215.soft_fail_to_hard()
class TestCase252(TestCase48):
    def test___safeIdentifierAcceptsAllUnderscoreNames__2634(self) -> None:
        'safeIdentifier accepts all-underscore names'
        test_216: Test = Test()
        try:
            id_1980: 'SafeIdentifier' = safe_identifier('___')
            def fn_3744() -> 'str29':
                return 'all underscores should work'
            test_216.assert_(id_1980.sql_value == '___', fn_3744)
        finally:
            test_216.soft_fail_to_hard()
class TestCase253(TestCase48):
    def test___tableDefWithEmptyFieldList__2635(self) -> None:
        'TableDef with empty field list'
        test_217: Test = Test()
        try:
            t_3203: 'SafeIdentifier' = safe_identifier('empty')
            tbl_1982: 'TableDef' = TableDef(t_3203, (), None)
            did_bubble_1983: 'bool37'
            try:
                tbl_1982.field('anything')
                did_bubble_1983 = False
            except Exception41:
                did_bubble_1983 = True
            def fn_3743() -> 'str29':
                return 'field lookup on empty table should bubble'
            test_217.assert_(did_bubble_1983, fn_3743)
        finally:
            test_217.soft_fail_to_hard()
class TestCase254(TestCase48):
    def test___stringEscaping__2636(self) -> None:
        'string escaping'
        test_219: Test = Test()
        try:
            def build_2113(name_2115: 'str29', /) -> 'str29':
                accumulator_2637: 'SqlBuilder' = SqlBuilder()
                accumulator_2637.append_safe('select * from hi where name = ')
                accumulator_2637.append_string(name_2115)
                return accumulator_2637.accumulated.to_string()
            def build_wrong_2114(name_2117: 'str29', /) -> 'str29':
                return _str_cat_4031("select * from hi where name = '", name_2117, "'")
            def fn_3742() -> 'str29':
                return "expected build(\"world\") == (select * from hi where name = 'world') not (select * from hi where name = 'world')"
            test_219.assert_(True, fn_3742)
            bobby_tables_2119: 'str29' = "Robert'); drop table hi;--"
            def fn_3741() -> 'str29':
                return "expected build(bobbyTables) == (select * from hi where name = 'Robert''); drop table hi;--') not (select * from hi where name = 'Robert''); drop table hi;--')"
            test_219.assert_(True, fn_3741)
            def fn_3740() -> 'str29':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_219.assert_(True, fn_3740)
        finally:
            test_219.soft_fail_to_hard()
class TestCase255(TestCase48):
    def test___stringEdgeCases__2644(self) -> None:
        'string edge cases'
        test_220: Test = Test()
        try:
            accumulator_2647: 'SqlBuilder' = SqlBuilder()
            accumulator_2647.append_safe('v = ')
            accumulator_2647.append_string('')
            actual_2645: 'str29' = accumulator_2647.accumulated.to_string()
            def fn_3739() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_2645, ')')
            test_220.assert_(actual_2645 == "v = ''", fn_3739)
            accumulator_2650: 'SqlBuilder' = SqlBuilder()
            accumulator_2650.append_safe('v = ')
            accumulator_2650.append_string("a''b")
            actual_2648: 'str29' = accumulator_2650.accumulated.to_string()
            def fn_3738() -> 'str29':
                return _str_cat_4031("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_2648, ')')
            test_220.assert_(actual_2648 == "v = 'a''''b'", fn_3738)
            accumulator_2653: 'SqlBuilder' = SqlBuilder()
            accumulator_2653.append_safe('v = ')
            accumulator_2653.append_string('Hello \u4e16\u754c')
            actual_2651: 'str29' = accumulator_2653.accumulated.to_string()
            def fn_3737() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_2651, ')')
            test_220.assert_(actual_2651 == "v = 'Hello \u4e16\u754c'", fn_3737)
            accumulator_2656: 'SqlBuilder' = SqlBuilder()
            accumulator_2656.append_safe('v = ')
            accumulator_2656.append_string('Line1\nLine2')
            actual_2654: 'str29' = accumulator_2656.accumulated.to_string()
            def fn_3736() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_2654, ')')
            test_220.assert_(actual_2654 == "v = 'Line1\nLine2'", fn_3736)
        finally:
            test_220.soft_fail_to_hard()
class TestCase256(TestCase48):
    def test___numbersAndBooleans__2657(self) -> None:
        'numbers and booleans'
        test_221: Test = Test()
        try:
            accumulator_2660: 'SqlBuilder' = SqlBuilder()
            accumulator_2660.append_safe('select ')
            accumulator_2660.append_int32(42)
            accumulator_2660.append_safe(', ')
            accumulator_2660.append_int64(43)
            accumulator_2660.append_safe(', ')
            accumulator_2660.append_float64(19.99)
            accumulator_2660.append_safe(', ')
            accumulator_2660.append_boolean(True)
            accumulator_2660.append_safe(', ')
            accumulator_2660.append_boolean(False)
            actual_2658: 'str29' = accumulator_2660.accumulated.to_string()
            def fn_3735() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_2658, ')')
            test_221.assert_(actual_2658 == 'select 42, 43, 19.99, TRUE, FALSE', fn_3735)
            date_2122: 'date28' = _date_4057(2024, 12, 25)
            accumulator_2663: 'SqlBuilder' = SqlBuilder()
            accumulator_2663.append_safe('insert into t values (')
            accumulator_2663.append_date(date_2122)
            accumulator_2663.append_safe(')')
            actual_2661: 'str29' = accumulator_2663.accumulated.to_string()
            def fn_3734() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_2661, ')')
            test_221.assert_(actual_2661 == "insert into t values ('2024-12-25')", fn_3734)
        finally:
            test_221.soft_fail_to_hard()
class TestCase257(TestCase48):
    def test___lists__2664(self) -> None:
        'lists'
        test_222: Test = Test()
        try:
            accumulator_2667: 'SqlBuilder' = SqlBuilder()
            accumulator_2667.append_safe('v IN (')
            accumulator_2667.append_string_list(('a', 'b', "c'd"))
            accumulator_2667.append_safe(')')
            actual_2665: 'str29' = accumulator_2667.accumulated.to_string()
            def fn_3733() -> 'str29':
                return _str_cat_4031("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_2665, ')')
            test_222.assert_(actual_2665 == "v IN ('a', 'b', 'c''d')", fn_3733)
            accumulator_2670: 'SqlBuilder' = SqlBuilder()
            accumulator_2670.append_safe('v IN (')
            accumulator_2670.append_int32_list((1, 2, 3))
            accumulator_2670.append_safe(')')
            actual_2668: 'str29' = accumulator_2670.accumulated.to_string()
            def fn_3732() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_2668, ')')
            test_222.assert_(actual_2668 == 'v IN (1, 2, 3)', fn_3732)
            accumulator_2673: 'SqlBuilder' = SqlBuilder()
            accumulator_2673.append_safe('v IN (')
            accumulator_2673.append_int64_list((1, 2))
            accumulator_2673.append_safe(')')
            actual_2671: 'str29' = accumulator_2673.accumulated.to_string()
            def fn_3731() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_2671, ')')
            test_222.assert_(actual_2671 == 'v IN (1, 2)', fn_3731)
            accumulator_2676: 'SqlBuilder' = SqlBuilder()
            accumulator_2676.append_safe('v IN (')
            accumulator_2676.append_float64_list((1.0, 2.0))
            accumulator_2676.append_safe(')')
            actual_2674: 'str29' = accumulator_2676.accumulated.to_string()
            def fn_3730() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_2674, ')')
            test_222.assert_(actual_2674 == 'v IN (1.0, 2.0)', fn_3730)
            accumulator_2679: 'SqlBuilder' = SqlBuilder()
            accumulator_2679.append_safe('v IN (')
            accumulator_2679.append_boolean_list((True, False))
            accumulator_2679.append_safe(')')
            actual_2677: 'str29' = accumulator_2679.accumulated.to_string()
            def fn_3729() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_2677, ')')
            test_222.assert_(actual_2677 == 'v IN (TRUE, FALSE)', fn_3729)
            t_3192: 'date28' = _date_4057(2024, 1, 1)
            t_3193: 'date28' = _date_4057(2024, 12, 25)
            dates_2124: 'Sequence33[date28]' = (t_3192, t_3193)
            accumulator_2682: 'SqlBuilder' = SqlBuilder()
            accumulator_2682.append_safe('v IN (')
            accumulator_2682.append_date_list(dates_2124)
            accumulator_2682.append_safe(')')
            actual_2680: 'str29' = accumulator_2682.accumulated.to_string()
            def fn_3728() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_2680, ')')
            test_222.assert_(actual_2680 == "v IN ('2024-01-01', '2024-12-25')", fn_3728)
        finally:
            test_222.soft_fail_to_hard()
class TestCase258(TestCase48):
    def test___sqlFloat64_naNRendersAsNull__2683(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_223: Test = Test()
        try:
            nan_2126: 'float31' = nan259
            accumulator_2686: 'SqlBuilder' = SqlBuilder()
            accumulator_2686.append_safe('v = ')
            accumulator_2686.append_float64(nan259)
            actual_2684: 'str29' = accumulator_2686.accumulated.to_string()
            def fn_3727() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_2684, ')')
            test_223.assert_(actual_2684 == 'v = NULL', fn_3727)
        finally:
            test_223.soft_fail_to_hard()
class TestCase260(TestCase48):
    def test___sqlFloat64_infinityRendersAsNull__2687(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_224: Test = Test()
        try:
            inf_2128: 'float31' = inf261
            accumulator_2690: 'SqlBuilder' = SqlBuilder()
            accumulator_2690.append_safe('v = ')
            accumulator_2690.append_float64(inf261)
            actual_2688: 'str29' = accumulator_2690.accumulated.to_string()
            def fn_3726() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_2688, ')')
            test_224.assert_(actual_2688 == 'v = NULL', fn_3726)
        finally:
            test_224.soft_fail_to_hard()
class TestCase262(TestCase48):
    def test___sqlFloat64_negativeInfinityRendersAsNull__2691(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_225: Test = Test()
        try:
            ninf_2130: 'float31' = -inf261
            accumulator_2694: 'SqlBuilder' = SqlBuilder()
            accumulator_2694.append_safe('v = ')
            accumulator_2694.append_float64(-inf261)
            actual_2692: 'str29' = accumulator_2694.accumulated.to_string()
            def fn_3725() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_2692, ')')
            test_225.assert_(actual_2692 == 'v = NULL', fn_3725)
        finally:
            test_225.soft_fail_to_hard()
class TestCase263(TestCase48):
    def test___sqlFloat64_normalValuesStillWork__2695(self) -> None:
        'SqlFloat64 normal values still work'
        test_226: Test = Test()
        try:
            accumulator_2698: 'SqlBuilder' = SqlBuilder()
            accumulator_2698.append_safe('v = ')
            accumulator_2698.append_float64(3.14)
            actual_2696: 'str29' = accumulator_2698.accumulated.to_string()
            def fn_3724() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_2696, ')')
            test_226.assert_(actual_2696 == 'v = 3.14', fn_3724)
            accumulator_2701: 'SqlBuilder' = SqlBuilder()
            accumulator_2701.append_safe('v = ')
            accumulator_2701.append_float64(0.0)
            actual_2699: 'str29' = accumulator_2701.accumulated.to_string()
            def fn_3723() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_2699, ')')
            test_226.assert_(actual_2699 == 'v = 0.0', fn_3723)
            accumulator_2704: 'SqlBuilder' = SqlBuilder()
            accumulator_2704.append_safe('v = ')
            accumulator_2704.append_float64(-42.5)
            actual_2702: 'str29' = accumulator_2704.accumulated.to_string()
            def fn_3722() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_2702, ')')
            test_226.assert_(actual_2702 == 'v = -42.5', fn_3722)
        finally:
            test_226.soft_fail_to_hard()
class TestCase264(TestCase48):
    def test___sqlDateRendersWithQuotes__2705(self) -> None:
        'SqlDate renders with quotes'
        test_227: Test = Test()
        try:
            d_2133: 'date28' = _date_4057(2024, 6, 15)
            accumulator_2708: 'SqlBuilder' = SqlBuilder()
            accumulator_2708.append_safe('v = ')
            accumulator_2708.append_date(d_2133)
            actual_2706: 'str29' = accumulator_2708.accumulated.to_string()
            def fn_3721() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_2706, ')')
            test_227.assert_(actual_2706 == "v = '2024-06-15'", fn_3721)
        finally:
            test_227.soft_fail_to_hard()
class TestCase265(TestCase48):
    def test___nesting__2709(self) -> None:
        'nesting'
        test_228: Test = Test()
        try:
            name_2135: 'str29' = 'Someone'
            accumulator_2710: 'SqlBuilder' = SqlBuilder()
            accumulator_2710.append_safe('where p.last_name = ')
            accumulator_2710.append_string('Someone')
            condition_2136: 'SqlFragment' = accumulator_2710.accumulated
            accumulator_2713: 'SqlBuilder' = SqlBuilder()
            accumulator_2713.append_safe('select p.id from person p ')
            accumulator_2713.append_fragment(condition_2136)
            actual_2711: 'str29' = accumulator_2713.accumulated.to_string()
            def fn_3720() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2711, ')')
            test_228.assert_(actual_2711 == "select p.id from person p where p.last_name = 'Someone'", fn_3720)
            accumulator_2716: 'SqlBuilder' = SqlBuilder()
            accumulator_2716.append_safe('select p.id from person p ')
            accumulator_2716.append_part(condition_2136.to_source())
            actual_2714: 'str29' = accumulator_2716.accumulated.to_string()
            def fn_3719() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2714, ')')
            test_228.assert_(actual_2714 == "select p.id from person p where p.last_name = 'Someone'", fn_3719)
            parts_2137: 'Sequence33[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            accumulator_2719: 'SqlBuilder' = SqlBuilder()
            accumulator_2719.append_safe('select ')
            accumulator_2719.append_part_list(parts_2137)
            actual_2717: 'str29' = accumulator_2719.accumulated.to_string()
            def fn_3718() -> 'str29':
                return _str_cat_4031('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_2717, ')')
            test_228.assert_(actual_2717 == "select 'a''b', 3", fn_3718)
        finally:
            test_228.soft_fail_to_hard()
class TestCase266(TestCase48):
    def test___sqlInt32_negativeAndZeroValues__2720(self) -> None:
        'SqlInt32 negative and zero values'
        test_229: Test = Test()
        try:
            accumulator_2721: 'SqlBuilder' = SqlBuilder()
            accumulator_2721.append_safe('v = ')
            accumulator_2721.append_int32(-42)
            t_3173: 'SqlFragment' = accumulator_2721.accumulated
            def fn_3717() -> 'str29':
                return 'negative int'
            test_229.assert_(t_3173.to_string() == 'v = -42', fn_3717)
            accumulator_2722: 'SqlBuilder' = SqlBuilder()
            accumulator_2722.append_safe('v = ')
            accumulator_2722.append_int32(0)
            t_3174: 'SqlFragment' = accumulator_2722.accumulated
            def fn_3716() -> 'str29':
                return 'zero int'
            test_229.assert_(t_3174.to_string() == 'v = 0', fn_3716)
        finally:
            test_229.soft_fail_to_hard()
class TestCase267(TestCase48):
    def test___sqlInt64_negativeValue__2723(self) -> None:
        'SqlInt64 negative value'
        test_230: Test = Test()
        try:
            accumulator_2724: 'SqlBuilder' = SqlBuilder()
            accumulator_2724.append_safe('v = ')
            accumulator_2724.append_int64(-99)
            t_3172: 'SqlFragment' = accumulator_2724.accumulated
            def fn_3715() -> 'str29':
                return 'negative int64'
            test_230.assert_(t_3172.to_string() == 'v = -99', fn_3715)
        finally:
            test_230.soft_fail_to_hard()
class TestCase268(TestCase48):
    def test___singleElementListRendering__2725(self) -> None:
        'single element list rendering'
        test_231: Test = Test()
        try:
            accumulator_2726: 'SqlBuilder' = SqlBuilder()
            accumulator_2726.append_safe('v IN (')
            accumulator_2726.append_int32_list((42,))
            accumulator_2726.append_safe(')')
            t_3170: 'SqlFragment' = accumulator_2726.accumulated
            def fn_3714() -> 'str29':
                return 'single int'
            test_231.assert_(t_3170.to_string() == 'v IN (42)', fn_3714)
            accumulator_2727: 'SqlBuilder' = SqlBuilder()
            accumulator_2727.append_safe('v IN (')
            accumulator_2727.append_string_list(('only',))
            accumulator_2727.append_safe(')')
            t_3171: 'SqlFragment' = accumulator_2727.accumulated
            def fn_3713() -> 'str29':
                return 'single string'
            test_231.assert_(t_3171.to_string() == "v IN ('only')", fn_3713)
        finally:
            test_231.soft_fail_to_hard()
class TestCase269(TestCase48):
    def test___sqlDefaultRendersDefaultKeyword__2728(self) -> None:
        'SqlDefault renders DEFAULT keyword'
        test_232: Test = Test()
        try:
            b_2142: 'SqlBuilder' = SqlBuilder()
            b_2142.append_safe('v = ')
            b_2142.append_part(SqlDefault())
            def fn_3712() -> 'str29':
                return 'default keyword'
            test_232.assert_(b_2142.accumulated.to_string() == 'v = DEFAULT', fn_3712)
        finally:
            test_232.soft_fail_to_hard()
class TestCase270(TestCase48):
    def test___sqlStringWithBackslash__2729(self) -> None:
        'SqlString with backslash'
        test_233: Test = Test()
        try:
            accumulator_2730: 'SqlBuilder' = SqlBuilder()
            accumulator_2730.append_safe('v = ')
            accumulator_2730.append_string('a\\b')
            t_3169: 'SqlFragment' = accumulator_2730.accumulated
            def fn_3711() -> 'str29':
                return 'backslash passthrough'
            test_233.assert_(t_3169.to_string() == "v = 'a\\b'", fn_3711)
        finally:
            test_233.soft_fail_to_hard()
