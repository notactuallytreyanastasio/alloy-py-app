from temper_std.testing import Test
from builtins import str as str29, int as int35, bool as bool37, Exception as Exception41, float as float31
from unittest import TestCase as TestCase48
from types import MappingProxyType as MappingProxyType36
from typing import Sequence as Sequence33, MutableSequence as MutableSequence38
from datetime import date as date28
from math import nan as nan259, inf as inf261
from orm.src import safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, _map_constructor_4207, _pair_4208, changeset, Changeset, _mapped_has_4181, _len_4174, _list_get_4175, _int_add_4176, _str_cat_4183, SqlFragment, NumberValidationOpts, SqlDefault, timestamps, _list_4170, _tuple_4172, delete_sql, _int_to_string_4184, Int64Field, DateField, from_, Query, SqlBuilder, SafeIdentifier, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, update, UpdateQuery, SqlBoolean, delete_from, DeleteQuery, NullsFirst, NullsLast, ForUpdate, ForShare, _date_4209, SqlPart, ParameterizedSql
def _csid(name_1019: 'str29', /) -> 'SafeIdentifier':
    return safe_identifier(name_1019)
def _user_table() -> 'TableDef':
    return TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('email'), StringField(), False, None, False), FieldDef(_csid('age'), IntField(), True, None, False), FieldDef(_csid('score'), FloatField(), True, None, False), FieldDef(_csid('active'), BoolField(), True, None, False)), None)
class TestCase47(TestCase48):
    def test___castWhitelistsAllowedFields__2375(self) -> None:
        'cast whitelists allowed fields'
        test_13: Test = Test()
        try:
            params_1023: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('email', 'alice@example.com'), _pair_4208('admin', 'true')))
            cs_1024: 'Changeset' = changeset(_user_table(), params_1023).cast((_csid('name'), _csid('email')))
            def fn_4157() -> 'str29':
                return 'name should be in changes'
            test_13.assert_(_mapped_has_4181(cs_1024.changes, 'name'), fn_4157)
            def fn_4156() -> 'str29':
                return 'email should be in changes'
            test_13.assert_(_mapped_has_4181(cs_1024.changes, 'email'), fn_4156)
            def fn_4155() -> 'str29':
                return 'admin must be dropped (not in whitelist)'
            test_13.assert_(not _mapped_has_4181(cs_1024.changes, 'admin'), fn_4155)
            def fn_4154() -> 'str29':
                return 'should still be valid'
            test_13.assert_(cs_1024.is_valid, fn_4154)
        finally:
            test_13.soft_fail_to_hard()
class TestCase49(TestCase48):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__2376(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_14: Test = Test()
        try:
            params_1026: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('email', 'alice@example.com')))
            cs_1027: 'Changeset' = changeset(_user_table(), params_1026).cast((_csid('name'),)).cast((_csid('email'),))
            def fn_4153() -> 'str29':
                return 'name must be excluded by second cast'
            test_14.assert_(not _mapped_has_4181(cs_1027.changes, 'name'), fn_4153)
            def fn_4152() -> 'str29':
                return 'email should be present'
            test_14.assert_(_mapped_has_4181(cs_1027.changes, 'email'), fn_4152)
        finally:
            test_14.soft_fail_to_hard()
class TestCase50(TestCase48):
    def test___castIgnoresEmptyStringValues__2377(self) -> None:
        'cast ignores empty string values'
        test_15: Test = Test()
        try:
            params_1029: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', ''), _pair_4208('email', 'bob@example.com')))
            cs_1030: 'Changeset' = changeset(_user_table(), params_1029).cast((_csid('name'), _csid('email')))
            def fn_4151() -> 'str29':
                return 'empty name should not be in changes'
            test_15.assert_(not _mapped_has_4181(cs_1030.changes, 'name'), fn_4151)
            def fn_4150() -> 'str29':
                return 'email should be in changes'
            test_15.assert_(_mapped_has_4181(cs_1030.changes, 'email'), fn_4150)
        finally:
            test_15.soft_fail_to_hard()
class TestCase51(TestCase48):
    def test___validateRequiredPassesWhenFieldPresent__2378(self) -> None:
        'validateRequired passes when field present'
        test_16: Test = Test()
        try:
            params_1032: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1033: 'Changeset' = changeset(_user_table(), params_1032).cast((_csid('name'),)).validate_required((_csid('name'),))
            def fn_4149() -> 'str29':
                return 'should be valid'
            test_16.assert_(cs_1033.is_valid, fn_4149)
            def fn_4148() -> 'str29':
                return 'no errors expected'
            test_16.assert_(_len_4174(cs_1033.errors) == 0, fn_4148)
        finally:
            test_16.soft_fail_to_hard()
class TestCase52(TestCase48):
    def test___validateRequiredFailsWhenFieldMissing__2379(self) -> None:
        'validateRequired fails when field missing'
        test_17: Test = Test()
        try:
            params_1035: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1036: 'Changeset' = changeset(_user_table(), params_1035).cast((_csid('name'),)).validate_required((_csid('name'),))
            def fn_4147() -> 'str29':
                return 'should be invalid'
            test_17.assert_(not cs_1036.is_valid, fn_4147)
            def fn_4146() -> 'str29':
                return 'should have one error'
            test_17.assert_(_len_4174(cs_1036.errors) == 1, fn_4146)
            def fn_4145() -> 'str29':
                return 'error should name the field'
            test_17.assert_(_list_get_4175(cs_1036.errors, 0).field == 'name', fn_4145)
        finally:
            test_17.soft_fail_to_hard()
class TestCase53(TestCase48):
    def test___validateLengthPassesWithinRange__2380(self) -> None:
        'validateLength passes within range'
        test_18: Test = Test()
        try:
            params_1038: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1039: 'Changeset' = changeset(_user_table(), params_1038).cast((_csid('name'),)).validate_length(_csid('name'), 2, 50)
            def fn_4144() -> 'str29':
                return 'should be valid'
            test_18.assert_(cs_1039.is_valid, fn_4144)
        finally:
            test_18.soft_fail_to_hard()
class TestCase54(TestCase48):
    def test___validateLengthFailsWhenTooShort__2381(self) -> None:
        'validateLength fails when too short'
        test_19: Test = Test()
        try:
            params_1041: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'A'),))
            cs_1042: 'Changeset' = changeset(_user_table(), params_1041).cast((_csid('name'),)).validate_length(_csid('name'), 2, 50)
            def fn_4143() -> 'str29':
                return 'should be invalid'
            test_19.assert_(not cs_1042.is_valid, fn_4143)
        finally:
            test_19.soft_fail_to_hard()
class TestCase55(TestCase48):
    def test___validateLengthFailsWhenTooLong__2382(self) -> None:
        'validateLength fails when too long'
        test_20: Test = Test()
        try:
            params_1044: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            cs_1045: 'Changeset' = changeset(_user_table(), params_1044).cast((_csid('name'),)).validate_length(_csid('name'), 2, 10)
            def fn_4142() -> 'str29':
                return 'should be invalid'
            test_20.assert_(not cs_1045.is_valid, fn_4142)
        finally:
            test_20.soft_fail_to_hard()
class TestCase56(TestCase48):
    def test___validateIntPassesForValidInteger__2383(self) -> None:
        'validateInt passes for valid integer'
        test_21: Test = Test()
        try:
            params_1047: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '30'),))
            cs_1048: 'Changeset' = changeset(_user_table(), params_1047).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_4141() -> 'str29':
                return 'should be valid'
            test_21.assert_(cs_1048.is_valid, fn_4141)
        finally:
            test_21.soft_fail_to_hard()
class TestCase57(TestCase48):
    def test___validateIntFailsForNonInteger__2384(self) -> None:
        'validateInt fails for non-integer'
        test_22: Test = Test()
        try:
            params_1050: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', 'not-a-number'),))
            cs_1051: 'Changeset' = changeset(_user_table(), params_1050).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_4140() -> 'str29':
                return 'should be invalid'
            test_22.assert_(not cs_1051.is_valid, fn_4140)
        finally:
            test_22.soft_fail_to_hard()
class TestCase58(TestCase48):
    def test___validateFloatPassesForValidFloat__2385(self) -> None:
        'validateFloat passes for valid float'
        test_23: Test = Test()
        try:
            params_1053: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '9.5'),))
            cs_1054: 'Changeset' = changeset(_user_table(), params_1053).cast((_csid('score'),)).validate_float(_csid('score'))
            def fn_4139() -> 'str29':
                return 'should be valid'
            test_23.assert_(cs_1054.is_valid, fn_4139)
        finally:
            test_23.soft_fail_to_hard()
class TestCase59(TestCase48):
    def test___validateInt64_passesForValid64_bitInteger__2386(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_24: Test = Test()
        try:
            params_1056: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '9999999999'),))
            cs_1057: 'Changeset' = changeset(_user_table(), params_1056).cast((_csid('age'),)).validate_int64(_csid('age'))
            def fn_4138() -> 'str29':
                return 'should be valid'
            test_24.assert_(cs_1057.is_valid, fn_4138)
        finally:
            test_24.soft_fail_to_hard()
class TestCase60(TestCase48):
    def test___validateInt64_failsForNonInteger__2387(self) -> None:
        'validateInt64 fails for non-integer'
        test_25: Test = Test()
        try:
            params_1059: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', 'not-a-number'),))
            cs_1060: 'Changeset' = changeset(_user_table(), params_1059).cast((_csid('age'),)).validate_int64(_csid('age'))
            def fn_4137() -> 'str29':
                return 'should be invalid'
            test_25.assert_(not cs_1060.is_valid, fn_4137)
        finally:
            test_25.soft_fail_to_hard()
class TestCase61(TestCase48):
    def test___validateBoolAcceptsTrue1_yesOn__2388(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_26: Test = Test()
        try:
            this_3797: 'Sequence33[str29]' = ('true', '1', 'yes', 'on')
            n_3799: 'int35' = _len_4174(this_3797)
            i_3800: 'int35' = 0
            while i_3800 < n_3799:
                el_3801: 'str29' = _list_get_4175(this_3797, i_3800)
                i_3800 = _int_add_4176(i_3800, 1)
                v_1062: 'str29' = el_3801
                params_1063: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('active', v_1062),))
                cs_1064: 'Changeset' = changeset(_user_table(), params_1063).cast((_csid('active'),)).validate_bool(_csid('active'))
                def fn_4136() -> 'str29':
                    return _str_cat_4183('should accept: ', v_1062)
                test_26.assert_(cs_1064.is_valid, fn_4136)
        finally:
            test_26.soft_fail_to_hard()
class TestCase62(TestCase48):
    def test___validateBoolAcceptsFalse0_noOff__2389(self) -> None:
        'validateBool accepts false/0/no/off'
        test_27: Test = Test()
        try:
            this_3802: 'Sequence33[str29]' = ('false', '0', 'no', 'off')
            n_3804: 'int35' = _len_4174(this_3802)
            i_3805: 'int35' = 0
            while i_3805 < n_3804:
                el_3806: 'str29' = _list_get_4175(this_3802, i_3805)
                i_3805 = _int_add_4176(i_3805, 1)
                v_1066: 'str29' = el_3806
                params_1067: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('active', v_1066),))
                cs_1068: 'Changeset' = changeset(_user_table(), params_1067).cast((_csid('active'),)).validate_bool(_csid('active'))
                def fn_4135() -> 'str29':
                    return _str_cat_4183('should accept: ', v_1066)
                test_27.assert_(cs_1068.is_valid, fn_4135)
        finally:
            test_27.soft_fail_to_hard()
class TestCase63(TestCase48):
    def test___validateBoolRejectsAmbiguousValues__2390(self) -> None:
        'validateBool rejects ambiguous values'
        test_28: Test = Test()
        try:
            this_3807: 'Sequence33[str29]' = ('TRUE', 'Yes', 'maybe', '2', 'enabled')
            n_3809: 'int35' = _len_4174(this_3807)
            i_3810: 'int35' = 0
            while i_3810 < n_3809:
                el_3811: 'str29' = _list_get_4175(this_3807, i_3810)
                i_3810 = _int_add_4176(i_3810, 1)
                v_1070: 'str29' = el_3811
                params_1071: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('active', v_1070),))
                cs_1072: 'Changeset' = changeset(_user_table(), params_1071).cast((_csid('active'),)).validate_bool(_csid('active'))
                def fn_4134() -> 'str29':
                    return _str_cat_4183('should reject ambiguous: ', v_1070)
                test_28.assert_(not cs_1072.is_valid, fn_4134)
        finally:
            test_28.soft_fail_to_hard()
class TestCase64(TestCase48):
    def test___toInsertSqlEscapesBobbyTables__2391(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_29: Test = Test()
        try:
            params_1074: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', "Robert'); DROP TABLE users;--"), _pair_4208('email', 'bobby@evil.com')))
            cs_1075: 'Changeset' = changeset(_user_table(), params_1074).cast((_csid('name'), _csid('email'))).validate_required((_csid('name'), _csid('email')))
            sql_frag_1076: 'SqlFragment' = cs_1075.to_insert_sql()
            s_1077: 'str29' = sql_frag_1076.to_string()
            t_3696: 'bool37' = s_1077.find("''") >= 0
            def fn_4133() -> 'str29':
                return _str_cat_4183('single quote must be doubled: ', s_1077)
            test_29.assert_(t_3696, fn_4133)
        finally:
            test_29.soft_fail_to_hard()
class TestCase65(TestCase48):
    def test___toInsertSqlProducesCorrectSqlForStringField__2392(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_30: Test = Test()
        try:
            params_1079: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('email', 'a@example.com')))
            cs_1080: 'Changeset' = changeset(_user_table(), params_1079).cast((_csid('name'), _csid('email'))).validate_required((_csid('name'), _csid('email')))
            sql_frag_1081: 'SqlFragment' = cs_1080.to_insert_sql()
            s_1082: 'str29' = sql_frag_1081.to_string()
            t_3690: 'bool37' = s_1082.find('INSERT INTO users') >= 0
            def fn_4132() -> 'str29':
                return _str_cat_4183('has INSERT INTO: ', s_1082)
            test_30.assert_(t_3690, fn_4132)
            t_3692: 'bool37' = s_1082.find("'Alice'") >= 0
            def fn_4131() -> 'str29':
                return _str_cat_4183('has quoted name: ', s_1082)
            test_30.assert_(t_3692, fn_4131)
        finally:
            test_30.soft_fail_to_hard()
class TestCase66(TestCase48):
    def test___toInsertSqlProducesCorrectSqlForIntField__2393(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_31: Test = Test()
        try:
            params_1084: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Bob'), _pair_4208('email', 'b@example.com'), _pair_4208('age', '25')))
            cs_1085: 'Changeset' = changeset(_user_table(), params_1084).cast((_csid('name'), _csid('email'), _csid('age'))).validate_required((_csid('name'), _csid('email')))
            sql_frag_1086: 'SqlFragment' = cs_1085.to_insert_sql()
            s_1087: 'str29' = sql_frag_1086.to_string()
            t_3685: 'bool37' = s_1087.find('25') >= 0
            def fn_4130() -> 'str29':
                return _str_cat_4183('age rendered unquoted: ', s_1087)
            test_31.assert_(t_3685, fn_4130)
        finally:
            test_31.soft_fail_to_hard()
class TestCase67(TestCase48):
    def test___toInsertSqlBubblesOnInvalidChangeset__2394(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_32: Test = Test()
        try:
            params_1089: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1090: 'Changeset' = changeset(_user_table(), params_1089).cast((_csid('name'),)).validate_required((_csid('name'),))
            did_bubble_1091: 'bool37'
            try:
                cs_1090.to_insert_sql()
                did_bubble_1091 = False
            except Exception41:
                did_bubble_1091 = True
            def fn_4129() -> 'str29':
                return 'invalid changeset should bubble'
            test_32.assert_(did_bubble_1091, fn_4129)
        finally:
            test_32.soft_fail_to_hard()
class TestCase68(TestCase48):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__2395(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_33: Test = Test()
        try:
            strict_table_1093: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False), FieldDef(_csid('body'), StringField(), True, None, False)), None)
            params_1094: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('body', 'hello'),))
            cs_1095: 'Changeset' = changeset(strict_table_1093, params_1094).cast((_csid('body'),))
            def fn_4128() -> 'str29':
                return 'changeset should appear valid (no explicit validation run)'
            test_33.assert_(cs_1095.is_valid, fn_4128)
            did_bubble_1096: 'bool37'
            try:
                cs_1095.to_insert_sql()
                did_bubble_1096 = False
            except Exception41:
                did_bubble_1096 = True
            def fn_4127() -> 'str29':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_33.assert_(did_bubble_1096, fn_4127)
        finally:
            test_33.soft_fail_to_hard()
class TestCase69(TestCase48):
    def test___toUpdateSqlProducesCorrectSql__2396(self) -> None:
        'toUpdateSql produces correct SQL'
        test_34: Test = Test()
        try:
            params_1098: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Bob'),))
            cs_1099: 'Changeset' = changeset(_user_table(), params_1098).cast((_csid('name'),)).validate_required((_csid('name'),))
            sql_frag_1100: 'SqlFragment' = cs_1099.to_update_sql(42)
            s_1101: 'str29' = sql_frag_1100.to_string()
            def fn_4126() -> 'str29':
                return _str_cat_4183('got: ', s_1101)
            test_34.assert_(s_1101 == "UPDATE users SET name = 'Bob' WHERE id = 42", fn_4126)
        finally:
            test_34.soft_fail_to_hard()
class TestCase70(TestCase48):
    def test___toUpdateSqlBubblesOnInvalidChangeset__2397(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_35: Test = Test()
        try:
            params_1103: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1104: 'Changeset' = changeset(_user_table(), params_1103).cast((_csid('name'),)).validate_required((_csid('name'),))
            did_bubble_1105: 'bool37'
            try:
                cs_1104.to_update_sql(1)
                did_bubble_1105 = False
            except Exception41:
                did_bubble_1105 = True
            def fn_4125() -> 'str29':
                return 'invalid changeset should bubble'
            test_35.assert_(did_bubble_1105, fn_4125)
        finally:
            test_35.soft_fail_to_hard()
class TestCase71(TestCase48):
    def test___putChangeAddsANewField__2398(self) -> None:
        'putChange adds a new field'
        test_36: Test = Test()
        try:
            params_1107: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1108: 'Changeset' = changeset(_user_table(), params_1107).cast((_csid('name'),)).put_change(_csid('email'), 'alice@example.com')
            def fn_4124() -> 'str29':
                return 'email should be in changes'
            test_36.assert_(_mapped_has_4181(cs_1108.changes, 'email'), fn_4124)
            def fn_4123() -> 'str29':
                return 'email value'
            test_36.assert_(cs_1108.changes.get('email', '') == 'alice@example.com', fn_4123)
        finally:
            test_36.soft_fail_to_hard()
class TestCase72(TestCase48):
    def test___putChangeOverwritesExistingField__2399(self) -> None:
        'putChange overwrites existing field'
        test_37: Test = Test()
        try:
            params_1110: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1111: 'Changeset' = changeset(_user_table(), params_1110).cast((_csid('name'),)).put_change(_csid('name'), 'Bob')
            def fn_4122() -> 'str29':
                return 'name should be overwritten'
            test_37.assert_(cs_1111.changes.get('name', '') == 'Bob', fn_4122)
        finally:
            test_37.soft_fail_to_hard()
class TestCase73(TestCase48):
    def test___putChangeValueAppearsInToInsertSql__2400(self) -> None:
        'putChange value appears in toInsertSql'
        test_38: Test = Test()
        try:
            params_1113: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('email', 'a@example.com')))
            cs_1114: 'Changeset' = changeset(_user_table(), params_1113).cast((_csid('name'), _csid('email'))).put_change(_csid('name'), 'Bob')
            t_3676: 'SqlFragment' = cs_1114.to_insert_sql()
            s_1115: 'str29' = t_3676.to_string()
            t_3677: 'bool37' = s_1115.find("'Bob'") >= 0
            def fn_4121() -> 'str29':
                return _str_cat_4183('should use putChange value: ', s_1115)
            test_38.assert_(t_3677, fn_4121)
        finally:
            test_38.soft_fail_to_hard()
class TestCase74(TestCase48):
    def test___getChangeReturnsValueForExistingField__2401(self) -> None:
        'getChange returns value for existing field'
        test_39: Test = Test()
        try:
            params_1117: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1118: 'Changeset' = changeset(_user_table(), params_1117).cast((_csid('name'),))
            val_1119: 'str29' = cs_1118.get_change(_csid('name'))
            def fn_4120() -> 'str29':
                return 'should return Alice'
            test_39.assert_(val_1119 == 'Alice', fn_4120)
        finally:
            test_39.soft_fail_to_hard()
class TestCase75(TestCase48):
    def test___getChangeBubblesOnMissingField__2402(self) -> None:
        'getChange bubbles on missing field'
        test_40: Test = Test()
        try:
            params_1121: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1122: 'Changeset' = changeset(_user_table(), params_1121).cast((_csid('name'),))
            did_bubble_1123: 'bool37'
            try:
                cs_1122.get_change(_csid('email'))
                did_bubble_1123 = False
            except Exception41:
                did_bubble_1123 = True
            def fn_4119() -> 'str29':
                return 'should bubble for missing field'
            test_40.assert_(did_bubble_1123, fn_4119)
        finally:
            test_40.soft_fail_to_hard()
class TestCase76(TestCase48):
    def test___deleteChangeRemovesField__2403(self) -> None:
        'deleteChange removes field'
        test_41: Test = Test()
        try:
            params_1125: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('email', 'a@example.com')))
            cs_1126: 'Changeset' = changeset(_user_table(), params_1125).cast((_csid('name'), _csid('email'))).delete_change(_csid('email'))
            def fn_4118() -> 'str29':
                return 'email should be removed'
            test_41.assert_(not _mapped_has_4181(cs_1126.changes, 'email'), fn_4118)
            def fn_4117() -> 'str29':
                return 'name should remain'
            test_41.assert_(_mapped_has_4181(cs_1126.changes, 'name'), fn_4117)
        finally:
            test_41.soft_fail_to_hard()
