from temper_std.testing import Test
from builtins import str as str27, bool as bool33, Exception as Exception37, int as int31, float as float38
from unittest import TestCase as TestCase46
from types import MappingProxyType as MappingProxyType32
from typing import Sequence as Sequence29
from datetime import date as date26
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_10960, pair_10964, changeset, Changeset, mapped_has_10937, len_10940, list_get_10948, str_cat_10942, list_for_each_10934, SqlFragment, from_, Query, SqlBuilder, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, update, UpdateQuery, SqlBoolean, delete_from, DeleteQuery, date_10967, SqlPart
def csid_503(name_648: 'str27') -> 'SafeIdentifier':
    t_6032: 'SafeIdentifier'
    t_6032 = safe_identifier(name_648)
    return t_6032
def user_table_504() -> 'TableDef':
    return TableDef(csid_503('users'), (FieldDef(csid_503('name'), StringField(), False), FieldDef(csid_503('email'), StringField(), False), FieldDef(csid_503('age'), IntField(), True), FieldDef(csid_503('score'), FloatField(), True), FieldDef(csid_503('active'), BoolField(), True)))
class TestCase45(TestCase46):
    def test___castWhitelistsAllowedFields__1546(self) -> None:
        'cast whitelists allowed fields'
        test_24: Test = Test()
        try:
            params_652: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'Alice'), pair_10964('email', 'alice@example.com'), pair_10964('admin', 'true')))
            t_10651: 'TableDef' = user_table_504()
            t_10652: 'SafeIdentifier' = csid_503('name')
            t_10653: 'SafeIdentifier' = csid_503('email')
            cs_653: 'Changeset' = changeset(t_10651, params_652).cast((t_10652, t_10653))
            t_10656: 'bool33' = mapped_has_10937(cs_653.changes, 'name')
            def fn_10646() -> 'str27':
                return 'name should be in changes'
            test_24.assert_(t_10656, fn_10646)
            t_10660: 'bool33' = mapped_has_10937(cs_653.changes, 'email')
            def fn_10645() -> 'str27':
                return 'email should be in changes'
            test_24.assert_(t_10660, fn_10645)
            t_10666: 'bool33' = not mapped_has_10937(cs_653.changes, 'admin')
            def fn_10644() -> 'str27':
                return 'admin must be dropped (not in whitelist)'
            test_24.assert_(t_10666, fn_10644)
            t_10668: 'bool33' = cs_653.is_valid
            def fn_10643() -> 'str27':
                return 'should still be valid'
            test_24.assert_(t_10668, fn_10643)
        finally:
            test_24.soft_fail_to_hard()
class TestCase47(TestCase46):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__1547(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_25: Test = Test()
        try:
            params_655: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'Alice'), pair_10964('email', 'alice@example.com')))
            t_10629: 'TableDef' = user_table_504()
            t_10630: 'SafeIdentifier' = csid_503('name')
            cs_656: 'Changeset' = changeset(t_10629, params_655).cast((t_10630,)).cast((csid_503('email'),))
            t_10637: 'bool33' = not mapped_has_10937(cs_656.changes, 'name')
            def fn_10625() -> 'str27':
                return 'name must be excluded by second cast'
            test_25.assert_(t_10637, fn_10625)
            t_10640: 'bool33' = mapped_has_10937(cs_656.changes, 'email')
            def fn_10624() -> 'str27':
                return 'email should be present'
            test_25.assert_(t_10640, fn_10624)
        finally:
            test_25.soft_fail_to_hard()
class TestCase48(TestCase46):
    def test___castIgnoresEmptyStringValues__1548(self) -> None:
        'cast ignores empty string values'
        test_26: Test = Test()
        try:
            params_658: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', ''), pair_10964('email', 'bob@example.com')))
            t_10611: 'TableDef' = user_table_504()
            t_10612: 'SafeIdentifier' = csid_503('name')
            t_10613: 'SafeIdentifier' = csid_503('email')
            cs_659: 'Changeset' = changeset(t_10611, params_658).cast((t_10612, t_10613))
            t_10618: 'bool33' = not mapped_has_10937(cs_659.changes, 'name')
            def fn_10607() -> 'str27':
                return 'empty name should not be in changes'
            test_26.assert_(t_10618, fn_10607)
            t_10621: 'bool33' = mapped_has_10937(cs_659.changes, 'email')
            def fn_10606() -> 'str27':
                return 'email should be in changes'
            test_26.assert_(t_10621, fn_10606)
        finally:
            test_26.soft_fail_to_hard()
class TestCase49(TestCase46):
    def test___validateRequiredPassesWhenFieldPresent__1549(self) -> None:
        'validateRequired passes when field present'
        test_27: Test = Test()
        try:
            params_661: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'Alice'),))
            t_10593: 'TableDef' = user_table_504()
            t_10594: 'SafeIdentifier' = csid_503('name')
            cs_662: 'Changeset' = changeset(t_10593, params_661).cast((t_10594,)).validate_required((csid_503('name'),))
            t_10598: 'bool33' = cs_662.is_valid
            def fn_10590() -> 'str27':
                return 'should be valid'
            test_27.assert_(t_10598, fn_10590)
            t_10604: 'bool33' = len_10940(cs_662.errors) == 0
            def fn_10589() -> 'str27':
                return 'no errors expected'
            test_27.assert_(t_10604, fn_10589)
        finally:
            test_27.soft_fail_to_hard()
class TestCase50(TestCase46):
    def test___validateRequiredFailsWhenFieldMissing__1550(self) -> None:
        'validateRequired fails when field missing'
        test_28: Test = Test()
        try:
            params_664: 'MappingProxyType32[str27, str27]' = map_constructor_10960(())
            t_10569: 'TableDef' = user_table_504()
            t_10570: 'SafeIdentifier' = csid_503('name')
            cs_665: 'Changeset' = changeset(t_10569, params_664).cast((t_10570,)).validate_required((csid_503('name'),))
            t_10576: 'bool33' = not cs_665.is_valid
            def fn_10567() -> 'str27':
                return 'should be invalid'
            test_28.assert_(t_10576, fn_10567)
            t_10581: 'bool33' = len_10940(cs_665.errors) == 1
            def fn_10566() -> 'str27':
                return 'should have one error'
            test_28.assert_(t_10581, fn_10566)
            t_10587: 'bool33' = list_get_10948(cs_665.errors, 0).field == 'name'
            def fn_10565() -> 'str27':
                return 'error should name the field'
            test_28.assert_(t_10587, fn_10565)
        finally:
            test_28.soft_fail_to_hard()
class TestCase51(TestCase46):
    def test___validateLengthPassesWithinRange__1551(self) -> None:
        'validateLength passes within range'
        test_29: Test = Test()
        try:
            params_667: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'Alice'),))
            t_10557: 'TableDef' = user_table_504()
            t_10558: 'SafeIdentifier' = csid_503('name')
            cs_668: 'Changeset' = changeset(t_10557, params_667).cast((t_10558,)).validate_length(csid_503('name'), 2, 50)
            t_10562: 'bool33' = cs_668.is_valid
            def fn_10554() -> 'str27':
                return 'should be valid'
            test_29.assert_(t_10562, fn_10554)
        finally:
            test_29.soft_fail_to_hard()
class TestCase52(TestCase46):
    def test___validateLengthFailsWhenTooShort__1552(self) -> None:
        'validateLength fails when too short'
        test_30: Test = Test()
        try:
            params_670: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'A'),))
            t_10545: 'TableDef' = user_table_504()
            t_10546: 'SafeIdentifier' = csid_503('name')
            cs_671: 'Changeset' = changeset(t_10545, params_670).cast((t_10546,)).validate_length(csid_503('name'), 2, 50)
            t_10552: 'bool33' = not cs_671.is_valid
            def fn_10542() -> 'str27':
                return 'should be invalid'
            test_30.assert_(t_10552, fn_10542)
        finally:
            test_30.soft_fail_to_hard()
class TestCase53(TestCase46):
    def test___validateLengthFailsWhenTooLong__1553(self) -> None:
        'validateLength fails when too long'
        test_31: Test = Test()
        try:
            params_673: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_10533: 'TableDef' = user_table_504()
            t_10534: 'SafeIdentifier' = csid_503('name')
            cs_674: 'Changeset' = changeset(t_10533, params_673).cast((t_10534,)).validate_length(csid_503('name'), 2, 10)
            t_10540: 'bool33' = not cs_674.is_valid
            def fn_10530() -> 'str27':
                return 'should be invalid'
            test_31.assert_(t_10540, fn_10530)
        finally:
            test_31.soft_fail_to_hard()
class TestCase54(TestCase46):
    def test___validateIntPassesForValidInteger__1554(self) -> None:
        'validateInt passes for valid integer'
        test_32: Test = Test()
        try:
            params_676: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('age', '30'),))
            t_10522: 'TableDef' = user_table_504()
            t_10523: 'SafeIdentifier' = csid_503('age')
            cs_677: 'Changeset' = changeset(t_10522, params_676).cast((t_10523,)).validate_int(csid_503('age'))
            t_10527: 'bool33' = cs_677.is_valid
            def fn_10519() -> 'str27':
                return 'should be valid'
            test_32.assert_(t_10527, fn_10519)
        finally:
            test_32.soft_fail_to_hard()
class TestCase55(TestCase46):
    def test___validateIntFailsForNonInteger__1555(self) -> None:
        'validateInt fails for non-integer'
        test_33: Test = Test()
        try:
            params_679: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('age', 'not-a-number'),))
            t_10510: 'TableDef' = user_table_504()
            t_10511: 'SafeIdentifier' = csid_503('age')
            cs_680: 'Changeset' = changeset(t_10510, params_679).cast((t_10511,)).validate_int(csid_503('age'))
            t_10517: 'bool33' = not cs_680.is_valid
            def fn_10507() -> 'str27':
                return 'should be invalid'
            test_33.assert_(t_10517, fn_10507)
        finally:
            test_33.soft_fail_to_hard()
class TestCase56(TestCase46):
    def test___validateFloatPassesForValidFloat__1556(self) -> None:
        'validateFloat passes for valid float'
        test_34: Test = Test()
        try:
            params_682: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('score', '9.5'),))
            t_10499: 'TableDef' = user_table_504()
            t_10500: 'SafeIdentifier' = csid_503('score')
            cs_683: 'Changeset' = changeset(t_10499, params_682).cast((t_10500,)).validate_float(csid_503('score'))
            t_10504: 'bool33' = cs_683.is_valid
            def fn_10496() -> 'str27':
                return 'should be valid'
            test_34.assert_(t_10504, fn_10496)
        finally:
            test_34.soft_fail_to_hard()
class TestCase57(TestCase46):
    def test___validateInt64_passesForValid64_bitInteger__1557(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_35: Test = Test()
        try:
            params_685: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('age', '9999999999'),))
            t_10488: 'TableDef' = user_table_504()
            t_10489: 'SafeIdentifier' = csid_503('age')
            cs_686: 'Changeset' = changeset(t_10488, params_685).cast((t_10489,)).validate_int64(csid_503('age'))
            t_10493: 'bool33' = cs_686.is_valid
            def fn_10485() -> 'str27':
                return 'should be valid'
            test_35.assert_(t_10493, fn_10485)
        finally:
            test_35.soft_fail_to_hard()
class TestCase58(TestCase46):
    def test___validateInt64_failsForNonInteger__1558(self) -> None:
        'validateInt64 fails for non-integer'
        test_36: Test = Test()
        try:
            params_688: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('age', 'not-a-number'),))
            t_10476: 'TableDef' = user_table_504()
            t_10477: 'SafeIdentifier' = csid_503('age')
            cs_689: 'Changeset' = changeset(t_10476, params_688).cast((t_10477,)).validate_int64(csid_503('age'))
            t_10483: 'bool33' = not cs_689.is_valid
            def fn_10473() -> 'str27':
                return 'should be invalid'
            test_36.assert_(t_10483, fn_10473)
        finally:
            test_36.soft_fail_to_hard()
class TestCase59(TestCase46):
    def test___validateBoolAcceptsTrue1_yesOn__1559(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_37: Test = Test()
        try:
            def fn_10470(v_691: 'str27') -> 'None':
                params_692: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('active', v_691),))
                t_10462: 'TableDef' = user_table_504()
                t_10463: 'SafeIdentifier' = csid_503('active')
                cs_693: 'Changeset' = changeset(t_10462, params_692).cast((t_10463,)).validate_bool(csid_503('active'))
                t_10467: 'bool33' = cs_693.is_valid
                def fn_10459() -> 'str27':
                    return str_cat_10942('should accept: ', v_691)
                test_37.assert_(t_10467, fn_10459)
            list_for_each_10934(('true', '1', 'yes', 'on'), fn_10470)
        finally:
            test_37.soft_fail_to_hard()
class TestCase60(TestCase46):
    def test___validateBoolAcceptsFalse0_noOff__1560(self) -> None:
        'validateBool accepts false/0/no/off'
        test_38: Test = Test()
        try:
            def fn_10456(v_695: 'str27') -> 'None':
                params_696: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('active', v_695),))
                t_10448: 'TableDef' = user_table_504()
                t_10449: 'SafeIdentifier' = csid_503('active')
                cs_697: 'Changeset' = changeset(t_10448, params_696).cast((t_10449,)).validate_bool(csid_503('active'))
                t_10453: 'bool33' = cs_697.is_valid
                def fn_10445() -> 'str27':
                    return str_cat_10942('should accept: ', v_695)
                test_38.assert_(t_10453, fn_10445)
            list_for_each_10934(('false', '0', 'no', 'off'), fn_10456)
        finally:
            test_38.soft_fail_to_hard()
class TestCase61(TestCase46):
    def test___validateBoolRejectsAmbiguousValues__1561(self) -> None:
        'validateBool rejects ambiguous values'
        test_39: Test = Test()
        try:
            def fn_10442(v_699: 'str27') -> 'None':
                params_700: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('active', v_699),))
                t_10433: 'TableDef' = user_table_504()
                t_10434: 'SafeIdentifier' = csid_503('active')
                cs_701: 'Changeset' = changeset(t_10433, params_700).cast((t_10434,)).validate_bool(csid_503('active'))
                t_10440: 'bool33' = not cs_701.is_valid
                def fn_10430() -> 'str27':
                    return str_cat_10942('should reject ambiguous: ', v_699)
                test_39.assert_(t_10440, fn_10430)
            list_for_each_10934(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_10442)
        finally:
            test_39.soft_fail_to_hard()
