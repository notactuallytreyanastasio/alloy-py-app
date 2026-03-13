from temper_std.testing import Test
from builtins import str as str34, bool as bool42, Exception as Exception46, int as int40, float as float36
from unittest import TestCase as TestCase53
from types import MappingProxyType as MappingProxyType41
from typing import Sequence as Sequence38, MutableSequence as MutableSequence45
from datetime import date as date33
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_15602, pair_15603, changeset, Changeset, mapped_has_15567, len_15570, list_get_15578, str_cat_15572, list_for_each_15564, SqlFragment, NumberValidationOpts, SqlDefault, timestamps, list_15566, tuple_15569, delete_sql, from_, Query, SqlBuilder, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, update, UpdateQuery, SqlBoolean, delete_from, DeleteQuery, NullsFirst, NullsLast, ForUpdate, ForShare, date_15604, SqlPart
def csid_660(name_953: 'str34') -> 'SafeIdentifier':
    t_8354: 'SafeIdentifier'
    t_8354 = safe_identifier(name_953)
    return t_8354
def user_table_661() -> 'TableDef':
    return TableDef(csid_660('users'), (FieldDef(csid_660('name'), StringField(), False, None, False), FieldDef(csid_660('email'), StringField(), False, None, False), FieldDef(csid_660('age'), IntField(), True, None, False), FieldDef(csid_660('score'), FloatField(), True, None, False), FieldDef(csid_660('active'), BoolField(), True, None, False)), None)
class TestCase52(TestCase53):
    def test___castWhitelistsAllowedFields__2120(self) -> None:
        'cast whitelists allowed fields'
        test_32: Test = Test()
        try:
            params_957: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'), pair_15603('email', 'alice@example.com'), pair_15603('admin', 'true')))
            t_15072: 'TableDef' = user_table_661()
            t_15073: 'SafeIdentifier' = csid_660('name')
            t_15074: 'SafeIdentifier' = csid_660('email')
            cs_958: 'Changeset' = changeset(t_15072, params_957).cast((t_15073, t_15074))
            t_15077: 'bool42' = mapped_has_15567(cs_958.changes, 'name')
            def fn_15067() -> 'str34':
                return 'name should be in changes'
            test_32.assert_(t_15077, fn_15067)
            t_15081: 'bool42' = mapped_has_15567(cs_958.changes, 'email')
            def fn_15066() -> 'str34':
                return 'email should be in changes'
            test_32.assert_(t_15081, fn_15066)
            t_15087: 'bool42' = not mapped_has_15567(cs_958.changes, 'admin')
            def fn_15065() -> 'str34':
                return 'admin must be dropped (not in whitelist)'
            test_32.assert_(t_15087, fn_15065)
            t_15089: 'bool42' = cs_958.is_valid
            def fn_15064() -> 'str34':
                return 'should still be valid'
            test_32.assert_(t_15089, fn_15064)
        finally:
            test_32.soft_fail_to_hard()
class TestCase54(TestCase53):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__2121(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_33: Test = Test()
        try:
            params_960: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'), pair_15603('email', 'alice@example.com')))
            t_15050: 'TableDef' = user_table_661()
            t_15051: 'SafeIdentifier' = csid_660('name')
            cs_961: 'Changeset' = changeset(t_15050, params_960).cast((t_15051,)).cast((csid_660('email'),))
            t_15058: 'bool42' = not mapped_has_15567(cs_961.changes, 'name')
            def fn_15046() -> 'str34':
                return 'name must be excluded by second cast'
            test_33.assert_(t_15058, fn_15046)
            t_15061: 'bool42' = mapped_has_15567(cs_961.changes, 'email')
            def fn_15045() -> 'str34':
                return 'email should be present'
            test_33.assert_(t_15061, fn_15045)
        finally:
            test_33.soft_fail_to_hard()
class TestCase55(TestCase53):
    def test___castIgnoresEmptyStringValues__2122(self) -> None:
        'cast ignores empty string values'
        test_34: Test = Test()
        try:
            params_963: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', ''), pair_15603('email', 'bob@example.com')))
            t_15032: 'TableDef' = user_table_661()
            t_15033: 'SafeIdentifier' = csid_660('name')
            t_15034: 'SafeIdentifier' = csid_660('email')
            cs_964: 'Changeset' = changeset(t_15032, params_963).cast((t_15033, t_15034))
            t_15039: 'bool42' = not mapped_has_15567(cs_964.changes, 'name')
            def fn_15028() -> 'str34':
                return 'empty name should not be in changes'
            test_34.assert_(t_15039, fn_15028)
            t_15042: 'bool42' = mapped_has_15567(cs_964.changes, 'email')
            def fn_15027() -> 'str34':
                return 'email should be in changes'
            test_34.assert_(t_15042, fn_15027)
        finally:
            test_34.soft_fail_to_hard()
class TestCase56(TestCase53):
    def test___validateRequiredPassesWhenFieldPresent__2123(self) -> None:
        'validateRequired passes when field present'
        test_35: Test = Test()
        try:
            params_966: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_15014: 'TableDef' = user_table_661()
            t_15015: 'SafeIdentifier' = csid_660('name')
            cs_967: 'Changeset' = changeset(t_15014, params_966).cast((t_15015,)).validate_required((csid_660('name'),))
            t_15019: 'bool42' = cs_967.is_valid
            def fn_15011() -> 'str34':
                return 'should be valid'
            test_35.assert_(t_15019, fn_15011)
            t_15025: 'bool42' = len_15570(cs_967.errors) == 0
            def fn_15010() -> 'str34':
                return 'no errors expected'
            test_35.assert_(t_15025, fn_15010)
        finally:
            test_35.soft_fail_to_hard()
class TestCase57(TestCase53):
    def test___validateRequiredFailsWhenFieldMissing__2124(self) -> None:
        'validateRequired fails when field missing'
        test_36: Test = Test()
        try:
            params_969: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
            t_14990: 'TableDef' = user_table_661()
            t_14991: 'SafeIdentifier' = csid_660('name')
            cs_970: 'Changeset' = changeset(t_14990, params_969).cast((t_14991,)).validate_required((csid_660('name'),))
            t_14997: 'bool42' = not cs_970.is_valid
            def fn_14988() -> 'str34':
                return 'should be invalid'
            test_36.assert_(t_14997, fn_14988)
            t_15002: 'bool42' = len_15570(cs_970.errors) == 1
            def fn_14987() -> 'str34':
                return 'should have one error'
            test_36.assert_(t_15002, fn_14987)
            t_15008: 'bool42' = list_get_15578(cs_970.errors, 0).field == 'name'
            def fn_14986() -> 'str34':
                return 'error should name the field'
            test_36.assert_(t_15008, fn_14986)
        finally:
            test_36.soft_fail_to_hard()
class TestCase58(TestCase53):
    def test___validateLengthPassesWithinRange__2125(self) -> None:
        'validateLength passes within range'
        test_37: Test = Test()
        try:
            params_972: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14978: 'TableDef' = user_table_661()
            t_14979: 'SafeIdentifier' = csid_660('name')
            cs_973: 'Changeset' = changeset(t_14978, params_972).cast((t_14979,)).validate_length(csid_660('name'), 2, 50)
            t_14983: 'bool42' = cs_973.is_valid
            def fn_14975() -> 'str34':
                return 'should be valid'
            test_37.assert_(t_14983, fn_14975)
        finally:
            test_37.soft_fail_to_hard()
class TestCase59(TestCase53):
    def test___validateLengthFailsWhenTooShort__2126(self) -> None:
        'validateLength fails when too short'
        test_38: Test = Test()
        try:
            params_975: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'A'),))
            t_14966: 'TableDef' = user_table_661()
            t_14967: 'SafeIdentifier' = csid_660('name')
            cs_976: 'Changeset' = changeset(t_14966, params_975).cast((t_14967,)).validate_length(csid_660('name'), 2, 50)
            t_14973: 'bool42' = not cs_976.is_valid
            def fn_14963() -> 'str34':
                return 'should be invalid'
            test_38.assert_(t_14973, fn_14963)
        finally:
            test_38.soft_fail_to_hard()
class TestCase60(TestCase53):
    def test___validateLengthFailsWhenTooLong__2127(self) -> None:
        'validateLength fails when too long'
        test_39: Test = Test()
        try:
            params_978: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_14954: 'TableDef' = user_table_661()
            t_14955: 'SafeIdentifier' = csid_660('name')
            cs_979: 'Changeset' = changeset(t_14954, params_978).cast((t_14955,)).validate_length(csid_660('name'), 2, 10)
            t_14961: 'bool42' = not cs_979.is_valid
            def fn_14951() -> 'str34':
                return 'should be invalid'
            test_39.assert_(t_14961, fn_14951)
        finally:
            test_39.soft_fail_to_hard()
class TestCase61(TestCase53):
    def test___validateIntPassesForValidInteger__2128(self) -> None:
        'validateInt passes for valid integer'
        test_40: Test = Test()
        try:
            params_981: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', '30'),))
            t_14943: 'TableDef' = user_table_661()
            t_14944: 'SafeIdentifier' = csid_660('age')
            cs_982: 'Changeset' = changeset(t_14943, params_981).cast((t_14944,)).validate_int(csid_660('age'))
            t_14948: 'bool42' = cs_982.is_valid
            def fn_14940() -> 'str34':
                return 'should be valid'
            test_40.assert_(t_14948, fn_14940)
        finally:
            test_40.soft_fail_to_hard()
class TestCase62(TestCase53):
    def test___validateIntFailsForNonInteger__2129(self) -> None:
        'validateInt fails for non-integer'
        test_41: Test = Test()
        try:
            params_984: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', 'not-a-number'),))
            t_14931: 'TableDef' = user_table_661()
            t_14932: 'SafeIdentifier' = csid_660('age')
            cs_985: 'Changeset' = changeset(t_14931, params_984).cast((t_14932,)).validate_int(csid_660('age'))
            t_14938: 'bool42' = not cs_985.is_valid
            def fn_14928() -> 'str34':
                return 'should be invalid'
            test_41.assert_(t_14938, fn_14928)
        finally:
            test_41.soft_fail_to_hard()
class TestCase63(TestCase53):
    def test___validateFloatPassesForValidFloat__2130(self) -> None:
        'validateFloat passes for valid float'
        test_42: Test = Test()
        try:
            params_987: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('score', '9.5'),))
            t_14920: 'TableDef' = user_table_661()
            t_14921: 'SafeIdentifier' = csid_660('score')
            cs_988: 'Changeset' = changeset(t_14920, params_987).cast((t_14921,)).validate_float(csid_660('score'))
            t_14925: 'bool42' = cs_988.is_valid
            def fn_14917() -> 'str34':
                return 'should be valid'
            test_42.assert_(t_14925, fn_14917)
        finally:
            test_42.soft_fail_to_hard()
class TestCase64(TestCase53):
    def test___validateInt64_passesForValid64_bitInteger__2131(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_43: Test = Test()
        try:
            params_990: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', '9999999999'),))
            t_14909: 'TableDef' = user_table_661()
            t_14910: 'SafeIdentifier' = csid_660('age')
            cs_991: 'Changeset' = changeset(t_14909, params_990).cast((t_14910,)).validate_int64(csid_660('age'))
            t_14914: 'bool42' = cs_991.is_valid
            def fn_14906() -> 'str34':
                return 'should be valid'
            test_43.assert_(t_14914, fn_14906)
        finally:
            test_43.soft_fail_to_hard()
class TestCase65(TestCase53):
    def test___validateInt64_failsForNonInteger__2132(self) -> None:
        'validateInt64 fails for non-integer'
        test_44: Test = Test()
        try:
            params_993: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', 'not-a-number'),))
            t_14897: 'TableDef' = user_table_661()
            t_14898: 'SafeIdentifier' = csid_660('age')
            cs_994: 'Changeset' = changeset(t_14897, params_993).cast((t_14898,)).validate_int64(csid_660('age'))
            t_14904: 'bool42' = not cs_994.is_valid
            def fn_14894() -> 'str34':
                return 'should be invalid'
            test_44.assert_(t_14904, fn_14894)
        finally:
            test_44.soft_fail_to_hard()
class TestCase66(TestCase53):
    def test___validateBoolAcceptsTrue1_yesOn__2133(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_45: Test = Test()
        try:
            def fn_14891(v_996: 'str34') -> 'None':
                params_997: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('active', v_996),))
                t_14883: 'TableDef' = user_table_661()
                t_14884: 'SafeIdentifier' = csid_660('active')
                cs_998: 'Changeset' = changeset(t_14883, params_997).cast((t_14884,)).validate_bool(csid_660('active'))
                t_14888: 'bool42' = cs_998.is_valid
                def fn_14880() -> 'str34':
                    return str_cat_15572('should accept: ', v_996)
                test_45.assert_(t_14888, fn_14880)
            list_for_each_15564(('true', '1', 'yes', 'on'), fn_14891)
        finally:
            test_45.soft_fail_to_hard()
class TestCase67(TestCase53):
    def test___validateBoolAcceptsFalse0_noOff__2134(self) -> None:
        'validateBool accepts false/0/no/off'
        test_46: Test = Test()
        try:
            def fn_14877(v_1000: 'str34') -> 'None':
                params_1001: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('active', v_1000),))
                t_14869: 'TableDef' = user_table_661()
                t_14870: 'SafeIdentifier' = csid_660('active')
                cs_1002: 'Changeset' = changeset(t_14869, params_1001).cast((t_14870,)).validate_bool(csid_660('active'))
                t_14874: 'bool42' = cs_1002.is_valid
                def fn_14866() -> 'str34':
                    return str_cat_15572('should accept: ', v_1000)
                test_46.assert_(t_14874, fn_14866)
            list_for_each_15564(('false', '0', 'no', 'off'), fn_14877)
        finally:
            test_46.soft_fail_to_hard()
class TestCase68(TestCase53):
    def test___validateBoolRejectsAmbiguousValues__2135(self) -> None:
        'validateBool rejects ambiguous values'
        test_47: Test = Test()
        try:
            def fn_14863(v_1004: 'str34') -> 'None':
                params_1005: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('active', v_1004),))
                t_14854: 'TableDef' = user_table_661()
                t_14855: 'SafeIdentifier' = csid_660('active')
                cs_1006: 'Changeset' = changeset(t_14854, params_1005).cast((t_14855,)).validate_bool(csid_660('active'))
                t_14861: 'bool42' = not cs_1006.is_valid
                def fn_14851() -> 'str34':
                    return str_cat_15572('should reject ambiguous: ', v_1004)
                test_47.assert_(t_14861, fn_14851)
            list_for_each_15564(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_14863)
        finally:
            test_47.soft_fail_to_hard()
class TestCase69(TestCase53):
    def test___toInsertSqlEscapesBobbyTables__2136(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_48: Test = Test()
        try:
            params_1008: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', "Robert'); DROP TABLE users;--"), pair_15603('email', 'bobby@evil.com')))
            t_14839: 'TableDef' = user_table_661()
            t_14840: 'SafeIdentifier' = csid_660('name')
            t_14841: 'SafeIdentifier' = csid_660('email')
            cs_1009: 'Changeset' = changeset(t_14839, params_1008).cast((t_14840, t_14841)).validate_required((csid_660('name'), csid_660('email')))
            t_8155: 'SqlFragment'
            t_8155 = cs_1009.to_insert_sql()
            sql_frag_1010: 'SqlFragment' = t_8155
            s_1011: 'str34' = sql_frag_1010.to_string()
            t_14848: 'bool42' = s_1011.find("''") >= 0
            def fn_14835() -> 'str34':
                return str_cat_15572('single quote must be doubled: ', s_1011)
            test_48.assert_(t_14848, fn_14835)
        finally:
            test_48.soft_fail_to_hard()
