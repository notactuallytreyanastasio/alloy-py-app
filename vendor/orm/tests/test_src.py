from temper_std.testing import Test
from builtins import str as str27, bool as bool33, Exception as Exception37, int as int31, float as float38
from unittest import TestCase as TestCase46
from types import MappingProxyType as MappingProxyType32
from typing import Sequence as Sequence29
from datetime import date as date26
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_7255, pair_7259, changeset, Changeset, mapped_has_7232, len_7235, list_get_7243, str_cat_7237, list_for_each_7229, SqlFragment, from_, Query, SqlBuilder, col, SqlInt32, SqlString, date_7262, SqlPart
def csid_398(name_543: 'str27') -> 'SafeIdentifier':
    t_3969: 'SafeIdentifier'
    t_3969 = safe_identifier(name_543)
    return t_3969
def user_table_399() -> 'TableDef':
    return TableDef(csid_398('users'), (FieldDef(csid_398('name'), StringField(), False), FieldDef(csid_398('email'), StringField(), False), FieldDef(csid_398('age'), IntField(), True), FieldDef(csid_398('score'), FloatField(), True), FieldDef(csid_398('active'), BoolField(), True)))
class TestCase45(TestCase46):
    def test___castWhitelistsAllowedFields__1178(self) -> None:
        'cast whitelists allowed fields'
        test_22: Test = Test()
        try:
            params_547: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'Alice'), pair_7259('email', 'alice@example.com'), pair_7259('admin', 'true')))
            t_6946: 'TableDef' = user_table_399()
            t_6947: 'SafeIdentifier' = csid_398('name')
            t_6948: 'SafeIdentifier' = csid_398('email')
            cs_548: 'Changeset' = changeset(t_6946, params_547).cast((t_6947, t_6948))
            t_6951: 'bool33' = mapped_has_7232(cs_548.changes, 'name')
            def fn_6941() -> 'str27':
                return 'name should be in changes'
            test_22.assert_(t_6951, fn_6941)
            t_6955: 'bool33' = mapped_has_7232(cs_548.changes, 'email')
            def fn_6940() -> 'str27':
                return 'email should be in changes'
            test_22.assert_(t_6955, fn_6940)
            t_6961: 'bool33' = not mapped_has_7232(cs_548.changes, 'admin')
            def fn_6939() -> 'str27':
                return 'admin must be dropped (not in whitelist)'
            test_22.assert_(t_6961, fn_6939)
            t_6963: 'bool33' = cs_548.is_valid
            def fn_6938() -> 'str27':
                return 'should still be valid'
            test_22.assert_(t_6963, fn_6938)
        finally:
            test_22.soft_fail_to_hard()
class TestCase47(TestCase46):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__1179(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_23: Test = Test()
        try:
            params_550: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'Alice'), pair_7259('email', 'alice@example.com')))
            t_6924: 'TableDef' = user_table_399()
            t_6925: 'SafeIdentifier' = csid_398('name')
            cs_551: 'Changeset' = changeset(t_6924, params_550).cast((t_6925,)).cast((csid_398('email'),))
            t_6932: 'bool33' = not mapped_has_7232(cs_551.changes, 'name')
            def fn_6920() -> 'str27':
                return 'name must be excluded by second cast'
            test_23.assert_(t_6932, fn_6920)
            t_6935: 'bool33' = mapped_has_7232(cs_551.changes, 'email')
            def fn_6919() -> 'str27':
                return 'email should be present'
            test_23.assert_(t_6935, fn_6919)
        finally:
            test_23.soft_fail_to_hard()
class TestCase48(TestCase46):
    def test___castIgnoresEmptyStringValues__1180(self) -> None:
        'cast ignores empty string values'
        test_24: Test = Test()
        try:
            params_553: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', ''), pair_7259('email', 'bob@example.com')))
            t_6906: 'TableDef' = user_table_399()
            t_6907: 'SafeIdentifier' = csid_398('name')
            t_6908: 'SafeIdentifier' = csid_398('email')
            cs_554: 'Changeset' = changeset(t_6906, params_553).cast((t_6907, t_6908))
            t_6913: 'bool33' = not mapped_has_7232(cs_554.changes, 'name')
            def fn_6902() -> 'str27':
                return 'empty name should not be in changes'
            test_24.assert_(t_6913, fn_6902)
            t_6916: 'bool33' = mapped_has_7232(cs_554.changes, 'email')
            def fn_6901() -> 'str27':
                return 'email should be in changes'
            test_24.assert_(t_6916, fn_6901)
        finally:
            test_24.soft_fail_to_hard()
class TestCase49(TestCase46):
    def test___validateRequiredPassesWhenFieldPresent__1181(self) -> None:
        'validateRequired passes when field present'
        test_25: Test = Test()
        try:
            params_556: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'Alice'),))
            t_6888: 'TableDef' = user_table_399()
            t_6889: 'SafeIdentifier' = csid_398('name')
            cs_557: 'Changeset' = changeset(t_6888, params_556).cast((t_6889,)).validate_required((csid_398('name'),))
            t_6893: 'bool33' = cs_557.is_valid
            def fn_6885() -> 'str27':
                return 'should be valid'
            test_25.assert_(t_6893, fn_6885)
            t_6899: 'bool33' = len_7235(cs_557.errors) == 0
            def fn_6884() -> 'str27':
                return 'no errors expected'
            test_25.assert_(t_6899, fn_6884)
        finally:
            test_25.soft_fail_to_hard()
class TestCase50(TestCase46):
    def test___validateRequiredFailsWhenFieldMissing__1182(self) -> None:
        'validateRequired fails when field missing'
        test_26: Test = Test()
        try:
            params_559: 'MappingProxyType32[str27, str27]' = map_constructor_7255(())
            t_6864: 'TableDef' = user_table_399()
            t_6865: 'SafeIdentifier' = csid_398('name')
            cs_560: 'Changeset' = changeset(t_6864, params_559).cast((t_6865,)).validate_required((csid_398('name'),))
            t_6871: 'bool33' = not cs_560.is_valid
            def fn_6862() -> 'str27':
                return 'should be invalid'
            test_26.assert_(t_6871, fn_6862)
            t_6876: 'bool33' = len_7235(cs_560.errors) == 1
            def fn_6861() -> 'str27':
                return 'should have one error'
            test_26.assert_(t_6876, fn_6861)
            t_6882: 'bool33' = list_get_7243(cs_560.errors, 0).field == 'name'
            def fn_6860() -> 'str27':
                return 'error should name the field'
            test_26.assert_(t_6882, fn_6860)
        finally:
            test_26.soft_fail_to_hard()
class TestCase51(TestCase46):
    def test___validateLengthPassesWithinRange__1183(self) -> None:
        'validateLength passes within range'
        test_27: Test = Test()
        try:
            params_562: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'Alice'),))
            t_6852: 'TableDef' = user_table_399()
            t_6853: 'SafeIdentifier' = csid_398('name')
            cs_563: 'Changeset' = changeset(t_6852, params_562).cast((t_6853,)).validate_length(csid_398('name'), 2, 50)
            t_6857: 'bool33' = cs_563.is_valid
            def fn_6849() -> 'str27':
                return 'should be valid'
            test_27.assert_(t_6857, fn_6849)
        finally:
            test_27.soft_fail_to_hard()
class TestCase52(TestCase46):
    def test___validateLengthFailsWhenTooShort__1184(self) -> None:
        'validateLength fails when too short'
        test_28: Test = Test()
        try:
            params_565: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'A'),))
            t_6840: 'TableDef' = user_table_399()
            t_6841: 'SafeIdentifier' = csid_398('name')
            cs_566: 'Changeset' = changeset(t_6840, params_565).cast((t_6841,)).validate_length(csid_398('name'), 2, 50)
            t_6847: 'bool33' = not cs_566.is_valid
            def fn_6837() -> 'str27':
                return 'should be invalid'
            test_28.assert_(t_6847, fn_6837)
        finally:
            test_28.soft_fail_to_hard()
class TestCase53(TestCase46):
    def test___validateLengthFailsWhenTooLong__1185(self) -> None:
        'validateLength fails when too long'
        test_29: Test = Test()
        try:
            params_568: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_6828: 'TableDef' = user_table_399()
            t_6829: 'SafeIdentifier' = csid_398('name')
            cs_569: 'Changeset' = changeset(t_6828, params_568).cast((t_6829,)).validate_length(csid_398('name'), 2, 10)
            t_6835: 'bool33' = not cs_569.is_valid
            def fn_6825() -> 'str27':
                return 'should be invalid'
            test_29.assert_(t_6835, fn_6825)
        finally:
            test_29.soft_fail_to_hard()
class TestCase54(TestCase46):
    def test___validateIntPassesForValidInteger__1186(self) -> None:
        'validateInt passes for valid integer'
        test_30: Test = Test()
        try:
            params_571: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('age', '30'),))
            t_6817: 'TableDef' = user_table_399()
            t_6818: 'SafeIdentifier' = csid_398('age')
            cs_572: 'Changeset' = changeset(t_6817, params_571).cast((t_6818,)).validate_int(csid_398('age'))
            t_6822: 'bool33' = cs_572.is_valid
            def fn_6814() -> 'str27':
                return 'should be valid'
            test_30.assert_(t_6822, fn_6814)
        finally:
            test_30.soft_fail_to_hard()