class TestCase62(TestCase46):
    def test___toInsertSqlEscapesBobbyTables__1562(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_40: Test = Test()
        try:
            params_703: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', "Robert'); DROP TABLE users;--"), pair_10964('email', 'bobby@evil.com')))
            t_10418: 'TableDef' = user_table_504()
            t_10419: 'SafeIdentifier' = csid_503('name')
            t_10420: 'SafeIdentifier' = csid_503('email')
            cs_704: 'Changeset' = changeset(t_10418, params_703).cast((t_10419, t_10420)).validate_required((csid_503('name'), csid_503('email')))
            t_5833: 'SqlFragment'
            t_5833 = cs_704.to_insert_sql()
            sql_frag_705: 'SqlFragment' = t_5833
            s_706: 'str27' = sql_frag_705.to_string()
            t_10427: 'bool33' = s_706.find("''") >= 0
            def fn_10414() -> 'str27':
                return str_cat_10942('single quote must be doubled: ', s_706)
            test_40.assert_(t_10427, fn_10414)
        finally:
            test_40.soft_fail_to_hard()
class TestCase63(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForStringField__1563(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_41: Test = Test()
        try:
            params_708: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'Alice'), pair_10964('email', 'a@example.com')))
            t_10398: 'TableDef' = user_table_504()
            t_10399: 'SafeIdentifier' = csid_503('name')
            t_10400: 'SafeIdentifier' = csid_503('email')
            cs_709: 'Changeset' = changeset(t_10398, params_708).cast((t_10399, t_10400)).validate_required((csid_503('name'), csid_503('email')))
            t_5812: 'SqlFragment'
            t_5812 = cs_709.to_insert_sql()
            sql_frag_710: 'SqlFragment' = t_5812
            s_711: 'str27' = sql_frag_710.to_string()
            t_10407: 'bool33' = s_711.find('INSERT INTO users') >= 0
            def fn_10394() -> 'str27':
                return str_cat_10942('has INSERT INTO: ', s_711)
            test_41.assert_(t_10407, fn_10394)
            t_10411: 'bool33' = s_711.find("'Alice'") >= 0
            def fn_10393() -> 'str27':
                return str_cat_10942('has quoted name: ', s_711)
            test_41.assert_(t_10411, fn_10393)
        finally:
            test_41.soft_fail_to_hard()
class TestCase64(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForIntField__1564(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_42: Test = Test()
        try:
            params_713: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'Bob'), pair_10964('email', 'b@example.com'), pair_10964('age', '25')))
            t_10380: 'TableDef' = user_table_504()
            t_10381: 'SafeIdentifier' = csid_503('name')
            t_10382: 'SafeIdentifier' = csid_503('email')
            t_10383: 'SafeIdentifier' = csid_503('age')
            cs_714: 'Changeset' = changeset(t_10380, params_713).cast((t_10381, t_10382, t_10383)).validate_required((csid_503('name'), csid_503('email')))
            t_5795: 'SqlFragment'
            t_5795 = cs_714.to_insert_sql()
            sql_frag_715: 'SqlFragment' = t_5795
            s_716: 'str27' = sql_frag_715.to_string()
            t_10390: 'bool33' = s_716.find('25') >= 0
            def fn_10375() -> 'str27':
                return str_cat_10942('age rendered unquoted: ', s_716)
            test_42.assert_(t_10390, fn_10375)
        finally:
            test_42.soft_fail_to_hard()
class TestCase65(TestCase46):
    def test___toInsertSqlBubblesOnInvalidChangeset__1565(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_43: Test = Test()
        try:
            params_718: 'MappingProxyType32[str27, str27]' = map_constructor_10960(())
            t_10368: 'TableDef' = user_table_504()
            t_10369: 'SafeIdentifier' = csid_503('name')
            cs_719: 'Changeset' = changeset(t_10368, params_718).cast((t_10369,)).validate_required((csid_503('name'),))
            did_bubble_720: 'bool33'
            try:
                cs_719.to_insert_sql()
                did_bubble_720 = False
            except Exception37:
                did_bubble_720 = True
            def fn_10366() -> 'str27':
                return 'invalid changeset should bubble'
            test_43.assert_(did_bubble_720, fn_10366)
        finally:
            test_43.soft_fail_to_hard()
class TestCase66(TestCase46):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__1566(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_44: Test = Test()
        try:
            strict_table_722: 'TableDef' = TableDef(csid_503('posts'), (FieldDef(csid_503('title'), StringField(), False), FieldDef(csid_503('body'), StringField(), True)))
            params_723: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('body', 'hello'),))
            t_10359: 'SafeIdentifier' = csid_503('body')
            cs_724: 'Changeset' = changeset(strict_table_722, params_723).cast((t_10359,))
            t_10361: 'bool33' = cs_724.is_valid
            def fn_10348() -> 'str27':
                return 'changeset should appear valid (no explicit validation run)'
            test_44.assert_(t_10361, fn_10348)
            did_bubble_725: 'bool33'
            try:
                cs_724.to_insert_sql()
                did_bubble_725 = False
            except Exception37:
                did_bubble_725 = True
            def fn_10347() -> 'str27':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_44.assert_(did_bubble_725, fn_10347)
        finally:
            test_44.soft_fail_to_hard()
class TestCase67(TestCase46):
    def test___toUpdateSqlProducesCorrectSql__1567(self) -> None:
        'toUpdateSql produces correct SQL'
        test_45: Test = Test()
        try:
            params_727: 'MappingProxyType32[str27, str27]' = map_constructor_10960((pair_10964('name', 'Bob'),))
            t_10338: 'TableDef' = user_table_504()
            t_10339: 'SafeIdentifier' = csid_503('name')
            cs_728: 'Changeset' = changeset(t_10338, params_727).cast((t_10339,)).validate_required((csid_503('name'),))
            t_5755: 'SqlFragment'
            t_5755 = cs_728.to_update_sql(42)
            sql_frag_729: 'SqlFragment' = t_5755
            s_730: 'str27' = sql_frag_729.to_string()
            t_10345: 'bool33' = s_730 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_10335() -> 'str27':
                return str_cat_10942('got: ', s_730)
            test_45.assert_(t_10345, fn_10335)
        finally:
            test_45.soft_fail_to_hard()