class TestCase70(TestCase53):
    def test___toInsertSqlProducesCorrectSqlForStringField__2137(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_49: Test = Test()
        try:
            params_1013: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'), pair_15603('email', 'a@example.com')))
            t_14819: 'TableDef' = user_table_661()
            t_14820: 'SafeIdentifier' = csid_660('name')
            t_14821: 'SafeIdentifier' = csid_660('email')
            cs_1014: 'Changeset' = changeset(t_14819, params_1013).cast((t_14820, t_14821)).validate_required((csid_660('name'), csid_660('email')))
            t_8134: 'SqlFragment'
            t_8134 = cs_1014.to_insert_sql()
            sql_frag_1015: 'SqlFragment' = t_8134
            s_1016: 'str34' = sql_frag_1015.to_string()
            t_14828: 'bool42' = s_1016.find('INSERT INTO users') >= 0
            def fn_14815() -> 'str34':
                return str_cat_15572('has INSERT INTO: ', s_1016)
            test_49.assert_(t_14828, fn_14815)
            t_14832: 'bool42' = s_1016.find("'Alice'") >= 0
            def fn_14814() -> 'str34':
                return str_cat_15572('has quoted name: ', s_1016)
            test_49.assert_(t_14832, fn_14814)
        finally:
            test_49.soft_fail_to_hard()
class TestCase71(TestCase53):
    def test___toInsertSqlProducesCorrectSqlForIntField__2138(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_50: Test = Test()
        try:
            params_1018: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Bob'), pair_15603('email', 'b@example.com'), pair_15603('age', '25')))
            t_14801: 'TableDef' = user_table_661()
            t_14802: 'SafeIdentifier' = csid_660('name')
            t_14803: 'SafeIdentifier' = csid_660('email')
            t_14804: 'SafeIdentifier' = csid_660('age')
            cs_1019: 'Changeset' = changeset(t_14801, params_1018).cast((t_14802, t_14803, t_14804)).validate_required((csid_660('name'), csid_660('email')))
            t_8117: 'SqlFragment'
            t_8117 = cs_1019.to_insert_sql()
            sql_frag_1020: 'SqlFragment' = t_8117
            s_1021: 'str34' = sql_frag_1020.to_string()
            t_14811: 'bool42' = s_1021.find('25') >= 0
            def fn_14796() -> 'str34':
                return str_cat_15572('age rendered unquoted: ', s_1021)
            test_50.assert_(t_14811, fn_14796)
        finally:
            test_50.soft_fail_to_hard()
class TestCase72(TestCase53):
    def test___toInsertSqlBubblesOnInvalidChangeset__2139(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_51: Test = Test()
        try:
            params_1023: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
            t_14789: 'TableDef' = user_table_661()
            t_14790: 'SafeIdentifier' = csid_660('name')
            cs_1024: 'Changeset' = changeset(t_14789, params_1023).cast((t_14790,)).validate_required((csid_660('name'),))
            did_bubble_1025: 'bool42'
            try:
                cs_1024.to_insert_sql()
                did_bubble_1025 = False
            except Exception46:
                did_bubble_1025 = True
            def fn_14787() -> 'str34':
                return 'invalid changeset should bubble'
            test_51.assert_(did_bubble_1025, fn_14787)
        finally:
            test_51.soft_fail_to_hard()
class TestCase73(TestCase53):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__2140(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_52: Test = Test()
        try:
            strict_table_1027: 'TableDef' = TableDef(csid_660('posts'), (FieldDef(csid_660('title'), StringField(), False, None, False), FieldDef(csid_660('body'), StringField(), True, None, False)), None)
            params_1028: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('body', 'hello'),))
            t_14780: 'SafeIdentifier' = csid_660('body')
            cs_1029: 'Changeset' = changeset(strict_table_1027, params_1028).cast((t_14780,))
            t_14782: 'bool42' = cs_1029.is_valid
            def fn_14769() -> 'str34':
                return 'changeset should appear valid (no explicit validation run)'
            test_52.assert_(t_14782, fn_14769)
            did_bubble_1030: 'bool42'
            try:
                cs_1029.to_insert_sql()
                did_bubble_1030 = False
            except Exception46:
                did_bubble_1030 = True
            def fn_14768() -> 'str34':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_52.assert_(did_bubble_1030, fn_14768)
        finally:
            test_52.soft_fail_to_hard()
class TestCase74(TestCase53):
    def test___toUpdateSqlProducesCorrectSql__2141(self) -> None:
        'toUpdateSql produces correct SQL'
        test_53: Test = Test()
        try:
            params_1032: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Bob'),))
            t_14759: 'TableDef' = user_table_661()
            t_14760: 'SafeIdentifier' = csid_660('name')
            cs_1033: 'Changeset' = changeset(t_14759, params_1032).cast((t_14760,)).validate_required((csid_660('name'),))
            t_8077: 'SqlFragment'
            t_8077 = cs_1033.to_update_sql(42)
            sql_frag_1034: 'SqlFragment' = t_8077
            s_1035: 'str34' = sql_frag_1034.to_string()
            t_14766: 'bool42' = s_1035 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_14756() -> 'str34':
                return str_cat_15572('got: ', s_1035)
            test_53.assert_(t_14766, fn_14756)
        finally:
            test_53.soft_fail_to_hard()
class TestCase75(TestCase53):
    def test___toUpdateSqlBubblesOnInvalidChangeset__2142(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_54: Test = Test()
        try:
            params_1037: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
            t_14749: 'TableDef' = user_table_661()
            t_14750: 'SafeIdentifier' = csid_660('name')
            cs_1038: 'Changeset' = changeset(t_14749, params_1037).cast((t_14750,)).validate_required((csid_660('name'),))
            did_bubble_1039: 'bool42'
            try:
                cs_1038.to_update_sql(1)
                did_bubble_1039 = False
            except Exception46:
                did_bubble_1039 = True
            def fn_14747() -> 'str34':
                return 'invalid changeset should bubble'
            test_54.assert_(did_bubble_1039, fn_14747)
        finally:
            test_54.soft_fail_to_hard()
class TestCase76(TestCase53):
    def test___putChangeAddsANewField__2143(self) -> None:
        'putChange adds a new field'
        test_55: Test = Test()
        try:
            params_1041: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14733: 'TableDef' = user_table_661()
            t_14734: 'SafeIdentifier' = csid_660('name')
            cs_1042: 'Changeset' = changeset(t_14733, params_1041).cast((t_14734,)).put_change(csid_660('email'), 'alice@example.com')
            t_14739: 'bool42' = mapped_has_15567(cs_1042.changes, 'email')
            def fn_14730() -> 'str34':
                return 'email should be in changes'
            test_55.assert_(t_14739, fn_14730)
            t_14745: 'bool42' = cs_1042.changes.get('email', '') == 'alice@example.com'
            def fn_14729() -> 'str34':
                return 'email value'
            test_55.assert_(t_14745, fn_14729)
        finally:
            test_55.soft_fail_to_hard()
class TestCase77(TestCase53):
    def test___putChangeOverwritesExistingField__2144(self) -> None:
        'putChange overwrites existing field'
        test_56: Test = Test()
        try:
            params_1044: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14719: 'TableDef' = user_table_661()
            t_14720: 'SafeIdentifier' = csid_660('name')
            cs_1045: 'Changeset' = changeset(t_14719, params_1044).cast((t_14720,)).put_change(csid_660('name'), 'Bob')
            t_14727: 'bool42' = cs_1045.changes.get('name', '') == 'Bob'
            def fn_14716() -> 'str34':
                return 'name should be overwritten'
            test_56.assert_(t_14727, fn_14716)
        finally:
            test_56.soft_fail_to_hard()
class TestCase78(TestCase53):
    def test___putChangeValueAppearsInToInsertSql__2145(self) -> None:
        'putChange value appears in toInsertSql'
        test_57: Test = Test()
        try:
            params_1047: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'), pair_15603('email', 'a@example.com')))
            t_14705: 'TableDef' = user_table_661()
            t_14706: 'SafeIdentifier' = csid_660('name')
            t_14707: 'SafeIdentifier' = csid_660('email')
            cs_1048: 'Changeset' = changeset(t_14705, params_1047).cast((t_14706, t_14707)).put_change(csid_660('name'), 'Bob')
            t_8032: 'SqlFragment'
            t_8032 = cs_1048.to_insert_sql()
            t_8033: 'SqlFragment' = t_8032
            s_1049: 'str34' = t_8033.to_string()
            t_14713: 'bool42' = s_1049.find("'Bob'") >= 0
            def fn_14701() -> 'str34':
                return str_cat_15572('should use putChange value: ', s_1049)
            test_57.assert_(t_14713, fn_14701)
        finally:
            test_57.soft_fail_to_hard()
class TestCase79(TestCase53):
    def test___getChangeReturnsValueForExistingField__2146(self) -> None:
        'getChange returns value for existing field'
        test_58: Test = Test()
        try:
            params_1051: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14694: 'TableDef' = user_table_661()
            t_14695: 'SafeIdentifier' = csid_660('name')
            cs_1052: 'Changeset' = changeset(t_14694, params_1051).cast((t_14695,))
            t_8020: 'str34'
            t_8020 = cs_1052.get_change(csid_660('name'))
            val_1053: 'str34' = t_8020
            t_14699: 'bool42' = val_1053 == 'Alice'
            def fn_14691() -> 'str34':
                return 'should return Alice'
            test_58.assert_(t_14699, fn_14691)
        finally:
            test_58.soft_fail_to_hard()
class TestCase80(TestCase53):
    def test___getChangeBubblesOnMissingField__2147(self) -> None:
        'getChange bubbles on missing field'
        test_59: Test = Test()
        try:
            params_1055: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14685: 'TableDef' = user_table_661()
            t_14686: 'SafeIdentifier' = csid_660('name')
            cs_1056: 'Changeset' = changeset(t_14685, params_1055).cast((t_14686,))
            did_bubble_1057: 'bool42'
            try:
                cs_1056.get_change(csid_660('email'))
                did_bubble_1057 = False
            except Exception46:
                did_bubble_1057 = True
            def fn_14682() -> 'str34':
                return 'should bubble for missing field'
            test_59.assert_(did_bubble_1057, fn_14682)
        finally:
            test_59.soft_fail_to_hard()
class TestCase81(TestCase53):
    def test___deleteChangeRemovesField__2148(self) -> None:
        'deleteChange removes field'
        test_60: Test = Test()
        try:
            params_1059: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'), pair_15603('email', 'a@example.com')))
            t_14667: 'TableDef' = user_table_661()
            t_14668: 'SafeIdentifier' = csid_660('name')
            t_14669: 'SafeIdentifier' = csid_660('email')
            cs_1060: 'Changeset' = changeset(t_14667, params_1059).cast((t_14668, t_14669)).delete_change(csid_660('email'))
            t_14676: 'bool42' = not mapped_has_15567(cs_1060.changes, 'email')
            def fn_14663() -> 'str34':
                return 'email should be removed'
            test_60.assert_(t_14676, fn_14663)
            t_14679: 'bool42' = mapped_has_15567(cs_1060.changes, 'name')
            def fn_14662() -> 'str34':
                return 'name should remain'
            test_60.assert_(t_14679, fn_14662)
        finally:
            test_60.soft_fail_to_hard()
class TestCase82(TestCase53):
    def test___deleteChangeOnNonexistentFieldIsNoOp__2149(self) -> None:
        'deleteChange on nonexistent field is no-op'
        test_61: Test = Test()
        try:
            params_1062: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14650: 'TableDef' = user_table_661()
            t_14651: 'SafeIdentifier' = csid_660('name')
            cs_1063: 'Changeset' = changeset(t_14650, params_1062).cast((t_14651,)).delete_change(csid_660('email'))
            t_14656: 'bool42' = mapped_has_15567(cs_1063.changes, 'name')
            def fn_14647() -> 'str34':
                return 'name should still be present'
            test_61.assert_(t_14656, fn_14647)
            t_14659: 'bool42' = cs_1063.is_valid
            def fn_14646() -> 'str34':
                return 'should still be valid'
            test_61.assert_(t_14659, fn_14646)
        finally:
            test_61.soft_fail_to_hard()
class TestCase83(TestCase53):
    def test___validateInclusionPassesWhenValueInList__2150(self) -> None:
        'validateInclusion passes when value in list'
        test_62: Test = Test()
        try:
            params_1065: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'admin'),))
            t_14638: 'TableDef' = user_table_661()
            t_14639: 'SafeIdentifier' = csid_660('name')
            cs_1066: 'Changeset' = changeset(t_14638, params_1065).cast((t_14639,)).validate_inclusion(csid_660('name'), ('admin', 'user', 'guest'))
            t_14643: 'bool42' = cs_1066.is_valid
            def fn_14635() -> 'str34':
                return 'should be valid'
            test_62.assert_(t_14643, fn_14635)
        finally:
            test_62.soft_fail_to_hard()
class TestCase84(TestCase53):
    def test___validateInclusionFailsWhenValueNotInList__2151(self) -> None:
        'validateInclusion fails when value not in list'
        test_63: Test = Test()
        try:
            params_1068: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'hacker'),))
            t_14620: 'TableDef' = user_table_661()
            t_14621: 'SafeIdentifier' = csid_660('name')
            cs_1069: 'Changeset' = changeset(t_14620, params_1068).cast((t_14621,)).validate_inclusion(csid_660('name'), ('admin', 'user', 'guest'))
            t_14627: 'bool42' = not cs_1069.is_valid
            def fn_14617() -> 'str34':
                return 'should be invalid'
            test_63.assert_(t_14627, fn_14617)
            t_14633: 'bool42' = list_get_15578(cs_1069.errors, 0).field == 'name'
            def fn_14616() -> 'str34':
                return 'error on name'
            test_63.assert_(t_14633, fn_14616)
        finally:
            test_63.soft_fail_to_hard()
class TestCase85(TestCase53):
    def test___validateInclusionSkipsWhenFieldNotInChanges__2152(self) -> None:
        'validateInclusion skips when field not in changes'
        test_64: Test = Test()
        try:
            params_1071: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
            t_14608: 'TableDef' = user_table_661()
            t_14609: 'SafeIdentifier' = csid_660('name')
            cs_1072: 'Changeset' = changeset(t_14608, params_1071).cast((t_14609,)).validate_inclusion(csid_660('name'), ('admin', 'user'))
            t_14613: 'bool42' = cs_1072.is_valid
            def fn_14606() -> 'str34':
                return 'should be valid when field absent'
            test_64.assert_(t_14613, fn_14606)
        finally:
            test_64.soft_fail_to_hard()
class TestCase86(TestCase53):
    def test___validateExclusionPassesWhenValueNotInList__2153(self) -> None:
        'validateExclusion passes when value not in list'
        test_65: Test = Test()
        try:
            params_1074: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14598: 'TableDef' = user_table_661()
            t_14599: 'SafeIdentifier' = csid_660('name')
            cs_1075: 'Changeset' = changeset(t_14598, params_1074).cast((t_14599,)).validate_exclusion(csid_660('name'), ('root', 'admin', 'superuser'))
            t_14603: 'bool42' = cs_1075.is_valid
            def fn_14595() -> 'str34':
                return 'should be valid'
            test_65.assert_(t_14603, fn_14595)
        finally:
            test_65.soft_fail_to_hard()
class TestCase87(TestCase53):
    def test___validateExclusionFailsWhenValueInList__2154(self) -> None:
        'validateExclusion fails when value in list'
        test_66: Test = Test()
        try:
            params_1077: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'admin'),))
            t_14580: 'TableDef' = user_table_661()
            t_14581: 'SafeIdentifier' = csid_660('name')
            cs_1078: 'Changeset' = changeset(t_14580, params_1077).cast((t_14581,)).validate_exclusion(csid_660('name'), ('root', 'admin', 'superuser'))
            t_14587: 'bool42' = not cs_1078.is_valid
            def fn_14577() -> 'str34':
                return 'should be invalid'
            test_66.assert_(t_14587, fn_14577)
            t_14593: 'bool42' = list_get_15578(cs_1078.errors, 0).field == 'name'
            def fn_14576() -> 'str34':
                return 'error on name'
            test_66.assert_(t_14593, fn_14576)
        finally:
            test_66.soft_fail_to_hard()
class TestCase88(TestCase53):
    def test___validateExclusionSkipsWhenFieldNotInChanges__2155(self) -> None:
        'validateExclusion skips when field not in changes'
        test_67: Test = Test()
        try:
            params_1080: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
            t_14568: 'TableDef' = user_table_661()
            t_14569: 'SafeIdentifier' = csid_660('name')
            cs_1081: 'Changeset' = changeset(t_14568, params_1080).cast((t_14569,)).validate_exclusion(csid_660('name'), ('root', 'admin'))
            t_14573: 'bool42' = cs_1081.is_valid
            def fn_14566() -> 'str34':
                return 'should be valid when field absent'
            test_67.assert_(t_14573, fn_14566)
        finally:
            test_67.soft_fail_to_hard()
class TestCase89(TestCase53):
    def test___validateNumberGreaterThanPasses__2156(self) -> None:
        'validateNumber greaterThan passes'
        test_68: Test = Test()
        try:
            params_1083: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', '25'),))
            t_14557: 'TableDef' = user_table_661()
            t_14558: 'SafeIdentifier' = csid_660('age')
            cs_1084: 'Changeset' = changeset(t_14557, params_1083).cast((t_14558,)).validate_number(csid_660('age'), NumberValidationOpts(18.0, None, None, None, None))
            t_14563: 'bool42' = cs_1084.is_valid
            def fn_14554() -> 'str34':
                return '25 > 18 should pass'
            test_68.assert_(t_14563, fn_14554)
        finally:
            test_68.soft_fail_to_hard()
class TestCase90(TestCase53):
    def test___validateNumberGreaterThanFails__2157(self) -> None:
        'validateNumber greaterThan fails'
        test_69: Test = Test()
        try:
            params_1086: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', '15'),))
            t_14544: 'TableDef' = user_table_661()
            t_14545: 'SafeIdentifier' = csid_660('age')
            cs_1087: 'Changeset' = changeset(t_14544, params_1086).cast((t_14545,)).validate_number(csid_660('age'), NumberValidationOpts(18.0, None, None, None, None))
            t_14552: 'bool42' = not cs_1087.is_valid
            def fn_14541() -> 'str34':
                return '15 > 18 should fail'
            test_69.assert_(t_14552, fn_14541)
        finally:
            test_69.soft_fail_to_hard()
class TestCase91(TestCase53):
    def test___validateNumberLessThanPasses__2158(self) -> None:
        'validateNumber lessThan passes'
        test_70: Test = Test()
        try:
            params_1089: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('score', '8.5'),))
            t_14532: 'TableDef' = user_table_661()
            t_14533: 'SafeIdentifier' = csid_660('score')
            cs_1090: 'Changeset' = changeset(t_14532, params_1089).cast((t_14533,)).validate_number(csid_660('score'), NumberValidationOpts(None, 10.0, None, None, None))
            t_14538: 'bool42' = cs_1090.is_valid
            def fn_14529() -> 'str34':
                return '8.5 < 10 should pass'
            test_70.assert_(t_14538, fn_14529)
        finally:
            test_70.soft_fail_to_hard()
class TestCase92(TestCase53):
    def test___validateNumberLessThanFails__2159(self) -> None:
        'validateNumber lessThan fails'
        test_71: Test = Test()
        try:
            params_1092: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('score', '12.0'),))
            t_14519: 'TableDef' = user_table_661()
            t_14520: 'SafeIdentifier' = csid_660('score')
            cs_1093: 'Changeset' = changeset(t_14519, params_1092).cast((t_14520,)).validate_number(csid_660('score'), NumberValidationOpts(None, 10.0, None, None, None))
            t_14527: 'bool42' = not cs_1093.is_valid
            def fn_14516() -> 'str34':
                return '12 < 10 should fail'
            test_71.assert_(t_14527, fn_14516)
        finally:
            test_71.soft_fail_to_hard()
class TestCase93(TestCase53):
    def test___validateNumberGreaterThanOrEqualBoundary__2160(self) -> None:
        'validateNumber greaterThanOrEqual boundary'
        test_72: Test = Test()
        try:
            params_1095: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', '18'),))
            t_14507: 'TableDef' = user_table_661()
            t_14508: 'SafeIdentifier' = csid_660('age')
            cs_1096: 'Changeset' = changeset(t_14507, params_1095).cast((t_14508,)).validate_number(csid_660('age'), NumberValidationOpts(None, None, 18.0, None, None))
            t_14513: 'bool42' = cs_1096.is_valid
            def fn_14504() -> 'str34':
                return '18 >= 18 should pass'
            test_72.assert_(t_14513, fn_14504)
        finally:
            test_72.soft_fail_to_hard()
class TestCase94(TestCase53):
    def test___validateNumberCombinedOptions__2161(self) -> None:
        'validateNumber combined options'
        test_73: Test = Test()
        try:
            params_1098: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('score', '5.0'),))
            t_14495: 'TableDef' = user_table_661()
            t_14496: 'SafeIdentifier' = csid_660('score')
            cs_1099: 'Changeset' = changeset(t_14495, params_1098).cast((t_14496,)).validate_number(csid_660('score'), NumberValidationOpts(0.0, 10.0, None, None, None))
            t_14501: 'bool42' = cs_1099.is_valid
            def fn_14492() -> 'str34':
                return '5 > 0 and < 10 should pass'
            test_73.assert_(t_14501, fn_14492)
        finally:
            test_73.soft_fail_to_hard()
class TestCase95(TestCase53):
    def test___validateNumberNonNumericValue__2162(self) -> None:
        'validateNumber non-numeric value'
        test_74: Test = Test()
        try:
            params_1101: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('age', 'abc'),))
            t_14476: 'TableDef' = user_table_661()
            t_14477: 'SafeIdentifier' = csid_660('age')
            cs_1102: 'Changeset' = changeset(t_14476, params_1101).cast((t_14477,)).validate_number(csid_660('age'), NumberValidationOpts(0.0, None, None, None, None))
            t_14484: 'bool42' = not cs_1102.is_valid
            def fn_14473() -> 'str34':
                return 'non-numeric should fail'
            test_74.assert_(t_14484, fn_14473)
            t_14490: 'bool42' = list_get_15578(cs_1102.errors, 0).message == 'must be a number'
            def fn_14472() -> 'str34':
                return 'correct error message'
            test_74.assert_(t_14490, fn_14472)
        finally:
            test_74.soft_fail_to_hard()
class TestCase96(TestCase53):
    def test___validateNumberSkipsWhenFieldNotInChanges__2163(self) -> None:
        'validateNumber skips when field not in changes'
        test_75: Test = Test()
        try:
            params_1104: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
            t_14463: 'TableDef' = user_table_661()
            t_14464: 'SafeIdentifier' = csid_660('age')
            cs_1105: 'Changeset' = changeset(t_14463, params_1104).cast((t_14464,)).validate_number(csid_660('age'), NumberValidationOpts(0.0, None, None, None, None))
            t_14469: 'bool42' = cs_1105.is_valid
            def fn_14461() -> 'str34':
                return 'should be valid when field absent'
            test_75.assert_(t_14469, fn_14461)
        finally:
            test_75.soft_fail_to_hard()
class TestCase97(TestCase53):
    def test___validateAcceptancePassesForTrueValues__2164(self) -> None:
        'validateAcceptance passes for true values'
        test_76: Test = Test()
        try:
            def fn_14458(v_1107: 'str34') -> 'None':
                params_1108: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('active', v_1107),))
                t_14450: 'TableDef' = user_table_661()
                t_14451: 'SafeIdentifier' = csid_660('active')
                cs_1109: 'Changeset' = changeset(t_14450, params_1108).cast((t_14451,)).validate_acceptance(csid_660('active'))
                t_14455: 'bool42' = cs_1109.is_valid
                def fn_14447() -> 'str34':
                    return str_cat_15572('should accept: ', v_1107)
                test_76.assert_(t_14455, fn_14447)
            list_for_each_15564(('true', '1', 'yes', 'on'), fn_14458)
        finally:
            test_76.soft_fail_to_hard()
class TestCase98(TestCase53):
    def test___validateAcceptanceFailsForNonTrueValues__2165(self) -> None:
        'validateAcceptance fails for non-true values'
        test_77: Test = Test()
        try:
            params_1111: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('active', 'false'),))
            t_14432: 'TableDef' = user_table_661()
            t_14433: 'SafeIdentifier' = csid_660('active')
            cs_1112: 'Changeset' = changeset(t_14432, params_1111).cast((t_14433,)).validate_acceptance(csid_660('active'))
            t_14439: 'bool42' = not cs_1112.is_valid
            def fn_14429() -> 'str34':
                return 'false should not be accepted'
            test_77.assert_(t_14439, fn_14429)
            t_14445: 'bool42' = list_get_15578(cs_1112.errors, 0).message == 'must be accepted'
            def fn_14428() -> 'str34':
                return 'correct message'
            test_77.assert_(t_14445, fn_14428)
        finally:
            test_77.soft_fail_to_hard()
