from temper_std.testing import Test
from builtins import str as str34, bool as bool42, Exception as Exception46, int as int40, float as float36
from unittest import TestCase as TestCase53
from types import MappingProxyType as MappingProxyType41
from typing import Sequence as Sequence38
from datetime import date as date33
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_14328, pair_14329, changeset, Changeset, mapped_has_14293, len_14296, list_get_14304, str_cat_14298, list_for_each_14290, SqlFragment, NumberValidationOpts, from_, Query, SqlBuilder, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, update, UpdateQuery, SqlBoolean, delete_from, DeleteQuery, NullsFirst, NullsLast, ForUpdate, ForShare, date_14330, SqlPart
def csid_636(name_924: 'str34') -> 'SafeIdentifier':
    t_7681: 'SafeIdentifier'
    t_7681 = safe_identifier(name_924)
    return t_7681
def user_table_637() -> 'TableDef':
    return TableDef(csid_636('users'), (FieldDef(csid_636('name'), StringField(), False), FieldDef(csid_636('email'), StringField(), False), FieldDef(csid_636('age'), IntField(), True), FieldDef(csid_636('score'), FloatField(), True), FieldDef(csid_636('active'), BoolField(), True)))
class TestCase52(TestCase53):
    def test___castWhitelistsAllowedFields__2009(self) -> None:
        'cast whitelists allowed fields'
        test_31: Test = Test()
        try:
            params_928: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'), pair_14329('email', 'alice@example.com'), pair_14329('admin', 'true')))
            t_13823: 'TableDef' = user_table_637()
            t_13824: 'SafeIdentifier' = csid_636('name')
            t_13825: 'SafeIdentifier' = csid_636('email')
            cs_929: 'Changeset' = changeset(t_13823, params_928).cast((t_13824, t_13825))
            t_13828: 'bool42' = mapped_has_14293(cs_929.changes, 'name')
            def fn_13818() -> 'str34':
                return 'name should be in changes'
            test_31.assert_(t_13828, fn_13818)
            t_13832: 'bool42' = mapped_has_14293(cs_929.changes, 'email')
            def fn_13817() -> 'str34':
                return 'email should be in changes'
            test_31.assert_(t_13832, fn_13817)
            t_13838: 'bool42' = not mapped_has_14293(cs_929.changes, 'admin')
            def fn_13816() -> 'str34':
                return 'admin must be dropped (not in whitelist)'
            test_31.assert_(t_13838, fn_13816)
            t_13840: 'bool42' = cs_929.is_valid
            def fn_13815() -> 'str34':
                return 'should still be valid'
            test_31.assert_(t_13840, fn_13815)
        finally:
            test_31.soft_fail_to_hard()
class TestCase54(TestCase53):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__2010(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_32: Test = Test()
        try:
            params_931: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'), pair_14329('email', 'alice@example.com')))
            t_13801: 'TableDef' = user_table_637()
            t_13802: 'SafeIdentifier' = csid_636('name')
            cs_932: 'Changeset' = changeset(t_13801, params_931).cast((t_13802,)).cast((csid_636('email'),))
            t_13809: 'bool42' = not mapped_has_14293(cs_932.changes, 'name')
            def fn_13797() -> 'str34':
                return 'name must be excluded by second cast'
            test_32.assert_(t_13809, fn_13797)
            t_13812: 'bool42' = mapped_has_14293(cs_932.changes, 'email')
            def fn_13796() -> 'str34':
                return 'email should be present'
            test_32.assert_(t_13812, fn_13796)
        finally:
            test_32.soft_fail_to_hard()
class TestCase55(TestCase53):
    def test___castIgnoresEmptyStringValues__2011(self) -> None:
        'cast ignores empty string values'
        test_33: Test = Test()
        try:
            params_934: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', ''), pair_14329('email', 'bob@example.com')))
            t_13783: 'TableDef' = user_table_637()
            t_13784: 'SafeIdentifier' = csid_636('name')
            t_13785: 'SafeIdentifier' = csid_636('email')
            cs_935: 'Changeset' = changeset(t_13783, params_934).cast((t_13784, t_13785))
            t_13790: 'bool42' = not mapped_has_14293(cs_935.changes, 'name')
            def fn_13779() -> 'str34':
                return 'empty name should not be in changes'
            test_33.assert_(t_13790, fn_13779)
            t_13793: 'bool42' = mapped_has_14293(cs_935.changes, 'email')
            def fn_13778() -> 'str34':
                return 'email should be in changes'
            test_33.assert_(t_13793, fn_13778)
        finally:
            test_33.soft_fail_to_hard()
class TestCase56(TestCase53):
    def test___validateRequiredPassesWhenFieldPresent__2012(self) -> None:
        'validateRequired passes when field present'
        test_34: Test = Test()
        try:
            params_937: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13765: 'TableDef' = user_table_637()
            t_13766: 'SafeIdentifier' = csid_636('name')
            cs_938: 'Changeset' = changeset(t_13765, params_937).cast((t_13766,)).validate_required((csid_636('name'),))
            t_13770: 'bool42' = cs_938.is_valid
            def fn_13762() -> 'str34':
                return 'should be valid'
            test_34.assert_(t_13770, fn_13762)
            t_13776: 'bool42' = len_14296(cs_938.errors) == 0
            def fn_13761() -> 'str34':
                return 'no errors expected'
            test_34.assert_(t_13776, fn_13761)
        finally:
            test_34.soft_fail_to_hard()
class TestCase57(TestCase53):
    def test___validateRequiredFailsWhenFieldMissing__2013(self) -> None:
        'validateRequired fails when field missing'
        test_35: Test = Test()
        try:
            params_940: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
            t_13741: 'TableDef' = user_table_637()
            t_13742: 'SafeIdentifier' = csid_636('name')
            cs_941: 'Changeset' = changeset(t_13741, params_940).cast((t_13742,)).validate_required((csid_636('name'),))
            t_13748: 'bool42' = not cs_941.is_valid
            def fn_13739() -> 'str34':
                return 'should be invalid'
            test_35.assert_(t_13748, fn_13739)
            t_13753: 'bool42' = len_14296(cs_941.errors) == 1
            def fn_13738() -> 'str34':
                return 'should have one error'
            test_35.assert_(t_13753, fn_13738)
            t_13759: 'bool42' = list_get_14304(cs_941.errors, 0).field == 'name'
            def fn_13737() -> 'str34':
                return 'error should name the field'
            test_35.assert_(t_13759, fn_13737)
        finally:
            test_35.soft_fail_to_hard()
class TestCase58(TestCase53):
    def test___validateLengthPassesWithinRange__2014(self) -> None:
        'validateLength passes within range'
        test_36: Test = Test()
        try:
            params_943: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13729: 'TableDef' = user_table_637()
            t_13730: 'SafeIdentifier' = csid_636('name')
            cs_944: 'Changeset' = changeset(t_13729, params_943).cast((t_13730,)).validate_length(csid_636('name'), 2, 50)
            t_13734: 'bool42' = cs_944.is_valid
            def fn_13726() -> 'str34':
                return 'should be valid'
            test_36.assert_(t_13734, fn_13726)
        finally:
            test_36.soft_fail_to_hard()
class TestCase59(TestCase53):
    def test___validateLengthFailsWhenTooShort__2015(self) -> None:
        'validateLength fails when too short'
        test_37: Test = Test()
        try:
            params_946: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'A'),))
            t_13717: 'TableDef' = user_table_637()
            t_13718: 'SafeIdentifier' = csid_636('name')
            cs_947: 'Changeset' = changeset(t_13717, params_946).cast((t_13718,)).validate_length(csid_636('name'), 2, 50)
            t_13724: 'bool42' = not cs_947.is_valid
            def fn_13714() -> 'str34':
                return 'should be invalid'
            test_37.assert_(t_13724, fn_13714)
        finally:
            test_37.soft_fail_to_hard()
class TestCase60(TestCase53):
    def test___validateLengthFailsWhenTooLong__2016(self) -> None:
        'validateLength fails when too long'
        test_38: Test = Test()
        try:
            params_949: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_13705: 'TableDef' = user_table_637()
            t_13706: 'SafeIdentifier' = csid_636('name')
            cs_950: 'Changeset' = changeset(t_13705, params_949).cast((t_13706,)).validate_length(csid_636('name'), 2, 10)
            t_13712: 'bool42' = not cs_950.is_valid
            def fn_13702() -> 'str34':
                return 'should be invalid'
            test_38.assert_(t_13712, fn_13702)
        finally:
            test_38.soft_fail_to_hard()
class TestCase61(TestCase53):
    def test___validateIntPassesForValidInteger__2017(self) -> None:
        'validateInt passes for valid integer'
        test_39: Test = Test()
        try:
            params_952: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', '30'),))
            t_13694: 'TableDef' = user_table_637()
            t_13695: 'SafeIdentifier' = csid_636('age')
            cs_953: 'Changeset' = changeset(t_13694, params_952).cast((t_13695,)).validate_int(csid_636('age'))
            t_13699: 'bool42' = cs_953.is_valid
            def fn_13691() -> 'str34':
                return 'should be valid'
            test_39.assert_(t_13699, fn_13691)
        finally:
            test_39.soft_fail_to_hard()
class TestCase62(TestCase53):
    def test___validateIntFailsForNonInteger__2018(self) -> None:
        'validateInt fails for non-integer'
        test_40: Test = Test()
        try:
            params_955: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', 'not-a-number'),))
            t_13682: 'TableDef' = user_table_637()
            t_13683: 'SafeIdentifier' = csid_636('age')
            cs_956: 'Changeset' = changeset(t_13682, params_955).cast((t_13683,)).validate_int(csid_636('age'))
            t_13689: 'bool42' = not cs_956.is_valid
            def fn_13679() -> 'str34':
                return 'should be invalid'
            test_40.assert_(t_13689, fn_13679)
        finally:
            test_40.soft_fail_to_hard()
class TestCase63(TestCase53):
    def test___validateFloatPassesForValidFloat__2019(self) -> None:
        'validateFloat passes for valid float'
        test_41: Test = Test()
        try:
            params_958: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('score', '9.5'),))
            t_13671: 'TableDef' = user_table_637()
            t_13672: 'SafeIdentifier' = csid_636('score')
            cs_959: 'Changeset' = changeset(t_13671, params_958).cast((t_13672,)).validate_float(csid_636('score'))
            t_13676: 'bool42' = cs_959.is_valid
            def fn_13668() -> 'str34':
                return 'should be valid'
            test_41.assert_(t_13676, fn_13668)
        finally:
            test_41.soft_fail_to_hard()
class TestCase64(TestCase53):
    def test___validateInt64_passesForValid64_bitInteger__2020(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_42: Test = Test()
        try:
            params_961: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', '9999999999'),))
            t_13660: 'TableDef' = user_table_637()
            t_13661: 'SafeIdentifier' = csid_636('age')
            cs_962: 'Changeset' = changeset(t_13660, params_961).cast((t_13661,)).validate_int64(csid_636('age'))
            t_13665: 'bool42' = cs_962.is_valid
            def fn_13657() -> 'str34':
                return 'should be valid'
            test_42.assert_(t_13665, fn_13657)
        finally:
            test_42.soft_fail_to_hard()
class TestCase65(TestCase53):
    def test___validateInt64_failsForNonInteger__2021(self) -> None:
        'validateInt64 fails for non-integer'
        test_43: Test = Test()
        try:
            params_964: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', 'not-a-number'),))
            t_13648: 'TableDef' = user_table_637()
            t_13649: 'SafeIdentifier' = csid_636('age')
            cs_965: 'Changeset' = changeset(t_13648, params_964).cast((t_13649,)).validate_int64(csid_636('age'))
            t_13655: 'bool42' = not cs_965.is_valid
            def fn_13645() -> 'str34':
                return 'should be invalid'
            test_43.assert_(t_13655, fn_13645)
        finally:
            test_43.soft_fail_to_hard()
class TestCase66(TestCase53):
    def test___validateBoolAcceptsTrue1_yesOn__2022(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_44: Test = Test()
        try:
            def fn_13642(v_967: 'str34') -> 'None':
                params_968: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('active', v_967),))
                t_13634: 'TableDef' = user_table_637()
                t_13635: 'SafeIdentifier' = csid_636('active')
                cs_969: 'Changeset' = changeset(t_13634, params_968).cast((t_13635,)).validate_bool(csid_636('active'))
                t_13639: 'bool42' = cs_969.is_valid
                def fn_13631() -> 'str34':
                    return str_cat_14298('should accept: ', v_967)
                test_44.assert_(t_13639, fn_13631)
            list_for_each_14290(('true', '1', 'yes', 'on'), fn_13642)
        finally:
            test_44.soft_fail_to_hard()
class TestCase67(TestCase53):
    def test___validateBoolAcceptsFalse0_noOff__2023(self) -> None:
        'validateBool accepts false/0/no/off'
        test_45: Test = Test()
        try:
            def fn_13628(v_971: 'str34') -> 'None':
                params_972: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('active', v_971),))
                t_13620: 'TableDef' = user_table_637()
                t_13621: 'SafeIdentifier' = csid_636('active')
                cs_973: 'Changeset' = changeset(t_13620, params_972).cast((t_13621,)).validate_bool(csid_636('active'))
                t_13625: 'bool42' = cs_973.is_valid
                def fn_13617() -> 'str34':
                    return str_cat_14298('should accept: ', v_971)
                test_45.assert_(t_13625, fn_13617)
            list_for_each_14290(('false', '0', 'no', 'off'), fn_13628)
        finally:
            test_45.soft_fail_to_hard()
class TestCase68(TestCase53):
    def test___validateBoolRejectsAmbiguousValues__2024(self) -> None:
        'validateBool rejects ambiguous values'
        test_46: Test = Test()
        try:
            def fn_13614(v_975: 'str34') -> 'None':
                params_976: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('active', v_975),))
                t_13605: 'TableDef' = user_table_637()
                t_13606: 'SafeIdentifier' = csid_636('active')
                cs_977: 'Changeset' = changeset(t_13605, params_976).cast((t_13606,)).validate_bool(csid_636('active'))
                t_13612: 'bool42' = not cs_977.is_valid
                def fn_13602() -> 'str34':
                    return str_cat_14298('should reject ambiguous: ', v_975)
                test_46.assert_(t_13612, fn_13602)
            list_for_each_14290(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_13614)
        finally:
            test_46.soft_fail_to_hard()
class TestCase69(TestCase53):
    def test___toInsertSqlEscapesBobbyTables__2025(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_47: Test = Test()
        try:
            params_979: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', "Robert'); DROP TABLE users;--"), pair_14329('email', 'bobby@evil.com')))
            t_13590: 'TableDef' = user_table_637()
            t_13591: 'SafeIdentifier' = csid_636('name')
            t_13592: 'SafeIdentifier' = csid_636('email')
            cs_980: 'Changeset' = changeset(t_13590, params_979).cast((t_13591, t_13592)).validate_required((csid_636('name'), csid_636('email')))
            t_7482: 'SqlFragment'
            t_7482 = cs_980.to_insert_sql()
            sql_frag_981: 'SqlFragment' = t_7482
            s_982: 'str34' = sql_frag_981.to_string()
            t_13599: 'bool42' = s_982.find("''") >= 0
            def fn_13586() -> 'str34':
                return str_cat_14298('single quote must be doubled: ', s_982)
            test_47.assert_(t_13599, fn_13586)
        finally:
            test_47.soft_fail_to_hard()