class TestCase68(TestCase46):
    def test___toUpdateSqlBubblesOnInvalidChangeset__1568(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_46: Test = Test()
        try:
            params_732: 'MappingProxyType32[str27, str27]' = map_constructor_10960(())
            t_10328: 'TableDef' = user_table_504()
            t_10329: 'SafeIdentifier' = csid_503('name')
            cs_733: 'Changeset' = changeset(t_10328, params_732).cast((t_10329,)).validate_required((csid_503('name'),))
            did_bubble_734: 'bool33'
            try:
                cs_733.to_update_sql(1)
                did_bubble_734 = False
            except Exception37:
                did_bubble_734 = True
            def fn_10326() -> 'str27':
                return 'invalid changeset should bubble'
            test_46.assert_(did_bubble_734, fn_10326)
        finally:
            test_46.soft_fail_to_hard()
def sid_505(name_1039: 'str27') -> 'SafeIdentifier':
    t_5241: 'SafeIdentifier'
    t_5241 = safe_identifier(name_1039)
    return t_5241
class TestCase69(TestCase46):
    def test___bareFromProducesSelect__1644(self) -> None:
        'bare from produces SELECT *'
        test_47: Test = Test()
        try:
            q_1042: 'Query' = from_(sid_505('users'))
            t_9837: 'bool33' = q_1042.to_sql().to_string() == 'SELECT * FROM users'
            def fn_9832() -> 'str27':
                return 'bare query'
            test_47.assert_(t_9837, fn_9832)
        finally:
            test_47.soft_fail_to_hard()
class TestCase70(TestCase46):
    def test___selectRestrictsColumns__1645(self) -> None:
        'select restricts columns'
        test_48: Test = Test()
        try:
            t_9823: 'SafeIdentifier' = sid_505('users')
            t_9824: 'SafeIdentifier' = sid_505('id')
            t_9825: 'SafeIdentifier' = sid_505('name')
            q_1044: 'Query' = from_(t_9823).select((t_9824, t_9825))
            t_9830: 'bool33' = q_1044.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_9822() -> 'str27':
                return 'select columns'
            test_48.assert_(t_9830, fn_9822)
        finally:
            test_48.soft_fail_to_hard()
class TestCase71(TestCase46):
    def test___whereAddsConditionWithIntValue__1646(self) -> None:
        'where adds condition with int value'
        test_49: Test = Test()
        try:
            t_9811: 'SafeIdentifier' = sid_505('users')
            t_9812: 'SqlBuilder' = SqlBuilder()
            t_9812.append_safe('age > ')
            t_9812.append_int32(18)
            t_9815: 'SqlFragment' = t_9812.accumulated
            q_1046: 'Query' = from_(t_9811).where(t_9815)
            t_9820: 'bool33' = q_1046.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_9810() -> 'str27':
                return 'where int'
            test_49.assert_(t_9820, fn_9810)
        finally:
            test_49.soft_fail_to_hard()
class TestCase72(TestCase46):
    def test___whereAddsConditionWithBoolValue__1648(self) -> None:
        'where adds condition with bool value'
        test_50: Test = Test()
        try:
            t_9799: 'SafeIdentifier' = sid_505('users')
            t_9800: 'SqlBuilder' = SqlBuilder()
            t_9800.append_safe('active = ')
            t_9800.append_boolean(True)
            t_9803: 'SqlFragment' = t_9800.accumulated
            q_1048: 'Query' = from_(t_9799).where(t_9803)
            t_9808: 'bool33' = q_1048.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_9798() -> 'str27':
                return 'where bool'
            test_50.assert_(t_9808, fn_9798)
        finally:
            test_50.soft_fail_to_hard()
class TestCase73(TestCase46):
    def test___chainedWhereUsesAnd__1650(self) -> None:
        'chained where uses AND'
        test_51: Test = Test()
        try:
            t_9782: 'SafeIdentifier' = sid_505('users')
            t_9783: 'SqlBuilder' = SqlBuilder()
            t_9783.append_safe('age > ')
            t_9783.append_int32(18)
            t_9786: 'SqlFragment' = t_9783.accumulated
            t_9787: 'Query' = from_(t_9782).where(t_9786)
            t_9788: 'SqlBuilder' = SqlBuilder()
            t_9788.append_safe('active = ')
            t_9788.append_boolean(True)
            q_1050: 'Query' = t_9787.where(t_9788.accumulated)
            t_9796: 'bool33' = q_1050.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_9781() -> 'str27':
                return 'chained where'
            test_51.assert_(t_9796, fn_9781)
        finally:
            test_51.soft_fail_to_hard()
class TestCase74(TestCase46):
    def test___orderByAsc__1653(self) -> None:
        'orderBy ASC'
        test_52: Test = Test()
        try:
            t_9773: 'SafeIdentifier' = sid_505('users')
            t_9774: 'SafeIdentifier' = sid_505('name')
            q_1052: 'Query' = from_(t_9773).order_by(t_9774, True)
            t_9779: 'bool33' = q_1052.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_9772() -> 'str27':
                return 'order asc'
            test_52.assert_(t_9779, fn_9772)
        finally:
            test_52.soft_fail_to_hard()
class TestCase75(TestCase46):
    def test___orderByDesc__1654(self) -> None:
        'orderBy DESC'
        test_53: Test = Test()
        try:
            t_9764: 'SafeIdentifier' = sid_505('users')
            t_9765: 'SafeIdentifier' = sid_505('created_at')
            q_1054: 'Query' = from_(t_9764).order_by(t_9765, False)
            t_9770: 'bool33' = q_1054.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_9763() -> 'str27':
                return 'order desc'
            test_53.assert_(t_9770, fn_9763)
        finally:
            test_53.soft_fail_to_hard()
class TestCase76(TestCase46):
    def test___limitAndOffset__1655(self) -> None:
        'limit and offset'
        test_54: Test = Test()
        try:
            t_5175: 'Query'
            t_5175 = from_(sid_505('users')).limit(10)
            t_5176: 'Query'
            t_5176 = t_5175.offset(20)
            q_1056: 'Query' = t_5176
            t_9761: 'bool33' = q_1056.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_9756() -> 'str27':
                return 'limit/offset'
            test_54.assert_(t_9761, fn_9756)
        finally:
            test_54.soft_fail_to_hard()
class TestCase77(TestCase46):
    def test___limitBubblesOnNegative__1656(self) -> None:
        'limit bubbles on negative'
        test_55: Test = Test()
        try:
            did_bubble_1058: 'bool33'
            try:
                from_(sid_505('users')).limit(-1)
                did_bubble_1058 = False
            except Exception37:
                did_bubble_1058 = True
            def fn_9752() -> 'str27':
                return 'negative limit should bubble'
            test_55.assert_(did_bubble_1058, fn_9752)
        finally:
            test_55.soft_fail_to_hard()
class TestCase78(TestCase46):
    def test___offsetBubblesOnNegative__1657(self) -> None:
        'offset bubbles on negative'
        test_56: Test = Test()
        try:
            did_bubble_1060: 'bool33'
            try:
                from_(sid_505('users')).offset(-1)
                did_bubble_1060 = False
            except Exception37:
                did_bubble_1060 = True
            def fn_9748() -> 'str27':
                return 'negative offset should bubble'
            test_56.assert_(did_bubble_1060, fn_9748)
        finally:
            test_56.soft_fail_to_hard()
class TestCase79(TestCase46):
    def test___complexComposedQuery__1658(self) -> None:
        'complex composed query'
        test_57: Test = Test()
        try:
            min_age_1062: 'int31' = 21
            t_9726: 'SafeIdentifier' = sid_505('users')
            t_9727: 'SafeIdentifier' = sid_505('id')
            t_9728: 'SafeIdentifier' = sid_505('name')
            t_9729: 'SafeIdentifier' = sid_505('email')
            t_9730: 'Query' = from_(t_9726).select((t_9727, t_9728, t_9729))
            t_9731: 'SqlBuilder' = SqlBuilder()
            t_9731.append_safe('age >= ')
            t_9731.append_int32(21)
            t_9735: 'Query' = t_9730.where(t_9731.accumulated)
            t_9736: 'SqlBuilder' = SqlBuilder()
            t_9736.append_safe('active = ')
            t_9736.append_boolean(True)
            t_5161: 'Query'
            t_5161 = t_9735.where(t_9736.accumulated).order_by(sid_505('name'), True).limit(25)
            t_5162: 'Query'
            t_5162 = t_5161.offset(0)
            q_1063: 'Query' = t_5162
            t_9746: 'bool33' = q_1063.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_9725() -> 'str27':
                return 'complex query'
            test_57.assert_(t_9746, fn_9725)
        finally:
            test_57.soft_fail_to_hard()
class TestCase80(TestCase46):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__1661(self) -> None:
        'safeToSql applies default limit when none set'
        test_58: Test = Test()
        try:
            q_1065: 'Query' = from_(sid_505('users'))
            t_5138: 'SqlFragment'
            t_5138 = q_1065.safe_to_sql(100)
            t_5139: 'SqlFragment' = t_5138
            s_1066: 'str27' = t_5139.to_string()
            t_9723: 'bool33' = s_1066 == 'SELECT * FROM users LIMIT 100'
            def fn_9719() -> 'str27':
                return str_cat_10942('should have limit: ', s_1066)
            test_58.assert_(t_9723, fn_9719)
        finally:
            test_58.soft_fail_to_hard()
class TestCase81(TestCase46):
    def test___safeToSqlRespectsExplicitLimit__1662(self) -> None:
        'safeToSql respects explicit limit'
        test_59: Test = Test()
        try:
            t_5130: 'Query'
            t_5130 = from_(sid_505('users')).limit(5)
            q_1068: 'Query' = t_5130
            t_5133: 'SqlFragment'
            t_5133 = q_1068.safe_to_sql(100)
            t_5134: 'SqlFragment' = t_5133
            s_1069: 'str27' = t_5134.to_string()
            t_9717: 'bool33' = s_1069 == 'SELECT * FROM users LIMIT 5'
            def fn_9713() -> 'str27':
                return str_cat_10942('explicit limit preserved: ', s_1069)
            test_59.assert_(t_9717, fn_9713)
        finally:
            test_59.soft_fail_to_hard()
class TestCase82(TestCase46):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__1663(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_60: Test = Test()
        try:
            did_bubble_1071: 'bool33'
            try:
                from_(sid_505('users')).safe_to_sql(-1)
                did_bubble_1071 = False
            except Exception37:
                did_bubble_1071 = True
            def fn_9709() -> 'str27':
                return 'negative defaultLimit should bubble'
            test_60.assert_(did_bubble_1071, fn_9709)
        finally:
            test_60.soft_fail_to_hard()
class TestCase83(TestCase46):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__1664(self) -> None:
        'where with injection attempt in string value is escaped'
        test_61: Test = Test()
        try:
            evil_1073: 'str27' = "'; DROP TABLE users; --"
            t_9693: 'SafeIdentifier' = sid_505('users')
            t_9694: 'SqlBuilder' = SqlBuilder()
            t_9694.append_safe('name = ')
            t_9694.append_string("'; DROP TABLE users; --")
            t_9697: 'SqlFragment' = t_9694.accumulated
            q_1074: 'Query' = from_(t_9693).where(t_9697)
            s_1075: 'str27' = q_1074.to_sql().to_string()
            t_9702: 'bool33' = s_1075.find("''") >= 0
            def fn_9692() -> 'str27':
                return str_cat_10942('quotes must be doubled: ', s_1075)
            test_61.assert_(t_9702, fn_9692)
            t_9706: 'bool33' = s_1075.find('SELECT * FROM users WHERE name =') >= 0
            def fn_9691() -> 'str27':
                return str_cat_10942('structure intact: ', s_1075)
            test_61.assert_(t_9706, fn_9691)
        finally:
            test_61.soft_fail_to_hard()
class TestCase84(TestCase46):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__1666(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_62: Test = Test()
        try:
            attack_1077: 'str27' = 'users; DROP TABLE users; --'
            did_bubble_1078: 'bool33'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_1078 = False
            except Exception37:
                did_bubble_1078 = True
            def fn_9688() -> 'str27':
                return 'metacharacter-containing name must be rejected at construction'
            test_62.assert_(did_bubble_1078, fn_9688)
        finally:
            test_62.soft_fail_to_hard()
class TestCase85(TestCase46):
    def test___innerJoinProducesInnerJoin__1667(self) -> None:
        'innerJoin produces INNER JOIN'
        test_63: Test = Test()
        try:
            t_9677: 'SafeIdentifier' = sid_505('users')
            t_9678: 'SafeIdentifier' = sid_505('orders')
            t_9679: 'SqlBuilder' = SqlBuilder()
            t_9679.append_safe('users.id = orders.user_id')
            t_9681: 'SqlFragment' = t_9679.accumulated
            q_1080: 'Query' = from_(t_9677).inner_join(t_9678, t_9681)
            t_9686: 'bool33' = q_1080.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_9676() -> 'str27':
                return 'inner join'
            test_63.assert_(t_9686, fn_9676)
        finally:
            test_63.soft_fail_to_hard()
class TestCase86(TestCase46):
    def test___leftJoinProducesLeftJoin__1669(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_64: Test = Test()
        try:
            t_9665: 'SafeIdentifier' = sid_505('users')
            t_9666: 'SafeIdentifier' = sid_505('profiles')
            t_9667: 'SqlBuilder' = SqlBuilder()
            t_9667.append_safe('users.id = profiles.user_id')
            t_9669: 'SqlFragment' = t_9667.accumulated
            q_1082: 'Query' = from_(t_9665).left_join(t_9666, t_9669)
            t_9674: 'bool33' = q_1082.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_9664() -> 'str27':
                return 'left join'
            test_64.assert_(t_9674, fn_9664)
        finally:
            test_64.soft_fail_to_hard()
class TestCase87(TestCase46):
    def test___rightJoinProducesRightJoin__1671(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_65: Test = Test()
        try:
            t_9653: 'SafeIdentifier' = sid_505('orders')
            t_9654: 'SafeIdentifier' = sid_505('users')
            t_9655: 'SqlBuilder' = SqlBuilder()
            t_9655.append_safe('orders.user_id = users.id')
            t_9657: 'SqlFragment' = t_9655.accumulated
            q_1084: 'Query' = from_(t_9653).right_join(t_9654, t_9657)
            t_9662: 'bool33' = q_1084.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_9652() -> 'str27':
                return 'right join'
            test_65.assert_(t_9662, fn_9652)
        finally:
            test_65.soft_fail_to_hard()
class TestCase88(TestCase46):
    def test___fullJoinProducesFullOuterJoin__1673(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_66: Test = Test()
        try:
            t_9641: 'SafeIdentifier' = sid_505('users')
            t_9642: 'SafeIdentifier' = sid_505('orders')
            t_9643: 'SqlBuilder' = SqlBuilder()
            t_9643.append_safe('users.id = orders.user_id')
            t_9645: 'SqlFragment' = t_9643.accumulated
            q_1086: 'Query' = from_(t_9641).full_join(t_9642, t_9645)
            t_9650: 'bool33' = q_1086.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_9640() -> 'str27':
                return 'full join'
            test_66.assert_(t_9650, fn_9640)
        finally:
            test_66.soft_fail_to_hard()
class TestCase89(TestCase46):
    def test___chainedJoins__1675(self) -> None:
        'chained joins'
        test_67: Test = Test()
        try:
            t_9624: 'SafeIdentifier' = sid_505('users')
            t_9625: 'SafeIdentifier' = sid_505('orders')
            t_9626: 'SqlBuilder' = SqlBuilder()
            t_9626.append_safe('users.id = orders.user_id')
            t_9628: 'SqlFragment' = t_9626.accumulated
            t_9629: 'Query' = from_(t_9624).inner_join(t_9625, t_9628)
            t_9630: 'SafeIdentifier' = sid_505('profiles')
            t_9631: 'SqlBuilder' = SqlBuilder()
            t_9631.append_safe('users.id = profiles.user_id')
            q_1088: 'Query' = t_9629.left_join(t_9630, t_9631.accumulated)
            t_9638: 'bool33' = q_1088.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_9623() -> 'str27':
                return 'chained joins'
            test_67.assert_(t_9638, fn_9623)
        finally:
            test_67.soft_fail_to_hard()
class TestCase90(TestCase46):
    def test___joinWithWhereAndOrderBy__1678(self) -> None:
        'join with where and orderBy'
        test_68: Test = Test()
        try:
            t_9605: 'SafeIdentifier' = sid_505('users')
            t_9606: 'SafeIdentifier' = sid_505('orders')
            t_9607: 'SqlBuilder' = SqlBuilder()
            t_9607.append_safe('users.id = orders.user_id')
            t_9609: 'SqlFragment' = t_9607.accumulated
            t_9610: 'Query' = from_(t_9605).inner_join(t_9606, t_9609)
            t_9611: 'SqlBuilder' = SqlBuilder()
            t_9611.append_safe('orders.total > ')
            t_9611.append_int32(100)
            t_5045: 'Query'
            t_5045 = t_9610.where(t_9611.accumulated).order_by(sid_505('name'), True).limit(10)
            q_1090: 'Query' = t_5045
            t_9621: 'bool33' = q_1090.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_9604() -> 'str27':
                return 'join with where/order/limit'
            test_68.assert_(t_9621, fn_9604)
        finally:
            test_68.soft_fail_to_hard()
class TestCase91(TestCase46):
    def test___colHelperProducesQualifiedReference__1681(self) -> None:
        'col helper produces qualified reference'
        test_69: Test = Test()
        try:
            c_1092: 'SqlFragment' = col(sid_505('users'), sid_505('id'))
            t_9602: 'bool33' = c_1092.to_string() == 'users.id'
            def fn_9596() -> 'str27':
                return 'col helper'
            test_69.assert_(t_9602, fn_9596)
        finally:
            test_69.soft_fail_to_hard()
class TestCase92(TestCase46):
    def test___joinWithColHelper__1682(self) -> None:
        'join with col helper'
        test_70: Test = Test()
        try:
            on_cond_1094: 'SqlFragment' = col(sid_505('users'), sid_505('id'))
            b_1095: 'SqlBuilder' = SqlBuilder()
            b_1095.append_fragment(on_cond_1094)
            b_1095.append_safe(' = ')
            b_1095.append_fragment(col(sid_505('orders'), sid_505('user_id')))
            t_9587: 'SafeIdentifier' = sid_505('users')
            t_9588: 'SafeIdentifier' = sid_505('orders')
            t_9589: 'SqlFragment' = b_1095.accumulated
            q_1096: 'Query' = from_(t_9587).inner_join(t_9588, t_9589)
            t_9594: 'bool33' = q_1096.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_9576() -> 'str27':
                return 'join with col'
            test_70.assert_(t_9594, fn_9576)
        finally:
            test_70.soft_fail_to_hard()
class TestCase93(TestCase46):
    def test___orWhereBasic__1683(self) -> None:
        'orWhere basic'
        test_71: Test = Test()
        try:
            t_9565: 'SafeIdentifier' = sid_505('users')
            t_9566: 'SqlBuilder' = SqlBuilder()
            t_9566.append_safe('status = ')
            t_9566.append_string('active')
            t_9569: 'SqlFragment' = t_9566.accumulated
            q_1098: 'Query' = from_(t_9565).or_where(t_9569)
            t_9574: 'bool33' = q_1098.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_9564() -> 'str27':
                return 'orWhere basic'
            test_71.assert_(t_9574, fn_9564)
        finally:
            test_71.soft_fail_to_hard()
class TestCase94(TestCase46):
    def test___whereThenOrWhere__1685(self) -> None:
        'where then orWhere'
        test_72: Test = Test()
        try:
            t_9548: 'SafeIdentifier' = sid_505('users')
            t_9549: 'SqlBuilder' = SqlBuilder()
            t_9549.append_safe('age > ')
            t_9549.append_int32(18)
            t_9552: 'SqlFragment' = t_9549.accumulated
            t_9553: 'Query' = from_(t_9548).where(t_9552)
            t_9554: 'SqlBuilder' = SqlBuilder()
            t_9554.append_safe('vip = ')
            t_9554.append_boolean(True)
            q_1100: 'Query' = t_9553.or_where(t_9554.accumulated)
            t_9562: 'bool33' = q_1100.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_9547() -> 'str27':
                return 'where then orWhere'
            test_72.assert_(t_9562, fn_9547)
        finally:
            test_72.soft_fail_to_hard()
class TestCase95(TestCase46):
    def test___multipleOrWhere__1688(self) -> None:
        'multiple orWhere'
        test_73: Test = Test()
        try:
            t_9526: 'SafeIdentifier' = sid_505('users')
            t_9527: 'SqlBuilder' = SqlBuilder()
            t_9527.append_safe('active = ')
            t_9527.append_boolean(True)
            t_9530: 'SqlFragment' = t_9527.accumulated
            t_9531: 'Query' = from_(t_9526).where(t_9530)
            t_9532: 'SqlBuilder' = SqlBuilder()
            t_9532.append_safe('role = ')
            t_9532.append_string('admin')
            t_9536: 'Query' = t_9531.or_where(t_9532.accumulated)
            t_9537: 'SqlBuilder' = SqlBuilder()
            t_9537.append_safe('role = ')
            t_9537.append_string('moderator')
            q_1102: 'Query' = t_9536.or_where(t_9537.accumulated)
            t_9545: 'bool33' = q_1102.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_9525() -> 'str27':
                return 'multiple orWhere'
            test_73.assert_(t_9545, fn_9525)
        finally:
            test_73.soft_fail_to_hard()
class TestCase96(TestCase46):
    def test___mixedWhereAndOrWhere__1692(self) -> None:
        'mixed where and orWhere'
        test_74: Test = Test()
        try:
            t_9504: 'SafeIdentifier' = sid_505('users')
            t_9505: 'SqlBuilder' = SqlBuilder()
            t_9505.append_safe('age > ')
            t_9505.append_int32(18)
            t_9508: 'SqlFragment' = t_9505.accumulated
            t_9509: 'Query' = from_(t_9504).where(t_9508)
            t_9510: 'SqlBuilder' = SqlBuilder()
            t_9510.append_safe('active = ')
            t_9510.append_boolean(True)
            t_9514: 'Query' = t_9509.where(t_9510.accumulated)
            t_9515: 'SqlBuilder' = SqlBuilder()
            t_9515.append_safe('vip = ')
            t_9515.append_boolean(True)
            q_1104: 'Query' = t_9514.or_where(t_9515.accumulated)
            t_9523: 'bool33' = q_1104.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_9503() -> 'str27':
                return 'mixed where and orWhere'
            test_74.assert_(t_9523, fn_9503)
        finally:
            test_74.soft_fail_to_hard()
class TestCase97(TestCase46):
    def test___whereNull__1696(self) -> None:
        'whereNull'
        test_75: Test = Test()
        try:
            t_9495: 'SafeIdentifier' = sid_505('users')
            t_9496: 'SafeIdentifier' = sid_505('deleted_at')
            q_1106: 'Query' = from_(t_9495).where_null(t_9496)
            t_9501: 'bool33' = q_1106.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_9494() -> 'str27':
                return 'whereNull'
            test_75.assert_(t_9501, fn_9494)
        finally:
            test_75.soft_fail_to_hard()
class TestCase98(TestCase46):
    def test___whereNotNull__1697(self) -> None:
        'whereNotNull'
        test_76: Test = Test()
        try:
            t_9486: 'SafeIdentifier' = sid_505('users')
            t_9487: 'SafeIdentifier' = sid_505('email')
            q_1108: 'Query' = from_(t_9486).where_not_null(t_9487)
            t_9492: 'bool33' = q_1108.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_9485() -> 'str27':
                return 'whereNotNull'
            test_76.assert_(t_9492, fn_9485)
        finally:
            test_76.soft_fail_to_hard()
class TestCase99(TestCase46):
    def test___whereNullChainedWithWhere__1698(self) -> None:
        'whereNull chained with where'
        test_77: Test = Test()
        try:
            t_9472: 'SafeIdentifier' = sid_505('users')
            t_9473: 'SqlBuilder' = SqlBuilder()
            t_9473.append_safe('active = ')
            t_9473.append_boolean(True)
            t_9476: 'SqlFragment' = t_9473.accumulated
            q_1110: 'Query' = from_(t_9472).where(t_9476).where_null(sid_505('deleted_at'))
            t_9483: 'bool33' = q_1110.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_9471() -> 'str27':
                return 'whereNull chained'
            test_77.assert_(t_9483, fn_9471)
        finally:
            test_77.soft_fail_to_hard()
class TestCase100(TestCase46):
    def test___whereNotNullChainedWithOrWhere__1700(self) -> None:
        'whereNotNull chained with orWhere'
        test_78: Test = Test()
        try:
            t_9458: 'SafeIdentifier' = sid_505('users')
            t_9459: 'SafeIdentifier' = sid_505('deleted_at')
            t_9460: 'Query' = from_(t_9458).where_null(t_9459)
            t_9461: 'SqlBuilder' = SqlBuilder()
            t_9461.append_safe('role = ')
            t_9461.append_string('admin')
            q_1112: 'Query' = t_9460.or_where(t_9461.accumulated)
            t_9469: 'bool33' = q_1112.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_9457() -> 'str27':
                return 'whereNotNull with orWhere'
            test_78.assert_(t_9469, fn_9457)
        finally:
            test_78.soft_fail_to_hard()
class TestCase101(TestCase46):
    def test___whereInWithIntValues__1702(self) -> None:
        'whereIn with int values'
        test_79: Test = Test()
        try:
            t_9446: 'SafeIdentifier' = sid_505('users')
            t_9447: 'SafeIdentifier' = sid_505('id')
            t_9448: 'SqlInt32' = SqlInt32(1)
            t_9449: 'SqlInt32' = SqlInt32(2)
            t_9450: 'SqlInt32' = SqlInt32(3)
            q_1114: 'Query' = from_(t_9446).where_in(t_9447, (t_9448, t_9449, t_9450))
            t_9455: 'bool33' = q_1114.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_9445() -> 'str27':
                return 'whereIn ints'
            test_79.assert_(t_9455, fn_9445)
        finally:
            test_79.soft_fail_to_hard()
class TestCase102(TestCase46):
    def test___whereInWithStringValuesEscaping__1703(self) -> None:
        'whereIn with string values escaping'
        test_80: Test = Test()
        try:
            t_9435: 'SafeIdentifier' = sid_505('users')
            t_9436: 'SafeIdentifier' = sid_505('name')
            t_9437: 'SqlString' = SqlString('Alice')
            t_9438: 'SqlString' = SqlString("Bob's")
            q_1116: 'Query' = from_(t_9435).where_in(t_9436, (t_9437, t_9438))
            t_9443: 'bool33' = q_1116.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_9434() -> 'str27':
                return 'whereIn strings'
            test_80.assert_(t_9443, fn_9434)
        finally:
            test_80.soft_fail_to_hard()
class TestCase103(TestCase46):
    def test___whereInWithEmptyListProduces1_0__1704(self) -> None:
        'whereIn with empty list produces 1=0'
        test_81: Test = Test()
        try:
            t_9426: 'SafeIdentifier' = sid_505('users')
            t_9427: 'SafeIdentifier' = sid_505('id')
            q_1118: 'Query' = from_(t_9426).where_in(t_9427, ())
            t_9432: 'bool33' = q_1118.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_9425() -> 'str27':
                return 'whereIn empty'
            test_81.assert_(t_9432, fn_9425)
        finally:
            test_81.soft_fail_to_hard()
class TestCase104(TestCase46):
    def test___whereInChained__1705(self) -> None:
        'whereIn chained'
        test_82: Test = Test()
        try:
            t_9410: 'SafeIdentifier' = sid_505('users')
            t_9411: 'SqlBuilder' = SqlBuilder()
            t_9411.append_safe('active = ')
            t_9411.append_boolean(True)
            t_9414: 'SqlFragment' = t_9411.accumulated
            q_1120: 'Query' = from_(t_9410).where(t_9414).where_in(sid_505('role'), (SqlString('admin'), SqlString('user')))
            t_9423: 'bool33' = q_1120.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_9409() -> 'str27':
                return 'whereIn chained'
            test_82.assert_(t_9423, fn_9409)
        finally:
            test_82.soft_fail_to_hard()
class TestCase105(TestCase46):
    def test___whereInSingleElement__1707(self) -> None:
        'whereIn single element'
        test_83: Test = Test()
        try:
            t_9400: 'SafeIdentifier' = sid_505('users')
            t_9401: 'SafeIdentifier' = sid_505('id')
            t_9402: 'SqlInt32' = SqlInt32(42)
            q_1122: 'Query' = from_(t_9400).where_in(t_9401, (t_9402,))
            t_9407: 'bool33' = q_1122.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_9399() -> 'str27':
                return 'whereIn single'
            test_83.assert_(t_9407, fn_9399)
        finally:
            test_83.soft_fail_to_hard()
class TestCase106(TestCase46):
    def test___whereNotBasic__1708(self) -> None:
        'whereNot basic'
        test_84: Test = Test()
        try:
            t_9388: 'SafeIdentifier' = sid_505('users')
            t_9389: 'SqlBuilder' = SqlBuilder()
            t_9389.append_safe('active = ')
            t_9389.append_boolean(True)
            t_9392: 'SqlFragment' = t_9389.accumulated
            q_1124: 'Query' = from_(t_9388).where_not(t_9392)
            t_9397: 'bool33' = q_1124.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_9387() -> 'str27':
                return 'whereNot'
            test_84.assert_(t_9397, fn_9387)
        finally:
            test_84.soft_fail_to_hard()
class TestCase107(TestCase46):
    def test___whereNotChained__1710(self) -> None:
        'whereNot chained'
        test_85: Test = Test()
        try:
            t_9371: 'SafeIdentifier' = sid_505('users')
            t_9372: 'SqlBuilder' = SqlBuilder()
            t_9372.append_safe('age > ')
            t_9372.append_int32(18)
            t_9375: 'SqlFragment' = t_9372.accumulated
            t_9376: 'Query' = from_(t_9371).where(t_9375)
            t_9377: 'SqlBuilder' = SqlBuilder()
            t_9377.append_safe('banned = ')
            t_9377.append_boolean(True)
            q_1126: 'Query' = t_9376.where_not(t_9377.accumulated)
            t_9385: 'bool33' = q_1126.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_9370() -> 'str27':
                return 'whereNot chained'
            test_85.assert_(t_9385, fn_9370)
        finally:
            test_85.soft_fail_to_hard()
class TestCase108(TestCase46):
    def test___whereBetweenIntegers__1713(self) -> None:
        'whereBetween integers'
        test_86: Test = Test()
        try:
            t_9360: 'SafeIdentifier' = sid_505('users')
            t_9361: 'SafeIdentifier' = sid_505('age')
            t_9362: 'SqlInt32' = SqlInt32(18)
            t_9363: 'SqlInt32' = SqlInt32(65)
            q_1128: 'Query' = from_(t_9360).where_between(t_9361, t_9362, t_9363)
            t_9368: 'bool33' = q_1128.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_9359() -> 'str27':
                return 'whereBetween ints'
            test_86.assert_(t_9368, fn_9359)
        finally:
            test_86.soft_fail_to_hard()
class TestCase109(TestCase46):
    def test___whereBetweenChained__1714(self) -> None:
        'whereBetween chained'
        test_87: Test = Test()
        try:
            t_9344: 'SafeIdentifier' = sid_505('users')
            t_9345: 'SqlBuilder' = SqlBuilder()
            t_9345.append_safe('active = ')
            t_9345.append_boolean(True)
            t_9348: 'SqlFragment' = t_9345.accumulated
            q_1130: 'Query' = from_(t_9344).where(t_9348).where_between(sid_505('age'), SqlInt32(21), SqlInt32(30))
            t_9357: 'bool33' = q_1130.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_9343() -> 'str27':
                return 'whereBetween chained'
            test_87.assert_(t_9357, fn_9343)
        finally:
            test_87.soft_fail_to_hard()
class TestCase110(TestCase46):
    def test___whereLikeBasic__1716(self) -> None:
        'whereLike basic'
        test_88: Test = Test()
        try:
            t_9335: 'SafeIdentifier' = sid_505('users')
            t_9336: 'SafeIdentifier' = sid_505('name')
            q_1132: 'Query' = from_(t_9335).where_like(t_9336, 'John%')
            t_9341: 'bool33' = q_1132.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_9334() -> 'str27':
                return 'whereLike'
            test_88.assert_(t_9341, fn_9334)
        finally:
            test_88.soft_fail_to_hard()
class TestCase111(TestCase46):
    def test___whereIlikeBasic__1717(self) -> None:
        'whereILike basic'
        test_89: Test = Test()
        try:
            t_9326: 'SafeIdentifier' = sid_505('users')
            t_9327: 'SafeIdentifier' = sid_505('email')
            q_1134: 'Query' = from_(t_9326).where_i_like(t_9327, '%@gmail.com')
            t_9332: 'bool33' = q_1134.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_9325() -> 'str27':
                return 'whereILike'
            test_89.assert_(t_9332, fn_9325)
        finally:
            test_89.soft_fail_to_hard()
class TestCase112(TestCase46):
    def test___whereLikeWithInjectionAttempt__1718(self) -> None:
        'whereLike with injection attempt'
        test_90: Test = Test()
        try:
            t_9312: 'SafeIdentifier' = sid_505('users')
            t_9313: 'SafeIdentifier' = sid_505('name')
            q_1136: 'Query' = from_(t_9312).where_like(t_9313, "'; DROP TABLE users; --")
            s_1137: 'str27' = q_1136.to_sql().to_string()
            t_9318: 'bool33' = s_1137.find("''") >= 0
            def fn_9311() -> 'str27':
                return str_cat_10942('like injection escaped: ', s_1137)
            test_90.assert_(t_9318, fn_9311)
            t_9322: 'bool33' = s_1137.find('LIKE') >= 0
            def fn_9310() -> 'str27':
                return str_cat_10942('like structure intact: ', s_1137)
            test_90.assert_(t_9322, fn_9310)
        finally:
            test_90.soft_fail_to_hard()
class TestCase113(TestCase46):
    def test___whereLikeWildcardPatterns__1719(self) -> None:
        'whereLike wildcard patterns'
        test_91: Test = Test()
        try:
            t_9302: 'SafeIdentifier' = sid_505('users')
            t_9303: 'SafeIdentifier' = sid_505('name')
            q_1139: 'Query' = from_(t_9302).where_like(t_9303, '%son%')
            t_9308: 'bool33' = q_1139.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_9301() -> 'str27':
                return 'whereLike wildcard'
            test_91.assert_(t_9308, fn_9301)
        finally:
            test_91.soft_fail_to_hard()
class TestCase114(TestCase46):
    def test___countAllProducesCount__1720(self) -> None:
        'countAll produces COUNT(*)'
        test_92: Test = Test()
        try:
            f_1141: 'SqlFragment' = count_all()
            t_9299: 'bool33' = f_1141.to_string() == 'COUNT(*)'
            def fn_9295() -> 'str27':
                return 'countAll'
            test_92.assert_(t_9299, fn_9295)
        finally:
            test_92.soft_fail_to_hard()
class TestCase115(TestCase46):
    def test___countColProducesCountField__1721(self) -> None:
        'countCol produces COUNT(field)'
        test_93: Test = Test()
        try:
            f_1143: 'SqlFragment' = count_col(sid_505('id'))
            t_9293: 'bool33' = f_1143.to_string() == 'COUNT(id)'
            def fn_9288() -> 'str27':
                return 'countCol'
            test_93.assert_(t_9293, fn_9288)
        finally:
            test_93.soft_fail_to_hard()
class TestCase116(TestCase46):
    def test___sumColProducesSumField__1722(self) -> None:
        'sumCol produces SUM(field)'
        test_94: Test = Test()
        try:
            f_1145: 'SqlFragment' = sum_col(sid_505('amount'))
            t_9286: 'bool33' = f_1145.to_string() == 'SUM(amount)'
            def fn_9281() -> 'str27':
                return 'sumCol'
            test_94.assert_(t_9286, fn_9281)
        finally:
            test_94.soft_fail_to_hard()
class TestCase117(TestCase46):
    def test___avgColProducesAvgField__1723(self) -> None:
        'avgCol produces AVG(field)'
        test_95: Test = Test()
        try:
            f_1147: 'SqlFragment' = avg_col(sid_505('price'))
            t_9279: 'bool33' = f_1147.to_string() == 'AVG(price)'
            def fn_9274() -> 'str27':
                return 'avgCol'
            test_95.assert_(t_9279, fn_9274)
        finally:
            test_95.soft_fail_to_hard()
class TestCase118(TestCase46):
    def test___minColProducesMinField__1724(self) -> None:
        'minCol produces MIN(field)'
        test_96: Test = Test()
        try:
            f_1149: 'SqlFragment' = min_col(sid_505('created_at'))
            t_9272: 'bool33' = f_1149.to_string() == 'MIN(created_at)'
            def fn_9267() -> 'str27':
                return 'minCol'
            test_96.assert_(t_9272, fn_9267)
        finally:
            test_96.soft_fail_to_hard()
class TestCase119(TestCase46):
    def test___maxColProducesMaxField__1725(self) -> None:
        'maxCol produces MAX(field)'
        test_97: Test = Test()
        try:
            f_1151: 'SqlFragment' = max_col(sid_505('score'))
            t_9265: 'bool33' = f_1151.to_string() == 'MAX(score)'
            def fn_9260() -> 'str27':
                return 'maxCol'
            test_97.assert_(t_9265, fn_9260)
        finally:
            test_97.soft_fail_to_hard()
class TestCase120(TestCase46):
    def test___selectExprWithAggregate__1726(self) -> None:
        'selectExpr with aggregate'
        test_98: Test = Test()
        try:
            t_9252: 'SafeIdentifier' = sid_505('orders')
            t_9253: 'SqlFragment' = count_all()
            q_1153: 'Query' = from_(t_9252).select_expr((t_9253,))
            t_9258: 'bool33' = q_1153.to_sql().to_string() == 'SELECT COUNT(*) FROM orders'
            def fn_9251() -> 'str27':
                return 'selectExpr count'
            test_98.assert_(t_9258, fn_9251)
        finally:
            test_98.soft_fail_to_hard()
class TestCase121(TestCase46):
    def test___selectExprWithMultipleExpressions__1727(self) -> None:
        'selectExpr with multiple expressions'
        test_99: Test = Test()
        try:
            name_frag_1155: 'SqlFragment' = col(sid_505('users'), sid_505('name'))
            t_9243: 'SafeIdentifier' = sid_505('users')
            t_9244: 'SqlFragment' = count_all()
            q_1156: 'Query' = from_(t_9243).select_expr((name_frag_1155, t_9244))
            t_9249: 'bool33' = q_1156.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users'
            def fn_9239() -> 'str27':
                return 'selectExpr multi'
            test_99.assert_(t_9249, fn_9239)
        finally:
            test_99.soft_fail_to_hard()
class TestCase122(TestCase46):
    def test___selectExprOverridesSelectedFields__1728(self) -> None:
        'selectExpr overrides selectedFields'
        test_100: Test = Test()
        try:
            t_9228: 'SafeIdentifier' = sid_505('users')
            t_9229: 'SafeIdentifier' = sid_505('id')
            t_9230: 'SafeIdentifier' = sid_505('name')
            q_1158: 'Query' = from_(t_9228).select((t_9229, t_9230)).select_expr((count_all(),))
            t_9237: 'bool33' = q_1158.to_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_9227() -> 'str27':
                return 'selectExpr overrides select'
            test_100.assert_(t_9237, fn_9227)
        finally:
            test_100.soft_fail_to_hard()
class TestCase123(TestCase46):
    def test___groupBySingleField__1729(self) -> None:
        'groupBy single field'
        test_101: Test = Test()
        try:
            t_9214: 'SafeIdentifier' = sid_505('orders')
            t_9217: 'SqlFragment' = col(sid_505('orders'), sid_505('status'))
            t_9218: 'SqlFragment' = count_all()
            q_1160: 'Query' = from_(t_9214).select_expr((t_9217, t_9218)).group_by(sid_505('status'))
            t_9225: 'bool33' = q_1160.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status'
            def fn_9213() -> 'str27':
                return 'groupBy single'
            test_101.assert_(t_9225, fn_9213)
        finally:
            test_101.soft_fail_to_hard()
class TestCase124(TestCase46):
    def test___groupByMultipleFields__1730(self) -> None:
        'groupBy multiple fields'
        test_102: Test = Test()
        try:
            t_9203: 'SafeIdentifier' = sid_505('orders')
            t_9204: 'SafeIdentifier' = sid_505('status')
            q_1162: 'Query' = from_(t_9203).group_by(t_9204).group_by(sid_505('category'))
            t_9211: 'bool33' = q_1162.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category'
            def fn_9202() -> 'str27':
                return 'groupBy multiple'
            test_102.assert_(t_9211, fn_9202)
        finally:
            test_102.soft_fail_to_hard()
class TestCase125(TestCase46):
    def test___havingBasic__1731(self) -> None:
        'having basic'
        test_103: Test = Test()
        try:
            t_9184: 'SafeIdentifier' = sid_505('orders')
            t_9187: 'SqlFragment' = col(sid_505('orders'), sid_505('status'))
            t_9188: 'SqlFragment' = count_all()
            t_9191: 'Query' = from_(t_9184).select_expr((t_9187, t_9188)).group_by(sid_505('status'))
            t_9192: 'SqlBuilder' = SqlBuilder()
            t_9192.append_safe('COUNT(*) > ')
            t_9192.append_int32(5)
            q_1164: 'Query' = t_9191.having(t_9192.accumulated)
            t_9200: 'bool33' = q_1164.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5'
            def fn_9183() -> 'str27':
                return 'having basic'
            test_103.assert_(t_9200, fn_9183)
        finally:
            test_103.soft_fail_to_hard()
class TestCase126(TestCase46):
    def test___orHaving__1733(self) -> None:
        'orHaving'
        test_104: Test = Test()
        try:
            t_9165: 'SafeIdentifier' = sid_505('orders')
            t_9166: 'SafeIdentifier' = sid_505('status')
            t_9167: 'Query' = from_(t_9165).group_by(t_9166)
            t_9168: 'SqlBuilder' = SqlBuilder()
            t_9168.append_safe('COUNT(*) > ')
            t_9168.append_int32(5)
            t_9172: 'Query' = t_9167.having(t_9168.accumulated)
            t_9173: 'SqlBuilder' = SqlBuilder()
            t_9173.append_safe('SUM(total) > ')
            t_9173.append_int32(1000)
            q_1166: 'Query' = t_9172.or_having(t_9173.accumulated)
            t_9181: 'bool33' = q_1166.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000'
            def fn_9164() -> 'str27':
                return 'orHaving'
            test_104.assert_(t_9181, fn_9164)
        finally:
            test_104.soft_fail_to_hard()
class TestCase127(TestCase46):
    def test___distinctBasic__1736(self) -> None:
        'distinct basic'
        test_105: Test = Test()
        try:
            t_9155: 'SafeIdentifier' = sid_505('users')
            t_9156: 'SafeIdentifier' = sid_505('name')
            q_1168: 'Query' = from_(t_9155).select((t_9156,)).distinct()
            t_9162: 'bool33' = q_1168.to_sql().to_string() == 'SELECT DISTINCT name FROM users'
            def fn_9154() -> 'str27':
                return 'distinct'
            test_105.assert_(t_9162, fn_9154)
        finally:
            test_105.soft_fail_to_hard()
class TestCase128(TestCase46):
    def test___distinctWithWhere__1737(self) -> None:
        'distinct with where'
        test_106: Test = Test()
        try:
            t_9140: 'SafeIdentifier' = sid_505('users')
            t_9141: 'SafeIdentifier' = sid_505('email')
            t_9142: 'Query' = from_(t_9140).select((t_9141,))
            t_9143: 'SqlBuilder' = SqlBuilder()
            t_9143.append_safe('active = ')
            t_9143.append_boolean(True)
            q_1170: 'Query' = t_9142.where(t_9143.accumulated).distinct()
            t_9152: 'bool33' = q_1170.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE'
            def fn_9139() -> 'str27':
                return 'distinct with where'
            test_106.assert_(t_9152, fn_9139)
        finally:
            test_106.soft_fail_to_hard()
class TestCase129(TestCase46):
    def test___countSqlBare__1739(self) -> None:
        'countSql bare'
        test_107: Test = Test()
        try:
            q_1172: 'Query' = from_(sid_505('users'))
            t_9137: 'bool33' = q_1172.count_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_9132() -> 'str27':
                return 'countSql bare'
            test_107.assert_(t_9137, fn_9132)
        finally:
            test_107.soft_fail_to_hard()
class TestCase130(TestCase46):
    def test___countSqlWithWhere__1740(self) -> None:
        'countSql with WHERE'
        test_108: Test = Test()
        try:
            t_9121: 'SafeIdentifier' = sid_505('users')
            t_9122: 'SqlBuilder' = SqlBuilder()
            t_9122.append_safe('active = ')
            t_9122.append_boolean(True)
            t_9125: 'SqlFragment' = t_9122.accumulated
            q_1174: 'Query' = from_(t_9121).where(t_9125)
            t_9130: 'bool33' = q_1174.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_9120() -> 'str27':
                return 'countSql with where'
            test_108.assert_(t_9130, fn_9120)
        finally:
            test_108.soft_fail_to_hard()
class TestCase131(TestCase46):
    def test___countSqlWithJoin__1742(self) -> None:
        'countSql with JOIN'
        test_109: Test = Test()
        try:
            t_9104: 'SafeIdentifier' = sid_505('users')
            t_9105: 'SafeIdentifier' = sid_505('orders')
            t_9106: 'SqlBuilder' = SqlBuilder()
            t_9106.append_safe('users.id = orders.user_id')
            t_9108: 'SqlFragment' = t_9106.accumulated
            t_9109: 'Query' = from_(t_9104).inner_join(t_9105, t_9108)
            t_9110: 'SqlBuilder' = SqlBuilder()
            t_9110.append_safe('orders.total > ')
            t_9110.append_int32(100)
            q_1176: 'Query' = t_9109.where(t_9110.accumulated)
            t_9118: 'bool33' = q_1176.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100'
            def fn_9103() -> 'str27':
                return 'countSql with join'
            test_109.assert_(t_9118, fn_9103)
        finally:
            test_109.soft_fail_to_hard()
class TestCase132(TestCase46):
    def test___countSqlDropsOrderByLimitOffset__1745(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_110: Test = Test()
        try:
            t_9090: 'SafeIdentifier' = sid_505('users')
            t_9091: 'SqlBuilder' = SqlBuilder()
            t_9091.append_safe('active = ')
            t_9091.append_boolean(True)
            t_9094: 'SqlFragment' = t_9091.accumulated
            t_4621: 'Query'
            t_4621 = from_(t_9090).where(t_9094).order_by(sid_505('name'), True).limit(10)
            t_4622: 'Query'
            t_4622 = t_4621.offset(20)
            q_1178: 'Query' = t_4622
            s_1179: 'str27' = q_1178.count_sql().to_string()
            t_9101: 'bool33' = s_1179 == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_9089() -> 'str27':
                return str_cat_10942('countSql drops extras: ', s_1179)
            test_110.assert_(t_9101, fn_9089)
        finally:
            test_110.soft_fail_to_hard()
class TestCase133(TestCase46):
    def test___fullAggregationQuery__1747(self) -> None:
        'full aggregation query'
        test_111: Test = Test()
        try:
            t_9057: 'SafeIdentifier' = sid_505('orders')
            t_9060: 'SqlFragment' = col(sid_505('orders'), sid_505('status'))
            t_9061: 'SqlFragment' = count_all()
            t_9063: 'SqlFragment' = sum_col(sid_505('total'))
            t_9064: 'Query' = from_(t_9057).select_expr((t_9060, t_9061, t_9063))
            t_9065: 'SafeIdentifier' = sid_505('users')
            t_9066: 'SqlBuilder' = SqlBuilder()
            t_9066.append_safe('orders.user_id = users.id')
            t_9069: 'Query' = t_9064.inner_join(t_9065, t_9066.accumulated)
            t_9070: 'SqlBuilder' = SqlBuilder()
            t_9070.append_safe('users.active = ')
            t_9070.append_boolean(True)
            t_9076: 'Query' = t_9069.where(t_9070.accumulated).group_by(sid_505('status'))
            t_9077: 'SqlBuilder' = SqlBuilder()
            t_9077.append_safe('COUNT(*) > ')
            t_9077.append_int32(3)
            q_1181: 'Query' = t_9076.having(t_9077.accumulated).order_by(sid_505('status'), True)
            expected_1182: 'str27' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            t_9087: 'bool33' = q_1181.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_9056() -> 'str27':
                return 'full aggregation'
            test_111.assert_(t_9087, fn_9056)
        finally:
            test_111.soft_fail_to_hard()
class TestCase134(TestCase46):
    def test___unionSql__1751(self) -> None:
        'unionSql'
        test_112: Test = Test()
        try:
            t_9039: 'SafeIdentifier' = sid_505('users')
            t_9040: 'SqlBuilder' = SqlBuilder()
            t_9040.append_safe('role = ')
            t_9040.append_string('admin')
            t_9043: 'SqlFragment' = t_9040.accumulated
            a_1184: 'Query' = from_(t_9039).where(t_9043)
            t_9045: 'SafeIdentifier' = sid_505('users')
            t_9046: 'SqlBuilder' = SqlBuilder()
            t_9046.append_safe('role = ')
            t_9046.append_string('moderator')
            t_9049: 'SqlFragment' = t_9046.accumulated
            b_1185: 'Query' = from_(t_9045).where(t_9049)
            s_1186: 'str27' = union_sql(a_1184, b_1185).to_string()
            t_9054: 'bool33' = s_1186 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')"
            def fn_9038() -> 'str27':
                return str_cat_10942('unionSql: ', s_1186)
            test_112.assert_(t_9054, fn_9038)
        finally:
            test_112.soft_fail_to_hard()
class TestCase135(TestCase46):
    def test___unionAllSql__1754(self) -> None:
        'unionAllSql'
        test_113: Test = Test()
        try:
            t_9027: 'SafeIdentifier' = sid_505('users')
            t_9028: 'SafeIdentifier' = sid_505('name')
            a_1188: 'Query' = from_(t_9027).select((t_9028,))
            t_9030: 'SafeIdentifier' = sid_505('contacts')
            t_9031: 'SafeIdentifier' = sid_505('name')
            b_1189: 'Query' = from_(t_9030).select((t_9031,))
            s_1190: 'str27' = union_all_sql(a_1188, b_1189).to_string()
            t_9036: 'bool33' = s_1190 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)'
            def fn_9026() -> 'str27':
                return str_cat_10942('unionAllSql: ', s_1190)
            test_113.assert_(t_9036, fn_9026)
        finally:
            test_113.soft_fail_to_hard()
class TestCase136(TestCase46):
    def test___intersectSql__1755(self) -> None:
        'intersectSql'
        test_114: Test = Test()
        try:
            t_9015: 'SafeIdentifier' = sid_505('users')
            t_9016: 'SafeIdentifier' = sid_505('email')
            a_1192: 'Query' = from_(t_9015).select((t_9016,))
            t_9018: 'SafeIdentifier' = sid_505('subscribers')
            t_9019: 'SafeIdentifier' = sid_505('email')
            b_1193: 'Query' = from_(t_9018).select((t_9019,))
            s_1194: 'str27' = intersect_sql(a_1192, b_1193).to_string()
            t_9024: 'bool33' = s_1194 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)'
            def fn_9014() -> 'str27':
                return str_cat_10942('intersectSql: ', s_1194)
            test_114.assert_(t_9024, fn_9014)
        finally:
            test_114.soft_fail_to_hard()
class TestCase137(TestCase46):
    def test___exceptSql__1756(self) -> None:
        'exceptSql'
        test_115: Test = Test()
        try:
            t_9003: 'SafeIdentifier' = sid_505('users')
            t_9004: 'SafeIdentifier' = sid_505('id')
            a_1196: 'Query' = from_(t_9003).select((t_9004,))
            t_9006: 'SafeIdentifier' = sid_505('banned')
            t_9007: 'SafeIdentifier' = sid_505('id')
            b_1197: 'Query' = from_(t_9006).select((t_9007,))
            s_1198: 'str27' = except_sql(a_1196, b_1197).to_string()
            t_9012: 'bool33' = s_1198 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)'
            def fn_9002() -> 'str27':
                return str_cat_10942('exceptSql: ', s_1198)
            test_115.assert_(t_9012, fn_9002)
        finally:
            test_115.soft_fail_to_hard()
class TestCase138(TestCase46):
    def test___subqueryWithAlias__1757(self) -> None:
        'subquery with alias'
        test_116: Test = Test()
        try:
            t_8988: 'SafeIdentifier' = sid_505('orders')
            t_8989: 'SafeIdentifier' = sid_505('user_id')
            t_8990: 'Query' = from_(t_8988).select((t_8989,))
            t_8991: 'SqlBuilder' = SqlBuilder()
            t_8991.append_safe('total > ')
            t_8991.append_int32(100)
            inner_1200: 'Query' = t_8990.where(t_8991.accumulated)
            s_1201: 'str27' = subquery(inner_1200, sid_505('big_orders')).to_string()
            t_9000: 'bool33' = s_1201 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders'
            def fn_8987() -> 'str27':
                return str_cat_10942('subquery: ', s_1201)
            test_116.assert_(t_9000, fn_8987)
        finally:
            test_116.soft_fail_to_hard()
class TestCase139(TestCase46):
    def test___existsSql__1759(self) -> None:
        'existsSql'
        test_117: Test = Test()
        try:
            t_8977: 'SafeIdentifier' = sid_505('orders')
            t_8978: 'SqlBuilder' = SqlBuilder()
            t_8978.append_safe('orders.user_id = users.id')
            t_8980: 'SqlFragment' = t_8978.accumulated
            inner_1203: 'Query' = from_(t_8977).where(t_8980)
            s_1204: 'str27' = exists_sql(inner_1203).to_string()
            t_8985: 'bool33' = s_1204 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_8976() -> 'str27':
                return str_cat_10942('existsSql: ', s_1204)
            test_117.assert_(t_8985, fn_8976)
        finally:
            test_117.soft_fail_to_hard()
class TestCase140(TestCase46):
    def test___whereInSubquery__1761(self) -> None:
        'whereInSubquery'
        test_118: Test = Test()
        try:
            t_8960: 'SafeIdentifier' = sid_505('orders')
            t_8961: 'SafeIdentifier' = sid_505('user_id')
            t_8962: 'Query' = from_(t_8960).select((t_8961,))
            t_8963: 'SqlBuilder' = SqlBuilder()
            t_8963.append_safe('total > ')
            t_8963.append_int32(1000)
            sub_1206: 'Query' = t_8962.where(t_8963.accumulated)
            t_8968: 'SafeIdentifier' = sid_505('users')
            t_8969: 'SafeIdentifier' = sid_505('id')
            q_1207: 'Query' = from_(t_8968).where_in_subquery(t_8969, sub_1206)
            s_1208: 'str27' = q_1207.to_sql().to_string()
            t_8974: 'bool33' = s_1208 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)'
            def fn_8959() -> 'str27':
                return str_cat_10942('whereInSubquery: ', s_1208)
            test_118.assert_(t_8974, fn_8959)
        finally:
            test_118.soft_fail_to_hard()
class TestCase141(TestCase46):
    def test___setOperationWithWhereOnEachSide__1763(self) -> None:
        'set operation with WHERE on each side'
        test_119: Test = Test()
        try:
            t_8937: 'SafeIdentifier' = sid_505('users')
            t_8938: 'SqlBuilder' = SqlBuilder()
            t_8938.append_safe('age > ')
            t_8938.append_int32(18)
            t_8941: 'SqlFragment' = t_8938.accumulated
            t_8942: 'Query' = from_(t_8937).where(t_8941)
            t_8943: 'SqlBuilder' = SqlBuilder()
            t_8943.append_safe('active = ')
            t_8943.append_boolean(True)
            a_1210: 'Query' = t_8942.where(t_8943.accumulated)
            t_8948: 'SafeIdentifier' = sid_505('users')
            t_8949: 'SqlBuilder' = SqlBuilder()
            t_8949.append_safe('role = ')
            t_8949.append_string('vip')
            t_8952: 'SqlFragment' = t_8949.accumulated
            b_1211: 'Query' = from_(t_8948).where(t_8952)
            s_1212: 'str27' = union_sql(a_1210, b_1211).to_string()
            t_8957: 'bool33' = s_1212 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')"
            def fn_8936() -> 'str27':
                return str_cat_10942('union with where: ', s_1212)
            test_119.assert_(t_8957, fn_8936)
        finally:
            test_119.soft_fail_to_hard()
class TestCase142(TestCase46):
    def test___whereInSubqueryChainedWithWhere__1767(self) -> None:
        'whereInSubquery chained with where'
        test_120: Test = Test()
        try:
            t_8920: 'SafeIdentifier' = sid_505('orders')
            t_8921: 'SafeIdentifier' = sid_505('user_id')
            sub_1214: 'Query' = from_(t_8920).select((t_8921,))
            t_8923: 'SafeIdentifier' = sid_505('users')
            t_8924: 'SqlBuilder' = SqlBuilder()
            t_8924.append_safe('active = ')
            t_8924.append_boolean(True)
            t_8927: 'SqlFragment' = t_8924.accumulated
            q_1215: 'Query' = from_(t_8923).where(t_8927).where_in_subquery(sid_505('id'), sub_1214)
            s_1216: 'str27' = q_1215.to_sql().to_string()
            t_8934: 'bool33' = s_1216 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)'
            def fn_8919() -> 'str27':
                return str_cat_10942('whereInSubquery chained: ', s_1216)
            test_120.assert_(t_8934, fn_8919)
        finally:
            test_120.soft_fail_to_hard()
class TestCase143(TestCase46):
    def test___existsSqlUsedInWhere__1769(self) -> None:
        'existsSql used in where'
        test_121: Test = Test()
        try:
            t_8906: 'SafeIdentifier' = sid_505('orders')
            t_8907: 'SqlBuilder' = SqlBuilder()
            t_8907.append_safe('orders.user_id = users.id')
            t_8909: 'SqlFragment' = t_8907.accumulated
            sub_1218: 'Query' = from_(t_8906).where(t_8909)
            t_8911: 'SafeIdentifier' = sid_505('users')
            t_8912: 'SqlFragment' = exists_sql(sub_1218)
            q_1219: 'Query' = from_(t_8911).where(t_8912)
            s_1220: 'str27' = q_1219.to_sql().to_string()
            t_8917: 'bool33' = s_1220 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_8905() -> 'str27':
                return str_cat_10942('exists in where: ', s_1220)
            test_121.assert_(t_8917, fn_8905)
        finally:
            test_121.soft_fail_to_hard()
class TestCase144(TestCase46):
    def test___updateQueryBasic__1771(self) -> None:
        'UpdateQuery basic'
        test_122: Test = Test()
        try:
            t_8892: 'SafeIdentifier' = sid_505('users')
            t_8893: 'SafeIdentifier' = sid_505('name')
            t_8894: 'SqlString' = SqlString('Alice')
            t_8895: 'UpdateQuery' = update(t_8892).set(t_8893, t_8894)
            t_8896: 'SqlBuilder' = SqlBuilder()
            t_8896.append_safe('id = ')
            t_8896.append_int32(1)
            t_4443: 'SqlFragment'
            t_4443 = t_8895.where(t_8896.accumulated).to_sql()
            q_1222: 'SqlFragment' = t_4443
            t_8903: 'bool33' = q_1222.to_string() == "UPDATE users SET name = 'Alice' WHERE id = 1"
            def fn_8891() -> 'str27':
                return 'update basic'
            test_122.assert_(t_8903, fn_8891)
        finally:
            test_122.soft_fail_to_hard()
class TestCase145(TestCase46):
    def test___updateQueryMultipleSet__1773(self) -> None:
        'UpdateQuery multiple SET'
        test_123: Test = Test()
        try:
            t_8875: 'SafeIdentifier' = sid_505('users')
            t_8876: 'SafeIdentifier' = sid_505('name')
            t_8877: 'SqlString' = SqlString('Bob')
            t_8881: 'UpdateQuery' = update(t_8875).set(t_8876, t_8877).set(sid_505('age'), SqlInt32(30))
            t_8882: 'SqlBuilder' = SqlBuilder()
            t_8882.append_safe('id = ')
            t_8882.append_int32(2)
            t_4428: 'SqlFragment'
            t_4428 = t_8881.where(t_8882.accumulated).to_sql()
            q_1224: 'SqlFragment' = t_4428
            t_8889: 'bool33' = q_1224.to_string() == "UPDATE users SET name = 'Bob', age = 30 WHERE id = 2"
            def fn_8874() -> 'str27':
                return 'update multi set'
            test_123.assert_(t_8889, fn_8874)
        finally:
            test_123.soft_fail_to_hard()
class TestCase146(TestCase46):
    def test___updateQueryMultipleWhere__1775(self) -> None:
        'UpdateQuery multiple WHERE'
        test_124: Test = Test()
        try:
            t_8856: 'SafeIdentifier' = sid_505('users')
            t_8857: 'SafeIdentifier' = sid_505('active')
            t_8858: 'SqlBoolean' = SqlBoolean(False)
            t_8859: 'UpdateQuery' = update(t_8856).set(t_8857, t_8858)
            t_8860: 'SqlBuilder' = SqlBuilder()
            t_8860.append_safe('age < ')
            t_8860.append_int32(18)
            t_8864: 'UpdateQuery' = t_8859.where(t_8860.accumulated)
            t_8865: 'SqlBuilder' = SqlBuilder()
            t_8865.append_safe('role = ')
            t_8865.append_string('guest')
            t_4410: 'SqlFragment'
            t_4410 = t_8864.where(t_8865.accumulated).to_sql()
            q_1226: 'SqlFragment' = t_4410
            t_8872: 'bool33' = q_1226.to_string() == "UPDATE users SET active = FALSE WHERE age < 18 AND role = 'guest'"
            def fn_8855() -> 'str27':
                return 'update multi where'
            test_124.assert_(t_8872, fn_8855)
        finally:
            test_124.soft_fail_to_hard()
class TestCase147(TestCase46):
    def test___updateQueryOrWhere__1778(self) -> None:
        'UpdateQuery orWhere'
        test_125: Test = Test()
        try:
            t_8837: 'SafeIdentifier' = sid_505('users')
            t_8838: 'SafeIdentifier' = sid_505('status')
            t_8839: 'SqlString' = SqlString('banned')
            t_8840: 'UpdateQuery' = update(t_8837).set(t_8838, t_8839)
            t_8841: 'SqlBuilder' = SqlBuilder()
            t_8841.append_safe('spam_count > ')
            t_8841.append_int32(10)
            t_8845: 'UpdateQuery' = t_8840.where(t_8841.accumulated)
            t_8846: 'SqlBuilder' = SqlBuilder()
            t_8846.append_safe('reported = ')
            t_8846.append_boolean(True)
            t_4389: 'SqlFragment'
            t_4389 = t_8845.or_where(t_8846.accumulated).to_sql()
            q_1228: 'SqlFragment' = t_4389
            t_8853: 'bool33' = q_1228.to_string() == "UPDATE users SET status = 'banned' WHERE spam_count > 10 OR reported = TRUE"
            def fn_8836() -> 'str27':
                return 'update orWhere'
            test_125.assert_(t_8853, fn_8836)
        finally:
            test_125.soft_fail_to_hard()
class TestCase148(TestCase46):
    def test___updateQueryBubblesWithoutWhere__1781(self) -> None:
        'UpdateQuery bubbles without WHERE'
        test_126: Test = Test()
        try:
            t_8830: 'SafeIdentifier'
            t_8831: 'SafeIdentifier'
            t_8832: 'SqlInt32'
            did_bubble_1230: 'bool33'
            try:
                t_8830 = sid_505('users')
                t_8831 = sid_505('x')
                t_8832 = SqlInt32(1)
                update(t_8830).set(t_8831, t_8832).to_sql()
                did_bubble_1230 = False
            except Exception37:
                did_bubble_1230 = True
            def fn_8829() -> 'str27':
                return 'update without WHERE should bubble'
            test_126.assert_(did_bubble_1230, fn_8829)
        finally:
            test_126.soft_fail_to_hard()
class TestCase149(TestCase46):
    def test___updateQueryBubblesWithoutSet__1782(self) -> None:
        'UpdateQuery bubbles without SET'
        test_127: Test = Test()
        try:
            t_8821: 'SafeIdentifier'
            t_8822: 'SqlBuilder'
            t_8825: 'SqlFragment'
            did_bubble_1232: 'bool33'
            try:
                t_8821 = sid_505('users')
                t_8822 = SqlBuilder()
                t_8822.append_safe('id = ')
                t_8822.append_int32(1)
                t_8825 = t_8822.accumulated
                update(t_8821).where(t_8825).to_sql()
                did_bubble_1232 = False
            except Exception37:
                did_bubble_1232 = True
            def fn_8820() -> 'str27':
                return 'update without SET should bubble'
            test_127.assert_(did_bubble_1232, fn_8820)
        finally:
            test_127.soft_fail_to_hard()
class TestCase150(TestCase46):
    def test___updateQueryWithLimit__1784(self) -> None:
        'UpdateQuery with limit'
        test_128: Test = Test()
        try:
            t_8807: 'SafeIdentifier' = sid_505('users')
            t_8808: 'SafeIdentifier' = sid_505('active')
            t_8809: 'SqlBoolean' = SqlBoolean(False)
            t_8810: 'UpdateQuery' = update(t_8807).set(t_8808, t_8809)
            t_8811: 'SqlBuilder' = SqlBuilder()
            t_8811.append_safe('last_login < ')
            t_8811.append_string('2024-01-01')
            t_4352: 'UpdateQuery'
            t_4352 = t_8810.where(t_8811.accumulated).limit(100)
            t_4353: 'SqlFragment'
            t_4353 = t_4352.to_sql()
            q_1234: 'SqlFragment' = t_4353
            t_8818: 'bool33' = q_1234.to_string() == "UPDATE users SET active = FALSE WHERE last_login < '2024-01-01' LIMIT 100"
            def fn_8806() -> 'str27':
                return 'update limit'
            test_128.assert_(t_8818, fn_8806)
        finally:
            test_128.soft_fail_to_hard()
class TestCase151(TestCase46):
    def test___updateQueryEscaping__1786(self) -> None:
        'UpdateQuery escaping'
        test_129: Test = Test()
        try:
            t_8793: 'SafeIdentifier' = sid_505('users')
            t_8794: 'SafeIdentifier' = sid_505('bio')
            t_8795: 'SqlString' = SqlString("It's a test")
            t_8796: 'UpdateQuery' = update(t_8793).set(t_8794, t_8795)
            t_8797: 'SqlBuilder' = SqlBuilder()
            t_8797.append_safe('id = ')
            t_8797.append_int32(1)
            t_4337: 'SqlFragment'
            t_4337 = t_8796.where(t_8797.accumulated).to_sql()
            q_1236: 'SqlFragment' = t_4337
            t_8804: 'bool33' = q_1236.to_string() == "UPDATE users SET bio = 'It''s a test' WHERE id = 1"
            def fn_8792() -> 'str27':
                return 'update escaping'
            test_129.assert_(t_8804, fn_8792)
        finally:
            test_129.soft_fail_to_hard()
class TestCase152(TestCase46):
    def test___deleteQueryBasic__1788(self) -> None:
        'DeleteQuery basic'
        test_130: Test = Test()
        try:
            t_8782: 'SafeIdentifier' = sid_505('users')
            t_8783: 'SqlBuilder' = SqlBuilder()
            t_8783.append_safe('id = ')
            t_8783.append_int32(1)
            t_8786: 'SqlFragment' = t_8783.accumulated
            t_4322: 'SqlFragment'
            t_4322 = delete_from(t_8782).where(t_8786).to_sql()
            q_1238: 'SqlFragment' = t_4322
            t_8790: 'bool33' = q_1238.to_string() == 'DELETE FROM users WHERE id = 1'
            def fn_8781() -> 'str27':
                return 'delete basic'
            test_130.assert_(t_8790, fn_8781)
        finally:
            test_130.soft_fail_to_hard()
class TestCase153(TestCase46):
    def test___deleteQueryMultipleWhere__1790(self) -> None:
        'DeleteQuery multiple WHERE'
        test_131: Test = Test()
        try:
            t_8766: 'SafeIdentifier' = sid_505('logs')
            t_8767: 'SqlBuilder' = SqlBuilder()
            t_8767.append_safe('created_at < ')
            t_8767.append_string('2024-01-01')
            t_8770: 'SqlFragment' = t_8767.accumulated
            t_8771: 'DeleteQuery' = delete_from(t_8766).where(t_8770)
            t_8772: 'SqlBuilder' = SqlBuilder()
            t_8772.append_safe('level = ')
            t_8772.append_string('debug')
            t_4310: 'SqlFragment'
            t_4310 = t_8771.where(t_8772.accumulated).to_sql()
            q_1240: 'SqlFragment' = t_4310
            t_8779: 'bool33' = q_1240.to_string() == "DELETE FROM logs WHERE created_at < '2024-01-01' AND level = 'debug'"
            def fn_8765() -> 'str27':
                return 'delete multi where'
            test_131.assert_(t_8779, fn_8765)
        finally:
            test_131.soft_fail_to_hard()
class TestCase154(TestCase46):
    def test___deleteQueryBubblesWithoutWhere__1793(self) -> None:
        'DeleteQuery bubbles without WHERE'
        test_132: Test = Test()
        try:
            did_bubble_1242: 'bool33'
            try:
                delete_from(sid_505('users')).to_sql()
                did_bubble_1242 = False
            except Exception37:
                did_bubble_1242 = True
            def fn_8761() -> 'str27':
                return 'delete without WHERE should bubble'
            test_132.assert_(did_bubble_1242, fn_8761)
        finally:
            test_132.soft_fail_to_hard()
class TestCase155(TestCase46):
    def test___deleteQueryOrWhere__1794(self) -> None:
        'DeleteQuery orWhere'
        test_133: Test = Test()
        try:
            t_8746: 'SafeIdentifier' = sid_505('sessions')
            t_8747: 'SqlBuilder' = SqlBuilder()
            t_8747.append_safe('expired = ')
            t_8747.append_boolean(True)
            t_8750: 'SqlFragment' = t_8747.accumulated
            t_8751: 'DeleteQuery' = delete_from(t_8746).where(t_8750)
            t_8752: 'SqlBuilder' = SqlBuilder()
            t_8752.append_safe('created_at < ')
            t_8752.append_string('2023-01-01')
            t_4289: 'SqlFragment'
            t_4289 = t_8751.or_where(t_8752.accumulated).to_sql()
            q_1244: 'SqlFragment' = t_4289
            t_8759: 'bool33' = q_1244.to_string() == "DELETE FROM sessions WHERE expired = TRUE OR created_at < '2023-01-01'"
            def fn_8745() -> 'str27':
                return 'delete orWhere'
            test_133.assert_(t_8759, fn_8745)
        finally:
            test_133.soft_fail_to_hard()
class TestCase156(TestCase46):
    def test___deleteQueryWithLimit__1797(self) -> None:
        'DeleteQuery with limit'
        test_134: Test = Test()
        try:
            t_8735: 'SafeIdentifier' = sid_505('logs')
            t_8736: 'SqlBuilder' = SqlBuilder()
            t_8736.append_safe('level = ')
            t_8736.append_string('debug')
            t_8739: 'SqlFragment' = t_8736.accumulated
            t_4270: 'DeleteQuery'
            t_4270 = delete_from(t_8735).where(t_8739).limit(1000)
            t_4271: 'SqlFragment'
            t_4271 = t_4270.to_sql()
            q_1246: 'SqlFragment' = t_4271
            t_8743: 'bool33' = q_1246.to_string() == "DELETE FROM logs WHERE level = 'debug' LIMIT 1000"
            def fn_8734() -> 'str27':
                return 'delete limit'
            test_134.assert_(t_8743, fn_8734)
        finally:
            test_134.soft_fail_to_hard()
class TestCase157(TestCase46):
    def test___safeIdentifierAcceptsValidNames__1799(self) -> None:
        'safeIdentifier accepts valid names'
        test_141: Test = Test()
        try:
            t_4259: 'SafeIdentifier'
            t_4259 = safe_identifier('user_name')
            id_1284: 'SafeIdentifier' = t_4259
            t_8732: 'bool33' = id_1284.sql_value == 'user_name'
            def fn_8729() -> 'str27':
                return 'value should round-trip'
            test_141.assert_(t_8732, fn_8729)
        finally:
            test_141.soft_fail_to_hard()
class TestCase158(TestCase46):
    def test___safeIdentifierRejectsEmptyString__1800(self) -> None:
        'safeIdentifier rejects empty string'
        test_142: Test = Test()
        try:
            did_bubble_1286: 'bool33'
            try:
                safe_identifier('')
                did_bubble_1286 = False
            except Exception37:
                did_bubble_1286 = True
            def fn_8726() -> 'str27':
                return 'empty string should bubble'
            test_142.assert_(did_bubble_1286, fn_8726)
        finally:
            test_142.soft_fail_to_hard()
class TestCase159(TestCase46):
    def test___safeIdentifierRejectsLeadingDigit__1801(self) -> None:
        'safeIdentifier rejects leading digit'
        test_143: Test = Test()
        try:
            did_bubble_1288: 'bool33'
            try:
                safe_identifier('1col')
                did_bubble_1288 = False
            except Exception37:
                did_bubble_1288 = True
            def fn_8723() -> 'str27':
                return 'leading digit should bubble'
            test_143.assert_(did_bubble_1288, fn_8723)
        finally:
            test_143.soft_fail_to_hard()
class TestCase160(TestCase46):
    def test___safeIdentifierRejectsSqlMetacharacters__1802(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_144: Test = Test()
        try:
            cases_1290: 'Sequence29[str27]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_8720(c_1291: 'str27') -> 'None':
                did_bubble_1292: 'bool33'
                try:
                    safe_identifier(c_1291)
                    did_bubble_1292 = False
                except Exception37:
                    did_bubble_1292 = True
                def fn_8717() -> 'str27':
                    return str_cat_10942('should reject: ', c_1291)
                test_144.assert_(did_bubble_1292, fn_8717)
            list_for_each_10934(cases_1290, fn_8720)
        finally:
            test_144.soft_fail_to_hard()
class TestCase161(TestCase46):
    def test___tableDefFieldLookupFound__1803(self) -> None:
        'TableDef field lookup - found'
        test_145: Test = Test()
        try:
            t_4236: 'SafeIdentifier'
            t_4236 = safe_identifier('users')
            t_4237: 'SafeIdentifier' = t_4236
            t_4238: 'SafeIdentifier'
            t_4238 = safe_identifier('name')
            t_4239: 'SafeIdentifier' = t_4238
            t_8707: 'StringField' = StringField()
            t_8708: 'FieldDef' = FieldDef(t_4239, t_8707, False)
            t_4242: 'SafeIdentifier'
            t_4242 = safe_identifier('age')
            t_4243: 'SafeIdentifier' = t_4242
            t_8709: 'IntField' = IntField()
            t_8710: 'FieldDef' = FieldDef(t_4243, t_8709, False)
            td_1294: 'TableDef' = TableDef(t_4237, (t_8708, t_8710))
            t_4247: 'FieldDef'
            t_4247 = td_1294.field('age')
            f_1295: 'FieldDef' = t_4247
            t_8715: 'bool33' = f_1295.name.sql_value == 'age'
            def fn_8706() -> 'str27':
                return 'should find age field'
            test_145.assert_(t_8715, fn_8706)
        finally:
            test_145.soft_fail_to_hard()
class TestCase162(TestCase46):
    def test___tableDefFieldLookupNotFoundBubbles__1804(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_146: Test = Test()
        try:
            t_4227: 'SafeIdentifier'
            t_4227 = safe_identifier('users')
            t_4228: 'SafeIdentifier' = t_4227
            t_4229: 'SafeIdentifier'
            t_4229 = safe_identifier('name')
            t_4230: 'SafeIdentifier' = t_4229
            t_8701: 'StringField' = StringField()
            t_8702: 'FieldDef' = FieldDef(t_4230, t_8701, False)
            td_1297: 'TableDef' = TableDef(t_4228, (t_8702,))
            did_bubble_1298: 'bool33'
            try:
                td_1297.field('nonexistent')
                did_bubble_1298 = False
            except Exception37:
                did_bubble_1298 = True
            def fn_8700() -> 'str27':
                return 'unknown field should bubble'
            test_146.assert_(did_bubble_1298, fn_8700)
        finally:
            test_146.soft_fail_to_hard()
class TestCase163(TestCase46):
    def test___fieldDefNullableFlag__1805(self) -> None:
        'FieldDef nullable flag'
        test_147: Test = Test()
        try:
            t_4215: 'SafeIdentifier'
            t_4215 = safe_identifier('email')
            t_4216: 'SafeIdentifier' = t_4215
            t_8689: 'StringField' = StringField()
            required_1300: 'FieldDef' = FieldDef(t_4216, t_8689, False)
            t_4219: 'SafeIdentifier'
            t_4219 = safe_identifier('bio')
            t_4220: 'SafeIdentifier' = t_4219
            t_8691: 'StringField' = StringField()
            optional_1301: 'FieldDef' = FieldDef(t_4220, t_8691, True)
            t_8695: 'bool33' = not required_1300.nullable
            def fn_8688() -> 'str27':
                return 'required field should not be nullable'
            test_147.assert_(t_8695, fn_8688)
            t_8697: 'bool33' = optional_1301.nullable
            def fn_8687() -> 'str27':
                return 'optional field should be nullable'
            test_147.assert_(t_8697, fn_8687)
        finally:
            test_147.soft_fail_to_hard()
class TestCase164(TestCase46):
    def test___stringEscaping__1806(self) -> None:
        'string escaping'
        test_151: Test = Test()
        try:
            def build_1427(name_1429: 'str27') -> 'str27':
                t_8669: 'SqlBuilder' = SqlBuilder()
                t_8669.append_safe('select * from hi where name = ')
                t_8669.append_string(name_1429)
                return t_8669.accumulated.to_string()
            def build_wrong_1428(name_1431: 'str27') -> 'str27':
                return str_cat_10942("select * from hi where name = '", name_1431, "'")
            actual_1808: 'str27' = build_1427('world')
            t_8679: 'bool33' = actual_1808 == "select * from hi where name = 'world'"
            def fn_8676() -> 'str27':
                return str_cat_10942('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_1808, ')')
            test_151.assert_(t_8679, fn_8676)
            bobby_tables_1433: 'str27' = "Robert'); drop table hi;--"
            actual_1810: 'str27' = build_1427("Robert'); drop table hi;--")
            t_8683: 'bool33' = actual_1810 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_8675() -> 'str27':
                return str_cat_10942('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_1810, ')')
            test_151.assert_(t_8683, fn_8675)
            def fn_8674() -> 'str27':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_151.assert_(True, fn_8674)
        finally:
            test_151.soft_fail_to_hard()
class TestCase165(TestCase46):
    def test___stringEdgeCases__1814(self) -> None:
        'string edge cases'
        test_152: Test = Test()
        try:
            t_8637: 'SqlBuilder' = SqlBuilder()
            t_8637.append_safe('v = ')
            t_8637.append_string('')
            actual_1815: 'str27' = t_8637.accumulated.to_string()
            t_8643: 'bool33' = actual_1815 == "v = ''"
            def fn_8636() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_1815, ')')
            test_152.assert_(t_8643, fn_8636)
            t_8645: 'SqlBuilder' = SqlBuilder()
            t_8645.append_safe('v = ')
            t_8645.append_string("a''b")
            actual_1818: 'str27' = t_8645.accumulated.to_string()
            t_8651: 'bool33' = actual_1818 == "v = 'a''''b'"
            def fn_8635() -> 'str27':
                return str_cat_10942("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_1818, ')')
            test_152.assert_(t_8651, fn_8635)
            t_8653: 'SqlBuilder' = SqlBuilder()
            t_8653.append_safe('v = ')
            t_8653.append_string('Hello \u4e16\u754c')
            actual_1821: 'str27' = t_8653.accumulated.to_string()
            t_8659: 'bool33' = actual_1821 == "v = 'Hello \u4e16\u754c'"
            def fn_8634() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_1821, ')')
            test_152.assert_(t_8659, fn_8634)
            t_8661: 'SqlBuilder' = SqlBuilder()
            t_8661.append_safe('v = ')
            t_8661.append_string('Line1\nLine2')
            actual_1824: 'str27' = t_8661.accumulated.to_string()
            t_8667: 'bool33' = actual_1824 == "v = 'Line1\nLine2'"
            def fn_8633() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_1824, ')')
            test_152.assert_(t_8667, fn_8633)
        finally:
            test_152.soft_fail_to_hard()
class TestCase166(TestCase46):
    def test___numbersAndBooleans__1827(self) -> None:
        'numbers and booleans'
        test_153: Test = Test()
        try:
            t_8608: 'SqlBuilder' = SqlBuilder()
            t_8608.append_safe('select ')
            t_8608.append_int32(42)
            t_8608.append_safe(', ')
            t_8608.append_int64(43)
            t_8608.append_safe(', ')
            t_8608.append_float64(19.99)
            t_8608.append_safe(', ')
            t_8608.append_boolean(True)
            t_8608.append_safe(', ')
            t_8608.append_boolean(False)
            actual_1828: 'str27' = t_8608.accumulated.to_string()
            t_8622: 'bool33' = actual_1828 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_8607() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_1828, ')')
            test_153.assert_(t_8622, fn_8607)
            t_4160: 'date26'
            t_4160 = date_10967(2024, 12, 25)
            date_1436: 'date26' = t_4160
            t_8624: 'SqlBuilder' = SqlBuilder()
            t_8624.append_safe('insert into t values (')
            t_8624.append_date(date_1436)
            t_8624.append_safe(')')
            actual_1831: 'str27' = t_8624.accumulated.to_string()
            t_8631: 'bool33' = actual_1831 == "insert into t values ('2024-12-25')"
            def fn_8606() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_1831, ')')
            test_153.assert_(t_8631, fn_8606)
        finally:
            test_153.soft_fail_to_hard()