class TestCase99(TestCase53):
    def test___validateConfirmationPassesWhenFieldsMatch__2166(self) -> None:
        'validateConfirmation passes when fields match'
        test_78: Test = Test()
        try:
            tbl_1114: 'TableDef' = TableDef(csid_660('users'), (FieldDef(csid_660('password'), StringField(), False, None, False), FieldDef(csid_660('password_confirmation'), StringField(), True, None, False)), None)
            params_1115: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('password', 'secret123'), pair_15603('password_confirmation', 'secret123')))
            t_14419: 'SafeIdentifier' = csid_660('password')
            t_14420: 'SafeIdentifier' = csid_660('password_confirmation')
            cs_1116: 'Changeset' = changeset(tbl_1114, params_1115).cast((t_14419, t_14420)).validate_confirmation(csid_660('password'), csid_660('password_confirmation'))
            t_14425: 'bool42' = cs_1116.is_valid
            def fn_14407() -> 'str34':
                return 'matching fields should pass'
            test_78.assert_(t_14425, fn_14407)
        finally:
            test_78.soft_fail_to_hard()
class TestCase100(TestCase53):
    def test___validateConfirmationFailsWhenFieldsDiffer__2167(self) -> None:
        'validateConfirmation fails when fields differ'
        test_79: Test = Test()
        try:
            tbl_1118: 'TableDef' = TableDef(csid_660('users'), (FieldDef(csid_660('password'), StringField(), False, None, False), FieldDef(csid_660('password_confirmation'), StringField(), True, None, False)), None)
            params_1119: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('password', 'secret123'), pair_15603('password_confirmation', 'wrong456')))
            t_14391: 'SafeIdentifier' = csid_660('password')
            t_14392: 'SafeIdentifier' = csid_660('password_confirmation')
            cs_1120: 'Changeset' = changeset(tbl_1118, params_1119).cast((t_14391, t_14392)).validate_confirmation(csid_660('password'), csid_660('password_confirmation'))
            t_14399: 'bool42' = not cs_1120.is_valid
            def fn_14379() -> 'str34':
                return 'mismatched fields should fail'
            test_79.assert_(t_14399, fn_14379)
            t_14405: 'bool42' = list_get_15578(cs_1120.errors, 0).field == 'password_confirmation'
            def fn_14378() -> 'str34':
                return 'error on confirmation field'
            test_79.assert_(t_14405, fn_14378)
        finally:
            test_79.soft_fail_to_hard()
class TestCase101(TestCase53):
    def test___validateConfirmationFailsWhenConfirmationMissing__2168(self) -> None:
        'validateConfirmation fails when confirmation missing'
        test_80: Test = Test()
        try:
            tbl_1122: 'TableDef' = TableDef(csid_660('users'), (FieldDef(csid_660('password'), StringField(), False, None, False), FieldDef(csid_660('password_confirmation'), StringField(), True, None, False)), None)
            params_1123: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('password', 'secret123'),))
            t_14369: 'SafeIdentifier' = csid_660('password')
            cs_1124: 'Changeset' = changeset(tbl_1122, params_1123).cast((t_14369,)).validate_confirmation(csid_660('password'), csid_660('password_confirmation'))
            t_14376: 'bool42' = not cs_1124.is_valid
            def fn_14358() -> 'str34':
                return 'missing confirmation should fail'
            test_80.assert_(t_14376, fn_14358)
        finally:
            test_80.soft_fail_to_hard()
class TestCase102(TestCase53):
    def test___validateContainsPassesWhenSubstringFound__2169(self) -> None:
        'validateContains passes when substring found'
        test_81: Test = Test()
        try:
            params_1126: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('email', 'alice@example.com'),))
            t_14350: 'TableDef' = user_table_661()
            t_14351: 'SafeIdentifier' = csid_660('email')
            cs_1127: 'Changeset' = changeset(t_14350, params_1126).cast((t_14351,)).validate_contains(csid_660('email'), '@')
            t_14355: 'bool42' = cs_1127.is_valid
            def fn_14347() -> 'str34':
                return 'should pass when @ present'
            test_81.assert_(t_14355, fn_14347)
        finally:
            test_81.soft_fail_to_hard()
class TestCase103(TestCase53):
    def test___validateContainsFailsWhenSubstringNotFound__2170(self) -> None:
        'validateContains fails when substring not found'
        test_82: Test = Test()
        try:
            params_1129: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('email', 'alice-example.com'),))
            t_14338: 'TableDef' = user_table_661()
            t_14339: 'SafeIdentifier' = csid_660('email')
            cs_1130: 'Changeset' = changeset(t_14338, params_1129).cast((t_14339,)).validate_contains(csid_660('email'), '@')
            t_14345: 'bool42' = not cs_1130.is_valid
            def fn_14335() -> 'str34':
                return 'should fail when @ absent'
            test_82.assert_(t_14345, fn_14335)
        finally:
            test_82.soft_fail_to_hard()
class TestCase104(TestCase53):
    def test___validateContainsSkipsWhenFieldNotInChanges__2171(self) -> None:
        'validateContains skips when field not in changes'
        test_83: Test = Test()
        try:
            params_1132: 'MappingProxyType41[str34, str34]' = map_constructor_15602(())
            t_14327: 'TableDef' = user_table_661()
            t_14328: 'SafeIdentifier' = csid_660('email')
            cs_1133: 'Changeset' = changeset(t_14327, params_1132).cast((t_14328,)).validate_contains(csid_660('email'), '@')
            t_14332: 'bool42' = cs_1133.is_valid
            def fn_14325() -> 'str34':
                return 'should be valid when field absent'
            test_83.assert_(t_14332, fn_14325)
        finally:
            test_83.soft_fail_to_hard()
class TestCase105(TestCase53):
    def test___validateStartsWithPasses__2172(self) -> None:
        'validateStartsWith passes'
        test_84: Test = Test()
        try:
            params_1135: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Dr. Smith'),))
            t_14317: 'TableDef' = user_table_661()
            t_14318: 'SafeIdentifier' = csid_660('name')
            cs_1136: 'Changeset' = changeset(t_14317, params_1135).cast((t_14318,)).validate_starts_with(csid_660('name'), 'Dr.')
            t_14322: 'bool42' = cs_1136.is_valid
            def fn_14314() -> 'str34':
                return 'should pass for Dr. prefix'
            test_84.assert_(t_14322, fn_14314)
        finally:
            test_84.soft_fail_to_hard()
class TestCase106(TestCase53):
    def test___validateStartsWithFails__2173(self) -> None:
        'validateStartsWith fails'
        test_85: Test = Test()
        try:
            params_1138: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Mr. Smith'),))
            t_14305: 'TableDef' = user_table_661()
            t_14306: 'SafeIdentifier' = csid_660('name')
            cs_1139: 'Changeset' = changeset(t_14305, params_1138).cast((t_14306,)).validate_starts_with(csid_660('name'), 'Dr.')
            t_14312: 'bool42' = not cs_1139.is_valid
            def fn_14302() -> 'str34':
                return 'should fail for Mr. prefix'
            test_85.assert_(t_14312, fn_14302)
        finally:
            test_85.soft_fail_to_hard()
class TestCase107(TestCase53):
    def test___validateEndsWithPasses__2174(self) -> None:
        'validateEndsWith passes'
        test_86: Test = Test()
        try:
            params_1141: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('email', 'alice@example.com'),))
            t_14294: 'TableDef' = user_table_661()
            t_14295: 'SafeIdentifier' = csid_660('email')
            cs_1142: 'Changeset' = changeset(t_14294, params_1141).cast((t_14295,)).validate_ends_with(csid_660('email'), '.com')
            t_14299: 'bool42' = cs_1142.is_valid
            def fn_14291() -> 'str34':
                return 'should pass for .com suffix'
            test_86.assert_(t_14299, fn_14291)
        finally:
            test_86.soft_fail_to_hard()
class TestCase108(TestCase53):
    def test___validateEndsWithFails__2175(self) -> None:
        'validateEndsWith fails'
        test_87: Test = Test()
        try:
            params_1144: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('email', 'alice@example.org'),))
            t_14282: 'TableDef' = user_table_661()
            t_14283: 'SafeIdentifier' = csid_660('email')
            cs_1145: 'Changeset' = changeset(t_14282, params_1144).cast((t_14283,)).validate_ends_with(csid_660('email'), '.com')
            t_14289: 'bool42' = not cs_1145.is_valid
            def fn_14279() -> 'str34':
                return 'should fail for .org when expecting .com'
            test_87.assert_(t_14289, fn_14279)
        finally:
            test_87.soft_fail_to_hard()
class TestCase109(TestCase53):
    def test___validateEndsWithHandlesRepeatedSuffixCorrectly__2176(self) -> None:
        'validateEndsWith handles repeated suffix correctly'
        test_88: Test = Test()
        try:
            params_1147: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'abcabc'),))
            t_14271: 'TableDef' = user_table_661()
            t_14272: 'SafeIdentifier' = csid_660('name')
            cs_1148: 'Changeset' = changeset(t_14271, params_1147).cast((t_14272,)).validate_ends_with(csid_660('name'), 'abc')
            t_14276: 'bool42' = cs_1148.is_valid
            def fn_14268() -> 'str34':
                return 'abcabc should end with abc'
            test_88.assert_(t_14276, fn_14268)
        finally:
            test_88.soft_fail_to_hard()
class TestCase110(TestCase53):
    def test___toInsertSqlUsesDefaultValueWhenFieldNotInChanges__2177(self) -> None:
        'toInsertSql uses default value when field not in changes'
        test_89: Test = Test()
        try:
            tbl_1150: 'TableDef' = TableDef(csid_660('posts'), (FieldDef(csid_660('title'), StringField(), False, None, False), FieldDef(csid_660('status'), StringField(), False, SqlDefault(), False)), None)
            params_1151: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('title', 'Hello'),))
            t_14252: 'SafeIdentifier' = csid_660('title')
            cs_1152: 'Changeset' = changeset(tbl_1150, params_1151).cast((t_14252,))
            t_7668: 'SqlFragment'
            t_7668 = cs_1152.to_insert_sql()
            t_7669: 'SqlFragment' = t_7668
            s_1153: 'str34' = t_7669.to_string()
            t_14256: 'bool42' = s_1153.find('INSERT INTO posts') >= 0
            def fn_14240() -> 'str34':
                return str_cat_15572('has INSERT INTO: ', s_1153)
            test_89.assert_(t_14256, fn_14240)
            t_14260: 'bool42' = s_1153.find("'Hello'") >= 0
            def fn_14239() -> 'str34':
                return str_cat_15572('has title value: ', s_1153)
            test_89.assert_(t_14260, fn_14239)
            t_14264: 'bool42' = s_1153.find('DEFAULT') >= 0
            def fn_14238() -> 'str34':
                return str_cat_15572('status should use DEFAULT: ', s_1153)
            test_89.assert_(t_14264, fn_14238)
        finally:
            test_89.soft_fail_to_hard()
class TestCase111(TestCase53):
    def test___toInsertSqlChangeOverridesDefaultValue__2178(self) -> None:
        'toInsertSql change overrides default value'
        test_90: Test = Test()
        try:
            tbl_1155: 'TableDef' = TableDef(csid_660('posts'), (FieldDef(csid_660('title'), StringField(), False, None, False), FieldDef(csid_660('status'), StringField(), False, SqlDefault(), False)), None)
            params_1156: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('title', 'Hello'), pair_15603('status', 'published')))
            t_14230: 'SafeIdentifier' = csid_660('title')
            t_14231: 'SafeIdentifier' = csid_660('status')
            cs_1157: 'Changeset' = changeset(tbl_1155, params_1156).cast((t_14230, t_14231))
            t_7648: 'SqlFragment'
            t_7648 = cs_1157.to_insert_sql()
            t_7649: 'SqlFragment' = t_7648
            s_1158: 'str34' = t_7649.to_string()
            t_14235: 'bool42' = s_1158.find("'published'") >= 0
            def fn_14217() -> 'str34':
                return str_cat_15572('should use provided value: ', s_1158)
            test_90.assert_(t_14235, fn_14217)
        finally:
            test_90.soft_fail_to_hard()
class TestCase112(TestCase53):
    def test___toInsertSqlWithTimestampsUsesDefault__2179(self) -> None:
        'toInsertSql with timestamps uses DEFAULT'
        test_91: Test = Test()
        try:
            t_7595: 'Sequence38[FieldDef]'
            t_7595 = timestamps()
            ts_1160: 'Sequence38[FieldDef]' = t_7595
            fields_1161: 'MutableSequence45[FieldDef]' = list_15566()
            fields_1161.append(FieldDef(csid_660('title'), StringField(), False, None, False))
            def fn_14183(t_1162: 'FieldDef') -> 'None':
                fields_1161.append(t_1162)
            list_for_each_15564(ts_1160, fn_14183)
            tbl_1163: 'TableDef' = TableDef(csid_660('articles'), tuple_15569(fields_1161), None)
            params_1164: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('title', 'News'),))
            t_14196: 'SafeIdentifier' = csid_660('title')
            cs_1165: 'Changeset' = changeset(tbl_1163, params_1164).cast((t_14196,))
            t_7610: 'SqlFragment'
            t_7610 = cs_1165.to_insert_sql()
            t_7611: 'SqlFragment' = t_7610
            s_1166: 'str34' = t_7611.to_string()
            t_14200: 'bool42' = s_1166.find('inserted_at') >= 0
            def fn_14182() -> 'str34':
                return str_cat_15572('should include inserted_at: ', s_1166)
            test_91.assert_(t_14200, fn_14182)
            t_14204: 'bool42' = s_1166.find('updated_at') >= 0
            def fn_14181() -> 'str34':
                return str_cat_15572('should include updated_at: ', s_1166)
            test_91.assert_(t_14204, fn_14181)
            t_14208: 'bool42' = s_1166.find('DEFAULT') >= 0
            def fn_14180() -> 'str34':
                return str_cat_15572('timestamps should use DEFAULT: ', s_1166)
            test_91.assert_(t_14208, fn_14180)
        finally:
            test_91.soft_fail_to_hard()
class TestCase113(TestCase53):
    def test___toInsertSqlSkipsVirtualFields__2180(self) -> None:
        'toInsertSql skips virtual fields'
        test_92: Test = Test()
        try:
            tbl_1168: 'TableDef' = TableDef(csid_660('users'), (FieldDef(csid_660('name'), StringField(), False, None, False), FieldDef(csid_660('full_name'), StringField(), True, None, True)), None)
            params_1169: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'), pair_15603('full_name', 'Alice Smith')))
            t_14166: 'SafeIdentifier' = csid_660('name')
            t_14167: 'SafeIdentifier' = csid_660('full_name')
            cs_1170: 'Changeset' = changeset(tbl_1168, params_1169).cast((t_14166, t_14167))
            t_7584: 'SqlFragment'
            t_7584 = cs_1170.to_insert_sql()
            t_7585: 'SqlFragment' = t_7584
            s_1171: 'str34' = t_7585.to_string()
            t_14171: 'bool42' = s_1171.find("'Alice'") >= 0
            def fn_14154() -> 'str34':
                return str_cat_15572('name should be included: ', s_1171)
            test_92.assert_(t_14171, fn_14154)
            t_14177: 'bool42' = not s_1171.find('full_name') >= 0
            def fn_14153() -> 'str34':
                return str_cat_15572('virtual field should be excluded: ', s_1171)
            test_92.assert_(t_14177, fn_14153)
        finally:
            test_92.soft_fail_to_hard()
class TestCase114(TestCase53):
    def test___toInsertSqlAllowsMissingNonNullableVirtualField__2181(self) -> None:
        'toInsertSql allows missing non-nullable virtual field'
        test_93: Test = Test()
        try:
            tbl_1173: 'TableDef' = TableDef(csid_660('users'), (FieldDef(csid_660('name'), StringField(), False, None, False), FieldDef(csid_660('computed'), StringField(), False, None, True)), None)
            params_1174: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Alice'),))
            t_14146: 'SafeIdentifier' = csid_660('name')
            cs_1175: 'Changeset' = changeset(tbl_1173, params_1174).cast((t_14146,))
            t_7563: 'SqlFragment'
            t_7563 = cs_1175.to_insert_sql()
            t_7564: 'SqlFragment' = t_7563
            s_1176: 'str34' = t_7564.to_string()
            t_14150: 'bool42' = s_1176.find("'Alice'") >= 0
            def fn_14135() -> 'str34':
                return str_cat_15572('should succeed: ', s_1176)
            test_93.assert_(t_14150, fn_14135)
        finally:
            test_93.soft_fail_to_hard()
class TestCase115(TestCase53):
    def test___toUpdateSqlSkipsVirtualFields__2182(self) -> None:
        'toUpdateSql skips virtual fields'
        test_94: Test = Test()
        try:
            tbl_1178: 'TableDef' = TableDef(csid_660('users'), (FieldDef(csid_660('name'), StringField(), False, None, False), FieldDef(csid_660('display'), StringField(), True, None, True)), None)
            params_1179: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('name', 'Bob'), pair_15603('display', 'Bobby')))
            t_14122: 'SafeIdentifier' = csid_660('name')
            t_14123: 'SafeIdentifier' = csid_660('display')
            cs_1180: 'Changeset' = changeset(tbl_1178, params_1179).cast((t_14122, t_14123))
            t_7540: 'SqlFragment'
            t_7540 = cs_1180.to_update_sql(1)
            t_7541: 'SqlFragment' = t_7540
            s_1181: 'str34' = t_7541.to_string()
            t_14127: 'bool42' = s_1181.find("name = 'Bob'") >= 0
            def fn_14110() -> 'str34':
                return str_cat_15572('name should be in SET: ', s_1181)
            test_94.assert_(t_14127, fn_14110)
            t_14133: 'bool42' = not s_1181.find('display') >= 0
            def fn_14109() -> 'str34':
                return str_cat_15572('virtual field excluded from UPDATE: ', s_1181)
            test_94.assert_(t_14133, fn_14109)
        finally:
            test_94.soft_fail_to_hard()
class TestCase116(TestCase53):
    def test___toUpdateSqlUsesCustomPrimaryKey__2183(self) -> None:
        'toUpdateSql uses custom primary key'
        test_95: Test = Test()
        try:
            tbl_1183: 'TableDef' = TableDef(csid_660('posts'), (FieldDef(csid_660('title'), StringField(), False, None, False),), csid_660('post_id'))
            params_1184: 'MappingProxyType41[str34, str34]' = map_constructor_15602((pair_15603('title', 'Updated'),))
            t_14103: 'SafeIdentifier' = csid_660('title')
            cs_1185: 'Changeset' = changeset(tbl_1183, params_1184).cast((t_14103,))
            t_7522: 'SqlFragment'
            t_7522 = cs_1185.to_update_sql(99)
            t_7523: 'SqlFragment' = t_7522
            s_1186: 'str34' = t_7523.to_string()
            t_14107: 'bool42' = s_1186 == "UPDATE posts SET title = 'Updated' WHERE post_id = 99"
            def fn_14093() -> 'str34':
                return str_cat_15572('got: ', s_1186)
            test_95.assert_(t_14107, fn_14093)
        finally:
            test_95.soft_fail_to_hard()
class TestCase117(TestCase53):
    def test___deleteSqlUsesCustomPrimaryKey__2184(self) -> None:
        'deleteSql uses custom primary key'
        test_96: Test = Test()
        try:
            tbl_1188: 'TableDef' = TableDef(csid_660('posts'), (FieldDef(csid_660('title'), StringField(), False, None, False),), csid_660('post_id'))
            s_1189: 'str34' = delete_sql(tbl_1188, 42).to_string()
            t_14080: 'bool42' = s_1189 == 'DELETE FROM posts WHERE post_id = 42'
            def fn_14069() -> 'str34':
                return str_cat_15572('got: ', s_1189)
            test_96.assert_(t_14080, fn_14069)
        finally:
            test_96.soft_fail_to_hard()
class TestCase118(TestCase53):
    def test___deleteSqlUsesDefaultIdWhenPrimaryKeyNull__2185(self) -> None:
        'deleteSql uses default id when primaryKey null'
        test_97: Test = Test()
        try:
            tbl_1191: 'TableDef' = TableDef(csid_660('users'), (FieldDef(csid_660('name'), StringField(), False, None, False),), None)
            s_1192: 'str34' = delete_sql(tbl_1191, 7).to_string()
            t_14067: 'bool42' = s_1192 == 'DELETE FROM users WHERE id = 7'
            def fn_14058() -> 'str34':
                return str_cat_15572('got: ', s_1192)
            test_97.assert_(t_14067, fn_14058)
        finally:
            test_97.soft_fail_to_hard()
def sid_662(name_1537: 'str34') -> 'SafeIdentifier':
    t_6965: 'SafeIdentifier'
    t_6965 = safe_identifier(name_1537)
    return t_6965
class TestCase119(TestCase53):
    def test___bareFromProducesSelect__2267(self) -> None:
        'bare from produces SELECT *'
        test_98: Test = Test()
        try:
            q_1540: 'Query' = from_(sid_662('users'))
            t_13551: 'bool42' = q_1540.to_sql().to_string() == 'SELECT * FROM users'
            def fn_13546() -> 'str34':
                return 'bare query'
            test_98.assert_(t_13551, fn_13546)
        finally:
            test_98.soft_fail_to_hard()