class TestCase77(TestCase48):
    def test___deleteChangeOnNonexistentFieldIsNoOp__2404(self) -> None:
        'deleteChange on nonexistent field is no-op'
        test_42: Test = Test()
        try:
            params_1128: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1129: 'Changeset' = changeset(_user_table(), params_1128).cast((_csid('name'),)).delete_change(_csid('email'))
            def fn_4116() -> 'str29':
                return 'name should still be present'
            test_42.assert_(_mapped_has_4181(cs_1129.changes, 'name'), fn_4116)
            def fn_4115() -> 'str29':
                return 'should still be valid'
            test_42.assert_(cs_1129.is_valid, fn_4115)
        finally:
            test_42.soft_fail_to_hard()
class TestCase78(TestCase48):
    def test___validateInclusionPassesWhenValueInList__2405(self) -> None:
        'validateInclusion passes when value in list'
        test_43: Test = Test()
        try:
            params_1131: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'admin'),))
            cs_1132: 'Changeset' = changeset(_user_table(), params_1131).cast((_csid('name'),)).validate_inclusion(_csid('name'), ('admin', 'user', 'guest'))
            def fn_4114() -> 'str29':
                return 'should be valid'
            test_43.assert_(cs_1132.is_valid, fn_4114)
        finally:
            test_43.soft_fail_to_hard()
class TestCase79(TestCase48):
    def test___validateInclusionFailsWhenValueNotInList__2406(self) -> None:
        'validateInclusion fails when value not in list'
        test_44: Test = Test()
        try:
            params_1134: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'hacker'),))
            cs_1135: 'Changeset' = changeset(_user_table(), params_1134).cast((_csid('name'),)).validate_inclusion(_csid('name'), ('admin', 'user', 'guest'))
            def fn_4113() -> 'str29':
                return 'should be invalid'
            test_44.assert_(not cs_1135.is_valid, fn_4113)
            def fn_4112() -> 'str29':
                return 'error on name'
            test_44.assert_(_list_get_4175(cs_1135.errors, 0).field == 'name', fn_4112)
        finally:
            test_44.soft_fail_to_hard()
class TestCase80(TestCase48):
    def test___validateInclusionSkipsWhenFieldNotInChanges__2407(self) -> None:
        'validateInclusion skips when field not in changes'
        test_45: Test = Test()
        try:
            params_1137: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1138: 'Changeset' = changeset(_user_table(), params_1137).cast((_csid('name'),)).validate_inclusion(_csid('name'), ('admin', 'user'))
            def fn_4111() -> 'str29':
                return 'should be valid when field absent'
            test_45.assert_(cs_1138.is_valid, fn_4111)
        finally:
            test_45.soft_fail_to_hard()
class TestCase81(TestCase48):
    def test___validateExclusionPassesWhenValueNotInList__2408(self) -> None:
        'validateExclusion passes when value not in list'
        test_46: Test = Test()
        try:
            params_1140: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1141: 'Changeset' = changeset(_user_table(), params_1140).cast((_csid('name'),)).validate_exclusion(_csid('name'), ('root', 'admin', 'superuser'))
            def fn_4110() -> 'str29':
                return 'should be valid'
            test_46.assert_(cs_1141.is_valid, fn_4110)
        finally:
            test_46.soft_fail_to_hard()
class TestCase82(TestCase48):
    def test___validateExclusionFailsWhenValueInList__2409(self) -> None:
        'validateExclusion fails when value in list'
        test_47: Test = Test()
        try:
            params_1143: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'admin'),))
            cs_1144: 'Changeset' = changeset(_user_table(), params_1143).cast((_csid('name'),)).validate_exclusion(_csid('name'), ('root', 'admin', 'superuser'))
            def fn_4109() -> 'str29':
                return 'should be invalid'
            test_47.assert_(not cs_1144.is_valid, fn_4109)
            def fn_4108() -> 'str29':
                return 'error on name'
            test_47.assert_(_list_get_4175(cs_1144.errors, 0).field == 'name', fn_4108)
        finally:
            test_47.soft_fail_to_hard()
class TestCase83(TestCase48):
    def test___validateExclusionSkipsWhenFieldNotInChanges__2410(self) -> None:
        'validateExclusion skips when field not in changes'
        test_48: Test = Test()
        try:
            params_1146: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1147: 'Changeset' = changeset(_user_table(), params_1146).cast((_csid('name'),)).validate_exclusion(_csid('name'), ('root', 'admin'))
            def fn_4107() -> 'str29':
                return 'should be valid when field absent'
            test_48.assert_(cs_1147.is_valid, fn_4107)
        finally:
            test_48.soft_fail_to_hard()
class TestCase84(TestCase48):
    def test___validateNumberGreaterThanPasses__2411(self) -> None:
        'validateNumber greaterThan passes'
        test_49: Test = Test()
        try:
            params_1149: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '25'),))
            cs_1150: 'Changeset' = changeset(_user_table(), params_1149).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(18.0, None, None, None, None))
            def fn_4106() -> 'str29':
                return '25 > 18 should pass'
            test_49.assert_(cs_1150.is_valid, fn_4106)
        finally:
            test_49.soft_fail_to_hard()
class TestCase85(TestCase48):
    def test___validateNumberGreaterThanFails__2412(self) -> None:
        'validateNumber greaterThan fails'
        test_50: Test = Test()
        try:
            params_1152: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '15'),))
            cs_1153: 'Changeset' = changeset(_user_table(), params_1152).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(18.0, None, None, None, None))
            def fn_4105() -> 'str29':
                return '15 > 18 should fail'
            test_50.assert_(not cs_1153.is_valid, fn_4105)
        finally:
            test_50.soft_fail_to_hard()
class TestCase86(TestCase48):
    def test___validateNumberLessThanPasses__2413(self) -> None:
        'validateNumber lessThan passes'
        test_51: Test = Test()
        try:
            params_1155: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '8.5'),))
            cs_1156: 'Changeset' = changeset(_user_table(), params_1155).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, 10.0, None, None, None))
            def fn_4104() -> 'str29':
                return '8.5 < 10 should pass'
            test_51.assert_(cs_1156.is_valid, fn_4104)
        finally:
            test_51.soft_fail_to_hard()
class TestCase87(TestCase48):
    def test___validateNumberLessThanFails__2414(self) -> None:
        'validateNumber lessThan fails'
        test_52: Test = Test()
        try:
            params_1158: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '12.0'),))
            cs_1159: 'Changeset' = changeset(_user_table(), params_1158).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, 10.0, None, None, None))
            def fn_4103() -> 'str29':
                return '12 < 10 should fail'
            test_52.assert_(not cs_1159.is_valid, fn_4103)
        finally:
            test_52.soft_fail_to_hard()
class TestCase88(TestCase48):
    def test___validateNumberGreaterThanOrEqualBoundary__2415(self) -> None:
        'validateNumber greaterThanOrEqual boundary'
        test_53: Test = Test()
        try:
            params_1161: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '18'),))
            cs_1162: 'Changeset' = changeset(_user_table(), params_1161).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(None, None, 18.0, None, None))
            def fn_4102() -> 'str29':
                return '18 >= 18 should pass'
            test_53.assert_(cs_1162.is_valid, fn_4102)
        finally:
            test_53.soft_fail_to_hard()
class TestCase89(TestCase48):
    def test___validateNumberCombinedOptions__2416(self) -> None:
        'validateNumber combined options'
        test_54: Test = Test()
        try:
            params_1164: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '5.0'),))
            cs_1165: 'Changeset' = changeset(_user_table(), params_1164).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(0.0, 10.0, None, None, None))
            def fn_4101() -> 'str29':
                return '5 > 0 and < 10 should pass'
            test_54.assert_(cs_1165.is_valid, fn_4101)
        finally:
            test_54.soft_fail_to_hard()
class TestCase90(TestCase48):
    def test___validateNumberNonNumericValue__2417(self) -> None:
        'validateNumber non-numeric value'
        test_55: Test = Test()
        try:
            params_1167: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', 'abc'),))
            cs_1168: 'Changeset' = changeset(_user_table(), params_1167).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(0.0, None, None, None, None))
            def fn_4100() -> 'str29':
                return 'non-numeric should fail'
            test_55.assert_(not cs_1168.is_valid, fn_4100)
            def fn_4099() -> 'str29':
                return 'correct error message'
            test_55.assert_(_list_get_4175(cs_1168.errors, 0).message == 'must be a number', fn_4099)
        finally:
            test_55.soft_fail_to_hard()
class TestCase91(TestCase48):
    def test___validateNumberSkipsWhenFieldNotInChanges__2418(self) -> None:
        'validateNumber skips when field not in changes'
        test_56: Test = Test()
        try:
            params_1170: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1171: 'Changeset' = changeset(_user_table(), params_1170).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(0.0, None, None, None, None))
            def fn_4098() -> 'str29':
                return 'should be valid when field absent'
            test_56.assert_(cs_1171.is_valid, fn_4098)
        finally:
            test_56.soft_fail_to_hard()
class TestCase92(TestCase48):
    def test___validateAcceptancePassesForTrueValues__2419(self) -> None:
        'validateAcceptance passes for true values'
        test_57: Test = Test()
        try:
            this_3812: 'Sequence33[str29]' = ('true', '1', 'yes', 'on')
            n_3814: 'int35' = _len_4174(this_3812)
            i_3815: 'int35' = 0
            while i_3815 < n_3814:
                el_3816: 'str29' = _list_get_4175(this_3812, i_3815)
                i_3815 = _int_add_4176(i_3815, 1)
                v_1173: 'str29' = el_3816
                params_1174: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('active', v_1173),))
                cs_1175: 'Changeset' = changeset(_user_table(), params_1174).cast((_csid('active'),)).validate_acceptance(_csid('active'))
                def fn_4097() -> 'str29':
                    return _str_cat_4183('should accept: ', v_1173)
                test_57.assert_(cs_1175.is_valid, fn_4097)
        finally:
            test_57.soft_fail_to_hard()
class TestCase93(TestCase48):
    def test___validateAcceptanceFailsForNonTrueValues__2420(self) -> None:
        'validateAcceptance fails for non-true values'
        test_58: Test = Test()
        try:
            params_1177: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('active', 'false'),))
            cs_1178: 'Changeset' = changeset(_user_table(), params_1177).cast((_csid('active'),)).validate_acceptance(_csid('active'))
            def fn_4096() -> 'str29':
                return 'false should not be accepted'
            test_58.assert_(not cs_1178.is_valid, fn_4096)
            def fn_4095() -> 'str29':
                return 'correct message'
            test_58.assert_(_list_get_4175(cs_1178.errors, 0).message == 'must be accepted', fn_4095)
        finally:
            test_58.soft_fail_to_hard()
class TestCase94(TestCase48):
    def test___validateConfirmationPassesWhenFieldsMatch__2421(self) -> None:
        'validateConfirmation passes when fields match'
        test_59: Test = Test()
        try:
            tbl_1180: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('password'), StringField(), False, None, False), FieldDef(_csid('password_confirmation'), StringField(), True, None, False)), None)
            params_1181: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('password', 'secret123'), _pair_4208('password_confirmation', 'secret123')))
            cs_1182: 'Changeset' = changeset(tbl_1180, params_1181).cast((_csid('password'), _csid('password_confirmation'))).validate_confirmation(_csid('password'), _csid('password_confirmation'))
            def fn_4094() -> 'str29':
                return 'matching fields should pass'
            test_59.assert_(cs_1182.is_valid, fn_4094)
        finally:
            test_59.soft_fail_to_hard()
class TestCase95(TestCase48):
    def test___validateConfirmationFailsWhenFieldsDiffer__2422(self) -> None:
        'validateConfirmation fails when fields differ'
        test_60: Test = Test()
        try:
            tbl_1184: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('password'), StringField(), False, None, False), FieldDef(_csid('password_confirmation'), StringField(), True, None, False)), None)
            params_1185: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('password', 'secret123'), _pair_4208('password_confirmation', 'wrong456')))
            cs_1186: 'Changeset' = changeset(tbl_1184, params_1185).cast((_csid('password'), _csid('password_confirmation'))).validate_confirmation(_csid('password'), _csid('password_confirmation'))
            def fn_4093() -> 'str29':
                return 'mismatched fields should fail'
            test_60.assert_(not cs_1186.is_valid, fn_4093)
            def fn_4092() -> 'str29':
                return 'error on confirmation field'
            test_60.assert_(_list_get_4175(cs_1186.errors, 0).field == 'password_confirmation', fn_4092)
        finally:
            test_60.soft_fail_to_hard()
class TestCase96(TestCase48):
    def test___validateConfirmationFailsWhenConfirmationMissing__2423(self) -> None:
        'validateConfirmation fails when confirmation missing'
        test_61: Test = Test()
        try:
            tbl_1188: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('password'), StringField(), False, None, False), FieldDef(_csid('password_confirmation'), StringField(), True, None, False)), None)
            params_1189: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('password', 'secret123'),))
            cs_1190: 'Changeset' = changeset(tbl_1188, params_1189).cast((_csid('password'),)).validate_confirmation(_csid('password'), _csid('password_confirmation'))
            def fn_4091() -> 'str29':
                return 'missing confirmation should fail'
            test_61.assert_(not cs_1190.is_valid, fn_4091)
        finally:
            test_61.soft_fail_to_hard()
class TestCase97(TestCase48):
    def test___validateContainsPassesWhenSubstringFound__2424(self) -> None:
        'validateContains passes when substring found'
        test_62: Test = Test()
        try:
            params_1192: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('email', 'alice@example.com'),))
            cs_1193: 'Changeset' = changeset(_user_table(), params_1192).cast((_csid('email'),)).validate_contains(_csid('email'), '@')
            def fn_4090() -> 'str29':
                return 'should pass when @ present'
            test_62.assert_(cs_1193.is_valid, fn_4090)
        finally:
            test_62.soft_fail_to_hard()
class TestCase98(TestCase48):
    def test___validateContainsFailsWhenSubstringNotFound__2425(self) -> None:
        'validateContains fails when substring not found'
        test_63: Test = Test()
        try:
            params_1195: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('email', 'alice-example.com'),))
            cs_1196: 'Changeset' = changeset(_user_table(), params_1195).cast((_csid('email'),)).validate_contains(_csid('email'), '@')
            def fn_4089() -> 'str29':
                return 'should fail when @ absent'
            test_63.assert_(not cs_1196.is_valid, fn_4089)
        finally:
            test_63.soft_fail_to_hard()
class TestCase99(TestCase48):
    def test___validateContainsSkipsWhenFieldNotInChanges__2426(self) -> None:
        'validateContains skips when field not in changes'
        test_64: Test = Test()
        try:
            params_1198: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1199: 'Changeset' = changeset(_user_table(), params_1198).cast((_csid('email'),)).validate_contains(_csid('email'), '@')
            def fn_4088() -> 'str29':
                return 'should be valid when field absent'
            test_64.assert_(cs_1199.is_valid, fn_4088)
        finally:
            test_64.soft_fail_to_hard()
class TestCase100(TestCase48):
    def test___validateStartsWithPasses__2427(self) -> None:
        'validateStartsWith passes'
        test_65: Test = Test()
        try:
            params_1201: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Dr. Smith'),))
            cs_1202: 'Changeset' = changeset(_user_table(), params_1201).cast((_csid('name'),)).validate_starts_with(_csid('name'), 'Dr.')
            def fn_4087() -> 'str29':
                return 'should pass for Dr. prefix'
            test_65.assert_(cs_1202.is_valid, fn_4087)
        finally:
            test_65.soft_fail_to_hard()
class TestCase101(TestCase48):
    def test___validateStartsWithFails__2428(self) -> None:
        'validateStartsWith fails'
        test_66: Test = Test()
        try:
            params_1204: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Mr. Smith'),))
            cs_1205: 'Changeset' = changeset(_user_table(), params_1204).cast((_csid('name'),)).validate_starts_with(_csid('name'), 'Dr.')
            def fn_4086() -> 'str29':
                return 'should fail for Mr. prefix'
            test_66.assert_(not cs_1205.is_valid, fn_4086)
        finally:
            test_66.soft_fail_to_hard()
class TestCase102(TestCase48):
    def test___validateEndsWithPasses__2429(self) -> None:
        'validateEndsWith passes'
        test_67: Test = Test()
        try:
            params_1207: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('email', 'alice@example.com'),))
            cs_1208: 'Changeset' = changeset(_user_table(), params_1207).cast((_csid('email'),)).validate_ends_with(_csid('email'), '.com')
            def fn_4085() -> 'str29':
                return 'should pass for .com suffix'
            test_67.assert_(cs_1208.is_valid, fn_4085)
        finally:
            test_67.soft_fail_to_hard()
class TestCase103(TestCase48):
    def test___validateEndsWithFails__2430(self) -> None:
        'validateEndsWith fails'
        test_68: Test = Test()
        try:
            params_1210: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('email', 'alice@example.org'),))
            cs_1211: 'Changeset' = changeset(_user_table(), params_1210).cast((_csid('email'),)).validate_ends_with(_csid('email'), '.com')
            def fn_4084() -> 'str29':
                return 'should fail for .org when expecting .com'
            test_68.assert_(not cs_1211.is_valid, fn_4084)
        finally:
            test_68.soft_fail_to_hard()
class TestCase104(TestCase48):
    def test___validateEndsWithHandlesRepeatedSuffixCorrectly__2431(self) -> None:
        'validateEndsWith handles repeated suffix correctly'
        test_69: Test = Test()
        try:
            params_1213: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'abcabc'),))
            cs_1214: 'Changeset' = changeset(_user_table(), params_1213).cast((_csid('name'),)).validate_ends_with(_csid('name'), 'abc')
            def fn_4083() -> 'str29':
                return 'abcabc should end with abc'
            test_69.assert_(cs_1214.is_valid, fn_4083)
        finally:
            test_69.soft_fail_to_hard()
class TestCase105(TestCase48):
    def test___toInsertSqlUsesDefaultValueWhenFieldNotInChanges__2432(self) -> None:
        'toInsertSql uses default value when field not in changes'
        test_70: Test = Test()
        try:
            tbl_1216: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False), FieldDef(_csid('status'), StringField(), False, SqlDefault(), False)), None)
            params_1217: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('title', 'Hello'),))
            cs_1218: 'Changeset' = changeset(tbl_1216, params_1217).cast((_csid('title'),))
            t_3666: 'SqlFragment' = cs_1218.to_insert_sql()
            s_1219: 'str29' = t_3666.to_string()
            t_3667: 'bool37' = s_1219.find('INSERT INTO posts') >= 0
            def fn_4082() -> 'str29':
                return _str_cat_4183('has INSERT INTO: ', s_1219)
            test_70.assert_(t_3667, fn_4082)
            t_3669: 'bool37' = s_1219.find("'Hello'") >= 0
            def fn_4081() -> 'str29':
                return _str_cat_4183('has title value: ', s_1219)
            test_70.assert_(t_3669, fn_4081)
            t_3671: 'bool37' = s_1219.find('DEFAULT') >= 0
            def fn_4080() -> 'str29':
                return _str_cat_4183('status should use DEFAULT: ', s_1219)
            test_70.assert_(t_3671, fn_4080)
        finally:
            test_70.soft_fail_to_hard()
class TestCase106(TestCase48):
    def test___toInsertSqlChangeOverridesDefaultValue__2433(self) -> None:
        'toInsertSql change overrides default value'
        test_71: Test = Test()
        try:
            tbl_1221: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False), FieldDef(_csid('status'), StringField(), False, SqlDefault(), False)), None)
            params_1222: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('title', 'Hello'), _pair_4208('status', 'published')))
            cs_1223: 'Changeset' = changeset(tbl_1221, params_1222).cast((_csid('title'), _csid('status')))
            t_3660: 'SqlFragment' = cs_1223.to_insert_sql()
            s_1224: 'str29' = t_3660.to_string()
            t_3661: 'bool37' = s_1224.find("'published'") >= 0
            def fn_4079() -> 'str29':
                return _str_cat_4183('should use provided value: ', s_1224)
            test_71.assert_(t_3661, fn_4079)
        finally:
            test_71.soft_fail_to_hard()
class TestCase107(TestCase48):
    def test___toInsertSqlWithTimestampsUsesDefault__2434(self) -> None:
        'toInsertSql with timestamps uses DEFAULT'
        test_72: Test = Test()
        try:
            ts_1226: 'Sequence33[FieldDef]' = timestamps()
            fields_1227: 'MutableSequence38[FieldDef]' = _list_4170()
            fields_1227.append(FieldDef(_csid('title'), StringField(), False, None, False))
            this_3817: 'Sequence33[FieldDef]' = ts_1226
            n_3819: 'int35' = _len_4174(this_3817)
            i_3820: 'int35' = 0
            while i_3820 < n_3819:
                el_3821: 'FieldDef' = _list_get_4175(this_3817, i_3820)
                i_3820 = _int_add_4176(i_3820, 1)
                t_1228: 'FieldDef' = el_3821
                fields_1227.append(t_1228)
            tbl_1229: 'TableDef' = TableDef(_csid('articles'), _tuple_4172(fields_1227), None)
            params_1230: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('title', 'News'),))
            cs_1231: 'Changeset' = changeset(tbl_1229, params_1230).cast((_csid('title'),))
            t_3652: 'SqlFragment' = cs_1231.to_insert_sql()
            s_1232: 'str29' = t_3652.to_string()
            t_3653: 'bool37' = s_1232.find('inserted_at') >= 0
            def fn_4078() -> 'str29':
                return _str_cat_4183('should include inserted_at: ', s_1232)
            test_72.assert_(t_3653, fn_4078)
            t_3655: 'bool37' = s_1232.find('updated_at') >= 0
            def fn_4077() -> 'str29':
                return _str_cat_4183('should include updated_at: ', s_1232)
            test_72.assert_(t_3655, fn_4077)
            t_3657: 'bool37' = s_1232.find('DEFAULT') >= 0
            def fn_4076() -> 'str29':
                return _str_cat_4183('timestamps should use DEFAULT: ', s_1232)
            test_72.assert_(t_3657, fn_4076)
        finally:
            test_72.soft_fail_to_hard()