class TestCase167(TestCase46):
    def test___lists__1834(self) -> None:
        'lists'
        test_154: Test = Test()
        try:
            t_8552: 'SqlBuilder' = SqlBuilder()
            t_8552.append_safe('v IN (')
            t_8552.append_string_list(('a', 'b', "c'd"))
            t_8552.append_safe(')')
            actual_1835: 'str27' = t_8552.accumulated.to_string()
            t_8559: 'bool33' = actual_1835 == "v IN ('a', 'b', 'c''d')"
            def fn_8551() -> 'str27':
                return str_cat_10942("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_1835, ')')
            test_154.assert_(t_8559, fn_8551)
            t_8561: 'SqlBuilder' = SqlBuilder()
            t_8561.append_safe('v IN (')
            t_8561.append_int32_list((1, 2, 3))
            t_8561.append_safe(')')
            actual_1838: 'str27' = t_8561.accumulated.to_string()
            t_8568: 'bool33' = actual_1838 == 'v IN (1, 2, 3)'
            def fn_8550() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_1838, ')')
            test_154.assert_(t_8568, fn_8550)
            t_8570: 'SqlBuilder' = SqlBuilder()
            t_8570.append_safe('v IN (')
            t_8570.append_int64_list((1, 2))
            t_8570.append_safe(')')
            actual_1841: 'str27' = t_8570.accumulated.to_string()
            t_8577: 'bool33' = actual_1841 == 'v IN (1, 2)'
            def fn_8549() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_1841, ')')
            test_154.assert_(t_8577, fn_8549)
            t_8579: 'SqlBuilder' = SqlBuilder()
            t_8579.append_safe('v IN (')
            t_8579.append_float64_list((1.0, 2.0))
            t_8579.append_safe(')')
            actual_1844: 'str27' = t_8579.accumulated.to_string()
            t_8586: 'bool33' = actual_1844 == 'v IN (1.0, 2.0)'
            def fn_8548() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_1844, ')')
            test_154.assert_(t_8586, fn_8548)
            t_8588: 'SqlBuilder' = SqlBuilder()
            t_8588.append_safe('v IN (')
            t_8588.append_boolean_list((True, False))
            t_8588.append_safe(')')
            actual_1847: 'str27' = t_8588.accumulated.to_string()
            t_8595: 'bool33' = actual_1847 == 'v IN (TRUE, FALSE)'
            def fn_8547() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_1847, ')')
            test_154.assert_(t_8595, fn_8547)
            t_4132: 'date26'
            t_4132 = date_10967(2024, 1, 1)
            t_4133: 'date26' = t_4132
            t_4134: 'date26'
            t_4134 = date_10967(2024, 12, 25)
            t_4135: 'date26' = t_4134
            dates_1438: 'Sequence29[date26]' = (t_4133, t_4135)
            t_8597: 'SqlBuilder' = SqlBuilder()
            t_8597.append_safe('v IN (')
            t_8597.append_date_list(dates_1438)
            t_8597.append_safe(')')
            actual_1850: 'str27' = t_8597.accumulated.to_string()
            t_8604: 'bool33' = actual_1850 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_8546() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_1850, ')')
            test_154.assert_(t_8604, fn_8546)
        finally:
            test_154.soft_fail_to_hard()