class TestCase70(TestCase53):
    def test___toInsertSqlProducesCorrectSqlForStringField__2026(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_48: Test = Test()
        try:
            params_984: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'), pair_14329('email', 'a@example.com')))
            t_13570: 'TableDef' = user_table_637()
            t_13571: 'SafeIdentifier' = csid_636('name')
            t_13572: 'SafeIdentifier' = csid_636('email')
            cs_985: 'Changeset' = changeset(t_13570, params_984).cast((t_13571, t_13572)).validate_required((csid_636('name'), csid_636('email')))
            t_7461: 'SqlFragment'
            t_7461 = cs_985.to_insert_sql()
            sql_frag_986: 'SqlFragment' = t_7461
            s_987: 'str34' = sql_frag_986.to_string()
            t_13579: 'bool42' = s_987.find('INSERT INTO users') >= 0
            def fn_13566() -> 'str34':
                return str_cat_14298('has INSERT INTO: ', s_987)
            test_48.assert_(t_13579, fn_13566)
            t_13583: 'bool42' = s_987.find("'Alice'") >= 0
            def fn_13565() -> 'str34':
                return str_cat_14298('has quoted name: ', s_987)
            test_48.assert_(t_13583, fn_13565)
        finally:
            test_48.soft_fail_to_hard()
class TestCase71(TestCase53):
    def test___toInsertSqlProducesCorrectSqlForIntField__2027(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_49: Test = Test()
        try:
            params_989: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Bob'), pair_14329('email', 'b@example.com'), pair_14329('age', '25')))
            t_13552: 'TableDef' = user_table_637()
            t_13553: 'SafeIdentifier' = csid_636('name')
            t_13554: 'SafeIdentifier' = csid_636('email')
            t_13555: 'SafeIdentifier' = csid_636('age')
            cs_990: 'Changeset' = changeset(t_13552, params_989).cast((t_13553, t_13554, t_13555)).validate_required((csid_636('name'), csid_636('email')))
            t_7444: 'SqlFragment'
            t_7444 = cs_990.to_insert_sql()
            sql_frag_991: 'SqlFragment' = t_7444
            s_992: 'str34' = sql_frag_991.to_string()
            t_13562: 'bool42' = s_992.find('25') >= 0
            def fn_13547() -> 'str34':
                return str_cat_14298('age rendered unquoted: ', s_992)
            test_49.assert_(t_13562, fn_13547)
        finally:
            test_49.soft_fail_to_hard()
class TestCase72(TestCase53):
    def test___toInsertSqlBubblesOnInvalidChangeset__2028(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_50: Test = Test()
        try:
            params_994: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
            t_13540: 'TableDef' = user_table_637()
            t_13541: 'SafeIdentifier' = csid_636('name')
            cs_995: 'Changeset' = changeset(t_13540, params_994).cast((t_13541,)).validate_required((csid_636('name'),))
            did_bubble_996: 'bool42'
            try:
                cs_995.to_insert_sql()
                did_bubble_996 = False
            except Exception46:
                did_bubble_996 = True
            def fn_13538() -> 'str34':
                return 'invalid changeset should bubble'
            test_50.assert_(did_bubble_996, fn_13538)
        finally:
            test_50.soft_fail_to_hard()
class TestCase73(TestCase53):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__2029(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_51: Test = Test()
        try:
            strict_table_998: 'TableDef' = TableDef(csid_636('posts'), (FieldDef(csid_636('title'), StringField(), False), FieldDef(csid_636('body'), StringField(), True)))
            params_999: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('body', 'hello'),))
            t_13531: 'SafeIdentifier' = csid_636('body')
            cs_1000: 'Changeset' = changeset(strict_table_998, params_999).cast((t_13531,))
            t_13533: 'bool42' = cs_1000.is_valid
            def fn_13520() -> 'str34':
                return 'changeset should appear valid (no explicit validation run)'
            test_51.assert_(t_13533, fn_13520)
            did_bubble_1001: 'bool42'
            try:
                cs_1000.to_insert_sql()
                did_bubble_1001 = False
            except Exception46:
                did_bubble_1001 = True
            def fn_13519() -> 'str34':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_51.assert_(did_bubble_1001, fn_13519)
        finally:
            test_51.soft_fail_to_hard()
class TestCase74(TestCase53):
    def test___toUpdateSqlProducesCorrectSql__2030(self) -> None:
        'toUpdateSql produces correct SQL'
        test_52: Test = Test()
        try:
            params_1003: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Bob'),))
            t_13510: 'TableDef' = user_table_637()
            t_13511: 'SafeIdentifier' = csid_636('name')
            cs_1004: 'Changeset' = changeset(t_13510, params_1003).cast((t_13511,)).validate_required((csid_636('name'),))
            t_7404: 'SqlFragment'
            t_7404 = cs_1004.to_update_sql(42)
            sql_frag_1005: 'SqlFragment' = t_7404
            s_1006: 'str34' = sql_frag_1005.to_string()
            t_13517: 'bool42' = s_1006 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_13507() -> 'str34':
                return str_cat_14298('got: ', s_1006)
            test_52.assert_(t_13517, fn_13507)
        finally:
            test_52.soft_fail_to_hard()
class TestCase75(TestCase53):
    def test___toUpdateSqlBubblesOnInvalidChangeset__2031(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_53: Test = Test()
        try:
            params_1008: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
            t_13500: 'TableDef' = user_table_637()
            t_13501: 'SafeIdentifier' = csid_636('name')
            cs_1009: 'Changeset' = changeset(t_13500, params_1008).cast((t_13501,)).validate_required((csid_636('name'),))
            did_bubble_1010: 'bool42'
            try:
                cs_1009.to_update_sql(1)
                did_bubble_1010 = False
            except Exception46:
                did_bubble_1010 = True
            def fn_13498() -> 'str34':
                return 'invalid changeset should bubble'
            test_53.assert_(did_bubble_1010, fn_13498)
        finally:
            test_53.soft_fail_to_hard()
class TestCase76(TestCase53):
    def test___putChangeAddsANewField__2032(self) -> None:
        'putChange adds a new field'
        test_54: Test = Test()
        try:
            params_1012: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13484: 'TableDef' = user_table_637()
            t_13485: 'SafeIdentifier' = csid_636('name')
            cs_1013: 'Changeset' = changeset(t_13484, params_1012).cast((t_13485,)).put_change(csid_636('email'), 'alice@example.com')
            t_13490: 'bool42' = mapped_has_14293(cs_1013.changes, 'email')
            def fn_13481() -> 'str34':
                return 'email should be in changes'
            test_54.assert_(t_13490, fn_13481)
            t_13496: 'bool42' = cs_1013.changes.get('email', '') == 'alice@example.com'
            def fn_13480() -> 'str34':
                return 'email value'
            test_54.assert_(t_13496, fn_13480)
        finally:
            test_54.soft_fail_to_hard()
class TestCase77(TestCase53):
    def test___putChangeOverwritesExistingField__2033(self) -> None:
        'putChange overwrites existing field'
        test_55: Test = Test()
        try:
            params_1015: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13470: 'TableDef' = user_table_637()
            t_13471: 'SafeIdentifier' = csid_636('name')
            cs_1016: 'Changeset' = changeset(t_13470, params_1015).cast((t_13471,)).put_change(csid_636('name'), 'Bob')
            t_13478: 'bool42' = cs_1016.changes.get('name', '') == 'Bob'
            def fn_13467() -> 'str34':
                return 'name should be overwritten'
            test_55.assert_(t_13478, fn_13467)
        finally:
            test_55.soft_fail_to_hard()
class TestCase78(TestCase53):
    def test___putChangeValueAppearsInToInsertSql__2034(self) -> None:
        'putChange value appears in toInsertSql'
        test_56: Test = Test()
        try:
            params_1018: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'), pair_14329('email', 'a@example.com')))
            t_13456: 'TableDef' = user_table_637()
            t_13457: 'SafeIdentifier' = csid_636('name')
            t_13458: 'SafeIdentifier' = csid_636('email')
            cs_1019: 'Changeset' = changeset(t_13456, params_1018).cast((t_13457, t_13458)).put_change(csid_636('name'), 'Bob')
            t_7359: 'SqlFragment'
            t_7359 = cs_1019.to_insert_sql()
            t_7360: 'SqlFragment' = t_7359
            s_1020: 'str34' = t_7360.to_string()
            t_13464: 'bool42' = s_1020.find("'Bob'") >= 0
            def fn_13452() -> 'str34':
                return str_cat_14298('should use putChange value: ', s_1020)
            test_56.assert_(t_13464, fn_13452)
        finally:
            test_56.soft_fail_to_hard()
class TestCase79(TestCase53):
    def test___getChangeReturnsValueForExistingField__2035(self) -> None:
        'getChange returns value for existing field'
        test_57: Test = Test()
        try:
            params_1022: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13445: 'TableDef' = user_table_637()
            t_13446: 'SafeIdentifier' = csid_636('name')
            cs_1023: 'Changeset' = changeset(t_13445, params_1022).cast((t_13446,))
            t_7347: 'str34'
            t_7347 = cs_1023.get_change(csid_636('name'))
            val_1024: 'str34' = t_7347
            t_13450: 'bool42' = val_1024 == 'Alice'
            def fn_13442() -> 'str34':
                return 'should return Alice'
            test_57.assert_(t_13450, fn_13442)
        finally:
            test_57.soft_fail_to_hard()
class TestCase80(TestCase53):
    def test___getChangeBubblesOnMissingField__2036(self) -> None:
        'getChange bubbles on missing field'
        test_58: Test = Test()
        try:
            params_1026: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13436: 'TableDef' = user_table_637()
            t_13437: 'SafeIdentifier' = csid_636('name')
            cs_1027: 'Changeset' = changeset(t_13436, params_1026).cast((t_13437,))
            did_bubble_1028: 'bool42'
            try:
                cs_1027.get_change(csid_636('email'))
                did_bubble_1028 = False
            except Exception46:
                did_bubble_1028 = True
            def fn_13433() -> 'str34':
                return 'should bubble for missing field'
            test_58.assert_(did_bubble_1028, fn_13433)
        finally:
            test_58.soft_fail_to_hard()
class TestCase81(TestCase53):
    def test___deleteChangeRemovesField__2037(self) -> None:
        'deleteChange removes field'
        test_59: Test = Test()
        try:
            params_1030: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'), pair_14329('email', 'a@example.com')))
            t_13418: 'TableDef' = user_table_637()
            t_13419: 'SafeIdentifier' = csid_636('name')
            t_13420: 'SafeIdentifier' = csid_636('email')
            cs_1031: 'Changeset' = changeset(t_13418, params_1030).cast((t_13419, t_13420)).delete_change(csid_636('email'))
            t_13427: 'bool42' = not mapped_has_14293(cs_1031.changes, 'email')
            def fn_13414() -> 'str34':
                return 'email should be removed'
            test_59.assert_(t_13427, fn_13414)
            t_13430: 'bool42' = mapped_has_14293(cs_1031.changes, 'name')
            def fn_13413() -> 'str34':
                return 'name should remain'
            test_59.assert_(t_13430, fn_13413)
        finally:
            test_59.soft_fail_to_hard()
class TestCase82(TestCase53):
    def test___deleteChangeOnNonexistentFieldIsNoOp__2038(self) -> None:
        'deleteChange on nonexistent field is no-op'
        test_60: Test = Test()
        try:
            params_1033: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13401: 'TableDef' = user_table_637()
            t_13402: 'SafeIdentifier' = csid_636('name')
            cs_1034: 'Changeset' = changeset(t_13401, params_1033).cast((t_13402,)).delete_change(csid_636('email'))
            t_13407: 'bool42' = mapped_has_14293(cs_1034.changes, 'name')
            def fn_13398() -> 'str34':
                return 'name should still be present'
            test_60.assert_(t_13407, fn_13398)
            t_13410: 'bool42' = cs_1034.is_valid
            def fn_13397() -> 'str34':
                return 'should still be valid'
            test_60.assert_(t_13410, fn_13397)
        finally:
            test_60.soft_fail_to_hard()
class TestCase83(TestCase53):
    def test___validateInclusionPassesWhenValueInList__2039(self) -> None:
        'validateInclusion passes when value in list'
        test_61: Test = Test()
        try:
            params_1036: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'admin'),))
            t_13389: 'TableDef' = user_table_637()
            t_13390: 'SafeIdentifier' = csid_636('name')
            cs_1037: 'Changeset' = changeset(t_13389, params_1036).cast((t_13390,)).validate_inclusion(csid_636('name'), ('admin', 'user', 'guest'))
            t_13394: 'bool42' = cs_1037.is_valid
            def fn_13386() -> 'str34':
                return 'should be valid'
            test_61.assert_(t_13394, fn_13386)
        finally:
            test_61.soft_fail_to_hard()
class TestCase84(TestCase53):
    def test___validateInclusionFailsWhenValueNotInList__2040(self) -> None:
        'validateInclusion fails when value not in list'
        test_62: Test = Test()
        try:
            params_1039: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'hacker'),))
            t_13371: 'TableDef' = user_table_637()
            t_13372: 'SafeIdentifier' = csid_636('name')
            cs_1040: 'Changeset' = changeset(t_13371, params_1039).cast((t_13372,)).validate_inclusion(csid_636('name'), ('admin', 'user', 'guest'))
            t_13378: 'bool42' = not cs_1040.is_valid
            def fn_13368() -> 'str34':
                return 'should be invalid'
            test_62.assert_(t_13378, fn_13368)
            t_13384: 'bool42' = list_get_14304(cs_1040.errors, 0).field == 'name'
            def fn_13367() -> 'str34':
                return 'error on name'
            test_62.assert_(t_13384, fn_13367)
        finally:
            test_62.soft_fail_to_hard()
class TestCase85(TestCase53):
    def test___validateInclusionSkipsWhenFieldNotInChanges__2041(self) -> None:
        'validateInclusion skips when field not in changes'
        test_63: Test = Test()
        try:
            params_1042: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
            t_13359: 'TableDef' = user_table_637()
            t_13360: 'SafeIdentifier' = csid_636('name')
            cs_1043: 'Changeset' = changeset(t_13359, params_1042).cast((t_13360,)).validate_inclusion(csid_636('name'), ('admin', 'user'))
            t_13364: 'bool42' = cs_1043.is_valid
            def fn_13357() -> 'str34':
                return 'should be valid when field absent'
            test_63.assert_(t_13364, fn_13357)
        finally:
            test_63.soft_fail_to_hard()
class TestCase86(TestCase53):
    def test___validateExclusionPassesWhenValueNotInList__2042(self) -> None:
        'validateExclusion passes when value not in list'
        test_64: Test = Test()
        try:
            params_1045: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Alice'),))
            t_13349: 'TableDef' = user_table_637()
            t_13350: 'SafeIdentifier' = csid_636('name')
            cs_1046: 'Changeset' = changeset(t_13349, params_1045).cast((t_13350,)).validate_exclusion(csid_636('name'), ('root', 'admin', 'superuser'))
            t_13354: 'bool42' = cs_1046.is_valid
            def fn_13346() -> 'str34':
                return 'should be valid'
            test_64.assert_(t_13354, fn_13346)
        finally:
            test_64.soft_fail_to_hard()
class TestCase87(TestCase53):
    def test___validateExclusionFailsWhenValueInList__2043(self) -> None:
        'validateExclusion fails when value in list'
        test_65: Test = Test()
        try:
            params_1048: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'admin'),))
            t_13331: 'TableDef' = user_table_637()
            t_13332: 'SafeIdentifier' = csid_636('name')
            cs_1049: 'Changeset' = changeset(t_13331, params_1048).cast((t_13332,)).validate_exclusion(csid_636('name'), ('root', 'admin', 'superuser'))
            t_13338: 'bool42' = not cs_1049.is_valid
            def fn_13328() -> 'str34':
                return 'should be invalid'
            test_65.assert_(t_13338, fn_13328)
            t_13344: 'bool42' = list_get_14304(cs_1049.errors, 0).field == 'name'
            def fn_13327() -> 'str34':
                return 'error on name'
            test_65.assert_(t_13344, fn_13327)
        finally:
            test_65.soft_fail_to_hard()
class TestCase88(TestCase53):
    def test___validateExclusionSkipsWhenFieldNotInChanges__2044(self) -> None:
        'validateExclusion skips when field not in changes'
        test_66: Test = Test()
        try:
            params_1051: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
            t_13319: 'TableDef' = user_table_637()
            t_13320: 'SafeIdentifier' = csid_636('name')
            cs_1052: 'Changeset' = changeset(t_13319, params_1051).cast((t_13320,)).validate_exclusion(csid_636('name'), ('root', 'admin'))
            t_13324: 'bool42' = cs_1052.is_valid
            def fn_13317() -> 'str34':
                return 'should be valid when field absent'
            test_66.assert_(t_13324, fn_13317)
        finally:
            test_66.soft_fail_to_hard()
class TestCase89(TestCase53):
    def test___validateNumberGreaterThanPasses__2045(self) -> None:
        'validateNumber greaterThan passes'
        test_67: Test = Test()
        try:
            params_1054: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', '25'),))
            t_13308: 'TableDef' = user_table_637()
            t_13309: 'SafeIdentifier' = csid_636('age')
            cs_1055: 'Changeset' = changeset(t_13308, params_1054).cast((t_13309,)).validate_number(csid_636('age'), NumberValidationOpts(18.0, None, None, None, None))
            t_13314: 'bool42' = cs_1055.is_valid
            def fn_13305() -> 'str34':
                return '25 > 18 should pass'
            test_67.assert_(t_13314, fn_13305)
        finally:
            test_67.soft_fail_to_hard()
class TestCase90(TestCase53):
    def test___validateNumberGreaterThanFails__2046(self) -> None:
        'validateNumber greaterThan fails'
        test_68: Test = Test()
        try:
            params_1057: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', '15'),))
            t_13295: 'TableDef' = user_table_637()
            t_13296: 'SafeIdentifier' = csid_636('age')
            cs_1058: 'Changeset' = changeset(t_13295, params_1057).cast((t_13296,)).validate_number(csid_636('age'), NumberValidationOpts(18.0, None, None, None, None))
            t_13303: 'bool42' = not cs_1058.is_valid
            def fn_13292() -> 'str34':
                return '15 > 18 should fail'
            test_68.assert_(t_13303, fn_13292)
        finally:
            test_68.soft_fail_to_hard()
class TestCase91(TestCase53):
    def test___validateNumberLessThanPasses__2047(self) -> None:
        'validateNumber lessThan passes'
        test_69: Test = Test()
        try:
            params_1060: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('score', '8.5'),))
            t_13283: 'TableDef' = user_table_637()
            t_13284: 'SafeIdentifier' = csid_636('score')
            cs_1061: 'Changeset' = changeset(t_13283, params_1060).cast((t_13284,)).validate_number(csid_636('score'), NumberValidationOpts(None, 10.0, None, None, None))
            t_13289: 'bool42' = cs_1061.is_valid
            def fn_13280() -> 'str34':
                return '8.5 < 10 should pass'
            test_69.assert_(t_13289, fn_13280)
        finally:
            test_69.soft_fail_to_hard()
class TestCase92(TestCase53):
    def test___validateNumberLessThanFails__2048(self) -> None:
        'validateNumber lessThan fails'
        test_70: Test = Test()
        try:
            params_1063: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('score', '12.0'),))
            t_13270: 'TableDef' = user_table_637()
            t_13271: 'SafeIdentifier' = csid_636('score')
            cs_1064: 'Changeset' = changeset(t_13270, params_1063).cast((t_13271,)).validate_number(csid_636('score'), NumberValidationOpts(None, 10.0, None, None, None))
            t_13278: 'bool42' = not cs_1064.is_valid
            def fn_13267() -> 'str34':
                return '12 < 10 should fail'
            test_70.assert_(t_13278, fn_13267)
        finally:
            test_70.soft_fail_to_hard()
class TestCase93(TestCase53):
    def test___validateNumberGreaterThanOrEqualBoundary__2049(self) -> None:
        'validateNumber greaterThanOrEqual boundary'
        test_71: Test = Test()
        try:
            params_1066: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', '18'),))
            t_13258: 'TableDef' = user_table_637()
            t_13259: 'SafeIdentifier' = csid_636('age')
            cs_1067: 'Changeset' = changeset(t_13258, params_1066).cast((t_13259,)).validate_number(csid_636('age'), NumberValidationOpts(None, None, 18.0, None, None))
            t_13264: 'bool42' = cs_1067.is_valid
            def fn_13255() -> 'str34':
                return '18 >= 18 should pass'
            test_71.assert_(t_13264, fn_13255)
        finally:
            test_71.soft_fail_to_hard()
class TestCase94(TestCase53):
    def test___validateNumberCombinedOptions__2050(self) -> None:
        'validateNumber combined options'
        test_72: Test = Test()
        try:
            params_1069: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('score', '5.0'),))
            t_13246: 'TableDef' = user_table_637()
            t_13247: 'SafeIdentifier' = csid_636('score')
            cs_1070: 'Changeset' = changeset(t_13246, params_1069).cast((t_13247,)).validate_number(csid_636('score'), NumberValidationOpts(0.0, 10.0, None, None, None))
            t_13252: 'bool42' = cs_1070.is_valid
            def fn_13243() -> 'str34':
                return '5 > 0 and < 10 should pass'
            test_72.assert_(t_13252, fn_13243)
        finally:
            test_72.soft_fail_to_hard()