class TestCase55(TestCase46):
    def test___validateIntFailsForNonInteger__1187(self) -> None:
        'validateInt fails for non-integer'
        test_31: Test = Test()
        try:
            params_574: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('age', 'not-a-number'),))
            t_6805: 'TableDef' = user_table_399()
            t_6806: 'SafeIdentifier' = csid_398('age')
            cs_575: 'Changeset' = changeset(t_6805, params_574).cast((t_6806,)).validate_int(csid_398('age'))
            t_6812: 'bool33' = not cs_575.is_valid
            def fn_6802() -> 'str27':
                return 'should be invalid'
            test_31.assert_(t_6812, fn_6802)
        finally:
            test_31.soft_fail_to_hard()
class TestCase56(TestCase46):
    def test___validateFloatPassesForValidFloat__1188(self) -> None:
        'validateFloat passes for valid float'
        test_32: Test = Test()
        try:
            params_577: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('score', '9.5'),))
            t_6794: 'TableDef' = user_table_399()
            t_6795: 'SafeIdentifier' = csid_398('score')
            cs_578: 'Changeset' = changeset(t_6794, params_577).cast((t_6795,)).validate_float(csid_398('score'))
            t_6799: 'bool33' = cs_578.is_valid
            def fn_6791() -> 'str27':
                return 'should be valid'
            test_32.assert_(t_6799, fn_6791)
        finally:
            test_32.soft_fail_to_hard()
class TestCase57(TestCase46):
    def test___validateInt64_passesForValid64_bitInteger__1189(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_33: Test = Test()
        try:
            params_580: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('age', '9999999999'),))
            t_6783: 'TableDef' = user_table_399()
            t_6784: 'SafeIdentifier' = csid_398('age')
            cs_581: 'Changeset' = changeset(t_6783, params_580).cast((t_6784,)).validate_int64(csid_398('age'))
            t_6788: 'bool33' = cs_581.is_valid
            def fn_6780() -> 'str27':
                return 'should be valid'
            test_33.assert_(t_6788, fn_6780)
        finally:
            test_33.soft_fail_to_hard()
class TestCase58(TestCase46):
    def test___validateInt64_failsForNonInteger__1190(self) -> None:
        'validateInt64 fails for non-integer'
        test_34: Test = Test()
        try:
            params_583: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('age', 'not-a-number'),))
            t_6771: 'TableDef' = user_table_399()
            t_6772: 'SafeIdentifier' = csid_398('age')
            cs_584: 'Changeset' = changeset(t_6771, params_583).cast((t_6772,)).validate_int64(csid_398('age'))
            t_6778: 'bool33' = not cs_584.is_valid
            def fn_6768() -> 'str27':
                return 'should be invalid'
            test_34.assert_(t_6778, fn_6768)
        finally:
            test_34.soft_fail_to_hard()
class TestCase59(TestCase46):
    def test___validateBoolAcceptsTrue1_yesOn__1191(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_35: Test = Test()
        try:
            def fn_6765(v_586: 'str27') -> 'None':
                params_587: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('active', v_586),))
                t_6757: 'TableDef' = user_table_399()
                t_6758: 'SafeIdentifier' = csid_398('active')
                cs_588: 'Changeset' = changeset(t_6757, params_587).cast((t_6758,)).validate_bool(csid_398('active'))
                t_6762: 'bool33' = cs_588.is_valid
                def fn_6754() -> 'str27':
                    return str_cat_7237('should accept: ', v_586)
                test_35.assert_(t_6762, fn_6754)
            list_for_each_7229(('true', '1', 'yes', 'on'), fn_6765)
        finally:
            test_35.soft_fail_to_hard()
class TestCase60(TestCase46):
    def test___validateBoolAcceptsFalse0_noOff__1192(self) -> None:
        'validateBool accepts false/0/no/off'
        test_36: Test = Test()
        try:
            def fn_6751(v_590: 'str27') -> 'None':
                params_591: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('active', v_590),))
                t_6743: 'TableDef' = user_table_399()
                t_6744: 'SafeIdentifier' = csid_398('active')
                cs_592: 'Changeset' = changeset(t_6743, params_591).cast((t_6744,)).validate_bool(csid_398('active'))
                t_6748: 'bool33' = cs_592.is_valid
                def fn_6740() -> 'str27':
                    return str_cat_7237('should accept: ', v_590)
                test_36.assert_(t_6748, fn_6740)
            list_for_each_7229(('false', '0', 'no', 'off'), fn_6751)
        finally:
            test_36.soft_fail_to_hard()
class TestCase61(TestCase46):
    def test___validateBoolRejectsAmbiguousValues__1193(self) -> None:
        'validateBool rejects ambiguous values'
        test_37: Test = Test()
        try:
            def fn_6737(v_594: 'str27') -> 'None':
                params_595: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('active', v_594),))
                t_6728: 'TableDef' = user_table_399()
                t_6729: 'SafeIdentifier' = csid_398('active')
                cs_596: 'Changeset' = changeset(t_6728, params_595).cast((t_6729,)).validate_bool(csid_398('active'))
                t_6735: 'bool33' = not cs_596.is_valid
                def fn_6725() -> 'str27':
                    return str_cat_7237('should reject ambiguous: ', v_594)
                test_37.assert_(t_6735, fn_6725)
            list_for_each_7229(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_6737)
        finally:
            test_37.soft_fail_to_hard()
class TestCase62(TestCase46):
    def test___toInsertSqlEscapesBobbyTables__1194(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_38: Test = Test()
        try:
            params_598: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', "Robert'); DROP TABLE users;--"), pair_7259('email', 'bobby@evil.com')))
            t_6713: 'TableDef' = user_table_399()
            t_6714: 'SafeIdentifier' = csid_398('name')
            t_6715: 'SafeIdentifier' = csid_398('email')
            cs_599: 'Changeset' = changeset(t_6713, params_598).cast((t_6714, t_6715)).validate_required((csid_398('name'), csid_398('email')))
            t_3770: 'SqlFragment'
            t_3770 = cs_599.to_insert_sql()
            sql_frag_600: 'SqlFragment' = t_3770
            s_601: 'str27' = sql_frag_600.to_string()
            t_6722: 'bool33' = s_601.find("''") >= 0
            def fn_6709() -> 'str27':
                return str_cat_7237('single quote must be doubled: ', s_601)
            test_38.assert_(t_6722, fn_6709)
        finally:
            test_38.soft_fail_to_hard()
class TestCase63(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForStringField__1195(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_39: Test = Test()
        try:
            params_603: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'Alice'), pair_7259('email', 'a@example.com')))
            t_6693: 'TableDef' = user_table_399()
            t_6694: 'SafeIdentifier' = csid_398('name')
            t_6695: 'SafeIdentifier' = csid_398('email')
            cs_604: 'Changeset' = changeset(t_6693, params_603).cast((t_6694, t_6695)).validate_required((csid_398('name'), csid_398('email')))
            t_3749: 'SqlFragment'
            t_3749 = cs_604.to_insert_sql()
            sql_frag_605: 'SqlFragment' = t_3749
            s_606: 'str27' = sql_frag_605.to_string()
            t_6702: 'bool33' = s_606.find('INSERT INTO users') >= 0
            def fn_6689() -> 'str27':
                return str_cat_7237('has INSERT INTO: ', s_606)
            test_39.assert_(t_6702, fn_6689)
            t_6706: 'bool33' = s_606.find("'Alice'") >= 0
            def fn_6688() -> 'str27':
                return str_cat_7237('has quoted name: ', s_606)
            test_39.assert_(t_6706, fn_6688)
        finally:
            test_39.soft_fail_to_hard()
class TestCase64(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForIntField__1196(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_40: Test = Test()
        try:
            params_608: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'Bob'), pair_7259('email', 'b@example.com'), pair_7259('age', '25')))
            t_6675: 'TableDef' = user_table_399()
            t_6676: 'SafeIdentifier' = csid_398('name')
            t_6677: 'SafeIdentifier' = csid_398('email')
            t_6678: 'SafeIdentifier' = csid_398('age')
            cs_609: 'Changeset' = changeset(t_6675, params_608).cast((t_6676, t_6677, t_6678)).validate_required((csid_398('name'), csid_398('email')))
            t_3732: 'SqlFragment'
            t_3732 = cs_609.to_insert_sql()
            sql_frag_610: 'SqlFragment' = t_3732
            s_611: 'str27' = sql_frag_610.to_string()
            t_6685: 'bool33' = s_611.find('25') >= 0
            def fn_6670() -> 'str27':
                return str_cat_7237('age rendered unquoted: ', s_611)
            test_40.assert_(t_6685, fn_6670)
        finally:
            test_40.soft_fail_to_hard()