class TestCase168(TestCase46):
    def test___sqlFloat64_naNRendersAsNull__1853(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_155: Test = Test()
        try:
            nan_1440: 'float38'
            nan_1440 = 0.0 / 0.0
            t_8538: 'SqlBuilder' = SqlBuilder()
            t_8538.append_safe('v = ')
            t_8538.append_float64(nan_1440)
            actual_1854: 'str27' = t_8538.accumulated.to_string()
            t_8544: 'bool33' = actual_1854 == 'v = NULL'
            def fn_8537() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_1854, ')')
            test_155.assert_(t_8544, fn_8537)
        finally:
            test_155.soft_fail_to_hard()
class TestCase169(TestCase46):
    def test___sqlFloat64_infinityRendersAsNull__1857(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_156: Test = Test()
        try:
            inf_1442: 'float38'
            inf_1442 = 1.0 / 0.0
            t_8529: 'SqlBuilder' = SqlBuilder()
            t_8529.append_safe('v = ')
            t_8529.append_float64(inf_1442)
            actual_1858: 'str27' = t_8529.accumulated.to_string()
            t_8535: 'bool33' = actual_1858 == 'v = NULL'
            def fn_8528() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_1858, ')')
            test_156.assert_(t_8535, fn_8528)
        finally:
            test_156.soft_fail_to_hard()
