from temper_std.testing import Test
from builtins import str as str27, bool as bool33, Exception as Exception37, int as int31, float as float38
from unittest import TestCase as TestCase46
from types import MappingProxyType as MappingProxyType32
from typing import Sequence as Sequence29
from datetime import date as date26
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_11486, pair_11490, changeset, Changeset, mapped_has_11463, len_11466, list_get_11474, str_cat_11468, list_for_each_11460, SqlFragment, from_, Query, SqlBuilder, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, update, UpdateQuery, SqlBoolean, delete_from, DeleteQuery, NullsFirst, NullsLast, ForUpdate, ForShare, date_11493, SqlPart
def csid_544(name_689: 'str27') -> 'SafeIdentifier':
    t_6343: 'SafeIdentifier'
    t_6343 = safe_identifier(name_689)
    return t_6343
def user_table_545() -> 'TableDef':
    return TableDef(csid_544('users'), (FieldDef(csid_544('name'), StringField(), False), FieldDef(csid_544('email'), StringField(), False), FieldDef(csid_544('age'), IntField(), True), FieldDef(csid_544('score'), FloatField(), True), FieldDef(csid_544('active'), BoolField(), True)))
class TestCase45(TestCase46):
    def test___castWhitelistsAllowedFields__1645(self) -> None:
        'cast whitelists allowed fields'
        test_24: Test = Test()
        try:
            params_693: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'Alice'), pair_11490('email', 'alice@example.com'), pair_11490('admin', 'true')))
            t_11177: 'TableDef' = user_table_545()
            t_11178: 'SafeIdentifier' = csid_544('name')
            t_11179: 'SafeIdentifier' = csid_544('email')
            cs_694: 'Changeset' = changeset(t_11177, params_693).cast((t_11178, t_11179))
            t_11182: 'bool33' = mapped_has_11463(cs_694.changes, 'name')
            def fn_11172() -> 'str27':
                return 'name should be in changes'
            test_24.assert_(t_11182, fn_11172)
            t_11186: 'bool33' = mapped_has_11463(cs_694.changes, 'email')
            def fn_11171() -> 'str27':
                return 'email should be in changes'
            test_24.assert_(t_11186, fn_11171)
            t_11192: 'bool33' = not mapped_has_11463(cs_694.changes, 'admin')
            def fn_11170() -> 'str27':
                return 'admin must be dropped (not in whitelist)'
            test_24.assert_(t_11192, fn_11170)
            t_11194: 'bool33' = cs_694.is_valid
            def fn_11169() -> 'str27':
                return 'should still be valid'
            test_24.assert_(t_11194, fn_11169)
        finally:
            test_24.soft_fail_to_hard()
class TestCase47(TestCase46):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__1646(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_25: Test = Test()
        try:
            params_696: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'Alice'), pair_11490('email', 'alice@example.com')))
            t_11155: 'TableDef' = user_table_545()
            t_11156: 'SafeIdentifier' = csid_544('name')
            cs_697: 'Changeset' = changeset(t_11155, params_696).cast((t_11156,)).cast((csid_544('email'),))
            t_11163: 'bool33' = not mapped_has_11463(cs_697.changes, 'name')
            def fn_11151() -> 'str27':
                return 'name must be excluded by second cast'
            test_25.assert_(t_11163, fn_11151)
            t_11166: 'bool33' = mapped_has_11463(cs_697.changes, 'email')
            def fn_11150() -> 'str27':
                return 'email should be present'
            test_25.assert_(t_11166, fn_11150)
        finally:
            test_25.soft_fail_to_hard()
class TestCase48(TestCase46):
    def test___castIgnoresEmptyStringValues__1647(self) -> None:
        'cast ignores empty string values'
        test_26: Test = Test()
        try:
            params_699: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', ''), pair_11490('email', 'bob@example.com')))
            t_11137: 'TableDef' = user_table_545()
            t_11138: 'SafeIdentifier' = csid_544('name')
            t_11139: 'SafeIdentifier' = csid_544('email')
            cs_700: 'Changeset' = changeset(t_11137, params_699).cast((t_11138, t_11139))
            t_11144: 'bool33' = not mapped_has_11463(cs_700.changes, 'name')
            def fn_11133() -> 'str27':
                return 'empty name should not be in changes'
            test_26.assert_(t_11144, fn_11133)
            t_11147: 'bool33' = mapped_has_11463(cs_700.changes, 'email')
            def fn_11132() -> 'str27':
                return 'email should be in changes'
            test_26.assert_(t_11147, fn_11132)
        finally:
            test_26.soft_fail_to_hard()
class TestCase49(TestCase46):
    def test___validateRequiredPassesWhenFieldPresent__1648(self) -> None:
        'validateRequired passes when field present'
        test_27: Test = Test()
        try:
            params_702: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'Alice'),))
            t_11119: 'TableDef' = user_table_545()
            t_11120: 'SafeIdentifier' = csid_544('name')
            cs_703: 'Changeset' = changeset(t_11119, params_702).cast((t_11120,)).validate_required((csid_544('name'),))
            t_11124: 'bool33' = cs_703.is_valid
            def fn_11116() -> 'str27':
                return 'should be valid'
            test_27.assert_(t_11124, fn_11116)
            t_11130: 'bool33' = len_11466(cs_703.errors) == 0
            def fn_11115() -> 'str27':
                return 'no errors expected'
            test_27.assert_(t_11130, fn_11115)
        finally:
            test_27.soft_fail_to_hard()
class TestCase50(TestCase46):
    def test___validateRequiredFailsWhenFieldMissing__1649(self) -> None:
        'validateRequired fails when field missing'
        test_28: Test = Test()
        try:
            params_705: 'MappingProxyType32[str27, str27]' = map_constructor_11486(())
            t_11095: 'TableDef' = user_table_545()
            t_11096: 'SafeIdentifier' = csid_544('name')
            cs_706: 'Changeset' = changeset(t_11095, params_705).cast((t_11096,)).validate_required((csid_544('name'),))
            t_11102: 'bool33' = not cs_706.is_valid
            def fn_11093() -> 'str27':
                return 'should be invalid'
            test_28.assert_(t_11102, fn_11093)
            t_11107: 'bool33' = len_11466(cs_706.errors) == 1
            def fn_11092() -> 'str27':
                return 'should have one error'
            test_28.assert_(t_11107, fn_11092)
            t_11113: 'bool33' = list_get_11474(cs_706.errors, 0).field == 'name'
            def fn_11091() -> 'str27':
                return 'error should name the field'
            test_28.assert_(t_11113, fn_11091)
        finally:
            test_28.soft_fail_to_hard()
class TestCase51(TestCase46):
    def test___validateLengthPassesWithinRange__1650(self) -> None:
        'validateLength passes within range'
        test_29: Test = Test()
        try:
            params_708: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'Alice'),))
            t_11083: 'TableDef' = user_table_545()
            t_11084: 'SafeIdentifier' = csid_544('name')
            cs_709: 'Changeset' = changeset(t_11083, params_708).cast((t_11084,)).validate_length(csid_544('name'), 2, 50)
            t_11088: 'bool33' = cs_709.is_valid
            def fn_11080() -> 'str27':
                return 'should be valid'
            test_29.assert_(t_11088, fn_11080)
        finally:
            test_29.soft_fail_to_hard()
class TestCase52(TestCase46):
    def test___validateLengthFailsWhenTooShort__1651(self) -> None:
        'validateLength fails when too short'
        test_30: Test = Test()
        try:
            params_711: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'A'),))
            t_11071: 'TableDef' = user_table_545()
            t_11072: 'SafeIdentifier' = csid_544('name')
            cs_712: 'Changeset' = changeset(t_11071, params_711).cast((t_11072,)).validate_length(csid_544('name'), 2, 50)
            t_11078: 'bool33' = not cs_712.is_valid
            def fn_11068() -> 'str27':
                return 'should be invalid'
            test_30.assert_(t_11078, fn_11068)
        finally:
            test_30.soft_fail_to_hard()
class TestCase53(TestCase46):
    def test___validateLengthFailsWhenTooLong__1652(self) -> None:
        'validateLength fails when too long'
        test_31: Test = Test()
        try:
            params_714: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_11059: 'TableDef' = user_table_545()
            t_11060: 'SafeIdentifier' = csid_544('name')
            cs_715: 'Changeset' = changeset(t_11059, params_714).cast((t_11060,)).validate_length(csid_544('name'), 2, 10)
            t_11066: 'bool33' = not cs_715.is_valid
            def fn_11056() -> 'str27':
                return 'should be invalid'
            test_31.assert_(t_11066, fn_11056)
        finally:
            test_31.soft_fail_to_hard()
class TestCase54(TestCase46):
    def test___validateIntPassesForValidInteger__1653(self) -> None:
        'validateInt passes for valid integer'
        test_32: Test = Test()
        try:
            params_717: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('age', '30'),))
            t_11048: 'TableDef' = user_table_545()
            t_11049: 'SafeIdentifier' = csid_544('age')
            cs_718: 'Changeset' = changeset(t_11048, params_717).cast((t_11049,)).validate_int(csid_544('age'))
            t_11053: 'bool33' = cs_718.is_valid
            def fn_11045() -> 'str27':
                return 'should be valid'
            test_32.assert_(t_11053, fn_11045)
        finally:
            test_32.soft_fail_to_hard()
class TestCase55(TestCase46):
    def test___validateIntFailsForNonInteger__1654(self) -> None:
        'validateInt fails for non-integer'
        test_33: Test = Test()
        try:
            params_720: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('age', 'not-a-number'),))
            t_11036: 'TableDef' = user_table_545()
            t_11037: 'SafeIdentifier' = csid_544('age')
            cs_721: 'Changeset' = changeset(t_11036, params_720).cast((t_11037,)).validate_int(csid_544('age'))
            t_11043: 'bool33' = not cs_721.is_valid
            def fn_11033() -> 'str27':
                return 'should be invalid'
            test_33.assert_(t_11043, fn_11033)
        finally:
            test_33.soft_fail_to_hard()
class TestCase56(TestCase46):
    def test___validateFloatPassesForValidFloat__1655(self) -> None:
        'validateFloat passes for valid float'
        test_34: Test = Test()
        try:
            params_723: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('score', '9.5'),))
            t_11025: 'TableDef' = user_table_545()
            t_11026: 'SafeIdentifier' = csid_544('score')
            cs_724: 'Changeset' = changeset(t_11025, params_723).cast((t_11026,)).validate_float(csid_544('score'))
            t_11030: 'bool33' = cs_724.is_valid
            def fn_11022() -> 'str27':
                return 'should be valid'
            test_34.assert_(t_11030, fn_11022)
        finally:
            test_34.soft_fail_to_hard()
class TestCase57(TestCase46):
    def test___validateInt64_passesForValid64_bitInteger__1656(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_35: Test = Test()
        try:
            params_726: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('age', '9999999999'),))
            t_11014: 'TableDef' = user_table_545()
            t_11015: 'SafeIdentifier' = csid_544('age')
            cs_727: 'Changeset' = changeset(t_11014, params_726).cast((t_11015,)).validate_int64(csid_544('age'))
            t_11019: 'bool33' = cs_727.is_valid
            def fn_11011() -> 'str27':
                return 'should be valid'
            test_35.assert_(t_11019, fn_11011)
        finally:
            test_35.soft_fail_to_hard()
class TestCase58(TestCase46):
    def test___validateInt64_failsForNonInteger__1657(self) -> None:
        'validateInt64 fails for non-integer'
        test_36: Test = Test()
        try:
            params_729: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('age', 'not-a-number'),))
            t_11002: 'TableDef' = user_table_545()
            t_11003: 'SafeIdentifier' = csid_544('age')
            cs_730: 'Changeset' = changeset(t_11002, params_729).cast((t_11003,)).validate_int64(csid_544('age'))
            t_11009: 'bool33' = not cs_730.is_valid
            def fn_10999() -> 'str27':
                return 'should be invalid'
            test_36.assert_(t_11009, fn_10999)
        finally:
            test_36.soft_fail_to_hard()
class TestCase59(TestCase46):
    def test___validateBoolAcceptsTrue1_yesOn__1658(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_37: Test = Test()
        try:
            def fn_10996(v_732: 'str27') -> 'None':
                params_733: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('active', v_732),))
                t_10988: 'TableDef' = user_table_545()
                t_10989: 'SafeIdentifier' = csid_544('active')
                cs_734: 'Changeset' = changeset(t_10988, params_733).cast((t_10989,)).validate_bool(csid_544('active'))
                t_10993: 'bool33' = cs_734.is_valid
                def fn_10985() -> 'str27':
                    return str_cat_11468('should accept: ', v_732)
                test_37.assert_(t_10993, fn_10985)
            list_for_each_11460(('true', '1', 'yes', 'on'), fn_10996)
        finally:
            test_37.soft_fail_to_hard()
class TestCase60(TestCase46):
    def test___validateBoolAcceptsFalse0_noOff__1659(self) -> None:
        'validateBool accepts false/0/no/off'
        test_38: Test = Test()
        try:
            def fn_10982(v_736: 'str27') -> 'None':
                params_737: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('active', v_736),))
                t_10974: 'TableDef' = user_table_545()
                t_10975: 'SafeIdentifier' = csid_544('active')
                cs_738: 'Changeset' = changeset(t_10974, params_737).cast((t_10975,)).validate_bool(csid_544('active'))
                t_10979: 'bool33' = cs_738.is_valid
                def fn_10971() -> 'str27':
                    return str_cat_11468('should accept: ', v_736)
                test_38.assert_(t_10979, fn_10971)
            list_for_each_11460(('false', '0', 'no', 'off'), fn_10982)
        finally:
            test_38.soft_fail_to_hard()
class TestCase61(TestCase46):
    def test___validateBoolRejectsAmbiguousValues__1660(self) -> None:
        'validateBool rejects ambiguous values'
        test_39: Test = Test()
        try:
            def fn_10968(v_740: 'str27') -> 'None':
                params_741: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('active', v_740),))
                t_10959: 'TableDef' = user_table_545()
                t_10960: 'SafeIdentifier' = csid_544('active')
                cs_742: 'Changeset' = changeset(t_10959, params_741).cast((t_10960,)).validate_bool(csid_544('active'))
                t_10966: 'bool33' = not cs_742.is_valid
                def fn_10956() -> 'str27':
                    return str_cat_11468('should reject ambiguous: ', v_740)
                test_39.assert_(t_10966, fn_10956)
            list_for_each_11460(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_10968)
        finally:
            test_39.soft_fail_to_hard()