class TestCase120(TestCase53):
    def test___selectRestrictsColumns__2268(self) -> None:
        'select restricts columns'
        test_99: Test = Test()
        try:
            t_13537: 'SafeIdentifier' = sid_662('users')
            t_13538: 'SafeIdentifier' = sid_662('id')
            t_13539: 'SafeIdentifier' = sid_662('name')
            q_1542: 'Query' = from_(t_13537).select((t_13538, t_13539))
            t_13544: 'bool42' = q_1542.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_13536() -> 'str34':
                return 'select columns'
            test_99.assert_(t_13544, fn_13536)
        finally:
            test_99.soft_fail_to_hard()
class TestCase121(TestCase53):
    def test___whereAddsConditionWithIntValue__2269(self) -> None:
        'where adds condition with int value'
        test_100: Test = Test()
        try:
            t_13525: 'SafeIdentifier' = sid_662('users')
            t_13526: 'SqlBuilder' = SqlBuilder()
            t_13526.append_safe('age > ')
            t_13526.append_int32(18)
            t_13529: 'SqlFragment' = t_13526.accumulated
            q_1544: 'Query' = from_(t_13525).where(t_13529)
            t_13534: 'bool42' = q_1544.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_13524() -> 'str34':
                return 'where int'
            test_100.assert_(t_13534, fn_13524)
        finally:
            test_100.soft_fail_to_hard()
class TestCase122(TestCase53):
    def test___whereAddsConditionWithBoolValue__2271(self) -> None:
        'where adds condition with bool value'
        test_101: Test = Test()
        try:
            t_13513: 'SafeIdentifier' = sid_662('users')
            t_13514: 'SqlBuilder' = SqlBuilder()
            t_13514.append_safe('active = ')
            t_13514.append_boolean(True)
            t_13517: 'SqlFragment' = t_13514.accumulated
            q_1546: 'Query' = from_(t_13513).where(t_13517)
            t_13522: 'bool42' = q_1546.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_13512() -> 'str34':
                return 'where bool'
            test_101.assert_(t_13522, fn_13512)
        finally:
            test_101.soft_fail_to_hard()
class TestCase123(TestCase53):
    def test___chainedWhereUsesAnd__2273(self) -> None:
        'chained where uses AND'
        test_102: Test = Test()
        try:
            t_13496: 'SafeIdentifier' = sid_662('users')
            t_13497: 'SqlBuilder' = SqlBuilder()
            t_13497.append_safe('age > ')
            t_13497.append_int32(18)
            t_13500: 'SqlFragment' = t_13497.accumulated
            t_13501: 'Query' = from_(t_13496).where(t_13500)
            t_13502: 'SqlBuilder' = SqlBuilder()
            t_13502.append_safe('active = ')
            t_13502.append_boolean(True)
            q_1548: 'Query' = t_13501.where(t_13502.accumulated)
            t_13510: 'bool42' = q_1548.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_13495() -> 'str34':
                return 'chained where'
            test_102.assert_(t_13510, fn_13495)
        finally:
            test_102.soft_fail_to_hard()
class TestCase124(TestCase53):
    def test___orderByAsc__2276(self) -> None:
        'orderBy ASC'
        test_103: Test = Test()
        try:
            t_13487: 'SafeIdentifier' = sid_662('users')
            t_13488: 'SafeIdentifier' = sid_662('name')
            q_1550: 'Query' = from_(t_13487).order_by(t_13488, True)
            t_13493: 'bool42' = q_1550.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_13486() -> 'str34':
                return 'order asc'
            test_103.assert_(t_13493, fn_13486)
        finally:
            test_103.soft_fail_to_hard()
class TestCase125(TestCase53):
    def test___orderByDesc__2277(self) -> None:
        'orderBy DESC'
        test_104: Test = Test()
        try:
            t_13478: 'SafeIdentifier' = sid_662('users')
            t_13479: 'SafeIdentifier' = sid_662('created_at')
            q_1552: 'Query' = from_(t_13478).order_by(t_13479, False)
            t_13484: 'bool42' = q_1552.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_13477() -> 'str34':
                return 'order desc'
            test_104.assert_(t_13484, fn_13477)
        finally:
            test_104.soft_fail_to_hard()
class TestCase126(TestCase53):
    def test___limitAndOffset__2278(self) -> None:
        'limit and offset'
        test_105: Test = Test()
        try:
            t_6899: 'Query'
            t_6899 = from_(sid_662('users')).limit(10)
            t_6900: 'Query'
            t_6900 = t_6899.offset(20)
            q_1554: 'Query' = t_6900
            t_13475: 'bool42' = q_1554.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_13470() -> 'str34':
                return 'limit/offset'
            test_105.assert_(t_13475, fn_13470)
        finally:
            test_105.soft_fail_to_hard()
class TestCase127(TestCase53):
    def test___limitBubblesOnNegative__2279(self) -> None:
        'limit bubbles on negative'
        test_106: Test = Test()
        try:
            did_bubble_1556: 'bool42'
            try:
                from_(sid_662('users')).limit(-1)
                did_bubble_1556 = False
            except Exception46:
                did_bubble_1556 = True
            def fn_13466() -> 'str34':
                return 'negative limit should bubble'
            test_106.assert_(did_bubble_1556, fn_13466)
        finally:
            test_106.soft_fail_to_hard()
class TestCase128(TestCase53):
    def test___offsetBubblesOnNegative__2280(self) -> None:
        'offset bubbles on negative'
        test_107: Test = Test()
        try:
            did_bubble_1558: 'bool42'
            try:
                from_(sid_662('users')).offset(-1)
                did_bubble_1558 = False
            except Exception46:
                did_bubble_1558 = True
            def fn_13462() -> 'str34':
                return 'negative offset should bubble'
            test_107.assert_(did_bubble_1558, fn_13462)
        finally:
            test_107.soft_fail_to_hard()
class TestCase129(TestCase53):
    def test___complexComposedQuery__2281(self) -> None:
        'complex composed query'
        test_108: Test = Test()
        try:
            min_age_1560: 'int40' = 21
            t_13440: 'SafeIdentifier' = sid_662('users')
            t_13441: 'SafeIdentifier' = sid_662('id')
            t_13442: 'SafeIdentifier' = sid_662('name')
            t_13443: 'SafeIdentifier' = sid_662('email')
            t_13444: 'Query' = from_(t_13440).select((t_13441, t_13442, t_13443))
            t_13445: 'SqlBuilder' = SqlBuilder()
            t_13445.append_safe('age >= ')
            t_13445.append_int32(21)
            t_13449: 'Query' = t_13444.where(t_13445.accumulated)
            t_13450: 'SqlBuilder' = SqlBuilder()
            t_13450.append_safe('active = ')
            t_13450.append_boolean(True)
            t_6885: 'Query'
            t_6885 = t_13449.where(t_13450.accumulated).order_by(sid_662('name'), True).limit(25)
            t_6886: 'Query'
            t_6886 = t_6885.offset(0)
            q_1561: 'Query' = t_6886
            t_13460: 'bool42' = q_1561.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_13439() -> 'str34':
                return 'complex query'
            test_108.assert_(t_13460, fn_13439)
        finally:
            test_108.soft_fail_to_hard()
class TestCase130(TestCase53):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__2284(self) -> None:
        'safeToSql applies default limit when none set'
        test_109: Test = Test()
        try:
            q_1563: 'Query' = from_(sid_662('users'))
            t_6862: 'SqlFragment'
            t_6862 = q_1563.safe_to_sql(100)
            t_6863: 'SqlFragment' = t_6862
            s_1564: 'str34' = t_6863.to_string()
            t_13437: 'bool42' = s_1564 == 'SELECT * FROM users LIMIT 100'
            def fn_13433() -> 'str34':
                return str_cat_15572('should have limit: ', s_1564)
            test_109.assert_(t_13437, fn_13433)
        finally:
            test_109.soft_fail_to_hard()
class TestCase131(TestCase53):
    def test___safeToSqlRespectsExplicitLimit__2285(self) -> None:
        'safeToSql respects explicit limit'
        test_110: Test = Test()
        try:
            t_6854: 'Query'
            t_6854 = from_(sid_662('users')).limit(5)
            q_1566: 'Query' = t_6854
            t_6857: 'SqlFragment'
            t_6857 = q_1566.safe_to_sql(100)
            t_6858: 'SqlFragment' = t_6857
            s_1567: 'str34' = t_6858.to_string()
            t_13431: 'bool42' = s_1567 == 'SELECT * FROM users LIMIT 5'
            def fn_13427() -> 'str34':
                return str_cat_15572('explicit limit preserved: ', s_1567)
            test_110.assert_(t_13431, fn_13427)
        finally:
            test_110.soft_fail_to_hard()