class TestCase170(TestCase46):
    def test___sqlFloat64_negativeInfinityRendersAsNull__1861(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_157: Test = Test()
        try:
            ninf_1444: 'float38'
            ninf_1444 = -1.0 / 0.0
            t_8520: 'SqlBuilder' = SqlBuilder()
            t_8520.append_safe('v = ')
            t_8520.append_float64(ninf_1444)
            actual_1862: 'str27' = t_8520.accumulated.to_string()
            t_8526: 'bool33' = actual_1862 == 'v = NULL'
            def fn_8519() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_1862, ')')
            test_157.assert_(t_8526, fn_8519)
        finally:
            test_157.soft_fail_to_hard()
class TestCase171(TestCase46):
    def test___sqlFloat64_normalValuesStillWork__1865(self) -> None:
        'SqlFloat64 normal values still work'
        test_158: Test = Test()
        try:
            t_8495: 'SqlBuilder' = SqlBuilder()
            t_8495.append_safe('v = ')
            t_8495.append_float64(3.14)
            actual_1866: 'str27' = t_8495.accumulated.to_string()
            t_8501: 'bool33' = actual_1866 == 'v = 3.14'
            def fn_8494() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_1866, ')')
            test_158.assert_(t_8501, fn_8494)
            t_8503: 'SqlBuilder' = SqlBuilder()
            t_8503.append_safe('v = ')
            t_8503.append_float64(0.0)
            actual_1869: 'str27' = t_8503.accumulated.to_string()
            t_8509: 'bool33' = actual_1869 == 'v = 0.0'
            def fn_8493() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_1869, ')')
            test_158.assert_(t_8509, fn_8493)
            t_8511: 'SqlBuilder' = SqlBuilder()
            t_8511.append_safe('v = ')
            t_8511.append_float64(-42.5)
            actual_1872: 'str27' = t_8511.accumulated.to_string()
            t_8517: 'bool33' = actual_1872 == 'v = -42.5'
            def fn_8492() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_1872, ')')
            test_158.assert_(t_8517, fn_8492)
        finally:
            test_158.soft_fail_to_hard()