class TestCase62(TestCase46):
    def test___toInsertSqlEscapesBobbyTables__1661(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_40: Test = Test()
        try:
            params_744: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', "Robert'); DROP TABLE users;--"), pair_11490('email', 'bobby@evil.com')))
            t_10944: 'TableDef' = user_table_545()
            t_10945: 'SafeIdentifier' = csid_544('name')
            t_10946: 'SafeIdentifier' = csid_544('email')
            cs_745: 'Changeset' = changeset(t_10944, params_744).cast((t_10945, t_10946)).validate_required((csid_544('name'), csid_544('email')))
            t_6144: 'SqlFragment'
            t_6144 = cs_745.to_insert_sql()
            sql_frag_746: 'SqlFragment' = t_6144
            s_747: 'str27' = sql_frag_746.to_string()
            t_10953: 'bool33' = s_747.find("''") >= 0
            def fn_10940() -> 'str27':
                return str_cat_11468('single quote must be doubled: ', s_747)
            test_40.assert_(t_10953, fn_10940)
        finally:
            test_40.soft_fail_to_hard()
class TestCase63(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForStringField__1662(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_41: Test = Test()
        try:
            params_749: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'Alice'), pair_11490('email', 'a@example.com')))
            t_10924: 'TableDef' = user_table_545()
            t_10925: 'SafeIdentifier' = csid_544('name')
            t_10926: 'SafeIdentifier' = csid_544('email')
            cs_750: 'Changeset' = changeset(t_10924, params_749).cast((t_10925, t_10926)).validate_required((csid_544('name'), csid_544('email')))
            t_6123: 'SqlFragment'
            t_6123 = cs_750.to_insert_sql()
            sql_frag_751: 'SqlFragment' = t_6123
            s_752: 'str27' = sql_frag_751.to_string()
            t_10933: 'bool33' = s_752.find('INSERT INTO users') >= 0
            def fn_10920() -> 'str27':
                return str_cat_11468('has INSERT INTO: ', s_752)
            test_41.assert_(t_10933, fn_10920)
            t_10937: 'bool33' = s_752.find("'Alice'") >= 0
            def fn_10919() -> 'str27':
                return str_cat_11468('has quoted name: ', s_752)
            test_41.assert_(t_10937, fn_10919)
        finally:
            test_41.soft_fail_to_hard()
class TestCase64(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForIntField__1663(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_42: Test = Test()
        try:
            params_754: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'Bob'), pair_11490('email', 'b@example.com'), pair_11490('age', '25')))
            t_10906: 'TableDef' = user_table_545()
            t_10907: 'SafeIdentifier' = csid_544('name')
            t_10908: 'SafeIdentifier' = csid_544('email')
            t_10909: 'SafeIdentifier' = csid_544('age')
            cs_755: 'Changeset' = changeset(t_10906, params_754).cast((t_10907, t_10908, t_10909)).validate_required((csid_544('name'), csid_544('email')))
            t_6106: 'SqlFragment'
            t_6106 = cs_755.to_insert_sql()
            sql_frag_756: 'SqlFragment' = t_6106
            s_757: 'str27' = sql_frag_756.to_string()
            t_10916: 'bool33' = s_757.find('25') >= 0
            def fn_10901() -> 'str27':
                return str_cat_11468('age rendered unquoted: ', s_757)
            test_42.assert_(t_10916, fn_10901)
        finally:
            test_42.soft_fail_to_hard()
class TestCase65(TestCase46):
    def test___toInsertSqlBubblesOnInvalidChangeset__1664(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_43: Test = Test()
        try:
            params_759: 'MappingProxyType32[str27, str27]' = map_constructor_11486(())
            t_10894: 'TableDef' = user_table_545()
            t_10895: 'SafeIdentifier' = csid_544('name')
            cs_760: 'Changeset' = changeset(t_10894, params_759).cast((t_10895,)).validate_required((csid_544('name'),))
            did_bubble_761: 'bool33'
            try:
                cs_760.to_insert_sql()
                did_bubble_761 = False
            except Exception37:
                did_bubble_761 = True
            def fn_10892() -> 'str27':
                return 'invalid changeset should bubble'
            test_43.assert_(did_bubble_761, fn_10892)
        finally:
            test_43.soft_fail_to_hard()
class TestCase66(TestCase46):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__1665(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_44: Test = Test()
        try:
            strict_table_763: 'TableDef' = TableDef(csid_544('posts'), (FieldDef(csid_544('title'), StringField(), False), FieldDef(csid_544('body'), StringField(), True)))
            params_764: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('body', 'hello'),))
            t_10885: 'SafeIdentifier' = csid_544('body')
            cs_765: 'Changeset' = changeset(strict_table_763, params_764).cast((t_10885,))
            t_10887: 'bool33' = cs_765.is_valid
            def fn_10874() -> 'str27':
                return 'changeset should appear valid (no explicit validation run)'
            test_44.assert_(t_10887, fn_10874)
            did_bubble_766: 'bool33'
            try:
                cs_765.to_insert_sql()
                did_bubble_766 = False
            except Exception37:
                did_bubble_766 = True
            def fn_10873() -> 'str27':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_44.assert_(did_bubble_766, fn_10873)
        finally:
            test_44.soft_fail_to_hard()
class TestCase67(TestCase46):
    def test___toUpdateSqlProducesCorrectSql__1666(self) -> None:
        'toUpdateSql produces correct SQL'
        test_45: Test = Test()
        try:
            params_768: 'MappingProxyType32[str27, str27]' = map_constructor_11486((pair_11490('name', 'Bob'),))
            t_10864: 'TableDef' = user_table_545()
            t_10865: 'SafeIdentifier' = csid_544('name')
            cs_769: 'Changeset' = changeset(t_10864, params_768).cast((t_10865,)).validate_required((csid_544('name'),))
            t_6066: 'SqlFragment'
            t_6066 = cs_769.to_update_sql(42)
            sql_frag_770: 'SqlFragment' = t_6066
            s_771: 'str27' = sql_frag_770.to_string()
            t_10871: 'bool33' = s_771 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_10861() -> 'str27':
                return str_cat_11468('got: ', s_771)
            test_45.assert_(t_10871, fn_10861)
        finally:
            test_45.soft_fail_to_hard()