class TestCase132(TestCase53):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__2286(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_111: Test = Test()
        try:
            did_bubble_1569: 'bool42'
            try:
                from_(sid_662('users')).safe_to_sql(-1)
                did_bubble_1569 = False
            except Exception46:
                did_bubble_1569 = True
            def fn_13423() -> 'str34':
                return 'negative defaultLimit should bubble'
            test_111.assert_(did_bubble_1569, fn_13423)
        finally:
            test_111.soft_fail_to_hard()
class TestCase133(TestCase53):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__2287(self) -> None:
        'where with injection attempt in string value is escaped'
        test_112: Test = Test()
        try:
            evil_1571: 'str34' = "'; DROP TABLE users; --"
            t_13407: 'SafeIdentifier' = sid_662('users')
            t_13408: 'SqlBuilder' = SqlBuilder()
            t_13408.append_safe('name = ')
            t_13408.append_string("'; DROP TABLE users; --")
            t_13411: 'SqlFragment' = t_13408.accumulated
            q_1572: 'Query' = from_(t_13407).where(t_13411)
            s_1573: 'str34' = q_1572.to_sql().to_string()
            t_13416: 'bool42' = s_1573.find("''") >= 0
            def fn_13406() -> 'str34':
                return str_cat_15572('quotes must be doubled: ', s_1573)
            test_112.assert_(t_13416, fn_13406)
            t_13420: 'bool42' = s_1573.find('SELECT * FROM users WHERE name =') >= 0
            def fn_13405() -> 'str34':
                return str_cat_15572('structure intact: ', s_1573)
            test_112.assert_(t_13420, fn_13405)
        finally:
            test_112.soft_fail_to_hard()
class TestCase134(TestCase53):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__2289(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_113: Test = Test()
        try:
            attack_1575: 'str34' = 'users; DROP TABLE users; --'
            did_bubble_1576: 'bool42'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_1576 = False
            except Exception46:
                did_bubble_1576 = True
            def fn_13402() -> 'str34':
                return 'metacharacter-containing name must be rejected at construction'
            test_113.assert_(did_bubble_1576, fn_13402)
        finally:
            test_113.soft_fail_to_hard()
class TestCase135(TestCase53):
    def test___innerJoinProducesInnerJoin__2290(self) -> None:
        'innerJoin produces INNER JOIN'
        test_114: Test = Test()
        try:
            t_13391: 'SafeIdentifier' = sid_662('users')
            t_13392: 'SafeIdentifier' = sid_662('orders')
            t_13393: 'SqlBuilder' = SqlBuilder()
            t_13393.append_safe('users.id = orders.user_id')
            t_13395: 'SqlFragment' = t_13393.accumulated
            q_1578: 'Query' = from_(t_13391).inner_join(t_13392, t_13395)
            t_13400: 'bool42' = q_1578.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_13390() -> 'str34':
                return 'inner join'
            test_114.assert_(t_13400, fn_13390)
        finally:
            test_114.soft_fail_to_hard()
class TestCase136(TestCase53):
    def test___leftJoinProducesLeftJoin__2292(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_115: Test = Test()
        try:
            t_13379: 'SafeIdentifier' = sid_662('users')
            t_13380: 'SafeIdentifier' = sid_662('profiles')
            t_13381: 'SqlBuilder' = SqlBuilder()
            t_13381.append_safe('users.id = profiles.user_id')
            t_13383: 'SqlFragment' = t_13381.accumulated
            q_1580: 'Query' = from_(t_13379).left_join(t_13380, t_13383)
            t_13388: 'bool42' = q_1580.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_13378() -> 'str34':
                return 'left join'
            test_115.assert_(t_13388, fn_13378)
        finally:
            test_115.soft_fail_to_hard()
class TestCase137(TestCase53):
    def test___rightJoinProducesRightJoin__2294(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_116: Test = Test()
        try:
            t_13367: 'SafeIdentifier' = sid_662('orders')
            t_13368: 'SafeIdentifier' = sid_662('users')
            t_13369: 'SqlBuilder' = SqlBuilder()
            t_13369.append_safe('orders.user_id = users.id')
            t_13371: 'SqlFragment' = t_13369.accumulated
            q_1582: 'Query' = from_(t_13367).right_join(t_13368, t_13371)
            t_13376: 'bool42' = q_1582.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_13366() -> 'str34':
                return 'right join'
            test_116.assert_(t_13376, fn_13366)
        finally:
            test_116.soft_fail_to_hard()
class TestCase138(TestCase53):
    def test___fullJoinProducesFullOuterJoin__2296(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_117: Test = Test()
        try:
            t_13355: 'SafeIdentifier' = sid_662('users')
            t_13356: 'SafeIdentifier' = sid_662('orders')
            t_13357: 'SqlBuilder' = SqlBuilder()
            t_13357.append_safe('users.id = orders.user_id')
            t_13359: 'SqlFragment' = t_13357.accumulated
            q_1584: 'Query' = from_(t_13355).full_join(t_13356, t_13359)
            t_13364: 'bool42' = q_1584.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_13354() -> 'str34':
                return 'full join'
            test_117.assert_(t_13364, fn_13354)
        finally:
            test_117.soft_fail_to_hard()
class TestCase139(TestCase53):
    def test___chainedJoins__2298(self) -> None:
        'chained joins'
        test_118: Test = Test()
        try:
            t_13338: 'SafeIdentifier' = sid_662('users')
            t_13339: 'SafeIdentifier' = sid_662('orders')
            t_13340: 'SqlBuilder' = SqlBuilder()
            t_13340.append_safe('users.id = orders.user_id')
            t_13342: 'SqlFragment' = t_13340.accumulated
            t_13343: 'Query' = from_(t_13338).inner_join(t_13339, t_13342)
            t_13344: 'SafeIdentifier' = sid_662('profiles')
            t_13345: 'SqlBuilder' = SqlBuilder()
            t_13345.append_safe('users.id = profiles.user_id')
            q_1586: 'Query' = t_13343.left_join(t_13344, t_13345.accumulated)
            t_13352: 'bool42' = q_1586.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_13337() -> 'str34':
                return 'chained joins'
            test_118.assert_(t_13352, fn_13337)
        finally:
            test_118.soft_fail_to_hard()
class TestCase140(TestCase53):
    def test___joinWithWhereAndOrderBy__2301(self) -> None:
        'join with where and orderBy'
        test_119: Test = Test()
        try:
            t_13319: 'SafeIdentifier' = sid_662('users')
            t_13320: 'SafeIdentifier' = sid_662('orders')
            t_13321: 'SqlBuilder' = SqlBuilder()
            t_13321.append_safe('users.id = orders.user_id')
            t_13323: 'SqlFragment' = t_13321.accumulated
            t_13324: 'Query' = from_(t_13319).inner_join(t_13320, t_13323)
            t_13325: 'SqlBuilder' = SqlBuilder()
            t_13325.append_safe('orders.total > ')
            t_13325.append_int32(100)
            t_6769: 'Query'
            t_6769 = t_13324.where(t_13325.accumulated).order_by(sid_662('name'), True).limit(10)
            q_1588: 'Query' = t_6769
            t_13335: 'bool42' = q_1588.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_13318() -> 'str34':
                return 'join with where/order/limit'
            test_119.assert_(t_13335, fn_13318)
        finally:
            test_119.soft_fail_to_hard()
class TestCase141(TestCase53):
    def test___colHelperProducesQualifiedReference__2304(self) -> None:
        'col helper produces qualified reference'
        test_120: Test = Test()
        try:
            c_1590: 'SqlFragment' = col(sid_662('users'), sid_662('id'))
            t_13316: 'bool42' = c_1590.to_string() == 'users.id'
            def fn_13310() -> 'str34':
                return 'col helper'
            test_120.assert_(t_13316, fn_13310)
        finally:
            test_120.soft_fail_to_hard()
class TestCase142(TestCase53):
    def test___joinWithColHelper__2305(self) -> None:
        'join with col helper'
        test_121: Test = Test()
        try:
            on_cond_1592: 'SqlFragment' = col(sid_662('users'), sid_662('id'))
            b_1593: 'SqlBuilder' = SqlBuilder()
            b_1593.append_fragment(on_cond_1592)
            b_1593.append_safe(' = ')
            b_1593.append_fragment(col(sid_662('orders'), sid_662('user_id')))
            t_13301: 'SafeIdentifier' = sid_662('users')
            t_13302: 'SafeIdentifier' = sid_662('orders')
            t_13303: 'SqlFragment' = b_1593.accumulated
            q_1594: 'Query' = from_(t_13301).inner_join(t_13302, t_13303)
            t_13308: 'bool42' = q_1594.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_13290() -> 'str34':
                return 'join with col'
            test_121.assert_(t_13308, fn_13290)
        finally:
            test_121.soft_fail_to_hard()
class TestCase143(TestCase53):
    def test___orWhereBasic__2306(self) -> None:
        'orWhere basic'
        test_122: Test = Test()
        try:
            t_13279: 'SafeIdentifier' = sid_662('users')
            t_13280: 'SqlBuilder' = SqlBuilder()
            t_13280.append_safe('status = ')
            t_13280.append_string('active')
            t_13283: 'SqlFragment' = t_13280.accumulated
            q_1596: 'Query' = from_(t_13279).or_where(t_13283)
            t_13288: 'bool42' = q_1596.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_13278() -> 'str34':
                return 'orWhere basic'
            test_122.assert_(t_13288, fn_13278)
        finally:
            test_122.soft_fail_to_hard()
class TestCase144(TestCase53):
    def test___whereThenOrWhere__2308(self) -> None:
        'where then orWhere'
        test_123: Test = Test()
        try:
            t_13262: 'SafeIdentifier' = sid_662('users')
            t_13263: 'SqlBuilder' = SqlBuilder()
            t_13263.append_safe('age > ')
            t_13263.append_int32(18)
            t_13266: 'SqlFragment' = t_13263.accumulated
            t_13267: 'Query' = from_(t_13262).where(t_13266)
            t_13268: 'SqlBuilder' = SqlBuilder()
            t_13268.append_safe('vip = ')
            t_13268.append_boolean(True)
            q_1598: 'Query' = t_13267.or_where(t_13268.accumulated)
            t_13276: 'bool42' = q_1598.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_13261() -> 'str34':
                return 'where then orWhere'
            test_123.assert_(t_13276, fn_13261)
        finally:
            test_123.soft_fail_to_hard()
class TestCase145(TestCase53):
    def test___multipleOrWhere__2311(self) -> None:
        'multiple orWhere'
        test_124: Test = Test()
        try:
            t_13240: 'SafeIdentifier' = sid_662('users')
            t_13241: 'SqlBuilder' = SqlBuilder()
            t_13241.append_safe('active = ')
            t_13241.append_boolean(True)
            t_13244: 'SqlFragment' = t_13241.accumulated
            t_13245: 'Query' = from_(t_13240).where(t_13244)
            t_13246: 'SqlBuilder' = SqlBuilder()
            t_13246.append_safe('role = ')
            t_13246.append_string('admin')
            t_13250: 'Query' = t_13245.or_where(t_13246.accumulated)
            t_13251: 'SqlBuilder' = SqlBuilder()
            t_13251.append_safe('role = ')
            t_13251.append_string('moderator')
            q_1600: 'Query' = t_13250.or_where(t_13251.accumulated)
            t_13259: 'bool42' = q_1600.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_13239() -> 'str34':
                return 'multiple orWhere'
            test_124.assert_(t_13259, fn_13239)
        finally:
            test_124.soft_fail_to_hard()
class TestCase146(TestCase53):
    def test___mixedWhereAndOrWhere__2315(self) -> None:
        'mixed where and orWhere'
        test_125: Test = Test()
        try:
            t_13218: 'SafeIdentifier' = sid_662('users')
            t_13219: 'SqlBuilder' = SqlBuilder()
            t_13219.append_safe('age > ')
            t_13219.append_int32(18)
            t_13222: 'SqlFragment' = t_13219.accumulated
            t_13223: 'Query' = from_(t_13218).where(t_13222)
            t_13224: 'SqlBuilder' = SqlBuilder()
            t_13224.append_safe('active = ')
            t_13224.append_boolean(True)
            t_13228: 'Query' = t_13223.where(t_13224.accumulated)
            t_13229: 'SqlBuilder' = SqlBuilder()
            t_13229.append_safe('vip = ')
            t_13229.append_boolean(True)
            q_1602: 'Query' = t_13228.or_where(t_13229.accumulated)
            t_13237: 'bool42' = q_1602.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_13217() -> 'str34':
                return 'mixed where and orWhere'
            test_125.assert_(t_13237, fn_13217)
        finally:
            test_125.soft_fail_to_hard()
class TestCase147(TestCase53):
    def test___whereNull__2319(self) -> None:
        'whereNull'
        test_126: Test = Test()
        try:
            t_13209: 'SafeIdentifier' = sid_662('users')
            t_13210: 'SafeIdentifier' = sid_662('deleted_at')
            q_1604: 'Query' = from_(t_13209).where_null(t_13210)
            t_13215: 'bool42' = q_1604.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_13208() -> 'str34':
                return 'whereNull'
            test_126.assert_(t_13215, fn_13208)
        finally:
            test_126.soft_fail_to_hard()
class TestCase148(TestCase53):
    def test___whereNotNull__2320(self) -> None:
        'whereNotNull'
        test_127: Test = Test()
        try:
            t_13200: 'SafeIdentifier' = sid_662('users')
            t_13201: 'SafeIdentifier' = sid_662('email')
            q_1606: 'Query' = from_(t_13200).where_not_null(t_13201)
            t_13206: 'bool42' = q_1606.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_13199() -> 'str34':
                return 'whereNotNull'
            test_127.assert_(t_13206, fn_13199)
        finally:
            test_127.soft_fail_to_hard()
class TestCase149(TestCase53):
    def test___whereNullChainedWithWhere__2321(self) -> None:
        'whereNull chained with where'
        test_128: Test = Test()
        try:
            t_13186: 'SafeIdentifier' = sid_662('users')
            t_13187: 'SqlBuilder' = SqlBuilder()
            t_13187.append_safe('active = ')
            t_13187.append_boolean(True)
            t_13190: 'SqlFragment' = t_13187.accumulated
            q_1608: 'Query' = from_(t_13186).where(t_13190).where_null(sid_662('deleted_at'))
            t_13197: 'bool42' = q_1608.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_13185() -> 'str34':
                return 'whereNull chained'
            test_128.assert_(t_13197, fn_13185)
        finally:
            test_128.soft_fail_to_hard()
class TestCase150(TestCase53):
    def test___whereNotNullChainedWithOrWhere__2323(self) -> None:
        'whereNotNull chained with orWhere'
        test_129: Test = Test()
        try:
            t_13172: 'SafeIdentifier' = sid_662('users')
            t_13173: 'SafeIdentifier' = sid_662('deleted_at')
            t_13174: 'Query' = from_(t_13172).where_null(t_13173)
            t_13175: 'SqlBuilder' = SqlBuilder()
            t_13175.append_safe('role = ')
            t_13175.append_string('admin')
            q_1610: 'Query' = t_13174.or_where(t_13175.accumulated)
            t_13183: 'bool42' = q_1610.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_13171() -> 'str34':
                return 'whereNotNull with orWhere'
            test_129.assert_(t_13183, fn_13171)
        finally:
            test_129.soft_fail_to_hard()
class TestCase151(TestCase53):
    def test___whereInWithIntValues__2325(self) -> None:
        'whereIn with int values'
        test_130: Test = Test()
        try:
            t_13160: 'SafeIdentifier' = sid_662('users')
            t_13161: 'SafeIdentifier' = sid_662('id')
            t_13162: 'SqlInt32' = SqlInt32(1)
            t_13163: 'SqlInt32' = SqlInt32(2)
            t_13164: 'SqlInt32' = SqlInt32(3)
            q_1612: 'Query' = from_(t_13160).where_in(t_13161, (t_13162, t_13163, t_13164))
            t_13169: 'bool42' = q_1612.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_13159() -> 'str34':
                return 'whereIn ints'
            test_130.assert_(t_13169, fn_13159)
        finally:
            test_130.soft_fail_to_hard()
class TestCase152(TestCase53):
    def test___whereInWithStringValuesEscaping__2326(self) -> None:
        'whereIn with string values escaping'
        test_131: Test = Test()
        try:
            t_13149: 'SafeIdentifier' = sid_662('users')
            t_13150: 'SafeIdentifier' = sid_662('name')
            t_13151: 'SqlString' = SqlString('Alice')
            t_13152: 'SqlString' = SqlString("Bob's")
            q_1614: 'Query' = from_(t_13149).where_in(t_13150, (t_13151, t_13152))
            t_13157: 'bool42' = q_1614.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_13148() -> 'str34':
                return 'whereIn strings'
            test_131.assert_(t_13157, fn_13148)
        finally:
            test_131.soft_fail_to_hard()
class TestCase153(TestCase53):
    def test___whereInWithEmptyListProduces1_0__2327(self) -> None:
        'whereIn with empty list produces 1=0'
        test_132: Test = Test()
        try:
            t_13140: 'SafeIdentifier' = sid_662('users')
            t_13141: 'SafeIdentifier' = sid_662('id')
            q_1616: 'Query' = from_(t_13140).where_in(t_13141, ())
            t_13146: 'bool42' = q_1616.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_13139() -> 'str34':
                return 'whereIn empty'
            test_132.assert_(t_13146, fn_13139)
        finally:
            test_132.soft_fail_to_hard()
class TestCase154(TestCase53):
    def test___whereInChained__2328(self) -> None:
        'whereIn chained'
        test_133: Test = Test()
        try:
            t_13124: 'SafeIdentifier' = sid_662('users')
            t_13125: 'SqlBuilder' = SqlBuilder()
            t_13125.append_safe('active = ')
            t_13125.append_boolean(True)
            t_13128: 'SqlFragment' = t_13125.accumulated
            q_1618: 'Query' = from_(t_13124).where(t_13128).where_in(sid_662('role'), (SqlString('admin'), SqlString('user')))
            t_13137: 'bool42' = q_1618.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_13123() -> 'str34':
                return 'whereIn chained'
            test_133.assert_(t_13137, fn_13123)
        finally:
            test_133.soft_fail_to_hard()
class TestCase155(TestCase53):
    def test___whereInSingleElement__2330(self) -> None:
        'whereIn single element'
        test_134: Test = Test()
        try:
            t_13114: 'SafeIdentifier' = sid_662('users')
            t_13115: 'SafeIdentifier' = sid_662('id')
            t_13116: 'SqlInt32' = SqlInt32(42)
            q_1620: 'Query' = from_(t_13114).where_in(t_13115, (t_13116,))
            t_13121: 'bool42' = q_1620.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_13113() -> 'str34':
                return 'whereIn single'
            test_134.assert_(t_13121, fn_13113)
        finally:
            test_134.soft_fail_to_hard()
class TestCase156(TestCase53):
    def test___whereNotBasic__2331(self) -> None:
        'whereNot basic'
        test_135: Test = Test()
        try:
            t_13102: 'SafeIdentifier' = sid_662('users')
            t_13103: 'SqlBuilder' = SqlBuilder()
            t_13103.append_safe('active = ')
            t_13103.append_boolean(True)
            t_13106: 'SqlFragment' = t_13103.accumulated
            q_1622: 'Query' = from_(t_13102).where_not(t_13106)
            t_13111: 'bool42' = q_1622.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_13101() -> 'str34':
                return 'whereNot'
            test_135.assert_(t_13111, fn_13101)
        finally:
            test_135.soft_fail_to_hard()
class TestCase157(TestCase53):
    def test___whereNotChained__2333(self) -> None:
        'whereNot chained'
        test_136: Test = Test()
        try:
            t_13085: 'SafeIdentifier' = sid_662('users')
            t_13086: 'SqlBuilder' = SqlBuilder()
            t_13086.append_safe('age > ')
            t_13086.append_int32(18)
            t_13089: 'SqlFragment' = t_13086.accumulated
            t_13090: 'Query' = from_(t_13085).where(t_13089)
            t_13091: 'SqlBuilder' = SqlBuilder()
            t_13091.append_safe('banned = ')
            t_13091.append_boolean(True)
            q_1624: 'Query' = t_13090.where_not(t_13091.accumulated)
            t_13099: 'bool42' = q_1624.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_13084() -> 'str34':
                return 'whereNot chained'
            test_136.assert_(t_13099, fn_13084)
        finally:
            test_136.soft_fail_to_hard()
class TestCase158(TestCase53):
    def test___whereBetweenIntegers__2336(self) -> None:
        'whereBetween integers'
        test_137: Test = Test()
        try:
            t_13074: 'SafeIdentifier' = sid_662('users')
            t_13075: 'SafeIdentifier' = sid_662('age')
            t_13076: 'SqlInt32' = SqlInt32(18)
            t_13077: 'SqlInt32' = SqlInt32(65)
            q_1626: 'Query' = from_(t_13074).where_between(t_13075, t_13076, t_13077)
            t_13082: 'bool42' = q_1626.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_13073() -> 'str34':
                return 'whereBetween ints'
            test_137.assert_(t_13082, fn_13073)
        finally:
            test_137.soft_fail_to_hard()
class TestCase159(TestCase53):
    def test___whereBetweenChained__2337(self) -> None:
        'whereBetween chained'
        test_138: Test = Test()
        try:
            t_13058: 'SafeIdentifier' = sid_662('users')
            t_13059: 'SqlBuilder' = SqlBuilder()
            t_13059.append_safe('active = ')
            t_13059.append_boolean(True)
            t_13062: 'SqlFragment' = t_13059.accumulated
            q_1628: 'Query' = from_(t_13058).where(t_13062).where_between(sid_662('age'), SqlInt32(21), SqlInt32(30))
            t_13071: 'bool42' = q_1628.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_13057() -> 'str34':
                return 'whereBetween chained'
            test_138.assert_(t_13071, fn_13057)
        finally:
            test_138.soft_fail_to_hard()
class TestCase160(TestCase53):
    def test___whereLikeBasic__2339(self) -> None:
        'whereLike basic'
        test_139: Test = Test()
        try:
            t_13049: 'SafeIdentifier' = sid_662('users')
            t_13050: 'SafeIdentifier' = sid_662('name')
            q_1630: 'Query' = from_(t_13049).where_like(t_13050, 'John%')
            t_13055: 'bool42' = q_1630.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_13048() -> 'str34':
                return 'whereLike'
            test_139.assert_(t_13055, fn_13048)
        finally:
            test_139.soft_fail_to_hard()
class TestCase161(TestCase53):
    def test___whereIlikeBasic__2340(self) -> None:
        'whereILike basic'
        test_140: Test = Test()
        try:
            t_13040: 'SafeIdentifier' = sid_662('users')
            t_13041: 'SafeIdentifier' = sid_662('email')
            q_1632: 'Query' = from_(t_13040).where_i_like(t_13041, '%@gmail.com')
            t_13046: 'bool42' = q_1632.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_13039() -> 'str34':
                return 'whereILike'
            test_140.assert_(t_13046, fn_13039)
        finally:
            test_140.soft_fail_to_hard()
class TestCase162(TestCase53):
    def test___whereLikeWithInjectionAttempt__2341(self) -> None:
        'whereLike with injection attempt'
        test_141: Test = Test()
        try:
            t_13026: 'SafeIdentifier' = sid_662('users')
            t_13027: 'SafeIdentifier' = sid_662('name')
            q_1634: 'Query' = from_(t_13026).where_like(t_13027, "'; DROP TABLE users; --")
            s_1635: 'str34' = q_1634.to_sql().to_string()
            t_13032: 'bool42' = s_1635.find("''") >= 0
            def fn_13025() -> 'str34':
                return str_cat_15572('like injection escaped: ', s_1635)
            test_141.assert_(t_13032, fn_13025)
            t_13036: 'bool42' = s_1635.find('LIKE') >= 0
            def fn_13024() -> 'str34':
                return str_cat_15572('like structure intact: ', s_1635)
            test_141.assert_(t_13036, fn_13024)
        finally:
            test_141.soft_fail_to_hard()
class TestCase163(TestCase53):
    def test___whereLikeWildcardPatterns__2342(self) -> None:
        'whereLike wildcard patterns'
        test_142: Test = Test()
        try:
            t_13016: 'SafeIdentifier' = sid_662('users')
            t_13017: 'SafeIdentifier' = sid_662('name')
            q_1637: 'Query' = from_(t_13016).where_like(t_13017, '%son%')
            t_13022: 'bool42' = q_1637.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_13015() -> 'str34':
                return 'whereLike wildcard'
            test_142.assert_(t_13022, fn_13015)
        finally:
            test_142.soft_fail_to_hard()
class TestCase164(TestCase53):
    def test___countAllProducesCount__2343(self) -> None:
        'countAll produces COUNT(*)'
        test_143: Test = Test()
        try:
            f_1639: 'SqlFragment' = count_all()
            t_13013: 'bool42' = f_1639.to_string() == 'COUNT(*)'
            def fn_13009() -> 'str34':
                return 'countAll'
            test_143.assert_(t_13013, fn_13009)
        finally:
            test_143.soft_fail_to_hard()
class TestCase165(TestCase53):
    def test___countColProducesCountField__2344(self) -> None:
        'countCol produces COUNT(field)'
        test_144: Test = Test()
        try:
            f_1641: 'SqlFragment' = count_col(sid_662('id'))
            t_13007: 'bool42' = f_1641.to_string() == 'COUNT(id)'
            def fn_13002() -> 'str34':
                return 'countCol'
            test_144.assert_(t_13007, fn_13002)
        finally:
            test_144.soft_fail_to_hard()
class TestCase166(TestCase53):
    def test___sumColProducesSumField__2345(self) -> None:
        'sumCol produces SUM(field)'
        test_145: Test = Test()
        try:
            f_1643: 'SqlFragment' = sum_col(sid_662('amount'))
            t_13000: 'bool42' = f_1643.to_string() == 'SUM(amount)'
            def fn_12995() -> 'str34':
                return 'sumCol'
            test_145.assert_(t_13000, fn_12995)
        finally:
            test_145.soft_fail_to_hard()
class TestCase167(TestCase53):
    def test___avgColProducesAvgField__2346(self) -> None:
        'avgCol produces AVG(field)'
        test_146: Test = Test()
        try:
            f_1645: 'SqlFragment' = avg_col(sid_662('price'))
            t_12993: 'bool42' = f_1645.to_string() == 'AVG(price)'
            def fn_12988() -> 'str34':
                return 'avgCol'
            test_146.assert_(t_12993, fn_12988)
        finally:
            test_146.soft_fail_to_hard()
class TestCase168(TestCase53):
    def test___minColProducesMinField__2347(self) -> None:
        'minCol produces MIN(field)'
        test_147: Test = Test()
        try:
            f_1647: 'SqlFragment' = min_col(sid_662('created_at'))
            t_12986: 'bool42' = f_1647.to_string() == 'MIN(created_at)'
            def fn_12981() -> 'str34':
                return 'minCol'
            test_147.assert_(t_12986, fn_12981)
        finally:
            test_147.soft_fail_to_hard()
class TestCase169(TestCase53):
    def test___maxColProducesMaxField__2348(self) -> None:
        'maxCol produces MAX(field)'
        test_148: Test = Test()
        try:
            f_1649: 'SqlFragment' = max_col(sid_662('score'))
            t_12979: 'bool42' = f_1649.to_string() == 'MAX(score)'
            def fn_12974() -> 'str34':
                return 'maxCol'
            test_148.assert_(t_12979, fn_12974)
        finally:
            test_148.soft_fail_to_hard()
class TestCase170(TestCase53):
    def test___selectExprWithAggregate__2349(self) -> None:
        'selectExpr with aggregate'
        test_149: Test = Test()
        try:
            t_12966: 'SafeIdentifier' = sid_662('orders')
            t_12967: 'SqlFragment' = count_all()
            q_1651: 'Query' = from_(t_12966).select_expr((t_12967,))
            t_12972: 'bool42' = q_1651.to_sql().to_string() == 'SELECT COUNT(*) FROM orders'
            def fn_12965() -> 'str34':
                return 'selectExpr count'
            test_149.assert_(t_12972, fn_12965)
        finally:
            test_149.soft_fail_to_hard()
class TestCase171(TestCase53):
    def test___selectExprWithMultipleExpressions__2350(self) -> None:
        'selectExpr with multiple expressions'
        test_150: Test = Test()
        try:
            name_frag_1653: 'SqlFragment' = col(sid_662('users'), sid_662('name'))
            t_12957: 'SafeIdentifier' = sid_662('users')
            t_12958: 'SqlFragment' = count_all()
            q_1654: 'Query' = from_(t_12957).select_expr((name_frag_1653, t_12958))
            t_12963: 'bool42' = q_1654.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users'
            def fn_12953() -> 'str34':
                return 'selectExpr multi'
            test_150.assert_(t_12963, fn_12953)
        finally:
            test_150.soft_fail_to_hard()
class TestCase172(TestCase53):
    def test___selectExprOverridesSelectedFields__2351(self) -> None:
        'selectExpr overrides selectedFields'
        test_151: Test = Test()
        try:
            t_12942: 'SafeIdentifier' = sid_662('users')
            t_12943: 'SafeIdentifier' = sid_662('id')
            t_12944: 'SafeIdentifier' = sid_662('name')
            q_1656: 'Query' = from_(t_12942).select((t_12943, t_12944)).select_expr((count_all(),))
            t_12951: 'bool42' = q_1656.to_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_12941() -> 'str34':
                return 'selectExpr overrides select'
            test_151.assert_(t_12951, fn_12941)
        finally:
            test_151.soft_fail_to_hard()
class TestCase173(TestCase53):
    def test___groupBySingleField__2352(self) -> None:
        'groupBy single field'
        test_152: Test = Test()
        try:
            t_12928: 'SafeIdentifier' = sid_662('orders')
            t_12931: 'SqlFragment' = col(sid_662('orders'), sid_662('status'))
            t_12932: 'SqlFragment' = count_all()
            q_1658: 'Query' = from_(t_12928).select_expr((t_12931, t_12932)).group_by(sid_662('status'))
            t_12939: 'bool42' = q_1658.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status'
            def fn_12927() -> 'str34':
                return 'groupBy single'
            test_152.assert_(t_12939, fn_12927)
        finally:
            test_152.soft_fail_to_hard()
class TestCase174(TestCase53):
    def test___groupByMultipleFields__2353(self) -> None:
        'groupBy multiple fields'
        test_153: Test = Test()
        try:
            t_12917: 'SafeIdentifier' = sid_662('orders')
            t_12918: 'SafeIdentifier' = sid_662('status')
            q_1660: 'Query' = from_(t_12917).group_by(t_12918).group_by(sid_662('category'))
            t_12925: 'bool42' = q_1660.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category'
            def fn_12916() -> 'str34':
                return 'groupBy multiple'
            test_153.assert_(t_12925, fn_12916)
        finally:
            test_153.soft_fail_to_hard()
class TestCase175(TestCase53):
    def test___havingBasic__2354(self) -> None:
        'having basic'
        test_154: Test = Test()
        try:
            t_12898: 'SafeIdentifier' = sid_662('orders')
            t_12901: 'SqlFragment' = col(sid_662('orders'), sid_662('status'))
            t_12902: 'SqlFragment' = count_all()
            t_12905: 'Query' = from_(t_12898).select_expr((t_12901, t_12902)).group_by(sid_662('status'))
            t_12906: 'SqlBuilder' = SqlBuilder()
            t_12906.append_safe('COUNT(*) > ')
            t_12906.append_int32(5)
            q_1662: 'Query' = t_12905.having(t_12906.accumulated)
            t_12914: 'bool42' = q_1662.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5'
            def fn_12897() -> 'str34':
                return 'having basic'
            test_154.assert_(t_12914, fn_12897)
        finally:
            test_154.soft_fail_to_hard()
class TestCase176(TestCase53):
    def test___orHaving__2356(self) -> None:
        'orHaving'
        test_155: Test = Test()
        try:
            t_12879: 'SafeIdentifier' = sid_662('orders')
            t_12880: 'SafeIdentifier' = sid_662('status')
            t_12881: 'Query' = from_(t_12879).group_by(t_12880)
            t_12882: 'SqlBuilder' = SqlBuilder()
            t_12882.append_safe('COUNT(*) > ')
            t_12882.append_int32(5)
            t_12886: 'Query' = t_12881.having(t_12882.accumulated)
            t_12887: 'SqlBuilder' = SqlBuilder()
            t_12887.append_safe('SUM(total) > ')
            t_12887.append_int32(1000)
            q_1664: 'Query' = t_12886.or_having(t_12887.accumulated)
            t_12895: 'bool42' = q_1664.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000'
            def fn_12878() -> 'str34':
                return 'orHaving'
            test_155.assert_(t_12895, fn_12878)
        finally:
            test_155.soft_fail_to_hard()
class TestCase177(TestCase53):
    def test___distinctBasic__2359(self) -> None:
        'distinct basic'
        test_156: Test = Test()
        try:
            t_12869: 'SafeIdentifier' = sid_662('users')
            t_12870: 'SafeIdentifier' = sid_662('name')
            q_1666: 'Query' = from_(t_12869).select((t_12870,)).distinct()
            t_12876: 'bool42' = q_1666.to_sql().to_string() == 'SELECT DISTINCT name FROM users'
            def fn_12868() -> 'str34':
                return 'distinct'
            test_156.assert_(t_12876, fn_12868)
        finally:
            test_156.soft_fail_to_hard()
class TestCase178(TestCase53):
    def test___distinctWithWhere__2360(self) -> None:
        'distinct with where'
        test_157: Test = Test()
        try:
            t_12854: 'SafeIdentifier' = sid_662('users')
            t_12855: 'SafeIdentifier' = sid_662('email')
            t_12856: 'Query' = from_(t_12854).select((t_12855,))
            t_12857: 'SqlBuilder' = SqlBuilder()
            t_12857.append_safe('active = ')
            t_12857.append_boolean(True)
            q_1668: 'Query' = t_12856.where(t_12857.accumulated).distinct()
            t_12866: 'bool42' = q_1668.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE'
            def fn_12853() -> 'str34':
                return 'distinct with where'
            test_157.assert_(t_12866, fn_12853)
        finally:
            test_157.soft_fail_to_hard()
class TestCase179(TestCase53):
    def test___countSqlBare__2362(self) -> None:
        'countSql bare'
        test_158: Test = Test()
        try:
            q_1670: 'Query' = from_(sid_662('users'))
            t_12851: 'bool42' = q_1670.count_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_12846() -> 'str34':
                return 'countSql bare'
            test_158.assert_(t_12851, fn_12846)
        finally:
            test_158.soft_fail_to_hard()
class TestCase180(TestCase53):
    def test___countSqlWithWhere__2363(self) -> None:
        'countSql with WHERE'
        test_159: Test = Test()
        try:
            t_12835: 'SafeIdentifier' = sid_662('users')
            t_12836: 'SqlBuilder' = SqlBuilder()
            t_12836.append_safe('active = ')
            t_12836.append_boolean(True)
            t_12839: 'SqlFragment' = t_12836.accumulated
            q_1672: 'Query' = from_(t_12835).where(t_12839)
            t_12844: 'bool42' = q_1672.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_12834() -> 'str34':
                return 'countSql with where'
            test_159.assert_(t_12844, fn_12834)
        finally:
            test_159.soft_fail_to_hard()
class TestCase181(TestCase53):
    def test___countSqlWithJoin__2365(self) -> None:
        'countSql with JOIN'
        test_160: Test = Test()
        try:
            t_12818: 'SafeIdentifier' = sid_662('users')
            t_12819: 'SafeIdentifier' = sid_662('orders')
            t_12820: 'SqlBuilder' = SqlBuilder()
            t_12820.append_safe('users.id = orders.user_id')
            t_12822: 'SqlFragment' = t_12820.accumulated
            t_12823: 'Query' = from_(t_12818).inner_join(t_12819, t_12822)
            t_12824: 'SqlBuilder' = SqlBuilder()
            t_12824.append_safe('orders.total > ')
            t_12824.append_int32(100)
            q_1674: 'Query' = t_12823.where(t_12824.accumulated)
            t_12832: 'bool42' = q_1674.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100'
            def fn_12817() -> 'str34':
                return 'countSql with join'
            test_160.assert_(t_12832, fn_12817)
        finally:
            test_160.soft_fail_to_hard()
class TestCase182(TestCase53):
    def test___countSqlDropsOrderByLimitOffset__2368(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_161: Test = Test()
        try:
            t_12804: 'SafeIdentifier' = sid_662('users')
            t_12805: 'SqlBuilder' = SqlBuilder()
            t_12805.append_safe('active = ')
            t_12805.append_boolean(True)
            t_12808: 'SqlFragment' = t_12805.accumulated
            t_6345: 'Query'
            t_6345 = from_(t_12804).where(t_12808).order_by(sid_662('name'), True).limit(10)
            t_6346: 'Query'
            t_6346 = t_6345.offset(20)
            q_1676: 'Query' = t_6346
            s_1677: 'str34' = q_1676.count_sql().to_string()
            t_12815: 'bool42' = s_1677 == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_12803() -> 'str34':
                return str_cat_15572('countSql drops extras: ', s_1677)
            test_161.assert_(t_12815, fn_12803)
        finally:
            test_161.soft_fail_to_hard()
class TestCase183(TestCase53):
    def test___fullAggregationQuery__2370(self) -> None:
        'full aggregation query'
        test_162: Test = Test()
        try:
            t_12771: 'SafeIdentifier' = sid_662('orders')
            t_12774: 'SqlFragment' = col(sid_662('orders'), sid_662('status'))
            t_12775: 'SqlFragment' = count_all()
            t_12777: 'SqlFragment' = sum_col(sid_662('total'))
            t_12778: 'Query' = from_(t_12771).select_expr((t_12774, t_12775, t_12777))
            t_12779: 'SafeIdentifier' = sid_662('users')
            t_12780: 'SqlBuilder' = SqlBuilder()
            t_12780.append_safe('orders.user_id = users.id')
            t_12783: 'Query' = t_12778.inner_join(t_12779, t_12780.accumulated)
            t_12784: 'SqlBuilder' = SqlBuilder()
            t_12784.append_safe('users.active = ')
            t_12784.append_boolean(True)
            t_12790: 'Query' = t_12783.where(t_12784.accumulated).group_by(sid_662('status'))
            t_12791: 'SqlBuilder' = SqlBuilder()
            t_12791.append_safe('COUNT(*) > ')
            t_12791.append_int32(3)
            q_1679: 'Query' = t_12790.having(t_12791.accumulated).order_by(sid_662('status'), True)
            expected_1680: 'str34' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            t_12801: 'bool42' = q_1679.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_12770() -> 'str34':
                return 'full aggregation'
            test_162.assert_(t_12801, fn_12770)
        finally:
            test_162.soft_fail_to_hard()
class TestCase184(TestCase53):
    def test___unionSql__2374(self) -> None:
        'unionSql'
        test_163: Test = Test()
        try:
            t_12753: 'SafeIdentifier' = sid_662('users')
            t_12754: 'SqlBuilder' = SqlBuilder()
            t_12754.append_safe('role = ')
            t_12754.append_string('admin')
            t_12757: 'SqlFragment' = t_12754.accumulated
            a_1682: 'Query' = from_(t_12753).where(t_12757)
            t_12759: 'SafeIdentifier' = sid_662('users')
            t_12760: 'SqlBuilder' = SqlBuilder()
            t_12760.append_safe('role = ')
            t_12760.append_string('moderator')
            t_12763: 'SqlFragment' = t_12760.accumulated
            b_1683: 'Query' = from_(t_12759).where(t_12763)
            s_1684: 'str34' = union_sql(a_1682, b_1683).to_string()
            t_12768: 'bool42' = s_1684 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')"
            def fn_12752() -> 'str34':
                return str_cat_15572('unionSql: ', s_1684)
            test_163.assert_(t_12768, fn_12752)
        finally:
            test_163.soft_fail_to_hard()
class TestCase185(TestCase53):
    def test___unionAllSql__2377(self) -> None:
        'unionAllSql'
        test_164: Test = Test()
        try:
            t_12741: 'SafeIdentifier' = sid_662('users')
            t_12742: 'SafeIdentifier' = sid_662('name')
            a_1686: 'Query' = from_(t_12741).select((t_12742,))
            t_12744: 'SafeIdentifier' = sid_662('contacts')
            t_12745: 'SafeIdentifier' = sid_662('name')
            b_1687: 'Query' = from_(t_12744).select((t_12745,))
            s_1688: 'str34' = union_all_sql(a_1686, b_1687).to_string()
            t_12750: 'bool42' = s_1688 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)'
            def fn_12740() -> 'str34':
                return str_cat_15572('unionAllSql: ', s_1688)
            test_164.assert_(t_12750, fn_12740)
        finally:
            test_164.soft_fail_to_hard()
class TestCase186(TestCase53):
    def test___intersectSql__2378(self) -> None:
        'intersectSql'
        test_165: Test = Test()
        try:
            t_12729: 'SafeIdentifier' = sid_662('users')
            t_12730: 'SafeIdentifier' = sid_662('email')
            a_1690: 'Query' = from_(t_12729).select((t_12730,))
            t_12732: 'SafeIdentifier' = sid_662('subscribers')
            t_12733: 'SafeIdentifier' = sid_662('email')
            b_1691: 'Query' = from_(t_12732).select((t_12733,))
            s_1692: 'str34' = intersect_sql(a_1690, b_1691).to_string()
            t_12738: 'bool42' = s_1692 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)'
            def fn_12728() -> 'str34':
                return str_cat_15572('intersectSql: ', s_1692)
            test_165.assert_(t_12738, fn_12728)
        finally:
            test_165.soft_fail_to_hard()
class TestCase187(TestCase53):
    def test___exceptSql__2379(self) -> None:
        'exceptSql'
        test_166: Test = Test()
        try:
            t_12717: 'SafeIdentifier' = sid_662('users')
            t_12718: 'SafeIdentifier' = sid_662('id')
            a_1694: 'Query' = from_(t_12717).select((t_12718,))
            t_12720: 'SafeIdentifier' = sid_662('banned')
            t_12721: 'SafeIdentifier' = sid_662('id')
            b_1695: 'Query' = from_(t_12720).select((t_12721,))
            s_1696: 'str34' = except_sql(a_1694, b_1695).to_string()
            t_12726: 'bool42' = s_1696 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)'
            def fn_12716() -> 'str34':
                return str_cat_15572('exceptSql: ', s_1696)
            test_166.assert_(t_12726, fn_12716)
        finally:
            test_166.soft_fail_to_hard()
class TestCase188(TestCase53):
    def test___subqueryWithAlias__2380(self) -> None:
        'subquery with alias'
        test_167: Test = Test()
        try:
            t_12702: 'SafeIdentifier' = sid_662('orders')
            t_12703: 'SafeIdentifier' = sid_662('user_id')
            t_12704: 'Query' = from_(t_12702).select((t_12703,))
            t_12705: 'SqlBuilder' = SqlBuilder()
            t_12705.append_safe('total > ')
            t_12705.append_int32(100)
            inner_1698: 'Query' = t_12704.where(t_12705.accumulated)
            s_1699: 'str34' = subquery(inner_1698, sid_662('big_orders')).to_string()
            t_12714: 'bool42' = s_1699 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders'
            def fn_12701() -> 'str34':
                return str_cat_15572('subquery: ', s_1699)
            test_167.assert_(t_12714, fn_12701)
        finally:
            test_167.soft_fail_to_hard()
class TestCase189(TestCase53):
    def test___existsSql__2382(self) -> None:
        'existsSql'
        test_168: Test = Test()
        try:
            t_12691: 'SafeIdentifier' = sid_662('orders')
            t_12692: 'SqlBuilder' = SqlBuilder()
            t_12692.append_safe('orders.user_id = users.id')
            t_12694: 'SqlFragment' = t_12692.accumulated
            inner_1701: 'Query' = from_(t_12691).where(t_12694)
            s_1702: 'str34' = exists_sql(inner_1701).to_string()
            t_12699: 'bool42' = s_1702 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_12690() -> 'str34':
                return str_cat_15572('existsSql: ', s_1702)
            test_168.assert_(t_12699, fn_12690)
        finally:
            test_168.soft_fail_to_hard()
class TestCase190(TestCase53):
    def test___whereInSubquery__2384(self) -> None:
        'whereInSubquery'
        test_169: Test = Test()
        try:
            t_12674: 'SafeIdentifier' = sid_662('orders')
            t_12675: 'SafeIdentifier' = sid_662('user_id')
            t_12676: 'Query' = from_(t_12674).select((t_12675,))
            t_12677: 'SqlBuilder' = SqlBuilder()
            t_12677.append_safe('total > ')
            t_12677.append_int32(1000)
            sub_1704: 'Query' = t_12676.where(t_12677.accumulated)
            t_12682: 'SafeIdentifier' = sid_662('users')
            t_12683: 'SafeIdentifier' = sid_662('id')
            q_1705: 'Query' = from_(t_12682).where_in_subquery(t_12683, sub_1704)
            s_1706: 'str34' = q_1705.to_sql().to_string()
            t_12688: 'bool42' = s_1706 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)'
            def fn_12673() -> 'str34':
                return str_cat_15572('whereInSubquery: ', s_1706)
            test_169.assert_(t_12688, fn_12673)
        finally:
            test_169.soft_fail_to_hard()
class TestCase191(TestCase53):
    def test___setOperationWithWhereOnEachSide__2386(self) -> None:
        'set operation with WHERE on each side'
        test_170: Test = Test()
        try:
            t_12651: 'SafeIdentifier' = sid_662('users')
            t_12652: 'SqlBuilder' = SqlBuilder()
            t_12652.append_safe('age > ')
            t_12652.append_int32(18)
            t_12655: 'SqlFragment' = t_12652.accumulated
            t_12656: 'Query' = from_(t_12651).where(t_12655)
            t_12657: 'SqlBuilder' = SqlBuilder()
            t_12657.append_safe('active = ')
            t_12657.append_boolean(True)
            a_1708: 'Query' = t_12656.where(t_12657.accumulated)
            t_12662: 'SafeIdentifier' = sid_662('users')
            t_12663: 'SqlBuilder' = SqlBuilder()
            t_12663.append_safe('role = ')
            t_12663.append_string('vip')
            t_12666: 'SqlFragment' = t_12663.accumulated
            b_1709: 'Query' = from_(t_12662).where(t_12666)
            s_1710: 'str34' = union_sql(a_1708, b_1709).to_string()
            t_12671: 'bool42' = s_1710 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')"
            def fn_12650() -> 'str34':
                return str_cat_15572('union with where: ', s_1710)
            test_170.assert_(t_12671, fn_12650)
        finally:
            test_170.soft_fail_to_hard()
class TestCase192(TestCase53):
    def test___whereInSubqueryChainedWithWhere__2390(self) -> None:
        'whereInSubquery chained with where'
        test_171: Test = Test()
        try:
            t_12634: 'SafeIdentifier' = sid_662('orders')
            t_12635: 'SafeIdentifier' = sid_662('user_id')
            sub_1712: 'Query' = from_(t_12634).select((t_12635,))
            t_12637: 'SafeIdentifier' = sid_662('users')
            t_12638: 'SqlBuilder' = SqlBuilder()
            t_12638.append_safe('active = ')
            t_12638.append_boolean(True)
            t_12641: 'SqlFragment' = t_12638.accumulated
            q_1713: 'Query' = from_(t_12637).where(t_12641).where_in_subquery(sid_662('id'), sub_1712)
            s_1714: 'str34' = q_1713.to_sql().to_string()
            t_12648: 'bool42' = s_1714 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)'
            def fn_12633() -> 'str34':
                return str_cat_15572('whereInSubquery chained: ', s_1714)
            test_171.assert_(t_12648, fn_12633)
        finally:
            test_171.soft_fail_to_hard()
class TestCase193(TestCase53):
    def test___existsSqlUsedInWhere__2392(self) -> None:
        'existsSql used in where'
        test_172: Test = Test()
        try:
            t_12620: 'SafeIdentifier' = sid_662('orders')
            t_12621: 'SqlBuilder' = SqlBuilder()
            t_12621.append_safe('orders.user_id = users.id')
            t_12623: 'SqlFragment' = t_12621.accumulated
            sub_1716: 'Query' = from_(t_12620).where(t_12623)
            t_12625: 'SafeIdentifier' = sid_662('users')
            t_12626: 'SqlFragment' = exists_sql(sub_1716)
            q_1717: 'Query' = from_(t_12625).where(t_12626)
            s_1718: 'str34' = q_1717.to_sql().to_string()
            t_12631: 'bool42' = s_1718 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_12619() -> 'str34':
                return str_cat_15572('exists in where: ', s_1718)
            test_172.assert_(t_12631, fn_12619)
        finally:
            test_172.soft_fail_to_hard()
class TestCase194(TestCase53):
    def test___updateQueryBasic__2394(self) -> None:
        'UpdateQuery basic'
        test_173: Test = Test()
        try:
            t_12606: 'SafeIdentifier' = sid_662('users')
            t_12607: 'SafeIdentifier' = sid_662('name')
            t_12608: 'SqlString' = SqlString('Alice')
            t_12609: 'UpdateQuery' = update(t_12606).set(t_12607, t_12608)
            t_12610: 'SqlBuilder' = SqlBuilder()
            t_12610.append_safe('id = ')
            t_12610.append_int32(1)
            t_6167: 'SqlFragment'
            t_6167 = t_12609.where(t_12610.accumulated).to_sql()
            q_1720: 'SqlFragment' = t_6167
            t_12617: 'bool42' = q_1720.to_string() == "UPDATE users SET name = 'Alice' WHERE id = 1"
            def fn_12605() -> 'str34':
                return 'update basic'
            test_173.assert_(t_12617, fn_12605)
        finally:
            test_173.soft_fail_to_hard()
class TestCase195(TestCase53):
    def test___updateQueryMultipleSet__2396(self) -> None:
        'UpdateQuery multiple SET'
        test_174: Test = Test()
        try:
            t_12589: 'SafeIdentifier' = sid_662('users')
            t_12590: 'SafeIdentifier' = sid_662('name')
            t_12591: 'SqlString' = SqlString('Bob')
            t_12595: 'UpdateQuery' = update(t_12589).set(t_12590, t_12591).set(sid_662('age'), SqlInt32(30))
            t_12596: 'SqlBuilder' = SqlBuilder()
            t_12596.append_safe('id = ')
            t_12596.append_int32(2)
            t_6152: 'SqlFragment'
            t_6152 = t_12595.where(t_12596.accumulated).to_sql()
            q_1722: 'SqlFragment' = t_6152
            t_12603: 'bool42' = q_1722.to_string() == "UPDATE users SET name = 'Bob', age = 30 WHERE id = 2"
            def fn_12588() -> 'str34':
                return 'update multi set'
            test_174.assert_(t_12603, fn_12588)
        finally:
            test_174.soft_fail_to_hard()
class TestCase196(TestCase53):
    def test___updateQueryMultipleWhere__2398(self) -> None:
        'UpdateQuery multiple WHERE'
        test_175: Test = Test()
        try:
            t_12570: 'SafeIdentifier' = sid_662('users')
            t_12571: 'SafeIdentifier' = sid_662('active')
            t_12572: 'SqlBoolean' = SqlBoolean(False)
            t_12573: 'UpdateQuery' = update(t_12570).set(t_12571, t_12572)
            t_12574: 'SqlBuilder' = SqlBuilder()
            t_12574.append_safe('age < ')
            t_12574.append_int32(18)
            t_12578: 'UpdateQuery' = t_12573.where(t_12574.accumulated)
            t_12579: 'SqlBuilder' = SqlBuilder()
            t_12579.append_safe('role = ')
            t_12579.append_string('guest')
            t_6134: 'SqlFragment'
            t_6134 = t_12578.where(t_12579.accumulated).to_sql()
            q_1724: 'SqlFragment' = t_6134
            t_12586: 'bool42' = q_1724.to_string() == "UPDATE users SET active = FALSE WHERE age < 18 AND role = 'guest'"
            def fn_12569() -> 'str34':
                return 'update multi where'
            test_175.assert_(t_12586, fn_12569)
        finally:
            test_175.soft_fail_to_hard()
class TestCase197(TestCase53):
    def test___updateQueryOrWhere__2401(self) -> None:
        'UpdateQuery orWhere'
        test_176: Test = Test()
        try:
            t_12551: 'SafeIdentifier' = sid_662('users')
            t_12552: 'SafeIdentifier' = sid_662('status')
            t_12553: 'SqlString' = SqlString('banned')
            t_12554: 'UpdateQuery' = update(t_12551).set(t_12552, t_12553)
            t_12555: 'SqlBuilder' = SqlBuilder()
            t_12555.append_safe('spam_count > ')
            t_12555.append_int32(10)
            t_12559: 'UpdateQuery' = t_12554.where(t_12555.accumulated)
            t_12560: 'SqlBuilder' = SqlBuilder()
            t_12560.append_safe('reported = ')
            t_12560.append_boolean(True)
            t_6113: 'SqlFragment'
            t_6113 = t_12559.or_where(t_12560.accumulated).to_sql()
            q_1726: 'SqlFragment' = t_6113
            t_12567: 'bool42' = q_1726.to_string() == "UPDATE users SET status = 'banned' WHERE spam_count > 10 OR reported = TRUE"
            def fn_12550() -> 'str34':
                return 'update orWhere'
            test_176.assert_(t_12567, fn_12550)
        finally:
            test_176.soft_fail_to_hard()
class TestCase198(TestCase53):
    def test___updateQueryBubblesWithoutWhere__2404(self) -> None:
        'UpdateQuery bubbles without WHERE'
        test_177: Test = Test()
        try:
            t_12544: 'SafeIdentifier'
            t_12545: 'SafeIdentifier'
            t_12546: 'SqlInt32'
            did_bubble_1728: 'bool42'
            try:
                t_12544 = sid_662('users')
                t_12545 = sid_662('x')
                t_12546 = SqlInt32(1)
                update(t_12544).set(t_12545, t_12546).to_sql()
                did_bubble_1728 = False
            except Exception46:
                did_bubble_1728 = True
            def fn_12543() -> 'str34':
                return 'update without WHERE should bubble'
            test_177.assert_(did_bubble_1728, fn_12543)
        finally:
            test_177.soft_fail_to_hard()
class TestCase199(TestCase53):
    def test___updateQueryBubblesWithoutSet__2405(self) -> None:
        'UpdateQuery bubbles without SET'
        test_178: Test = Test()
        try:
            t_12535: 'SafeIdentifier'
            t_12536: 'SqlBuilder'
            t_12539: 'SqlFragment'
            did_bubble_1730: 'bool42'
            try:
                t_12535 = sid_662('users')
                t_12536 = SqlBuilder()
                t_12536.append_safe('id = ')
                t_12536.append_int32(1)
                t_12539 = t_12536.accumulated
                update(t_12535).where(t_12539).to_sql()
                did_bubble_1730 = False
            except Exception46:
                did_bubble_1730 = True
            def fn_12534() -> 'str34':
                return 'update without SET should bubble'
            test_178.assert_(did_bubble_1730, fn_12534)
        finally:
            test_178.soft_fail_to_hard()
class TestCase200(TestCase53):
    def test___updateQueryWithLimit__2407(self) -> None:
        'UpdateQuery with limit'
        test_179: Test = Test()
        try:
            t_12521: 'SafeIdentifier' = sid_662('users')
            t_12522: 'SafeIdentifier' = sid_662('active')
            t_12523: 'SqlBoolean' = SqlBoolean(False)
            t_12524: 'UpdateQuery' = update(t_12521).set(t_12522, t_12523)
            t_12525: 'SqlBuilder' = SqlBuilder()
            t_12525.append_safe('last_login < ')
            t_12525.append_string('2024-01-01')
            t_6076: 'UpdateQuery'
            t_6076 = t_12524.where(t_12525.accumulated).limit(100)
            t_6077: 'SqlFragment'
            t_6077 = t_6076.to_sql()
            q_1732: 'SqlFragment' = t_6077
            t_12532: 'bool42' = q_1732.to_string() == "UPDATE users SET active = FALSE WHERE last_login < '2024-01-01' LIMIT 100"
            def fn_12520() -> 'str34':
                return 'update limit'
            test_179.assert_(t_12532, fn_12520)
        finally:
            test_179.soft_fail_to_hard()
class TestCase201(TestCase53):
    def test___updateQueryEscaping__2409(self) -> None:
        'UpdateQuery escaping'
        test_180: Test = Test()
        try:
            t_12507: 'SafeIdentifier' = sid_662('users')
            t_12508: 'SafeIdentifier' = sid_662('bio')
            t_12509: 'SqlString' = SqlString("It's a test")
            t_12510: 'UpdateQuery' = update(t_12507).set(t_12508, t_12509)
            t_12511: 'SqlBuilder' = SqlBuilder()
            t_12511.append_safe('id = ')
            t_12511.append_int32(1)
            t_6061: 'SqlFragment'
            t_6061 = t_12510.where(t_12511.accumulated).to_sql()
            q_1734: 'SqlFragment' = t_6061
            t_12518: 'bool42' = q_1734.to_string() == "UPDATE users SET bio = 'It''s a test' WHERE id = 1"
            def fn_12506() -> 'str34':
                return 'update escaping'
            test_180.assert_(t_12518, fn_12506)
        finally:
            test_180.soft_fail_to_hard()
class TestCase202(TestCase53):
    def test___deleteQueryBasic__2411(self) -> None:
        'DeleteQuery basic'
        test_181: Test = Test()
        try:
            t_12496: 'SafeIdentifier' = sid_662('users')
            t_12497: 'SqlBuilder' = SqlBuilder()
            t_12497.append_safe('id = ')
            t_12497.append_int32(1)
            t_12500: 'SqlFragment' = t_12497.accumulated
            t_6046: 'SqlFragment'
            t_6046 = delete_from(t_12496).where(t_12500).to_sql()
            q_1736: 'SqlFragment' = t_6046
            t_12504: 'bool42' = q_1736.to_string() == 'DELETE FROM users WHERE id = 1'
            def fn_12495() -> 'str34':
                return 'delete basic'
            test_181.assert_(t_12504, fn_12495)
        finally:
            test_181.soft_fail_to_hard()
class TestCase203(TestCase53):
    def test___deleteQueryMultipleWhere__2413(self) -> None:
        'DeleteQuery multiple WHERE'
        test_182: Test = Test()
        try:
            t_12480: 'SafeIdentifier' = sid_662('logs')
            t_12481: 'SqlBuilder' = SqlBuilder()
            t_12481.append_safe('created_at < ')
            t_12481.append_string('2024-01-01')
            t_12484: 'SqlFragment' = t_12481.accumulated
            t_12485: 'DeleteQuery' = delete_from(t_12480).where(t_12484)
            t_12486: 'SqlBuilder' = SqlBuilder()
            t_12486.append_safe('level = ')
            t_12486.append_string('debug')
            t_6034: 'SqlFragment'
            t_6034 = t_12485.where(t_12486.accumulated).to_sql()
            q_1738: 'SqlFragment' = t_6034
            t_12493: 'bool42' = q_1738.to_string() == "DELETE FROM logs WHERE created_at < '2024-01-01' AND level = 'debug'"
            def fn_12479() -> 'str34':
                return 'delete multi where'
            test_182.assert_(t_12493, fn_12479)
        finally:
            test_182.soft_fail_to_hard()
class TestCase204(TestCase53):
    def test___deleteQueryBubblesWithoutWhere__2416(self) -> None:
        'DeleteQuery bubbles without WHERE'
        test_183: Test = Test()
        try:
            did_bubble_1740: 'bool42'
            try:
                delete_from(sid_662('users')).to_sql()
                did_bubble_1740 = False
            except Exception46:
                did_bubble_1740 = True
            def fn_12475() -> 'str34':
                return 'delete without WHERE should bubble'
            test_183.assert_(did_bubble_1740, fn_12475)
        finally:
            test_183.soft_fail_to_hard()
class TestCase205(TestCase53):
    def test___deleteQueryOrWhere__2417(self) -> None:
        'DeleteQuery orWhere'
        test_184: Test = Test()
        try:
            t_12460: 'SafeIdentifier' = sid_662('sessions')
            t_12461: 'SqlBuilder' = SqlBuilder()
            t_12461.append_safe('expired = ')
            t_12461.append_boolean(True)
            t_12464: 'SqlFragment' = t_12461.accumulated
            t_12465: 'DeleteQuery' = delete_from(t_12460).where(t_12464)
            t_12466: 'SqlBuilder' = SqlBuilder()
            t_12466.append_safe('created_at < ')
            t_12466.append_string('2023-01-01')
            t_6013: 'SqlFragment'
            t_6013 = t_12465.or_where(t_12466.accumulated).to_sql()
            q_1742: 'SqlFragment' = t_6013
            t_12473: 'bool42' = q_1742.to_string() == "DELETE FROM sessions WHERE expired = TRUE OR created_at < '2023-01-01'"
            def fn_12459() -> 'str34':
                return 'delete orWhere'
            test_184.assert_(t_12473, fn_12459)
        finally:
            test_184.soft_fail_to_hard()
class TestCase206(TestCase53):
    def test___deleteQueryWithLimit__2420(self) -> None:
        'DeleteQuery with limit'
        test_185: Test = Test()
        try:
            t_12449: 'SafeIdentifier' = sid_662('logs')
            t_12450: 'SqlBuilder' = SqlBuilder()
            t_12450.append_safe('level = ')
            t_12450.append_string('debug')
            t_12453: 'SqlFragment' = t_12450.accumulated
            t_5994: 'DeleteQuery'
            t_5994 = delete_from(t_12449).where(t_12453).limit(1000)
            t_5995: 'SqlFragment'
            t_5995 = t_5994.to_sql()
            q_1744: 'SqlFragment' = t_5995
            t_12457: 'bool42' = q_1744.to_string() == "DELETE FROM logs WHERE level = 'debug' LIMIT 1000"
            def fn_12448() -> 'str34':
                return 'delete limit'
            test_185.assert_(t_12457, fn_12448)
        finally:
            test_185.soft_fail_to_hard()
class TestCase207(TestCase53):
    def test___orderByNullsNullsFirst__2422(self) -> None:
        'orderByNulls NULLS FIRST'
        test_186: Test = Test()
        try:
            t_12439: 'SafeIdentifier' = sid_662('users')
            t_12440: 'SafeIdentifier' = sid_662('email')
            t_12441: 'NullsFirst' = NullsFirst()
            q_1746: 'Query' = from_(t_12439).order_by_nulls(t_12440, True, t_12441)
            t_12446: 'bool42' = q_1746.to_sql().to_string() == 'SELECT * FROM users ORDER BY email ASC NULLS FIRST'
            def fn_12438() -> 'str34':
                return 'nulls first'
            test_186.assert_(t_12446, fn_12438)
        finally:
            test_186.soft_fail_to_hard()
class TestCase208(TestCase53):
    def test___orderByNullsNullsLast__2423(self) -> None:
        'orderByNulls NULLS LAST'
        test_187: Test = Test()
        try:
            t_12429: 'SafeIdentifier' = sid_662('users')
            t_12430: 'SafeIdentifier' = sid_662('score')
            t_12431: 'NullsLast' = NullsLast()
            q_1748: 'Query' = from_(t_12429).order_by_nulls(t_12430, False, t_12431)
            t_12436: 'bool42' = q_1748.to_sql().to_string() == 'SELECT * FROM users ORDER BY score DESC NULLS LAST'
            def fn_12428() -> 'str34':
                return 'nulls last'
            test_187.assert_(t_12436, fn_12428)
        finally:
            test_187.soft_fail_to_hard()
class TestCase209(TestCase53):
    def test___mixedOrderByAndOrderByNulls__2424(self) -> None:
        'mixed orderBy and orderByNulls'
        test_188: Test = Test()
        try:
            t_12417: 'SafeIdentifier' = sid_662('users')
            t_12418: 'SafeIdentifier' = sid_662('name')
            q_1750: 'Query' = from_(t_12417).order_by(t_12418, True).order_by_nulls(sid_662('email'), True, NullsFirst())
            t_12426: 'bool42' = q_1750.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC, email ASC NULLS FIRST'
            def fn_12416() -> 'str34':
                return 'mixed order'
            test_188.assert_(t_12426, fn_12416)
        finally:
            test_188.soft_fail_to_hard()
class TestCase210(TestCase53):
    def test___crossJoin__2425(self) -> None:
        'crossJoin'
        test_189: Test = Test()
        try:
            t_12408: 'SafeIdentifier' = sid_662('users')
            t_12409: 'SafeIdentifier' = sid_662('colors')
            q_1752: 'Query' = from_(t_12408).cross_join(t_12409)
            t_12414: 'bool42' = q_1752.to_sql().to_string() == 'SELECT * FROM users CROSS JOIN colors'
            def fn_12407() -> 'str34':
                return 'cross join'
            test_189.assert_(t_12414, fn_12407)
        finally:
            test_189.soft_fail_to_hard()
class TestCase211(TestCase53):
    def test___crossJoinCombinedWithOtherJoins__2426(self) -> None:
        'crossJoin combined with other joins'
        test_190: Test = Test()
        try:
            t_12394: 'SafeIdentifier' = sid_662('users')
            t_12395: 'SafeIdentifier' = sid_662('orders')
            t_12396: 'SqlBuilder' = SqlBuilder()
            t_12396.append_safe('users.id = orders.user_id')
            t_12398: 'SqlFragment' = t_12396.accumulated
            q_1754: 'Query' = from_(t_12394).inner_join(t_12395, t_12398).cross_join(sid_662('colors'))
            t_12405: 'bool42' = q_1754.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id CROSS JOIN colors'
            def fn_12393() -> 'str34':
                return 'cross + inner join'
            test_190.assert_(t_12405, fn_12393)
        finally:
            test_190.soft_fail_to_hard()
class TestCase212(TestCase53):
    def test___lockForUpdate__2428(self) -> None:
        'lock FOR UPDATE'
        test_191: Test = Test()
        try:
            t_12380: 'SafeIdentifier' = sid_662('users')
            t_12381: 'SqlBuilder' = SqlBuilder()
            t_12381.append_safe('id = ')
            t_12381.append_int32(1)
            t_12384: 'SqlFragment' = t_12381.accumulated
            q_1756: 'Query' = from_(t_12380).where(t_12384).lock(ForUpdate())
            t_12391: 'bool42' = q_1756.to_sql().to_string() == 'SELECT * FROM users WHERE id = 1 FOR UPDATE'
            def fn_12379() -> 'str34':
                return 'for update'
            test_191.assert_(t_12391, fn_12379)
        finally:
            test_191.soft_fail_to_hard()
class TestCase213(TestCase53):
    def test___lockForShare__2430(self) -> None:
        'lock FOR SHARE'
        test_192: Test = Test()
        try:
            t_12369: 'SafeIdentifier' = sid_662('users')
            t_12370: 'SafeIdentifier' = sid_662('name')
            q_1758: 'Query' = from_(t_12369).select((t_12370,)).lock(ForShare())
            t_12377: 'bool42' = q_1758.to_sql().to_string() == 'SELECT name FROM users FOR SHARE'
            def fn_12368() -> 'str34':
                return 'for share'
            test_192.assert_(t_12377, fn_12368)
        finally:
            test_192.soft_fail_to_hard()
class TestCase214(TestCase53):
    def test___lockWithFullQuery__2431(self) -> None:
        'lock with full query'
        test_193: Test = Test()
        try:
            t_12355: 'SafeIdentifier' = sid_662('accounts')
            t_12356: 'SqlBuilder' = SqlBuilder()
            t_12356.append_safe('id = ')
            t_12356.append_int32(42)
            t_12359: 'SqlFragment' = t_12356.accumulated
            t_5918: 'Query'
            t_5918 = from_(t_12355).where(t_12359).limit(1)
            t_12362: 'Query' = t_5918.lock(ForUpdate())
            q_1760: 'Query' = t_12362
            t_12366: 'bool42' = q_1760.to_sql().to_string() == 'SELECT * FROM accounts WHERE id = 42 LIMIT 1 FOR UPDATE'
            def fn_12354() -> 'str34':
                return 'lock full query'
            test_193.assert_(t_12366, fn_12354)
        finally:
            test_193.soft_fail_to_hard()
class TestCase215(TestCase53):
    def test___safeIdentifierAcceptsValidNames__2433(self) -> None:
        'safeIdentifier accepts valid names'
        test_200: Test = Test()
        try:
            t_5907: 'SafeIdentifier'
            t_5907 = safe_identifier('user_name')
            id_1808: 'SafeIdentifier' = t_5907
            t_12352: 'bool42' = id_1808.sql_value == 'user_name'
            def fn_12349() -> 'str34':
                return 'value should round-trip'
            test_200.assert_(t_12352, fn_12349)
        finally:
            test_200.soft_fail_to_hard()
class TestCase216(TestCase53):
    def test___safeIdentifierRejectsEmptyString__2434(self) -> None:
        'safeIdentifier rejects empty string'
        test_201: Test = Test()
        try:
            did_bubble_1810: 'bool42'
            try:
                safe_identifier('')
                did_bubble_1810 = False
            except Exception46:
                did_bubble_1810 = True
            def fn_12346() -> 'str34':
                return 'empty string should bubble'
            test_201.assert_(did_bubble_1810, fn_12346)
        finally:
            test_201.soft_fail_to_hard()
class TestCase217(TestCase53):
    def test___safeIdentifierRejectsLeadingDigit__2435(self) -> None:
        'safeIdentifier rejects leading digit'
        test_202: Test = Test()
        try:
            did_bubble_1812: 'bool42'
            try:
                safe_identifier('1col')
                did_bubble_1812 = False
            except Exception46:
                did_bubble_1812 = True
            def fn_12343() -> 'str34':
                return 'leading digit should bubble'
            test_202.assert_(did_bubble_1812, fn_12343)
        finally:
            test_202.soft_fail_to_hard()
class TestCase218(TestCase53):
    def test___safeIdentifierRejectsSqlMetacharacters__2436(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_203: Test = Test()
        try:
            cases_1814: 'Sequence38[str34]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_12340(c_1815: 'str34') -> 'None':
                did_bubble_1816: 'bool42'
                try:
                    safe_identifier(c_1815)
                    did_bubble_1816 = False
                except Exception46:
                    did_bubble_1816 = True
                def fn_12337() -> 'str34':
                    return str_cat_15572('should reject: ', c_1815)
                test_203.assert_(did_bubble_1816, fn_12337)
            list_for_each_15564(cases_1814, fn_12340)
        finally:
            test_203.soft_fail_to_hard()
class TestCase219(TestCase53):
    def test___tableDefFieldLookupFound__2437(self) -> None:
        'TableDef field lookup - found'
        test_204: Test = Test()
        try:
            t_5884: 'SafeIdentifier'
            t_5884 = safe_identifier('users')
            t_5885: 'SafeIdentifier' = t_5884
            t_5886: 'SafeIdentifier'
            t_5886 = safe_identifier('name')
            t_5887: 'SafeIdentifier' = t_5886
            t_12327: 'StringField' = StringField()
            t_12328: 'FieldDef' = FieldDef(t_5887, t_12327, False, None, False)
            t_5890: 'SafeIdentifier'
            t_5890 = safe_identifier('age')
            t_5891: 'SafeIdentifier' = t_5890
            t_12329: 'IntField' = IntField()
            t_12330: 'FieldDef' = FieldDef(t_5891, t_12329, False, None, False)
            td_1818: 'TableDef' = TableDef(t_5885, (t_12328, t_12330), None)
            t_5895: 'FieldDef'
            t_5895 = td_1818.field('age')
            f_1819: 'FieldDef' = t_5895
            t_12335: 'bool42' = f_1819.name.sql_value == 'age'
            def fn_12326() -> 'str34':
                return 'should find age field'
            test_204.assert_(t_12335, fn_12326)
        finally:
            test_204.soft_fail_to_hard()
class TestCase220(TestCase53):
    def test___tableDefFieldLookupNotFoundBubbles__2438(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_205: Test = Test()
        try:
            t_5875: 'SafeIdentifier'
            t_5875 = safe_identifier('users')
            t_5876: 'SafeIdentifier' = t_5875
            t_5877: 'SafeIdentifier'
            t_5877 = safe_identifier('name')
            t_5878: 'SafeIdentifier' = t_5877
            t_12321: 'StringField' = StringField()
            t_12322: 'FieldDef' = FieldDef(t_5878, t_12321, False, None, False)
            td_1821: 'TableDef' = TableDef(t_5876, (t_12322,), None)
            did_bubble_1822: 'bool42'
            try:
                td_1821.field('nonexistent')
                did_bubble_1822 = False
            except Exception46:
                did_bubble_1822 = True
            def fn_12320() -> 'str34':
                return 'unknown field should bubble'
            test_205.assert_(did_bubble_1822, fn_12320)
        finally:
            test_205.soft_fail_to_hard()
class TestCase221(TestCase53):
    def test___fieldDefNullableFlag__2439(self) -> None:
        'FieldDef nullable flag'
        test_206: Test = Test()
        try:
            t_5863: 'SafeIdentifier'
            t_5863 = safe_identifier('email')
            t_5864: 'SafeIdentifier' = t_5863
            t_12309: 'StringField' = StringField()
            required_1824: 'FieldDef' = FieldDef(t_5864, t_12309, False, None, False)
            t_5867: 'SafeIdentifier'
            t_5867 = safe_identifier('bio')
            t_5868: 'SafeIdentifier' = t_5867
            t_12311: 'StringField' = StringField()
            optional_1825: 'FieldDef' = FieldDef(t_5868, t_12311, True, None, False)
            t_12315: 'bool42' = not required_1824.nullable
            def fn_12308() -> 'str34':
                return 'required field should not be nullable'
            test_206.assert_(t_12315, fn_12308)
            t_12317: 'bool42' = optional_1825.nullable
            def fn_12307() -> 'str34':
                return 'optional field should be nullable'
            test_206.assert_(t_12317, fn_12307)
        finally:
            test_206.soft_fail_to_hard()
class TestCase222(TestCase53):
    def test___pkNameDefaultsToIdWhenPrimaryKeyIsNull__2440(self) -> None:
        'pkName defaults to id when primaryKey is null'
        test_207: Test = Test()
        try:
            t_5854: 'SafeIdentifier'
            t_5854 = safe_identifier('users')
            t_5855: 'SafeIdentifier' = t_5854
            t_5856: 'SafeIdentifier'
            t_5856 = safe_identifier('name')
            t_5857: 'SafeIdentifier' = t_5856
            t_12300: 'StringField' = StringField()
            t_12301: 'FieldDef' = FieldDef(t_5857, t_12300, False, None, False)
            td_1827: 'TableDef' = TableDef(t_5855, (t_12301,), None)
            t_12305: 'bool42' = td_1827.pk_name() == 'id'
            def fn_12299() -> 'str34':
                return 'default pk should be id'
            test_207.assert_(t_12305, fn_12299)
        finally:
            test_207.soft_fail_to_hard()
class TestCase223(TestCase53):
    def test___pkNameReturnsCustomPrimaryKey__2441(self) -> None:
        'pkName returns custom primary key'
        test_208: Test = Test()
        try:
            t_5842: 'SafeIdentifier'
            t_5842 = safe_identifier('users')
            t_5843: 'SafeIdentifier' = t_5842
            t_5844: 'SafeIdentifier'
            t_5844 = safe_identifier('user_id')
            t_5845: 'SafeIdentifier' = t_5844
            t_12292: 'IntField' = IntField()
            t_5850: 'Sequence38[FieldDef]' = (FieldDef(t_5845, t_12292, False, None, False),)
            t_5848: 'SafeIdentifier'
            t_5848 = safe_identifier('user_id')
            t_5849: 'SafeIdentifier' = t_5848
            td_1829: 'TableDef' = TableDef(t_5843, t_5850, t_5849)
            t_12297: 'bool42' = td_1829.pk_name() == 'user_id'
            def fn_12291() -> 'str34':
                return 'custom pk should be user_id'
            test_208.assert_(t_12297, fn_12291)
        finally:
            test_208.soft_fail_to_hard()
class TestCase224(TestCase53):
    def test___timestampsReturnsTwoDateFieldDefs__2442(self) -> None:
        'timestamps returns two DateField defs'
        test_209: Test = Test()
        try:
            t_5818: 'Sequence38[FieldDef]'
            t_5818 = timestamps()
            ts_1831: 'Sequence38[FieldDef]' = t_5818
            t_12259: 'bool42' = len_15570(ts_1831) == 2
            def fn_12256() -> 'str34':
                return 'should return 2 fields'
            test_209.assert_(t_12259, fn_12256)
            t_12265: 'bool42' = list_get_15578(ts_1831, 0).name.sql_value == 'inserted_at'
            def fn_12255() -> 'str34':
                return 'first should be inserted_at'
            test_209.assert_(t_12265, fn_12255)
            t_12271: 'bool42' = list_get_15578(ts_1831, 1).name.sql_value == 'updated_at'
            def fn_12254() -> 'str34':
                return 'second should be updated_at'
            test_209.assert_(t_12271, fn_12254)
            t_12274: 'bool42' = list_get_15578(ts_1831, 0).nullable
            def fn_12253() -> 'str34':
                return 'inserted_at should be nullable'
            test_209.assert_(t_12274, fn_12253)
            t_12278: 'bool42' = list_get_15578(ts_1831, 1).nullable
            def fn_12252() -> 'str34':
                return 'updated_at should be nullable'
            test_209.assert_(t_12278, fn_12252)
            t_12284: 'bool42' = not list_get_15578(ts_1831, 0).default_value is None
            def fn_12251() -> 'str34':
                return 'inserted_at should have default'
            test_209.assert_(t_12284, fn_12251)
            t_12289: 'bool42' = not list_get_15578(ts_1831, 1).default_value is None
            def fn_12250() -> 'str34':
                return 'updated_at should have default'
            test_209.assert_(t_12289, fn_12250)
        finally:
            test_209.soft_fail_to_hard()
class TestCase225(TestCase53):
    def test___fieldDefDefaultValueField__2443(self) -> None:
        'FieldDef defaultValue field'
        test_210: Test = Test()
        try:
            t_5805: 'SafeIdentifier'
            t_5805 = safe_identifier('status')
            t_5806: 'SafeIdentifier' = t_5805
            t_12237: 'StringField' = StringField()
            t_12238: 'SqlDefault' = SqlDefault()
            with_default_1833: 'FieldDef' = FieldDef(t_5806, t_12237, False, t_12238, False)
            t_5810: 'SafeIdentifier'
            t_5810 = safe_identifier('name')
            t_5811: 'SafeIdentifier' = t_5810
            t_12240: 'StringField' = StringField()
            without_default_1834: 'FieldDef' = FieldDef(t_5811, t_12240, False, None, False)
            t_12244: 'bool42' = not with_default_1833.default_value is None
            def fn_12236() -> 'str34':
                return 'should have default'
            test_210.assert_(t_12244, fn_12236)
            t_12248: 'bool42' = without_default_1834.default_value is None
            def fn_12235() -> 'str34':
                return 'should not have default'
            test_210.assert_(t_12248, fn_12235)
        finally:
            test_210.soft_fail_to_hard()
class TestCase226(TestCase53):
    def test___fieldDefVirtualFlag__2444(self) -> None:
        'FieldDef virtual flag'
        test_211: Test = Test()
        try:
            t_5793: 'SafeIdentifier'
            t_5793 = safe_identifier('name')
            t_5794: 'SafeIdentifier' = t_5793
            t_12224: 'StringField' = StringField()
            normal_1836: 'FieldDef' = FieldDef(t_5794, t_12224, False, None, False)
            t_5797: 'SafeIdentifier'
            t_5797 = safe_identifier('full_name')
            t_5798: 'SafeIdentifier' = t_5797
            t_12226: 'StringField' = StringField()
            virt_1837: 'FieldDef' = FieldDef(t_5798, t_12226, True, None, True)
            t_12230: 'bool42' = not normal_1836.virtual
            def fn_12223() -> 'str34':
                return 'normal field should not be virtual'
            test_211.assert_(t_12230, fn_12223)
            t_12232: 'bool42' = virt_1837.virtual
            def fn_12222() -> 'str34':
                return 'virtual field should be virtual'
            test_211.assert_(t_12232, fn_12222)
        finally:
            test_211.soft_fail_to_hard()
class TestCase227(TestCase53):
    def test___stringEscaping__2445(self) -> None:
        'string escaping'
        test_215: Test = Test()
        try:
            def build_1967(name_1969: 'str34') -> 'str34':
                t_12204: 'SqlBuilder' = SqlBuilder()
                t_12204.append_safe('select * from hi where name = ')
                t_12204.append_string(name_1969)
                return t_12204.accumulated.to_string()
            def build_wrong_1968(name_1971: 'str34') -> 'str34':
                return str_cat_15572("select * from hi where name = '", name_1971, "'")
            actual_2447: 'str34' = build_1967('world')
            t_12214: 'bool42' = actual_2447 == "select * from hi where name = 'world'"
            def fn_12211() -> 'str34':
                return str_cat_15572('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_2447, ')')
            test_215.assert_(t_12214, fn_12211)
            bobby_tables_1973: 'str34' = "Robert'); drop table hi;--"
            actual_2449: 'str34' = build_1967("Robert'); drop table hi;--")
            t_12218: 'bool42' = actual_2449 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_12210() -> 'str34':
                return str_cat_15572('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_2449, ')')
            test_215.assert_(t_12218, fn_12210)
            def fn_12209() -> 'str34':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_215.assert_(True, fn_12209)
        finally:
            test_215.soft_fail_to_hard()
class TestCase228(TestCase53):
    def test___stringEdgeCases__2453(self) -> None:
        'string edge cases'
        test_216: Test = Test()
        try:
            t_12172: 'SqlBuilder' = SqlBuilder()
            t_12172.append_safe('v = ')
            t_12172.append_string('')
            actual_2454: 'str34' = t_12172.accumulated.to_string()
            t_12178: 'bool42' = actual_2454 == "v = ''"
            def fn_12171() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_2454, ')')
            test_216.assert_(t_12178, fn_12171)
            t_12180: 'SqlBuilder' = SqlBuilder()
            t_12180.append_safe('v = ')
            t_12180.append_string("a''b")
            actual_2457: 'str34' = t_12180.accumulated.to_string()
            t_12186: 'bool42' = actual_2457 == "v = 'a''''b'"
            def fn_12170() -> 'str34':
                return str_cat_15572("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_2457, ')')
            test_216.assert_(t_12186, fn_12170)
            t_12188: 'SqlBuilder' = SqlBuilder()
            t_12188.append_safe('v = ')
            t_12188.append_string('Hello \u4e16\u754c')
            actual_2460: 'str34' = t_12188.accumulated.to_string()
            t_12194: 'bool42' = actual_2460 == "v = 'Hello \u4e16\u754c'"
            def fn_12169() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_2460, ')')
            test_216.assert_(t_12194, fn_12169)
            t_12196: 'SqlBuilder' = SqlBuilder()
            t_12196.append_safe('v = ')
            t_12196.append_string('Line1\nLine2')
            actual_2463: 'str34' = t_12196.accumulated.to_string()
            t_12202: 'bool42' = actual_2463 == "v = 'Line1\nLine2'"
            def fn_12168() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_2463, ')')
            test_216.assert_(t_12202, fn_12168)
        finally:
            test_216.soft_fail_to_hard()
class TestCase229(TestCase53):
    def test___numbersAndBooleans__2466(self) -> None:
        'numbers and booleans'
        test_217: Test = Test()
        try:
            t_12143: 'SqlBuilder' = SqlBuilder()
            t_12143.append_safe('select ')
            t_12143.append_int32(42)
            t_12143.append_safe(', ')
            t_12143.append_int64(43)
            t_12143.append_safe(', ')
            t_12143.append_float64(19.99)
            t_12143.append_safe(', ')
            t_12143.append_boolean(True)
            t_12143.append_safe(', ')
            t_12143.append_boolean(False)
            actual_2467: 'str34' = t_12143.accumulated.to_string()
            t_12157: 'bool42' = actual_2467 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_12142() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_2467, ')')
            test_217.assert_(t_12157, fn_12142)
            t_5738: 'date33'
            t_5738 = date_15604(2024, 12, 25)
            date_1976: 'date33' = t_5738
            t_12159: 'SqlBuilder' = SqlBuilder()
            t_12159.append_safe('insert into t values (')
            t_12159.append_date(date_1976)
            t_12159.append_safe(')')
            actual_2470: 'str34' = t_12159.accumulated.to_string()
            t_12166: 'bool42' = actual_2470 == "insert into t values ('2024-12-25')"
            def fn_12141() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_2470, ')')
            test_217.assert_(t_12166, fn_12141)
        finally:
            test_217.soft_fail_to_hard()