class TestCase65(TestCase46):
    def test___toInsertSqlBubblesOnInvalidChangeset__1197(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_41: Test = Test()
        try:
            params_613: 'MappingProxyType32[str27, str27]' = map_constructor_7255(())
            t_6663: 'TableDef' = user_table_399()
            t_6664: 'SafeIdentifier' = csid_398('name')
            cs_614: 'Changeset' = changeset(t_6663, params_613).cast((t_6664,)).validate_required((csid_398('name'),))
            did_bubble_615: 'bool33'
            try:
                cs_614.to_insert_sql()
                did_bubble_615 = False
            except Exception37:
                did_bubble_615 = True
            def fn_6661() -> 'str27':
                return 'invalid changeset should bubble'
            test_41.assert_(did_bubble_615, fn_6661)
        finally:
            test_41.soft_fail_to_hard()
class TestCase66(TestCase46):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__1198(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_42: Test = Test()
        try:
            strict_table_617: 'TableDef' = TableDef(csid_398('posts'), (FieldDef(csid_398('title'), StringField(), False), FieldDef(csid_398('body'), StringField(), True)))
            params_618: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('body', 'hello'),))
            t_6654: 'SafeIdentifier' = csid_398('body')
            cs_619: 'Changeset' = changeset(strict_table_617, params_618).cast((t_6654,))
            t_6656: 'bool33' = cs_619.is_valid
            def fn_6643() -> 'str27':
                return 'changeset should appear valid (no explicit validation run)'
            test_42.assert_(t_6656, fn_6643)
            did_bubble_620: 'bool33'
            try:
                cs_619.to_insert_sql()
                did_bubble_620 = False
            except Exception37:
                did_bubble_620 = True
            def fn_6642() -> 'str27':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_42.assert_(did_bubble_620, fn_6642)
        finally:
            test_42.soft_fail_to_hard()
class TestCase67(TestCase46):
    def test___toUpdateSqlProducesCorrectSql__1199(self) -> None:
        'toUpdateSql produces correct SQL'
        test_43: Test = Test()
        try:
            params_622: 'MappingProxyType32[str27, str27]' = map_constructor_7255((pair_7259('name', 'Bob'),))
            t_6633: 'TableDef' = user_table_399()
            t_6634: 'SafeIdentifier' = csid_398('name')
            cs_623: 'Changeset' = changeset(t_6633, params_622).cast((t_6634,)).validate_required((csid_398('name'),))
            t_3692: 'SqlFragment'
            t_3692 = cs_623.to_update_sql(42)
            sql_frag_624: 'SqlFragment' = t_3692
            s_625: 'str27' = sql_frag_624.to_string()
            t_6640: 'bool33' = s_625 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_6630() -> 'str27':
                return str_cat_7237('got: ', s_625)
            test_43.assert_(t_6640, fn_6630)
        finally:
            test_43.soft_fail_to_hard()