class TestCase108(TestCase48):
    def test___toInsertSqlSkipsVirtualFields__2435(self) -> None:
        'toInsertSql skips virtual fields'
        test_73: Test = Test()
        try:
            tbl_1234: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('full_name'), StringField(), True, None, True)), None)
            params_1235: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('full_name', 'Alice Smith')))
            cs_1236: 'Changeset' = changeset(tbl_1234, params_1235).cast((_csid('name'), _csid('full_name')))
            t_3643: 'SqlFragment' = cs_1236.to_insert_sql()
            s_1237: 'str29' = t_3643.to_string()
            t_3644: 'bool37' = s_1237.find("'Alice'") >= 0
            def fn_4075() -> 'str29':
                return _str_cat_4183('name should be included: ', s_1237)
            test_73.assert_(t_3644, fn_4075)
            t_3646: 'bool37' = s_1237.find('full_name') >= 0
            def fn_4074() -> 'str29':
                return _str_cat_4183('virtual field should be excluded: ', s_1237)
            test_73.assert_(not t_3646, fn_4074)
        finally:
            test_73.soft_fail_to_hard()
class TestCase109(TestCase48):
    def test___toInsertSqlAllowsMissingNonNullableVirtualField__2436(self) -> None:
        'toInsertSql allows missing non-nullable virtual field'
        test_74: Test = Test()
        try:
            tbl_1239: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('computed'), StringField(), False, None, True)), None)
            params_1240: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'),))
            cs_1241: 'Changeset' = changeset(tbl_1239, params_1240).cast((_csid('name'),))
            t_3638: 'SqlFragment' = cs_1241.to_insert_sql()
            s_1242: 'str29' = t_3638.to_string()
            t_3639: 'bool37' = s_1242.find("'Alice'") >= 0
            def fn_4073() -> 'str29':
                return _str_cat_4183('should succeed: ', s_1242)
            test_74.assert_(t_3639, fn_4073)
        finally:
            test_74.soft_fail_to_hard()
class TestCase110(TestCase48):
    def test___toUpdateSqlSkipsVirtualFields__2437(self) -> None:
        'toUpdateSql skips virtual fields'
        test_75: Test = Test()
        try:
            tbl_1244: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('display'), StringField(), True, None, True)), None)
            params_1245: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Bob'), _pair_4208('display', 'Bobby')))
            cs_1246: 'Changeset' = changeset(tbl_1244, params_1245).cast((_csid('name'), _csid('display')))
            t_3632: 'SqlFragment' = cs_1246.to_update_sql(1)
            s_1247: 'str29' = t_3632.to_string()
            t_3633: 'bool37' = s_1247.find("name = 'Bob'") >= 0
            def fn_4072() -> 'str29':
                return _str_cat_4183('name should be in SET: ', s_1247)
            test_75.assert_(t_3633, fn_4072)
            t_3635: 'bool37' = s_1247.find('display') >= 0
            def fn_4071() -> 'str29':
                return _str_cat_4183('virtual field excluded from UPDATE: ', s_1247)
            test_75.assert_(not t_3635, fn_4071)
        finally:
            test_75.soft_fail_to_hard()
class TestCase111(TestCase48):
    def test___toUpdateSqlUsesCustomPrimaryKey__2438(self) -> None:
        'toUpdateSql uses custom primary key'
        test_76: Test = Test()
        try:
            tbl_1249: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False),), _csid('post_id'))
            params_1250: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('title', 'Updated'),))
            cs_1251: 'Changeset' = changeset(tbl_1249, params_1250).cast((_csid('title'),))
            t_3629: 'SqlFragment' = cs_1251.to_update_sql(99)
            s_1252: 'str29' = t_3629.to_string()
            def fn_4070() -> 'str29':
                return _str_cat_4183('got: ', s_1252)
            test_76.assert_(s_1252 == "UPDATE posts SET title = 'Updated' WHERE post_id = 99", fn_4070)
        finally:
            test_76.soft_fail_to_hard()
class TestCase112(TestCase48):
    def test___deleteSqlUsesCustomPrimaryKey__2439(self) -> None:
        'deleteSql uses custom primary key'
        test_77: Test = Test()
        try:
            tbl_1254: 'TableDef' = TableDef(_csid('posts'), (FieldDef(_csid('title'), StringField(), False, None, False),), _csid('post_id'))
            s_1255: 'str29' = delete_sql(tbl_1254, 42).to_string()
            def fn_4069() -> 'str29':
                return _str_cat_4183('got: ', s_1255)
            test_77.assert_(s_1255 == 'DELETE FROM posts WHERE post_id = 42', fn_4069)
        finally:
            test_77.soft_fail_to_hard()
class TestCase113(TestCase48):
    def test___deleteSqlUsesDefaultIdWhenPrimaryKeyNull__2440(self) -> None:
        'deleteSql uses default id when primaryKey null'
        test_78: Test = Test()
        try:
            tbl_1257: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False),), None)
            s_1258: 'str29' = delete_sql(tbl_1257, 7).to_string()
            def fn_4068() -> 'str29':
                return _str_cat_4183('got: ', s_1258)
            test_78.assert_(s_1258 == 'DELETE FROM users WHERE id = 7', fn_4068)
        finally:
            test_78.soft_fail_to_hard()
class TestCase114(TestCase48):
    def test___alreadyInvalidChangesetSkipsSubsequentValidators__2441(self) -> None:
        'already-invalid changeset skips subsequent validators'
        test_79: Test = Test()
        try:
            params_1260: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'A'), _pair_4208('email', 'alice@example.com')))
            cs_1261: 'Changeset' = changeset(_user_table(), params_1260).cast((_csid('name'), _csid('email'))).validate_length(_csid('name'), 3, 50).validate_required((_csid('name'), _csid('email'))).validate_contains(_csid('email'), '@')
            def fn_4067() -> 'str29':
                return 'should be invalid from validateLength'
            test_79.assert_(not cs_1261.is_valid, fn_4067)
            def fn_4066() -> 'str29':
                return _str_cat_4183('should have exactly 1 error, not accumulate: ', _int_to_string_4184(_len_4174(cs_1261.errors)))
            test_79.assert_(_len_4174(cs_1261.errors) == 1, fn_4066)
            def fn_4065() -> 'str29':
                return 'error should be on name'
            test_79.assert_(_list_get_4175(cs_1261.errors, 0).field == 'name', fn_4065)
        finally:
            test_79.soft_fail_to_hard()
class TestCase115(TestCase48):
    def test___validateNumberLessThanOrEqualPassesAtBoundary__2442(self) -> None:
        'validateNumber lessThanOrEqual passes at boundary'
        test_80: Test = Test()
        try:
            params_1263: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '10.0'),))
            cs_1264: 'Changeset' = changeset(_user_table(), params_1263).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, 10.0, None))
            def fn_4064() -> 'str29':
                return '10.0 <= 10.0 should pass'
            test_80.assert_(cs_1264.is_valid, fn_4064)
        finally:
            test_80.soft_fail_to_hard()
class TestCase116(TestCase48):
    def test___validateNumberLessThanOrEqualFailsAboveBoundary__2443(self) -> None:
        'validateNumber lessThanOrEqual fails above boundary'
        test_81: Test = Test()
        try:
            params_1266: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '10.1'),))
            cs_1267: 'Changeset' = changeset(_user_table(), params_1266).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, 10.0, None))
            def fn_4063() -> 'str29':
                return '10.1 <= 10.0 should fail'
            test_81.assert_(not cs_1267.is_valid, fn_4063)
            def fn_4062() -> 'str29':
                return 'correct message'
            test_81.assert_(_list_get_4175(cs_1267.errors, 0).message == 'must be less than or equal to 10.0', fn_4062)
        finally:
            test_81.soft_fail_to_hard()
class TestCase117(TestCase48):
    def test___validateNumberEqualToPassesWhenEqual__2444(self) -> None:
        'validateNumber equalTo passes when equal'
        test_82: Test = Test()
        try:
            params_1269: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '42.0'),))
            cs_1270: 'Changeset' = changeset(_user_table(), params_1269).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, None, 42.0))
            def fn_4061() -> 'str29':
                return '42.0 == 42.0 should pass'
            test_82.assert_(cs_1270.is_valid, fn_4061)
        finally:
            test_82.soft_fail_to_hard()
class TestCase118(TestCase48):
    def test___validateNumberEqualToFailsWhenNotEqual__2445(self) -> None:
        'validateNumber equalTo fails when not equal'
        test_83: Test = Test()
        try:
            params_1272: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '41.9'),))
            cs_1273: 'Changeset' = changeset(_user_table(), params_1272).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, None, None, None, 42.0))
            def fn_4060() -> 'str29':
                return '41.9 == 42.0 should fail'
            test_83.assert_(not cs_1273.is_valid, fn_4060)
            def fn_4059() -> 'str29':
                return 'correct message'
            test_83.assert_(_list_get_4175(cs_1273.errors, 0).message == 'must be equal to 42.0', fn_4059)
        finally:
            test_83.soft_fail_to_hard()
class TestCase119(TestCase48):
    def test___validateNumberGreaterThanFailsAtExactThreshold__2446(self) -> None:
        'validateNumber greaterThan fails at exact threshold'
        test_84: Test = Test()
        try:
            params_1275: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '18'),))
            cs_1276: 'Changeset' = changeset(_user_table(), params_1275).cast((_csid('age'),)).validate_number(_csid('age'), NumberValidationOpts(18.0, None, None, None, None))
            def fn_4058() -> 'str29':
                return '18 > 18 should fail (strict greater than)'
            test_84.assert_(not cs_1276.is_valid, fn_4058)
        finally:
            test_84.soft_fail_to_hard()
class TestCase120(TestCase48):
    def test___validateNumberLessThanFailsAtExactThreshold__2447(self) -> None:
        'validateNumber lessThan fails at exact threshold'
        test_85: Test = Test()
        try:
            params_1278: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', '10.0'),))
            cs_1279: 'Changeset' = changeset(_user_table(), params_1278).cast((_csid('score'),)).validate_number(_csid('score'), NumberValidationOpts(None, 10.0, None, None, None))
            def fn_4057() -> 'str29':
                return '10.0 < 10.0 should fail (strict less than)'
            test_85.assert_(not cs_1279.is_valid, fn_4057)
        finally:
            test_85.soft_fail_to_hard()
class TestCase121(TestCase48):
    def test___validateFloatFailsForNonFloatString__2448(self) -> None:
        'validateFloat fails for non-float string'
        test_86: Test = Test()
        try:
            params_1281: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('score', 'abc'),))
            cs_1282: 'Changeset' = changeset(_user_table(), params_1281).cast((_csid('score'),)).validate_float(_csid('score'))
            def fn_4056() -> 'str29':
                return 'abc should not parse as float'
            test_86.assert_(not cs_1282.is_valid, fn_4056)
            def fn_4055() -> 'str29':
                return 'correct message'
            test_86.assert_(_list_get_4175(cs_1282.errors, 0).message == 'must be a number', fn_4055)
        finally:
            test_86.soft_fail_to_hard()
class TestCase122(TestCase48):
    def test___toInsertSqlWithAllSixFieldTypes__2449(self) -> None:
        'toInsertSql with all six field types'
        test_87: Test = Test()
        try:
            tbl_1284: 'TableDef' = TableDef(_csid('records'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('count'), IntField(), False, None, False), FieldDef(_csid('big_id'), Int64Field(), False, None, False), FieldDef(_csid('rating'), FloatField(), False, None, False), FieldDef(_csid('active'), BoolField(), False, None, False), FieldDef(_csid('birthday'), DateField(), False, None, False)), None)
            params_1285: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('count', '42'), _pair_4208('big_id', '9999999999'), _pair_4208('rating', '3.14'), _pair_4208('active', 'true'), _pair_4208('birthday', '2000-01-15')))
            cs_1286: 'Changeset' = changeset(tbl_1284, params_1285).cast((_csid('name'), _csid('count'), _csid('big_id'), _csid('rating'), _csid('active'), _csid('birthday')))
            t_3616: 'SqlFragment' = cs_1286.to_insert_sql()
            s_1287: 'str29' = t_3616.to_string()
            t_3617: 'bool37' = s_1287.find("'Alice'") >= 0
            def fn_4054() -> 'str29':
                return _str_cat_4183('string field: ', s_1287)
            test_87.assert_(t_3617, fn_4054)
            t_3619: 'bool37' = s_1287.find('42') >= 0
            def fn_4053() -> 'str29':
                return _str_cat_4183('int field: ', s_1287)
            test_87.assert_(t_3619, fn_4053)
            t_3621: 'bool37' = s_1287.find('9999999999') >= 0
            def fn_4052() -> 'str29':
                return _str_cat_4183('int64 field: ', s_1287)
            test_87.assert_(t_3621, fn_4052)
            t_3623: 'bool37' = s_1287.find('3.14') >= 0
            def fn_4051() -> 'str29':
                return _str_cat_4183('float field: ', s_1287)
            test_87.assert_(t_3623, fn_4051)
            t_3625: 'bool37' = s_1287.find('TRUE') >= 0
            def fn_4050() -> 'str29':
                return _str_cat_4183('bool field: ', s_1287)
            test_87.assert_(t_3625, fn_4050)
            t_3627: 'bool37' = s_1287.find("'2000-01-15'") >= 0
            def fn_4049() -> 'str29':
                return _str_cat_4183('date field: ', s_1287)
            test_87.assert_(t_3627, fn_4049)
        finally:
            test_87.soft_fail_to_hard()
class TestCase123(TestCase48):
    def test___deleteChangeOnNonNullableFieldCausesToInsertSqlToBubble__2450(self) -> None:
        'deleteChange on non-nullable field causes toInsertSql to bubble'
        test_88: Test = Test()
        try:
            tbl_1289: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('email'), StringField(), False, None, False)), None)
            params_1290: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('email', 'a@b.com')))
            cs_1291: 'Changeset' = changeset(tbl_1289, params_1290).cast((_csid('name'), _csid('email'))).delete_change(_csid('email'))
            did_bubble_1292: 'bool37'
            try:
                cs_1291.to_insert_sql()
                did_bubble_1292 = False
            except Exception41:
                did_bubble_1292 = True
            def fn_4048() -> 'str29':
                return 'removing non-nullable field should make toInsertSql bubble'
            test_88.assert_(did_bubble_1292, fn_4048)
        finally:
            test_88.soft_fail_to_hard()
class TestCase124(TestCase48):
    def test___validateLengthPassesAtExactMin__2451(self) -> None:
        'validateLength passes at exact min'
        test_89: Test = Test()
        try:
            params_1294: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'abc'),))
            cs_1295: 'Changeset' = changeset(_user_table(), params_1294).cast((_csid('name'),)).validate_length(_csid('name'), 3, 10)
            def fn_4047() -> 'str29':
                return 'length 3 should pass for min 3'
            test_89.assert_(cs_1295.is_valid, fn_4047)
        finally:
            test_89.soft_fail_to_hard()
class TestCase125(TestCase48):
    def test___validateLengthPassesAtExactMax__2452(self) -> None:
        'validateLength passes at exact max'
        test_90: Test = Test()
        try:
            params_1297: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'abcdefghij'),))
            cs_1298: 'Changeset' = changeset(_user_table(), params_1297).cast((_csid('name'),)).validate_length(_csid('name'), 1, 10)
            def fn_4046() -> 'str29':
                return 'length 10 should pass for max 10'
            test_90.assert_(cs_1298.is_valid, fn_4046)
        finally:
            test_90.soft_fail_to_hard()
class TestCase126(TestCase48):
    def test___validateAcceptanceSkipsWhenFieldNotInChanges__2453(self) -> None:
        'validateAcceptance skips when field not in changes'
        test_91: Test = Test()
        try:
            params_1300: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1301: 'Changeset' = changeset(_user_table(), params_1300).cast((_csid('active'),)).validate_acceptance(_csid('active'))
            def fn_4045() -> 'str29':
                return 'should be valid when field absent'
            test_91.assert_(cs_1301.is_valid, fn_4045)
        finally:
            test_91.soft_fail_to_hard()
class TestCase127(TestCase48):
    def test___multipleValidatorsChainCorrectlyOnValidChangeset__2454(self) -> None:
        'multiple validators chain correctly on valid changeset'
        test_92: Test = Test()
        try:
            params_1303: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('email', 'alice@example.com'), _pair_4208('age', '25')))
            cs_1304: 'Changeset' = changeset(_user_table(), params_1303).cast((_csid('name'), _csid('email'), _csid('age'))).validate_required((_csid('name'), _csid('email'))).validate_length(_csid('name'), 2, 50).validate_contains(_csid('email'), '@').validate_int(_csid('age')).validate_number(_csid('age'), NumberValidationOpts(0.0, 150.0, None, None, None))
            def fn_4044() -> 'str29':
                return 'all validators should pass'
            test_92.assert_(cs_1304.is_valid, fn_4044)
            def fn_4043() -> 'str29':
                return 'no errors expected'
            test_92.assert_(_len_4174(cs_1304.errors) == 0, fn_4043)
        finally:
            test_92.soft_fail_to_hard()
class TestCase128(TestCase48):
    def test___toUpdateSqlWithMultipleNonVirtualFields__2455(self) -> None:
        'toUpdateSql with multiple non-virtual fields'
        test_93: Test = Test()
        try:
            tbl_1306: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('email'), StringField(), False, None, False)), None)
            params_1307: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Bob'), _pair_4208('email', 'bob@example.com')))
            cs_1308: 'Changeset' = changeset(tbl_1306, params_1307).cast((_csid('name'), _csid('email')))
            t_3602: 'SqlFragment' = cs_1308.to_update_sql(5)
            s_1309: 'str29' = t_3602.to_string()
            t_3603: 'bool37' = s_1309.find("name = 'Bob'") >= 0
            def fn_4042() -> 'str29':
                return _str_cat_4183('name in SET: ', s_1309)
            test_93.assert_(t_3603, fn_4042)
            t_3605: 'bool37' = s_1309.find("email = 'bob@example.com'") >= 0
            def fn_4041() -> 'str29':
                return _str_cat_4183('email in SET: ', s_1309)
            test_93.assert_(t_3605, fn_4041)
            t_3607: 'bool37' = s_1309.find('WHERE id = 5') >= 0
            def fn_4040() -> 'str29':
                return _str_cat_4183('WHERE clause: ', s_1309)
            test_93.assert_(t_3607, fn_4040)
        finally:
            test_93.soft_fail_to_hard()
class TestCase129(TestCase48):
    def test___toUpdateSqlBubblesWhenAllChangesAreVirtualFields__2456(self) -> None:
        'toUpdateSql bubbles when all changes are virtual fields'
        test_94: Test = Test()
        try:
            tbl_1311: 'TableDef' = TableDef(_csid('users'), (FieldDef(_csid('name'), StringField(), False, None, False), FieldDef(_csid('computed'), StringField(), True, None, True)), None)
            params_1312: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'Alice'), _pair_4208('computed', 'derived')))
            cs_1313: 'Changeset' = changeset(tbl_1311, params_1312).cast((_csid('computed'),))
            did_bubble_1314: 'bool37'
            try:
                cs_1313.to_update_sql(1)
                did_bubble_1314 = False
            except Exception41:
                did_bubble_1314 = True
            def fn_4039() -> 'str29':
                return 'should bubble when all changes are virtual'
            test_94.assert_(did_bubble_1314, fn_4039)
        finally:
            test_94.soft_fail_to_hard()
class TestCase130(TestCase48):
    def test___putChangeSatisfiesSubsequentValidateRequired__2457(self) -> None:
        'putChange satisfies subsequent validateRequired'
        test_95: Test = Test()
        try:
            params_1316: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1317: 'Changeset' = changeset(_user_table(), params_1316).cast((_csid('name'),)).put_change(_csid('name'), 'Injected').validate_required((_csid('name'),))
            def fn_4038() -> 'str29':
                return 'putChange should satisfy required'
            test_95.assert_(cs_1317.is_valid, fn_4038)
        finally:
            test_95.soft_fail_to_hard()
class TestCase131(TestCase48):
    def test___validateStartsWithSkipsWhenFieldNotInChanges__2458(self) -> None:
        'validateStartsWith skips when field not in changes'
        test_96: Test = Test()
        try:
            params_1319: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1320: 'Changeset' = changeset(_user_table(), params_1319).cast((_csid('name'),)).validate_starts_with(_csid('name'), 'Dr.')
            def fn_4037() -> 'str29':
                return 'should be valid when field absent'
            test_96.assert_(cs_1320.is_valid, fn_4037)
        finally:
            test_96.soft_fail_to_hard()
class TestCase132(TestCase48):
    def test___validateEndsWithSkipsWhenFieldNotInChanges__2459(self) -> None:
        'validateEndsWith skips when field not in changes'
        test_97: Test = Test()
        try:
            params_1322: 'MappingProxyType36[str29, str29]' = _map_constructor_4207(())
            cs_1323: 'Changeset' = changeset(_user_table(), params_1322).cast((_csid('name'),)).validate_ends_with(_csid('name'), '.com')
            def fn_4036() -> 'str29':
                return 'should be valid when field absent'
            test_97.assert_(cs_1323.is_valid, fn_4036)
        finally:
            test_97.soft_fail_to_hard()