class TestCase95(TestCase53):
    def test___validateNumberNonNumericValue__2051(self) -> None:
        'validateNumber non-numeric value'
        test_73: Test = Test()
        try:
            params_1072: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('age', 'abc'),))
            t_13227: 'TableDef' = user_table_637()
            t_13228: 'SafeIdentifier' = csid_636('age')
            cs_1073: 'Changeset' = changeset(t_13227, params_1072).cast((t_13228,)).validate_number(csid_636('age'), NumberValidationOpts(0.0, None, None, None, None))
            t_13235: 'bool42' = not cs_1073.is_valid
            def fn_13224() -> 'str34':
                return 'non-numeric should fail'
            test_73.assert_(t_13235, fn_13224)
            t_13241: 'bool42' = list_get_14304(cs_1073.errors, 0).message == 'must be a number'
            def fn_13223() -> 'str34':
                return 'correct error message'
            test_73.assert_(t_13241, fn_13223)
        finally:
            test_73.soft_fail_to_hard()
class TestCase96(TestCase53):
    def test___validateNumberSkipsWhenFieldNotInChanges__2052(self) -> None:
        'validateNumber skips when field not in changes'
        test_74: Test = Test()
        try:
            params_1075: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
            t_13214: 'TableDef' = user_table_637()
            t_13215: 'SafeIdentifier' = csid_636('age')
            cs_1076: 'Changeset' = changeset(t_13214, params_1075).cast((t_13215,)).validate_number(csid_636('age'), NumberValidationOpts(0.0, None, None, None, None))
            t_13220: 'bool42' = cs_1076.is_valid
            def fn_13212() -> 'str34':
                return 'should be valid when field absent'
            test_74.assert_(t_13220, fn_13212)
        finally:
            test_74.soft_fail_to_hard()
class TestCase97(TestCase53):
    def test___validateAcceptancePassesForTrueValues__2053(self) -> None:
        'validateAcceptance passes for true values'
        test_75: Test = Test()
        try:
            def fn_13209(v_1078: 'str34') -> 'None':
                params_1079: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('active', v_1078),))
                t_13201: 'TableDef' = user_table_637()
                t_13202: 'SafeIdentifier' = csid_636('active')
                cs_1080: 'Changeset' = changeset(t_13201, params_1079).cast((t_13202,)).validate_acceptance(csid_636('active'))
                t_13206: 'bool42' = cs_1080.is_valid
                def fn_13198() -> 'str34':
                    return str_cat_14298('should accept: ', v_1078)
                test_75.assert_(t_13206, fn_13198)
            list_for_each_14290(('true', '1', 'yes', 'on'), fn_13209)
        finally:
            test_75.soft_fail_to_hard()
class TestCase98(TestCase53):
    def test___validateAcceptanceFailsForNonTrueValues__2054(self) -> None:
        'validateAcceptance fails for non-true values'
        test_76: Test = Test()
        try:
            params_1082: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('active', 'false'),))
            t_13183: 'TableDef' = user_table_637()
            t_13184: 'SafeIdentifier' = csid_636('active')
            cs_1083: 'Changeset' = changeset(t_13183, params_1082).cast((t_13184,)).validate_acceptance(csid_636('active'))
            t_13190: 'bool42' = not cs_1083.is_valid
            def fn_13180() -> 'str34':
                return 'false should not be accepted'
            test_76.assert_(t_13190, fn_13180)
            t_13196: 'bool42' = list_get_14304(cs_1083.errors, 0).message == 'must be accepted'
            def fn_13179() -> 'str34':
                return 'correct message'
            test_76.assert_(t_13196, fn_13179)
        finally:
            test_76.soft_fail_to_hard()
class TestCase99(TestCase53):
    def test___validateConfirmationPassesWhenFieldsMatch__2055(self) -> None:
        'validateConfirmation passes when fields match'
        test_77: Test = Test()
        try:
            tbl_1085: 'TableDef' = TableDef(csid_636('users'), (FieldDef(csid_636('password'), StringField(), False), FieldDef(csid_636('password_confirmation'), StringField(), True)))
            params_1086: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('password', 'secret123'), pair_14329('password_confirmation', 'secret123')))
            t_13170: 'SafeIdentifier' = csid_636('password')
            t_13171: 'SafeIdentifier' = csid_636('password_confirmation')
            cs_1087: 'Changeset' = changeset(tbl_1085, params_1086).cast((t_13170, t_13171)).validate_confirmation(csid_636('password'), csid_636('password_confirmation'))
            t_13176: 'bool42' = cs_1087.is_valid
            def fn_13158() -> 'str34':
                return 'matching fields should pass'
            test_77.assert_(t_13176, fn_13158)
        finally:
            test_77.soft_fail_to_hard()
class TestCase100(TestCase53):
    def test___validateConfirmationFailsWhenFieldsDiffer__2056(self) -> None:
        'validateConfirmation fails when fields differ'
        test_78: Test = Test()
        try:
            tbl_1089: 'TableDef' = TableDef(csid_636('users'), (FieldDef(csid_636('password'), StringField(), False), FieldDef(csid_636('password_confirmation'), StringField(), True)))
            params_1090: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('password', 'secret123'), pair_14329('password_confirmation', 'wrong456')))
            t_13142: 'SafeIdentifier' = csid_636('password')
            t_13143: 'SafeIdentifier' = csid_636('password_confirmation')
            cs_1091: 'Changeset' = changeset(tbl_1089, params_1090).cast((t_13142, t_13143)).validate_confirmation(csid_636('password'), csid_636('password_confirmation'))
            t_13150: 'bool42' = not cs_1091.is_valid
            def fn_13130() -> 'str34':
                return 'mismatched fields should fail'
            test_78.assert_(t_13150, fn_13130)
            t_13156: 'bool42' = list_get_14304(cs_1091.errors, 0).field == 'password_confirmation'
            def fn_13129() -> 'str34':
                return 'error on confirmation field'
            test_78.assert_(t_13156, fn_13129)
        finally:
            test_78.soft_fail_to_hard()
class TestCase101(TestCase53):
    def test___validateConfirmationFailsWhenConfirmationMissing__2057(self) -> None:
        'validateConfirmation fails when confirmation missing'
        test_79: Test = Test()
        try:
            tbl_1093: 'TableDef' = TableDef(csid_636('users'), (FieldDef(csid_636('password'), StringField(), False), FieldDef(csid_636('password_confirmation'), StringField(), True)))
            params_1094: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('password', 'secret123'),))
            t_13120: 'SafeIdentifier' = csid_636('password')
            cs_1095: 'Changeset' = changeset(tbl_1093, params_1094).cast((t_13120,)).validate_confirmation(csid_636('password'), csid_636('password_confirmation'))
            t_13127: 'bool42' = not cs_1095.is_valid
            def fn_13109() -> 'str34':
                return 'missing confirmation should fail'
            test_79.assert_(t_13127, fn_13109)
        finally:
            test_79.soft_fail_to_hard()
class TestCase102(TestCase53):
    def test___validateContainsPassesWhenSubstringFound__2058(self) -> None:
        'validateContains passes when substring found'
        test_80: Test = Test()
        try:
            params_1097: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('email', 'alice@example.com'),))
            t_13101: 'TableDef' = user_table_637()
            t_13102: 'SafeIdentifier' = csid_636('email')
            cs_1098: 'Changeset' = changeset(t_13101, params_1097).cast((t_13102,)).validate_contains(csid_636('email'), '@')
            t_13106: 'bool42' = cs_1098.is_valid
            def fn_13098() -> 'str34':
                return 'should pass when @ present'
            test_80.assert_(t_13106, fn_13098)
        finally:
            test_80.soft_fail_to_hard()
class TestCase103(TestCase53):
    def test___validateContainsFailsWhenSubstringNotFound__2059(self) -> None:
        'validateContains fails when substring not found'
        test_81: Test = Test()
        try:
            params_1100: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('email', 'alice-example.com'),))
            t_13089: 'TableDef' = user_table_637()
            t_13090: 'SafeIdentifier' = csid_636('email')
            cs_1101: 'Changeset' = changeset(t_13089, params_1100).cast((t_13090,)).validate_contains(csid_636('email'), '@')
            t_13096: 'bool42' = not cs_1101.is_valid
            def fn_13086() -> 'str34':
                return 'should fail when @ absent'
            test_81.assert_(t_13096, fn_13086)
        finally:
            test_81.soft_fail_to_hard()
class TestCase104(TestCase53):
    def test___validateContainsSkipsWhenFieldNotInChanges__2060(self) -> None:
        'validateContains skips when field not in changes'
        test_82: Test = Test()
        try:
            params_1103: 'MappingProxyType41[str34, str34]' = map_constructor_14328(())
            t_13078: 'TableDef' = user_table_637()
            t_13079: 'SafeIdentifier' = csid_636('email')
            cs_1104: 'Changeset' = changeset(t_13078, params_1103).cast((t_13079,)).validate_contains(csid_636('email'), '@')
            t_13083: 'bool42' = cs_1104.is_valid
            def fn_13076() -> 'str34':
                return 'should be valid when field absent'
            test_82.assert_(t_13083, fn_13076)
        finally:
            test_82.soft_fail_to_hard()
class TestCase105(TestCase53):
    def test___validateStartsWithPasses__2061(self) -> None:
        'validateStartsWith passes'
        test_83: Test = Test()
        try:
            params_1106: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Dr. Smith'),))
            t_13068: 'TableDef' = user_table_637()
            t_13069: 'SafeIdentifier' = csid_636('name')
            cs_1107: 'Changeset' = changeset(t_13068, params_1106).cast((t_13069,)).validate_starts_with(csid_636('name'), 'Dr.')
            t_13073: 'bool42' = cs_1107.is_valid
            def fn_13065() -> 'str34':
                return 'should pass for Dr. prefix'
            test_83.assert_(t_13073, fn_13065)
        finally:
            test_83.soft_fail_to_hard()
class TestCase106(TestCase53):
    def test___validateStartsWithFails__2062(self) -> None:
        'validateStartsWith fails'
        test_84: Test = Test()
        try:
            params_1109: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'Mr. Smith'),))
            t_13056: 'TableDef' = user_table_637()
            t_13057: 'SafeIdentifier' = csid_636('name')
            cs_1110: 'Changeset' = changeset(t_13056, params_1109).cast((t_13057,)).validate_starts_with(csid_636('name'), 'Dr.')
            t_13063: 'bool42' = not cs_1110.is_valid
            def fn_13053() -> 'str34':
                return 'should fail for Mr. prefix'
            test_84.assert_(t_13063, fn_13053)
        finally:
            test_84.soft_fail_to_hard()
class TestCase107(TestCase53):
    def test___validateEndsWithPasses__2063(self) -> None:
        'validateEndsWith passes'
        test_85: Test = Test()
        try:
            params_1112: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('email', 'alice@example.com'),))
            t_13045: 'TableDef' = user_table_637()
            t_13046: 'SafeIdentifier' = csid_636('email')
            cs_1113: 'Changeset' = changeset(t_13045, params_1112).cast((t_13046,)).validate_ends_with(csid_636('email'), '.com')
            t_13050: 'bool42' = cs_1113.is_valid
            def fn_13042() -> 'str34':
                return 'should pass for .com suffix'
            test_85.assert_(t_13050, fn_13042)
        finally:
            test_85.soft_fail_to_hard()
class TestCase108(TestCase53):
    def test___validateEndsWithFails__2064(self) -> None:
        'validateEndsWith fails'
        test_86: Test = Test()
        try:
            params_1115: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('email', 'alice@example.org'),))
            t_13033: 'TableDef' = user_table_637()
            t_13034: 'SafeIdentifier' = csid_636('email')
            cs_1116: 'Changeset' = changeset(t_13033, params_1115).cast((t_13034,)).validate_ends_with(csid_636('email'), '.com')
            t_13040: 'bool42' = not cs_1116.is_valid
            def fn_13030() -> 'str34':
                return 'should fail for .org when expecting .com'
            test_86.assert_(t_13040, fn_13030)
        finally:
            test_86.soft_fail_to_hard()
class TestCase109(TestCase53):
    def test___validateEndsWithHandlesRepeatedSuffixCorrectly__2065(self) -> None:
        'validateEndsWith handles repeated suffix correctly'
        test_87: Test = Test()
        try:
            params_1118: 'MappingProxyType41[str34, str34]' = map_constructor_14328((pair_14329('name', 'abcabc'),))
            t_13022: 'TableDef' = user_table_637()
            t_13023: 'SafeIdentifier' = csid_636('name')
            cs_1119: 'Changeset' = changeset(t_13022, params_1118).cast((t_13023,)).validate_ends_with(csid_636('name'), 'abc')
            t_13027: 'bool42' = cs_1119.is_valid
            def fn_13019() -> 'str34':
                return 'abcabc should end with abc'
            test_87.assert_(t_13027, fn_13019)
        finally:
            test_87.soft_fail_to_hard()
def sid_638(name_1464: 'str34') -> 'SafeIdentifier':
    t_6485: 'SafeIdentifier'
    t_6485 = safe_identifier(name_1464)
    return t_6485
class TestCase110(TestCase53):
    def test___bareFromProducesSelect__2147(self) -> None:
        'bare from produces SELECT *'
        test_88: Test = Test()
        try:
            q_1467: 'Query' = from_(sid_638('users'))
            t_12504: 'bool42' = q_1467.to_sql().to_string() == 'SELECT * FROM users'
            def fn_12499() -> 'str34':
                return 'bare query'
            test_88.assert_(t_12504, fn_12499)
        finally:
            test_88.soft_fail_to_hard()
class TestCase111(TestCase53):
    def test___selectRestrictsColumns__2148(self) -> None:
        'select restricts columns'
        test_89: Test = Test()
        try:
            t_12490: 'SafeIdentifier' = sid_638('users')
            t_12491: 'SafeIdentifier' = sid_638('id')
            t_12492: 'SafeIdentifier' = sid_638('name')
            q_1469: 'Query' = from_(t_12490).select((t_12491, t_12492))
            t_12497: 'bool42' = q_1469.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_12489() -> 'str34':
                return 'select columns'
            test_89.assert_(t_12497, fn_12489)
        finally:
            test_89.soft_fail_to_hard()
class TestCase112(TestCase53):
    def test___whereAddsConditionWithIntValue__2149(self) -> None:
        'where adds condition with int value'
        test_90: Test = Test()
        try:
            t_12478: 'SafeIdentifier' = sid_638('users')
            t_12479: 'SqlBuilder' = SqlBuilder()
            t_12479.append_safe('age > ')
            t_12479.append_int32(18)
            t_12482: 'SqlFragment' = t_12479.accumulated
            q_1471: 'Query' = from_(t_12478).where(t_12482)
            t_12487: 'bool42' = q_1471.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_12477() -> 'str34':
                return 'where int'
            test_90.assert_(t_12487, fn_12477)
        finally:
            test_90.soft_fail_to_hard()
class TestCase113(TestCase53):
    def test___whereAddsConditionWithBoolValue__2151(self) -> None:
        'where adds condition with bool value'
        test_91: Test = Test()
        try:
            t_12466: 'SafeIdentifier' = sid_638('users')
            t_12467: 'SqlBuilder' = SqlBuilder()
            t_12467.append_safe('active = ')
            t_12467.append_boolean(True)
            t_12470: 'SqlFragment' = t_12467.accumulated
            q_1473: 'Query' = from_(t_12466).where(t_12470)
            t_12475: 'bool42' = q_1473.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_12465() -> 'str34':
                return 'where bool'
            test_91.assert_(t_12475, fn_12465)
        finally:
            test_91.soft_fail_to_hard()
class TestCase114(TestCase53):
    def test___chainedWhereUsesAnd__2153(self) -> None:
        'chained where uses AND'
        test_92: Test = Test()
        try:
            t_12449: 'SafeIdentifier' = sid_638('users')
            t_12450: 'SqlBuilder' = SqlBuilder()
            t_12450.append_safe('age > ')
            t_12450.append_int32(18)
            t_12453: 'SqlFragment' = t_12450.accumulated
            t_12454: 'Query' = from_(t_12449).where(t_12453)
            t_12455: 'SqlBuilder' = SqlBuilder()
            t_12455.append_safe('active = ')
            t_12455.append_boolean(True)
            q_1475: 'Query' = t_12454.where(t_12455.accumulated)
            t_12463: 'bool42' = q_1475.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_12448() -> 'str34':
                return 'chained where'
            test_92.assert_(t_12463, fn_12448)
        finally:
            test_92.soft_fail_to_hard()
class TestCase115(TestCase53):
    def test___orderByAsc__2156(self) -> None:
        'orderBy ASC'
        test_93: Test = Test()
        try:
            t_12440: 'SafeIdentifier' = sid_638('users')
            t_12441: 'SafeIdentifier' = sid_638('name')
            q_1477: 'Query' = from_(t_12440).order_by(t_12441, True)
            t_12446: 'bool42' = q_1477.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_12439() -> 'str34':
                return 'order asc'
            test_93.assert_(t_12446, fn_12439)
        finally:
            test_93.soft_fail_to_hard()
class TestCase116(TestCase53):
    def test___orderByDesc__2157(self) -> None:
        'orderBy DESC'
        test_94: Test = Test()
        try:
            t_12431: 'SafeIdentifier' = sid_638('users')
            t_12432: 'SafeIdentifier' = sid_638('created_at')
            q_1479: 'Query' = from_(t_12431).order_by(t_12432, False)
            t_12437: 'bool42' = q_1479.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_12430() -> 'str34':
                return 'order desc'
            test_94.assert_(t_12437, fn_12430)
        finally:
            test_94.soft_fail_to_hard()
class TestCase117(TestCase53):
    def test___limitAndOffset__2158(self) -> None:
        'limit and offset'
        test_95: Test = Test()
        try:
            t_6419: 'Query'
            t_6419 = from_(sid_638('users')).limit(10)
            t_6420: 'Query'
            t_6420 = t_6419.offset(20)
            q_1481: 'Query' = t_6420
            t_12428: 'bool42' = q_1481.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_12423() -> 'str34':
                return 'limit/offset'
            test_95.assert_(t_12428, fn_12423)
        finally:
            test_95.soft_fail_to_hard()