class TestCase68(TestCase46):
    def test___toUpdateSqlBubblesOnInvalidChangeset__1200(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_44: Test = Test()
        try:
            params_627: 'MappingProxyType32[str27, str27]' = map_constructor_7255(())
            t_6623: 'TableDef' = user_table_399()
            t_6624: 'SafeIdentifier' = csid_398('name')
            cs_628: 'Changeset' = changeset(t_6623, params_627).cast((t_6624,)).validate_required((csid_398('name'),))
            did_bubble_629: 'bool33'
            try:
                cs_628.to_update_sql(1)
                did_bubble_629 = False
            except Exception37:
                did_bubble_629 = True
            def fn_6621() -> 'str27':
                return 'invalid changeset should bubble'
            test_44.assert_(did_bubble_629, fn_6621)
        finally:
            test_44.soft_fail_to_hard()
def sid_400(name_791: 'str27') -> 'SafeIdentifier':
    t_3489: 'SafeIdentifier'
    t_3489 = safe_identifier(name_791)
    return t_3489
class TestCase69(TestCase46):
    def test___bareFromProducesSelect__1237(self) -> None:
        'bare from produces SELECT *'
        test_45: Test = Test()
        try:
            q_794: 'Query' = from_(sid_400('users'))
            t_6444: 'bool33' = q_794.to_sql().to_string() == 'SELECT * FROM users'
            def fn_6439() -> 'str27':
                return 'bare query'
            test_45.assert_(t_6444, fn_6439)
        finally:
            test_45.soft_fail_to_hard()
class TestCase70(TestCase46):
    def test___selectRestrictsColumns__1238(self) -> None:
        'select restricts columns'
        test_46: Test = Test()
        try:
            t_6430: 'SafeIdentifier' = sid_400('users')
            t_6431: 'SafeIdentifier' = sid_400('id')
            t_6432: 'SafeIdentifier' = sid_400('name')
            q_796: 'Query' = from_(t_6430).select((t_6431, t_6432))
            t_6437: 'bool33' = q_796.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_6429() -> 'str27':
                return 'select columns'
            test_46.assert_(t_6437, fn_6429)
        finally:
            test_46.soft_fail_to_hard()
class TestCase71(TestCase46):
    def test___whereAddsConditionWithIntValue__1239(self) -> None:
        'where adds condition with int value'
        test_47: Test = Test()
        try:
            t_6418: 'SafeIdentifier' = sid_400('users')
            t_6419: 'SqlBuilder' = SqlBuilder()
            t_6419.append_safe('age > ')
            t_6419.append_int32(18)
            t_6422: 'SqlFragment' = t_6419.accumulated
            q_798: 'Query' = from_(t_6418).where(t_6422)
            t_6427: 'bool33' = q_798.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_6417() -> 'str27':
                return 'where int'
            test_47.assert_(t_6427, fn_6417)
        finally:
            test_47.soft_fail_to_hard()
class TestCase72(TestCase46):
    def test___whereAddsConditionWithBoolValue__1241(self) -> None:
        'where adds condition with bool value'
        test_48: Test = Test()
        try:
            t_6406: 'SafeIdentifier' = sid_400('users')
            t_6407: 'SqlBuilder' = SqlBuilder()
            t_6407.append_safe('active = ')
            t_6407.append_boolean(True)
            t_6410: 'SqlFragment' = t_6407.accumulated
            q_800: 'Query' = from_(t_6406).where(t_6410)
            t_6415: 'bool33' = q_800.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_6405() -> 'str27':
                return 'where bool'
            test_48.assert_(t_6415, fn_6405)
        finally:
            test_48.soft_fail_to_hard()
class TestCase73(TestCase46):
    def test___chainedWhereUsesAnd__1243(self) -> None:
        'chained where uses AND'
        test_49: Test = Test()
        try:
            t_6389: 'SafeIdentifier' = sid_400('users')
            t_6390: 'SqlBuilder' = SqlBuilder()
            t_6390.append_safe('age > ')
            t_6390.append_int32(18)
            t_6393: 'SqlFragment' = t_6390.accumulated
            t_6394: 'Query' = from_(t_6389).where(t_6393)
            t_6395: 'SqlBuilder' = SqlBuilder()
            t_6395.append_safe('active = ')
            t_6395.append_boolean(True)
            q_802: 'Query' = t_6394.where(t_6395.accumulated)
            t_6403: 'bool33' = q_802.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_6388() -> 'str27':
                return 'chained where'
            test_49.assert_(t_6403, fn_6388)
        finally:
            test_49.soft_fail_to_hard()
class TestCase74(TestCase46):
    def test___orderByAsc__1246(self) -> None:
        'orderBy ASC'
        test_50: Test = Test()
        try:
            t_6380: 'SafeIdentifier' = sid_400('users')
            t_6381: 'SafeIdentifier' = sid_400('name')
            q_804: 'Query' = from_(t_6380).order_by(t_6381, True)
            t_6386: 'bool33' = q_804.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_6379() -> 'str27':
                return 'order asc'
            test_50.assert_(t_6386, fn_6379)
        finally:
            test_50.soft_fail_to_hard()
class TestCase75(TestCase46):
    def test___orderByDesc__1247(self) -> None:
        'orderBy DESC'
        test_51: Test = Test()
        try:
            t_6371: 'SafeIdentifier' = sid_400('users')
            t_6372: 'SafeIdentifier' = sid_400('created_at')
            q_806: 'Query' = from_(t_6371).order_by(t_6372, False)
            t_6377: 'bool33' = q_806.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_6370() -> 'str27':
                return 'order desc'
            test_51.assert_(t_6377, fn_6370)
        finally:
            test_51.soft_fail_to_hard()
class TestCase76(TestCase46):
    def test___limitAndOffset__1248(self) -> None:
        'limit and offset'
        test_52: Test = Test()
        try:
            t_3423: 'Query'
            t_3423 = from_(sid_400('users')).limit(10)
            t_3424: 'Query'
            t_3424 = t_3423.offset(20)
            q_808: 'Query' = t_3424
            t_6368: 'bool33' = q_808.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_6363() -> 'str27':
                return 'limit/offset'
            test_52.assert_(t_6368, fn_6363)
        finally:
            test_52.soft_fail_to_hard()
class TestCase77(TestCase46):
    def test___limitBubblesOnNegative__1249(self) -> None:
        'limit bubbles on negative'
        test_53: Test = Test()
        try:
            did_bubble_810: 'bool33'
            try:
                from_(sid_400('users')).limit(-1)
                did_bubble_810 = False
            except Exception37:
                did_bubble_810 = True
            def fn_6359() -> 'str27':
                return 'negative limit should bubble'
            test_53.assert_(did_bubble_810, fn_6359)
        finally:
            test_53.soft_fail_to_hard()
class TestCase78(TestCase46):
    def test___offsetBubblesOnNegative__1250(self) -> None:
        'offset bubbles on negative'
        test_54: Test = Test()
        try:
            did_bubble_812: 'bool33'
            try:
                from_(sid_400('users')).offset(-1)
                did_bubble_812 = False
            except Exception37:
                did_bubble_812 = True
            def fn_6355() -> 'str27':
                return 'negative offset should bubble'
            test_54.assert_(did_bubble_812, fn_6355)
        finally:
            test_54.soft_fail_to_hard()
class TestCase79(TestCase46):
    def test___complexComposedQuery__1251(self) -> None:
        'complex composed query'
        test_55: Test = Test()
        try:
            min_age_814: 'int31' = 21
            t_6333: 'SafeIdentifier' = sid_400('users')
            t_6334: 'SafeIdentifier' = sid_400('id')
            t_6335: 'SafeIdentifier' = sid_400('name')
            t_6336: 'SafeIdentifier' = sid_400('email')
            t_6337: 'Query' = from_(t_6333).select((t_6334, t_6335, t_6336))
            t_6338: 'SqlBuilder' = SqlBuilder()
            t_6338.append_safe('age >= ')
            t_6338.append_int32(21)
            t_6342: 'Query' = t_6337.where(t_6338.accumulated)
            t_6343: 'SqlBuilder' = SqlBuilder()
            t_6343.append_safe('active = ')
            t_6343.append_boolean(True)
            t_3409: 'Query'
            t_3409 = t_6342.where(t_6343.accumulated).order_by(sid_400('name'), True).limit(25)
            t_3410: 'Query'
            t_3410 = t_3409.offset(0)
            q_815: 'Query' = t_3410
            t_6353: 'bool33' = q_815.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_6332() -> 'str27':
                return 'complex query'
            test_55.assert_(t_6353, fn_6332)
        finally:
            test_55.soft_fail_to_hard()
class TestCase80(TestCase46):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__1254(self) -> None:
        'safeToSql applies default limit when none set'
        test_56: Test = Test()
        try:
            q_817: 'Query' = from_(sid_400('users'))
            t_3386: 'SqlFragment'
            t_3386 = q_817.safe_to_sql(100)
            t_3387: 'SqlFragment' = t_3386
            s_818: 'str27' = t_3387.to_string()
            t_6330: 'bool33' = s_818 == 'SELECT * FROM users LIMIT 100'
            def fn_6326() -> 'str27':
                return str_cat_7237('should have limit: ', s_818)
            test_56.assert_(t_6330, fn_6326)
        finally:
            test_56.soft_fail_to_hard()
class TestCase81(TestCase46):
    def test___safeToSqlRespectsExplicitLimit__1255(self) -> None:
        'safeToSql respects explicit limit'
        test_57: Test = Test()
        try:
            t_3378: 'Query'
            t_3378 = from_(sid_400('users')).limit(5)
            q_820: 'Query' = t_3378
            t_3381: 'SqlFragment'
            t_3381 = q_820.safe_to_sql(100)
            t_3382: 'SqlFragment' = t_3381
            s_821: 'str27' = t_3382.to_string()
            t_6324: 'bool33' = s_821 == 'SELECT * FROM users LIMIT 5'
            def fn_6320() -> 'str27':
                return str_cat_7237('explicit limit preserved: ', s_821)
            test_57.assert_(t_6324, fn_6320)
        finally:
            test_57.soft_fail_to_hard()
class TestCase82(TestCase46):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__1256(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_58: Test = Test()
        try:
            did_bubble_823: 'bool33'
            try:
                from_(sid_400('users')).safe_to_sql(-1)
                did_bubble_823 = False
            except Exception37:
                did_bubble_823 = True
            def fn_6316() -> 'str27':
                return 'negative defaultLimit should bubble'
            test_58.assert_(did_bubble_823, fn_6316)
        finally:
            test_58.soft_fail_to_hard()
class TestCase83(TestCase46):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__1257(self) -> None:
        'where with injection attempt in string value is escaped'
        test_59: Test = Test()
        try:
            evil_825: 'str27' = "'; DROP TABLE users; --"
            t_6300: 'SafeIdentifier' = sid_400('users')
            t_6301: 'SqlBuilder' = SqlBuilder()
            t_6301.append_safe('name = ')
            t_6301.append_string("'; DROP TABLE users; --")
            t_6304: 'SqlFragment' = t_6301.accumulated
            q_826: 'Query' = from_(t_6300).where(t_6304)
            s_827: 'str27' = q_826.to_sql().to_string()
            t_6309: 'bool33' = s_827.find("''") >= 0
            def fn_6299() -> 'str27':
                return str_cat_7237('quotes must be doubled: ', s_827)
            test_59.assert_(t_6309, fn_6299)
            t_6313: 'bool33' = s_827.find('SELECT * FROM users WHERE name =') >= 0
            def fn_6298() -> 'str27':
                return str_cat_7237('structure intact: ', s_827)
            test_59.assert_(t_6313, fn_6298)
        finally:
            test_59.soft_fail_to_hard()
class TestCase84(TestCase46):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__1259(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_60: Test = Test()
        try:
            attack_829: 'str27' = 'users; DROP TABLE users; --'
            did_bubble_830: 'bool33'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_830 = False
            except Exception37:
                did_bubble_830 = True
            def fn_6295() -> 'str27':
                return 'metacharacter-containing name must be rejected at construction'
            test_60.assert_(did_bubble_830, fn_6295)
        finally:
            test_60.soft_fail_to_hard()
class TestCase85(TestCase46):
    def test___innerJoinProducesInnerJoin__1260(self) -> None:
        'innerJoin produces INNER JOIN'
        test_61: Test = Test()
        try:
            t_6284: 'SafeIdentifier' = sid_400('users')
            t_6285: 'SafeIdentifier' = sid_400('orders')
            t_6286: 'SqlBuilder' = SqlBuilder()
            t_6286.append_safe('users.id = orders.user_id')
            t_6288: 'SqlFragment' = t_6286.accumulated
            q_832: 'Query' = from_(t_6284).inner_join(t_6285, t_6288)
            t_6293: 'bool33' = q_832.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_6283() -> 'str27':
                return 'inner join'
            test_61.assert_(t_6293, fn_6283)
        finally:
            test_61.soft_fail_to_hard()
class TestCase86(TestCase46):
    def test___leftJoinProducesLeftJoin__1262(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_62: Test = Test()
        try:
            t_6272: 'SafeIdentifier' = sid_400('users')
            t_6273: 'SafeIdentifier' = sid_400('profiles')
            t_6274: 'SqlBuilder' = SqlBuilder()
            t_6274.append_safe('users.id = profiles.user_id')
            t_6276: 'SqlFragment' = t_6274.accumulated
            q_834: 'Query' = from_(t_6272).left_join(t_6273, t_6276)
            t_6281: 'bool33' = q_834.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_6271() -> 'str27':
                return 'left join'
            test_62.assert_(t_6281, fn_6271)
        finally:
            test_62.soft_fail_to_hard()
class TestCase87(TestCase46):
    def test___rightJoinProducesRightJoin__1264(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_63: Test = Test()
        try:
            t_6260: 'SafeIdentifier' = sid_400('orders')
            t_6261: 'SafeIdentifier' = sid_400('users')
            t_6262: 'SqlBuilder' = SqlBuilder()
            t_6262.append_safe('orders.user_id = users.id')
            t_6264: 'SqlFragment' = t_6262.accumulated
            q_836: 'Query' = from_(t_6260).right_join(t_6261, t_6264)
            t_6269: 'bool33' = q_836.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_6259() -> 'str27':
                return 'right join'
            test_63.assert_(t_6269, fn_6259)
        finally:
            test_63.soft_fail_to_hard()
class TestCase88(TestCase46):
    def test___fullJoinProducesFullOuterJoin__1266(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_64: Test = Test()
        try:
            t_6248: 'SafeIdentifier' = sid_400('users')
            t_6249: 'SafeIdentifier' = sid_400('orders')
            t_6250: 'SqlBuilder' = SqlBuilder()
            t_6250.append_safe('users.id = orders.user_id')
            t_6252: 'SqlFragment' = t_6250.accumulated
            q_838: 'Query' = from_(t_6248).full_join(t_6249, t_6252)
            t_6257: 'bool33' = q_838.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_6247() -> 'str27':
                return 'full join'
            test_64.assert_(t_6257, fn_6247)
        finally:
            test_64.soft_fail_to_hard()
class TestCase89(TestCase46):
    def test___chainedJoins__1268(self) -> None:
        'chained joins'
        test_65: Test = Test()
        try:
            t_6231: 'SafeIdentifier' = sid_400('users')
            t_6232: 'SafeIdentifier' = sid_400('orders')
            t_6233: 'SqlBuilder' = SqlBuilder()
            t_6233.append_safe('users.id = orders.user_id')
            t_6235: 'SqlFragment' = t_6233.accumulated
            t_6236: 'Query' = from_(t_6231).inner_join(t_6232, t_6235)
            t_6237: 'SafeIdentifier' = sid_400('profiles')
            t_6238: 'SqlBuilder' = SqlBuilder()
            t_6238.append_safe('users.id = profiles.user_id')
            q_840: 'Query' = t_6236.left_join(t_6237, t_6238.accumulated)
            t_6245: 'bool33' = q_840.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_6230() -> 'str27':
                return 'chained joins'
            test_65.assert_(t_6245, fn_6230)
        finally:
            test_65.soft_fail_to_hard()
class TestCase90(TestCase46):
    def test___joinWithWhereAndOrderBy__1271(self) -> None:
        'join with where and orderBy'
        test_66: Test = Test()
        try:
            t_6212: 'SafeIdentifier' = sid_400('users')
            t_6213: 'SafeIdentifier' = sid_400('orders')
            t_6214: 'SqlBuilder' = SqlBuilder()
            t_6214.append_safe('users.id = orders.user_id')
            t_6216: 'SqlFragment' = t_6214.accumulated
            t_6217: 'Query' = from_(t_6212).inner_join(t_6213, t_6216)
            t_6218: 'SqlBuilder' = SqlBuilder()
            t_6218.append_safe('orders.total > ')
            t_6218.append_int32(100)
            t_3293: 'Query'
            t_3293 = t_6217.where(t_6218.accumulated).order_by(sid_400('name'), True).limit(10)
            q_842: 'Query' = t_3293
            t_6228: 'bool33' = q_842.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_6211() -> 'str27':
                return 'join with where/order/limit'
            test_66.assert_(t_6228, fn_6211)
        finally:
            test_66.soft_fail_to_hard()
class TestCase91(TestCase46):
    def test___colHelperProducesQualifiedReference__1274(self) -> None:
        'col helper produces qualified reference'
        test_67: Test = Test()
        try:
            c_844: 'SqlFragment' = col(sid_400('users'), sid_400('id'))
            t_6209: 'bool33' = c_844.to_string() == 'users.id'
            def fn_6203() -> 'str27':
                return 'col helper'
            test_67.assert_(t_6209, fn_6203)
        finally:
            test_67.soft_fail_to_hard()
class TestCase92(TestCase46):
    def test___joinWithColHelper__1275(self) -> None:
        'join with col helper'
        test_68: Test = Test()
        try:
            on_cond_846: 'SqlFragment' = col(sid_400('users'), sid_400('id'))
            b_847: 'SqlBuilder' = SqlBuilder()
            b_847.append_fragment(on_cond_846)
            b_847.append_safe(' = ')
            b_847.append_fragment(col(sid_400('orders'), sid_400('user_id')))
            t_6194: 'SafeIdentifier' = sid_400('users')
            t_6195: 'SafeIdentifier' = sid_400('orders')
            t_6196: 'SqlFragment' = b_847.accumulated
            q_848: 'Query' = from_(t_6194).inner_join(t_6195, t_6196)
            t_6201: 'bool33' = q_848.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_6183() -> 'str27':
                return 'join with col'
            test_68.assert_(t_6201, fn_6183)
        finally:
            test_68.soft_fail_to_hard()
class TestCase93(TestCase46):
    def test___orWhereBasic__1276(self) -> None:
        'orWhere basic'
        test_69: Test = Test()
        try:
            t_6172: 'SafeIdentifier' = sid_400('users')
            t_6173: 'SqlBuilder' = SqlBuilder()
            t_6173.append_safe('status = ')
            t_6173.append_string('active')
            t_6176: 'SqlFragment' = t_6173.accumulated
            q_850: 'Query' = from_(t_6172).or_where(t_6176)
            t_6181: 'bool33' = q_850.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_6171() -> 'str27':
                return 'orWhere basic'
            test_69.assert_(t_6181, fn_6171)
        finally:
            test_69.soft_fail_to_hard()
class TestCase94(TestCase46):
    def test___whereThenOrWhere__1278(self) -> None:
        'where then orWhere'
        test_70: Test = Test()
        try:
            t_6155: 'SafeIdentifier' = sid_400('users')
            t_6156: 'SqlBuilder' = SqlBuilder()
            t_6156.append_safe('age > ')
            t_6156.append_int32(18)
            t_6159: 'SqlFragment' = t_6156.accumulated
            t_6160: 'Query' = from_(t_6155).where(t_6159)
            t_6161: 'SqlBuilder' = SqlBuilder()
            t_6161.append_safe('vip = ')
            t_6161.append_boolean(True)
            q_852: 'Query' = t_6160.or_where(t_6161.accumulated)
            t_6169: 'bool33' = q_852.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_6154() -> 'str27':
                return 'where then orWhere'
            test_70.assert_(t_6169, fn_6154)
        finally:
            test_70.soft_fail_to_hard()
class TestCase95(TestCase46):
    def test___multipleOrWhere__1281(self) -> None:
        'multiple orWhere'
        test_71: Test = Test()
        try:
            t_6133: 'SafeIdentifier' = sid_400('users')
            t_6134: 'SqlBuilder' = SqlBuilder()
            t_6134.append_safe('active = ')
            t_6134.append_boolean(True)
            t_6137: 'SqlFragment' = t_6134.accumulated
            t_6138: 'Query' = from_(t_6133).where(t_6137)
            t_6139: 'SqlBuilder' = SqlBuilder()
            t_6139.append_safe('role = ')
            t_6139.append_string('admin')
            t_6143: 'Query' = t_6138.or_where(t_6139.accumulated)
            t_6144: 'SqlBuilder' = SqlBuilder()
            t_6144.append_safe('role = ')
            t_6144.append_string('moderator')
            q_854: 'Query' = t_6143.or_where(t_6144.accumulated)
            t_6152: 'bool33' = q_854.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_6132() -> 'str27':
                return 'multiple orWhere'
            test_71.assert_(t_6152, fn_6132)
        finally:
            test_71.soft_fail_to_hard()
class TestCase96(TestCase46):
    def test___mixedWhereAndOrWhere__1285(self) -> None:
        'mixed where and orWhere'
        test_72: Test = Test()
        try:
            t_6111: 'SafeIdentifier' = sid_400('users')
            t_6112: 'SqlBuilder' = SqlBuilder()
            t_6112.append_safe('age > ')
            t_6112.append_int32(18)
            t_6115: 'SqlFragment' = t_6112.accumulated
            t_6116: 'Query' = from_(t_6111).where(t_6115)
            t_6117: 'SqlBuilder' = SqlBuilder()
            t_6117.append_safe('active = ')
            t_6117.append_boolean(True)
            t_6121: 'Query' = t_6116.where(t_6117.accumulated)
            t_6122: 'SqlBuilder' = SqlBuilder()
            t_6122.append_safe('vip = ')
            t_6122.append_boolean(True)
            q_856: 'Query' = t_6121.or_where(t_6122.accumulated)
            t_6130: 'bool33' = q_856.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_6110() -> 'str27':
                return 'mixed where and orWhere'
            test_72.assert_(t_6130, fn_6110)
        finally:
            test_72.soft_fail_to_hard()
class TestCase97(TestCase46):
    def test___whereNull__1289(self) -> None:
        'whereNull'
        test_73: Test = Test()
        try:
            t_6102: 'SafeIdentifier' = sid_400('users')
            t_6103: 'SafeIdentifier' = sid_400('deleted_at')
            q_858: 'Query' = from_(t_6102).where_null(t_6103)
            t_6108: 'bool33' = q_858.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_6101() -> 'str27':
                return 'whereNull'
            test_73.assert_(t_6108, fn_6101)
        finally:
            test_73.soft_fail_to_hard()
class TestCase98(TestCase46):
    def test___whereNotNull__1290(self) -> None:
        'whereNotNull'
        test_74: Test = Test()
        try:
            t_6093: 'SafeIdentifier' = sid_400('users')
            t_6094: 'SafeIdentifier' = sid_400('email')
            q_860: 'Query' = from_(t_6093).where_not_null(t_6094)
            t_6099: 'bool33' = q_860.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_6092() -> 'str27':
                return 'whereNotNull'
            test_74.assert_(t_6099, fn_6092)
        finally:
            test_74.soft_fail_to_hard()
class TestCase99(TestCase46):
    def test___whereNullChainedWithWhere__1291(self) -> None:
        'whereNull chained with where'
        test_75: Test = Test()
        try:
            t_6079: 'SafeIdentifier' = sid_400('users')
            t_6080: 'SqlBuilder' = SqlBuilder()
            t_6080.append_safe('active = ')
            t_6080.append_boolean(True)
            t_6083: 'SqlFragment' = t_6080.accumulated
            q_862: 'Query' = from_(t_6079).where(t_6083).where_null(sid_400('deleted_at'))
            t_6090: 'bool33' = q_862.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_6078() -> 'str27':
                return 'whereNull chained'
            test_75.assert_(t_6090, fn_6078)
        finally:
            test_75.soft_fail_to_hard()
class TestCase100(TestCase46):
    def test___whereNotNullChainedWithOrWhere__1293(self) -> None:
        'whereNotNull chained with orWhere'
        test_76: Test = Test()
        try:
            t_6065: 'SafeIdentifier' = sid_400('users')
            t_6066: 'SafeIdentifier' = sid_400('deleted_at')
            t_6067: 'Query' = from_(t_6065).where_null(t_6066)
            t_6068: 'SqlBuilder' = SqlBuilder()
            t_6068.append_safe('role = ')
            t_6068.append_string('admin')
            q_864: 'Query' = t_6067.or_where(t_6068.accumulated)
            t_6076: 'bool33' = q_864.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_6064() -> 'str27':
                return 'whereNotNull with orWhere'
            test_76.assert_(t_6076, fn_6064)
        finally:
            test_76.soft_fail_to_hard()
class TestCase101(TestCase46):
    def test___whereInWithIntValues__1295(self) -> None:
        'whereIn with int values'
        test_77: Test = Test()
        try:
            t_6053: 'SafeIdentifier' = sid_400('users')
            t_6054: 'SafeIdentifier' = sid_400('id')
            t_6055: 'SqlInt32' = SqlInt32(1)
            t_6056: 'SqlInt32' = SqlInt32(2)
            t_6057: 'SqlInt32' = SqlInt32(3)
            q_866: 'Query' = from_(t_6053).where_in(t_6054, (t_6055, t_6056, t_6057))
            t_6062: 'bool33' = q_866.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_6052() -> 'str27':
                return 'whereIn ints'
            test_77.assert_(t_6062, fn_6052)
        finally:
            test_77.soft_fail_to_hard()
class TestCase102(TestCase46):
    def test___whereInWithStringValuesEscaping__1296(self) -> None:
        'whereIn with string values escaping'
        test_78: Test = Test()
        try:
            t_6042: 'SafeIdentifier' = sid_400('users')
            t_6043: 'SafeIdentifier' = sid_400('name')
            t_6044: 'SqlString' = SqlString('Alice')
            t_6045: 'SqlString' = SqlString("Bob's")
            q_868: 'Query' = from_(t_6042).where_in(t_6043, (t_6044, t_6045))
            t_6050: 'bool33' = q_868.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_6041() -> 'str27':
                return 'whereIn strings'
            test_78.assert_(t_6050, fn_6041)
        finally:
            test_78.soft_fail_to_hard()
class TestCase103(TestCase46):
    def test___whereInWithEmptyListProduces1_0__1297(self) -> None:
        'whereIn with empty list produces 1=0'
        test_79: Test = Test()
        try:
            t_6033: 'SafeIdentifier' = sid_400('users')
            t_6034: 'SafeIdentifier' = sid_400('id')
            q_870: 'Query' = from_(t_6033).where_in(t_6034, ())
            t_6039: 'bool33' = q_870.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_6032() -> 'str27':
                return 'whereIn empty'
            test_79.assert_(t_6039, fn_6032)
        finally:
            test_79.soft_fail_to_hard()
class TestCase104(TestCase46):
    def test___whereInChained__1298(self) -> None:
        'whereIn chained'
        test_80: Test = Test()
        try:
            t_6017: 'SafeIdentifier' = sid_400('users')
            t_6018: 'SqlBuilder' = SqlBuilder()
            t_6018.append_safe('active = ')
            t_6018.append_boolean(True)
            t_6021: 'SqlFragment' = t_6018.accumulated
            q_872: 'Query' = from_(t_6017).where(t_6021).where_in(sid_400('role'), (SqlString('admin'), SqlString('user')))
            t_6030: 'bool33' = q_872.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_6016() -> 'str27':
                return 'whereIn chained'
            test_80.assert_(t_6030, fn_6016)
        finally:
            test_80.soft_fail_to_hard()
class TestCase105(TestCase46):
    def test___whereInSingleElement__1300(self) -> None:
        'whereIn single element'
        test_81: Test = Test()
        try:
            t_6007: 'SafeIdentifier' = sid_400('users')
            t_6008: 'SafeIdentifier' = sid_400('id')
            t_6009: 'SqlInt32' = SqlInt32(42)
            q_874: 'Query' = from_(t_6007).where_in(t_6008, (t_6009,))
            t_6014: 'bool33' = q_874.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_6006() -> 'str27':
                return 'whereIn single'
            test_81.assert_(t_6014, fn_6006)
        finally:
            test_81.soft_fail_to_hard()
class TestCase106(TestCase46):
    def test___whereNotBasic__1301(self) -> None:
        'whereNot basic'
        test_82: Test = Test()
        try:
            t_5995: 'SafeIdentifier' = sid_400('users')
            t_5996: 'SqlBuilder' = SqlBuilder()
            t_5996.append_safe('active = ')
            t_5996.append_boolean(True)
            t_5999: 'SqlFragment' = t_5996.accumulated
            q_876: 'Query' = from_(t_5995).where_not(t_5999)
            t_6004: 'bool33' = q_876.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_5994() -> 'str27':
                return 'whereNot'
            test_82.assert_(t_6004, fn_5994)
        finally:
            test_82.soft_fail_to_hard()
class TestCase107(TestCase46):
    def test___whereNotChained__1303(self) -> None:
        'whereNot chained'
        test_83: Test = Test()
        try:
            t_5978: 'SafeIdentifier' = sid_400('users')
            t_5979: 'SqlBuilder' = SqlBuilder()
            t_5979.append_safe('age > ')
            t_5979.append_int32(18)
            t_5982: 'SqlFragment' = t_5979.accumulated
            t_5983: 'Query' = from_(t_5978).where(t_5982)
            t_5984: 'SqlBuilder' = SqlBuilder()
            t_5984.append_safe('banned = ')
            t_5984.append_boolean(True)
            q_878: 'Query' = t_5983.where_not(t_5984.accumulated)
            t_5992: 'bool33' = q_878.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_5977() -> 'str27':
                return 'whereNot chained'
            test_83.assert_(t_5992, fn_5977)
        finally:
            test_83.soft_fail_to_hard()
class TestCase108(TestCase46):
    def test___whereBetweenIntegers__1306(self) -> None:
        'whereBetween integers'
        test_84: Test = Test()
        try:
            t_5967: 'SafeIdentifier' = sid_400('users')
            t_5968: 'SafeIdentifier' = sid_400('age')
            t_5969: 'SqlInt32' = SqlInt32(18)
            t_5970: 'SqlInt32' = SqlInt32(65)
            q_880: 'Query' = from_(t_5967).where_between(t_5968, t_5969, t_5970)
            t_5975: 'bool33' = q_880.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_5966() -> 'str27':
                return 'whereBetween ints'
            test_84.assert_(t_5975, fn_5966)
        finally:
            test_84.soft_fail_to_hard()
class TestCase109(TestCase46):
    def test___whereBetweenChained__1307(self) -> None:
        'whereBetween chained'
        test_85: Test = Test()
        try:
            t_5951: 'SafeIdentifier' = sid_400('users')
            t_5952: 'SqlBuilder' = SqlBuilder()
            t_5952.append_safe('active = ')
            t_5952.append_boolean(True)
            t_5955: 'SqlFragment' = t_5952.accumulated
            q_882: 'Query' = from_(t_5951).where(t_5955).where_between(sid_400('age'), SqlInt32(21), SqlInt32(30))
            t_5964: 'bool33' = q_882.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_5950() -> 'str27':
                return 'whereBetween chained'
            test_85.assert_(t_5964, fn_5950)
        finally:
            test_85.soft_fail_to_hard()
class TestCase110(TestCase46):
    def test___whereLikeBasic__1309(self) -> None:
        'whereLike basic'
        test_86: Test = Test()
        try:
            t_5942: 'SafeIdentifier' = sid_400('users')
            t_5943: 'SafeIdentifier' = sid_400('name')
            q_884: 'Query' = from_(t_5942).where_like(t_5943, 'John%')
            t_5948: 'bool33' = q_884.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_5941() -> 'str27':
                return 'whereLike'
            test_86.assert_(t_5948, fn_5941)
        finally:
            test_86.soft_fail_to_hard()
class TestCase111(TestCase46):
    def test___whereIlikeBasic__1310(self) -> None:
        'whereILike basic'
        test_87: Test = Test()
        try:
            t_5933: 'SafeIdentifier' = sid_400('users')
            t_5934: 'SafeIdentifier' = sid_400('email')
            q_886: 'Query' = from_(t_5933).where_i_like(t_5934, '%@gmail.com')
            t_5939: 'bool33' = q_886.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_5932() -> 'str27':
                return 'whereILike'
            test_87.assert_(t_5939, fn_5932)
        finally:
            test_87.soft_fail_to_hard()
class TestCase112(TestCase46):
    def test___whereLikeWithInjectionAttempt__1311(self) -> None:
        'whereLike with injection attempt'
        test_88: Test = Test()
        try:
            t_5919: 'SafeIdentifier' = sid_400('users')
            t_5920: 'SafeIdentifier' = sid_400('name')
            q_888: 'Query' = from_(t_5919).where_like(t_5920, "'; DROP TABLE users; --")
            s_889: 'str27' = q_888.to_sql().to_string()
            t_5925: 'bool33' = s_889.find("''") >= 0
            def fn_5918() -> 'str27':
                return str_cat_7237('like injection escaped: ', s_889)
            test_88.assert_(t_5925, fn_5918)
            t_5929: 'bool33' = s_889.find('LIKE') >= 0
            def fn_5917() -> 'str27':
                return str_cat_7237('like structure intact: ', s_889)
            test_88.assert_(t_5929, fn_5917)
        finally:
            test_88.soft_fail_to_hard()
class TestCase113(TestCase46):
    def test___whereLikeWildcardPatterns__1312(self) -> None:
        'whereLike wildcard patterns'
        test_89: Test = Test()
        try:
            t_5909: 'SafeIdentifier' = sid_400('users')
            t_5910: 'SafeIdentifier' = sid_400('name')
            q_891: 'Query' = from_(t_5909).where_like(t_5910, '%son%')
            t_5915: 'bool33' = q_891.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_5908() -> 'str27':
                return 'whereLike wildcard'
            test_89.assert_(t_5915, fn_5908)
        finally:
            test_89.soft_fail_to_hard()
class TestCase114(TestCase46):
    def test___safeIdentifierAcceptsValidNames__1313(self) -> None:
        'safeIdentifier accepts valid names'
        test_96: Test = Test()
        try:
            t_3023: 'SafeIdentifier'
            t_3023 = safe_identifier('user_name')
            id_929: 'SafeIdentifier' = t_3023
            t_5906: 'bool33' = id_929.sql_value == 'user_name'
            def fn_5903() -> 'str27':
                return 'value should round-trip'
            test_96.assert_(t_5906, fn_5903)
        finally:
            test_96.soft_fail_to_hard()
class TestCase115(TestCase46):
    def test___safeIdentifierRejectsEmptyString__1314(self) -> None:
        'safeIdentifier rejects empty string'
        test_97: Test = Test()
        try:
            did_bubble_931: 'bool33'
            try:
                safe_identifier('')
                did_bubble_931 = False
            except Exception37:
                did_bubble_931 = True
            def fn_5900() -> 'str27':
                return 'empty string should bubble'
            test_97.assert_(did_bubble_931, fn_5900)
        finally:
            test_97.soft_fail_to_hard()
class TestCase116(TestCase46):
    def test___safeIdentifierRejectsLeadingDigit__1315(self) -> None:
        'safeIdentifier rejects leading digit'
        test_98: Test = Test()
        try:
            did_bubble_933: 'bool33'
            try:
                safe_identifier('1col')
                did_bubble_933 = False
            except Exception37:
                did_bubble_933 = True
            def fn_5897() -> 'str27':
                return 'leading digit should bubble'
            test_98.assert_(did_bubble_933, fn_5897)
        finally:
            test_98.soft_fail_to_hard()
class TestCase117(TestCase46):
    def test___safeIdentifierRejectsSqlMetacharacters__1316(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_99: Test = Test()
        try:
            cases_935: 'Sequence29[str27]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_5894(c_936: 'str27') -> 'None':
                did_bubble_937: 'bool33'
                try:
                    safe_identifier(c_936)
                    did_bubble_937 = False
                except Exception37:
                    did_bubble_937 = True
                def fn_5891() -> 'str27':
                    return str_cat_7237('should reject: ', c_936)
                test_99.assert_(did_bubble_937, fn_5891)
            list_for_each_7229(cases_935, fn_5894)
        finally:
            test_99.soft_fail_to_hard()
class TestCase118(TestCase46):
    def test___tableDefFieldLookupFound__1317(self) -> None:
        'TableDef field lookup - found'
        test_100: Test = Test()
        try:
            t_3000: 'SafeIdentifier'
            t_3000 = safe_identifier('users')
            t_3001: 'SafeIdentifier' = t_3000
            t_3002: 'SafeIdentifier'
            t_3002 = safe_identifier('name')
            t_3003: 'SafeIdentifier' = t_3002
            t_5881: 'StringField' = StringField()
            t_5882: 'FieldDef' = FieldDef(t_3003, t_5881, False)
            t_3006: 'SafeIdentifier'
            t_3006 = safe_identifier('age')
            t_3007: 'SafeIdentifier' = t_3006
            t_5883: 'IntField' = IntField()
            t_5884: 'FieldDef' = FieldDef(t_3007, t_5883, False)
            td_939: 'TableDef' = TableDef(t_3001, (t_5882, t_5884))
            t_3011: 'FieldDef'
            t_3011 = td_939.field('age')
            f_940: 'FieldDef' = t_3011
            t_5889: 'bool33' = f_940.name.sql_value == 'age'
            def fn_5880() -> 'str27':
                return 'should find age field'
            test_100.assert_(t_5889, fn_5880)
        finally:
            test_100.soft_fail_to_hard()
class TestCase119(TestCase46):
    def test___tableDefFieldLookupNotFoundBubbles__1318(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_101: Test = Test()
        try:
            t_2991: 'SafeIdentifier'
            t_2991 = safe_identifier('users')
            t_2992: 'SafeIdentifier' = t_2991
            t_2993: 'SafeIdentifier'
            t_2993 = safe_identifier('name')
            t_2994: 'SafeIdentifier' = t_2993
            t_5875: 'StringField' = StringField()
            t_5876: 'FieldDef' = FieldDef(t_2994, t_5875, False)
            td_942: 'TableDef' = TableDef(t_2992, (t_5876,))
            did_bubble_943: 'bool33'
            try:
                td_942.field('nonexistent')
                did_bubble_943 = False
            except Exception37:
                did_bubble_943 = True
            def fn_5874() -> 'str27':
                return 'unknown field should bubble'
            test_101.assert_(did_bubble_943, fn_5874)
        finally:
            test_101.soft_fail_to_hard()
class TestCase120(TestCase46):
    def test___fieldDefNullableFlag__1319(self) -> None:
        'FieldDef nullable flag'
        test_102: Test = Test()
        try:
            t_2979: 'SafeIdentifier'
            t_2979 = safe_identifier('email')
            t_2980: 'SafeIdentifier' = t_2979
            t_5863: 'StringField' = StringField()
            required_945: 'FieldDef' = FieldDef(t_2980, t_5863, False)
            t_2983: 'SafeIdentifier'
            t_2983 = safe_identifier('bio')
            t_2984: 'SafeIdentifier' = t_2983
            t_5865: 'StringField' = StringField()
            optional_946: 'FieldDef' = FieldDef(t_2984, t_5865, True)
            t_5869: 'bool33' = not required_945.nullable
            def fn_5862() -> 'str27':
                return 'required field should not be nullable'
            test_102.assert_(t_5869, fn_5862)
            t_5871: 'bool33' = optional_946.nullable
            def fn_5861() -> 'str27':
                return 'optional field should be nullable'
            test_102.assert_(t_5871, fn_5861)
        finally:
            test_102.soft_fail_to_hard()
class TestCase121(TestCase46):
    def test___stringEscaping__1320(self) -> None:
        'string escaping'
        test_106: Test = Test()
        try:
            def build_1072(name_1074: 'str27') -> 'str27':
                t_5843: 'SqlBuilder' = SqlBuilder()
                t_5843.append_safe('select * from hi where name = ')
                t_5843.append_string(name_1074)
                return t_5843.accumulated.to_string()
            def build_wrong_1073(name_1076: 'str27') -> 'str27':
                return str_cat_7237("select * from hi where name = '", name_1076, "'")
            actual_1322: 'str27' = build_1072('world')
            t_5853: 'bool33' = actual_1322 == "select * from hi where name = 'world'"
            def fn_5850() -> 'str27':
                return str_cat_7237('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_1322, ')')
            test_106.assert_(t_5853, fn_5850)
            bobby_tables_1078: 'str27' = "Robert'); drop table hi;--"
            actual_1324: 'str27' = build_1072("Robert'); drop table hi;--")
            t_5857: 'bool33' = actual_1324 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_5849() -> 'str27':
                return str_cat_7237('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_1324, ')')
            test_106.assert_(t_5857, fn_5849)
            def fn_5848() -> 'str27':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_106.assert_(True, fn_5848)
        finally:
            test_106.soft_fail_to_hard()
class TestCase122(TestCase46):
    def test___stringEdgeCases__1328(self) -> None:
        'string edge cases'
        test_107: Test = Test()
        try:
            t_5811: 'SqlBuilder' = SqlBuilder()
            t_5811.append_safe('v = ')
            t_5811.append_string('')
            actual_1329: 'str27' = t_5811.accumulated.to_string()
            t_5817: 'bool33' = actual_1329 == "v = ''"
            def fn_5810() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_1329, ')')
            test_107.assert_(t_5817, fn_5810)
            t_5819: 'SqlBuilder' = SqlBuilder()
            t_5819.append_safe('v = ')
            t_5819.append_string("a''b")
            actual_1332: 'str27' = t_5819.accumulated.to_string()
            t_5825: 'bool33' = actual_1332 == "v = 'a''''b'"
            def fn_5809() -> 'str27':
                return str_cat_7237("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_1332, ')')
            test_107.assert_(t_5825, fn_5809)
            t_5827: 'SqlBuilder' = SqlBuilder()
            t_5827.append_safe('v = ')
            t_5827.append_string('Hello \u4e16\u754c')
            actual_1335: 'str27' = t_5827.accumulated.to_string()
            t_5833: 'bool33' = actual_1335 == "v = 'Hello \u4e16\u754c'"
            def fn_5808() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_1335, ')')
            test_107.assert_(t_5833, fn_5808)
            t_5835: 'SqlBuilder' = SqlBuilder()
            t_5835.append_safe('v = ')
            t_5835.append_string('Line1\nLine2')
            actual_1338: 'str27' = t_5835.accumulated.to_string()
            t_5841: 'bool33' = actual_1338 == "v = 'Line1\nLine2'"
            def fn_5807() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_1338, ')')
            test_107.assert_(t_5841, fn_5807)
        finally:
            test_107.soft_fail_to_hard()
class TestCase123(TestCase46):
    def test___numbersAndBooleans__1341(self) -> None:
        'numbers and booleans'
        test_108: Test = Test()
        try:
            t_5782: 'SqlBuilder' = SqlBuilder()
            t_5782.append_safe('select ')
            t_5782.append_int32(42)
            t_5782.append_safe(', ')
            t_5782.append_int64(43)
            t_5782.append_safe(', ')
            t_5782.append_float64(19.99)
            t_5782.append_safe(', ')
            t_5782.append_boolean(True)
            t_5782.append_safe(', ')
            t_5782.append_boolean(False)
            actual_1342: 'str27' = t_5782.accumulated.to_string()
            t_5796: 'bool33' = actual_1342 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_5781() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_1342, ')')
            test_108.assert_(t_5796, fn_5781)
            t_2924: 'date26'
            t_2924 = date_7262(2024, 12, 25)
            date_1081: 'date26' = t_2924
            t_5798: 'SqlBuilder' = SqlBuilder()
            t_5798.append_safe('insert into t values (')
            t_5798.append_date(date_1081)
            t_5798.append_safe(')')
            actual_1345: 'str27' = t_5798.accumulated.to_string()
            t_5805: 'bool33' = actual_1345 == "insert into t values ('2024-12-25')"
            def fn_5780() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_1345, ')')
            test_108.assert_(t_5805, fn_5780)
        finally:
            test_108.soft_fail_to_hard()
class TestCase124(TestCase46):
    def test___lists__1348(self) -> None:
        'lists'
        test_109: Test = Test()
        try:
            t_5726: 'SqlBuilder' = SqlBuilder()
            t_5726.append_safe('v IN (')
            t_5726.append_string_list(('a', 'b', "c'd"))
            t_5726.append_safe(')')
            actual_1349: 'str27' = t_5726.accumulated.to_string()
            t_5733: 'bool33' = actual_1349 == "v IN ('a', 'b', 'c''d')"
            def fn_5725() -> 'str27':
                return str_cat_7237("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_1349, ')')
            test_109.assert_(t_5733, fn_5725)
            t_5735: 'SqlBuilder' = SqlBuilder()
            t_5735.append_safe('v IN (')
            t_5735.append_int32_list((1, 2, 3))
            t_5735.append_safe(')')
            actual_1352: 'str27' = t_5735.accumulated.to_string()
            t_5742: 'bool33' = actual_1352 == 'v IN (1, 2, 3)'
            def fn_5724() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_1352, ')')
            test_109.assert_(t_5742, fn_5724)
            t_5744: 'SqlBuilder' = SqlBuilder()
            t_5744.append_safe('v IN (')
            t_5744.append_int64_list((1, 2))
            t_5744.append_safe(')')
            actual_1355: 'str27' = t_5744.accumulated.to_string()
            t_5751: 'bool33' = actual_1355 == 'v IN (1, 2)'
            def fn_5723() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_1355, ')')
            test_109.assert_(t_5751, fn_5723)
            t_5753: 'SqlBuilder' = SqlBuilder()
            t_5753.append_safe('v IN (')
            t_5753.append_float64_list((1.0, 2.0))
            t_5753.append_safe(')')
            actual_1358: 'str27' = t_5753.accumulated.to_string()
            t_5760: 'bool33' = actual_1358 == 'v IN (1.0, 2.0)'
            def fn_5722() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_1358, ')')
            test_109.assert_(t_5760, fn_5722)
            t_5762: 'SqlBuilder' = SqlBuilder()
            t_5762.append_safe('v IN (')
            t_5762.append_boolean_list((True, False))
            t_5762.append_safe(')')
            actual_1361: 'str27' = t_5762.accumulated.to_string()
            t_5769: 'bool33' = actual_1361 == 'v IN (TRUE, FALSE)'
            def fn_5721() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_1361, ')')
            test_109.assert_(t_5769, fn_5721)
            t_2896: 'date26'
            t_2896 = date_7262(2024, 1, 1)
            t_2897: 'date26' = t_2896
            t_2898: 'date26'
            t_2898 = date_7262(2024, 12, 25)
            t_2899: 'date26' = t_2898
            dates_1083: 'Sequence29[date26]' = (t_2897, t_2899)
            t_5771: 'SqlBuilder' = SqlBuilder()
            t_5771.append_safe('v IN (')
            t_5771.append_date_list(dates_1083)
            t_5771.append_safe(')')
            actual_1364: 'str27' = t_5771.accumulated.to_string()
            t_5778: 'bool33' = actual_1364 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_5720() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_1364, ')')
            test_109.assert_(t_5778, fn_5720)
        finally:
            test_109.soft_fail_to_hard()