class TestCase230(TestCase53):
    def test___lists__2473(self) -> None:
        'lists'
        test_218: Test = Test()
        try:
            t_12087: 'SqlBuilder' = SqlBuilder()
            t_12087.append_safe('v IN (')
            t_12087.append_string_list(('a', 'b', "c'd"))
            t_12087.append_safe(')')
            actual_2474: 'str34' = t_12087.accumulated.to_string()
            t_12094: 'bool42' = actual_2474 == "v IN ('a', 'b', 'c''d')"
            def fn_12086() -> 'str34':
                return str_cat_15572("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_2474, ')')
            test_218.assert_(t_12094, fn_12086)
            t_12096: 'SqlBuilder' = SqlBuilder()
            t_12096.append_safe('v IN (')
            t_12096.append_int32_list((1, 2, 3))
            t_12096.append_safe(')')
            actual_2477: 'str34' = t_12096.accumulated.to_string()
            t_12103: 'bool42' = actual_2477 == 'v IN (1, 2, 3)'
            def fn_12085() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_2477, ')')
            test_218.assert_(t_12103, fn_12085)
            t_12105: 'SqlBuilder' = SqlBuilder()
            t_12105.append_safe('v IN (')
            t_12105.append_int64_list((1, 2))
            t_12105.append_safe(')')
            actual_2480: 'str34' = t_12105.accumulated.to_string()
            t_12112: 'bool42' = actual_2480 == 'v IN (1, 2)'
            def fn_12084() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_2480, ')')
            test_218.assert_(t_12112, fn_12084)
            t_12114: 'SqlBuilder' = SqlBuilder()
            t_12114.append_safe('v IN (')
            t_12114.append_float64_list((1.0, 2.0))
            t_12114.append_safe(')')
            actual_2483: 'str34' = t_12114.accumulated.to_string()
            t_12121: 'bool42' = actual_2483 == 'v IN (1.0, 2.0)'
            def fn_12083() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_2483, ')')
            test_218.assert_(t_12121, fn_12083)
            t_12123: 'SqlBuilder' = SqlBuilder()
            t_12123.append_safe('v IN (')
            t_12123.append_boolean_list((True, False))
            t_12123.append_safe(')')
            actual_2486: 'str34' = t_12123.accumulated.to_string()
            t_12130: 'bool42' = actual_2486 == 'v IN (TRUE, FALSE)'
            def fn_12082() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_2486, ')')
            test_218.assert_(t_12130, fn_12082)
            t_5710: 'date33'
            t_5710 = date_15604(2024, 1, 1)
            t_5711: 'date33' = t_5710
            t_5712: 'date33'
            t_5712 = date_15604(2024, 12, 25)
            t_5713: 'date33' = t_5712
            dates_1978: 'Sequence38[date33]' = (t_5711, t_5713)
            t_12132: 'SqlBuilder' = SqlBuilder()
            t_12132.append_safe('v IN (')
            t_12132.append_date_list(dates_1978)
            t_12132.append_safe(')')
            actual_2489: 'str34' = t_12132.accumulated.to_string()
            t_12139: 'bool42' = actual_2489 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_12081() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_2489, ')')
            test_218.assert_(t_12139, fn_12081)
        finally:
            test_218.soft_fail_to_hard()