class TestCase133(TestCase48):
    def test___validateIntAcceptsZero__2460(self) -> None:
        'validateInt accepts zero'
        test_98: Test = Test()
        try:
            params_1325: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '0'),))
            cs_1326: 'Changeset' = changeset(_user_table(), params_1325).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_4035() -> 'str29':
                return '0 should be a valid int'
            test_98.assert_(cs_1326.is_valid, fn_4035)
        finally:
            test_98.soft_fail_to_hard()
class TestCase134(TestCase48):
    def test___validateIntAcceptsNegative__2461(self) -> None:
        'validateInt accepts negative'
        test_99: Test = Test()
        try:
            params_1328: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('age', '-5'),))
            cs_1329: 'Changeset' = changeset(_user_table(), params_1328).cast((_csid('age'),)).validate_int(_csid('age'))
            def fn_4034() -> 'str29':
                return '-5 should be a valid int'
            test_99.assert_(cs_1329.is_valid, fn_4034)
        finally:
            test_99.soft_fail_to_hard()
class TestCase135(TestCase48):
    def test___changesetImmutabilityValidatorsDoNotMutateBase__2462(self) -> None:
        'changeset immutability - validators do not mutate base'
        test_100: Test = Test()
        try:
            params_1331: 'MappingProxyType36[str29, str29]' = _map_constructor_4207((_pair_4208('name', 'A'), _pair_4208('email', 'alice@example.com')))
            base_1332: 'Changeset' = changeset(_user_table(), params_1331).cast((_csid('name'), _csid('email')))
            failed_1333: 'Changeset' = base_1332.validate_length(_csid('name'), 3, 50)
            passed_1334: 'Changeset' = base_1332.validate_required((_csid('name'), _csid('email')))
            def fn_4033() -> 'str29':
                return 'failed branch should be invalid'
            test_100.assert_(not failed_1333.is_valid, fn_4033)
            def fn_4032() -> 'str29':
                return 'passed branch should still be valid'
            test_100.assert_(passed_1334.is_valid, fn_4032)
        finally:
            test_100.soft_fail_to_hard()
def _sid(name_1684: 'str29', /) -> 'SafeIdentifier':
    return safe_identifier(name_1684)
class TestCase136(TestCase48):
    def test___bareFromProducesSelect__2544(self) -> None:
        'bare from produces SELECT *'
        test_101: Test = Test()
        try:
            q_1687: 'Query' = from_(_sid('users'))
            def fn_4029() -> 'str29':
                return 'bare query'
            test_101.assert_(q_1687.to_sql().to_string() == 'SELECT * FROM users', fn_4029)
        finally:
            test_101.soft_fail_to_hard()
class TestCase137(TestCase48):
    def test___selectRestrictsColumns__2545(self) -> None:
        'select restricts columns'
        test_102: Test = Test()
        try:
            q_1689: 'Query' = from_(_sid('users')).select((_sid('id'), _sid('name')))
            def fn_4028() -> 'str29':
                return 'select columns'
            test_102.assert_(q_1689.to_sql().to_string() == 'SELECT id, name FROM users', fn_4028)
        finally:
            test_102.soft_fail_to_hard()