class TestCase118(TestCase53):
    def test___limitBubblesOnNegative__2159(self) -> None:
        'limit bubbles on negative'
        test_96: Test = Test()
        try:
            did_bubble_1483: 'bool42'
            try:
                from_(sid_638('users')).limit(-1)
                did_bubble_1483 = False
            except Exception46:
                did_bubble_1483 = True
            def fn_12419() -> 'str34':
                return 'negative limit should bubble'
            test_96.assert_(did_bubble_1483, fn_12419)
        finally:
            test_96.soft_fail_to_hard()
class TestCase119(TestCase53):
    def test___offsetBubblesOnNegative__2160(self) -> None:
        'offset bubbles on negative'
        test_97: Test = Test()
        try:
            did_bubble_1485: 'bool42'
            try:
                from_(sid_638('users')).offset(-1)
                did_bubble_1485 = False
            except Exception46:
                did_bubble_1485 = True
            def fn_12415() -> 'str34':
                return 'negative offset should bubble'
            test_97.assert_(did_bubble_1485, fn_12415)
        finally:
            test_97.soft_fail_to_hard()
class TestCase120(TestCase53):
    def test___complexComposedQuery__2161(self) -> None:
        'complex composed query'
        test_98: Test = Test()
        try:
            min_age_1487: 'int40' = 21
            t_12393: 'SafeIdentifier' = sid_638('users')
            t_12394: 'SafeIdentifier' = sid_638('id')
            t_12395: 'SafeIdentifier' = sid_638('name')
            t_12396: 'SafeIdentifier' = sid_638('email')
            t_12397: 'Query' = from_(t_12393).select((t_12394, t_12395, t_12396))
            t_12398: 'SqlBuilder' = SqlBuilder()
            t_12398.append_safe('age >= ')
            t_12398.append_int32(21)
            t_12402: 'Query' = t_12397.where(t_12398.accumulated)
            t_12403: 'SqlBuilder' = SqlBuilder()
            t_12403.append_safe('active = ')
            t_12403.append_boolean(True)
            t_6405: 'Query'
            t_6405 = t_12402.where(t_12403.accumulated).order_by(sid_638('name'), True).limit(25)
            t_6406: 'Query'
            t_6406 = t_6405.offset(0)
            q_1488: 'Query' = t_6406
            t_12413: 'bool42' = q_1488.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_12392() -> 'str34':
                return 'complex query'
            test_98.assert_(t_12413, fn_12392)
        finally:
            test_98.soft_fail_to_hard()
class TestCase121(TestCase53):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__2164(self) -> None:
        'safeToSql applies default limit when none set'
        test_99: Test = Test()
        try:
            q_1490: 'Query' = from_(sid_638('users'))
            t_6382: 'SqlFragment'
            t_6382 = q_1490.safe_to_sql(100)
            t_6383: 'SqlFragment' = t_6382
            s_1491: 'str34' = t_6383.to_string()
            t_12390: 'bool42' = s_1491 == 'SELECT * FROM users LIMIT 100'
            def fn_12386() -> 'str34':
                return str_cat_14298('should have limit: ', s_1491)
            test_99.assert_(t_12390, fn_12386)
        finally:
            test_99.soft_fail_to_hard()
class TestCase122(TestCase53):
    def test___safeToSqlRespectsExplicitLimit__2165(self) -> None:
        'safeToSql respects explicit limit'
        test_100: Test = Test()
        try:
            t_6374: 'Query'
            t_6374 = from_(sid_638('users')).limit(5)
            q_1493: 'Query' = t_6374
            t_6377: 'SqlFragment'
            t_6377 = q_1493.safe_to_sql(100)
            t_6378: 'SqlFragment' = t_6377
            s_1494: 'str34' = t_6378.to_string()
            t_12384: 'bool42' = s_1494 == 'SELECT * FROM users LIMIT 5'
            def fn_12380() -> 'str34':
                return str_cat_14298('explicit limit preserved: ', s_1494)
            test_100.assert_(t_12384, fn_12380)
        finally:
            test_100.soft_fail_to_hard()