class TestCase231(TestCase53):
    def test___sqlFloat64_naNRendersAsNull__2492(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_219: Test = Test()
        try:
            nan_1980: 'float36'
            nan_1980 = 0.0 / 0.0
            t_12073: 'SqlBuilder' = SqlBuilder()
            t_12073.append_safe('v = ')
            t_12073.append_float64(nan_1980)
            actual_2493: 'str34' = t_12073.accumulated.to_string()
            t_12079: 'bool42' = actual_2493 == 'v = NULL'
            def fn_12072() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_2493, ')')
            test_219.assert_(t_12079, fn_12072)
        finally:
            test_219.soft_fail_to_hard()
class TestCase232(TestCase53):
    def test___sqlFloat64_infinityRendersAsNull__2496(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_220: Test = Test()
        try:
            inf_1982: 'float36'
            inf_1982 = 1.0 / 0.0
            t_12064: 'SqlBuilder' = SqlBuilder()
            t_12064.append_safe('v = ')
            t_12064.append_float64(inf_1982)
            actual_2497: 'str34' = t_12064.accumulated.to_string()
            t_12070: 'bool42' = actual_2497 == 'v = NULL'
            def fn_12063() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_2497, ')')
            test_220.assert_(t_12070, fn_12063)
        finally:
            test_220.soft_fail_to_hard()