class TestCase125(TestCase46):
    def test___sqlFloat64_naNRendersAsNull__1367(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_110: Test = Test()
        try:
            nan_1085: 'float38'
            nan_1085 = 0.0 / 0.0
            t_5712: 'SqlBuilder' = SqlBuilder()
            t_5712.append_safe('v = ')
            t_5712.append_float64(nan_1085)
            actual_1368: 'str27' = t_5712.accumulated.to_string()
            t_5718: 'bool33' = actual_1368 == 'v = NULL'
            def fn_5711() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_1368, ')')
            test_110.assert_(t_5718, fn_5711)
        finally:
            test_110.soft_fail_to_hard()
class TestCase126(TestCase46):
    def test___sqlFloat64_infinityRendersAsNull__1371(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_111: Test = Test()
        try:
            inf_1087: 'float38'
            inf_1087 = 1.0 / 0.0
            t_5703: 'SqlBuilder' = SqlBuilder()
            t_5703.append_safe('v = ')
            t_5703.append_float64(inf_1087)
            actual_1372: 'str27' = t_5703.accumulated.to_string()
            t_5709: 'bool33' = actual_1372 == 'v = NULL'
            def fn_5702() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_1372, ')')
            test_111.assert_(t_5709, fn_5702)
        finally:
            test_111.soft_fail_to_hard()