class TestCase123(TestCase53):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__2166(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_101: Test = Test()
        try:
            did_bubble_1496: 'bool42'
            try:
                from_(sid_638('users')).safe_to_sql(-1)
                did_bubble_1496 = False
            except Exception46:
                did_bubble_1496 = True
            def fn_12376() -> 'str34':
                return 'negative defaultLimit should bubble'
            test_101.assert_(did_bubble_1496, fn_12376)
        finally:
            test_101.soft_fail_to_hard()
class TestCase124(TestCase53):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__2167(self) -> None:
        'where with injection attempt in string value is escaped'
        test_102: Test = Test()
        try:
            evil_1498: 'str34' = "'; DROP TABLE users; --"
            t_12360: 'SafeIdentifier' = sid_638('users')
            t_12361: 'SqlBuilder' = SqlBuilder()
            t_12361.append_safe('name = ')
            t_12361.append_string("'; DROP TABLE users; --")
            t_12364: 'SqlFragment' = t_12361.accumulated
            q_1499: 'Query' = from_(t_12360).where(t_12364)
            s_1500: 'str34' = q_1499.to_sql().to_string()
            t_12369: 'bool42' = s_1500.find("''") >= 0
            def fn_12359() -> 'str34':
                return str_cat_14298('quotes must be doubled: ', s_1500)
            test_102.assert_(t_12369, fn_12359)
            t_12373: 'bool42' = s_1500.find('SELECT * FROM users WHERE name =') >= 0
            def fn_12358() -> 'str34':
                return str_cat_14298('structure intact: ', s_1500)
            test_102.assert_(t_12373, fn_12358)
        finally:
            test_102.soft_fail_to_hard()
class TestCase125(TestCase53):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__2169(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_103: Test = Test()
        try:
            attack_1502: 'str34' = 'users; DROP TABLE users; --'
            did_bubble_1503: 'bool42'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_1503 = False
            except Exception46:
                did_bubble_1503 = True
            def fn_12355() -> 'str34':
                return 'metacharacter-containing name must be rejected at construction'
            test_103.assert_(did_bubble_1503, fn_12355)
        finally:
            test_103.soft_fail_to_hard()
class TestCase126(TestCase53):
    def test___innerJoinProducesInnerJoin__2170(self) -> None:
        'innerJoin produces INNER JOIN'
        test_104: Test = Test()
        try:
            t_12344: 'SafeIdentifier' = sid_638('users')
            t_12345: 'SafeIdentifier' = sid_638('orders')
            t_12346: 'SqlBuilder' = SqlBuilder()
            t_12346.append_safe('users.id = orders.user_id')
            t_12348: 'SqlFragment' = t_12346.accumulated
            q_1505: 'Query' = from_(t_12344).inner_join(t_12345, t_12348)
            t_12353: 'bool42' = q_1505.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_12343() -> 'str34':
                return 'inner join'
            test_104.assert_(t_12353, fn_12343)
        finally:
            test_104.soft_fail_to_hard()
class TestCase127(TestCase53):
    def test___leftJoinProducesLeftJoin__2172(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_105: Test = Test()
        try:
            t_12332: 'SafeIdentifier' = sid_638('users')
            t_12333: 'SafeIdentifier' = sid_638('profiles')
            t_12334: 'SqlBuilder' = SqlBuilder()
            t_12334.append_safe('users.id = profiles.user_id')
            t_12336: 'SqlFragment' = t_12334.accumulated
            q_1507: 'Query' = from_(t_12332).left_join(t_12333, t_12336)
            t_12341: 'bool42' = q_1507.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_12331() -> 'str34':
                return 'left join'
            test_105.assert_(t_12341, fn_12331)
        finally:
            test_105.soft_fail_to_hard()
class TestCase128(TestCase53):
    def test___rightJoinProducesRightJoin__2174(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_106: Test = Test()
        try:
            t_12320: 'SafeIdentifier' = sid_638('orders')
            t_12321: 'SafeIdentifier' = sid_638('users')
            t_12322: 'SqlBuilder' = SqlBuilder()
            t_12322.append_safe('orders.user_id = users.id')
            t_12324: 'SqlFragment' = t_12322.accumulated
            q_1509: 'Query' = from_(t_12320).right_join(t_12321, t_12324)
            t_12329: 'bool42' = q_1509.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_12319() -> 'str34':
                return 'right join'
            test_106.assert_(t_12329, fn_12319)
        finally:
            test_106.soft_fail_to_hard()
class TestCase129(TestCase53):
    def test___fullJoinProducesFullOuterJoin__2176(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_107: Test = Test()
        try:
            t_12308: 'SafeIdentifier' = sid_638('users')
            t_12309: 'SafeIdentifier' = sid_638('orders')
            t_12310: 'SqlBuilder' = SqlBuilder()
            t_12310.append_safe('users.id = orders.user_id')
            t_12312: 'SqlFragment' = t_12310.accumulated
            q_1511: 'Query' = from_(t_12308).full_join(t_12309, t_12312)
            t_12317: 'bool42' = q_1511.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_12307() -> 'str34':
                return 'full join'
            test_107.assert_(t_12317, fn_12307)
        finally:
            test_107.soft_fail_to_hard()
class TestCase130(TestCase53):
    def test___chainedJoins__2178(self) -> None:
        'chained joins'
        test_108: Test = Test()
        try:
            t_12291: 'SafeIdentifier' = sid_638('users')
            t_12292: 'SafeIdentifier' = sid_638('orders')
            t_12293: 'SqlBuilder' = SqlBuilder()
            t_12293.append_safe('users.id = orders.user_id')
            t_12295: 'SqlFragment' = t_12293.accumulated
            t_12296: 'Query' = from_(t_12291).inner_join(t_12292, t_12295)
            t_12297: 'SafeIdentifier' = sid_638('profiles')
            t_12298: 'SqlBuilder' = SqlBuilder()
            t_12298.append_safe('users.id = profiles.user_id')
            q_1513: 'Query' = t_12296.left_join(t_12297, t_12298.accumulated)
            t_12305: 'bool42' = q_1513.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_12290() -> 'str34':
                return 'chained joins'
            test_108.assert_(t_12305, fn_12290)
        finally:
            test_108.soft_fail_to_hard()
class TestCase131(TestCase53):
    def test___joinWithWhereAndOrderBy__2181(self) -> None:
        'join with where and orderBy'
        test_109: Test = Test()
        try:
            t_12272: 'SafeIdentifier' = sid_638('users')
            t_12273: 'SafeIdentifier' = sid_638('orders')
            t_12274: 'SqlBuilder' = SqlBuilder()
            t_12274.append_safe('users.id = orders.user_id')
            t_12276: 'SqlFragment' = t_12274.accumulated
            t_12277: 'Query' = from_(t_12272).inner_join(t_12273, t_12276)
            t_12278: 'SqlBuilder' = SqlBuilder()
            t_12278.append_safe('orders.total > ')
            t_12278.append_int32(100)
            t_6289: 'Query'
            t_6289 = t_12277.where(t_12278.accumulated).order_by(sid_638('name'), True).limit(10)
            q_1515: 'Query' = t_6289
            t_12288: 'bool42' = q_1515.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_12271() -> 'str34':
                return 'join with where/order/limit'
            test_109.assert_(t_12288, fn_12271)
        finally:
            test_109.soft_fail_to_hard()
class TestCase132(TestCase53):
    def test___colHelperProducesQualifiedReference__2184(self) -> None:
        'col helper produces qualified reference'
        test_110: Test = Test()
        try:
            c_1517: 'SqlFragment' = col(sid_638('users'), sid_638('id'))
            t_12269: 'bool42' = c_1517.to_string() == 'users.id'
            def fn_12263() -> 'str34':
                return 'col helper'
            test_110.assert_(t_12269, fn_12263)
        finally:
            test_110.soft_fail_to_hard()
class TestCase133(TestCase53):
    def test___joinWithColHelper__2185(self) -> None:
        'join with col helper'
        test_111: Test = Test()
        try:
            on_cond_1519: 'SqlFragment' = col(sid_638('users'), sid_638('id'))
            b_1520: 'SqlBuilder' = SqlBuilder()
            b_1520.append_fragment(on_cond_1519)
            b_1520.append_safe(' = ')
            b_1520.append_fragment(col(sid_638('orders'), sid_638('user_id')))
            t_12254: 'SafeIdentifier' = sid_638('users')
            t_12255: 'SafeIdentifier' = sid_638('orders')
            t_12256: 'SqlFragment' = b_1520.accumulated
            q_1521: 'Query' = from_(t_12254).inner_join(t_12255, t_12256)
            t_12261: 'bool42' = q_1521.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_12243() -> 'str34':
                return 'join with col'
            test_111.assert_(t_12261, fn_12243)
        finally:
            test_111.soft_fail_to_hard()
class TestCase134(TestCase53):
    def test___orWhereBasic__2186(self) -> None:
        'orWhere basic'
        test_112: Test = Test()
        try:
            t_12232: 'SafeIdentifier' = sid_638('users')
            t_12233: 'SqlBuilder' = SqlBuilder()
            t_12233.append_safe('status = ')
            t_12233.append_string('active')
            t_12236: 'SqlFragment' = t_12233.accumulated
            q_1523: 'Query' = from_(t_12232).or_where(t_12236)
            t_12241: 'bool42' = q_1523.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_12231() -> 'str34':
                return 'orWhere basic'
            test_112.assert_(t_12241, fn_12231)
        finally:
            test_112.soft_fail_to_hard()
class TestCase135(TestCase53):
    def test___whereThenOrWhere__2188(self) -> None:
        'where then orWhere'
        test_113: Test = Test()
        try:
            t_12215: 'SafeIdentifier' = sid_638('users')
            t_12216: 'SqlBuilder' = SqlBuilder()
            t_12216.append_safe('age > ')
            t_12216.append_int32(18)
            t_12219: 'SqlFragment' = t_12216.accumulated
            t_12220: 'Query' = from_(t_12215).where(t_12219)
            t_12221: 'SqlBuilder' = SqlBuilder()
            t_12221.append_safe('vip = ')
            t_12221.append_boolean(True)
            q_1525: 'Query' = t_12220.or_where(t_12221.accumulated)
            t_12229: 'bool42' = q_1525.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_12214() -> 'str34':
                return 'where then orWhere'
            test_113.assert_(t_12229, fn_12214)
        finally:
            test_113.soft_fail_to_hard()
class TestCase136(TestCase53):
    def test___multipleOrWhere__2191(self) -> None:
        'multiple orWhere'
        test_114: Test = Test()
        try:
            t_12193: 'SafeIdentifier' = sid_638('users')
            t_12194: 'SqlBuilder' = SqlBuilder()
            t_12194.append_safe('active = ')
            t_12194.append_boolean(True)
            t_12197: 'SqlFragment' = t_12194.accumulated
            t_12198: 'Query' = from_(t_12193).where(t_12197)
            t_12199: 'SqlBuilder' = SqlBuilder()
            t_12199.append_safe('role = ')
            t_12199.append_string('admin')
            t_12203: 'Query' = t_12198.or_where(t_12199.accumulated)
            t_12204: 'SqlBuilder' = SqlBuilder()
            t_12204.append_safe('role = ')
            t_12204.append_string('moderator')
            q_1527: 'Query' = t_12203.or_where(t_12204.accumulated)
            t_12212: 'bool42' = q_1527.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_12192() -> 'str34':
                return 'multiple orWhere'
            test_114.assert_(t_12212, fn_12192)
        finally:
            test_114.soft_fail_to_hard()
class TestCase137(TestCase53):
    def test___mixedWhereAndOrWhere__2195(self) -> None:
        'mixed where and orWhere'
        test_115: Test = Test()
        try:
            t_12171: 'SafeIdentifier' = sid_638('users')
            t_12172: 'SqlBuilder' = SqlBuilder()
            t_12172.append_safe('age > ')
            t_12172.append_int32(18)
            t_12175: 'SqlFragment' = t_12172.accumulated
            t_12176: 'Query' = from_(t_12171).where(t_12175)
            t_12177: 'SqlBuilder' = SqlBuilder()
            t_12177.append_safe('active = ')
            t_12177.append_boolean(True)
            t_12181: 'Query' = t_12176.where(t_12177.accumulated)
            t_12182: 'SqlBuilder' = SqlBuilder()
            t_12182.append_safe('vip = ')
            t_12182.append_boolean(True)
            q_1529: 'Query' = t_12181.or_where(t_12182.accumulated)
            t_12190: 'bool42' = q_1529.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_12170() -> 'str34':
                return 'mixed where and orWhere'
            test_115.assert_(t_12190, fn_12170)
        finally:
            test_115.soft_fail_to_hard()
class TestCase138(TestCase53):
    def test___whereNull__2199(self) -> None:
        'whereNull'
        test_116: Test = Test()
        try:
            t_12162: 'SafeIdentifier' = sid_638('users')
            t_12163: 'SafeIdentifier' = sid_638('deleted_at')
            q_1531: 'Query' = from_(t_12162).where_null(t_12163)
            t_12168: 'bool42' = q_1531.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_12161() -> 'str34':
                return 'whereNull'
            test_116.assert_(t_12168, fn_12161)
        finally:
            test_116.soft_fail_to_hard()
class TestCase139(TestCase53):
    def test___whereNotNull__2200(self) -> None:
        'whereNotNull'
        test_117: Test = Test()
        try:
            t_12153: 'SafeIdentifier' = sid_638('users')
            t_12154: 'SafeIdentifier' = sid_638('email')
            q_1533: 'Query' = from_(t_12153).where_not_null(t_12154)
            t_12159: 'bool42' = q_1533.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_12152() -> 'str34':
                return 'whereNotNull'
            test_117.assert_(t_12159, fn_12152)
        finally:
            test_117.soft_fail_to_hard()
class TestCase140(TestCase53):
    def test___whereNullChainedWithWhere__2201(self) -> None:
        'whereNull chained with where'
        test_118: Test = Test()
        try:
            t_12139: 'SafeIdentifier' = sid_638('users')
            t_12140: 'SqlBuilder' = SqlBuilder()
            t_12140.append_safe('active = ')
            t_12140.append_boolean(True)
            t_12143: 'SqlFragment' = t_12140.accumulated
            q_1535: 'Query' = from_(t_12139).where(t_12143).where_null(sid_638('deleted_at'))
            t_12150: 'bool42' = q_1535.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_12138() -> 'str34':
                return 'whereNull chained'
            test_118.assert_(t_12150, fn_12138)
        finally:
            test_118.soft_fail_to_hard()
class TestCase141(TestCase53):
    def test___whereNotNullChainedWithOrWhere__2203(self) -> None:
        'whereNotNull chained with orWhere'
        test_119: Test = Test()
        try:
            t_12125: 'SafeIdentifier' = sid_638('users')
            t_12126: 'SafeIdentifier' = sid_638('deleted_at')
            t_12127: 'Query' = from_(t_12125).where_null(t_12126)
            t_12128: 'SqlBuilder' = SqlBuilder()
            t_12128.append_safe('role = ')
            t_12128.append_string('admin')
            q_1537: 'Query' = t_12127.or_where(t_12128.accumulated)
            t_12136: 'bool42' = q_1537.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_12124() -> 'str34':
                return 'whereNotNull with orWhere'
            test_119.assert_(t_12136, fn_12124)
        finally:
            test_119.soft_fail_to_hard()
class TestCase142(TestCase53):
    def test___whereInWithIntValues__2205(self) -> None:
        'whereIn with int values'
        test_120: Test = Test()
        try:
            t_12113: 'SafeIdentifier' = sid_638('users')
            t_12114: 'SafeIdentifier' = sid_638('id')
            t_12115: 'SqlInt32' = SqlInt32(1)
            t_12116: 'SqlInt32' = SqlInt32(2)
            t_12117: 'SqlInt32' = SqlInt32(3)
            q_1539: 'Query' = from_(t_12113).where_in(t_12114, (t_12115, t_12116, t_12117))
            t_12122: 'bool42' = q_1539.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_12112() -> 'str34':
                return 'whereIn ints'
            test_120.assert_(t_12122, fn_12112)
        finally:
            test_120.soft_fail_to_hard()
class TestCase143(TestCase53):
    def test___whereInWithStringValuesEscaping__2206(self) -> None:
        'whereIn with string values escaping'
        test_121: Test = Test()
        try:
            t_12102: 'SafeIdentifier' = sid_638('users')
            t_12103: 'SafeIdentifier' = sid_638('name')
            t_12104: 'SqlString' = SqlString('Alice')
            t_12105: 'SqlString' = SqlString("Bob's")
            q_1541: 'Query' = from_(t_12102).where_in(t_12103, (t_12104, t_12105))
            t_12110: 'bool42' = q_1541.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_12101() -> 'str34':
                return 'whereIn strings'
            test_121.assert_(t_12110, fn_12101)
        finally:
            test_121.soft_fail_to_hard()
class TestCase144(TestCase53):
    def test___whereInWithEmptyListProduces1_0__2207(self) -> None:
        'whereIn with empty list produces 1=0'
        test_122: Test = Test()
        try:
            t_12093: 'SafeIdentifier' = sid_638('users')
            t_12094: 'SafeIdentifier' = sid_638('id')
            q_1543: 'Query' = from_(t_12093).where_in(t_12094, ())
            t_12099: 'bool42' = q_1543.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_12092() -> 'str34':
                return 'whereIn empty'
            test_122.assert_(t_12099, fn_12092)
        finally:
            test_122.soft_fail_to_hard()
class TestCase145(TestCase53):
    def test___whereInChained__2208(self) -> None:
        'whereIn chained'
        test_123: Test = Test()
        try:
            t_12077: 'SafeIdentifier' = sid_638('users')
            t_12078: 'SqlBuilder' = SqlBuilder()
            t_12078.append_safe('active = ')
            t_12078.append_boolean(True)
            t_12081: 'SqlFragment' = t_12078.accumulated
            q_1545: 'Query' = from_(t_12077).where(t_12081).where_in(sid_638('role'), (SqlString('admin'), SqlString('user')))
            t_12090: 'bool42' = q_1545.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_12076() -> 'str34':
                return 'whereIn chained'
            test_123.assert_(t_12090, fn_12076)
        finally:
            test_123.soft_fail_to_hard()
class TestCase146(TestCase53):
    def test___whereInSingleElement__2210(self) -> None:
        'whereIn single element'
        test_124: Test = Test()
        try:
            t_12067: 'SafeIdentifier' = sid_638('users')
            t_12068: 'SafeIdentifier' = sid_638('id')
            t_12069: 'SqlInt32' = SqlInt32(42)
            q_1547: 'Query' = from_(t_12067).where_in(t_12068, (t_12069,))
            t_12074: 'bool42' = q_1547.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_12066() -> 'str34':
                return 'whereIn single'
            test_124.assert_(t_12074, fn_12066)
        finally:
            test_124.soft_fail_to_hard()
class TestCase147(TestCase53):
    def test___whereNotBasic__2211(self) -> None:
        'whereNot basic'
        test_125: Test = Test()
        try:
            t_12055: 'SafeIdentifier' = sid_638('users')
            t_12056: 'SqlBuilder' = SqlBuilder()
            t_12056.append_safe('active = ')
            t_12056.append_boolean(True)
            t_12059: 'SqlFragment' = t_12056.accumulated
            q_1549: 'Query' = from_(t_12055).where_not(t_12059)
            t_12064: 'bool42' = q_1549.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_12054() -> 'str34':
                return 'whereNot'
            test_125.assert_(t_12064, fn_12054)
        finally:
            test_125.soft_fail_to_hard()
class TestCase148(TestCase53):
    def test___whereNotChained__2213(self) -> None:
        'whereNot chained'
        test_126: Test = Test()
        try:
            t_12038: 'SafeIdentifier' = sid_638('users')
            t_12039: 'SqlBuilder' = SqlBuilder()
            t_12039.append_safe('age > ')
            t_12039.append_int32(18)
            t_12042: 'SqlFragment' = t_12039.accumulated
            t_12043: 'Query' = from_(t_12038).where(t_12042)
            t_12044: 'SqlBuilder' = SqlBuilder()
            t_12044.append_safe('banned = ')
            t_12044.append_boolean(True)
            q_1551: 'Query' = t_12043.where_not(t_12044.accumulated)
            t_12052: 'bool42' = q_1551.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_12037() -> 'str34':
                return 'whereNot chained'
            test_126.assert_(t_12052, fn_12037)
        finally:
            test_126.soft_fail_to_hard()
class TestCase149(TestCase53):
    def test___whereBetweenIntegers__2216(self) -> None:
        'whereBetween integers'
        test_127: Test = Test()
        try:
            t_12027: 'SafeIdentifier' = sid_638('users')
            t_12028: 'SafeIdentifier' = sid_638('age')
            t_12029: 'SqlInt32' = SqlInt32(18)
            t_12030: 'SqlInt32' = SqlInt32(65)
            q_1553: 'Query' = from_(t_12027).where_between(t_12028, t_12029, t_12030)
            t_12035: 'bool42' = q_1553.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_12026() -> 'str34':
                return 'whereBetween ints'
            test_127.assert_(t_12035, fn_12026)
        finally:
            test_127.soft_fail_to_hard()
class TestCase150(TestCase53):
    def test___whereBetweenChained__2217(self) -> None:
        'whereBetween chained'
        test_128: Test = Test()
        try:
            t_12011: 'SafeIdentifier' = sid_638('users')
            t_12012: 'SqlBuilder' = SqlBuilder()
            t_12012.append_safe('active = ')
            t_12012.append_boolean(True)
            t_12015: 'SqlFragment' = t_12012.accumulated
            q_1555: 'Query' = from_(t_12011).where(t_12015).where_between(sid_638('age'), SqlInt32(21), SqlInt32(30))
            t_12024: 'bool42' = q_1555.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_12010() -> 'str34':
                return 'whereBetween chained'
            test_128.assert_(t_12024, fn_12010)
        finally:
            test_128.soft_fail_to_hard()
class TestCase151(TestCase53):
    def test___whereLikeBasic__2219(self) -> None:
        'whereLike basic'
        test_129: Test = Test()
        try:
            t_12002: 'SafeIdentifier' = sid_638('users')
            t_12003: 'SafeIdentifier' = sid_638('name')
            q_1557: 'Query' = from_(t_12002).where_like(t_12003, 'John%')
            t_12008: 'bool42' = q_1557.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_12001() -> 'str34':
                return 'whereLike'
            test_129.assert_(t_12008, fn_12001)
        finally:
            test_129.soft_fail_to_hard()
class TestCase152(TestCase53):
    def test___whereIlikeBasic__2220(self) -> None:
        'whereILike basic'
        test_130: Test = Test()
        try:
            t_11993: 'SafeIdentifier' = sid_638('users')
            t_11994: 'SafeIdentifier' = sid_638('email')
            q_1559: 'Query' = from_(t_11993).where_i_like(t_11994, '%@gmail.com')
            t_11999: 'bool42' = q_1559.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_11992() -> 'str34':
                return 'whereILike'
            test_130.assert_(t_11999, fn_11992)
        finally:
            test_130.soft_fail_to_hard()
class TestCase153(TestCase53):
    def test___whereLikeWithInjectionAttempt__2221(self) -> None:
        'whereLike with injection attempt'
        test_131: Test = Test()
        try:
            t_11979: 'SafeIdentifier' = sid_638('users')
            t_11980: 'SafeIdentifier' = sid_638('name')
            q_1561: 'Query' = from_(t_11979).where_like(t_11980, "'; DROP TABLE users; --")
            s_1562: 'str34' = q_1561.to_sql().to_string()
            t_11985: 'bool42' = s_1562.find("''") >= 0
            def fn_11978() -> 'str34':
                return str_cat_14298('like injection escaped: ', s_1562)
            test_131.assert_(t_11985, fn_11978)
            t_11989: 'bool42' = s_1562.find('LIKE') >= 0
            def fn_11977() -> 'str34':
                return str_cat_14298('like structure intact: ', s_1562)
            test_131.assert_(t_11989, fn_11977)
        finally:
            test_131.soft_fail_to_hard()
class TestCase154(TestCase53):
    def test___whereLikeWildcardPatterns__2222(self) -> None:
        'whereLike wildcard patterns'
        test_132: Test = Test()
        try:
            t_11969: 'SafeIdentifier' = sid_638('users')
            t_11970: 'SafeIdentifier' = sid_638('name')
            q_1564: 'Query' = from_(t_11969).where_like(t_11970, '%son%')
            t_11975: 'bool42' = q_1564.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_11968() -> 'str34':
                return 'whereLike wildcard'
            test_132.assert_(t_11975, fn_11968)
        finally:
            test_132.soft_fail_to_hard()
class TestCase155(TestCase53):
    def test___countAllProducesCount__2223(self) -> None:
        'countAll produces COUNT(*)'
        test_133: Test = Test()
        try:
            f_1566: 'SqlFragment' = count_all()
            t_11966: 'bool42' = f_1566.to_string() == 'COUNT(*)'
            def fn_11962() -> 'str34':
                return 'countAll'
            test_133.assert_(t_11966, fn_11962)
        finally:
            test_133.soft_fail_to_hard()
class TestCase156(TestCase53):
    def test___countColProducesCountField__2224(self) -> None:
        'countCol produces COUNT(field)'
        test_134: Test = Test()
        try:
            f_1568: 'SqlFragment' = count_col(sid_638('id'))
            t_11960: 'bool42' = f_1568.to_string() == 'COUNT(id)'
            def fn_11955() -> 'str34':
                return 'countCol'
            test_134.assert_(t_11960, fn_11955)
        finally:
            test_134.soft_fail_to_hard()
class TestCase157(TestCase53):
    def test___sumColProducesSumField__2225(self) -> None:
        'sumCol produces SUM(field)'
        test_135: Test = Test()
        try:
            f_1570: 'SqlFragment' = sum_col(sid_638('amount'))
            t_11953: 'bool42' = f_1570.to_string() == 'SUM(amount)'
            def fn_11948() -> 'str34':
                return 'sumCol'
            test_135.assert_(t_11953, fn_11948)
        finally:
            test_135.soft_fail_to_hard()
class TestCase158(TestCase53):
    def test___avgColProducesAvgField__2226(self) -> None:
        'avgCol produces AVG(field)'
        test_136: Test = Test()
        try:
            f_1572: 'SqlFragment' = avg_col(sid_638('price'))
            t_11946: 'bool42' = f_1572.to_string() == 'AVG(price)'
            def fn_11941() -> 'str34':
                return 'avgCol'
            test_136.assert_(t_11946, fn_11941)
        finally:
            test_136.soft_fail_to_hard()
class TestCase159(TestCase53):
    def test___minColProducesMinField__2227(self) -> None:
        'minCol produces MIN(field)'
        test_137: Test = Test()
        try:
            f_1574: 'SqlFragment' = min_col(sid_638('created_at'))
            t_11939: 'bool42' = f_1574.to_string() == 'MIN(created_at)'
            def fn_11934() -> 'str34':
                return 'minCol'
            test_137.assert_(t_11939, fn_11934)
        finally:
            test_137.soft_fail_to_hard()
class TestCase160(TestCase53):
    def test___maxColProducesMaxField__2228(self) -> None:
        'maxCol produces MAX(field)'
        test_138: Test = Test()
        try:
            f_1576: 'SqlFragment' = max_col(sid_638('score'))
            t_11932: 'bool42' = f_1576.to_string() == 'MAX(score)'
            def fn_11927() -> 'str34':
                return 'maxCol'
            test_138.assert_(t_11932, fn_11927)
        finally:
            test_138.soft_fail_to_hard()
class TestCase161(TestCase53):
    def test___selectExprWithAggregate__2229(self) -> None:
        'selectExpr with aggregate'
        test_139: Test = Test()
        try:
            t_11919: 'SafeIdentifier' = sid_638('orders')
            t_11920: 'SqlFragment' = count_all()
            q_1578: 'Query' = from_(t_11919).select_expr((t_11920,))
            t_11925: 'bool42' = q_1578.to_sql().to_string() == 'SELECT COUNT(*) FROM orders'
            def fn_11918() -> 'str34':
                return 'selectExpr count'
            test_139.assert_(t_11925, fn_11918)
        finally:
            test_139.soft_fail_to_hard()
class TestCase162(TestCase53):
    def test___selectExprWithMultipleExpressions__2230(self) -> None:
        'selectExpr with multiple expressions'
        test_140: Test = Test()
        try:
            name_frag_1580: 'SqlFragment' = col(sid_638('users'), sid_638('name'))
            t_11910: 'SafeIdentifier' = sid_638('users')
            t_11911: 'SqlFragment' = count_all()
            q_1581: 'Query' = from_(t_11910).select_expr((name_frag_1580, t_11911))
            t_11916: 'bool42' = q_1581.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users'
            def fn_11906() -> 'str34':
                return 'selectExpr multi'
            test_140.assert_(t_11916, fn_11906)
        finally:
            test_140.soft_fail_to_hard()
class TestCase163(TestCase53):
    def test___selectExprOverridesSelectedFields__2231(self) -> None:
        'selectExpr overrides selectedFields'
        test_141: Test = Test()
        try:
            t_11895: 'SafeIdentifier' = sid_638('users')
            t_11896: 'SafeIdentifier' = sid_638('id')
            t_11897: 'SafeIdentifier' = sid_638('name')
            q_1583: 'Query' = from_(t_11895).select((t_11896, t_11897)).select_expr((count_all(),))
            t_11904: 'bool42' = q_1583.to_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_11894() -> 'str34':
                return 'selectExpr overrides select'
            test_141.assert_(t_11904, fn_11894)
        finally:
            test_141.soft_fail_to_hard()
class TestCase164(TestCase53):
    def test___groupBySingleField__2232(self) -> None:
        'groupBy single field'
        test_142: Test = Test()
        try:
            t_11881: 'SafeIdentifier' = sid_638('orders')
            t_11884: 'SqlFragment' = col(sid_638('orders'), sid_638('status'))
            t_11885: 'SqlFragment' = count_all()
            q_1585: 'Query' = from_(t_11881).select_expr((t_11884, t_11885)).group_by(sid_638('status'))
            t_11892: 'bool42' = q_1585.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status'
            def fn_11880() -> 'str34':
                return 'groupBy single'
            test_142.assert_(t_11892, fn_11880)
        finally:
            test_142.soft_fail_to_hard()
class TestCase165(TestCase53):
    def test___groupByMultipleFields__2233(self) -> None:
        'groupBy multiple fields'
        test_143: Test = Test()
        try:
            t_11870: 'SafeIdentifier' = sid_638('orders')
            t_11871: 'SafeIdentifier' = sid_638('status')
            q_1587: 'Query' = from_(t_11870).group_by(t_11871).group_by(sid_638('category'))
            t_11878: 'bool42' = q_1587.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category'
            def fn_11869() -> 'str34':
                return 'groupBy multiple'
            test_143.assert_(t_11878, fn_11869)
        finally:
            test_143.soft_fail_to_hard()
class TestCase166(TestCase53):
    def test___havingBasic__2234(self) -> None:
        'having basic'
        test_144: Test = Test()
        try:
            t_11851: 'SafeIdentifier' = sid_638('orders')
            t_11854: 'SqlFragment' = col(sid_638('orders'), sid_638('status'))
            t_11855: 'SqlFragment' = count_all()
            t_11858: 'Query' = from_(t_11851).select_expr((t_11854, t_11855)).group_by(sid_638('status'))
            t_11859: 'SqlBuilder' = SqlBuilder()
            t_11859.append_safe('COUNT(*) > ')
            t_11859.append_int32(5)
            q_1589: 'Query' = t_11858.having(t_11859.accumulated)
            t_11867: 'bool42' = q_1589.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5'
            def fn_11850() -> 'str34':
                return 'having basic'
            test_144.assert_(t_11867, fn_11850)
        finally:
            test_144.soft_fail_to_hard()
class TestCase167(TestCase53):
    def test___orHaving__2236(self) -> None:
        'orHaving'
        test_145: Test = Test()
        try:
            t_11832: 'SafeIdentifier' = sid_638('orders')
            t_11833: 'SafeIdentifier' = sid_638('status')
            t_11834: 'Query' = from_(t_11832).group_by(t_11833)
            t_11835: 'SqlBuilder' = SqlBuilder()
            t_11835.append_safe('COUNT(*) > ')
            t_11835.append_int32(5)
            t_11839: 'Query' = t_11834.having(t_11835.accumulated)
            t_11840: 'SqlBuilder' = SqlBuilder()
            t_11840.append_safe('SUM(total) > ')
            t_11840.append_int32(1000)
            q_1591: 'Query' = t_11839.or_having(t_11840.accumulated)
            t_11848: 'bool42' = q_1591.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000'
            def fn_11831() -> 'str34':
                return 'orHaving'
            test_145.assert_(t_11848, fn_11831)
        finally:
            test_145.soft_fail_to_hard()
class TestCase168(TestCase53):
    def test___distinctBasic__2239(self) -> None:
        'distinct basic'
        test_146: Test = Test()
        try:
            t_11822: 'SafeIdentifier' = sid_638('users')
            t_11823: 'SafeIdentifier' = sid_638('name')
            q_1593: 'Query' = from_(t_11822).select((t_11823,)).distinct()
            t_11829: 'bool42' = q_1593.to_sql().to_string() == 'SELECT DISTINCT name FROM users'
            def fn_11821() -> 'str34':
                return 'distinct'
            test_146.assert_(t_11829, fn_11821)
        finally:
            test_146.soft_fail_to_hard()
class TestCase169(TestCase53):
    def test___distinctWithWhere__2240(self) -> None:
        'distinct with where'
        test_147: Test = Test()
        try:
            t_11807: 'SafeIdentifier' = sid_638('users')
            t_11808: 'SafeIdentifier' = sid_638('email')
            t_11809: 'Query' = from_(t_11807).select((t_11808,))
            t_11810: 'SqlBuilder' = SqlBuilder()
            t_11810.append_safe('active = ')
            t_11810.append_boolean(True)
            q_1595: 'Query' = t_11809.where(t_11810.accumulated).distinct()
            t_11819: 'bool42' = q_1595.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE'
            def fn_11806() -> 'str34':
                return 'distinct with where'
            test_147.assert_(t_11819, fn_11806)
        finally:
            test_147.soft_fail_to_hard()
class TestCase170(TestCase53):
    def test___countSqlBare__2242(self) -> None:
        'countSql bare'
        test_148: Test = Test()
        try:
            q_1597: 'Query' = from_(sid_638('users'))
            t_11804: 'bool42' = q_1597.count_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_11799() -> 'str34':
                return 'countSql bare'
            test_148.assert_(t_11804, fn_11799)
        finally:
            test_148.soft_fail_to_hard()
class TestCase171(TestCase53):
    def test___countSqlWithWhere__2243(self) -> None:
        'countSql with WHERE'
        test_149: Test = Test()
        try:
            t_11788: 'SafeIdentifier' = sid_638('users')
            t_11789: 'SqlBuilder' = SqlBuilder()
            t_11789.append_safe('active = ')
            t_11789.append_boolean(True)
            t_11792: 'SqlFragment' = t_11789.accumulated
            q_1599: 'Query' = from_(t_11788).where(t_11792)
            t_11797: 'bool42' = q_1599.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_11787() -> 'str34':
                return 'countSql with where'
            test_149.assert_(t_11797, fn_11787)
        finally:
            test_149.soft_fail_to_hard()
class TestCase172(TestCase53):
    def test___countSqlWithJoin__2245(self) -> None:
        'countSql with JOIN'
        test_150: Test = Test()
        try:
            t_11771: 'SafeIdentifier' = sid_638('users')
            t_11772: 'SafeIdentifier' = sid_638('orders')
            t_11773: 'SqlBuilder' = SqlBuilder()
            t_11773.append_safe('users.id = orders.user_id')
            t_11775: 'SqlFragment' = t_11773.accumulated
            t_11776: 'Query' = from_(t_11771).inner_join(t_11772, t_11775)
            t_11777: 'SqlBuilder' = SqlBuilder()
            t_11777.append_safe('orders.total > ')
            t_11777.append_int32(100)
            q_1601: 'Query' = t_11776.where(t_11777.accumulated)
            t_11785: 'bool42' = q_1601.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100'
            def fn_11770() -> 'str34':
                return 'countSql with join'
            test_150.assert_(t_11785, fn_11770)
        finally:
            test_150.soft_fail_to_hard()
class TestCase173(TestCase53):
    def test___countSqlDropsOrderByLimitOffset__2248(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_151: Test = Test()
        try:
            t_11757: 'SafeIdentifier' = sid_638('users')
            t_11758: 'SqlBuilder' = SqlBuilder()
            t_11758.append_safe('active = ')
            t_11758.append_boolean(True)
            t_11761: 'SqlFragment' = t_11758.accumulated
            t_5865: 'Query'
            t_5865 = from_(t_11757).where(t_11761).order_by(sid_638('name'), True).limit(10)
            t_5866: 'Query'
            t_5866 = t_5865.offset(20)
            q_1603: 'Query' = t_5866
            s_1604: 'str34' = q_1603.count_sql().to_string()
            t_11768: 'bool42' = s_1604 == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_11756() -> 'str34':
                return str_cat_14298('countSql drops extras: ', s_1604)
            test_151.assert_(t_11768, fn_11756)
        finally:
            test_151.soft_fail_to_hard()
class TestCase174(TestCase53):
    def test___fullAggregationQuery__2250(self) -> None:
        'full aggregation query'
        test_152: Test = Test()
        try:
            t_11724: 'SafeIdentifier' = sid_638('orders')
            t_11727: 'SqlFragment' = col(sid_638('orders'), sid_638('status'))
            t_11728: 'SqlFragment' = count_all()
            t_11730: 'SqlFragment' = sum_col(sid_638('total'))
            t_11731: 'Query' = from_(t_11724).select_expr((t_11727, t_11728, t_11730))
            t_11732: 'SafeIdentifier' = sid_638('users')
            t_11733: 'SqlBuilder' = SqlBuilder()
            t_11733.append_safe('orders.user_id = users.id')
            t_11736: 'Query' = t_11731.inner_join(t_11732, t_11733.accumulated)
            t_11737: 'SqlBuilder' = SqlBuilder()
            t_11737.append_safe('users.active = ')
            t_11737.append_boolean(True)
            t_11743: 'Query' = t_11736.where(t_11737.accumulated).group_by(sid_638('status'))
            t_11744: 'SqlBuilder' = SqlBuilder()
            t_11744.append_safe('COUNT(*) > ')
            t_11744.append_int32(3)
            q_1606: 'Query' = t_11743.having(t_11744.accumulated).order_by(sid_638('status'), True)
            expected_1607: 'str34' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            t_11754: 'bool42' = q_1606.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_11723() -> 'str34':
                return 'full aggregation'
            test_152.assert_(t_11754, fn_11723)
        finally:
            test_152.soft_fail_to_hard()
class TestCase175(TestCase53):
    def test___unionSql__2254(self) -> None:
        'unionSql'
        test_153: Test = Test()
        try:
            t_11706: 'SafeIdentifier' = sid_638('users')
            t_11707: 'SqlBuilder' = SqlBuilder()
            t_11707.append_safe('role = ')
            t_11707.append_string('admin')
            t_11710: 'SqlFragment' = t_11707.accumulated
            a_1609: 'Query' = from_(t_11706).where(t_11710)
            t_11712: 'SafeIdentifier' = sid_638('users')
            t_11713: 'SqlBuilder' = SqlBuilder()
            t_11713.append_safe('role = ')
            t_11713.append_string('moderator')
            t_11716: 'SqlFragment' = t_11713.accumulated
            b_1610: 'Query' = from_(t_11712).where(t_11716)
            s_1611: 'str34' = union_sql(a_1609, b_1610).to_string()
            t_11721: 'bool42' = s_1611 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')"
            def fn_11705() -> 'str34':
                return str_cat_14298('unionSql: ', s_1611)
            test_153.assert_(t_11721, fn_11705)
        finally:
            test_153.soft_fail_to_hard()
class TestCase176(TestCase53):
    def test___unionAllSql__2257(self) -> None:
        'unionAllSql'
        test_154: Test = Test()
        try:
            t_11694: 'SafeIdentifier' = sid_638('users')
            t_11695: 'SafeIdentifier' = sid_638('name')
            a_1613: 'Query' = from_(t_11694).select((t_11695,))
            t_11697: 'SafeIdentifier' = sid_638('contacts')
            t_11698: 'SafeIdentifier' = sid_638('name')
            b_1614: 'Query' = from_(t_11697).select((t_11698,))
            s_1615: 'str34' = union_all_sql(a_1613, b_1614).to_string()
            t_11703: 'bool42' = s_1615 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)'
            def fn_11693() -> 'str34':
                return str_cat_14298('unionAllSql: ', s_1615)
            test_154.assert_(t_11703, fn_11693)
        finally:
            test_154.soft_fail_to_hard()
class TestCase177(TestCase53):
    def test___intersectSql__2258(self) -> None:
        'intersectSql'
        test_155: Test = Test()
        try:
            t_11682: 'SafeIdentifier' = sid_638('users')
            t_11683: 'SafeIdentifier' = sid_638('email')
            a_1617: 'Query' = from_(t_11682).select((t_11683,))
            t_11685: 'SafeIdentifier' = sid_638('subscribers')
            t_11686: 'SafeIdentifier' = sid_638('email')
            b_1618: 'Query' = from_(t_11685).select((t_11686,))
            s_1619: 'str34' = intersect_sql(a_1617, b_1618).to_string()
            t_11691: 'bool42' = s_1619 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)'
            def fn_11681() -> 'str34':
                return str_cat_14298('intersectSql: ', s_1619)
            test_155.assert_(t_11691, fn_11681)
        finally:
            test_155.soft_fail_to_hard()
class TestCase178(TestCase53):
    def test___exceptSql__2259(self) -> None:
        'exceptSql'
        test_156: Test = Test()
        try:
            t_11670: 'SafeIdentifier' = sid_638('users')
            t_11671: 'SafeIdentifier' = sid_638('id')
            a_1621: 'Query' = from_(t_11670).select((t_11671,))
            t_11673: 'SafeIdentifier' = sid_638('banned')
            t_11674: 'SafeIdentifier' = sid_638('id')
            b_1622: 'Query' = from_(t_11673).select((t_11674,))
            s_1623: 'str34' = except_sql(a_1621, b_1622).to_string()
            t_11679: 'bool42' = s_1623 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)'
            def fn_11669() -> 'str34':
                return str_cat_14298('exceptSql: ', s_1623)
            test_156.assert_(t_11679, fn_11669)
        finally:
            test_156.soft_fail_to_hard()
class TestCase179(TestCase53):
    def test___subqueryWithAlias__2260(self) -> None:
        'subquery with alias'
        test_157: Test = Test()
        try:
            t_11655: 'SafeIdentifier' = sid_638('orders')
            t_11656: 'SafeIdentifier' = sid_638('user_id')
            t_11657: 'Query' = from_(t_11655).select((t_11656,))
            t_11658: 'SqlBuilder' = SqlBuilder()
            t_11658.append_safe('total > ')
            t_11658.append_int32(100)
            inner_1625: 'Query' = t_11657.where(t_11658.accumulated)
            s_1626: 'str34' = subquery(inner_1625, sid_638('big_orders')).to_string()
            t_11667: 'bool42' = s_1626 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders'
            def fn_11654() -> 'str34':
                return str_cat_14298('subquery: ', s_1626)
            test_157.assert_(t_11667, fn_11654)
        finally:
            test_157.soft_fail_to_hard()
class TestCase180(TestCase53):
    def test___existsSql__2262(self) -> None:
        'existsSql'
        test_158: Test = Test()
        try:
            t_11644: 'SafeIdentifier' = sid_638('orders')
            t_11645: 'SqlBuilder' = SqlBuilder()
            t_11645.append_safe('orders.user_id = users.id')
            t_11647: 'SqlFragment' = t_11645.accumulated
            inner_1628: 'Query' = from_(t_11644).where(t_11647)
            s_1629: 'str34' = exists_sql(inner_1628).to_string()
            t_11652: 'bool42' = s_1629 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_11643() -> 'str34':
                return str_cat_14298('existsSql: ', s_1629)
            test_158.assert_(t_11652, fn_11643)
        finally:
            test_158.soft_fail_to_hard()
class TestCase181(TestCase53):
    def test___whereInSubquery__2264(self) -> None:
        'whereInSubquery'
        test_159: Test = Test()
        try:
            t_11627: 'SafeIdentifier' = sid_638('orders')
            t_11628: 'SafeIdentifier' = sid_638('user_id')
            t_11629: 'Query' = from_(t_11627).select((t_11628,))
            t_11630: 'SqlBuilder' = SqlBuilder()
            t_11630.append_safe('total > ')
            t_11630.append_int32(1000)
            sub_1631: 'Query' = t_11629.where(t_11630.accumulated)
            t_11635: 'SafeIdentifier' = sid_638('users')
            t_11636: 'SafeIdentifier' = sid_638('id')
            q_1632: 'Query' = from_(t_11635).where_in_subquery(t_11636, sub_1631)
            s_1633: 'str34' = q_1632.to_sql().to_string()
            t_11641: 'bool42' = s_1633 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)'
            def fn_11626() -> 'str34':
                return str_cat_14298('whereInSubquery: ', s_1633)
            test_159.assert_(t_11641, fn_11626)
        finally:
            test_159.soft_fail_to_hard()
class TestCase182(TestCase53):
    def test___setOperationWithWhereOnEachSide__2266(self) -> None:
        'set operation with WHERE on each side'
        test_160: Test = Test()
        try:
            t_11604: 'SafeIdentifier' = sid_638('users')
            t_11605: 'SqlBuilder' = SqlBuilder()
            t_11605.append_safe('age > ')
            t_11605.append_int32(18)
            t_11608: 'SqlFragment' = t_11605.accumulated
            t_11609: 'Query' = from_(t_11604).where(t_11608)
            t_11610: 'SqlBuilder' = SqlBuilder()
            t_11610.append_safe('active = ')
            t_11610.append_boolean(True)
            a_1635: 'Query' = t_11609.where(t_11610.accumulated)
            t_11615: 'SafeIdentifier' = sid_638('users')
            t_11616: 'SqlBuilder' = SqlBuilder()
            t_11616.append_safe('role = ')
            t_11616.append_string('vip')
            t_11619: 'SqlFragment' = t_11616.accumulated
            b_1636: 'Query' = from_(t_11615).where(t_11619)
            s_1637: 'str34' = union_sql(a_1635, b_1636).to_string()
            t_11624: 'bool42' = s_1637 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')"
            def fn_11603() -> 'str34':
                return str_cat_14298('union with where: ', s_1637)
            test_160.assert_(t_11624, fn_11603)
        finally:
            test_160.soft_fail_to_hard()
class TestCase183(TestCase53):
    def test___whereInSubqueryChainedWithWhere__2270(self) -> None:
        'whereInSubquery chained with where'
        test_161: Test = Test()
        try:
            t_11587: 'SafeIdentifier' = sid_638('orders')
            t_11588: 'SafeIdentifier' = sid_638('user_id')
            sub_1639: 'Query' = from_(t_11587).select((t_11588,))
            t_11590: 'SafeIdentifier' = sid_638('users')
            t_11591: 'SqlBuilder' = SqlBuilder()
            t_11591.append_safe('active = ')
            t_11591.append_boolean(True)
            t_11594: 'SqlFragment' = t_11591.accumulated
            q_1640: 'Query' = from_(t_11590).where(t_11594).where_in_subquery(sid_638('id'), sub_1639)
            s_1641: 'str34' = q_1640.to_sql().to_string()
            t_11601: 'bool42' = s_1641 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)'
            def fn_11586() -> 'str34':
                return str_cat_14298('whereInSubquery chained: ', s_1641)
            test_161.assert_(t_11601, fn_11586)
        finally:
            test_161.soft_fail_to_hard()
class TestCase184(TestCase53):
    def test___existsSqlUsedInWhere__2272(self) -> None:
        'existsSql used in where'
        test_162: Test = Test()
        try:
            t_11573: 'SafeIdentifier' = sid_638('orders')
            t_11574: 'SqlBuilder' = SqlBuilder()
            t_11574.append_safe('orders.user_id = users.id')
            t_11576: 'SqlFragment' = t_11574.accumulated
            sub_1643: 'Query' = from_(t_11573).where(t_11576)
            t_11578: 'SafeIdentifier' = sid_638('users')
            t_11579: 'SqlFragment' = exists_sql(sub_1643)
            q_1644: 'Query' = from_(t_11578).where(t_11579)
            s_1645: 'str34' = q_1644.to_sql().to_string()
            t_11584: 'bool42' = s_1645 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_11572() -> 'str34':
                return str_cat_14298('exists in where: ', s_1645)
            test_162.assert_(t_11584, fn_11572)
        finally:
            test_162.soft_fail_to_hard()
class TestCase185(TestCase53):
    def test___updateQueryBasic__2274(self) -> None:
        'UpdateQuery basic'
        test_163: Test = Test()
        try:
            t_11559: 'SafeIdentifier' = sid_638('users')
            t_11560: 'SafeIdentifier' = sid_638('name')
            t_11561: 'SqlString' = SqlString('Alice')
            t_11562: 'UpdateQuery' = update(t_11559).set(t_11560, t_11561)
            t_11563: 'SqlBuilder' = SqlBuilder()
            t_11563.append_safe('id = ')
            t_11563.append_int32(1)
            t_5687: 'SqlFragment'
            t_5687 = t_11562.where(t_11563.accumulated).to_sql()
            q_1647: 'SqlFragment' = t_5687
            t_11570: 'bool42' = q_1647.to_string() == "UPDATE users SET name = 'Alice' WHERE id = 1"
            def fn_11558() -> 'str34':
                return 'update basic'
            test_163.assert_(t_11570, fn_11558)
        finally:
            test_163.soft_fail_to_hard()
class TestCase186(TestCase53):
    def test___updateQueryMultipleSet__2276(self) -> None:
        'UpdateQuery multiple SET'
        test_164: Test = Test()
        try:
            t_11542: 'SafeIdentifier' = sid_638('users')
            t_11543: 'SafeIdentifier' = sid_638('name')
            t_11544: 'SqlString' = SqlString('Bob')
            t_11548: 'UpdateQuery' = update(t_11542).set(t_11543, t_11544).set(sid_638('age'), SqlInt32(30))
            t_11549: 'SqlBuilder' = SqlBuilder()
            t_11549.append_safe('id = ')
            t_11549.append_int32(2)
            t_5672: 'SqlFragment'
            t_5672 = t_11548.where(t_11549.accumulated).to_sql()
            q_1649: 'SqlFragment' = t_5672
            t_11556: 'bool42' = q_1649.to_string() == "UPDATE users SET name = 'Bob', age = 30 WHERE id = 2"
            def fn_11541() -> 'str34':
                return 'update multi set'
            test_164.assert_(t_11556, fn_11541)
        finally:
            test_164.soft_fail_to_hard()
class TestCase187(TestCase53):
    def test___updateQueryMultipleWhere__2278(self) -> None:
        'UpdateQuery multiple WHERE'
        test_165: Test = Test()
        try:
            t_11523: 'SafeIdentifier' = sid_638('users')
            t_11524: 'SafeIdentifier' = sid_638('active')
            t_11525: 'SqlBoolean' = SqlBoolean(False)
            t_11526: 'UpdateQuery' = update(t_11523).set(t_11524, t_11525)
            t_11527: 'SqlBuilder' = SqlBuilder()
            t_11527.append_safe('age < ')
            t_11527.append_int32(18)
            t_11531: 'UpdateQuery' = t_11526.where(t_11527.accumulated)
            t_11532: 'SqlBuilder' = SqlBuilder()
            t_11532.append_safe('role = ')
            t_11532.append_string('guest')
            t_5654: 'SqlFragment'
            t_5654 = t_11531.where(t_11532.accumulated).to_sql()
            q_1651: 'SqlFragment' = t_5654
            t_11539: 'bool42' = q_1651.to_string() == "UPDATE users SET active = FALSE WHERE age < 18 AND role = 'guest'"
            def fn_11522() -> 'str34':
                return 'update multi where'
            test_165.assert_(t_11539, fn_11522)
        finally:
            test_165.soft_fail_to_hard()
class TestCase188(TestCase53):
    def test___updateQueryOrWhere__2281(self) -> None:
        'UpdateQuery orWhere'
        test_166: Test = Test()
        try:
            t_11504: 'SafeIdentifier' = sid_638('users')
            t_11505: 'SafeIdentifier' = sid_638('status')
            t_11506: 'SqlString' = SqlString('banned')
            t_11507: 'UpdateQuery' = update(t_11504).set(t_11505, t_11506)
            t_11508: 'SqlBuilder' = SqlBuilder()
            t_11508.append_safe('spam_count > ')
            t_11508.append_int32(10)
            t_11512: 'UpdateQuery' = t_11507.where(t_11508.accumulated)
            t_11513: 'SqlBuilder' = SqlBuilder()
            t_11513.append_safe('reported = ')
            t_11513.append_boolean(True)
            t_5633: 'SqlFragment'
            t_5633 = t_11512.or_where(t_11513.accumulated).to_sql()
            q_1653: 'SqlFragment' = t_5633
            t_11520: 'bool42' = q_1653.to_string() == "UPDATE users SET status = 'banned' WHERE spam_count > 10 OR reported = TRUE"
            def fn_11503() -> 'str34':
                return 'update orWhere'
            test_166.assert_(t_11520, fn_11503)
        finally:
            test_166.soft_fail_to_hard()
class TestCase189(TestCase53):
    def test___updateQueryBubblesWithoutWhere__2284(self) -> None:
        'UpdateQuery bubbles without WHERE'
        test_167: Test = Test()
        try:
            t_11497: 'SafeIdentifier'
            t_11498: 'SafeIdentifier'
            t_11499: 'SqlInt32'
            did_bubble_1655: 'bool42'
            try:
                t_11497 = sid_638('users')
                t_11498 = sid_638('x')
                t_11499 = SqlInt32(1)
                update(t_11497).set(t_11498, t_11499).to_sql()
                did_bubble_1655 = False
            except Exception46:
                did_bubble_1655 = True
            def fn_11496() -> 'str34':
                return 'update without WHERE should bubble'
            test_167.assert_(did_bubble_1655, fn_11496)
        finally:
            test_167.soft_fail_to_hard()
class TestCase190(TestCase53):
    def test___updateQueryBubblesWithoutSet__2285(self) -> None:
        'UpdateQuery bubbles without SET'
        test_168: Test = Test()
        try:
            t_11488: 'SafeIdentifier'
            t_11489: 'SqlBuilder'
            t_11492: 'SqlFragment'
            did_bubble_1657: 'bool42'
            try:
                t_11488 = sid_638('users')
                t_11489 = SqlBuilder()
                t_11489.append_safe('id = ')
                t_11489.append_int32(1)
                t_11492 = t_11489.accumulated
                update(t_11488).where(t_11492).to_sql()
                did_bubble_1657 = False
            except Exception46:
                did_bubble_1657 = True
            def fn_11487() -> 'str34':
                return 'update without SET should bubble'
            test_168.assert_(did_bubble_1657, fn_11487)
        finally:
            test_168.soft_fail_to_hard()
class TestCase191(TestCase53):
    def test___updateQueryWithLimit__2287(self) -> None:
        'UpdateQuery with limit'
        test_169: Test = Test()
        try:
            t_11474: 'SafeIdentifier' = sid_638('users')
            t_11475: 'SafeIdentifier' = sid_638('active')
            t_11476: 'SqlBoolean' = SqlBoolean(False)
            t_11477: 'UpdateQuery' = update(t_11474).set(t_11475, t_11476)
            t_11478: 'SqlBuilder' = SqlBuilder()
            t_11478.append_safe('last_login < ')
            t_11478.append_string('2024-01-01')
            t_5596: 'UpdateQuery'
            t_5596 = t_11477.where(t_11478.accumulated).limit(100)
            t_5597: 'SqlFragment'
            t_5597 = t_5596.to_sql()
            q_1659: 'SqlFragment' = t_5597
            t_11485: 'bool42' = q_1659.to_string() == "UPDATE users SET active = FALSE WHERE last_login < '2024-01-01' LIMIT 100"
            def fn_11473() -> 'str34':
                return 'update limit'
            test_169.assert_(t_11485, fn_11473)
        finally:
            test_169.soft_fail_to_hard()
class TestCase192(TestCase53):
    def test___updateQueryEscaping__2289(self) -> None:
        'UpdateQuery escaping'
        test_170: Test = Test()
        try:
            t_11460: 'SafeIdentifier' = sid_638('users')
            t_11461: 'SafeIdentifier' = sid_638('bio')
            t_11462: 'SqlString' = SqlString("It's a test")
            t_11463: 'UpdateQuery' = update(t_11460).set(t_11461, t_11462)
            t_11464: 'SqlBuilder' = SqlBuilder()
            t_11464.append_safe('id = ')
            t_11464.append_int32(1)
            t_5581: 'SqlFragment'
            t_5581 = t_11463.where(t_11464.accumulated).to_sql()
            q_1661: 'SqlFragment' = t_5581
            t_11471: 'bool42' = q_1661.to_string() == "UPDATE users SET bio = 'It''s a test' WHERE id = 1"
            def fn_11459() -> 'str34':
                return 'update escaping'
            test_170.assert_(t_11471, fn_11459)
        finally:
            test_170.soft_fail_to_hard()
class TestCase193(TestCase53):
    def test___deleteQueryBasic__2291(self) -> None:
        'DeleteQuery basic'
        test_171: Test = Test()
        try:
            t_11449: 'SafeIdentifier' = sid_638('users')
            t_11450: 'SqlBuilder' = SqlBuilder()
            t_11450.append_safe('id = ')
            t_11450.append_int32(1)
            t_11453: 'SqlFragment' = t_11450.accumulated
            t_5566: 'SqlFragment'
            t_5566 = delete_from(t_11449).where(t_11453).to_sql()
            q_1663: 'SqlFragment' = t_5566
            t_11457: 'bool42' = q_1663.to_string() == 'DELETE FROM users WHERE id = 1'
            def fn_11448() -> 'str34':
                return 'delete basic'
            test_171.assert_(t_11457, fn_11448)
        finally:
            test_171.soft_fail_to_hard()
class TestCase194(TestCase53):
    def test___deleteQueryMultipleWhere__2293(self) -> None:
        'DeleteQuery multiple WHERE'
        test_172: Test = Test()
        try:
            t_11433: 'SafeIdentifier' = sid_638('logs')
            t_11434: 'SqlBuilder' = SqlBuilder()
            t_11434.append_safe('created_at < ')
            t_11434.append_string('2024-01-01')
            t_11437: 'SqlFragment' = t_11434.accumulated
            t_11438: 'DeleteQuery' = delete_from(t_11433).where(t_11437)
            t_11439: 'SqlBuilder' = SqlBuilder()
            t_11439.append_safe('level = ')
            t_11439.append_string('debug')
            t_5554: 'SqlFragment'
            t_5554 = t_11438.where(t_11439.accumulated).to_sql()
            q_1665: 'SqlFragment' = t_5554
            t_11446: 'bool42' = q_1665.to_string() == "DELETE FROM logs WHERE created_at < '2024-01-01' AND level = 'debug'"
            def fn_11432() -> 'str34':
                return 'delete multi where'
            test_172.assert_(t_11446, fn_11432)
        finally:
            test_172.soft_fail_to_hard()
class TestCase195(TestCase53):
    def test___deleteQueryBubblesWithoutWhere__2296(self) -> None:
        'DeleteQuery bubbles without WHERE'
        test_173: Test = Test()
        try:
            did_bubble_1667: 'bool42'
            try:
                delete_from(sid_638('users')).to_sql()
                did_bubble_1667 = False
            except Exception46:
                did_bubble_1667 = True
            def fn_11428() -> 'str34':
                return 'delete without WHERE should bubble'
            test_173.assert_(did_bubble_1667, fn_11428)
        finally:
            test_173.soft_fail_to_hard()
class TestCase196(TestCase53):
    def test___deleteQueryOrWhere__2297(self) -> None:
        'DeleteQuery orWhere'
        test_174: Test = Test()
        try:
            t_11413: 'SafeIdentifier' = sid_638('sessions')
            t_11414: 'SqlBuilder' = SqlBuilder()
            t_11414.append_safe('expired = ')
            t_11414.append_boolean(True)
            t_11417: 'SqlFragment' = t_11414.accumulated
            t_11418: 'DeleteQuery' = delete_from(t_11413).where(t_11417)
            t_11419: 'SqlBuilder' = SqlBuilder()
            t_11419.append_safe('created_at < ')
            t_11419.append_string('2023-01-01')
            t_5533: 'SqlFragment'
            t_5533 = t_11418.or_where(t_11419.accumulated).to_sql()
            q_1669: 'SqlFragment' = t_5533
            t_11426: 'bool42' = q_1669.to_string() == "DELETE FROM sessions WHERE expired = TRUE OR created_at < '2023-01-01'"
            def fn_11412() -> 'str34':
                return 'delete orWhere'
            test_174.assert_(t_11426, fn_11412)
        finally:
            test_174.soft_fail_to_hard()
class TestCase197(TestCase53):
    def test___deleteQueryWithLimit__2300(self) -> None:
        'DeleteQuery with limit'
        test_175: Test = Test()
        try:
            t_11402: 'SafeIdentifier' = sid_638('logs')
            t_11403: 'SqlBuilder' = SqlBuilder()
            t_11403.append_safe('level = ')
            t_11403.append_string('debug')
            t_11406: 'SqlFragment' = t_11403.accumulated
            t_5514: 'DeleteQuery'
            t_5514 = delete_from(t_11402).where(t_11406).limit(1000)
            t_5515: 'SqlFragment'
            t_5515 = t_5514.to_sql()
            q_1671: 'SqlFragment' = t_5515
            t_11410: 'bool42' = q_1671.to_string() == "DELETE FROM logs WHERE level = 'debug' LIMIT 1000"
            def fn_11401() -> 'str34':
                return 'delete limit'
            test_175.assert_(t_11410, fn_11401)
        finally:
            test_175.soft_fail_to_hard()
class TestCase198(TestCase53):
    def test___orderByNullsNullsFirst__2302(self) -> None:
        'orderByNulls NULLS FIRST'
        test_176: Test = Test()
        try:
            t_11392: 'SafeIdentifier' = sid_638('users')
            t_11393: 'SafeIdentifier' = sid_638('email')
            t_11394: 'NullsFirst' = NullsFirst()
            q_1673: 'Query' = from_(t_11392).order_by_nulls(t_11393, True, t_11394)
            t_11399: 'bool42' = q_1673.to_sql().to_string() == 'SELECT * FROM users ORDER BY email ASC NULLS FIRST'
            def fn_11391() -> 'str34':
                return 'nulls first'
            test_176.assert_(t_11399, fn_11391)
        finally:
            test_176.soft_fail_to_hard()
class TestCase199(TestCase53):
    def test___orderByNullsNullsLast__2303(self) -> None:
        'orderByNulls NULLS LAST'
        test_177: Test = Test()
        try:
            t_11382: 'SafeIdentifier' = sid_638('users')
            t_11383: 'SafeIdentifier' = sid_638('score')
            t_11384: 'NullsLast' = NullsLast()
            q_1675: 'Query' = from_(t_11382).order_by_nulls(t_11383, False, t_11384)
            t_11389: 'bool42' = q_1675.to_sql().to_string() == 'SELECT * FROM users ORDER BY score DESC NULLS LAST'
            def fn_11381() -> 'str34':
                return 'nulls last'
            test_177.assert_(t_11389, fn_11381)
        finally:
            test_177.soft_fail_to_hard()
class TestCase200(TestCase53):
    def test___mixedOrderByAndOrderByNulls__2304(self) -> None:
        'mixed orderBy and orderByNulls'
        test_178: Test = Test()
        try:
            t_11370: 'SafeIdentifier' = sid_638('users')
            t_11371: 'SafeIdentifier' = sid_638('name')
            q_1677: 'Query' = from_(t_11370).order_by(t_11371, True).order_by_nulls(sid_638('email'), True, NullsFirst())
            t_11379: 'bool42' = q_1677.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC, email ASC NULLS FIRST'
            def fn_11369() -> 'str34':
                return 'mixed order'
            test_178.assert_(t_11379, fn_11369)
        finally:
            test_178.soft_fail_to_hard()
class TestCase201(TestCase53):
    def test___crossJoin__2305(self) -> None:
        'crossJoin'
        test_179: Test = Test()
        try:
            t_11361: 'SafeIdentifier' = sid_638('users')
            t_11362: 'SafeIdentifier' = sid_638('colors')
            q_1679: 'Query' = from_(t_11361).cross_join(t_11362)
            t_11367: 'bool42' = q_1679.to_sql().to_string() == 'SELECT * FROM users CROSS JOIN colors'
            def fn_11360() -> 'str34':
                return 'cross join'
            test_179.assert_(t_11367, fn_11360)
        finally:
            test_179.soft_fail_to_hard()
class TestCase202(TestCase53):
    def test___crossJoinCombinedWithOtherJoins__2306(self) -> None:
        'crossJoin combined with other joins'
        test_180: Test = Test()
        try:
            t_11347: 'SafeIdentifier' = sid_638('users')
            t_11348: 'SafeIdentifier' = sid_638('orders')
            t_11349: 'SqlBuilder' = SqlBuilder()
            t_11349.append_safe('users.id = orders.user_id')
            t_11351: 'SqlFragment' = t_11349.accumulated
            q_1681: 'Query' = from_(t_11347).inner_join(t_11348, t_11351).cross_join(sid_638('colors'))
            t_11358: 'bool42' = q_1681.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id CROSS JOIN colors'
            def fn_11346() -> 'str34':
                return 'cross + inner join'
            test_180.assert_(t_11358, fn_11346)
        finally:
            test_180.soft_fail_to_hard()
class TestCase203(TestCase53):
    def test___lockForUpdate__2308(self) -> None:
        'lock FOR UPDATE'
        test_181: Test = Test()
        try:
            t_11333: 'SafeIdentifier' = sid_638('users')
            t_11334: 'SqlBuilder' = SqlBuilder()
            t_11334.append_safe('id = ')
            t_11334.append_int32(1)
            t_11337: 'SqlFragment' = t_11334.accumulated
            q_1683: 'Query' = from_(t_11333).where(t_11337).lock(ForUpdate())
            t_11344: 'bool42' = q_1683.to_sql().to_string() == 'SELECT * FROM users WHERE id = 1 FOR UPDATE'
            def fn_11332() -> 'str34':
                return 'for update'
            test_181.assert_(t_11344, fn_11332)
        finally:
            test_181.soft_fail_to_hard()
class TestCase204(TestCase53):
    def test___lockForShare__2310(self) -> None:
        'lock FOR SHARE'
        test_182: Test = Test()
        try:
            t_11322: 'SafeIdentifier' = sid_638('users')
            t_11323: 'SafeIdentifier' = sid_638('name')
            q_1685: 'Query' = from_(t_11322).select((t_11323,)).lock(ForShare())
            t_11330: 'bool42' = q_1685.to_sql().to_string() == 'SELECT name FROM users FOR SHARE'
            def fn_11321() -> 'str34':
                return 'for share'
            test_182.assert_(t_11330, fn_11321)
        finally:
            test_182.soft_fail_to_hard()
class TestCase205(TestCase53):
    def test___lockWithFullQuery__2311(self) -> None:
        'lock with full query'
        test_183: Test = Test()
        try:
            t_11308: 'SafeIdentifier' = sid_638('accounts')
            t_11309: 'SqlBuilder' = SqlBuilder()
            t_11309.append_safe('id = ')
            t_11309.append_int32(42)
            t_11312: 'SqlFragment' = t_11309.accumulated
            t_5438: 'Query'
            t_5438 = from_(t_11308).where(t_11312).limit(1)
            t_11315: 'Query' = t_5438.lock(ForUpdate())
            q_1687: 'Query' = t_11315
            t_11319: 'bool42' = q_1687.to_sql().to_string() == 'SELECT * FROM accounts WHERE id = 42 LIMIT 1 FOR UPDATE'
            def fn_11307() -> 'str34':
                return 'lock full query'
            test_183.assert_(t_11319, fn_11307)
        finally:
            test_183.soft_fail_to_hard()
class TestCase206(TestCase53):
    def test___safeIdentifierAcceptsValidNames__2313(self) -> None:
        'safeIdentifier accepts valid names'
        test_190: Test = Test()
        try:
            t_5427: 'SafeIdentifier'
            t_5427 = safe_identifier('user_name')
            id_1725: 'SafeIdentifier' = t_5427
            t_11305: 'bool42' = id_1725.sql_value == 'user_name'
            def fn_11302() -> 'str34':
                return 'value should round-trip'
            test_190.assert_(t_11305, fn_11302)
        finally:
            test_190.soft_fail_to_hard()
class TestCase207(TestCase53):
    def test___safeIdentifierRejectsEmptyString__2314(self) -> None:
        'safeIdentifier rejects empty string'
        test_191: Test = Test()
        try:
            did_bubble_1727: 'bool42'
            try:
                safe_identifier('')
                did_bubble_1727 = False
            except Exception46:
                did_bubble_1727 = True
            def fn_11299() -> 'str34':
                return 'empty string should bubble'
            test_191.assert_(did_bubble_1727, fn_11299)
        finally:
            test_191.soft_fail_to_hard()
class TestCase208(TestCase53):
    def test___safeIdentifierRejectsLeadingDigit__2315(self) -> None:
        'safeIdentifier rejects leading digit'
        test_192: Test = Test()
        try:
            did_bubble_1729: 'bool42'
            try:
                safe_identifier('1col')
                did_bubble_1729 = False
            except Exception46:
                did_bubble_1729 = True
            def fn_11296() -> 'str34':
                return 'leading digit should bubble'
            test_192.assert_(did_bubble_1729, fn_11296)
        finally:
            test_192.soft_fail_to_hard()
class TestCase209(TestCase53):
    def test___safeIdentifierRejectsSqlMetacharacters__2316(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_193: Test = Test()
        try:
            cases_1731: 'Sequence38[str34]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_11293(c_1732: 'str34') -> 'None':
                did_bubble_1733: 'bool42'
                try:
                    safe_identifier(c_1732)
                    did_bubble_1733 = False
                except Exception46:
                    did_bubble_1733 = True
                def fn_11290() -> 'str34':
                    return str_cat_14298('should reject: ', c_1732)
                test_193.assert_(did_bubble_1733, fn_11290)
            list_for_each_14290(cases_1731, fn_11293)
        finally:
            test_193.soft_fail_to_hard()
class TestCase210(TestCase53):
    def test___tableDefFieldLookupFound__2317(self) -> None:
        'TableDef field lookup - found'
        test_194: Test = Test()
        try:
            t_5404: 'SafeIdentifier'
            t_5404 = safe_identifier('users')
            t_5405: 'SafeIdentifier' = t_5404
            t_5406: 'SafeIdentifier'
            t_5406 = safe_identifier('name')
            t_5407: 'SafeIdentifier' = t_5406
            t_11280: 'StringField' = StringField()
            t_11281: 'FieldDef' = FieldDef(t_5407, t_11280, False)
            t_5410: 'SafeIdentifier'
            t_5410 = safe_identifier('age')
            t_5411: 'SafeIdentifier' = t_5410
            t_11282: 'IntField' = IntField()
            t_11283: 'FieldDef' = FieldDef(t_5411, t_11282, False)
            td_1735: 'TableDef' = TableDef(t_5405, (t_11281, t_11283))
            t_5415: 'FieldDef'
            t_5415 = td_1735.field('age')
            f_1736: 'FieldDef' = t_5415
            t_11288: 'bool42' = f_1736.name.sql_value == 'age'
            def fn_11279() -> 'str34':
                return 'should find age field'
            test_194.assert_(t_11288, fn_11279)
        finally:
            test_194.soft_fail_to_hard()
class TestCase211(TestCase53):
    def test___tableDefFieldLookupNotFoundBubbles__2318(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_195: Test = Test()
        try:
            t_5395: 'SafeIdentifier'
            t_5395 = safe_identifier('users')
            t_5396: 'SafeIdentifier' = t_5395
            t_5397: 'SafeIdentifier'
            t_5397 = safe_identifier('name')
            t_5398: 'SafeIdentifier' = t_5397
            t_11274: 'StringField' = StringField()
            t_11275: 'FieldDef' = FieldDef(t_5398, t_11274, False)
            td_1738: 'TableDef' = TableDef(t_5396, (t_11275,))
            did_bubble_1739: 'bool42'
            try:
                td_1738.field('nonexistent')
                did_bubble_1739 = False
            except Exception46:
                did_bubble_1739 = True
            def fn_11273() -> 'str34':
                return 'unknown field should bubble'
            test_195.assert_(did_bubble_1739, fn_11273)
        finally:
            test_195.soft_fail_to_hard()
class TestCase212(TestCase53):
    def test___fieldDefNullableFlag__2319(self) -> None:
        'FieldDef nullable flag'
        test_196: Test = Test()
        try:
            t_5383: 'SafeIdentifier'
            t_5383 = safe_identifier('email')
            t_5384: 'SafeIdentifier' = t_5383
            t_11262: 'StringField' = StringField()
            required_1741: 'FieldDef' = FieldDef(t_5384, t_11262, False)
            t_5387: 'SafeIdentifier'
            t_5387 = safe_identifier('bio')
            t_5388: 'SafeIdentifier' = t_5387
            t_11264: 'StringField' = StringField()
            optional_1742: 'FieldDef' = FieldDef(t_5388, t_11264, True)
            t_11268: 'bool42' = not required_1741.nullable
            def fn_11261() -> 'str34':
                return 'required field should not be nullable'
            test_196.assert_(t_11268, fn_11261)
            t_11270: 'bool42' = optional_1742.nullable
            def fn_11260() -> 'str34':
                return 'optional field should be nullable'
            test_196.assert_(t_11270, fn_11260)
        finally:
            test_196.soft_fail_to_hard()
class TestCase213(TestCase53):
    def test___stringEscaping__2320(self) -> None:
        'string escaping'
        test_200: Test = Test()
        try:
            def build_1868(name_1870: 'str34') -> 'str34':
                t_11242: 'SqlBuilder' = SqlBuilder()
                t_11242.append_safe('select * from hi where name = ')
                t_11242.append_string(name_1870)
                return t_11242.accumulated.to_string()
            def build_wrong_1869(name_1872: 'str34') -> 'str34':
                return str_cat_14298("select * from hi where name = '", name_1872, "'")
            actual_2322: 'str34' = build_1868('world')
            t_11252: 'bool42' = actual_2322 == "select * from hi where name = 'world'"
            def fn_11249() -> 'str34':
                return str_cat_14298('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_2322, ')')
            test_200.assert_(t_11252, fn_11249)
            bobby_tables_1874: 'str34' = "Robert'); drop table hi;--"
            actual_2324: 'str34' = build_1868("Robert'); drop table hi;--")
            t_11256: 'bool42' = actual_2324 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_11248() -> 'str34':
                return str_cat_14298('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_2324, ')')
            test_200.assert_(t_11256, fn_11248)
            def fn_11247() -> 'str34':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_200.assert_(True, fn_11247)
        finally:
            test_200.soft_fail_to_hard()
class TestCase214(TestCase53):
    def test___stringEdgeCases__2328(self) -> None:
        'string edge cases'
        test_201: Test = Test()
        try:
            t_11210: 'SqlBuilder' = SqlBuilder()
            t_11210.append_safe('v = ')
            t_11210.append_string('')
            actual_2329: 'str34' = t_11210.accumulated.to_string()
            t_11216: 'bool42' = actual_2329 == "v = ''"
            def fn_11209() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_2329, ')')
            test_201.assert_(t_11216, fn_11209)
            t_11218: 'SqlBuilder' = SqlBuilder()
            t_11218.append_safe('v = ')
            t_11218.append_string("a''b")
            actual_2332: 'str34' = t_11218.accumulated.to_string()
            t_11224: 'bool42' = actual_2332 == "v = 'a''''b'"
            def fn_11208() -> 'str34':
                return str_cat_14298("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_2332, ')')
            test_201.assert_(t_11224, fn_11208)
            t_11226: 'SqlBuilder' = SqlBuilder()
            t_11226.append_safe('v = ')
            t_11226.append_string('Hello \u4e16\u754c')
            actual_2335: 'str34' = t_11226.accumulated.to_string()
            t_11232: 'bool42' = actual_2335 == "v = 'Hello \u4e16\u754c'"
            def fn_11207() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_2335, ')')
            test_201.assert_(t_11232, fn_11207)
            t_11234: 'SqlBuilder' = SqlBuilder()
            t_11234.append_safe('v = ')
            t_11234.append_string('Line1\nLine2')
            actual_2338: 'str34' = t_11234.accumulated.to_string()
            t_11240: 'bool42' = actual_2338 == "v = 'Line1\nLine2'"
            def fn_11206() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_2338, ')')
            test_201.assert_(t_11240, fn_11206)
        finally:
            test_201.soft_fail_to_hard()
class TestCase215(TestCase53):
    def test___numbersAndBooleans__2341(self) -> None:
        'numbers and booleans'
        test_202: Test = Test()
        try:
            t_11181: 'SqlBuilder' = SqlBuilder()
            t_11181.append_safe('select ')
            t_11181.append_int32(42)
            t_11181.append_safe(', ')
            t_11181.append_int64(43)
            t_11181.append_safe(', ')
            t_11181.append_float64(19.99)
            t_11181.append_safe(', ')
            t_11181.append_boolean(True)
            t_11181.append_safe(', ')
            t_11181.append_boolean(False)
            actual_2342: 'str34' = t_11181.accumulated.to_string()
            t_11195: 'bool42' = actual_2342 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_11180() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_2342, ')')
            test_202.assert_(t_11195, fn_11180)
            t_5328: 'date33'
            t_5328 = date_14330(2024, 12, 25)
            date_1877: 'date33' = t_5328
            t_11197: 'SqlBuilder' = SqlBuilder()
            t_11197.append_safe('insert into t values (')
            t_11197.append_date(date_1877)
            t_11197.append_safe(')')
            actual_2345: 'str34' = t_11197.accumulated.to_string()
            t_11204: 'bool42' = actual_2345 == "insert into t values ('2024-12-25')"
            def fn_11179() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_2345, ')')
            test_202.assert_(t_11204, fn_11179)
        finally:
            test_202.soft_fail_to_hard()