class TestCase68(TestCase46):
    def test___toUpdateSqlBubblesOnInvalidChangeset__1667(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_46: Test = Test()
        try:
            params_773: 'MappingProxyType32[str27, str27]' = map_constructor_11486(())
            t_10854: 'TableDef' = user_table_545()
            t_10855: 'SafeIdentifier' = csid_544('name')
            cs_774: 'Changeset' = changeset(t_10854, params_773).cast((t_10855,)).validate_required((csid_544('name'),))
            did_bubble_775: 'bool33'
            try:
                cs_774.to_update_sql(1)
                did_bubble_775 = False
            except Exception37:
                did_bubble_775 = True
            def fn_10852() -> 'str27':
                return 'invalid changeset should bubble'
            test_46.assert_(did_bubble_775, fn_10852)
        finally:
            test_46.soft_fail_to_hard()
def sid_546(name_1120: 'str27') -> 'SafeIdentifier':
    t_5526: 'SafeIdentifier'
    t_5526 = safe_identifier(name_1120)
    return t_5526
class TestCase69(TestCase46):
    def test___bareFromProducesSelect__1749(self) -> None:
        'bare from produces SELECT *'
        test_47: Test = Test()
        try:
            q_1123: 'Query' = from_(sid_546('users'))
            t_10337: 'bool33' = q_1123.to_sql().to_string() == 'SELECT * FROM users'
            def fn_10332() -> 'str27':
                return 'bare query'
            test_47.assert_(t_10337, fn_10332)
        finally:
            test_47.soft_fail_to_hard()
class TestCase70(TestCase46):
    def test___selectRestrictsColumns__1750(self) -> None:
        'select restricts columns'
        test_48: Test = Test()
        try:
            t_10323: 'SafeIdentifier' = sid_546('users')
            t_10324: 'SafeIdentifier' = sid_546('id')
            t_10325: 'SafeIdentifier' = sid_546('name')
            q_1125: 'Query' = from_(t_10323).select((t_10324, t_10325))
            t_10330: 'bool33' = q_1125.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_10322() -> 'str27':
                return 'select columns'
            test_48.assert_(t_10330, fn_10322)
        finally:
            test_48.soft_fail_to_hard()
class TestCase71(TestCase46):
    def test___whereAddsConditionWithIntValue__1751(self) -> None:
        'where adds condition with int value'
        test_49: Test = Test()
        try:
            t_10311: 'SafeIdentifier' = sid_546('users')
            t_10312: 'SqlBuilder' = SqlBuilder()
            t_10312.append_safe('age > ')
            t_10312.append_int32(18)
            t_10315: 'SqlFragment' = t_10312.accumulated
            q_1127: 'Query' = from_(t_10311).where(t_10315)
            t_10320: 'bool33' = q_1127.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_10310() -> 'str27':
                return 'where int'
            test_49.assert_(t_10320, fn_10310)
        finally:
            test_49.soft_fail_to_hard()
class TestCase72(TestCase46):
    def test___whereAddsConditionWithBoolValue__1753(self) -> None:
        'where adds condition with bool value'
        test_50: Test = Test()
        try:
            t_10299: 'SafeIdentifier' = sid_546('users')
            t_10300: 'SqlBuilder' = SqlBuilder()
            t_10300.append_safe('active = ')
            t_10300.append_boolean(True)
            t_10303: 'SqlFragment' = t_10300.accumulated
            q_1129: 'Query' = from_(t_10299).where(t_10303)
            t_10308: 'bool33' = q_1129.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_10298() -> 'str27':
                return 'where bool'
            test_50.assert_(t_10308, fn_10298)
        finally:
            test_50.soft_fail_to_hard()
class TestCase73(TestCase46):
    def test___chainedWhereUsesAnd__1755(self) -> None:
        'chained where uses AND'
        test_51: Test = Test()
        try:
            t_10282: 'SafeIdentifier' = sid_546('users')
            t_10283: 'SqlBuilder' = SqlBuilder()
            t_10283.append_safe('age > ')
            t_10283.append_int32(18)
            t_10286: 'SqlFragment' = t_10283.accumulated
            t_10287: 'Query' = from_(t_10282).where(t_10286)
            t_10288: 'SqlBuilder' = SqlBuilder()
            t_10288.append_safe('active = ')
            t_10288.append_boolean(True)
            q_1131: 'Query' = t_10287.where(t_10288.accumulated)
            t_10296: 'bool33' = q_1131.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_10281() -> 'str27':
                return 'chained where'
            test_51.assert_(t_10296, fn_10281)
        finally:
            test_51.soft_fail_to_hard()
class TestCase74(TestCase46):
    def test___orderByAsc__1758(self) -> None:
        'orderBy ASC'
        test_52: Test = Test()
        try:
            t_10273: 'SafeIdentifier' = sid_546('users')
            t_10274: 'SafeIdentifier' = sid_546('name')
            q_1133: 'Query' = from_(t_10273).order_by(t_10274, True)
            t_10279: 'bool33' = q_1133.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_10272() -> 'str27':
                return 'order asc'
            test_52.assert_(t_10279, fn_10272)
        finally:
            test_52.soft_fail_to_hard()
class TestCase75(TestCase46):
    def test___orderByDesc__1759(self) -> None:
        'orderBy DESC'
        test_53: Test = Test()
        try:
            t_10264: 'SafeIdentifier' = sid_546('users')
            t_10265: 'SafeIdentifier' = sid_546('created_at')
            q_1135: 'Query' = from_(t_10264).order_by(t_10265, False)
            t_10270: 'bool33' = q_1135.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_10263() -> 'str27':
                return 'order desc'
            test_53.assert_(t_10270, fn_10263)
        finally:
            test_53.soft_fail_to_hard()
class TestCase76(TestCase46):
    def test___limitAndOffset__1760(self) -> None:
        'limit and offset'
        test_54: Test = Test()
        try:
            t_5460: 'Query'
            t_5460 = from_(sid_546('users')).limit(10)
            t_5461: 'Query'
            t_5461 = t_5460.offset(20)
            q_1137: 'Query' = t_5461
            t_10261: 'bool33' = q_1137.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_10256() -> 'str27':
                return 'limit/offset'
            test_54.assert_(t_10261, fn_10256)
        finally:
            test_54.soft_fail_to_hard()
class TestCase77(TestCase46):
    def test___limitBubblesOnNegative__1761(self) -> None:
        'limit bubbles on negative'
        test_55: Test = Test()
        try:
            did_bubble_1139: 'bool33'
            try:
                from_(sid_546('users')).limit(-1)
                did_bubble_1139 = False
            except Exception37:
                did_bubble_1139 = True
            def fn_10252() -> 'str27':
                return 'negative limit should bubble'
            test_55.assert_(did_bubble_1139, fn_10252)
        finally:
            test_55.soft_fail_to_hard()
class TestCase78(TestCase46):
    def test___offsetBubblesOnNegative__1762(self) -> None:
        'offset bubbles on negative'
        test_56: Test = Test()
        try:
            did_bubble_1141: 'bool33'
            try:
                from_(sid_546('users')).offset(-1)
                did_bubble_1141 = False
            except Exception37:
                did_bubble_1141 = True
            def fn_10248() -> 'str27':
                return 'negative offset should bubble'
            test_56.assert_(did_bubble_1141, fn_10248)
        finally:
            test_56.soft_fail_to_hard()
class TestCase79(TestCase46):
    def test___complexComposedQuery__1763(self) -> None:
        'complex composed query'
        test_57: Test = Test()
        try:
            min_age_1143: 'int31' = 21
            t_10226: 'SafeIdentifier' = sid_546('users')
            t_10227: 'SafeIdentifier' = sid_546('id')
            t_10228: 'SafeIdentifier' = sid_546('name')
            t_10229: 'SafeIdentifier' = sid_546('email')
            t_10230: 'Query' = from_(t_10226).select((t_10227, t_10228, t_10229))
            t_10231: 'SqlBuilder' = SqlBuilder()
            t_10231.append_safe('age >= ')
            t_10231.append_int32(21)
            t_10235: 'Query' = t_10230.where(t_10231.accumulated)
            t_10236: 'SqlBuilder' = SqlBuilder()
            t_10236.append_safe('active = ')
            t_10236.append_boolean(True)
            t_5446: 'Query'
            t_5446 = t_10235.where(t_10236.accumulated).order_by(sid_546('name'), True).limit(25)
            t_5447: 'Query'
            t_5447 = t_5446.offset(0)
            q_1144: 'Query' = t_5447
            t_10246: 'bool33' = q_1144.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_10225() -> 'str27':
                return 'complex query'
            test_57.assert_(t_10246, fn_10225)
        finally:
            test_57.soft_fail_to_hard()
class TestCase80(TestCase46):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__1766(self) -> None:
        'safeToSql applies default limit when none set'
        test_58: Test = Test()
        try:
            q_1146: 'Query' = from_(sid_546('users'))
            t_5423: 'SqlFragment'
            t_5423 = q_1146.safe_to_sql(100)
            t_5424: 'SqlFragment' = t_5423
            s_1147: 'str27' = t_5424.to_string()
            t_10223: 'bool33' = s_1147 == 'SELECT * FROM users LIMIT 100'
            def fn_10219() -> 'str27':
                return str_cat_11468('should have limit: ', s_1147)
            test_58.assert_(t_10223, fn_10219)
        finally:
            test_58.soft_fail_to_hard()
class TestCase81(TestCase46):
    def test___safeToSqlRespectsExplicitLimit__1767(self) -> None:
        'safeToSql respects explicit limit'
        test_59: Test = Test()
        try:
            t_5415: 'Query'
            t_5415 = from_(sid_546('users')).limit(5)
            q_1149: 'Query' = t_5415
            t_5418: 'SqlFragment'
            t_5418 = q_1149.safe_to_sql(100)
            t_5419: 'SqlFragment' = t_5418
            s_1150: 'str27' = t_5419.to_string()
            t_10217: 'bool33' = s_1150 == 'SELECT * FROM users LIMIT 5'
            def fn_10213() -> 'str27':
                return str_cat_11468('explicit limit preserved: ', s_1150)
            test_59.assert_(t_10217, fn_10213)
        finally:
            test_59.soft_fail_to_hard()
class TestCase82(TestCase46):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__1768(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_60: Test = Test()
        try:
            did_bubble_1152: 'bool33'
            try:
                from_(sid_546('users')).safe_to_sql(-1)
                did_bubble_1152 = False
            except Exception37:
                did_bubble_1152 = True
            def fn_10209() -> 'str27':
                return 'negative defaultLimit should bubble'
            test_60.assert_(did_bubble_1152, fn_10209)
        finally:
            test_60.soft_fail_to_hard()
class TestCase83(TestCase46):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__1769(self) -> None:
        'where with injection attempt in string value is escaped'
        test_61: Test = Test()
        try:
            evil_1154: 'str27' = "'; DROP TABLE users; --"
            t_10193: 'SafeIdentifier' = sid_546('users')
            t_10194: 'SqlBuilder' = SqlBuilder()
            t_10194.append_safe('name = ')
            t_10194.append_string("'; DROP TABLE users; --")
            t_10197: 'SqlFragment' = t_10194.accumulated
            q_1155: 'Query' = from_(t_10193).where(t_10197)
            s_1156: 'str27' = q_1155.to_sql().to_string()
            t_10202: 'bool33' = s_1156.find("''") >= 0
            def fn_10192() -> 'str27':
                return str_cat_11468('quotes must be doubled: ', s_1156)
            test_61.assert_(t_10202, fn_10192)
            t_10206: 'bool33' = s_1156.find('SELECT * FROM users WHERE name =') >= 0
            def fn_10191() -> 'str27':
                return str_cat_11468('structure intact: ', s_1156)
            test_61.assert_(t_10206, fn_10191)
        finally:
            test_61.soft_fail_to_hard()
class TestCase84(TestCase46):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__1771(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_62: Test = Test()
        try:
            attack_1158: 'str27' = 'users; DROP TABLE users; --'
            did_bubble_1159: 'bool33'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_1159 = False
            except Exception37:
                did_bubble_1159 = True
            def fn_10188() -> 'str27':
                return 'metacharacter-containing name must be rejected at construction'
            test_62.assert_(did_bubble_1159, fn_10188)
        finally:
            test_62.soft_fail_to_hard()
class TestCase85(TestCase46):
    def test___innerJoinProducesInnerJoin__1772(self) -> None:
        'innerJoin produces INNER JOIN'
        test_63: Test = Test()
        try:
            t_10177: 'SafeIdentifier' = sid_546('users')
            t_10178: 'SafeIdentifier' = sid_546('orders')
            t_10179: 'SqlBuilder' = SqlBuilder()
            t_10179.append_safe('users.id = orders.user_id')
            t_10181: 'SqlFragment' = t_10179.accumulated
            q_1161: 'Query' = from_(t_10177).inner_join(t_10178, t_10181)
            t_10186: 'bool33' = q_1161.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_10176() -> 'str27':
                return 'inner join'
            test_63.assert_(t_10186, fn_10176)
        finally:
            test_63.soft_fail_to_hard()
class TestCase86(TestCase46):
    def test___leftJoinProducesLeftJoin__1774(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_64: Test = Test()
        try:
            t_10165: 'SafeIdentifier' = sid_546('users')
            t_10166: 'SafeIdentifier' = sid_546('profiles')
            t_10167: 'SqlBuilder' = SqlBuilder()
            t_10167.append_safe('users.id = profiles.user_id')
            t_10169: 'SqlFragment' = t_10167.accumulated
            q_1163: 'Query' = from_(t_10165).left_join(t_10166, t_10169)
            t_10174: 'bool33' = q_1163.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_10164() -> 'str27':
                return 'left join'
            test_64.assert_(t_10174, fn_10164)
        finally:
            test_64.soft_fail_to_hard()
class TestCase87(TestCase46):
    def test___rightJoinProducesRightJoin__1776(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_65: Test = Test()
        try:
            t_10153: 'SafeIdentifier' = sid_546('orders')
            t_10154: 'SafeIdentifier' = sid_546('users')
            t_10155: 'SqlBuilder' = SqlBuilder()
            t_10155.append_safe('orders.user_id = users.id')
            t_10157: 'SqlFragment' = t_10155.accumulated
            q_1165: 'Query' = from_(t_10153).right_join(t_10154, t_10157)
            t_10162: 'bool33' = q_1165.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_10152() -> 'str27':
                return 'right join'
            test_65.assert_(t_10162, fn_10152)
        finally:
            test_65.soft_fail_to_hard()
class TestCase88(TestCase46):
    def test___fullJoinProducesFullOuterJoin__1778(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_66: Test = Test()
        try:
            t_10141: 'SafeIdentifier' = sid_546('users')
            t_10142: 'SafeIdentifier' = sid_546('orders')
            t_10143: 'SqlBuilder' = SqlBuilder()
            t_10143.append_safe('users.id = orders.user_id')
            t_10145: 'SqlFragment' = t_10143.accumulated
            q_1167: 'Query' = from_(t_10141).full_join(t_10142, t_10145)
            t_10150: 'bool33' = q_1167.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_10140() -> 'str27':
                return 'full join'
            test_66.assert_(t_10150, fn_10140)
        finally:
            test_66.soft_fail_to_hard()
class TestCase89(TestCase46):
    def test___chainedJoins__1780(self) -> None:
        'chained joins'
        test_67: Test = Test()
        try:
            t_10124: 'SafeIdentifier' = sid_546('users')
            t_10125: 'SafeIdentifier' = sid_546('orders')
            t_10126: 'SqlBuilder' = SqlBuilder()
            t_10126.append_safe('users.id = orders.user_id')
            t_10128: 'SqlFragment' = t_10126.accumulated
            t_10129: 'Query' = from_(t_10124).inner_join(t_10125, t_10128)
            t_10130: 'SafeIdentifier' = sid_546('profiles')
            t_10131: 'SqlBuilder' = SqlBuilder()
            t_10131.append_safe('users.id = profiles.user_id')
            q_1169: 'Query' = t_10129.left_join(t_10130, t_10131.accumulated)
            t_10138: 'bool33' = q_1169.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_10123() -> 'str27':
                return 'chained joins'
            test_67.assert_(t_10138, fn_10123)
        finally:
            test_67.soft_fail_to_hard()
class TestCase90(TestCase46):
    def test___joinWithWhereAndOrderBy__1783(self) -> None:
        'join with where and orderBy'
        test_68: Test = Test()
        try:
            t_10105: 'SafeIdentifier' = sid_546('users')
            t_10106: 'SafeIdentifier' = sid_546('orders')
            t_10107: 'SqlBuilder' = SqlBuilder()
            t_10107.append_safe('users.id = orders.user_id')
            t_10109: 'SqlFragment' = t_10107.accumulated
            t_10110: 'Query' = from_(t_10105).inner_join(t_10106, t_10109)
            t_10111: 'SqlBuilder' = SqlBuilder()
            t_10111.append_safe('orders.total > ')
            t_10111.append_int32(100)
            t_5330: 'Query'
            t_5330 = t_10110.where(t_10111.accumulated).order_by(sid_546('name'), True).limit(10)
            q_1171: 'Query' = t_5330
            t_10121: 'bool33' = q_1171.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_10104() -> 'str27':
                return 'join with where/order/limit'
            test_68.assert_(t_10121, fn_10104)
        finally:
            test_68.soft_fail_to_hard()
class TestCase91(TestCase46):
    def test___colHelperProducesQualifiedReference__1786(self) -> None:
        'col helper produces qualified reference'
        test_69: Test = Test()
        try:
            c_1173: 'SqlFragment' = col(sid_546('users'), sid_546('id'))
            t_10102: 'bool33' = c_1173.to_string() == 'users.id'
            def fn_10096() -> 'str27':
                return 'col helper'
            test_69.assert_(t_10102, fn_10096)
        finally:
            test_69.soft_fail_to_hard()
class TestCase92(TestCase46):
    def test___joinWithColHelper__1787(self) -> None:
        'join with col helper'
        test_70: Test = Test()
        try:
            on_cond_1175: 'SqlFragment' = col(sid_546('users'), sid_546('id'))
            b_1176: 'SqlBuilder' = SqlBuilder()
            b_1176.append_fragment(on_cond_1175)
            b_1176.append_safe(' = ')
            b_1176.append_fragment(col(sid_546('orders'), sid_546('user_id')))
            t_10087: 'SafeIdentifier' = sid_546('users')
            t_10088: 'SafeIdentifier' = sid_546('orders')
            t_10089: 'SqlFragment' = b_1176.accumulated
            q_1177: 'Query' = from_(t_10087).inner_join(t_10088, t_10089)
            t_10094: 'bool33' = q_1177.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_10076() -> 'str27':
                return 'join with col'
            test_70.assert_(t_10094, fn_10076)
        finally:
            test_70.soft_fail_to_hard()
class TestCase93(TestCase46):
    def test___orWhereBasic__1788(self) -> None:
        'orWhere basic'
        test_71: Test = Test()
        try:
            t_10065: 'SafeIdentifier' = sid_546('users')
            t_10066: 'SqlBuilder' = SqlBuilder()
            t_10066.append_safe('status = ')
            t_10066.append_string('active')
            t_10069: 'SqlFragment' = t_10066.accumulated
            q_1179: 'Query' = from_(t_10065).or_where(t_10069)
            t_10074: 'bool33' = q_1179.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_10064() -> 'str27':
                return 'orWhere basic'
            test_71.assert_(t_10074, fn_10064)
        finally:
            test_71.soft_fail_to_hard()
class TestCase94(TestCase46):
    def test___whereThenOrWhere__1790(self) -> None:
        'where then orWhere'
        test_72: Test = Test()
        try:
            t_10048: 'SafeIdentifier' = sid_546('users')
            t_10049: 'SqlBuilder' = SqlBuilder()
            t_10049.append_safe('age > ')
            t_10049.append_int32(18)
            t_10052: 'SqlFragment' = t_10049.accumulated
            t_10053: 'Query' = from_(t_10048).where(t_10052)
            t_10054: 'SqlBuilder' = SqlBuilder()
            t_10054.append_safe('vip = ')
            t_10054.append_boolean(True)
            q_1181: 'Query' = t_10053.or_where(t_10054.accumulated)
            t_10062: 'bool33' = q_1181.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_10047() -> 'str27':
                return 'where then orWhere'
            test_72.assert_(t_10062, fn_10047)
        finally:
            test_72.soft_fail_to_hard()
class TestCase95(TestCase46):
    def test___multipleOrWhere__1793(self) -> None:
        'multiple orWhere'
        test_73: Test = Test()
        try:
            t_10026: 'SafeIdentifier' = sid_546('users')
            t_10027: 'SqlBuilder' = SqlBuilder()
            t_10027.append_safe('active = ')
            t_10027.append_boolean(True)
            t_10030: 'SqlFragment' = t_10027.accumulated
            t_10031: 'Query' = from_(t_10026).where(t_10030)
            t_10032: 'SqlBuilder' = SqlBuilder()
            t_10032.append_safe('role = ')
            t_10032.append_string('admin')
            t_10036: 'Query' = t_10031.or_where(t_10032.accumulated)
            t_10037: 'SqlBuilder' = SqlBuilder()
            t_10037.append_safe('role = ')
            t_10037.append_string('moderator')
            q_1183: 'Query' = t_10036.or_where(t_10037.accumulated)
            t_10045: 'bool33' = q_1183.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_10025() -> 'str27':
                return 'multiple orWhere'
            test_73.assert_(t_10045, fn_10025)
        finally:
            test_73.soft_fail_to_hard()
class TestCase96(TestCase46):
    def test___mixedWhereAndOrWhere__1797(self) -> None:
        'mixed where and orWhere'
        test_74: Test = Test()
        try:
            t_10004: 'SafeIdentifier' = sid_546('users')
            t_10005: 'SqlBuilder' = SqlBuilder()
            t_10005.append_safe('age > ')
            t_10005.append_int32(18)
            t_10008: 'SqlFragment' = t_10005.accumulated
            t_10009: 'Query' = from_(t_10004).where(t_10008)
            t_10010: 'SqlBuilder' = SqlBuilder()
            t_10010.append_safe('active = ')
            t_10010.append_boolean(True)
            t_10014: 'Query' = t_10009.where(t_10010.accumulated)
            t_10015: 'SqlBuilder' = SqlBuilder()
            t_10015.append_safe('vip = ')
            t_10015.append_boolean(True)
            q_1185: 'Query' = t_10014.or_where(t_10015.accumulated)
            t_10023: 'bool33' = q_1185.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_10003() -> 'str27':
                return 'mixed where and orWhere'
            test_74.assert_(t_10023, fn_10003)
        finally:
            test_74.soft_fail_to_hard()
class TestCase97(TestCase46):
    def test___whereNull__1801(self) -> None:
        'whereNull'
        test_75: Test = Test()
        try:
            t_9995: 'SafeIdentifier' = sid_546('users')
            t_9996: 'SafeIdentifier' = sid_546('deleted_at')
            q_1187: 'Query' = from_(t_9995).where_null(t_9996)
            t_10001: 'bool33' = q_1187.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_9994() -> 'str27':
                return 'whereNull'
            test_75.assert_(t_10001, fn_9994)
        finally:
            test_75.soft_fail_to_hard()
class TestCase98(TestCase46):
    def test___whereNotNull__1802(self) -> None:
        'whereNotNull'
        test_76: Test = Test()
        try:
            t_9986: 'SafeIdentifier' = sid_546('users')
            t_9987: 'SafeIdentifier' = sid_546('email')
            q_1189: 'Query' = from_(t_9986).where_not_null(t_9987)
            t_9992: 'bool33' = q_1189.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_9985() -> 'str27':
                return 'whereNotNull'
            test_76.assert_(t_9992, fn_9985)
        finally:
            test_76.soft_fail_to_hard()
class TestCase99(TestCase46):
    def test___whereNullChainedWithWhere__1803(self) -> None:
        'whereNull chained with where'
        test_77: Test = Test()
        try:
            t_9972: 'SafeIdentifier' = sid_546('users')
            t_9973: 'SqlBuilder' = SqlBuilder()
            t_9973.append_safe('active = ')
            t_9973.append_boolean(True)
            t_9976: 'SqlFragment' = t_9973.accumulated
            q_1191: 'Query' = from_(t_9972).where(t_9976).where_null(sid_546('deleted_at'))
            t_9983: 'bool33' = q_1191.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_9971() -> 'str27':
                return 'whereNull chained'
            test_77.assert_(t_9983, fn_9971)
        finally:
            test_77.soft_fail_to_hard()
class TestCase100(TestCase46):
    def test___whereNotNullChainedWithOrWhere__1805(self) -> None:
        'whereNotNull chained with orWhere'
        test_78: Test = Test()
        try:
            t_9958: 'SafeIdentifier' = sid_546('users')
            t_9959: 'SafeIdentifier' = sid_546('deleted_at')
            t_9960: 'Query' = from_(t_9958).where_null(t_9959)
            t_9961: 'SqlBuilder' = SqlBuilder()
            t_9961.append_safe('role = ')
            t_9961.append_string('admin')
            q_1193: 'Query' = t_9960.or_where(t_9961.accumulated)
            t_9969: 'bool33' = q_1193.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_9957() -> 'str27':
                return 'whereNotNull with orWhere'
            test_78.assert_(t_9969, fn_9957)
        finally:
            test_78.soft_fail_to_hard()
class TestCase101(TestCase46):
    def test___whereInWithIntValues__1807(self) -> None:
        'whereIn with int values'
        test_79: Test = Test()
        try:
            t_9946: 'SafeIdentifier' = sid_546('users')
            t_9947: 'SafeIdentifier' = sid_546('id')
            t_9948: 'SqlInt32' = SqlInt32(1)
            t_9949: 'SqlInt32' = SqlInt32(2)
            t_9950: 'SqlInt32' = SqlInt32(3)
            q_1195: 'Query' = from_(t_9946).where_in(t_9947, (t_9948, t_9949, t_9950))
            t_9955: 'bool33' = q_1195.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_9945() -> 'str27':
                return 'whereIn ints'
            test_79.assert_(t_9955, fn_9945)
        finally:
            test_79.soft_fail_to_hard()
class TestCase102(TestCase46):
    def test___whereInWithStringValuesEscaping__1808(self) -> None:
        'whereIn with string values escaping'
        test_80: Test = Test()
        try:
            t_9935: 'SafeIdentifier' = sid_546('users')
            t_9936: 'SafeIdentifier' = sid_546('name')
            t_9937: 'SqlString' = SqlString('Alice')
            t_9938: 'SqlString' = SqlString("Bob's")
            q_1197: 'Query' = from_(t_9935).where_in(t_9936, (t_9937, t_9938))
            t_9943: 'bool33' = q_1197.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_9934() -> 'str27':
                return 'whereIn strings'
            test_80.assert_(t_9943, fn_9934)
        finally:
            test_80.soft_fail_to_hard()
class TestCase103(TestCase46):
    def test___whereInWithEmptyListProduces1_0__1809(self) -> None:
        'whereIn with empty list produces 1=0'
        test_81: Test = Test()
        try:
            t_9926: 'SafeIdentifier' = sid_546('users')
            t_9927: 'SafeIdentifier' = sid_546('id')
            q_1199: 'Query' = from_(t_9926).where_in(t_9927, ())
            t_9932: 'bool33' = q_1199.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_9925() -> 'str27':
                return 'whereIn empty'
            test_81.assert_(t_9932, fn_9925)
        finally:
            test_81.soft_fail_to_hard()
class TestCase104(TestCase46):
    def test___whereInChained__1810(self) -> None:
        'whereIn chained'
        test_82: Test = Test()
        try:
            t_9910: 'SafeIdentifier' = sid_546('users')
            t_9911: 'SqlBuilder' = SqlBuilder()
            t_9911.append_safe('active = ')
            t_9911.append_boolean(True)
            t_9914: 'SqlFragment' = t_9911.accumulated
            q_1201: 'Query' = from_(t_9910).where(t_9914).where_in(sid_546('role'), (SqlString('admin'), SqlString('user')))
            t_9923: 'bool33' = q_1201.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_9909() -> 'str27':
                return 'whereIn chained'
            test_82.assert_(t_9923, fn_9909)
        finally:
            test_82.soft_fail_to_hard()
class TestCase105(TestCase46):
    def test___whereInSingleElement__1812(self) -> None:
        'whereIn single element'
        test_83: Test = Test()
        try:
            t_9900: 'SafeIdentifier' = sid_546('users')
            t_9901: 'SafeIdentifier' = sid_546('id')
            t_9902: 'SqlInt32' = SqlInt32(42)
            q_1203: 'Query' = from_(t_9900).where_in(t_9901, (t_9902,))
            t_9907: 'bool33' = q_1203.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_9899() -> 'str27':
                return 'whereIn single'
            test_83.assert_(t_9907, fn_9899)
        finally:
            test_83.soft_fail_to_hard()
class TestCase106(TestCase46):
    def test___whereNotBasic__1813(self) -> None:
        'whereNot basic'
        test_84: Test = Test()
        try:
            t_9888: 'SafeIdentifier' = sid_546('users')
            t_9889: 'SqlBuilder' = SqlBuilder()
            t_9889.append_safe('active = ')
            t_9889.append_boolean(True)
            t_9892: 'SqlFragment' = t_9889.accumulated
            q_1205: 'Query' = from_(t_9888).where_not(t_9892)
            t_9897: 'bool33' = q_1205.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_9887() -> 'str27':
                return 'whereNot'
            test_84.assert_(t_9897, fn_9887)
        finally:
            test_84.soft_fail_to_hard()
class TestCase107(TestCase46):
    def test___whereNotChained__1815(self) -> None:
        'whereNot chained'
        test_85: Test = Test()
        try:
            t_9871: 'SafeIdentifier' = sid_546('users')
            t_9872: 'SqlBuilder' = SqlBuilder()
            t_9872.append_safe('age > ')
            t_9872.append_int32(18)
            t_9875: 'SqlFragment' = t_9872.accumulated
            t_9876: 'Query' = from_(t_9871).where(t_9875)
            t_9877: 'SqlBuilder' = SqlBuilder()
            t_9877.append_safe('banned = ')
            t_9877.append_boolean(True)
            q_1207: 'Query' = t_9876.where_not(t_9877.accumulated)
            t_9885: 'bool33' = q_1207.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_9870() -> 'str27':
                return 'whereNot chained'
            test_85.assert_(t_9885, fn_9870)
        finally:
            test_85.soft_fail_to_hard()
class TestCase108(TestCase46):
    def test___whereBetweenIntegers__1818(self) -> None:
        'whereBetween integers'
        test_86: Test = Test()
        try:
            t_9860: 'SafeIdentifier' = sid_546('users')
            t_9861: 'SafeIdentifier' = sid_546('age')
            t_9862: 'SqlInt32' = SqlInt32(18)
            t_9863: 'SqlInt32' = SqlInt32(65)
            q_1209: 'Query' = from_(t_9860).where_between(t_9861, t_9862, t_9863)
            t_9868: 'bool33' = q_1209.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_9859() -> 'str27':
                return 'whereBetween ints'
            test_86.assert_(t_9868, fn_9859)
        finally:
            test_86.soft_fail_to_hard()
class TestCase109(TestCase46):
    def test___whereBetweenChained__1819(self) -> None:
        'whereBetween chained'
        test_87: Test = Test()
        try:
            t_9844: 'SafeIdentifier' = sid_546('users')
            t_9845: 'SqlBuilder' = SqlBuilder()
            t_9845.append_safe('active = ')
            t_9845.append_boolean(True)
            t_9848: 'SqlFragment' = t_9845.accumulated
            q_1211: 'Query' = from_(t_9844).where(t_9848).where_between(sid_546('age'), SqlInt32(21), SqlInt32(30))
            t_9857: 'bool33' = q_1211.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_9843() -> 'str27':
                return 'whereBetween chained'
            test_87.assert_(t_9857, fn_9843)
        finally:
            test_87.soft_fail_to_hard()
class TestCase110(TestCase46):
    def test___whereLikeBasic__1821(self) -> None:
        'whereLike basic'
        test_88: Test = Test()
        try:
            t_9835: 'SafeIdentifier' = sid_546('users')
            t_9836: 'SafeIdentifier' = sid_546('name')
            q_1213: 'Query' = from_(t_9835).where_like(t_9836, 'John%')
            t_9841: 'bool33' = q_1213.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_9834() -> 'str27':
                return 'whereLike'
            test_88.assert_(t_9841, fn_9834)
        finally:
            test_88.soft_fail_to_hard()
class TestCase111(TestCase46):
    def test___whereIlikeBasic__1822(self) -> None:
        'whereILike basic'
        test_89: Test = Test()
        try:
            t_9826: 'SafeIdentifier' = sid_546('users')
            t_9827: 'SafeIdentifier' = sid_546('email')
            q_1215: 'Query' = from_(t_9826).where_i_like(t_9827, '%@gmail.com')
            t_9832: 'bool33' = q_1215.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_9825() -> 'str27':
                return 'whereILike'
            test_89.assert_(t_9832, fn_9825)
        finally:
            test_89.soft_fail_to_hard()
class TestCase112(TestCase46):
    def test___whereLikeWithInjectionAttempt__1823(self) -> None:
        'whereLike with injection attempt'
        test_90: Test = Test()
        try:
            t_9812: 'SafeIdentifier' = sid_546('users')
            t_9813: 'SafeIdentifier' = sid_546('name')
            q_1217: 'Query' = from_(t_9812).where_like(t_9813, "'; DROP TABLE users; --")
            s_1218: 'str27' = q_1217.to_sql().to_string()
            t_9818: 'bool33' = s_1218.find("''") >= 0
            def fn_9811() -> 'str27':
                return str_cat_11468('like injection escaped: ', s_1218)
            test_90.assert_(t_9818, fn_9811)
            t_9822: 'bool33' = s_1218.find('LIKE') >= 0
            def fn_9810() -> 'str27':
                return str_cat_11468('like structure intact: ', s_1218)
            test_90.assert_(t_9822, fn_9810)
        finally:
            test_90.soft_fail_to_hard()
class TestCase113(TestCase46):
    def test___whereLikeWildcardPatterns__1824(self) -> None:
        'whereLike wildcard patterns'
        test_91: Test = Test()
        try:
            t_9802: 'SafeIdentifier' = sid_546('users')
            t_9803: 'SafeIdentifier' = sid_546('name')
            q_1220: 'Query' = from_(t_9802).where_like(t_9803, '%son%')
            t_9808: 'bool33' = q_1220.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_9801() -> 'str27':
                return 'whereLike wildcard'
            test_91.assert_(t_9808, fn_9801)
        finally:
            test_91.soft_fail_to_hard()
class TestCase114(TestCase46):
    def test___countAllProducesCount__1825(self) -> None:
        'countAll produces COUNT(*)'
        test_92: Test = Test()
        try:
            f_1222: 'SqlFragment' = count_all()
            t_9799: 'bool33' = f_1222.to_string() == 'COUNT(*)'
            def fn_9795() -> 'str27':
                return 'countAll'
            test_92.assert_(t_9799, fn_9795)
        finally:
            test_92.soft_fail_to_hard()
class TestCase115(TestCase46):
    def test___countColProducesCountField__1826(self) -> None:
        'countCol produces COUNT(field)'
        test_93: Test = Test()
        try:
            f_1224: 'SqlFragment' = count_col(sid_546('id'))
            t_9793: 'bool33' = f_1224.to_string() == 'COUNT(id)'
            def fn_9788() -> 'str27':
                return 'countCol'
            test_93.assert_(t_9793, fn_9788)
        finally:
            test_93.soft_fail_to_hard()
class TestCase116(TestCase46):
    def test___sumColProducesSumField__1827(self) -> None:
        'sumCol produces SUM(field)'
        test_94: Test = Test()
        try:
            f_1226: 'SqlFragment' = sum_col(sid_546('amount'))
            t_9786: 'bool33' = f_1226.to_string() == 'SUM(amount)'
            def fn_9781() -> 'str27':
                return 'sumCol'
            test_94.assert_(t_9786, fn_9781)
        finally:
            test_94.soft_fail_to_hard()
class TestCase117(TestCase46):
    def test___avgColProducesAvgField__1828(self) -> None:
        'avgCol produces AVG(field)'
        test_95: Test = Test()
        try:
            f_1228: 'SqlFragment' = avg_col(sid_546('price'))
            t_9779: 'bool33' = f_1228.to_string() == 'AVG(price)'
            def fn_9774() -> 'str27':
                return 'avgCol'
            test_95.assert_(t_9779, fn_9774)
        finally:
            test_95.soft_fail_to_hard()
class TestCase118(TestCase46):
    def test___minColProducesMinField__1829(self) -> None:
        'minCol produces MIN(field)'
        test_96: Test = Test()
        try:
            f_1230: 'SqlFragment' = min_col(sid_546('created_at'))
            t_9772: 'bool33' = f_1230.to_string() == 'MIN(created_at)'
            def fn_9767() -> 'str27':
                return 'minCol'
            test_96.assert_(t_9772, fn_9767)
        finally:
            test_96.soft_fail_to_hard()
class TestCase119(TestCase46):
    def test___maxColProducesMaxField__1830(self) -> None:
        'maxCol produces MAX(field)'
        test_97: Test = Test()
        try:
            f_1232: 'SqlFragment' = max_col(sid_546('score'))
            t_9765: 'bool33' = f_1232.to_string() == 'MAX(score)'
            def fn_9760() -> 'str27':
                return 'maxCol'
            test_97.assert_(t_9765, fn_9760)
        finally:
            test_97.soft_fail_to_hard()
class TestCase120(TestCase46):
    def test___selectExprWithAggregate__1831(self) -> None:
        'selectExpr with aggregate'
        test_98: Test = Test()
        try:
            t_9752: 'SafeIdentifier' = sid_546('orders')
            t_9753: 'SqlFragment' = count_all()
            q_1234: 'Query' = from_(t_9752).select_expr((t_9753,))
            t_9758: 'bool33' = q_1234.to_sql().to_string() == 'SELECT COUNT(*) FROM orders'
            def fn_9751() -> 'str27':
                return 'selectExpr count'
            test_98.assert_(t_9758, fn_9751)
        finally:
            test_98.soft_fail_to_hard()
class TestCase121(TestCase46):
    def test___selectExprWithMultipleExpressions__1832(self) -> None:
        'selectExpr with multiple expressions'
        test_99: Test = Test()
        try:
            name_frag_1236: 'SqlFragment' = col(sid_546('users'), sid_546('name'))
            t_9743: 'SafeIdentifier' = sid_546('users')
            t_9744: 'SqlFragment' = count_all()
            q_1237: 'Query' = from_(t_9743).select_expr((name_frag_1236, t_9744))
            t_9749: 'bool33' = q_1237.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users'
            def fn_9739() -> 'str27':
                return 'selectExpr multi'
            test_99.assert_(t_9749, fn_9739)
        finally:
            test_99.soft_fail_to_hard()
class TestCase122(TestCase46):
    def test___selectExprOverridesSelectedFields__1833(self) -> None:
        'selectExpr overrides selectedFields'
        test_100: Test = Test()
        try:
            t_9728: 'SafeIdentifier' = sid_546('users')
            t_9729: 'SafeIdentifier' = sid_546('id')
            t_9730: 'SafeIdentifier' = sid_546('name')
            q_1239: 'Query' = from_(t_9728).select((t_9729, t_9730)).select_expr((count_all(),))
            t_9737: 'bool33' = q_1239.to_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_9727() -> 'str27':
                return 'selectExpr overrides select'
            test_100.assert_(t_9737, fn_9727)
        finally:
            test_100.soft_fail_to_hard()
class TestCase123(TestCase46):
    def test___groupBySingleField__1834(self) -> None:
        'groupBy single field'
        test_101: Test = Test()
        try:
            t_9714: 'SafeIdentifier' = sid_546('orders')
            t_9717: 'SqlFragment' = col(sid_546('orders'), sid_546('status'))
            t_9718: 'SqlFragment' = count_all()
            q_1241: 'Query' = from_(t_9714).select_expr((t_9717, t_9718)).group_by(sid_546('status'))
            t_9725: 'bool33' = q_1241.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status'
            def fn_9713() -> 'str27':
                return 'groupBy single'
            test_101.assert_(t_9725, fn_9713)
        finally:
            test_101.soft_fail_to_hard()
class TestCase124(TestCase46):
    def test___groupByMultipleFields__1835(self) -> None:
        'groupBy multiple fields'
        test_102: Test = Test()
        try:
            t_9703: 'SafeIdentifier' = sid_546('orders')
            t_9704: 'SafeIdentifier' = sid_546('status')
            q_1243: 'Query' = from_(t_9703).group_by(t_9704).group_by(sid_546('category'))
            t_9711: 'bool33' = q_1243.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category'
            def fn_9702() -> 'str27':
                return 'groupBy multiple'
            test_102.assert_(t_9711, fn_9702)
        finally:
            test_102.soft_fail_to_hard()
class TestCase125(TestCase46):
    def test___havingBasic__1836(self) -> None:
        'having basic'
        test_103: Test = Test()
        try:
            t_9684: 'SafeIdentifier' = sid_546('orders')
            t_9687: 'SqlFragment' = col(sid_546('orders'), sid_546('status'))
            t_9688: 'SqlFragment' = count_all()
            t_9691: 'Query' = from_(t_9684).select_expr((t_9687, t_9688)).group_by(sid_546('status'))
            t_9692: 'SqlBuilder' = SqlBuilder()
            t_9692.append_safe('COUNT(*) > ')
            t_9692.append_int32(5)
            q_1245: 'Query' = t_9691.having(t_9692.accumulated)
            t_9700: 'bool33' = q_1245.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5'
            def fn_9683() -> 'str27':
                return 'having basic'
            test_103.assert_(t_9700, fn_9683)
        finally:
            test_103.soft_fail_to_hard()
class TestCase126(TestCase46):
    def test___orHaving__1838(self) -> None:
        'orHaving'
        test_104: Test = Test()
        try:
            t_9665: 'SafeIdentifier' = sid_546('orders')
            t_9666: 'SafeIdentifier' = sid_546('status')
            t_9667: 'Query' = from_(t_9665).group_by(t_9666)
            t_9668: 'SqlBuilder' = SqlBuilder()
            t_9668.append_safe('COUNT(*) > ')
            t_9668.append_int32(5)
            t_9672: 'Query' = t_9667.having(t_9668.accumulated)
            t_9673: 'SqlBuilder' = SqlBuilder()
            t_9673.append_safe('SUM(total) > ')
            t_9673.append_int32(1000)
            q_1247: 'Query' = t_9672.or_having(t_9673.accumulated)
            t_9681: 'bool33' = q_1247.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000'
            def fn_9664() -> 'str27':
                return 'orHaving'
            test_104.assert_(t_9681, fn_9664)
        finally:
            test_104.soft_fail_to_hard()
class TestCase127(TestCase46):
    def test___distinctBasic__1841(self) -> None:
        'distinct basic'
        test_105: Test = Test()
        try:
            t_9655: 'SafeIdentifier' = sid_546('users')
            t_9656: 'SafeIdentifier' = sid_546('name')
            q_1249: 'Query' = from_(t_9655).select((t_9656,)).distinct()
            t_9662: 'bool33' = q_1249.to_sql().to_string() == 'SELECT DISTINCT name FROM users'
            def fn_9654() -> 'str27':
                return 'distinct'
            test_105.assert_(t_9662, fn_9654)
        finally:
            test_105.soft_fail_to_hard()
class TestCase128(TestCase46):
    def test___distinctWithWhere__1842(self) -> None:
        'distinct with where'
        test_106: Test = Test()
        try:
            t_9640: 'SafeIdentifier' = sid_546('users')
            t_9641: 'SafeIdentifier' = sid_546('email')
            t_9642: 'Query' = from_(t_9640).select((t_9641,))
            t_9643: 'SqlBuilder' = SqlBuilder()
            t_9643.append_safe('active = ')
            t_9643.append_boolean(True)
            q_1251: 'Query' = t_9642.where(t_9643.accumulated).distinct()
            t_9652: 'bool33' = q_1251.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE'
            def fn_9639() -> 'str27':
                return 'distinct with where'
            test_106.assert_(t_9652, fn_9639)
        finally:
            test_106.soft_fail_to_hard()
class TestCase129(TestCase46):
    def test___countSqlBare__1844(self) -> None:
        'countSql bare'
        test_107: Test = Test()
        try:
            q_1253: 'Query' = from_(sid_546('users'))
            t_9637: 'bool33' = q_1253.count_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_9632() -> 'str27':
                return 'countSql bare'
            test_107.assert_(t_9637, fn_9632)
        finally:
            test_107.soft_fail_to_hard()
class TestCase130(TestCase46):
    def test___countSqlWithWhere__1845(self) -> None:
        'countSql with WHERE'
        test_108: Test = Test()
        try:
            t_9621: 'SafeIdentifier' = sid_546('users')
            t_9622: 'SqlBuilder' = SqlBuilder()
            t_9622.append_safe('active = ')
            t_9622.append_boolean(True)
            t_9625: 'SqlFragment' = t_9622.accumulated
            q_1255: 'Query' = from_(t_9621).where(t_9625)
            t_9630: 'bool33' = q_1255.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_9620() -> 'str27':
                return 'countSql with where'
            test_108.assert_(t_9630, fn_9620)
        finally:
            test_108.soft_fail_to_hard()
class TestCase131(TestCase46):
    def test___countSqlWithJoin__1847(self) -> None:
        'countSql with JOIN'
        test_109: Test = Test()
        try:
            t_9604: 'SafeIdentifier' = sid_546('users')
            t_9605: 'SafeIdentifier' = sid_546('orders')
            t_9606: 'SqlBuilder' = SqlBuilder()
            t_9606.append_safe('users.id = orders.user_id')
            t_9608: 'SqlFragment' = t_9606.accumulated
            t_9609: 'Query' = from_(t_9604).inner_join(t_9605, t_9608)
            t_9610: 'SqlBuilder' = SqlBuilder()
            t_9610.append_safe('orders.total > ')
            t_9610.append_int32(100)
            q_1257: 'Query' = t_9609.where(t_9610.accumulated)
            t_9618: 'bool33' = q_1257.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100'
            def fn_9603() -> 'str27':
                return 'countSql with join'
            test_109.assert_(t_9618, fn_9603)
        finally:
            test_109.soft_fail_to_hard()
class TestCase132(TestCase46):
    def test___countSqlDropsOrderByLimitOffset__1850(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_110: Test = Test()
        try:
            t_9590: 'SafeIdentifier' = sid_546('users')
            t_9591: 'SqlBuilder' = SqlBuilder()
            t_9591.append_safe('active = ')
            t_9591.append_boolean(True)
            t_9594: 'SqlFragment' = t_9591.accumulated
            t_4906: 'Query'
            t_4906 = from_(t_9590).where(t_9594).order_by(sid_546('name'), True).limit(10)
            t_4907: 'Query'
            t_4907 = t_4906.offset(20)
            q_1259: 'Query' = t_4907
            s_1260: 'str27' = q_1259.count_sql().to_string()
            t_9601: 'bool33' = s_1260 == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_9589() -> 'str27':
                return str_cat_11468('countSql drops extras: ', s_1260)
            test_110.assert_(t_9601, fn_9589)
        finally:
            test_110.soft_fail_to_hard()
class TestCase133(TestCase46):
    def test___fullAggregationQuery__1852(self) -> None:
        'full aggregation query'
        test_111: Test = Test()
        try:
            t_9557: 'SafeIdentifier' = sid_546('orders')
            t_9560: 'SqlFragment' = col(sid_546('orders'), sid_546('status'))
            t_9561: 'SqlFragment' = count_all()
            t_9563: 'SqlFragment' = sum_col(sid_546('total'))
            t_9564: 'Query' = from_(t_9557).select_expr((t_9560, t_9561, t_9563))
            t_9565: 'SafeIdentifier' = sid_546('users')
            t_9566: 'SqlBuilder' = SqlBuilder()
            t_9566.append_safe('orders.user_id = users.id')
            t_9569: 'Query' = t_9564.inner_join(t_9565, t_9566.accumulated)
            t_9570: 'SqlBuilder' = SqlBuilder()
            t_9570.append_safe('users.active = ')
            t_9570.append_boolean(True)
            t_9576: 'Query' = t_9569.where(t_9570.accumulated).group_by(sid_546('status'))
            t_9577: 'SqlBuilder' = SqlBuilder()
            t_9577.append_safe('COUNT(*) > ')
            t_9577.append_int32(3)
            q_1262: 'Query' = t_9576.having(t_9577.accumulated).order_by(sid_546('status'), True)
            expected_1263: 'str27' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            t_9587: 'bool33' = q_1262.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_9556() -> 'str27':
                return 'full aggregation'
            test_111.assert_(t_9587, fn_9556)
        finally:
            test_111.soft_fail_to_hard()
class TestCase134(TestCase46):
    def test___unionSql__1856(self) -> None:
        'unionSql'
        test_112: Test = Test()
        try:
            t_9539: 'SafeIdentifier' = sid_546('users')
            t_9540: 'SqlBuilder' = SqlBuilder()
            t_9540.append_safe('role = ')
            t_9540.append_string('admin')
            t_9543: 'SqlFragment' = t_9540.accumulated
            a_1265: 'Query' = from_(t_9539).where(t_9543)
            t_9545: 'SafeIdentifier' = sid_546('users')
            t_9546: 'SqlBuilder' = SqlBuilder()
            t_9546.append_safe('role = ')
            t_9546.append_string('moderator')
            t_9549: 'SqlFragment' = t_9546.accumulated
            b_1266: 'Query' = from_(t_9545).where(t_9549)
            s_1267: 'str27' = union_sql(a_1265, b_1266).to_string()
            t_9554: 'bool33' = s_1267 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')"
            def fn_9538() -> 'str27':
                return str_cat_11468('unionSql: ', s_1267)
            test_112.assert_(t_9554, fn_9538)
        finally:
            test_112.soft_fail_to_hard()
class TestCase135(TestCase46):
    def test___unionAllSql__1859(self) -> None:
        'unionAllSql'
        test_113: Test = Test()
        try:
            t_9527: 'SafeIdentifier' = sid_546('users')
            t_9528: 'SafeIdentifier' = sid_546('name')
            a_1269: 'Query' = from_(t_9527).select((t_9528,))
            t_9530: 'SafeIdentifier' = sid_546('contacts')
            t_9531: 'SafeIdentifier' = sid_546('name')
            b_1270: 'Query' = from_(t_9530).select((t_9531,))
            s_1271: 'str27' = union_all_sql(a_1269, b_1270).to_string()
            t_9536: 'bool33' = s_1271 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)'
            def fn_9526() -> 'str27':
                return str_cat_11468('unionAllSql: ', s_1271)
            test_113.assert_(t_9536, fn_9526)
        finally:
            test_113.soft_fail_to_hard()
class TestCase136(TestCase46):
    def test___intersectSql__1860(self) -> None:
        'intersectSql'
        test_114: Test = Test()
        try:
            t_9515: 'SafeIdentifier' = sid_546('users')
            t_9516: 'SafeIdentifier' = sid_546('email')
            a_1273: 'Query' = from_(t_9515).select((t_9516,))
            t_9518: 'SafeIdentifier' = sid_546('subscribers')
            t_9519: 'SafeIdentifier' = sid_546('email')
            b_1274: 'Query' = from_(t_9518).select((t_9519,))
            s_1275: 'str27' = intersect_sql(a_1273, b_1274).to_string()
            t_9524: 'bool33' = s_1275 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)'
            def fn_9514() -> 'str27':
                return str_cat_11468('intersectSql: ', s_1275)
            test_114.assert_(t_9524, fn_9514)
        finally:
            test_114.soft_fail_to_hard()
class TestCase137(TestCase46):
    def test___exceptSql__1861(self) -> None:
        'exceptSql'
        test_115: Test = Test()
        try:
            t_9503: 'SafeIdentifier' = sid_546('users')
            t_9504: 'SafeIdentifier' = sid_546('id')
            a_1277: 'Query' = from_(t_9503).select((t_9504,))
            t_9506: 'SafeIdentifier' = sid_546('banned')
            t_9507: 'SafeIdentifier' = sid_546('id')
            b_1278: 'Query' = from_(t_9506).select((t_9507,))
            s_1279: 'str27' = except_sql(a_1277, b_1278).to_string()
            t_9512: 'bool33' = s_1279 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)'
            def fn_9502() -> 'str27':
                return str_cat_11468('exceptSql: ', s_1279)
            test_115.assert_(t_9512, fn_9502)
        finally:
            test_115.soft_fail_to_hard()
class TestCase138(TestCase46):
    def test___subqueryWithAlias__1862(self) -> None:
        'subquery with alias'
        test_116: Test = Test()
        try:
            t_9488: 'SafeIdentifier' = sid_546('orders')
            t_9489: 'SafeIdentifier' = sid_546('user_id')
            t_9490: 'Query' = from_(t_9488).select((t_9489,))
            t_9491: 'SqlBuilder' = SqlBuilder()
            t_9491.append_safe('total > ')
            t_9491.append_int32(100)
            inner_1281: 'Query' = t_9490.where(t_9491.accumulated)
            s_1282: 'str27' = subquery(inner_1281, sid_546('big_orders')).to_string()
            t_9500: 'bool33' = s_1282 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders'
            def fn_9487() -> 'str27':
                return str_cat_11468('subquery: ', s_1282)
            test_116.assert_(t_9500, fn_9487)
        finally:
            test_116.soft_fail_to_hard()
class TestCase139(TestCase46):
    def test___existsSql__1864(self) -> None:
        'existsSql'
        test_117: Test = Test()
        try:
            t_9477: 'SafeIdentifier' = sid_546('orders')
            t_9478: 'SqlBuilder' = SqlBuilder()
            t_9478.append_safe('orders.user_id = users.id')
            t_9480: 'SqlFragment' = t_9478.accumulated
            inner_1284: 'Query' = from_(t_9477).where(t_9480)
            s_1285: 'str27' = exists_sql(inner_1284).to_string()
            t_9485: 'bool33' = s_1285 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_9476() -> 'str27':
                return str_cat_11468('existsSql: ', s_1285)
            test_117.assert_(t_9485, fn_9476)
        finally:
            test_117.soft_fail_to_hard()
class TestCase140(TestCase46):
    def test___whereInSubquery__1866(self) -> None:
        'whereInSubquery'
        test_118: Test = Test()
        try:
            t_9460: 'SafeIdentifier' = sid_546('orders')
            t_9461: 'SafeIdentifier' = sid_546('user_id')
            t_9462: 'Query' = from_(t_9460).select((t_9461,))
            t_9463: 'SqlBuilder' = SqlBuilder()
            t_9463.append_safe('total > ')
            t_9463.append_int32(1000)
            sub_1287: 'Query' = t_9462.where(t_9463.accumulated)
            t_9468: 'SafeIdentifier' = sid_546('users')
            t_9469: 'SafeIdentifier' = sid_546('id')
            q_1288: 'Query' = from_(t_9468).where_in_subquery(t_9469, sub_1287)
            s_1289: 'str27' = q_1288.to_sql().to_string()
            t_9474: 'bool33' = s_1289 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)'
            def fn_9459() -> 'str27':
                return str_cat_11468('whereInSubquery: ', s_1289)
            test_118.assert_(t_9474, fn_9459)
        finally:
            test_118.soft_fail_to_hard()
class TestCase141(TestCase46):
    def test___setOperationWithWhereOnEachSide__1868(self) -> None:
        'set operation with WHERE on each side'
        test_119: Test = Test()
        try:
            t_9437: 'SafeIdentifier' = sid_546('users')
            t_9438: 'SqlBuilder' = SqlBuilder()
            t_9438.append_safe('age > ')
            t_9438.append_int32(18)
            t_9441: 'SqlFragment' = t_9438.accumulated
            t_9442: 'Query' = from_(t_9437).where(t_9441)
            t_9443: 'SqlBuilder' = SqlBuilder()
            t_9443.append_safe('active = ')
            t_9443.append_boolean(True)
            a_1291: 'Query' = t_9442.where(t_9443.accumulated)
            t_9448: 'SafeIdentifier' = sid_546('users')
            t_9449: 'SqlBuilder' = SqlBuilder()
            t_9449.append_safe('role = ')
            t_9449.append_string('vip')
            t_9452: 'SqlFragment' = t_9449.accumulated
            b_1292: 'Query' = from_(t_9448).where(t_9452)
            s_1293: 'str27' = union_sql(a_1291, b_1292).to_string()
            t_9457: 'bool33' = s_1293 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')"
            def fn_9436() -> 'str27':
                return str_cat_11468('union with where: ', s_1293)
            test_119.assert_(t_9457, fn_9436)
        finally:
            test_119.soft_fail_to_hard()
class TestCase142(TestCase46):
    def test___whereInSubqueryChainedWithWhere__1872(self) -> None:
        'whereInSubquery chained with where'
        test_120: Test = Test()
        try:
            t_9420: 'SafeIdentifier' = sid_546('orders')
            t_9421: 'SafeIdentifier' = sid_546('user_id')
            sub_1295: 'Query' = from_(t_9420).select((t_9421,))
            t_9423: 'SafeIdentifier' = sid_546('users')
            t_9424: 'SqlBuilder' = SqlBuilder()
            t_9424.append_safe('active = ')
            t_9424.append_boolean(True)
            t_9427: 'SqlFragment' = t_9424.accumulated
            q_1296: 'Query' = from_(t_9423).where(t_9427).where_in_subquery(sid_546('id'), sub_1295)
            s_1297: 'str27' = q_1296.to_sql().to_string()
            t_9434: 'bool33' = s_1297 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)'
            def fn_9419() -> 'str27':
                return str_cat_11468('whereInSubquery chained: ', s_1297)
            test_120.assert_(t_9434, fn_9419)
        finally:
            test_120.soft_fail_to_hard()
class TestCase143(TestCase46):
    def test___existsSqlUsedInWhere__1874(self) -> None:
        'existsSql used in where'
        test_121: Test = Test()
        try:
            t_9406: 'SafeIdentifier' = sid_546('orders')
            t_9407: 'SqlBuilder' = SqlBuilder()
            t_9407.append_safe('orders.user_id = users.id')
            t_9409: 'SqlFragment' = t_9407.accumulated
            sub_1299: 'Query' = from_(t_9406).where(t_9409)
            t_9411: 'SafeIdentifier' = sid_546('users')
            t_9412: 'SqlFragment' = exists_sql(sub_1299)
            q_1300: 'Query' = from_(t_9411).where(t_9412)
            s_1301: 'str27' = q_1300.to_sql().to_string()
            t_9417: 'bool33' = s_1301 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_9405() -> 'str27':
                return str_cat_11468('exists in where: ', s_1301)
            test_121.assert_(t_9417, fn_9405)
        finally:
            test_121.soft_fail_to_hard()
class TestCase144(TestCase46):
    def test___updateQueryBasic__1876(self) -> None:
        'UpdateQuery basic'
        test_122: Test = Test()
        try:
            t_9392: 'SafeIdentifier' = sid_546('users')
            t_9393: 'SafeIdentifier' = sid_546('name')
            t_9394: 'SqlString' = SqlString('Alice')
            t_9395: 'UpdateQuery' = update(t_9392).set(t_9393, t_9394)
            t_9396: 'SqlBuilder' = SqlBuilder()
            t_9396.append_safe('id = ')
            t_9396.append_int32(1)
            t_4728: 'SqlFragment'
            t_4728 = t_9395.where(t_9396.accumulated).to_sql()
            q_1303: 'SqlFragment' = t_4728
            t_9403: 'bool33' = q_1303.to_string() == "UPDATE users SET name = 'Alice' WHERE id = 1"
            def fn_9391() -> 'str27':
                return 'update basic'
            test_122.assert_(t_9403, fn_9391)
        finally:
            test_122.soft_fail_to_hard()
class TestCase145(TestCase46):
    def test___updateQueryMultipleSet__1878(self) -> None:
        'UpdateQuery multiple SET'
        test_123: Test = Test()
        try:
            t_9375: 'SafeIdentifier' = sid_546('users')
            t_9376: 'SafeIdentifier' = sid_546('name')
            t_9377: 'SqlString' = SqlString('Bob')
            t_9381: 'UpdateQuery' = update(t_9375).set(t_9376, t_9377).set(sid_546('age'), SqlInt32(30))
            t_9382: 'SqlBuilder' = SqlBuilder()
            t_9382.append_safe('id = ')
            t_9382.append_int32(2)
            t_4713: 'SqlFragment'
            t_4713 = t_9381.where(t_9382.accumulated).to_sql()
            q_1305: 'SqlFragment' = t_4713
            t_9389: 'bool33' = q_1305.to_string() == "UPDATE users SET name = 'Bob', age = 30 WHERE id = 2"
            def fn_9374() -> 'str27':
                return 'update multi set'
            test_123.assert_(t_9389, fn_9374)
        finally:
            test_123.soft_fail_to_hard()
class TestCase146(TestCase46):
    def test___updateQueryMultipleWhere__1880(self) -> None:
        'UpdateQuery multiple WHERE'
        test_124: Test = Test()
        try:
            t_9356: 'SafeIdentifier' = sid_546('users')
            t_9357: 'SafeIdentifier' = sid_546('active')
            t_9358: 'SqlBoolean' = SqlBoolean(False)
            t_9359: 'UpdateQuery' = update(t_9356).set(t_9357, t_9358)
            t_9360: 'SqlBuilder' = SqlBuilder()
            t_9360.append_safe('age < ')
            t_9360.append_int32(18)
            t_9364: 'UpdateQuery' = t_9359.where(t_9360.accumulated)
            t_9365: 'SqlBuilder' = SqlBuilder()
            t_9365.append_safe('role = ')
            t_9365.append_string('guest')
            t_4695: 'SqlFragment'
            t_4695 = t_9364.where(t_9365.accumulated).to_sql()
            q_1307: 'SqlFragment' = t_4695
            t_9372: 'bool33' = q_1307.to_string() == "UPDATE users SET active = FALSE WHERE age < 18 AND role = 'guest'"
            def fn_9355() -> 'str27':
                return 'update multi where'
            test_124.assert_(t_9372, fn_9355)
        finally:
            test_124.soft_fail_to_hard()
class TestCase147(TestCase46):
    def test___updateQueryOrWhere__1883(self) -> None:
        'UpdateQuery orWhere'
        test_125: Test = Test()
        try:
            t_9337: 'SafeIdentifier' = sid_546('users')
            t_9338: 'SafeIdentifier' = sid_546('status')
            t_9339: 'SqlString' = SqlString('banned')
            t_9340: 'UpdateQuery' = update(t_9337).set(t_9338, t_9339)
            t_9341: 'SqlBuilder' = SqlBuilder()
            t_9341.append_safe('spam_count > ')
            t_9341.append_int32(10)
            t_9345: 'UpdateQuery' = t_9340.where(t_9341.accumulated)
            t_9346: 'SqlBuilder' = SqlBuilder()
            t_9346.append_safe('reported = ')
            t_9346.append_boolean(True)
            t_4674: 'SqlFragment'
            t_4674 = t_9345.or_where(t_9346.accumulated).to_sql()
            q_1309: 'SqlFragment' = t_4674
            t_9353: 'bool33' = q_1309.to_string() == "UPDATE users SET status = 'banned' WHERE spam_count > 10 OR reported = TRUE"
            def fn_9336() -> 'str27':
                return 'update orWhere'
            test_125.assert_(t_9353, fn_9336)
        finally:
            test_125.soft_fail_to_hard()
class TestCase148(TestCase46):
    def test___updateQueryBubblesWithoutWhere__1886(self) -> None:
        'UpdateQuery bubbles without WHERE'
        test_126: Test = Test()
        try:
            t_9330: 'SafeIdentifier'
            t_9331: 'SafeIdentifier'
            t_9332: 'SqlInt32'
            did_bubble_1311: 'bool33'
            try:
                t_9330 = sid_546('users')
                t_9331 = sid_546('x')
                t_9332 = SqlInt32(1)
                update(t_9330).set(t_9331, t_9332).to_sql()
                did_bubble_1311 = False
            except Exception37:
                did_bubble_1311 = True
            def fn_9329() -> 'str27':
                return 'update without WHERE should bubble'
            test_126.assert_(did_bubble_1311, fn_9329)
        finally:
            test_126.soft_fail_to_hard()
class TestCase149(TestCase46):
    def test___updateQueryBubblesWithoutSet__1887(self) -> None:
        'UpdateQuery bubbles without SET'
        test_127: Test = Test()
        try:
            t_9321: 'SafeIdentifier'
            t_9322: 'SqlBuilder'
            t_9325: 'SqlFragment'
            did_bubble_1313: 'bool33'
            try:
                t_9321 = sid_546('users')
                t_9322 = SqlBuilder()
                t_9322.append_safe('id = ')
                t_9322.append_int32(1)
                t_9325 = t_9322.accumulated
                update(t_9321).where(t_9325).to_sql()
                did_bubble_1313 = False
            except Exception37:
                did_bubble_1313 = True
            def fn_9320() -> 'str27':
                return 'update without SET should bubble'
            test_127.assert_(did_bubble_1313, fn_9320)
        finally:
            test_127.soft_fail_to_hard()
class TestCase150(TestCase46):
    def test___updateQueryWithLimit__1889(self) -> None:
        'UpdateQuery with limit'
        test_128: Test = Test()
        try:
            t_9307: 'SafeIdentifier' = sid_546('users')
            t_9308: 'SafeIdentifier' = sid_546('active')
            t_9309: 'SqlBoolean' = SqlBoolean(False)
            t_9310: 'UpdateQuery' = update(t_9307).set(t_9308, t_9309)
            t_9311: 'SqlBuilder' = SqlBuilder()
            t_9311.append_safe('last_login < ')
            t_9311.append_string('2024-01-01')
            t_4637: 'UpdateQuery'
            t_4637 = t_9310.where(t_9311.accumulated).limit(100)
            t_4638: 'SqlFragment'
            t_4638 = t_4637.to_sql()
            q_1315: 'SqlFragment' = t_4638
            t_9318: 'bool33' = q_1315.to_string() == "UPDATE users SET active = FALSE WHERE last_login < '2024-01-01' LIMIT 100"
            def fn_9306() -> 'str27':
                return 'update limit'
            test_128.assert_(t_9318, fn_9306)
        finally:
            test_128.soft_fail_to_hard()
class TestCase151(TestCase46):
    def test___updateQueryEscaping__1891(self) -> None:
        'UpdateQuery escaping'
        test_129: Test = Test()
        try:
            t_9293: 'SafeIdentifier' = sid_546('users')
            t_9294: 'SafeIdentifier' = sid_546('bio')
            t_9295: 'SqlString' = SqlString("It's a test")
            t_9296: 'UpdateQuery' = update(t_9293).set(t_9294, t_9295)
            t_9297: 'SqlBuilder' = SqlBuilder()
            t_9297.append_safe('id = ')
            t_9297.append_int32(1)
            t_4622: 'SqlFragment'
            t_4622 = t_9296.where(t_9297.accumulated).to_sql()
            q_1317: 'SqlFragment' = t_4622
            t_9304: 'bool33' = q_1317.to_string() == "UPDATE users SET bio = 'It''s a test' WHERE id = 1"
            def fn_9292() -> 'str27':
                return 'update escaping'
            test_129.assert_(t_9304, fn_9292)
        finally:
            test_129.soft_fail_to_hard()
class TestCase152(TestCase46):
    def test___deleteQueryBasic__1893(self) -> None:
        'DeleteQuery basic'
        test_130: Test = Test()
        try:
            t_9282: 'SafeIdentifier' = sid_546('users')
            t_9283: 'SqlBuilder' = SqlBuilder()
            t_9283.append_safe('id = ')
            t_9283.append_int32(1)
            t_9286: 'SqlFragment' = t_9283.accumulated
            t_4607: 'SqlFragment'
            t_4607 = delete_from(t_9282).where(t_9286).to_sql()
            q_1319: 'SqlFragment' = t_4607
            t_9290: 'bool33' = q_1319.to_string() == 'DELETE FROM users WHERE id = 1'
            def fn_9281() -> 'str27':
                return 'delete basic'
            test_130.assert_(t_9290, fn_9281)
        finally:
            test_130.soft_fail_to_hard()
class TestCase153(TestCase46):
    def test___deleteQueryMultipleWhere__1895(self) -> None:
        'DeleteQuery multiple WHERE'
        test_131: Test = Test()
        try:
            t_9266: 'SafeIdentifier' = sid_546('logs')
            t_9267: 'SqlBuilder' = SqlBuilder()
            t_9267.append_safe('created_at < ')
            t_9267.append_string('2024-01-01')
            t_9270: 'SqlFragment' = t_9267.accumulated
            t_9271: 'DeleteQuery' = delete_from(t_9266).where(t_9270)
            t_9272: 'SqlBuilder' = SqlBuilder()
            t_9272.append_safe('level = ')
            t_9272.append_string('debug')
            t_4595: 'SqlFragment'
            t_4595 = t_9271.where(t_9272.accumulated).to_sql()
            q_1321: 'SqlFragment' = t_4595
            t_9279: 'bool33' = q_1321.to_string() == "DELETE FROM logs WHERE created_at < '2024-01-01' AND level = 'debug'"
            def fn_9265() -> 'str27':
                return 'delete multi where'
            test_131.assert_(t_9279, fn_9265)
        finally:
            test_131.soft_fail_to_hard()
class TestCase154(TestCase46):
    def test___deleteQueryBubblesWithoutWhere__1898(self) -> None:
        'DeleteQuery bubbles without WHERE'
        test_132: Test = Test()
        try:
            did_bubble_1323: 'bool33'
            try:
                delete_from(sid_546('users')).to_sql()
                did_bubble_1323 = False
            except Exception37:
                did_bubble_1323 = True
            def fn_9261() -> 'str27':
                return 'delete without WHERE should bubble'
            test_132.assert_(did_bubble_1323, fn_9261)
        finally:
            test_132.soft_fail_to_hard()
class TestCase155(TestCase46):
    def test___deleteQueryOrWhere__1899(self) -> None:
        'DeleteQuery orWhere'
        test_133: Test = Test()
        try:
            t_9246: 'SafeIdentifier' = sid_546('sessions')
            t_9247: 'SqlBuilder' = SqlBuilder()
            t_9247.append_safe('expired = ')
            t_9247.append_boolean(True)
            t_9250: 'SqlFragment' = t_9247.accumulated
            t_9251: 'DeleteQuery' = delete_from(t_9246).where(t_9250)
            t_9252: 'SqlBuilder' = SqlBuilder()
            t_9252.append_safe('created_at < ')
            t_9252.append_string('2023-01-01')
            t_4574: 'SqlFragment'
            t_4574 = t_9251.or_where(t_9252.accumulated).to_sql()
            q_1325: 'SqlFragment' = t_4574
            t_9259: 'bool33' = q_1325.to_string() == "DELETE FROM sessions WHERE expired = TRUE OR created_at < '2023-01-01'"
            def fn_9245() -> 'str27':
                return 'delete orWhere'
            test_133.assert_(t_9259, fn_9245)
        finally:
            test_133.soft_fail_to_hard()
class TestCase156(TestCase46):
    def test___deleteQueryWithLimit__1902(self) -> None:
        'DeleteQuery with limit'
        test_134: Test = Test()
        try:
            t_9235: 'SafeIdentifier' = sid_546('logs')
            t_9236: 'SqlBuilder' = SqlBuilder()
            t_9236.append_safe('level = ')
            t_9236.append_string('debug')
            t_9239: 'SqlFragment' = t_9236.accumulated
            t_4555: 'DeleteQuery'
            t_4555 = delete_from(t_9235).where(t_9239).limit(1000)
            t_4556: 'SqlFragment'
            t_4556 = t_4555.to_sql()
            q_1327: 'SqlFragment' = t_4556
            t_9243: 'bool33' = q_1327.to_string() == "DELETE FROM logs WHERE level = 'debug' LIMIT 1000"
            def fn_9234() -> 'str27':
                return 'delete limit'
            test_134.assert_(t_9243, fn_9234)
        finally:
            test_134.soft_fail_to_hard()
class TestCase157(TestCase46):
    def test___orderByNullsNullsFirst__1904(self) -> None:
        'orderByNulls NULLS FIRST'
        test_135: Test = Test()
        try:
            t_9225: 'SafeIdentifier' = sid_546('users')
            t_9226: 'SafeIdentifier' = sid_546('email')
            t_9227: 'NullsFirst' = NullsFirst()
            q_1329: 'Query' = from_(t_9225).order_by_nulls(t_9226, True, t_9227)
            t_9232: 'bool33' = q_1329.to_sql().to_string() == 'SELECT * FROM users ORDER BY email ASC NULLS FIRST'
            def fn_9224() -> 'str27':
                return 'nulls first'
            test_135.assert_(t_9232, fn_9224)
        finally:
            test_135.soft_fail_to_hard()
class TestCase158(TestCase46):
    def test___orderByNullsNullsLast__1905(self) -> None:
        'orderByNulls NULLS LAST'
        test_136: Test = Test()
        try:
            t_9215: 'SafeIdentifier' = sid_546('users')
            t_9216: 'SafeIdentifier' = sid_546('score')
            t_9217: 'NullsLast' = NullsLast()
            q_1331: 'Query' = from_(t_9215).order_by_nulls(t_9216, False, t_9217)
            t_9222: 'bool33' = q_1331.to_sql().to_string() == 'SELECT * FROM users ORDER BY score DESC NULLS LAST'
            def fn_9214() -> 'str27':
                return 'nulls last'
            test_136.assert_(t_9222, fn_9214)
        finally:
            test_136.soft_fail_to_hard()
class TestCase159(TestCase46):
    def test___mixedOrderByAndOrderByNulls__1906(self) -> None:
        'mixed orderBy and orderByNulls'
        test_137: Test = Test()
        try:
            t_9203: 'SafeIdentifier' = sid_546('users')
            t_9204: 'SafeIdentifier' = sid_546('name')
            q_1333: 'Query' = from_(t_9203).order_by(t_9204, True).order_by_nulls(sid_546('email'), True, NullsFirst())
            t_9212: 'bool33' = q_1333.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC, email ASC NULLS FIRST'
            def fn_9202() -> 'str27':
                return 'mixed order'
            test_137.assert_(t_9212, fn_9202)
        finally:
            test_137.soft_fail_to_hard()
class TestCase160(TestCase46):
    def test___crossJoin__1907(self) -> None:
        'crossJoin'
        test_138: Test = Test()
        try:
            t_9194: 'SafeIdentifier' = sid_546('users')
            t_9195: 'SafeIdentifier' = sid_546('colors')
            q_1335: 'Query' = from_(t_9194).cross_join(t_9195)
            t_9200: 'bool33' = q_1335.to_sql().to_string() == 'SELECT * FROM users CROSS JOIN colors'
            def fn_9193() -> 'str27':
                return 'cross join'
            test_138.assert_(t_9200, fn_9193)
        finally:
            test_138.soft_fail_to_hard()
class TestCase161(TestCase46):
    def test___crossJoinCombinedWithOtherJoins__1908(self) -> None:
        'crossJoin combined with other joins'
        test_139: Test = Test()
        try:
            t_9180: 'SafeIdentifier' = sid_546('users')
            t_9181: 'SafeIdentifier' = sid_546('orders')
            t_9182: 'SqlBuilder' = SqlBuilder()
            t_9182.append_safe('users.id = orders.user_id')
            t_9184: 'SqlFragment' = t_9182.accumulated
            q_1337: 'Query' = from_(t_9180).inner_join(t_9181, t_9184).cross_join(sid_546('colors'))
            t_9191: 'bool33' = q_1337.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id CROSS JOIN colors'
            def fn_9179() -> 'str27':
                return 'cross + inner join'
            test_139.assert_(t_9191, fn_9179)
        finally:
            test_139.soft_fail_to_hard()
class TestCase162(TestCase46):
    def test___lockForUpdate__1910(self) -> None:
        'lock FOR UPDATE'
        test_140: Test = Test()
        try:
            t_9166: 'SafeIdentifier' = sid_546('users')
            t_9167: 'SqlBuilder' = SqlBuilder()
            t_9167.append_safe('id = ')
            t_9167.append_int32(1)
            t_9170: 'SqlFragment' = t_9167.accumulated
            q_1339: 'Query' = from_(t_9166).where(t_9170).lock(ForUpdate())
            t_9177: 'bool33' = q_1339.to_sql().to_string() == 'SELECT * FROM users WHERE id = 1 FOR UPDATE'
            def fn_9165() -> 'str27':
                return 'for update'
            test_140.assert_(t_9177, fn_9165)
        finally:
            test_140.soft_fail_to_hard()
class TestCase163(TestCase46):
    def test___lockForShare__1912(self) -> None:
        'lock FOR SHARE'
        test_141: Test = Test()
        try:
            t_9155: 'SafeIdentifier' = sid_546('users')
            t_9156: 'SafeIdentifier' = sid_546('name')
            q_1341: 'Query' = from_(t_9155).select((t_9156,)).lock(ForShare())
            t_9163: 'bool33' = q_1341.to_sql().to_string() == 'SELECT name FROM users FOR SHARE'
            def fn_9154() -> 'str27':
                return 'for share'
            test_141.assert_(t_9163, fn_9154)
        finally:
            test_141.soft_fail_to_hard()
class TestCase164(TestCase46):
    def test___lockWithFullQuery__1913(self) -> None:
        'lock with full query'
        test_142: Test = Test()
        try:
            t_9141: 'SafeIdentifier' = sid_546('accounts')
            t_9142: 'SqlBuilder' = SqlBuilder()
            t_9142.append_safe('id = ')
            t_9142.append_int32(42)
            t_9145: 'SqlFragment' = t_9142.accumulated
            t_4479: 'Query'
            t_4479 = from_(t_9141).where(t_9145).limit(1)
            t_9148: 'Query' = t_4479.lock(ForUpdate())
            q_1343: 'Query' = t_9148
            t_9152: 'bool33' = q_1343.to_sql().to_string() == 'SELECT * FROM accounts WHERE id = 42 LIMIT 1 FOR UPDATE'
            def fn_9140() -> 'str27':
                return 'lock full query'
            test_142.assert_(t_9152, fn_9140)
        finally:
            test_142.soft_fail_to_hard()
class TestCase165(TestCase46):
    def test___safeIdentifierAcceptsValidNames__1915(self) -> None:
        'safeIdentifier accepts valid names'
        test_149: Test = Test()
        try:
            t_4468: 'SafeIdentifier'
            t_4468 = safe_identifier('user_name')
            id_1381: 'SafeIdentifier' = t_4468
            t_9138: 'bool33' = id_1381.sql_value == 'user_name'
            def fn_9135() -> 'str27':
                return 'value should round-trip'
            test_149.assert_(t_9138, fn_9135)
        finally:
            test_149.soft_fail_to_hard()
class TestCase166(TestCase46):
    def test___safeIdentifierRejectsEmptyString__1916(self) -> None:
        'safeIdentifier rejects empty string'
        test_150: Test = Test()
        try:
            did_bubble_1383: 'bool33'
            try:
                safe_identifier('')
                did_bubble_1383 = False
            except Exception37:
                did_bubble_1383 = True
            def fn_9132() -> 'str27':
                return 'empty string should bubble'
            test_150.assert_(did_bubble_1383, fn_9132)
        finally:
            test_150.soft_fail_to_hard()
class TestCase167(TestCase46):
    def test___safeIdentifierRejectsLeadingDigit__1917(self) -> None:
        'safeIdentifier rejects leading digit'
        test_151: Test = Test()
        try:
            did_bubble_1385: 'bool33'
            try:
                safe_identifier('1col')
                did_bubble_1385 = False
            except Exception37:
                did_bubble_1385 = True
            def fn_9129() -> 'str27':
                return 'leading digit should bubble'
            test_151.assert_(did_bubble_1385, fn_9129)
        finally:
            test_151.soft_fail_to_hard()
class TestCase168(TestCase46):
    def test___safeIdentifierRejectsSqlMetacharacters__1918(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_152: Test = Test()
        try:
            cases_1387: 'Sequence29[str27]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_9126(c_1388: 'str27') -> 'None':
                did_bubble_1389: 'bool33'
                try:
                    safe_identifier(c_1388)
                    did_bubble_1389 = False
                except Exception37:
                    did_bubble_1389 = True
                def fn_9123() -> 'str27':
                    return str_cat_11468('should reject: ', c_1388)
                test_152.assert_(did_bubble_1389, fn_9123)
            list_for_each_11460(cases_1387, fn_9126)
        finally:
            test_152.soft_fail_to_hard()
class TestCase169(TestCase46):
    def test___tableDefFieldLookupFound__1919(self) -> None:
        'TableDef field lookup - found'
        test_153: Test = Test()
        try:
            t_4445: 'SafeIdentifier'
            t_4445 = safe_identifier('users')
            t_4446: 'SafeIdentifier' = t_4445
            t_4447: 'SafeIdentifier'
            t_4447 = safe_identifier('name')
            t_4448: 'SafeIdentifier' = t_4447
            t_9113: 'StringField' = StringField()
            t_9114: 'FieldDef' = FieldDef(t_4448, t_9113, False)
            t_4451: 'SafeIdentifier'
            t_4451 = safe_identifier('age')
            t_4452: 'SafeIdentifier' = t_4451
            t_9115: 'IntField' = IntField()
            t_9116: 'FieldDef' = FieldDef(t_4452, t_9115, False)
            td_1391: 'TableDef' = TableDef(t_4446, (t_9114, t_9116))
            t_4456: 'FieldDef'
            t_4456 = td_1391.field('age')
            f_1392: 'FieldDef' = t_4456
            t_9121: 'bool33' = f_1392.name.sql_value == 'age'
            def fn_9112() -> 'str27':
                return 'should find age field'
            test_153.assert_(t_9121, fn_9112)
        finally:
            test_153.soft_fail_to_hard()
class TestCase170(TestCase46):
    def test___tableDefFieldLookupNotFoundBubbles__1920(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_154: Test = Test()
        try:
            t_4436: 'SafeIdentifier'
            t_4436 = safe_identifier('users')
            t_4437: 'SafeIdentifier' = t_4436
            t_4438: 'SafeIdentifier'
            t_4438 = safe_identifier('name')
            t_4439: 'SafeIdentifier' = t_4438
            t_9107: 'StringField' = StringField()
            t_9108: 'FieldDef' = FieldDef(t_4439, t_9107, False)
            td_1394: 'TableDef' = TableDef(t_4437, (t_9108,))
            did_bubble_1395: 'bool33'
            try:
                td_1394.field('nonexistent')
                did_bubble_1395 = False
            except Exception37:
                did_bubble_1395 = True
            def fn_9106() -> 'str27':
                return 'unknown field should bubble'
            test_154.assert_(did_bubble_1395, fn_9106)
        finally:
            test_154.soft_fail_to_hard()
class TestCase171(TestCase46):
    def test___fieldDefNullableFlag__1921(self) -> None:
        'FieldDef nullable flag'
        test_155: Test = Test()
        try:
            t_4424: 'SafeIdentifier'
            t_4424 = safe_identifier('email')
            t_4425: 'SafeIdentifier' = t_4424
            t_9095: 'StringField' = StringField()
            required_1397: 'FieldDef' = FieldDef(t_4425, t_9095, False)
            t_4428: 'SafeIdentifier'
            t_4428 = safe_identifier('bio')
            t_4429: 'SafeIdentifier' = t_4428
            t_9097: 'StringField' = StringField()
            optional_1398: 'FieldDef' = FieldDef(t_4429, t_9097, True)
            t_9101: 'bool33' = not required_1397.nullable
            def fn_9094() -> 'str27':
                return 'required field should not be nullable'
            test_155.assert_(t_9101, fn_9094)
            t_9103: 'bool33' = optional_1398.nullable
            def fn_9093() -> 'str27':
                return 'optional field should be nullable'
            test_155.assert_(t_9103, fn_9093)
        finally:
            test_155.soft_fail_to_hard()
class TestCase172(TestCase46):
    def test___stringEscaping__1922(self) -> None:
        'string escaping'
        test_159: Test = Test()
        try:
            def build_1524(name_1526: 'str27') -> 'str27':
                t_9075: 'SqlBuilder' = SqlBuilder()
                t_9075.append_safe('select * from hi where name = ')
                t_9075.append_string(name_1526)
                return t_9075.accumulated.to_string()
            def build_wrong_1525(name_1528: 'str27') -> 'str27':
                return str_cat_11468("select * from hi where name = '", name_1528, "'")
            actual_1924: 'str27' = build_1524('world')
            t_9085: 'bool33' = actual_1924 == "select * from hi where name = 'world'"
            def fn_9082() -> 'str27':
                return str_cat_11468('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_1924, ')')
            test_159.assert_(t_9085, fn_9082)
            bobby_tables_1530: 'str27' = "Robert'); drop table hi;--"
            actual_1926: 'str27' = build_1524("Robert'); drop table hi;--")
            t_9089: 'bool33' = actual_1926 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_9081() -> 'str27':
                return str_cat_11468('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_1926, ')')
            test_159.assert_(t_9089, fn_9081)
            def fn_9080() -> 'str27':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_159.assert_(True, fn_9080)
        finally:
            test_159.soft_fail_to_hard()
class TestCase173(TestCase46):
    def test___stringEdgeCases__1930(self) -> None:
        'string edge cases'
        test_160: Test = Test()
        try:
            t_9043: 'SqlBuilder' = SqlBuilder()
            t_9043.append_safe('v = ')
            t_9043.append_string('')
            actual_1931: 'str27' = t_9043.accumulated.to_string()
            t_9049: 'bool33' = actual_1931 == "v = ''"
            def fn_9042() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_1931, ')')
            test_160.assert_(t_9049, fn_9042)
            t_9051: 'SqlBuilder' = SqlBuilder()
            t_9051.append_safe('v = ')
            t_9051.append_string("a''b")
            actual_1934: 'str27' = t_9051.accumulated.to_string()
            t_9057: 'bool33' = actual_1934 == "v = 'a''''b'"
            def fn_9041() -> 'str27':
                return str_cat_11468("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_1934, ')')
            test_160.assert_(t_9057, fn_9041)
            t_9059: 'SqlBuilder' = SqlBuilder()
            t_9059.append_safe('v = ')
            t_9059.append_string('Hello \u4e16\u754c')
            actual_1937: 'str27' = t_9059.accumulated.to_string()
            t_9065: 'bool33' = actual_1937 == "v = 'Hello \u4e16\u754c'"
            def fn_9040() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_1937, ')')
            test_160.assert_(t_9065, fn_9040)
            t_9067: 'SqlBuilder' = SqlBuilder()
            t_9067.append_safe('v = ')
            t_9067.append_string('Line1\nLine2')
            actual_1940: 'str27' = t_9067.accumulated.to_string()
            t_9073: 'bool33' = actual_1940 == "v = 'Line1\nLine2'"
            def fn_9039() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_1940, ')')
            test_160.assert_(t_9073, fn_9039)
        finally:
            test_160.soft_fail_to_hard()
class TestCase174(TestCase46):
    def test___numbersAndBooleans__1943(self) -> None:
        'numbers and booleans'
        test_161: Test = Test()
        try:
            t_9014: 'SqlBuilder' = SqlBuilder()
            t_9014.append_safe('select ')
            t_9014.append_int32(42)
            t_9014.append_safe(', ')
            t_9014.append_int64(43)
            t_9014.append_safe(', ')
            t_9014.append_float64(19.99)
            t_9014.append_safe(', ')
            t_9014.append_boolean(True)
            t_9014.append_safe(', ')
            t_9014.append_boolean(False)
            actual_1944: 'str27' = t_9014.accumulated.to_string()
            t_9028: 'bool33' = actual_1944 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_9013() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_1944, ')')
            test_161.assert_(t_9028, fn_9013)
            t_4369: 'date26'
            t_4369 = date_11493(2024, 12, 25)
            date_1533: 'date26' = t_4369
            t_9030: 'SqlBuilder' = SqlBuilder()
            t_9030.append_safe('insert into t values (')
            t_9030.append_date(date_1533)
            t_9030.append_safe(')')
            actual_1947: 'str27' = t_9030.accumulated.to_string()
            t_9037: 'bool33' = actual_1947 == "insert into t values ('2024-12-25')"
            def fn_9012() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_1947, ')')
            test_161.assert_(t_9037, fn_9012)
        finally:
            test_161.soft_fail_to_hard()