class TestCase127(TestCase46):
    def test___sqlFloat64_negativeInfinityRendersAsNull__1375(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_112: Test = Test()
        try:
            ninf_1089: 'float38'
            ninf_1089 = -1.0 / 0.0
            t_5694: 'SqlBuilder' = SqlBuilder()
            t_5694.append_safe('v = ')
            t_5694.append_float64(ninf_1089)
            actual_1376: 'str27' = t_5694.accumulated.to_string()
            t_5700: 'bool33' = actual_1376 == 'v = NULL'
            def fn_5693() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_1376, ')')
            test_112.assert_(t_5700, fn_5693)
        finally:
            test_112.soft_fail_to_hard()
class TestCase128(TestCase46):
    def test___sqlFloat64_normalValuesStillWork__1379(self) -> None:
        'SqlFloat64 normal values still work'
        test_113: Test = Test()
        try:
            t_5669: 'SqlBuilder' = SqlBuilder()
            t_5669.append_safe('v = ')
            t_5669.append_float64(3.14)
            actual_1380: 'str27' = t_5669.accumulated.to_string()
            t_5675: 'bool33' = actual_1380 == 'v = 3.14'
            def fn_5668() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_1380, ')')
            test_113.assert_(t_5675, fn_5668)
            t_5677: 'SqlBuilder' = SqlBuilder()
            t_5677.append_safe('v = ')
            t_5677.append_float64(0.0)
            actual_1383: 'str27' = t_5677.accumulated.to_string()
            t_5683: 'bool33' = actual_1383 == 'v = 0.0'
            def fn_5667() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_1383, ')')
            test_113.assert_(t_5683, fn_5667)
            t_5685: 'SqlBuilder' = SqlBuilder()
            t_5685.append_safe('v = ')
            t_5685.append_float64(-42.5)
            actual_1386: 'str27' = t_5685.accumulated.to_string()
            t_5691: 'bool33' = actual_1386 == 'v = -42.5'
            def fn_5666() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_1386, ')')
            test_113.assert_(t_5691, fn_5666)
        finally:
            test_113.soft_fail_to_hard()