class TestCase216(TestCase53):
    def test___lists__2348(self) -> None:
        'lists'
        test_203: Test = Test()
        try:
            t_11125: 'SqlBuilder' = SqlBuilder()
            t_11125.append_safe('v IN (')
            t_11125.append_string_list(('a', 'b', "c'd"))
            t_11125.append_safe(')')
            actual_2349: 'str34' = t_11125.accumulated.to_string()
            t_11132: 'bool42' = actual_2349 == "v IN ('a', 'b', 'c''d')"
            def fn_11124() -> 'str34':
                return str_cat_14298("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_2349, ')')
            test_203.assert_(t_11132, fn_11124)
            t_11134: 'SqlBuilder' = SqlBuilder()
            t_11134.append_safe('v IN (')
            t_11134.append_int32_list((1, 2, 3))
            t_11134.append_safe(')')
            actual_2352: 'str34' = t_11134.accumulated.to_string()
            t_11141: 'bool42' = actual_2352 == 'v IN (1, 2, 3)'
            def fn_11123() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_2352, ')')
            test_203.assert_(t_11141, fn_11123)
            t_11143: 'SqlBuilder' = SqlBuilder()
            t_11143.append_safe('v IN (')
            t_11143.append_int64_list((1, 2))
            t_11143.append_safe(')')
            actual_2355: 'str34' = t_11143.accumulated.to_string()
            t_11150: 'bool42' = actual_2355 == 'v IN (1, 2)'
            def fn_11122() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_2355, ')')
            test_203.assert_(t_11150, fn_11122)
            t_11152: 'SqlBuilder' = SqlBuilder()
            t_11152.append_safe('v IN (')
            t_11152.append_float64_list((1.0, 2.0))
            t_11152.append_safe(')')
            actual_2358: 'str34' = t_11152.accumulated.to_string()
            t_11159: 'bool42' = actual_2358 == 'v IN (1.0, 2.0)'
            def fn_11121() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_2358, ')')
            test_203.assert_(t_11159, fn_11121)
            t_11161: 'SqlBuilder' = SqlBuilder()
            t_11161.append_safe('v IN (')
            t_11161.append_boolean_list((True, False))
            t_11161.append_safe(')')
            actual_2361: 'str34' = t_11161.accumulated.to_string()
            t_11168: 'bool42' = actual_2361 == 'v IN (TRUE, FALSE)'
            def fn_11120() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_2361, ')')
            test_203.assert_(t_11168, fn_11120)
            t_5300: 'date33'
            t_5300 = date_14330(2024, 1, 1)
            t_5301: 'date33' = t_5300
            t_5302: 'date33'
            t_5302 = date_14330(2024, 12, 25)
            t_5303: 'date33' = t_5302
            dates_1879: 'Sequence38[date33]' = (t_5301, t_5303)
            t_11170: 'SqlBuilder' = SqlBuilder()
            t_11170.append_safe('v IN (')
            t_11170.append_date_list(dates_1879)
            t_11170.append_safe(')')
            actual_2364: 'str34' = t_11170.accumulated.to_string()
            t_11177: 'bool42' = actual_2364 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_11119() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_2364, ')')
            test_203.assert_(t_11177, fn_11119)
        finally:
            test_203.soft_fail_to_hard()