class TestCase175(TestCase46):
    def test___lists__1950(self) -> None:
        'lists'
        test_162: Test = Test()
        try:
            t_8958: 'SqlBuilder' = SqlBuilder()
            t_8958.append_safe('v IN (')
            t_8958.append_string_list(('a', 'b', "c'd"))
            t_8958.append_safe(')')
            actual_1951: 'str27' = t_8958.accumulated.to_string()
            t_8965: 'bool33' = actual_1951 == "v IN ('a', 'b', 'c''d')"
            def fn_8957() -> 'str27':
                return str_cat_11468("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_1951, ')')
            test_162.assert_(t_8965, fn_8957)
            t_8967: 'SqlBuilder' = SqlBuilder()
            t_8967.append_safe('v IN (')
            t_8967.append_int32_list((1, 2, 3))
            t_8967.append_safe(')')
            actual_1954: 'str27' = t_8967.accumulated.to_string()
            t_8974: 'bool33' = actual_1954 == 'v IN (1, 2, 3)'
            def fn_8956() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_1954, ')')
            test_162.assert_(t_8974, fn_8956)
            t_8976: 'SqlBuilder' = SqlBuilder()
            t_8976.append_safe('v IN (')
            t_8976.append_int64_list((1, 2))
            t_8976.append_safe(')')
            actual_1957: 'str27' = t_8976.accumulated.to_string()
            t_8983: 'bool33' = actual_1957 == 'v IN (1, 2)'
            def fn_8955() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_1957, ')')
            test_162.assert_(t_8983, fn_8955)
            t_8985: 'SqlBuilder' = SqlBuilder()
            t_8985.append_safe('v IN (')
            t_8985.append_float64_list((1.0, 2.0))
            t_8985.append_safe(')')
            actual_1960: 'str27' = t_8985.accumulated.to_string()
            t_8992: 'bool33' = actual_1960 == 'v IN (1.0, 2.0)'
            def fn_8954() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_1960, ')')
            test_162.assert_(t_8992, fn_8954)
            t_8994: 'SqlBuilder' = SqlBuilder()
            t_8994.append_safe('v IN (')
            t_8994.append_boolean_list((True, False))
            t_8994.append_safe(')')
            actual_1963: 'str27' = t_8994.accumulated.to_string()
            t_9001: 'bool33' = actual_1963 == 'v IN (TRUE, FALSE)'
            def fn_8953() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_1963, ')')
            test_162.assert_(t_9001, fn_8953)
            t_4341: 'date26'
            t_4341 = date_11493(2024, 1, 1)
            t_4342: 'date26' = t_4341
            t_4343: 'date26'
            t_4343 = date_11493(2024, 12, 25)
            t_4344: 'date26' = t_4343
            dates_1535: 'Sequence29[date26]' = (t_4342, t_4344)
            t_9003: 'SqlBuilder' = SqlBuilder()
            t_9003.append_safe('v IN (')
            t_9003.append_date_list(dates_1535)
            t_9003.append_safe(')')
            actual_1966: 'str27' = t_9003.accumulated.to_string()
            t_9010: 'bool33' = actual_1966 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_8952() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_1966, ')')
            test_162.assert_(t_9010, fn_8952)
        finally:
            test_162.soft_fail_to_hard()