class TestCase129(TestCase46):
    def test___sqlDateRendersWithQuotes__1389(self) -> None:
        'SqlDate renders with quotes'
        test_114: Test = Test()
        try:
            t_2792: 'date26'
            t_2792 = date_7262(2024, 6, 15)
            d_1092: 'date26' = t_2792
            t_5658: 'SqlBuilder' = SqlBuilder()
            t_5658.append_safe('v = ')
            t_5658.append_date(d_1092)
            actual_1390: 'str27' = t_5658.accumulated.to_string()
            t_5664: 'bool33' = actual_1390 == "v = '2024-06-15'"
            def fn_5657() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_1390, ')')
            test_114.assert_(t_5664, fn_5657)
        finally:
            test_114.soft_fail_to_hard()
class TestCase130(TestCase46):
    def test___nesting__1393(self) -> None:
        'nesting'
        test_115: Test = Test()
        try:
            name_1094: 'str27' = 'Someone'
            t_5626: 'SqlBuilder' = SqlBuilder()
            t_5626.append_safe('where p.last_name = ')
            t_5626.append_string('Someone')
            condition_1095: 'SqlFragment' = t_5626.accumulated
            t_5630: 'SqlBuilder' = SqlBuilder()
            t_5630.append_safe('select p.id from person p ')
            t_5630.append_fragment(condition_1095)
            actual_1395: 'str27' = t_5630.accumulated.to_string()
            t_5636: 'bool33' = actual_1395 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_5625() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1395, ')')
            test_115.assert_(t_5636, fn_5625)
            t_5638: 'SqlBuilder' = SqlBuilder()
            t_5638.append_safe('select p.id from person p ')
            t_5638.append_part(condition_1095.to_source())
            actual_1398: 'str27' = t_5638.accumulated.to_string()
            t_5645: 'bool33' = actual_1398 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_5624() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1398, ')')
            test_115.assert_(t_5645, fn_5624)
            parts_1096: 'Sequence29[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_5649: 'SqlBuilder' = SqlBuilder()
            t_5649.append_safe('select ')
            t_5649.append_part_list(parts_1096)
            actual_1401: 'str27' = t_5649.accumulated.to_string()
            t_5655: 'bool33' = actual_1401 == "select 'a''b', 3"
            def fn_5623() -> 'str27':
                return str_cat_7237('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_1401, ')')
            test_115.assert_(t_5655, fn_5623)
        finally:
            test_115.soft_fail_to_hard()