class TestCase217(TestCase53):
    def test___sqlFloat64_naNRendersAsNull__2367(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_204: Test = Test()
        try:
            nan_1881: 'float36'
            nan_1881 = 0.0 / 0.0
            t_11111: 'SqlBuilder' = SqlBuilder()
            t_11111.append_safe('v = ')
            t_11111.append_float64(nan_1881)
            actual_2368: 'str34' = t_11111.accumulated.to_string()
            t_11117: 'bool42' = actual_2368 == 'v = NULL'
            def fn_11110() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_2368, ')')
            test_204.assert_(t_11117, fn_11110)
        finally:
            test_204.soft_fail_to_hard()
class TestCase218(TestCase53):
    def test___sqlFloat64_infinityRendersAsNull__2371(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_205: Test = Test()
        try:
            inf_1883: 'float36'
            inf_1883 = 1.0 / 0.0
            t_11102: 'SqlBuilder' = SqlBuilder()
            t_11102.append_safe('v = ')
            t_11102.append_float64(inf_1883)
            actual_2372: 'str34' = t_11102.accumulated.to_string()
            t_11108: 'bool42' = actual_2372 == 'v = NULL'
            def fn_11101() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_2372, ')')
            test_205.assert_(t_11108, fn_11101)
        finally:
            test_205.soft_fail_to_hard()