class TestCase176(TestCase46):
    def test___sqlFloat64_naNRendersAsNull__1969(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_163: Test = Test()
        try:
            nan_1537: 'float38'
            nan_1537 = 0.0 / 0.0
            t_8944: 'SqlBuilder' = SqlBuilder()
            t_8944.append_safe('v = ')
            t_8944.append_float64(nan_1537)
            actual_1970: 'str27' = t_8944.accumulated.to_string()
            t_8950: 'bool33' = actual_1970 == 'v = NULL'
            def fn_8943() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_1970, ')')
            test_163.assert_(t_8950, fn_8943)
        finally:
            test_163.soft_fail_to_hard()
class TestCase177(TestCase46):
    def test___sqlFloat64_infinityRendersAsNull__1973(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_164: Test = Test()
        try:
            inf_1539: 'float38'
            inf_1539 = 1.0 / 0.0
            t_8935: 'SqlBuilder' = SqlBuilder()
            t_8935.append_safe('v = ')
            t_8935.append_float64(inf_1539)
            actual_1974: 'str27' = t_8935.accumulated.to_string()
            t_8941: 'bool33' = actual_1974 == 'v = NULL'
            def fn_8934() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_1974, ')')
            test_164.assert_(t_8941, fn_8934)
        finally:
            test_164.soft_fail_to_hard()