class TestCase138(TestCase48):
    def test___whereAddsConditionWithIntValue__2546(self) -> None:
        'where adds condition with int value'
        test_103: Test = Test()
        try:
            t_3596: 'Query' = from_(_sid('users'))
            accumulator_2547: 'SqlBuilder' = SqlBuilder()
            accumulator_2547.append_safe('age > ')
            accumulator_2547.append_int32(18)
            q_1691: 'Query' = t_3596.where(accumulator_2547.accumulated)
            def fn_4027() -> 'str29':
                return 'where int'
            test_103.assert_(q_1691.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18', fn_4027)
        finally:
            test_103.soft_fail_to_hard()
class TestCase139(TestCase48):
    def test___whereAddsConditionWithBoolValue__2548(self) -> None:
        'where adds condition with bool value'
        test_104: Test = Test()
        try:
            t_3594: 'Query' = from_(_sid('users'))
            accumulator_2549: 'SqlBuilder' = SqlBuilder()
            accumulator_2549.append_safe('active = ')
            accumulator_2549.append_boolean(True)
            q_1693: 'Query' = t_3594.where(accumulator_2549.accumulated)
            def fn_4026() -> 'str29':
                return 'where bool'
            test_104.assert_(q_1693.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE', fn_4026)
        finally:
            test_104.soft_fail_to_hard()
class TestCase140(TestCase48):
    def test___chainedWhereUsesAnd__2550(self) -> None:
        'chained where uses AND'
        test_105: Test = Test()
        try:
            t_3590: 'Query' = from_(_sid('users'))
            accumulator_2551: 'SqlBuilder' = SqlBuilder()
            accumulator_2551.append_safe('age > ')
            accumulator_2551.append_int32(18)
            t_3592: 'Query' = t_3590.where(accumulator_2551.accumulated)
            accumulator_2552: 'SqlBuilder' = SqlBuilder()
            accumulator_2552.append_safe('active = ')
            accumulator_2552.append_boolean(True)
            q_1695: 'Query' = t_3592.where(accumulator_2552.accumulated)
            def fn_4025() -> 'str29':
                return 'chained where'
            test_105.assert_(q_1695.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE', fn_4025)
        finally:
            test_105.soft_fail_to_hard()
class TestCase141(TestCase48):
    def test___orderByAsc__2553(self) -> None:
        'orderBy ASC'
        test_106: Test = Test()
        try:
            q_1697: 'Query' = from_(_sid('users')).order_by(_sid('name'), True)
            def fn_4024() -> 'str29':
                return 'order asc'
            test_106.assert_(q_1697.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC', fn_4024)
        finally:
            test_106.soft_fail_to_hard()
class TestCase142(TestCase48):
    def test___orderByDesc__2554(self) -> None:
        'orderBy DESC'
        test_107: Test = Test()
        try:
            q_1699: 'Query' = from_(_sid('users')).order_by(_sid('created_at'), False)
            def fn_4023() -> 'str29':
                return 'order desc'
            test_107.assert_(q_1699.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC', fn_4023)
        finally:
            test_107.soft_fail_to_hard()
class TestCase143(TestCase48):
    def test___limitAndOffset__2555(self) -> None:
        'limit and offset'
        test_108: Test = Test()
        try:
            t_3842: 'Query' = from_(_sid('users')).limit(10)
            q_1701: 'Query' = t_3842.offset(20)
            def fn_4022() -> 'str29':
                return 'limit/offset'
            test_108.assert_(q_1701.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20', fn_4022)
        finally:
            test_108.soft_fail_to_hard()
class TestCase144(TestCase48):
    def test___limitBubblesOnNegative__2556(self) -> None:
        'limit bubbles on negative'
        test_109: Test = Test()
        try:
            did_bubble_1703: 'bool37'
            try:
                from_(_sid('users')).limit(-1)
                did_bubble_1703 = False
            except Exception41:
                did_bubble_1703 = True
            def fn_4021() -> 'str29':
                return 'negative limit should bubble'
            test_109.assert_(did_bubble_1703, fn_4021)
        finally:
            test_109.soft_fail_to_hard()
class TestCase145(TestCase48):
    def test___offsetBubblesOnNegative__2557(self) -> None:
        'offset bubbles on negative'
        test_110: Test = Test()
        try:
            did_bubble_1705: 'bool37'
            try:
                from_(_sid('users')).offset(-1)
                did_bubble_1705 = False
            except Exception41:
                did_bubble_1705 = True
            def fn_4020() -> 'str29':
                return 'negative offset should bubble'
            test_110.assert_(did_bubble_1705, fn_4020)
        finally:
            test_110.soft_fail_to_hard()
class TestCase146(TestCase48):
    def test___complexComposedQuery__2558(self) -> None:
        'complex composed query'
        test_111: Test = Test()
        try:
            min_age_1707: 'int35' = 21
            t_3582: 'Query' = from_(_sid('users')).select((_sid('id'), _sid('name'), _sid('email')))
            accumulator_2559: 'SqlBuilder' = SqlBuilder()
            accumulator_2559.append_safe('age >= ')
            accumulator_2559.append_int32(21)
            t_3584: 'Query' = t_3582.where(accumulator_2559.accumulated)
            accumulator_2560: 'SqlBuilder' = SqlBuilder()
            accumulator_2560.append_safe('active = ')
            accumulator_2560.append_boolean(True)
            t_3841: 'Query' = t_3584.where(accumulator_2560.accumulated).order_by(_sid('name'), True).limit(25)
            q_1708: 'Query' = t_3841.offset(0)
            def fn_4019() -> 'str29':
                return 'complex query'
            test_111.assert_(q_1708.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0', fn_4019)
        finally:
            test_111.soft_fail_to_hard()
class TestCase147(TestCase48):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__2561(self) -> None:
        'safeToSql applies default limit when none set'
        test_112: Test = Test()
        try:
            q_1710: 'Query' = from_(_sid('users'))
            t_3580: 'SqlFragment' = q_1710.safe_to_sql(100)
            s_1711: 'str29' = t_3580.to_string()
            def fn_4018() -> 'str29':
                return _str_cat_4183('should have limit: ', s_1711)
            test_112.assert_(s_1711 == 'SELECT * FROM users LIMIT 100', fn_4018)
        finally:
            test_112.soft_fail_to_hard()
class TestCase148(TestCase48):
    def test___safeToSqlRespectsExplicitLimit__2562(self) -> None:
        'safeToSql respects explicit limit'
        test_113: Test = Test()
        try:
            q_1713: 'Query' = from_(_sid('users')).limit(5)
            t_3579: 'SqlFragment' = q_1713.safe_to_sql(100)
            s_1714: 'str29' = t_3579.to_string()
            def fn_4017() -> 'str29':
                return _str_cat_4183('explicit limit preserved: ', s_1714)
            test_113.assert_(s_1714 == 'SELECT * FROM users LIMIT 5', fn_4017)
        finally:
            test_113.soft_fail_to_hard()
class TestCase149(TestCase48):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__2563(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_114: Test = Test()
        try:
            did_bubble_1716: 'bool37'
            try:
                from_(_sid('users')).safe_to_sql(-1)
                did_bubble_1716 = False
            except Exception41:
                did_bubble_1716 = True
            def fn_4016() -> 'str29':
                return 'negative defaultLimit should bubble'
            test_114.assert_(did_bubble_1716, fn_4016)
        finally:
            test_114.soft_fail_to_hard()
class TestCase150(TestCase48):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__2564(self) -> None:
        'where with injection attempt in string value is escaped'
        test_115: Test = Test()
        try:
            evil_1718: 'str29' = "'; DROP TABLE users; --"
            t_3572: 'Query' = from_(_sid('users'))
            accumulator_2565: 'SqlBuilder' = SqlBuilder()
            accumulator_2565.append_safe('name = ')
            accumulator_2565.append_string("'; DROP TABLE users; --")
            q_1719: 'Query' = t_3572.where(accumulator_2565.accumulated)
            s_1720: 'str29' = q_1719.to_sql().to_string()
            t_3573: 'bool37' = s_1720.find("''") >= 0
            def fn_4015() -> 'str29':
                return _str_cat_4183('quotes must be doubled: ', s_1720)
            test_115.assert_(t_3573, fn_4015)
            t_3575: 'bool37' = s_1720.find('SELECT * FROM users WHERE name =') >= 0
            def fn_4014() -> 'str29':
                return _str_cat_4183('structure intact: ', s_1720)
            test_115.assert_(t_3575, fn_4014)
        finally:
            test_115.soft_fail_to_hard()
class TestCase151(TestCase48):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__2566(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_116: Test = Test()
        try:
            attack_1722: 'str29' = 'users; DROP TABLE users; --'
            did_bubble_1723: 'bool37'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_1723 = False
            except Exception41:
                did_bubble_1723 = True
            def fn_4013() -> 'str29':
                return 'metacharacter-containing name must be rejected at construction'
            test_116.assert_(did_bubble_1723, fn_4013)
        finally:
            test_116.soft_fail_to_hard()
class TestCase152(TestCase48):
    def test___innerJoinProducesInnerJoin__2567(self) -> None:
        'innerJoin produces INNER JOIN'
        test_117: Test = Test()
        try:
            t_3566: 'Query' = from_(_sid('users'))
            t_3567: 'SafeIdentifier' = _sid('orders')
            accumulator_2568: 'SqlBuilder' = SqlBuilder()
            accumulator_2568.append_safe('users.id = orders.user_id')
            q_1725: 'Query' = t_3566.inner_join(t_3567, accumulator_2568.accumulated)
            def fn_4012() -> 'str29':
                return 'inner join'
            test_117.assert_(q_1725.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id', fn_4012)
        finally:
            test_117.soft_fail_to_hard()
class TestCase153(TestCase48):
    def test___leftJoinProducesLeftJoin__2569(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_118: Test = Test()
        try:
            t_3563: 'Query' = from_(_sid('users'))
            t_3564: 'SafeIdentifier' = _sid('profiles')
            accumulator_2570: 'SqlBuilder' = SqlBuilder()
            accumulator_2570.append_safe('users.id = profiles.user_id')
            q_1727: 'Query' = t_3563.left_join(t_3564, accumulator_2570.accumulated)
            def fn_4011() -> 'str29':
                return 'left join'
            test_118.assert_(q_1727.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id', fn_4011)
        finally:
            test_118.soft_fail_to_hard()
class TestCase154(TestCase48):
    def test___rightJoinProducesRightJoin__2571(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_119: Test = Test()
        try:
            t_3560: 'Query' = from_(_sid('orders'))
            t_3561: 'SafeIdentifier' = _sid('users')
            accumulator_2572: 'SqlBuilder' = SqlBuilder()
            accumulator_2572.append_safe('orders.user_id = users.id')
            q_1729: 'Query' = t_3560.right_join(t_3561, accumulator_2572.accumulated)
            def fn_4010() -> 'str29':
                return 'right join'
            test_119.assert_(q_1729.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id', fn_4010)
        finally:
            test_119.soft_fail_to_hard()
class TestCase155(TestCase48):
    def test___fullJoinProducesFullOuterJoin__2573(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_120: Test = Test()
        try:
            t_3557: 'Query' = from_(_sid('users'))
            t_3558: 'SafeIdentifier' = _sid('orders')
            accumulator_2574: 'SqlBuilder' = SqlBuilder()
            accumulator_2574.append_safe('users.id = orders.user_id')
            q_1731: 'Query' = t_3557.full_join(t_3558, accumulator_2574.accumulated)
            def fn_4009() -> 'str29':
                return 'full join'
            test_120.assert_(q_1731.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id', fn_4009)
        finally:
            test_120.soft_fail_to_hard()
class TestCase156(TestCase48):
    def test___chainedJoins__2575(self) -> None:
        'chained joins'
        test_121: Test = Test()
        try:
            t_3551: 'Query' = from_(_sid('users'))
            t_3552: 'SafeIdentifier' = _sid('orders')
            accumulator_2576: 'SqlBuilder' = SqlBuilder()
            accumulator_2576.append_safe('users.id = orders.user_id')
            t_3554: 'Query' = t_3551.inner_join(t_3552, accumulator_2576.accumulated)
            t_3555: 'SafeIdentifier' = _sid('profiles')
            accumulator_2577: 'SqlBuilder' = SqlBuilder()
            accumulator_2577.append_safe('users.id = profiles.user_id')
            q_1733: 'Query' = t_3554.left_join(t_3555, accumulator_2577.accumulated)
            def fn_4008() -> 'str29':
                return 'chained joins'
            test_121.assert_(q_1733.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id', fn_4008)
        finally:
            test_121.soft_fail_to_hard()
class TestCase157(TestCase48):
    def test___joinWithWhereAndOrderBy__2578(self) -> None:
        'join with where and orderBy'
        test_122: Test = Test()
        try:
            t_3545: 'Query' = from_(_sid('users'))
            t_3546: 'SafeIdentifier' = _sid('orders')
            accumulator_2579: 'SqlBuilder' = SqlBuilder()
            accumulator_2579.append_safe('users.id = orders.user_id')
            t_3548: 'Query' = t_3545.inner_join(t_3546, accumulator_2579.accumulated)
            accumulator_2580: 'SqlBuilder' = SqlBuilder()
            accumulator_2580.append_safe('orders.total > ')
            accumulator_2580.append_int32(100)
            q_1735: 'Query' = t_3548.where(accumulator_2580.accumulated).order_by(_sid('name'), True).limit(10)
            def fn_4007() -> 'str29':
                return 'join with where/order/limit'
            test_122.assert_(q_1735.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10', fn_4007)
        finally:
            test_122.soft_fail_to_hard()
class TestCase158(TestCase48):
    def test___colHelperProducesQualifiedReference__2581(self) -> None:
        'col helper produces qualified reference'
        test_123: Test = Test()
        try:
            c_1737: 'SqlFragment' = col(_sid('users'), _sid('id'))
            def fn_4006() -> 'str29':
                return 'col helper'
            test_123.assert_(c_1737.to_string() == 'users.id', fn_4006)
        finally:
            test_123.soft_fail_to_hard()
class TestCase159(TestCase48):
    def test___joinWithColHelper__2582(self) -> None:
        'join with col helper'
        test_124: Test = Test()
        try:
            on_cond_1739: 'SqlFragment' = col(_sid('users'), _sid('id'))
            b_1740: 'SqlBuilder' = SqlBuilder()
            b_1740.append_fragment(on_cond_1739)
            b_1740.append_safe(' = ')
            b_1740.append_fragment(col(_sid('orders'), _sid('user_id')))
            q_1741: 'Query' = from_(_sid('users')).inner_join(_sid('orders'), b_1740.accumulated)
            def fn_4005() -> 'str29':
                return 'join with col'
            test_124.assert_(q_1741.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id', fn_4005)
        finally:
            test_124.soft_fail_to_hard()
class TestCase160(TestCase48):
    def test___orWhereBasic__2583(self) -> None:
        'orWhere basic'
        test_125: Test = Test()
        try:
            t_3543: 'Query' = from_(_sid('users'))
            accumulator_2584: 'SqlBuilder' = SqlBuilder()
            accumulator_2584.append_safe('status = ')
            accumulator_2584.append_string('active')
            q_1743: 'Query' = t_3543.or_where(accumulator_2584.accumulated)
            def fn_4004() -> 'str29':
                return 'orWhere basic'
            test_125.assert_(q_1743.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'", fn_4004)
        finally:
            test_125.soft_fail_to_hard()
class TestCase161(TestCase48):
    def test___whereThenOrWhere__2585(self) -> None:
        'where then orWhere'
        test_126: Test = Test()
        try:
            t_3539: 'Query' = from_(_sid('users'))
            accumulator_2586: 'SqlBuilder' = SqlBuilder()
            accumulator_2586.append_safe('age > ')
            accumulator_2586.append_int32(18)
            t_3541: 'Query' = t_3539.where(accumulator_2586.accumulated)
            accumulator_2587: 'SqlBuilder' = SqlBuilder()
            accumulator_2587.append_safe('vip = ')
            accumulator_2587.append_boolean(True)
            q_1745: 'Query' = t_3541.or_where(accumulator_2587.accumulated)
            def fn_4003() -> 'str29':
                return 'where then orWhere'
            test_126.assert_(q_1745.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE', fn_4003)
        finally:
            test_126.soft_fail_to_hard()
class TestCase162(TestCase48):
    def test___multipleOrWhere__2588(self) -> None:
        'multiple orWhere'
        test_127: Test = Test()
        try:
            t_3533: 'Query' = from_(_sid('users'))
            accumulator_2589: 'SqlBuilder' = SqlBuilder()
            accumulator_2589.append_safe('active = ')
            accumulator_2589.append_boolean(True)
            t_3535: 'Query' = t_3533.where(accumulator_2589.accumulated)
            accumulator_2590: 'SqlBuilder' = SqlBuilder()
            accumulator_2590.append_safe('role = ')
            accumulator_2590.append_string('admin')
            t_3537: 'Query' = t_3535.or_where(accumulator_2590.accumulated)
            accumulator_2591: 'SqlBuilder' = SqlBuilder()
            accumulator_2591.append_safe('role = ')
            accumulator_2591.append_string('moderator')
            q_1747: 'Query' = t_3537.or_where(accumulator_2591.accumulated)
            def fn_4002() -> 'str29':
                return 'multiple orWhere'
            test_127.assert_(q_1747.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'", fn_4002)
        finally:
            test_127.soft_fail_to_hard()
class TestCase163(TestCase48):
    def test___mixedWhereAndOrWhere__2592(self) -> None:
        'mixed where and orWhere'
        test_128: Test = Test()
        try:
            t_3527: 'Query' = from_(_sid('users'))
            accumulator_2593: 'SqlBuilder' = SqlBuilder()
            accumulator_2593.append_safe('age > ')
            accumulator_2593.append_int32(18)
            t_3529: 'Query' = t_3527.where(accumulator_2593.accumulated)
            accumulator_2594: 'SqlBuilder' = SqlBuilder()
            accumulator_2594.append_safe('active = ')
            accumulator_2594.append_boolean(True)
            t_3531: 'Query' = t_3529.where(accumulator_2594.accumulated)
            accumulator_2595: 'SqlBuilder' = SqlBuilder()
            accumulator_2595.append_safe('vip = ')
            accumulator_2595.append_boolean(True)
            q_1749: 'Query' = t_3531.or_where(accumulator_2595.accumulated)
            def fn_4001() -> 'str29':
                return 'mixed where and orWhere'
            test_128.assert_(q_1749.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE', fn_4001)
        finally:
            test_128.soft_fail_to_hard()
class TestCase164(TestCase48):
    def test___whereNull__2596(self) -> None:
        'whereNull'
        test_129: Test = Test()
        try:
            q_1751: 'Query' = from_(_sid('users')).where_null(_sid('deleted_at'))
            def fn_4000() -> 'str29':
                return 'whereNull'
            test_129.assert_(q_1751.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL', fn_4000)
        finally:
            test_129.soft_fail_to_hard()
class TestCase165(TestCase48):
    def test___whereNotNull__2597(self) -> None:
        'whereNotNull'
        test_130: Test = Test()
        try:
            q_1753: 'Query' = from_(_sid('users')).where_not_null(_sid('email'))
            def fn_3999() -> 'str29':
                return 'whereNotNull'
            test_130.assert_(q_1753.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL', fn_3999)
        finally:
            test_130.soft_fail_to_hard()
class TestCase166(TestCase48):
    def test___whereNullChainedWithWhere__2598(self) -> None:
        'whereNull chained with where'
        test_131: Test = Test()
        try:
            t_3525: 'Query' = from_(_sid('users'))
            accumulator_2599: 'SqlBuilder' = SqlBuilder()
            accumulator_2599.append_safe('active = ')
            accumulator_2599.append_boolean(True)
            q_1755: 'Query' = t_3525.where(accumulator_2599.accumulated).where_null(_sid('deleted_at'))
            def fn_3998() -> 'str29':
                return 'whereNull chained'
            test_131.assert_(q_1755.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL', fn_3998)
        finally:
            test_131.soft_fail_to_hard()
class TestCase167(TestCase48):
    def test___whereNotNullChainedWithOrWhere__2600(self) -> None:
        'whereNotNull chained with orWhere'
        test_132: Test = Test()
        try:
            t_3523: 'Query' = from_(_sid('users')).where_null(_sid('deleted_at'))
            accumulator_2601: 'SqlBuilder' = SqlBuilder()
            accumulator_2601.append_safe('role = ')
            accumulator_2601.append_string('admin')
            q_1757: 'Query' = t_3523.or_where(accumulator_2601.accumulated)
            def fn_3997() -> 'str29':
                return 'whereNotNull with orWhere'
            test_132.assert_(q_1757.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'", fn_3997)
        finally:
            test_132.soft_fail_to_hard()
class TestCase168(TestCase48):
    def test___whereInWithIntValues__2602(self) -> None:
        'whereIn with int values'
        test_133: Test = Test()
        try:
            q_1759: 'Query' = from_(_sid('users')).where_in(_sid('id'), (SqlInt32(1), SqlInt32(2), SqlInt32(3)))
            def fn_3996() -> 'str29':
                return 'whereIn ints'
            test_133.assert_(q_1759.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)', fn_3996)
        finally:
            test_133.soft_fail_to_hard()
class TestCase169(TestCase48):
    def test___whereInWithStringValuesEscaping__2603(self) -> None:
        'whereIn with string values escaping'
        test_134: Test = Test()
        try:
            q_1761: 'Query' = from_(_sid('users')).where_in(_sid('name'), (SqlString('Alice'), SqlString("Bob's")))
            def fn_3995() -> 'str29':
                return 'whereIn strings'
            test_134.assert_(q_1761.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')", fn_3995)
        finally:
            test_134.soft_fail_to_hard()
class TestCase170(TestCase48):
    def test___whereInWithEmptyListProduces1_0__2604(self) -> None:
        'whereIn with empty list produces 1=0'
        test_135: Test = Test()
        try:
            q_1763: 'Query' = from_(_sid('users')).where_in(_sid('id'), ())
            def fn_3994() -> 'str29':
                return 'whereIn empty'
            test_135.assert_(q_1763.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0', fn_3994)
        finally:
            test_135.soft_fail_to_hard()
class TestCase171(TestCase48):
    def test___whereInChained__2605(self) -> None:
        'whereIn chained'
        test_136: Test = Test()
        try:
            t_3521: 'Query' = from_(_sid('users'))
            accumulator_2606: 'SqlBuilder' = SqlBuilder()
            accumulator_2606.append_safe('active = ')
            accumulator_2606.append_boolean(True)
            q_1765: 'Query' = t_3521.where(accumulator_2606.accumulated).where_in(_sid('role'), (SqlString('admin'), SqlString('user')))
            def fn_3993() -> 'str29':
                return 'whereIn chained'
            test_136.assert_(q_1765.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')", fn_3993)
        finally:
            test_136.soft_fail_to_hard()
class TestCase172(TestCase48):
    def test___whereInSingleElement__2607(self) -> None:
        'whereIn single element'
        test_137: Test = Test()
        try:
            q_1767: 'Query' = from_(_sid('users')).where_in(_sid('id'), (SqlInt32(42),))
            def fn_3992() -> 'str29':
                return 'whereIn single'
            test_137.assert_(q_1767.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)', fn_3992)
        finally:
            test_137.soft_fail_to_hard()
class TestCase173(TestCase48):
    def test___whereNotBasic__2608(self) -> None:
        'whereNot basic'
        test_138: Test = Test()
        try:
            t_3519: 'Query' = from_(_sid('users'))
            accumulator_2609: 'SqlBuilder' = SqlBuilder()
            accumulator_2609.append_safe('active = ')
            accumulator_2609.append_boolean(True)
            q_1769: 'Query' = t_3519.where_not(accumulator_2609.accumulated)
            def fn_3991() -> 'str29':
                return 'whereNot'
            test_138.assert_(q_1769.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)', fn_3991)
        finally:
            test_138.soft_fail_to_hard()
class TestCase174(TestCase48):
    def test___whereNotChained__2610(self) -> None:
        'whereNot chained'
        test_139: Test = Test()
        try:
            t_3515: 'Query' = from_(_sid('users'))
            accumulator_2611: 'SqlBuilder' = SqlBuilder()
            accumulator_2611.append_safe('age > ')
            accumulator_2611.append_int32(18)
            t_3517: 'Query' = t_3515.where(accumulator_2611.accumulated)
            accumulator_2612: 'SqlBuilder' = SqlBuilder()
            accumulator_2612.append_safe('banned = ')
            accumulator_2612.append_boolean(True)
            q_1771: 'Query' = t_3517.where_not(accumulator_2612.accumulated)
            def fn_3990() -> 'str29':
                return 'whereNot chained'
            test_139.assert_(q_1771.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)', fn_3990)
        finally:
            test_139.soft_fail_to_hard()
class TestCase175(TestCase48):
    def test___whereBetweenIntegers__2613(self) -> None:
        'whereBetween integers'
        test_140: Test = Test()
        try:
            q_1773: 'Query' = from_(_sid('users')).where_between(_sid('age'), SqlInt32(18), SqlInt32(65))
            def fn_3989() -> 'str29':
                return 'whereBetween ints'
            test_140.assert_(q_1773.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65', fn_3989)
        finally:
            test_140.soft_fail_to_hard()
class TestCase176(TestCase48):
    def test___whereBetweenChained__2614(self) -> None:
        'whereBetween chained'
        test_141: Test = Test()
        try:
            t_3513: 'Query' = from_(_sid('users'))
            accumulator_2615: 'SqlBuilder' = SqlBuilder()
            accumulator_2615.append_safe('active = ')
            accumulator_2615.append_boolean(True)
            q_1775: 'Query' = t_3513.where(accumulator_2615.accumulated).where_between(_sid('age'), SqlInt32(21), SqlInt32(30))
            def fn_3988() -> 'str29':
                return 'whereBetween chained'
            test_141.assert_(q_1775.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30', fn_3988)
        finally:
            test_141.soft_fail_to_hard()
class TestCase177(TestCase48):
    def test___whereLikeBasic__2616(self) -> None:
        'whereLike basic'
        test_142: Test = Test()
        try:
            q_1777: 'Query' = from_(_sid('users')).where_like(_sid('name'), 'John%')
            def fn_3987() -> 'str29':
                return 'whereLike'
            test_142.assert_(q_1777.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'", fn_3987)
        finally:
            test_142.soft_fail_to_hard()
class TestCase178(TestCase48):
    def test___whereIlikeBasic__2617(self) -> None:
        'whereILike basic'
        test_143: Test = Test()
        try:
            q_1779: 'Query' = from_(_sid('users')).where_i_like(_sid('email'), '%@gmail.com')
            def fn_3986() -> 'str29':
                return 'whereILike'
            test_143.assert_(q_1779.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'", fn_3986)
        finally:
            test_143.soft_fail_to_hard()
class TestCase179(TestCase48):
    def test___whereLikeWithInjectionAttempt__2618(self) -> None:
        'whereLike with injection attempt'
        test_144: Test = Test()
        try:
            q_1781: 'Query' = from_(_sid('users')).where_like(_sid('name'), "'; DROP TABLE users; --")
            s_1782: 'str29' = q_1781.to_sql().to_string()
            t_3508: 'bool37' = s_1782.find("''") >= 0
            def fn_3985() -> 'str29':
                return _str_cat_4183('like injection escaped: ', s_1782)
            test_144.assert_(t_3508, fn_3985)
            t_3510: 'bool37' = s_1782.find('LIKE') >= 0
            def fn_3984() -> 'str29':
                return _str_cat_4183('like structure intact: ', s_1782)
            test_144.assert_(t_3510, fn_3984)
        finally:
            test_144.soft_fail_to_hard()
class TestCase180(TestCase48):
    def test___whereLikeWildcardPatterns__2619(self) -> None:
        'whereLike wildcard patterns'
        test_145: Test = Test()
        try:
            q_1784: 'Query' = from_(_sid('users')).where_like(_sid('name'), '%son%')
            def fn_3983() -> 'str29':
                return 'whereLike wildcard'
            test_145.assert_(q_1784.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'", fn_3983)
        finally:
            test_145.soft_fail_to_hard()
class TestCase181(TestCase48):
    def test___countAllProducesCount__2620(self) -> None:
        'countAll produces COUNT(*)'
        test_146: Test = Test()
        try:
            f_1786: 'SqlFragment' = count_all()
            def fn_3982() -> 'str29':
                return 'countAll'
            test_146.assert_(f_1786.to_string() == 'COUNT(*)', fn_3982)
        finally:
            test_146.soft_fail_to_hard()
class TestCase182(TestCase48):
    def test___countColProducesCountField__2621(self) -> None:
        'countCol produces COUNT(field)'
        test_147: Test = Test()
        try:
            f_1788: 'SqlFragment' = count_col(_sid('id'))
            def fn_3981() -> 'str29':
                return 'countCol'
            test_147.assert_(f_1788.to_string() == 'COUNT(id)', fn_3981)
        finally:
            test_147.soft_fail_to_hard()
class TestCase183(TestCase48):
    def test___sumColProducesSumField__2622(self) -> None:
        'sumCol produces SUM(field)'
        test_148: Test = Test()
        try:
            f_1790: 'SqlFragment' = sum_col(_sid('amount'))
            def fn_3980() -> 'str29':
                return 'sumCol'
            test_148.assert_(f_1790.to_string() == 'SUM(amount)', fn_3980)
        finally:
            test_148.soft_fail_to_hard()
class TestCase184(TestCase48):
    def test___avgColProducesAvgField__2623(self) -> None:
        'avgCol produces AVG(field)'
        test_149: Test = Test()
        try:
            f_1792: 'SqlFragment' = avg_col(_sid('price'))
            def fn_3979() -> 'str29':
                return 'avgCol'
            test_149.assert_(f_1792.to_string() == 'AVG(price)', fn_3979)
        finally:
            test_149.soft_fail_to_hard()
class TestCase185(TestCase48):
    def test___minColProducesMinField__2624(self) -> None:
        'minCol produces MIN(field)'
        test_150: Test = Test()
        try:
            f_1794: 'SqlFragment' = min_col(_sid('created_at'))
            def fn_3978() -> 'str29':
                return 'minCol'
            test_150.assert_(f_1794.to_string() == 'MIN(created_at)', fn_3978)
        finally:
            test_150.soft_fail_to_hard()
class TestCase186(TestCase48):
    def test___maxColProducesMaxField__2625(self) -> None:
        'maxCol produces MAX(field)'
        test_151: Test = Test()
        try:
            f_1796: 'SqlFragment' = max_col(_sid('score'))
            def fn_3977() -> 'str29':
                return 'maxCol'
            test_151.assert_(f_1796.to_string() == 'MAX(score)', fn_3977)
        finally:
            test_151.soft_fail_to_hard()
class TestCase187(TestCase48):
    def test___selectExprWithAggregate__2626(self) -> None:
        'selectExpr with aggregate'
        test_152: Test = Test()
        try:
            q_1798: 'Query' = from_(_sid('orders')).select_expr((count_all(),))
            def fn_3976() -> 'str29':
                return 'selectExpr count'
            test_152.assert_(q_1798.to_sql().to_string() == 'SELECT COUNT(*) FROM orders', fn_3976)
        finally:
            test_152.soft_fail_to_hard()
class TestCase188(TestCase48):
    def test___selectExprWithMultipleExpressions__2627(self) -> None:
        'selectExpr with multiple expressions'
        test_153: Test = Test()
        try:
            name_frag_1800: 'SqlFragment' = col(_sid('users'), _sid('name'))
            q_1801: 'Query' = from_(_sid('users')).select_expr((name_frag_1800, count_all()))
            def fn_3975() -> 'str29':
                return 'selectExpr multi'
            test_153.assert_(q_1801.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users', fn_3975)
        finally:
            test_153.soft_fail_to_hard()
class TestCase189(TestCase48):
    def test___selectExprOverridesSelectedFields__2628(self) -> None:
        'selectExpr overrides selectedFields'
        test_154: Test = Test()
        try:
            q_1803: 'Query' = from_(_sid('users')).select((_sid('id'), _sid('name'))).select_expr((count_all(),))
            def fn_3974() -> 'str29':
                return 'selectExpr overrides select'
            test_154.assert_(q_1803.to_sql().to_string() == 'SELECT COUNT(*) FROM users', fn_3974)
        finally:
            test_154.soft_fail_to_hard()
class TestCase190(TestCase48):
    def test___groupBySingleField__2629(self) -> None:
        'groupBy single field'
        test_155: Test = Test()
        try:
            q_1805: 'Query' = from_(_sid('orders')).select_expr((col(_sid('orders'), _sid('status')), count_all())).group_by(_sid('status'))
            def fn_3973() -> 'str29':
                return 'groupBy single'
            test_155.assert_(q_1805.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status', fn_3973)
        finally:
            test_155.soft_fail_to_hard()
class TestCase191(TestCase48):
    def test___groupByMultipleFields__2630(self) -> None:
        'groupBy multiple fields'
        test_156: Test = Test()
        try:
            q_1807: 'Query' = from_(_sid('orders')).group_by(_sid('status')).group_by(_sid('category'))
            def fn_3972() -> 'str29':
                return 'groupBy multiple'
            test_156.assert_(q_1807.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category', fn_3972)
        finally:
            test_156.soft_fail_to_hard()
class TestCase192(TestCase48):
    def test___havingBasic__2631(self) -> None:
        'having basic'
        test_157: Test = Test()
        try:
            t_3505: 'Query' = from_(_sid('orders')).select_expr((col(_sid('orders'), _sid('status')), count_all())).group_by(_sid('status'))
            accumulator_2632: 'SqlBuilder' = SqlBuilder()
            accumulator_2632.append_safe('COUNT(*) > ')
            accumulator_2632.append_int32(5)
            q_1809: 'Query' = t_3505.having(accumulator_2632.accumulated)
            def fn_3971() -> 'str29':
                return 'having basic'
            test_157.assert_(q_1809.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5', fn_3971)
        finally:
            test_157.soft_fail_to_hard()
class TestCase193(TestCase48):
    def test___orHaving__2633(self) -> None:
        'orHaving'
        test_158: Test = Test()
        try:
            t_3501: 'Query' = from_(_sid('orders')).group_by(_sid('status'))
            accumulator_2634: 'SqlBuilder' = SqlBuilder()
            accumulator_2634.append_safe('COUNT(*) > ')
            accumulator_2634.append_int32(5)
            t_3503: 'Query' = t_3501.having(accumulator_2634.accumulated)
            accumulator_2635: 'SqlBuilder' = SqlBuilder()
            accumulator_2635.append_safe('SUM(total) > ')
            accumulator_2635.append_int32(1000)
            q_1811: 'Query' = t_3503.or_having(accumulator_2635.accumulated)
            def fn_3970() -> 'str29':
                return 'orHaving'
            test_158.assert_(q_1811.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000', fn_3970)
        finally:
            test_158.soft_fail_to_hard()
class TestCase194(TestCase48):
    def test___distinctBasic__2636(self) -> None:
        'distinct basic'
        test_159: Test = Test()
        try:
            q_1813: 'Query' = from_(_sid('users')).select((_sid('name'),)).distinct()
            def fn_3969() -> 'str29':
                return 'distinct'
            test_159.assert_(q_1813.to_sql().to_string() == 'SELECT DISTINCT name FROM users', fn_3969)
        finally:
            test_159.soft_fail_to_hard()
class TestCase195(TestCase48):
    def test___distinctWithWhere__2637(self) -> None:
        'distinct with where'
        test_160: Test = Test()
        try:
            t_3499: 'Query' = from_(_sid('users')).select((_sid('email'),))
            accumulator_2638: 'SqlBuilder' = SqlBuilder()
            accumulator_2638.append_safe('active = ')
            accumulator_2638.append_boolean(True)
            q_1815: 'Query' = t_3499.where(accumulator_2638.accumulated).distinct()
            def fn_3968() -> 'str29':
                return 'distinct with where'
            test_160.assert_(q_1815.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE', fn_3968)
        finally:
            test_160.soft_fail_to_hard()
class TestCase196(TestCase48):
    def test___countSqlBare__2639(self) -> None:
        'countSql bare'
        test_161: Test = Test()
        try:
            q_1817: 'Query' = from_(_sid('users'))
            def fn_3967() -> 'str29':
                return 'countSql bare'
            test_161.assert_(q_1817.count_sql().to_string() == 'SELECT COUNT(*) FROM users', fn_3967)
        finally:
            test_161.soft_fail_to_hard()
class TestCase197(TestCase48):
    def test___countSqlWithWhere__2640(self) -> None:
        'countSql with WHERE'
        test_162: Test = Test()
        try:
            t_3497: 'Query' = from_(_sid('users'))
            accumulator_2641: 'SqlBuilder' = SqlBuilder()
            accumulator_2641.append_safe('active = ')
            accumulator_2641.append_boolean(True)
            q_1819: 'Query' = t_3497.where(accumulator_2641.accumulated)
            def fn_3966() -> 'str29':
                return 'countSql with where'
            test_162.assert_(q_1819.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE', fn_3966)
        finally:
            test_162.soft_fail_to_hard()
class TestCase198(TestCase48):
    def test___countSqlWithJoin__2642(self) -> None:
        'countSql with JOIN'
        test_163: Test = Test()
        try:
            t_3492: 'Query' = from_(_sid('users'))
            t_3493: 'SafeIdentifier' = _sid('orders')
            accumulator_2643: 'SqlBuilder' = SqlBuilder()
            accumulator_2643.append_safe('users.id = orders.user_id')
            t_3495: 'Query' = t_3492.inner_join(t_3493, accumulator_2643.accumulated)
            accumulator_2644: 'SqlBuilder' = SqlBuilder()
            accumulator_2644.append_safe('orders.total > ')
            accumulator_2644.append_int32(100)
            q_1821: 'Query' = t_3495.where(accumulator_2644.accumulated)
            def fn_3965() -> 'str29':
                return 'countSql with join'
            test_163.assert_(q_1821.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100', fn_3965)
        finally:
            test_163.soft_fail_to_hard()
class TestCase199(TestCase48):
    def test___countSqlDropsOrderByLimitOffset__2645(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_164: Test = Test()
        try:
            t_3489: 'Query' = from_(_sid('users'))
            accumulator_2646: 'SqlBuilder' = SqlBuilder()
            accumulator_2646.append_safe('active = ')
            accumulator_2646.append_boolean(True)
            t_3840: 'Query' = t_3489.where(accumulator_2646.accumulated).order_by(_sid('name'), True).limit(10)
            q_1823: 'Query' = t_3840.offset(20)
            s_1824: 'str29' = q_1823.count_sql().to_string()
            def fn_3964() -> 'str29':
                return _str_cat_4183('countSql drops extras: ', s_1824)
            test_164.assert_(s_1824 == 'SELECT COUNT(*) FROM users WHERE active = TRUE', fn_3964)
        finally:
            test_164.soft_fail_to_hard()
class TestCase200(TestCase48):
    def test___fullAggregationQuery__2647(self) -> None:
        'full aggregation query'
        test_165: Test = Test()
        try:
            t_3482: 'Query' = from_(_sid('orders')).select_expr((col(_sid('orders'), _sid('status')), count_all(), sum_col(_sid('total'))))
            t_3483: 'SafeIdentifier' = _sid('users')
            accumulator_2648: 'SqlBuilder' = SqlBuilder()
            accumulator_2648.append_safe('orders.user_id = users.id')
            t_3485: 'Query' = t_3482.inner_join(t_3483, accumulator_2648.accumulated)
            accumulator_2649: 'SqlBuilder' = SqlBuilder()
            accumulator_2649.append_safe('users.active = ')
            accumulator_2649.append_boolean(True)
            t_3487: 'Query' = t_3485.where(accumulator_2649.accumulated).group_by(_sid('status'))
            accumulator_2650: 'SqlBuilder' = SqlBuilder()
            accumulator_2650.append_safe('COUNT(*) > ')
            accumulator_2650.append_int32(3)
            q_1826: 'Query' = t_3487.having(accumulator_2650.accumulated).order_by(_sid('status'), True)
            expected_1827: 'str29' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_3963() -> 'str29':
                return 'full aggregation'
            test_165.assert_(q_1826.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC', fn_3963)
        finally:
            test_165.soft_fail_to_hard()
class TestCase201(TestCase48):
    def test___unionSql__2651(self) -> None:
        'unionSql'
        test_166: Test = Test()
        try:
            t_3478: 'Query' = from_(_sid('users'))
            accumulator_2652: 'SqlBuilder' = SqlBuilder()
            accumulator_2652.append_safe('role = ')
            accumulator_2652.append_string('admin')
            a_1829: 'Query' = t_3478.where(accumulator_2652.accumulated)
            t_3480: 'Query' = from_(_sid('users'))
            accumulator_2653: 'SqlBuilder' = SqlBuilder()
            accumulator_2653.append_safe('role = ')
            accumulator_2653.append_string('moderator')
            b_1830: 'Query' = t_3480.where(accumulator_2653.accumulated)
            s_1831: 'str29' = union_sql(a_1829, b_1830).to_string()
            def fn_3962() -> 'str29':
                return _str_cat_4183('unionSql: ', s_1831)
            test_166.assert_(s_1831 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')", fn_3962)
        finally:
            test_166.soft_fail_to_hard()
class TestCase202(TestCase48):
    def test___unionAllSql__2654(self) -> None:
        'unionAllSql'
        test_167: Test = Test()
        try:
            a_1833: 'Query' = from_(_sid('users')).select((_sid('name'),))
            b_1834: 'Query' = from_(_sid('contacts')).select((_sid('name'),))
            s_1835: 'str29' = union_all_sql(a_1833, b_1834).to_string()
            def fn_3961() -> 'str29':
                return _str_cat_4183('unionAllSql: ', s_1835)
            test_167.assert_(s_1835 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)', fn_3961)
        finally:
            test_167.soft_fail_to_hard()
class TestCase203(TestCase48):
    def test___intersectSql__2655(self) -> None:
        'intersectSql'
        test_168: Test = Test()
        try:
            a_1837: 'Query' = from_(_sid('users')).select((_sid('email'),))
            b_1838: 'Query' = from_(_sid('subscribers')).select((_sid('email'),))
            s_1839: 'str29' = intersect_sql(a_1837, b_1838).to_string()
            def fn_3960() -> 'str29':
                return _str_cat_4183('intersectSql: ', s_1839)
            test_168.assert_(s_1839 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)', fn_3960)
        finally:
            test_168.soft_fail_to_hard()
class TestCase204(TestCase48):
    def test___exceptSql__2656(self) -> None:
        'exceptSql'
        test_169: Test = Test()
        try:
            a_1841: 'Query' = from_(_sid('users')).select((_sid('id'),))
            b_1842: 'Query' = from_(_sid('banned')).select((_sid('id'),))
            s_1843: 'str29' = except_sql(a_1841, b_1842).to_string()
            def fn_3959() -> 'str29':
                return _str_cat_4183('exceptSql: ', s_1843)
            test_169.assert_(s_1843 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)', fn_3959)
        finally:
            test_169.soft_fail_to_hard()
class TestCase205(TestCase48):
    def test___subqueryWithAlias__2657(self) -> None:
        'subquery with alias'
        test_170: Test = Test()
        try:
            t_3476: 'Query' = from_(_sid('orders')).select((_sid('user_id'),))
            accumulator_2658: 'SqlBuilder' = SqlBuilder()
            accumulator_2658.append_safe('total > ')
            accumulator_2658.append_int32(100)
            inner_1845: 'Query' = t_3476.where(accumulator_2658.accumulated)
            s_1846: 'str29' = subquery(inner_1845, _sid('big_orders')).to_string()
            def fn_3958() -> 'str29':
                return _str_cat_4183('subquery: ', s_1846)
            test_170.assert_(s_1846 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders', fn_3958)
        finally:
            test_170.soft_fail_to_hard()
class TestCase206(TestCase48):
    def test___existsSql__2659(self) -> None:
        'existsSql'
        test_171: Test = Test()
        try:
            t_3474: 'Query' = from_(_sid('orders'))
            accumulator_2660: 'SqlBuilder' = SqlBuilder()
            accumulator_2660.append_safe('orders.user_id = users.id')
            inner_1848: 'Query' = t_3474.where(accumulator_2660.accumulated)
            s_1849: 'str29' = exists_sql(inner_1848).to_string()
            def fn_3957() -> 'str29':
                return _str_cat_4183('existsSql: ', s_1849)
            test_171.assert_(s_1849 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)', fn_3957)
        finally:
            test_171.soft_fail_to_hard()
class TestCase207(TestCase48):
    def test___whereInSubquery__2661(self) -> None:
        'whereInSubquery'
        test_172: Test = Test()
        try:
            t_3472: 'Query' = from_(_sid('orders')).select((_sid('user_id'),))
            accumulator_2662: 'SqlBuilder' = SqlBuilder()
            accumulator_2662.append_safe('total > ')
            accumulator_2662.append_int32(1000)
            sub_1851: 'Query' = t_3472.where(accumulator_2662.accumulated)
            q_1852: 'Query' = from_(_sid('users')).where_in_subquery(_sid('id'), sub_1851)
            s_1853: 'str29' = q_1852.to_sql().to_string()
            def fn_3956() -> 'str29':
                return _str_cat_4183('whereInSubquery: ', s_1853)
            test_172.assert_(s_1853 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)', fn_3956)
        finally:
            test_172.soft_fail_to_hard()
class TestCase208(TestCase48):
    def test___setOperationWithWhereOnEachSide__2663(self) -> None:
        'set operation with WHERE on each side'
        test_173: Test = Test()
        try:
            t_3466: 'Query' = from_(_sid('users'))
            accumulator_2664: 'SqlBuilder' = SqlBuilder()
            accumulator_2664.append_safe('age > ')
            accumulator_2664.append_int32(18)
            t_3468: 'Query' = t_3466.where(accumulator_2664.accumulated)
            accumulator_2665: 'SqlBuilder' = SqlBuilder()
            accumulator_2665.append_safe('active = ')
            accumulator_2665.append_boolean(True)
            a_1855: 'Query' = t_3468.where(accumulator_2665.accumulated)
            t_3470: 'Query' = from_(_sid('users'))
            accumulator_2666: 'SqlBuilder' = SqlBuilder()
            accumulator_2666.append_safe('role = ')
            accumulator_2666.append_string('vip')
            b_1856: 'Query' = t_3470.where(accumulator_2666.accumulated)
            s_1857: 'str29' = union_sql(a_1855, b_1856).to_string()
            def fn_3955() -> 'str29':
                return _str_cat_4183('union with where: ', s_1857)
            test_173.assert_(s_1857 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')", fn_3955)
        finally:
            test_173.soft_fail_to_hard()
class TestCase209(TestCase48):
    def test___whereInSubqueryChainedWithWhere__2667(self) -> None:
        'whereInSubquery chained with where'
        test_174: Test = Test()
        try:
            sub_1859: 'Query' = from_(_sid('orders')).select((_sid('user_id'),))
            t_3464: 'Query' = from_(_sid('users'))
            accumulator_2668: 'SqlBuilder' = SqlBuilder()
            accumulator_2668.append_safe('active = ')
            accumulator_2668.append_boolean(True)
            q_1860: 'Query' = t_3464.where(accumulator_2668.accumulated).where_in_subquery(_sid('id'), sub_1859)
            s_1861: 'str29' = q_1860.to_sql().to_string()
            def fn_3954() -> 'str29':
                return _str_cat_4183('whereInSubquery chained: ', s_1861)
            test_174.assert_(s_1861 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)', fn_3954)
        finally:
            test_174.soft_fail_to_hard()
class TestCase210(TestCase48):
    def test___existsSqlUsedInWhere__2669(self) -> None:
        'existsSql used in where'
        test_175: Test = Test()
        try:
            t_3462: 'Query' = from_(_sid('orders'))
            accumulator_2670: 'SqlBuilder' = SqlBuilder()
            accumulator_2670.append_safe('orders.user_id = users.id')
            sub_1863: 'Query' = t_3462.where(accumulator_2670.accumulated)
            q_1864: 'Query' = from_(_sid('users')).where(exists_sql(sub_1863))
            s_1865: 'str29' = q_1864.to_sql().to_string()
            def fn_3953() -> 'str29':
                return _str_cat_4183('exists in where: ', s_1865)
            test_175.assert_(s_1865 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)', fn_3953)
        finally:
            test_175.soft_fail_to_hard()
class TestCase211(TestCase48):
    def test___updateQueryBasic__2671(self) -> None:
        'UpdateQuery basic'
        test_176: Test = Test()
        try:
            t_3459: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('Alice'))
            accumulator_2672: 'SqlBuilder' = SqlBuilder()
            accumulator_2672.append_safe('id = ')
            accumulator_2672.append_int32(1)
            q_1867: 'SqlFragment' = t_3459.where(accumulator_2672.accumulated).to_sql()
            def fn_3952() -> 'str29':
                return 'update basic'
            test_176.assert_(q_1867.to_string() == "UPDATE users SET name = 'Alice' WHERE id = 1", fn_3952)
        finally:
            test_176.soft_fail_to_hard()
class TestCase212(TestCase48):
    def test___updateQueryMultipleSet__2673(self) -> None:
        'UpdateQuery multiple SET'
        test_177: Test = Test()
        try:
            t_3456: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('Bob')).set(_sid('age'), SqlInt32(30))
            accumulator_2674: 'SqlBuilder' = SqlBuilder()
            accumulator_2674.append_safe('id = ')
            accumulator_2674.append_int32(2)
            q_1869: 'SqlFragment' = t_3456.where(accumulator_2674.accumulated).to_sql()
            def fn_3951() -> 'str29':
                return 'update multi set'
            test_177.assert_(q_1869.to_string() == "UPDATE users SET name = 'Bob', age = 30 WHERE id = 2", fn_3951)
        finally:
            test_177.soft_fail_to_hard()
class TestCase213(TestCase48):
    def test___updateQueryMultipleWhere__2675(self) -> None:
        'UpdateQuery multiple WHERE'
        test_178: Test = Test()
        try:
            t_3451: 'UpdateQuery' = update(_sid('users')).set(_sid('active'), SqlBoolean(False))
            accumulator_2676: 'SqlBuilder' = SqlBuilder()
            accumulator_2676.append_safe('age < ')
            accumulator_2676.append_int32(18)
            t_3453: 'UpdateQuery' = t_3451.where(accumulator_2676.accumulated)
            accumulator_2677: 'SqlBuilder' = SqlBuilder()
            accumulator_2677.append_safe('role = ')
            accumulator_2677.append_string('guest')
            q_1871: 'SqlFragment' = t_3453.where(accumulator_2677.accumulated).to_sql()
            def fn_3950() -> 'str29':
                return 'update multi where'
            test_178.assert_(q_1871.to_string() == "UPDATE users SET active = FALSE WHERE age < 18 AND role = 'guest'", fn_3950)
        finally:
            test_178.soft_fail_to_hard()
class TestCase214(TestCase48):
    def test___updateQueryOrWhere__2678(self) -> None:
        'UpdateQuery orWhere'
        test_179: Test = Test()
        try:
            t_3446: 'UpdateQuery' = update(_sid('users')).set(_sid('status'), SqlString('banned'))
            accumulator_2679: 'SqlBuilder' = SqlBuilder()
            accumulator_2679.append_safe('spam_count > ')
            accumulator_2679.append_int32(10)
            t_3448: 'UpdateQuery' = t_3446.where(accumulator_2679.accumulated)
            accumulator_2680: 'SqlBuilder' = SqlBuilder()
            accumulator_2680.append_safe('reported = ')
            accumulator_2680.append_boolean(True)
            q_1873: 'SqlFragment' = t_3448.or_where(accumulator_2680.accumulated).to_sql()
            def fn_3949() -> 'str29':
                return 'update orWhere'
            test_179.assert_(q_1873.to_string() == "UPDATE users SET status = 'banned' WHERE spam_count > 10 OR reported = TRUE", fn_3949)
        finally:
            test_179.soft_fail_to_hard()
class TestCase215(TestCase48):
    def test___updateQueryBubblesWithoutWhere__2681(self) -> None:
        'UpdateQuery bubbles without WHERE'
        test_180: Test = Test()
        try:
            did_bubble_1875: 'bool37'
            try:
                update(_sid('users')).set(_sid('x'), SqlInt32(1)).to_sql()
                did_bubble_1875 = False
            except Exception41:
                did_bubble_1875 = True
            def fn_3948() -> 'str29':
                return 'update without WHERE should bubble'
            test_180.assert_(did_bubble_1875, fn_3948)
        finally:
            test_180.soft_fail_to_hard()
class TestCase216(TestCase48):
    def test___updateQueryBubblesWithoutSet__2682(self) -> None:
        'UpdateQuery bubbles without SET'
        test_181: Test = Test()
        try:
            did_bubble_1877: 'bool37'
            try:
                t_3442: 'UpdateQuery' = update(_sid('users'))
                accumulator_2683: 'SqlBuilder' = SqlBuilder()
                accumulator_2683.append_safe('id = ')
                accumulator_2683.append_int32(1)
                t_3442.where(accumulator_2683.accumulated).to_sql()
                did_bubble_1877 = False
            except Exception41:
                did_bubble_1877 = True
            def fn_3947() -> 'str29':
                return 'update without SET should bubble'
            test_181.assert_(did_bubble_1877, fn_3947)
        finally:
            test_181.soft_fail_to_hard()
class TestCase217(TestCase48):
    def test___updateQueryWithLimit__2684(self) -> None:
        'UpdateQuery with limit'
        test_182: Test = Test()
        try:
            t_3439: 'UpdateQuery' = update(_sid('users')).set(_sid('active'), SqlBoolean(False))
            accumulator_2685: 'SqlBuilder' = SqlBuilder()
            accumulator_2685.append_safe('last_login < ')
            accumulator_2685.append_string('2024-01-01')
            t_3839: 'UpdateQuery' = t_3439.where(accumulator_2685.accumulated).limit(100)
            q_1879: 'SqlFragment' = t_3839.to_sql()
            def fn_3946() -> 'str29':
                return 'update limit'
            test_182.assert_(q_1879.to_string() == "UPDATE users SET active = FALSE WHERE last_login < '2024-01-01' LIMIT 100", fn_3946)
        finally:
            test_182.soft_fail_to_hard()
class TestCase218(TestCase48):
    def test___updateQueryEscaping__2686(self) -> None:
        'UpdateQuery escaping'
        test_183: Test = Test()
        try:
            t_3436: 'UpdateQuery' = update(_sid('users')).set(_sid('bio'), SqlString("It's a test"))
            accumulator_2687: 'SqlBuilder' = SqlBuilder()
            accumulator_2687.append_safe('id = ')
            accumulator_2687.append_int32(1)
            q_1881: 'SqlFragment' = t_3436.where(accumulator_2687.accumulated).to_sql()
            def fn_3945() -> 'str29':
                return 'update escaping'
            test_183.assert_(q_1881.to_string() == "UPDATE users SET bio = 'It''s a test' WHERE id = 1", fn_3945)
        finally:
            test_183.soft_fail_to_hard()
class TestCase219(TestCase48):
    def test___deleteQueryBasic__2688(self) -> None:
        'DeleteQuery basic'
        test_184: Test = Test()
        try:
            t_3433: 'DeleteQuery' = delete_from(_sid('users'))
            accumulator_2689: 'SqlBuilder' = SqlBuilder()
            accumulator_2689.append_safe('id = ')
            accumulator_2689.append_int32(1)
            q_1883: 'SqlFragment' = t_3433.where(accumulator_2689.accumulated).to_sql()
            def fn_3944() -> 'str29':
                return 'delete basic'
            test_184.assert_(q_1883.to_string() == 'DELETE FROM users WHERE id = 1', fn_3944)
        finally:
            test_184.soft_fail_to_hard()
class TestCase220(TestCase48):
    def test___deleteQueryMultipleWhere__2690(self) -> None:
        'DeleteQuery multiple WHERE'
        test_185: Test = Test()
        try:
            t_3428: 'DeleteQuery' = delete_from(_sid('logs'))
            accumulator_2691: 'SqlBuilder' = SqlBuilder()
            accumulator_2691.append_safe('created_at < ')
            accumulator_2691.append_string('2024-01-01')
            t_3430: 'DeleteQuery' = t_3428.where(accumulator_2691.accumulated)
            accumulator_2692: 'SqlBuilder' = SqlBuilder()
            accumulator_2692.append_safe('level = ')
            accumulator_2692.append_string('debug')
            q_1885: 'SqlFragment' = t_3430.where(accumulator_2692.accumulated).to_sql()
            def fn_3943() -> 'str29':
                return 'delete multi where'
            test_185.assert_(q_1885.to_string() == "DELETE FROM logs WHERE created_at < '2024-01-01' AND level = 'debug'", fn_3943)
        finally:
            test_185.soft_fail_to_hard()
class TestCase221(TestCase48):
    def test___deleteQueryBubblesWithoutWhere__2693(self) -> None:
        'DeleteQuery bubbles without WHERE'
        test_186: Test = Test()
        try:
            did_bubble_1887: 'bool37'
            try:
                delete_from(_sid('users')).to_sql()
                did_bubble_1887 = False
            except Exception41:
                did_bubble_1887 = True
            def fn_3942() -> 'str29':
                return 'delete without WHERE should bubble'
            test_186.assert_(did_bubble_1887, fn_3942)
        finally:
            test_186.soft_fail_to_hard()
class TestCase222(TestCase48):
    def test___deleteQueryOrWhere__2694(self) -> None:
        'DeleteQuery orWhere'
        test_187: Test = Test()
        try:
            t_3422: 'DeleteQuery' = delete_from(_sid('sessions'))
            accumulator_2695: 'SqlBuilder' = SqlBuilder()
            accumulator_2695.append_safe('expired = ')
            accumulator_2695.append_boolean(True)
            t_3424: 'DeleteQuery' = t_3422.where(accumulator_2695.accumulated)
            accumulator_2696: 'SqlBuilder' = SqlBuilder()
            accumulator_2696.append_safe('created_at < ')
            accumulator_2696.append_string('2023-01-01')
            q_1889: 'SqlFragment' = t_3424.or_where(accumulator_2696.accumulated).to_sql()
            def fn_3941() -> 'str29':
                return 'delete orWhere'
            test_187.assert_(q_1889.to_string() == "DELETE FROM sessions WHERE expired = TRUE OR created_at < '2023-01-01'", fn_3941)
        finally:
            test_187.soft_fail_to_hard()
class TestCase223(TestCase48):
    def test___deleteQueryWithLimit__2697(self) -> None:
        'DeleteQuery with limit'
        test_188: Test = Test()
        try:
            t_3419: 'DeleteQuery' = delete_from(_sid('logs'))
            accumulator_2698: 'SqlBuilder' = SqlBuilder()
            accumulator_2698.append_safe('level = ')
            accumulator_2698.append_string('debug')
            t_3838: 'DeleteQuery' = t_3419.where(accumulator_2698.accumulated).limit(1000)
            q_1891: 'SqlFragment' = t_3838.to_sql()
            def fn_3940() -> 'str29':
                return 'delete limit'
            test_188.assert_(q_1891.to_string() == "DELETE FROM logs WHERE level = 'debug' LIMIT 1000", fn_3940)
        finally:
            test_188.soft_fail_to_hard()
class TestCase224(TestCase48):
    def test___orderByNullsNullsFirst__2699(self) -> None:
        'orderByNulls NULLS FIRST'
        test_189: Test = Test()
        try:
            q_1893: 'Query' = from_(_sid('users')).order_by_nulls(_sid('email'), True, NullsFirst())
            def fn_3939() -> 'str29':
                return 'nulls first'
            test_189.assert_(q_1893.to_sql().to_string() == 'SELECT * FROM users ORDER BY email ASC NULLS FIRST', fn_3939)
        finally:
            test_189.soft_fail_to_hard()
class TestCase225(TestCase48):
    def test___orderByNullsNullsLast__2700(self) -> None:
        'orderByNulls NULLS LAST'
        test_190: Test = Test()
        try:
            q_1895: 'Query' = from_(_sid('users')).order_by_nulls(_sid('score'), False, NullsLast())
            def fn_3938() -> 'str29':
                return 'nulls last'
            test_190.assert_(q_1895.to_sql().to_string() == 'SELECT * FROM users ORDER BY score DESC NULLS LAST', fn_3938)
        finally:
            test_190.soft_fail_to_hard()
class TestCase226(TestCase48):
    def test___mixedOrderByAndOrderByNulls__2701(self) -> None:
        'mixed orderBy and orderByNulls'
        test_191: Test = Test()
        try:
            q_1897: 'Query' = from_(_sid('users')).order_by(_sid('name'), True).order_by_nulls(_sid('email'), True, NullsFirst())
            def fn_3937() -> 'str29':
                return 'mixed order'
            test_191.assert_(q_1897.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC, email ASC NULLS FIRST', fn_3937)
        finally:
            test_191.soft_fail_to_hard()
class TestCase227(TestCase48):
    def test___crossJoin__2702(self) -> None:
        'crossJoin'
        test_192: Test = Test()
        try:
            q_1899: 'Query' = from_(_sid('users')).cross_join(_sid('colors'))
            def fn_3936() -> 'str29':
                return 'cross join'
            test_192.assert_(q_1899.to_sql().to_string() == 'SELECT * FROM users CROSS JOIN colors', fn_3936)
        finally:
            test_192.soft_fail_to_hard()
class TestCase228(TestCase48):
    def test___crossJoinCombinedWithOtherJoins__2703(self) -> None:
        'crossJoin combined with other joins'
        test_193: Test = Test()
        try:
            t_3416: 'Query' = from_(_sid('users'))
            t_3417: 'SafeIdentifier' = _sid('orders')
            accumulator_2704: 'SqlBuilder' = SqlBuilder()
            accumulator_2704.append_safe('users.id = orders.user_id')
            q_1901: 'Query' = t_3416.inner_join(t_3417, accumulator_2704.accumulated).cross_join(_sid('colors'))
            def fn_3935() -> 'str29':
                return 'cross + inner join'
            test_193.assert_(q_1901.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id CROSS JOIN colors', fn_3935)
        finally:
            test_193.soft_fail_to_hard()
class TestCase229(TestCase48):
    def test___lockForUpdate__2705(self) -> None:
        'lock FOR UPDATE'
        test_194: Test = Test()
        try:
            t_3414: 'Query' = from_(_sid('users'))
            accumulator_2706: 'SqlBuilder' = SqlBuilder()
            accumulator_2706.append_safe('id = ')
            accumulator_2706.append_int32(1)
            q_1903: 'Query' = t_3414.where(accumulator_2706.accumulated).lock(ForUpdate())
            def fn_3934() -> 'str29':
                return 'for update'
            test_194.assert_(q_1903.to_sql().to_string() == 'SELECT * FROM users WHERE id = 1 FOR UPDATE', fn_3934)
        finally:
            test_194.soft_fail_to_hard()
class TestCase230(TestCase48):
    def test___lockForShare__2707(self) -> None:
        'lock FOR SHARE'
        test_195: Test = Test()
        try:
            q_1905: 'Query' = from_(_sid('users')).select((_sid('name'),)).lock(ForShare())
            def fn_3933() -> 'str29':
                return 'for share'
            test_195.assert_(q_1905.to_sql().to_string() == 'SELECT name FROM users FOR SHARE', fn_3933)
        finally:
            test_195.soft_fail_to_hard()
class TestCase231(TestCase48):
    def test___lockWithFullQuery__2708(self) -> None:
        'lock with full query'
        test_196: Test = Test()
        try:
            t_3411: 'Query' = from_(_sid('accounts'))
            accumulator_2709: 'SqlBuilder' = SqlBuilder()
            accumulator_2709.append_safe('id = ')
            accumulator_2709.append_int32(42)
            t_3837: 'Query' = t_3411.where(accumulator_2709.accumulated).limit(1)
            q_1907: 'Query' = t_3837.lock(ForUpdate())
            def fn_3932() -> 'str29':
                return 'lock full query'
            test_196.assert_(q_1907.to_sql().to_string() == 'SELECT * FROM accounts WHERE id = 42 LIMIT 1 FOR UPDATE', fn_3932)
        finally:
            test_196.soft_fail_to_hard()
class TestCase232(TestCase48):
    def test___queryBuilderImmutabilityTwoQueriesFromSameBase__2710(self) -> None:
        'query builder immutability - two queries from same base'
        test_197: Test = Test()
        try:
            t_3407: 'Query' = from_(_sid('users'))
            accumulator_2711: 'SqlBuilder' = SqlBuilder()
            accumulator_2711.append_safe('active = ')
            accumulator_2711.append_boolean(True)
            base_1909: 'Query' = t_3407.where(accumulator_2711.accumulated)
            q1_1910: 'Query' = base_1909.limit(10)
            q2_1911: 'Query' = base_1909.limit(20)
            def fn_3931() -> 'str29':
                return 'q1'
            test_197.assert_(q1_1910.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE LIMIT 10', fn_3931)
            def fn_3930() -> 'str29':
                return 'q2'
            test_197.assert_(q2_1911.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE LIMIT 20', fn_3930)
        finally:
            test_197.soft_fail_to_hard()
class TestCase233(TestCase48):
    def test___limitZeroProducesLimit0__2712(self) -> None:
        'limit zero produces LIMIT 0'
        test_198: Test = Test()
        try:
            q_1913: 'Query' = from_(_sid('users')).limit(0)
            def fn_3929() -> 'str29':
                return 'limit 0'
            test_198.assert_(q_1913.to_sql().to_string() == 'SELECT * FROM users LIMIT 0', fn_3929)
        finally:
            test_198.soft_fail_to_hard()
class TestCase234(TestCase48):
    def test___safeToSqlWithZeroDefaultLimit__2713(self) -> None:
        'safeToSql with zero defaultLimit'
        test_199: Test = Test()
        try:
            q_1915: 'Query' = from_(_sid('users'))
            s_1916: 'SqlFragment' = q_1915.safe_to_sql(0)
            def fn_3928() -> 'str29':
                return 'safeToSql 0'
            test_199.assert_(s_1916.to_string() == 'SELECT * FROM users LIMIT 0', fn_3928)
        finally:
            test_199.soft_fail_to_hard()
class TestCase235(TestCase48):
    def test___updateQueryLimitBubblesOnNegative__2714(self) -> None:
        'UpdateQuery limit bubbles on negative'
        test_200: Test = Test()
        try:
            did_bubble_1918: 'bool37'
            try:
                t_3402: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('x'))
                accumulator_2715: 'SqlBuilder' = SqlBuilder()
                accumulator_2715.append_safe('id = ')
                accumulator_2715.append_int32(1)
                t_3402.where(accumulator_2715.accumulated).limit(-1)
                did_bubble_1918 = False
            except Exception41:
                did_bubble_1918 = True
            def fn_3927() -> 'str29':
                return 'UpdateQuery negative limit should bubble'
            test_200.assert_(did_bubble_1918, fn_3927)
        finally:
            test_200.soft_fail_to_hard()
class TestCase236(TestCase48):
    def test___deleteQueryLimitBubblesOnNegative__2716(self) -> None:
        'DeleteQuery limit bubbles on negative'
        test_201: Test = Test()
        try:
            did_bubble_1920: 'bool37'
            try:
                t_3399: 'DeleteQuery' = delete_from(_sid('users'))
                accumulator_2717: 'SqlBuilder' = SqlBuilder()
                accumulator_2717.append_safe('id = ')
                accumulator_2717.append_int32(1)
                t_3399.where(accumulator_2717.accumulated).limit(-1)
                did_bubble_1920 = False
            except Exception41:
                did_bubble_1920 = True
            def fn_3926() -> 'str29':
                return 'DeleteQuery negative limit should bubble'
            test_201.assert_(did_bubble_1920, fn_3926)
        finally:
            test_201.soft_fail_to_hard()
class TestCase237(TestCase48):
    def test___updateQueryImmutabilityTwoFromSameBase__2718(self) -> None:
        'UpdateQuery immutability - two from same base'
        test_202: Test = Test()
        try:
            t_3389: 'UpdateQuery' = update(_sid('users')).set(_sid('name'), SqlString('Alice'))
            accumulator_2719: 'SqlBuilder' = SqlBuilder()
            accumulator_2719.append_safe('id = ')
            accumulator_2719.append_int32(1)
            base_1922: 'UpdateQuery' = t_3389.where(accumulator_2719.accumulated)
            q1_1923: 'UpdateQuery' = base_1922.set(_sid('age'), SqlInt32(25))
            q2_1924: 'UpdateQuery' = base_1922.set(_sid('age'), SqlInt32(30))
            t_3390: 'SqlFragment' = q1_1923.to_sql()
            s1_1925: 'str29' = t_3390.to_string()
            t_3391: 'SqlFragment' = q2_1924.to_sql()
            s2_1926: 'str29' = t_3391.to_string()
            t_3392: 'bool37' = s1_1925.find('25') >= 0
            def fn_3925() -> 'str29':
                return _str_cat_4183('q1 should have 25: ', s1_1925)
            test_202.assert_(t_3392, fn_3925)
            t_3394: 'bool37' = s2_1926.find('30') >= 0
            def fn_3924() -> 'str29':
                return _str_cat_4183('q2 should have 30: ', s2_1926)
            test_202.assert_(t_3394, fn_3924)
            t_3396: 'bool37' = s1_1925.find('30') >= 0
            def fn_3923() -> 'str29':
                return _str_cat_4183('q1 should NOT have 30: ', s1_1925)
            test_202.assert_(not t_3396, fn_3923)
        finally:
            test_202.soft_fail_to_hard()
class TestCase238(TestCase48):
    def test___deleteQueryImmutability__2720(self) -> None:
        'DeleteQuery immutability'
        test_203: Test = Test()
        try:
            t_3374: 'DeleteQuery' = delete_from(_sid('users'))
            accumulator_2721: 'SqlBuilder' = SqlBuilder()
            accumulator_2721.append_safe('active = ')
            accumulator_2721.append_boolean(False)
            base_1928: 'DeleteQuery' = t_3374.where(accumulator_2721.accumulated)
            accumulator_2722: 'SqlBuilder' = SqlBuilder()
            accumulator_2722.append_safe('age < ')
            accumulator_2722.append_int32(18)
            q1_1929: 'DeleteQuery' = base_1928.where(accumulator_2722.accumulated)
            accumulator_2723: 'SqlBuilder' = SqlBuilder()
            accumulator_2723.append_safe('age > ')
            accumulator_2723.append_int32(65)
            q2_1930: 'DeleteQuery' = base_1928.where(accumulator_2723.accumulated)
            t_3377: 'SqlFragment' = q1_1929.to_sql()
            s1_1931: 'str29' = t_3377.to_string()
            t_3378: 'SqlFragment' = q2_1930.to_sql()
            s2_1932: 'str29' = t_3378.to_string()
            t_3379: 'bool37' = s1_1931.find('age < 18') >= 0
            def fn_3922() -> 'str29':
                return _str_cat_4183('q1: ', s1_1931)
            test_203.assert_(t_3379, fn_3922)
            t_3381: 'bool37' = s2_1932.find('age > 65') >= 0
            def fn_3921() -> 'str29':
                return _str_cat_4183('q2: ', s2_1932)
            test_203.assert_(t_3381, fn_3921)
            t_3383: 'bool37' = s1_1931.find('age > 65') >= 0
            def fn_3920() -> 'str29':
                return _str_cat_4183('q1 should not have q2 condition: ', s1_1931)
            test_203.assert_(not t_3383, fn_3920)
        finally:
            test_203.soft_fail_to_hard()
class TestCase239(TestCase48):
    def test___safeIdentifierAcceptsValidNames__2724(self) -> None:
        'safeIdentifier accepts valid names'
        test_204: Test = Test()
        try:
            id_1980: 'SafeIdentifier' = safe_identifier('user_name')
            def fn_3919() -> 'str29':
                return 'value should round-trip'
            test_204.assert_(id_1980.sql_value == 'user_name', fn_3919)
        finally:
            test_204.soft_fail_to_hard()
class TestCase240(TestCase48):
    def test___safeIdentifierRejectsEmptyString__2725(self) -> None:
        'safeIdentifier rejects empty string'
        test_205: Test = Test()
        try:
            did_bubble_1982: 'bool37'
            try:
                safe_identifier('')
                did_bubble_1982 = False
            except Exception41:
                did_bubble_1982 = True
            def fn_3918() -> 'str29':
                return 'empty string should bubble'
            test_205.assert_(did_bubble_1982, fn_3918)
        finally:
            test_205.soft_fail_to_hard()
class TestCase241(TestCase48):
    def test___safeIdentifierRejectsLeadingDigit__2726(self) -> None:
        'safeIdentifier rejects leading digit'
        test_206: Test = Test()
        try:
            did_bubble_1984: 'bool37'
            try:
                safe_identifier('1col')
                did_bubble_1984 = False
            except Exception41:
                did_bubble_1984 = True
            def fn_3917() -> 'str29':
                return 'leading digit should bubble'
            test_206.assert_(did_bubble_1984, fn_3917)
        finally:
            test_206.soft_fail_to_hard()
class TestCase242(TestCase48):
    def test___safeIdentifierRejectsSqlMetacharacters__2727(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_207: Test = Test()
        try:
            cases_1986: 'Sequence33[str29]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            this_3832: 'Sequence33[str29]' = cases_1986
            n_3834: 'int35' = _len_4174(this_3832)
            i_3835: 'int35' = 0
            while i_3835 < n_3834:
                el_3836: 'str29' = _list_get_4175(this_3832, i_3835)
                i_3835 = _int_add_4176(i_3835, 1)
                c_1987: 'str29' = el_3836
                did_bubble_1988: 'bool37'
                try:
                    safe_identifier(c_1987)
                    did_bubble_1988 = False
                except Exception41:
                    did_bubble_1988 = True
                def fn_3916() -> 'str29':
                    return _str_cat_4183('should reject: ', c_1987)
                test_207.assert_(did_bubble_1988, fn_3916)
        finally:
            test_207.soft_fail_to_hard()
class TestCase243(TestCase48):
    def test___tableDefFieldLookupFound__2728(self) -> None:
        'TableDef field lookup - found'
        test_208: Test = Test()
        try:
            t_3362: 'SafeIdentifier' = safe_identifier('users')
            t_3363: 'SafeIdentifier' = safe_identifier('name')
            t_3364: 'SafeIdentifier' = safe_identifier('age')
            td_1990: 'TableDef' = TableDef(t_3362, (FieldDef(t_3363, StringField(), False, None, False), FieldDef(t_3364, IntField(), False, None, False)), None)
            f_1991: 'FieldDef' = td_1990.field('age')
            def fn_3915() -> 'str29':
                return 'should find age field'
            test_208.assert_(f_1991.name.sql_value == 'age', fn_3915)
        finally:
            test_208.soft_fail_to_hard()
class TestCase244(TestCase48):
    def test___tableDefFieldLookupNotFoundBubbles__2729(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_209: Test = Test()
        try:
            t_3359: 'SafeIdentifier' = safe_identifier('users')
            t_3360: 'SafeIdentifier' = safe_identifier('name')
            td_1993: 'TableDef' = TableDef(t_3359, (FieldDef(t_3360, StringField(), False, None, False),), None)
            did_bubble_1994: 'bool37'
            try:
                td_1993.field('nonexistent')
                did_bubble_1994 = False
            except Exception41:
                did_bubble_1994 = True
            def fn_3914() -> 'str29':
                return 'unknown field should bubble'
            test_209.assert_(did_bubble_1994, fn_3914)
        finally:
            test_209.soft_fail_to_hard()
class TestCase245(TestCase48):
    def test___fieldDefNullableFlag__2730(self) -> None:
        'FieldDef nullable flag'
        test_210: Test = Test()
        try:
            t_3357: 'SafeIdentifier' = safe_identifier('email')
            required_1996: 'FieldDef' = FieldDef(t_3357, StringField(), False, None, False)
            t_3358: 'SafeIdentifier' = safe_identifier('bio')
            optional_1997: 'FieldDef' = FieldDef(t_3358, StringField(), True, None, False)
            def fn_3913() -> 'str29':
                return 'required field should not be nullable'
            test_210.assert_(not required_1996.nullable, fn_3913)
            def fn_3912() -> 'str29':
                return 'optional field should be nullable'
            test_210.assert_(optional_1997.nullable, fn_3912)
        finally:
            test_210.soft_fail_to_hard()
class TestCase246(TestCase48):
    def test___pkNameDefaultsToIdWhenPrimaryKeyIsNull__2731(self) -> None:
        'pkName defaults to id when primaryKey is null'
        test_211: Test = Test()
        try:
            t_3355: 'SafeIdentifier' = safe_identifier('users')
            t_3356: 'SafeIdentifier' = safe_identifier('name')
            td_1999: 'TableDef' = TableDef(t_3355, (FieldDef(t_3356, StringField(), False, None, False),), None)
            def fn_3911() -> 'str29':
                return 'default pk should be id'
            test_211.assert_(td_1999.pk_name() == 'id', fn_3911)
        finally:
            test_211.soft_fail_to_hard()
class TestCase247(TestCase48):
    def test___pkNameReturnsCustomPrimaryKey__2732(self) -> None:
        'pkName returns custom primary key'
        test_212: Test = Test()
        try:
            t_3351: 'SafeIdentifier' = safe_identifier('users')
            t_3352: 'SafeIdentifier' = safe_identifier('user_id')
            t_3354: 'Sequence33[FieldDef]' = (FieldDef(t_3352, IntField(), False, None, False),)
            t_3353: 'SafeIdentifier' = safe_identifier('user_id')
            td_2001: 'TableDef' = TableDef(t_3351, t_3354, t_3353)
            def fn_3910() -> 'str29':
                return 'custom pk should be user_id'
            test_212.assert_(td_2001.pk_name() == 'user_id', fn_3910)
        finally:
            test_212.soft_fail_to_hard()
class TestCase248(TestCase48):
    def test___timestampsReturnsTwoDateFieldDefs__2733(self) -> None:
        'timestamps returns two DateField defs'
        test_213: Test = Test()
        try:
            ts_2003: 'Sequence33[FieldDef]' = timestamps()
            def fn_3909() -> 'str29':
                return 'should return 2 fields'
            test_213.assert_(_len_4174(ts_2003) == 2, fn_3909)
            def fn_3908() -> 'str29':
                return 'first should be inserted_at'
            test_213.assert_(_list_get_4175(ts_2003, 0).name.sql_value == 'inserted_at', fn_3908)
            def fn_3907() -> 'str29':
                return 'second should be updated_at'
            test_213.assert_(_list_get_4175(ts_2003, 1).name.sql_value == 'updated_at', fn_3907)
            def fn_3906() -> 'str29':
                return 'inserted_at should be nullable'
            test_213.assert_(_list_get_4175(ts_2003, 0).nullable, fn_3906)
            def fn_3905() -> 'str29':
                return 'updated_at should be nullable'
            test_213.assert_(_list_get_4175(ts_2003, 1).nullable, fn_3905)
            def fn_3904() -> 'str29':
                return 'inserted_at should have default'
            test_213.assert_(not _list_get_4175(ts_2003, 0).default_value is None, fn_3904)
            def fn_3903() -> 'str29':
                return 'updated_at should have default'
            test_213.assert_(not _list_get_4175(ts_2003, 1).default_value is None, fn_3903)
        finally:
            test_213.soft_fail_to_hard()
class TestCase249(TestCase48):
    def test___fieldDefDefaultValueField__2734(self) -> None:
        'FieldDef defaultValue field'
        test_214: Test = Test()
        try:
            t_3348: 'SafeIdentifier' = safe_identifier('status')
            with_default_2005: 'FieldDef' = FieldDef(t_3348, StringField(), False, SqlDefault(), False)
            t_3349: 'SafeIdentifier' = safe_identifier('name')
            without_default_2006: 'FieldDef' = FieldDef(t_3349, StringField(), False, None, False)
            def fn_3902() -> 'str29':
                return 'should have default'
            test_214.assert_(not with_default_2005.default_value is None, fn_3902)
            def fn_3901() -> 'str29':
                return 'should not have default'
            test_214.assert_(without_default_2006.default_value is None, fn_3901)
        finally:
            test_214.soft_fail_to_hard()
class TestCase250(TestCase48):
    def test___fieldDefVirtualFlag__2735(self) -> None:
        'FieldDef virtual flag'
        test_215: Test = Test()
        try:
            t_3346: 'SafeIdentifier' = safe_identifier('name')
            normal_2008: 'FieldDef' = FieldDef(t_3346, StringField(), False, None, False)
            t_3347: 'SafeIdentifier' = safe_identifier('full_name')
            virt_2009: 'FieldDef' = FieldDef(t_3347, StringField(), True, None, True)
            def fn_3900() -> 'str29':
                return 'normal field should not be virtual'
            test_215.assert_(not normal_2008.virtual, fn_3900)
            def fn_3899() -> 'str29':
                return 'virtual field should be virtual'
            test_215.assert_(virt_2009.virtual, fn_3899)
        finally:
            test_215.soft_fail_to_hard()
class TestCase251(TestCase48):
    def test___safeIdentifierAcceptsSingleCharacterNames__2736(self) -> None:
        'safeIdentifier accepts single character names'
        test_216: Test = Test()
        try:
            a_2011: 'SafeIdentifier' = safe_identifier('a')
            def fn_3898() -> 'str29':
                return 'single letter should work'
            test_216.assert_(a_2011.sql_value == 'a', fn_3898)
            u_2012: 'SafeIdentifier' = safe_identifier('_')
            def fn_3897() -> 'str29':
                return 'single underscore should work'
            test_216.assert_(u_2012.sql_value == '_', fn_3897)
        finally:
            test_216.soft_fail_to_hard()
class TestCase252(TestCase48):
    def test___safeIdentifierAcceptsAllUnderscoreNames__2737(self) -> None:
        'safeIdentifier accepts all-underscore names'
        test_217: Test = Test()
        try:
            id_2014: 'SafeIdentifier' = safe_identifier('___')
            def fn_3896() -> 'str29':
                return 'all underscores should work'
            test_217.assert_(id_2014.sql_value == '___', fn_3896)
        finally:
            test_217.soft_fail_to_hard()
class TestCase253(TestCase48):
    def test___tableDefWithEmptyFieldList__2738(self) -> None:
        'TableDef with empty field list'
        test_218: Test = Test()
        try:
            t_3341: 'SafeIdentifier' = safe_identifier('empty')
            tbl_2016: 'TableDef' = TableDef(t_3341, (), None)
            did_bubble_2017: 'bool37'
            try:
                tbl_2016.field('anything')
                did_bubble_2017 = False
            except Exception41:
                did_bubble_2017 = True
            def fn_3895() -> 'str29':
                return 'field lookup on empty table should bubble'
            test_218.assert_(did_bubble_2017, fn_3895)
        finally:
            test_218.soft_fail_to_hard()
class TestCase254(TestCase48):
    def test___stringEscaping__2739(self) -> None:
        'string escaping'
        test_220: Test = Test()
        try:
            def build_2198(name_2200: 'str29', /) -> 'str29':
                accumulator_2740: 'SqlBuilder' = SqlBuilder()
                accumulator_2740.append_safe('select * from hi where name = ')
                accumulator_2740.append_string(name_2200)
                return accumulator_2740.accumulated.to_string()
            def build_wrong_2199(name_2202: 'str29', /) -> 'str29':
                return _str_cat_4183("select * from hi where name = '", name_2202, "'")
            def fn_3894() -> 'str29':
                return "expected build(\"world\") == (select * from hi where name = 'world') not (select * from hi where name = 'world')"
            test_220.assert_(True, fn_3894)
            bobby_tables_2204: 'str29' = "Robert'); drop table hi;--"
            def fn_3893() -> 'str29':
                return "expected build(bobbyTables) == (select * from hi where name = 'Robert''); drop table hi;--') not (select * from hi where name = 'Robert''); drop table hi;--')"
            test_220.assert_(True, fn_3893)
            def fn_3892() -> 'str29':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_220.assert_(True, fn_3892)
        finally:
            test_220.soft_fail_to_hard()
class TestCase255(TestCase48):
    def test___stringEdgeCases__2747(self) -> None:
        'string edge cases'
        test_221: Test = Test()
        try:
            accumulator_2750: 'SqlBuilder' = SqlBuilder()
            accumulator_2750.append_safe('v = ')
            accumulator_2750.append_string('')
            actual_2748: 'str29' = accumulator_2750.accumulated.to_string()
            def fn_3891() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_2748, ')')
            test_221.assert_(actual_2748 == "v = ''", fn_3891)
            accumulator_2753: 'SqlBuilder' = SqlBuilder()
            accumulator_2753.append_safe('v = ')
            accumulator_2753.append_string("a''b")
            actual_2751: 'str29' = accumulator_2753.accumulated.to_string()
            def fn_3890() -> 'str29':
                return _str_cat_4183("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_2751, ')')
            test_221.assert_(actual_2751 == "v = 'a''''b'", fn_3890)
            accumulator_2756: 'SqlBuilder' = SqlBuilder()
            accumulator_2756.append_safe('v = ')
            accumulator_2756.append_string('Hello \u4e16\u754c')
            actual_2754: 'str29' = accumulator_2756.accumulated.to_string()
            def fn_3889() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_2754, ')')
            test_221.assert_(actual_2754 == "v = 'Hello \u4e16\u754c'", fn_3889)
            accumulator_2759: 'SqlBuilder' = SqlBuilder()
            accumulator_2759.append_safe('v = ')
            accumulator_2759.append_string('Line1\nLine2')
            actual_2757: 'str29' = accumulator_2759.accumulated.to_string()
            def fn_3888() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_2757, ')')
            test_221.assert_(actual_2757 == "v = 'Line1\nLine2'", fn_3888)
        finally:
            test_221.soft_fail_to_hard()
class TestCase256(TestCase48):
    def test___numbersAndBooleans__2760(self) -> None:
        'numbers and booleans'
        test_222: Test = Test()
        try:
            accumulator_2763: 'SqlBuilder' = SqlBuilder()
            accumulator_2763.append_safe('select ')
            accumulator_2763.append_int32(42)
            accumulator_2763.append_safe(', ')
            accumulator_2763.append_int64(43)
            accumulator_2763.append_safe(', ')
            accumulator_2763.append_float64(19.99)
            accumulator_2763.append_safe(', ')
            accumulator_2763.append_boolean(True)
            accumulator_2763.append_safe(', ')
            accumulator_2763.append_boolean(False)
            actual_2761: 'str29' = accumulator_2763.accumulated.to_string()
            def fn_3887() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_2761, ')')
            test_222.assert_(actual_2761 == 'select 42, 43, 19.99, TRUE, FALSE', fn_3887)
            date_2207: 'date28' = _date_4209(2024, 12, 25)
            accumulator_2766: 'SqlBuilder' = SqlBuilder()
            accumulator_2766.append_safe('insert into t values (')
            accumulator_2766.append_date(date_2207)
            accumulator_2766.append_safe(')')
            actual_2764: 'str29' = accumulator_2766.accumulated.to_string()
            def fn_3886() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_2764, ')')
            test_222.assert_(actual_2764 == "insert into t values ('2024-12-25')", fn_3886)
        finally:
            test_222.soft_fail_to_hard()
class TestCase257(TestCase48):
    def test___lists__2767(self) -> None:
        'lists'
        test_223: Test = Test()
        try:
            accumulator_2770: 'SqlBuilder' = SqlBuilder()
            accumulator_2770.append_safe('v IN (')
            accumulator_2770.append_string_list(('a', 'b', "c'd"))
            accumulator_2770.append_safe(')')
            actual_2768: 'str29' = accumulator_2770.accumulated.to_string()
            def fn_3885() -> 'str29':
                return _str_cat_4183("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_2768, ')')
            test_223.assert_(actual_2768 == "v IN ('a', 'b', 'c''d')", fn_3885)
            accumulator_2773: 'SqlBuilder' = SqlBuilder()
            accumulator_2773.append_safe('v IN (')
            accumulator_2773.append_int32_list((1, 2, 3))
            accumulator_2773.append_safe(')')
            actual_2771: 'str29' = accumulator_2773.accumulated.to_string()
            def fn_3884() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_2771, ')')
            test_223.assert_(actual_2771 == 'v IN (1, 2, 3)', fn_3884)
            accumulator_2776: 'SqlBuilder' = SqlBuilder()
            accumulator_2776.append_safe('v IN (')
            accumulator_2776.append_int64_list((1, 2))
            accumulator_2776.append_safe(')')
            actual_2774: 'str29' = accumulator_2776.accumulated.to_string()
            def fn_3883() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_2774, ')')
            test_223.assert_(actual_2774 == 'v IN (1, 2)', fn_3883)
            accumulator_2779: 'SqlBuilder' = SqlBuilder()
            accumulator_2779.append_safe('v IN (')
            accumulator_2779.append_float64_list((1.0, 2.0))
            accumulator_2779.append_safe(')')
            actual_2777: 'str29' = accumulator_2779.accumulated.to_string()
            def fn_3882() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_2777, ')')
            test_223.assert_(actual_2777 == 'v IN (1.0, 2.0)', fn_3882)
            accumulator_2782: 'SqlBuilder' = SqlBuilder()
            accumulator_2782.append_safe('v IN (')
            accumulator_2782.append_boolean_list((True, False))
            accumulator_2782.append_safe(')')
            actual_2780: 'str29' = accumulator_2782.accumulated.to_string()
            def fn_3881() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_2780, ')')
            test_223.assert_(actual_2780 == 'v IN (TRUE, FALSE)', fn_3881)
            t_3330: 'date28' = _date_4209(2024, 1, 1)
            t_3331: 'date28' = _date_4209(2024, 12, 25)
            dates_2209: 'Sequence33[date28]' = (t_3330, t_3331)
            accumulator_2785: 'SqlBuilder' = SqlBuilder()
            accumulator_2785.append_safe('v IN (')
            accumulator_2785.append_date_list(dates_2209)
            accumulator_2785.append_safe(')')
            actual_2783: 'str29' = accumulator_2785.accumulated.to_string()
            def fn_3880() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_2783, ')')
            test_223.assert_(actual_2783 == "v IN ('2024-01-01', '2024-12-25')", fn_3880)
        finally:
            test_223.soft_fail_to_hard()
class TestCase258(TestCase48):
    def test___sqlFloat64_naNRendersAsNull__2786(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_224: Test = Test()
        try:
            nan_2211: 'float31' = nan259
            accumulator_2789: 'SqlBuilder' = SqlBuilder()
            accumulator_2789.append_safe('v = ')
            accumulator_2789.append_float64(nan259)
            actual_2787: 'str29' = accumulator_2789.accumulated.to_string()
            def fn_3879() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_2787, ')')
            test_224.assert_(actual_2787 == 'v = NULL', fn_3879)
        finally:
            test_224.soft_fail_to_hard()
class TestCase260(TestCase48):
    def test___sqlFloat64_infinityRendersAsNull__2790(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_225: Test = Test()
        try:
            inf_2213: 'float31' = inf261
            accumulator_2793: 'SqlBuilder' = SqlBuilder()
            accumulator_2793.append_safe('v = ')
            accumulator_2793.append_float64(inf261)
            actual_2791: 'str29' = accumulator_2793.accumulated.to_string()
            def fn_3878() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_2791, ')')
            test_225.assert_(actual_2791 == 'v = NULL', fn_3878)
        finally:
            test_225.soft_fail_to_hard()
class TestCase262(TestCase48):
    def test___sqlFloat64_negativeInfinityRendersAsNull__2794(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_226: Test = Test()
        try:
            ninf_2215: 'float31' = -inf261
            accumulator_2797: 'SqlBuilder' = SqlBuilder()
            accumulator_2797.append_safe('v = ')
            accumulator_2797.append_float64(-inf261)
            actual_2795: 'str29' = accumulator_2797.accumulated.to_string()
            def fn_3877() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_2795, ')')
            test_226.assert_(actual_2795 == 'v = NULL', fn_3877)
        finally:
            test_226.soft_fail_to_hard()
class TestCase263(TestCase48):
    def test___sqlFloat64_normalValuesStillWork__2798(self) -> None:
        'SqlFloat64 normal values still work'
        test_227: Test = Test()
        try:
            accumulator_2801: 'SqlBuilder' = SqlBuilder()
            accumulator_2801.append_safe('v = ')
            accumulator_2801.append_float64(3.14)
            actual_2799: 'str29' = accumulator_2801.accumulated.to_string()
            def fn_3876() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_2799, ')')
            test_227.assert_(actual_2799 == 'v = 3.14', fn_3876)
            accumulator_2804: 'SqlBuilder' = SqlBuilder()
            accumulator_2804.append_safe('v = ')
            accumulator_2804.append_float64(0.0)
            actual_2802: 'str29' = accumulator_2804.accumulated.to_string()
            def fn_3875() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_2802, ')')
            test_227.assert_(actual_2802 == 'v = 0.0', fn_3875)
            accumulator_2807: 'SqlBuilder' = SqlBuilder()
            accumulator_2807.append_safe('v = ')
            accumulator_2807.append_float64(-42.5)
            actual_2805: 'str29' = accumulator_2807.accumulated.to_string()
            def fn_3874() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_2805, ')')
            test_227.assert_(actual_2805 == 'v = -42.5', fn_3874)
        finally:
            test_227.soft_fail_to_hard()
class TestCase264(TestCase48):
    def test___sqlDateRendersWithQuotes__2808(self) -> None:
        'SqlDate renders with quotes'
        test_228: Test = Test()
        try:
            d_2218: 'date28' = _date_4209(2024, 6, 15)
            accumulator_2811: 'SqlBuilder' = SqlBuilder()
            accumulator_2811.append_safe('v = ')
            accumulator_2811.append_date(d_2218)
            actual_2809: 'str29' = accumulator_2811.accumulated.to_string()
            def fn_3873() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_2809, ')')
            test_228.assert_(actual_2809 == "v = '2024-06-15'", fn_3873)
        finally:
            test_228.soft_fail_to_hard()
class TestCase265(TestCase48):
    def test___nesting__2812(self) -> None:
        'nesting'
        test_229: Test = Test()
        try:
            name_2220: 'str29' = 'Someone'
            accumulator_2813: 'SqlBuilder' = SqlBuilder()
            accumulator_2813.append_safe('where p.last_name = ')
            accumulator_2813.append_string('Someone')
            condition_2221: 'SqlFragment' = accumulator_2813.accumulated
            accumulator_2816: 'SqlBuilder' = SqlBuilder()
            accumulator_2816.append_safe('select p.id from person p ')
            accumulator_2816.append_fragment(condition_2221)
            actual_2814: 'str29' = accumulator_2816.accumulated.to_string()
            def fn_3872() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2814, ')')
            test_229.assert_(actual_2814 == "select p.id from person p where p.last_name = 'Someone'", fn_3872)
            accumulator_2819: 'SqlBuilder' = SqlBuilder()
            accumulator_2819.append_safe('select p.id from person p ')
            accumulator_2819.append_part(condition_2221.to_source())
            actual_2817: 'str29' = accumulator_2819.accumulated.to_string()
            def fn_3871() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2817, ')')
            test_229.assert_(actual_2817 == "select p.id from person p where p.last_name = 'Someone'", fn_3871)
            parts_2222: 'Sequence33[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            accumulator_2822: 'SqlBuilder' = SqlBuilder()
            accumulator_2822.append_safe('select ')
            accumulator_2822.append_part_list(parts_2222)
            actual_2820: 'str29' = accumulator_2822.accumulated.to_string()
            def fn_3870() -> 'str29':
                return _str_cat_4183('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_2820, ')')
            test_229.assert_(actual_2820 == "select 'a''b', 3", fn_3870)
        finally:
            test_229.soft_fail_to_hard()
class TestCase266(TestCase48):
    def test___sqlInt32_negativeAndZeroValues__2823(self) -> None:
        'SqlInt32 negative and zero values'
        test_230: Test = Test()
        try:
            accumulator_2824: 'SqlBuilder' = SqlBuilder()
            accumulator_2824.append_safe('v = ')
            accumulator_2824.append_int32(-42)
            t_3311: 'SqlFragment' = accumulator_2824.accumulated
            def fn_3869() -> 'str29':
                return 'negative int'
            test_230.assert_(t_3311.to_string() == 'v = -42', fn_3869)
            accumulator_2825: 'SqlBuilder' = SqlBuilder()
            accumulator_2825.append_safe('v = ')
            accumulator_2825.append_int32(0)
            t_3312: 'SqlFragment' = accumulator_2825.accumulated
            def fn_3868() -> 'str29':
                return 'zero int'
            test_230.assert_(t_3312.to_string() == 'v = 0', fn_3868)
        finally:
            test_230.soft_fail_to_hard()
class TestCase267(TestCase48):
    def test___sqlInt64_negativeValue__2826(self) -> None:
        'SqlInt64 negative value'
        test_231: Test = Test()
        try:
            accumulator_2827: 'SqlBuilder' = SqlBuilder()
            accumulator_2827.append_safe('v = ')
            accumulator_2827.append_int64(-99)
            t_3310: 'SqlFragment' = accumulator_2827.accumulated
            def fn_3867() -> 'str29':
                return 'negative int64'
            test_231.assert_(t_3310.to_string() == 'v = -99', fn_3867)
        finally:
            test_231.soft_fail_to_hard()
class TestCase268(TestCase48):
    def test___singleElementListRendering__2828(self) -> None:
        'single element list rendering'
        test_232: Test = Test()
        try:
            accumulator_2829: 'SqlBuilder' = SqlBuilder()
            accumulator_2829.append_safe('v IN (')
            accumulator_2829.append_int32_list((42,))
            accumulator_2829.append_safe(')')
            t_3308: 'SqlFragment' = accumulator_2829.accumulated
            def fn_3866() -> 'str29':
                return 'single int'
            test_232.assert_(t_3308.to_string() == 'v IN (42)', fn_3866)
            accumulator_2830: 'SqlBuilder' = SqlBuilder()
            accumulator_2830.append_safe('v IN (')
            accumulator_2830.append_string_list(('only',))
            accumulator_2830.append_safe(')')
            t_3309: 'SqlFragment' = accumulator_2830.accumulated
            def fn_3865() -> 'str29':
                return 'single string'
            test_232.assert_(t_3309.to_string() == "v IN ('only')", fn_3865)
        finally:
            test_232.soft_fail_to_hard()
class TestCase269(TestCase48):
    def test___sqlDefaultRendersDefaultKeyword__2831(self) -> None:
        'SqlDefault renders DEFAULT keyword'
        test_233: Test = Test()
        try:
            b_2227: 'SqlBuilder' = SqlBuilder()
            b_2227.append_safe('v = ')
            b_2227.append_part(SqlDefault())
            def fn_3864() -> 'str29':
                return 'default keyword'
            test_233.assert_(b_2227.accumulated.to_string() == 'v = DEFAULT', fn_3864)
        finally:
            test_233.soft_fail_to_hard()
class TestCase270(TestCase48):
    def test___sqlStringWithBackslash__2832(self) -> None:
        'SqlString with backslash'
        test_234: Test = Test()
        try:
            accumulator_2833: 'SqlBuilder' = SqlBuilder()
            accumulator_2833.append_safe('v = ')
            accumulator_2833.append_string('a\\b')
            t_3307: 'SqlFragment' = accumulator_2833.accumulated
            def fn_3863() -> 'str29':
                return 'backslash passthrough'
            test_234.assert_(t_3307.to_string() == "v = 'a\\b'", fn_3863)
        finally:
            test_234.soft_fail_to_hard()
class TestCase271(TestCase48):
    def test___toParameterizedNumbersTheValuesAndKeepsThemOutOfTheText__2834(self) -> None:
        'toParameterized numbers the values and keeps them out of the text'
        test_235: Test = Test()
        try:
            name_2230: 'str29' = "O'Brien; drop table people"
            accumulator_2835: 'SqlBuilder' = SqlBuilder()
            accumulator_2835.append_safe('select * from people where name = ')
            accumulator_2835.append_string("O'Brien; drop table people")
            accumulator_2835.append_safe(' and age > ')
            accumulator_2835.append_int32(30)
            accumulator_2835.append_safe(' and height < ')
            accumulator_2835.append_float64(1.5)
            p_2231: 'ParameterizedSql' = accumulator_2835.accumulated.to_parameterized()
            def fn_3862() -> 'str29':
                return p_2231.text
            test_235.assert_(p_2231.text == 'select * from people where name = $1 and age > $2 and height < $3', fn_3862)
            def fn_3861() -> 'str29':
                return 'three params'
            test_235.assert_(_len_4174(p_2231.params) == 3, fn_3861)
            def fn_3860() -> 'str29':
                return _list_get_4175(p_2231.params, 0)
            test_235.assert_(_list_get_4175(p_2231.params, 0) == "O'Brien; drop table people", fn_3860)
            def fn_3859() -> 'str29':
                return _list_get_4175(p_2231.params, 1)
            test_235.assert_(_list_get_4175(p_2231.params, 1) == '30', fn_3859)
            def fn_3858() -> 'str29':
                return _list_get_4175(p_2231.params, 2)
            test_235.assert_(_list_get_4175(p_2231.params, 2) == '1.5', fn_3858)
        finally:
            test_235.soft_fail_to_hard()
class TestCase272(TestCase48):
    def test___toParameterizedLeavesWhatIsNotDataInTheText__2836(self) -> None:
        'toParameterized leaves what is not data in the text'
        test_236: Test = Test()
        try:
            t_3304: 'bool37'
            b_2233: 'SqlBuilder' = SqlBuilder()
            b_2233.append_safe('insert into t (a, b, c, d) values (')
            b_2233.append_boolean(True)
            b_2233.append_safe(', ')
            b_2233.append_part(SqlDefault())
            b_2233.append_safe(', ')
            b_2233.append_float64(nan259)
            b_2233.append_safe(', ')
            b_2233.append_int64(-7)
            b_2233.append_safe(')')
            p_2234: 'ParameterizedSql' = b_2233.accumulated.to_parameterized()
            def fn_3857() -> 'str29':
                return p_2234.text
            test_236.assert_(p_2234.text == 'insert into t (a, b, c, d) values (TRUE, DEFAULT, NULL, $1)', fn_3857)
            if _len_4174(p_2234.params) == 1:
                t_3304 = _list_get_4175(p_2234.params, 0) == '-7'
            else:
                t_3304 = False
            def fn_3856() -> 'str29':
                return 'one param'
            test_236.assert_(t_3304, fn_3856)
        finally:
            test_236.soft_fail_to_hard()
class TestCase273(TestCase48):
    def test___toParameterizedWorksOnAWholeQuery__2837(self) -> None:
        'toParameterized works on a whole query'
        test_237: Test = Test()
        try:
            t_3302: 'bool37'
            t_3297: 'SafeIdentifier' = safe_identifier('users')
            t_3299: 'Query' = from_(t_3297)
            accumulator_2838: 'SqlBuilder' = SqlBuilder()
            accumulator_2838.append_safe('email = ')
            accumulator_2838.append_string('a@b.c')
            t_3301: 'Query' = t_3299.where(accumulator_2838.accumulated)
            accumulator_2839: 'SqlBuilder' = SqlBuilder()
            accumulator_2839.append_safe('id = ')
            accumulator_2839.append_int32(7)
            p_2236: 'ParameterizedSql' = t_3301.or_where(accumulator_2839.accumulated).to_sql().to_parameterized()
            def fn_3855() -> 'str29':
                return p_2236.text
            test_237.assert_(p_2236.text == 'SELECT * FROM users WHERE email = $1 OR id = $2', fn_3855)
            if _list_get_4175(p_2236.params, 0) == 'a@b.c':
                t_3302 = _list_get_4175(p_2236.params, 1) == '7'
            else:
                t_3302 = False
            def fn_3854() -> 'str29':
                return 'params in order'
            test_237.assert_(t_3302, fn_3854)
        finally:
            test_237.soft_fail_to_hard()
class TestCase274(TestCase48):
    def test___toParameterizedWithNoValuesIsTheSameTextAsToString__2840(self) -> None:
        'toParameterized with no values is the same text as toString'
        test_238: Test = Test()
        try:
            accumulator_2841: 'SqlBuilder' = SqlBuilder()
            accumulator_2841.append_safe('select 1')
            f_2238: 'SqlFragment' = accumulator_2841.accumulated
            actual_2842: 'str29' = f_2238.to_parameterized().text
            expected_2843: 'str29' = f_2238.to_string()
            def fn_3853() -> 'str29':
                return _str_cat_4183('expected f.toParameterized().text == (', expected_2843, ') not (', actual_2842, ')')
            test_238.assert_(actual_2842 == expected_2843, fn_3853)
            actual_2844: 'int35' = _len_4174(f_2238.to_parameterized().params)
            def fn_3852() -> 'str29':
                return _str_cat_4183('expected f.toParameterized().params.length == (', _int_to_string_4184(0), ') not (', _int_to_string_4184(actual_2844), ')')
            test_238.assert_(actual_2844 == 0, fn_3852)
        finally:
            test_238.soft_fail_to_hard()