class TestCase219(TestCase53):
    def test___sqlFloat64_negativeInfinityRendersAsNull__2375(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_206: Test = Test()
        try:
            ninf_1885: 'float36'
            ninf_1885 = -1.0 / 0.0
            t_11093: 'SqlBuilder' = SqlBuilder()
            t_11093.append_safe('v = ')
            t_11093.append_float64(ninf_1885)
            actual_2376: 'str34' = t_11093.accumulated.to_string()
            t_11099: 'bool42' = actual_2376 == 'v = NULL'
            def fn_11092() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_2376, ')')
            test_206.assert_(t_11099, fn_11092)
        finally:
            test_206.soft_fail_to_hard()
class TestCase220(TestCase53):
    def test___sqlFloat64_normalValuesStillWork__2379(self) -> None:
        'SqlFloat64 normal values still work'
        test_207: Test = Test()
        try:
            t_11068: 'SqlBuilder' = SqlBuilder()
            t_11068.append_safe('v = ')
            t_11068.append_float64(3.14)
            actual_2380: 'str34' = t_11068.accumulated.to_string()
            t_11074: 'bool42' = actual_2380 == 'v = 3.14'
            def fn_11067() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_2380, ')')
            test_207.assert_(t_11074, fn_11067)
            t_11076: 'SqlBuilder' = SqlBuilder()
            t_11076.append_safe('v = ')
            t_11076.append_float64(0.0)
            actual_2383: 'str34' = t_11076.accumulated.to_string()
            t_11082: 'bool42' = actual_2383 == 'v = 0.0'
            def fn_11066() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_2383, ')')
            test_207.assert_(t_11082, fn_11066)
            t_11084: 'SqlBuilder' = SqlBuilder()
            t_11084.append_safe('v = ')
            t_11084.append_float64(-42.5)
            actual_2386: 'str34' = t_11084.accumulated.to_string()
            t_11090: 'bool42' = actual_2386 == 'v = -42.5'
            def fn_11065() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_2386, ')')
            test_207.assert_(t_11090, fn_11065)
        finally:
            test_207.soft_fail_to_hard()
class TestCase221(TestCase53):
    def test___sqlDateRendersWithQuotes__2389(self) -> None:
        'SqlDate renders with quotes'
        test_208: Test = Test()
        try:
            t_5196: 'date33'
            t_5196 = date_14330(2024, 6, 15)
            d_1888: 'date33' = t_5196
            t_11057: 'SqlBuilder' = SqlBuilder()
            t_11057.append_safe('v = ')
            t_11057.append_date(d_1888)
            actual_2390: 'str34' = t_11057.accumulated.to_string()
            t_11063: 'bool42' = actual_2390 == "v = '2024-06-15'"
            def fn_11056() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_2390, ')')
            test_208.assert_(t_11063, fn_11056)
        finally:
            test_208.soft_fail_to_hard()
class TestCase222(TestCase53):
    def test___nesting__2393(self) -> None:
        'nesting'
        test_209: Test = Test()
        try:
            name_1890: 'str34' = 'Someone'
            t_11025: 'SqlBuilder' = SqlBuilder()
            t_11025.append_safe('where p.last_name = ')
            t_11025.append_string('Someone')
            condition_1891: 'SqlFragment' = t_11025.accumulated
            t_11029: 'SqlBuilder' = SqlBuilder()
            t_11029.append_safe('select p.id from person p ')
            t_11029.append_fragment(condition_1891)
            actual_2395: 'str34' = t_11029.accumulated.to_string()
            t_11035: 'bool42' = actual_2395 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_11024() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2395, ')')
            test_209.assert_(t_11035, fn_11024)
            t_11037: 'SqlBuilder' = SqlBuilder()
            t_11037.append_safe('select p.id from person p ')
            t_11037.append_part(condition_1891.to_source())
            actual_2398: 'str34' = t_11037.accumulated.to_string()
            t_11044: 'bool42' = actual_2398 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_11023() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2398, ')')
            test_209.assert_(t_11044, fn_11023)
            parts_1892: 'Sequence38[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_11048: 'SqlBuilder' = SqlBuilder()
            t_11048.append_safe('select ')
            t_11048.append_part_list(parts_1892)
            actual_2401: 'str34' = t_11048.accumulated.to_string()
            t_11054: 'bool42' = actual_2401 == "select 'a''b', 3"
            def fn_11022() -> 'str34':
                return str_cat_14298('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_2401, ')')
            test_209.assert_(t_11054, fn_11022)
        finally:
            test_209.soft_fail_to_hard()