class TestCase178(TestCase46):
    def test___sqlFloat64_negativeInfinityRendersAsNull__1977(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_165: Test = Test()
        try:
            ninf_1541: 'float38'
            ninf_1541 = -1.0 / 0.0
            t_8926: 'SqlBuilder' = SqlBuilder()
            t_8926.append_safe('v = ')
            t_8926.append_float64(ninf_1541)
            actual_1978: 'str27' = t_8926.accumulated.to_string()
            t_8932: 'bool33' = actual_1978 == 'v = NULL'
            def fn_8925() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_1978, ')')
            test_165.assert_(t_8932, fn_8925)
        finally:
            test_165.soft_fail_to_hard()
class TestCase179(TestCase46):
    def test___sqlFloat64_normalValuesStillWork__1981(self) -> None:
        'SqlFloat64 normal values still work'
        test_166: Test = Test()
        try:
            t_8901: 'SqlBuilder' = SqlBuilder()
            t_8901.append_safe('v = ')
            t_8901.append_float64(3.14)
            actual_1982: 'str27' = t_8901.accumulated.to_string()
            t_8907: 'bool33' = actual_1982 == 'v = 3.14'
            def fn_8900() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_1982, ')')
            test_166.assert_(t_8907, fn_8900)
            t_8909: 'SqlBuilder' = SqlBuilder()
            t_8909.append_safe('v = ')
            t_8909.append_float64(0.0)
            actual_1985: 'str27' = t_8909.accumulated.to_string()
            t_8915: 'bool33' = actual_1985 == 'v = 0.0'
            def fn_8899() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_1985, ')')
            test_166.assert_(t_8915, fn_8899)
            t_8917: 'SqlBuilder' = SqlBuilder()
            t_8917.append_safe('v = ')
            t_8917.append_float64(-42.5)
            actual_1988: 'str27' = t_8917.accumulated.to_string()
            t_8923: 'bool33' = actual_1988 == 'v = -42.5'
            def fn_8898() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_1988, ')')
            test_166.assert_(t_8923, fn_8898)
        finally:
            test_166.soft_fail_to_hard()