class TestCase233(TestCase53):
    def test___sqlFloat64_negativeInfinityRendersAsNull__2500(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_221: Test = Test()
        try:
            ninf_1984: 'float36'
            ninf_1984 = -1.0 / 0.0
            t_12055: 'SqlBuilder' = SqlBuilder()
            t_12055.append_safe('v = ')
            t_12055.append_float64(ninf_1984)
            actual_2501: 'str34' = t_12055.accumulated.to_string()
            t_12061: 'bool42' = actual_2501 == 'v = NULL'
            def fn_12054() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_2501, ')')
            test_221.assert_(t_12061, fn_12054)
        finally:
            test_221.soft_fail_to_hard()
class TestCase234(TestCase53):
    def test___sqlFloat64_normalValuesStillWork__2504(self) -> None:
        'SqlFloat64 normal values still work'
        test_222: Test = Test()
        try:
            t_12030: 'SqlBuilder' = SqlBuilder()
            t_12030.append_safe('v = ')
            t_12030.append_float64(3.14)
            actual_2505: 'str34' = t_12030.accumulated.to_string()
            t_12036: 'bool42' = actual_2505 == 'v = 3.14'
            def fn_12029() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_2505, ')')
            test_222.assert_(t_12036, fn_12029)
            t_12038: 'SqlBuilder' = SqlBuilder()
            t_12038.append_safe('v = ')
            t_12038.append_float64(0.0)
            actual_2508: 'str34' = t_12038.accumulated.to_string()
            t_12044: 'bool42' = actual_2508 == 'v = 0.0'
            def fn_12028() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_2508, ')')
            test_222.assert_(t_12044, fn_12028)
            t_12046: 'SqlBuilder' = SqlBuilder()
            t_12046.append_safe('v = ')
            t_12046.append_float64(-42.5)
            actual_2511: 'str34' = t_12046.accumulated.to_string()
            t_12052: 'bool42' = actual_2511 == 'v = -42.5'
            def fn_12027() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_2511, ')')
            test_222.assert_(t_12052, fn_12027)
        finally:
            test_222.soft_fail_to_hard()
class TestCase235(TestCase53):
    def test___sqlDateRendersWithQuotes__2514(self) -> None:
        'SqlDate renders with quotes'
        test_223: Test = Test()
        try:
            t_5606: 'date33'
            t_5606 = date_15604(2024, 6, 15)
            d_1987: 'date33' = t_5606
            t_12019: 'SqlBuilder' = SqlBuilder()
            t_12019.append_safe('v = ')
            t_12019.append_date(d_1987)
            actual_2515: 'str34' = t_12019.accumulated.to_string()
            t_12025: 'bool42' = actual_2515 == "v = '2024-06-15'"
            def fn_12018() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_2515, ')')
            test_223.assert_(t_12025, fn_12018)
        finally:
            test_223.soft_fail_to_hard()
class TestCase236(TestCase53):
    def test___nesting__2518(self) -> None:
        'nesting'
        test_224: Test = Test()
        try:
            name_1989: 'str34' = 'Someone'
            t_11987: 'SqlBuilder' = SqlBuilder()
            t_11987.append_safe('where p.last_name = ')
            t_11987.append_string('Someone')
            condition_1990: 'SqlFragment' = t_11987.accumulated
            t_11991: 'SqlBuilder' = SqlBuilder()
            t_11991.append_safe('select p.id from person p ')
            t_11991.append_fragment(condition_1990)
            actual_2520: 'str34' = t_11991.accumulated.to_string()
            t_11997: 'bool42' = actual_2520 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_11986() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2520, ')')
            test_224.assert_(t_11997, fn_11986)
            t_11999: 'SqlBuilder' = SqlBuilder()
            t_11999.append_safe('select p.id from person p ')
            t_11999.append_part(condition_1990.to_source())
            actual_2523: 'str34' = t_11999.accumulated.to_string()
            t_12006: 'bool42' = actual_2523 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_11985() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2523, ')')
            test_224.assert_(t_12006, fn_11985)
            parts_1991: 'Sequence38[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_12010: 'SqlBuilder' = SqlBuilder()
            t_12010.append_safe('select ')
            t_12010.append_part_list(parts_1991)
            actual_2526: 'str34' = t_12010.accumulated.to_string()
            t_12016: 'bool42' = actual_2526 == "select 'a''b', 3"
            def fn_11984() -> 'str34':
                return str_cat_15572('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_2526, ')')
            test_224.assert_(t_12016, fn_11984)
        finally:
            test_224.soft_fail_to_hard()