class TestCase172(TestCase46):
    def test___sqlDateRendersWithQuotes__1875(self) -> None:
        'SqlDate renders with quotes'
        test_159: Test = Test()
        try:
            t_4028: 'date26'
            t_4028 = date_10967(2024, 6, 15)
            d_1447: 'date26' = t_4028
            t_8484: 'SqlBuilder' = SqlBuilder()
            t_8484.append_safe('v = ')
            t_8484.append_date(d_1447)
            actual_1876: 'str27' = t_8484.accumulated.to_string()
            t_8490: 'bool33' = actual_1876 == "v = '2024-06-15'"
            def fn_8483() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_1876, ')')
            test_159.assert_(t_8490, fn_8483)
        finally:
            test_159.soft_fail_to_hard()
class TestCase173(TestCase46):
    def test___nesting__1879(self) -> None:
        'nesting'
        test_160: Test = Test()
        try:
            name_1449: 'str27' = 'Someone'
            t_8452: 'SqlBuilder' = SqlBuilder()
            t_8452.append_safe('where p.last_name = ')
            t_8452.append_string('Someone')
            condition_1450: 'SqlFragment' = t_8452.accumulated
            t_8456: 'SqlBuilder' = SqlBuilder()
            t_8456.append_safe('select p.id from person p ')
            t_8456.append_fragment(condition_1450)
            actual_1881: 'str27' = t_8456.accumulated.to_string()
            t_8462: 'bool33' = actual_1881 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_8451() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1881, ')')
            test_160.assert_(t_8462, fn_8451)
            t_8464: 'SqlBuilder' = SqlBuilder()
            t_8464.append_safe('select p.id from person p ')
            t_8464.append_part(condition_1450.to_source())
            actual_1884: 'str27' = t_8464.accumulated.to_string()
            t_8471: 'bool33' = actual_1884 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_8450() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1884, ')')
            test_160.assert_(t_8471, fn_8450)
            parts_1451: 'Sequence29[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_8475: 'SqlBuilder' = SqlBuilder()
            t_8475.append_safe('select ')
            t_8475.append_part_list(parts_1451)
            actual_1887: 'str27' = t_8475.accumulated.to_string()
            t_8481: 'bool33' = actual_1887 == "select 'a''b', 3"
            def fn_8449() -> 'str27':
                return str_cat_10942('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_1887, ')')
            test_160.assert_(t_8481, fn_8449)
        finally:
            test_160.soft_fail_to_hard()