class TestCase180(TestCase46):
    def test___sqlDateRendersWithQuotes__1991(self) -> None:
        'SqlDate renders with quotes'
        test_167: Test = Test()
        try:
            t_4237: 'date26'
            t_4237 = date_11493(2024, 6, 15)
            d_1544: 'date26' = t_4237
            t_8890: 'SqlBuilder' = SqlBuilder()
            t_8890.append_safe('v = ')
            t_8890.append_date(d_1544)
            actual_1992: 'str27' = t_8890.accumulated.to_string()
            t_8896: 'bool33' = actual_1992 == "v = '2024-06-15'"
            def fn_8889() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_1992, ')')
            test_167.assert_(t_8896, fn_8889)
        finally:
            test_167.soft_fail_to_hard()
class TestCase181(TestCase46):
    def test___nesting__1995(self) -> None:
        'nesting'
        test_168: Test = Test()
        try:
            name_1546: 'str27' = 'Someone'
            t_8858: 'SqlBuilder' = SqlBuilder()
            t_8858.append_safe('where p.last_name = ')
            t_8858.append_string('Someone')
            condition_1547: 'SqlFragment' = t_8858.accumulated
            t_8862: 'SqlBuilder' = SqlBuilder()
            t_8862.append_safe('select p.id from person p ')
            t_8862.append_fragment(condition_1547)
            actual_1997: 'str27' = t_8862.accumulated.to_string()
            t_8868: 'bool33' = actual_1997 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_8857() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1997, ')')
            test_168.assert_(t_8868, fn_8857)
            t_8870: 'SqlBuilder' = SqlBuilder()
            t_8870.append_safe('select p.id from person p ')
            t_8870.append_part(condition_1547.to_source())
            actual_2000: 'str27' = t_8870.accumulated.to_string()
            t_8877: 'bool33' = actual_2000 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_8856() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2000, ')')
            test_168.assert_(t_8877, fn_8856)
            parts_1548: 'Sequence29[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_8881: 'SqlBuilder' = SqlBuilder()
            t_8881.append_safe('select ')
            t_8881.append_part_list(parts_1548)
            actual_2003: 'str27' = t_8881.accumulated.to_string()
            t_8887: 'bool33' = actual_2003 == "select 'a''b', 3"
            def fn_8855() -> 'str27':
                return str_cat_11468('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_2003, ')')
            test_168.assert_(t_8887, fn_8855)
        finally:
            test_168.soft_fail_to_hard()
