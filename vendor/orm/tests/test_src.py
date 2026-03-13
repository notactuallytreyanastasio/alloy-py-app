from temper_std.testing import Test
from builtins import str as str27, bool as bool33, Exception as Exception37, int as int31, float as float38
from unittest import TestCase as TestCase46
from types import MappingProxyType as MappingProxyType32
from typing import Sequence as Sequence29
from datetime import date as date26
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_9706, pair_9710, changeset, Changeset, mapped_has_9683, len_9686, list_get_9694, str_cat_9688, list_for_each_9680, SqlFragment, from_, Query, SqlBuilder, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, date_9713, SqlPart
def csid_459(name_604: 'str27') -> 'SafeIdentifier':
    t_5286: 'SafeIdentifier'
    t_5286 = safe_identifier(name_604)
    return t_5286
def user_table_460() -> 'TableDef':
    return TableDef(csid_459('users'), (FieldDef(csid_459('name'), StringField(), False), FieldDef(csid_459('email'), StringField(), False), FieldDef(csid_459('age'), IntField(), True), FieldDef(csid_459('score'), FloatField(), True), FieldDef(csid_459('active'), BoolField(), True)))
class TestCase45(TestCase46):
    def test___castWhitelistsAllowedFields__1404(self) -> None:
        'cast whitelists allowed fields'
        test_24: Test = Test()
        try:
            params_608: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'Alice'), pair_9710('email', 'alice@example.com'), pair_9710('admin', 'true')))
            t_9397: 'TableDef' = user_table_460()
            t_9398: 'SafeIdentifier' = csid_459('name')
            t_9399: 'SafeIdentifier' = csid_459('email')
            cs_609: 'Changeset' = changeset(t_9397, params_608).cast((t_9398, t_9399))
            t_9402: 'bool33' = mapped_has_9683(cs_609.changes, 'name')
            def fn_9392() -> 'str27':
                return 'name should be in changes'
            test_24.assert_(t_9402, fn_9392)
            t_9406: 'bool33' = mapped_has_9683(cs_609.changes, 'email')
            def fn_9391() -> 'str27':
                return 'email should be in changes'
            test_24.assert_(t_9406, fn_9391)
            t_9412: 'bool33' = not mapped_has_9683(cs_609.changes, 'admin')
            def fn_9390() -> 'str27':
                return 'admin must be dropped (not in whitelist)'
            test_24.assert_(t_9412, fn_9390)
            t_9414: 'bool33' = cs_609.is_valid
            def fn_9389() -> 'str27':
                return 'should still be valid'
            test_24.assert_(t_9414, fn_9389)
        finally:
            test_24.soft_fail_to_hard()
class TestCase47(TestCase46):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__1405(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_25: Test = Test()
        try:
            params_611: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'Alice'), pair_9710('email', 'alice@example.com')))
            t_9375: 'TableDef' = user_table_460()
            t_9376: 'SafeIdentifier' = csid_459('name')
            cs_612: 'Changeset' = changeset(t_9375, params_611).cast((t_9376,)).cast((csid_459('email'),))
            t_9383: 'bool33' = not mapped_has_9683(cs_612.changes, 'name')
            def fn_9371() -> 'str27':
                return 'name must be excluded by second cast'
            test_25.assert_(t_9383, fn_9371)
            t_9386: 'bool33' = mapped_has_9683(cs_612.changes, 'email')
            def fn_9370() -> 'str27':
                return 'email should be present'
            test_25.assert_(t_9386, fn_9370)
        finally:
            test_25.soft_fail_to_hard()
class TestCase48(TestCase46):
    def test___castIgnoresEmptyStringValues__1406(self) -> None:
        'cast ignores empty string values'
        test_26: Test = Test()
        try:
            params_614: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', ''), pair_9710('email', 'bob@example.com')))
            t_9357: 'TableDef' = user_table_460()
            t_9358: 'SafeIdentifier' = csid_459('name')
            t_9359: 'SafeIdentifier' = csid_459('email')
            cs_615: 'Changeset' = changeset(t_9357, params_614).cast((t_9358, t_9359))
            t_9364: 'bool33' = not mapped_has_9683(cs_615.changes, 'name')
            def fn_9353() -> 'str27':
                return 'empty name should not be in changes'
            test_26.assert_(t_9364, fn_9353)
            t_9367: 'bool33' = mapped_has_9683(cs_615.changes, 'email')
            def fn_9352() -> 'str27':
                return 'email should be in changes'
            test_26.assert_(t_9367, fn_9352)
        finally:
            test_26.soft_fail_to_hard()
class TestCase49(TestCase46):
    def test___validateRequiredPassesWhenFieldPresent__1407(self) -> None:
        'validateRequired passes when field present'
        test_27: Test = Test()
        try:
            params_617: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'Alice'),))
            t_9339: 'TableDef' = user_table_460()
            t_9340: 'SafeIdentifier' = csid_459('name')
            cs_618: 'Changeset' = changeset(t_9339, params_617).cast((t_9340,)).validate_required((csid_459('name'),))
            t_9344: 'bool33' = cs_618.is_valid
            def fn_9336() -> 'str27':
                return 'should be valid'
            test_27.assert_(t_9344, fn_9336)
            t_9350: 'bool33' = len_9686(cs_618.errors) == 0
            def fn_9335() -> 'str27':
                return 'no errors expected'
            test_27.assert_(t_9350, fn_9335)
        finally:
            test_27.soft_fail_to_hard()
class TestCase50(TestCase46):
    def test___validateRequiredFailsWhenFieldMissing__1408(self) -> None:
        'validateRequired fails when field missing'
        test_28: Test = Test()
        try:
            params_620: 'MappingProxyType32[str27, str27]' = map_constructor_9706(())
            t_9315: 'TableDef' = user_table_460()
            t_9316: 'SafeIdentifier' = csid_459('name')
            cs_621: 'Changeset' = changeset(t_9315, params_620).cast((t_9316,)).validate_required((csid_459('name'),))
            t_9322: 'bool33' = not cs_621.is_valid
            def fn_9313() -> 'str27':
                return 'should be invalid'
            test_28.assert_(t_9322, fn_9313)
            t_9327: 'bool33' = len_9686(cs_621.errors) == 1
            def fn_9312() -> 'str27':
                return 'should have one error'
            test_28.assert_(t_9327, fn_9312)
            t_9333: 'bool33' = list_get_9694(cs_621.errors, 0).field == 'name'
            def fn_9311() -> 'str27':
                return 'error should name the field'
            test_28.assert_(t_9333, fn_9311)
        finally:
            test_28.soft_fail_to_hard()
class TestCase51(TestCase46):
    def test___validateLengthPassesWithinRange__1409(self) -> None:
        'validateLength passes within range'
        test_29: Test = Test()
        try:
            params_623: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'Alice'),))
            t_9303: 'TableDef' = user_table_460()
            t_9304: 'SafeIdentifier' = csid_459('name')
            cs_624: 'Changeset' = changeset(t_9303, params_623).cast((t_9304,)).validate_length(csid_459('name'), 2, 50)
            t_9308: 'bool33' = cs_624.is_valid
            def fn_9300() -> 'str27':
                return 'should be valid'
            test_29.assert_(t_9308, fn_9300)
        finally:
            test_29.soft_fail_to_hard()
class TestCase52(TestCase46):
    def test___validateLengthFailsWhenTooShort__1410(self) -> None:
        'validateLength fails when too short'
        test_30: Test = Test()
        try:
            params_626: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'A'),))
            t_9291: 'TableDef' = user_table_460()
            t_9292: 'SafeIdentifier' = csid_459('name')
            cs_627: 'Changeset' = changeset(t_9291, params_626).cast((t_9292,)).validate_length(csid_459('name'), 2, 50)
            t_9298: 'bool33' = not cs_627.is_valid
            def fn_9288() -> 'str27':
                return 'should be invalid'
            test_30.assert_(t_9298, fn_9288)
        finally:
            test_30.soft_fail_to_hard()
class TestCase53(TestCase46):
    def test___validateLengthFailsWhenTooLong__1411(self) -> None:
        'validateLength fails when too long'
        test_31: Test = Test()
        try:
            params_629: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_9279: 'TableDef' = user_table_460()
            t_9280: 'SafeIdentifier' = csid_459('name')
            cs_630: 'Changeset' = changeset(t_9279, params_629).cast((t_9280,)).validate_length(csid_459('name'), 2, 10)
            t_9286: 'bool33' = not cs_630.is_valid
            def fn_9276() -> 'str27':
                return 'should be invalid'
            test_31.assert_(t_9286, fn_9276)
        finally:
            test_31.soft_fail_to_hard()
class TestCase54(TestCase46):
    def test___validateIntPassesForValidInteger__1412(self) -> None:
        'validateInt passes for valid integer'
        test_32: Test = Test()
        try:
            params_632: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('age', '30'),))
            t_9268: 'TableDef' = user_table_460()
            t_9269: 'SafeIdentifier' = csid_459('age')
            cs_633: 'Changeset' = changeset(t_9268, params_632).cast((t_9269,)).validate_int(csid_459('age'))
            t_9273: 'bool33' = cs_633.is_valid
            def fn_9265() -> 'str27':
                return 'should be valid'
            test_32.assert_(t_9273, fn_9265)
        finally:
            test_32.soft_fail_to_hard()
class TestCase55(TestCase46):
    def test___validateIntFailsForNonInteger__1413(self) -> None:
        'validateInt fails for non-integer'
        test_33: Test = Test()
        try:
            params_635: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('age', 'not-a-number'),))
            t_9256: 'TableDef' = user_table_460()
            t_9257: 'SafeIdentifier' = csid_459('age')
            cs_636: 'Changeset' = changeset(t_9256, params_635).cast((t_9257,)).validate_int(csid_459('age'))
            t_9263: 'bool33' = not cs_636.is_valid
            def fn_9253() -> 'str27':
                return 'should be invalid'
            test_33.assert_(t_9263, fn_9253)
        finally:
            test_33.soft_fail_to_hard()
class TestCase56(TestCase46):
    def test___validateFloatPassesForValidFloat__1414(self) -> None:
        'validateFloat passes for valid float'
        test_34: Test = Test()
        try:
            params_638: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('score', '9.5'),))
            t_9245: 'TableDef' = user_table_460()
            t_9246: 'SafeIdentifier' = csid_459('score')
            cs_639: 'Changeset' = changeset(t_9245, params_638).cast((t_9246,)).validate_float(csid_459('score'))
            t_9250: 'bool33' = cs_639.is_valid
            def fn_9242() -> 'str27':
                return 'should be valid'
            test_34.assert_(t_9250, fn_9242)
        finally:
            test_34.soft_fail_to_hard()
class TestCase57(TestCase46):
    def test___validateInt64_passesForValid64_bitInteger__1415(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_35: Test = Test()
        try:
            params_641: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('age', '9999999999'),))
            t_9234: 'TableDef' = user_table_460()
            t_9235: 'SafeIdentifier' = csid_459('age')
            cs_642: 'Changeset' = changeset(t_9234, params_641).cast((t_9235,)).validate_int64(csid_459('age'))
            t_9239: 'bool33' = cs_642.is_valid
            def fn_9231() -> 'str27':
                return 'should be valid'
            test_35.assert_(t_9239, fn_9231)
        finally:
            test_35.soft_fail_to_hard()
class TestCase58(TestCase46):
    def test___validateInt64_failsForNonInteger__1416(self) -> None:
        'validateInt64 fails for non-integer'
        test_36: Test = Test()
        try:
            params_644: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('age', 'not-a-number'),))
            t_9222: 'TableDef' = user_table_460()
            t_9223: 'SafeIdentifier' = csid_459('age')
            cs_645: 'Changeset' = changeset(t_9222, params_644).cast((t_9223,)).validate_int64(csid_459('age'))
            t_9229: 'bool33' = not cs_645.is_valid
            def fn_9219() -> 'str27':
                return 'should be invalid'
            test_36.assert_(t_9229, fn_9219)
        finally:
            test_36.soft_fail_to_hard()
class TestCase59(TestCase46):
    def test___validateBoolAcceptsTrue1_yesOn__1417(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_37: Test = Test()
        try:
            def fn_9216(v_647: 'str27') -> 'None':
                params_648: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('active', v_647),))
                t_9208: 'TableDef' = user_table_460()
                t_9209: 'SafeIdentifier' = csid_459('active')
                cs_649: 'Changeset' = changeset(t_9208, params_648).cast((t_9209,)).validate_bool(csid_459('active'))
                t_9213: 'bool33' = cs_649.is_valid
                def fn_9205() -> 'str27':
                    return str_cat_9688('should accept: ', v_647)
                test_37.assert_(t_9213, fn_9205)
            list_for_each_9680(('true', '1', 'yes', 'on'), fn_9216)
        finally:
            test_37.soft_fail_to_hard()
class TestCase60(TestCase46):
    def test___validateBoolAcceptsFalse0_noOff__1418(self) -> None:
        'validateBool accepts false/0/no/off'
        test_38: Test = Test()
        try:
            def fn_9202(v_651: 'str27') -> 'None':
                params_652: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('active', v_651),))
                t_9194: 'TableDef' = user_table_460()
                t_9195: 'SafeIdentifier' = csid_459('active')
                cs_653: 'Changeset' = changeset(t_9194, params_652).cast((t_9195,)).validate_bool(csid_459('active'))
                t_9199: 'bool33' = cs_653.is_valid
                def fn_9191() -> 'str27':
                    return str_cat_9688('should accept: ', v_651)
                test_38.assert_(t_9199, fn_9191)
            list_for_each_9680(('false', '0', 'no', 'off'), fn_9202)
        finally:
            test_38.soft_fail_to_hard()
class TestCase61(TestCase46):
    def test___validateBoolRejectsAmbiguousValues__1419(self) -> None:
        'validateBool rejects ambiguous values'
        test_39: Test = Test()
        try:
            def fn_9188(v_655: 'str27') -> 'None':
                params_656: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('active', v_655),))
                t_9179: 'TableDef' = user_table_460()
                t_9180: 'SafeIdentifier' = csid_459('active')
                cs_657: 'Changeset' = changeset(t_9179, params_656).cast((t_9180,)).validate_bool(csid_459('active'))
                t_9186: 'bool33' = not cs_657.is_valid
                def fn_9176() -> 'str27':
                    return str_cat_9688('should reject ambiguous: ', v_655)
                test_39.assert_(t_9186, fn_9176)
            list_for_each_9680(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_9188)
        finally:
            test_39.soft_fail_to_hard()
class TestCase62(TestCase46):
    def test___toInsertSqlEscapesBobbyTables__1420(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_40: Test = Test()
        try:
            params_659: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', "Robert'); DROP TABLE users;--"), pair_9710('email', 'bobby@evil.com')))
            t_9164: 'TableDef' = user_table_460()
            t_9165: 'SafeIdentifier' = csid_459('name')
            t_9166: 'SafeIdentifier' = csid_459('email')
            cs_660: 'Changeset' = changeset(t_9164, params_659).cast((t_9165, t_9166)).validate_required((csid_459('name'), csid_459('email')))
            t_5087: 'SqlFragment'
            t_5087 = cs_660.to_insert_sql()
            sql_frag_661: 'SqlFragment' = t_5087
            s_662: 'str27' = sql_frag_661.to_string()
            t_9173: 'bool33' = s_662.find("''") >= 0
            def fn_9160() -> 'str27':
                return str_cat_9688('single quote must be doubled: ', s_662)
            test_40.assert_(t_9173, fn_9160)
        finally:
            test_40.soft_fail_to_hard()
class TestCase63(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForStringField__1421(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_41: Test = Test()
        try:
            params_664: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'Alice'), pair_9710('email', 'a@example.com')))
            t_9144: 'TableDef' = user_table_460()
            t_9145: 'SafeIdentifier' = csid_459('name')
            t_9146: 'SafeIdentifier' = csid_459('email')
            cs_665: 'Changeset' = changeset(t_9144, params_664).cast((t_9145, t_9146)).validate_required((csid_459('name'), csid_459('email')))
            t_5066: 'SqlFragment'
            t_5066 = cs_665.to_insert_sql()
            sql_frag_666: 'SqlFragment' = t_5066
            s_667: 'str27' = sql_frag_666.to_string()
            t_9153: 'bool33' = s_667.find('INSERT INTO users') >= 0
            def fn_9140() -> 'str27':
                return str_cat_9688('has INSERT INTO: ', s_667)
            test_41.assert_(t_9153, fn_9140)
            t_9157: 'bool33' = s_667.find("'Alice'") >= 0
            def fn_9139() -> 'str27':
                return str_cat_9688('has quoted name: ', s_667)
            test_41.assert_(t_9157, fn_9139)
        finally:
            test_41.soft_fail_to_hard()
class TestCase64(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForIntField__1422(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_42: Test = Test()
        try:
            params_669: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'Bob'), pair_9710('email', 'b@example.com'), pair_9710('age', '25')))
            t_9126: 'TableDef' = user_table_460()
            t_9127: 'SafeIdentifier' = csid_459('name')
            t_9128: 'SafeIdentifier' = csid_459('email')
            t_9129: 'SafeIdentifier' = csid_459('age')
            cs_670: 'Changeset' = changeset(t_9126, params_669).cast((t_9127, t_9128, t_9129)).validate_required((csid_459('name'), csid_459('email')))
            t_5049: 'SqlFragment'
            t_5049 = cs_670.to_insert_sql()
            sql_frag_671: 'SqlFragment' = t_5049
            s_672: 'str27' = sql_frag_671.to_string()
            t_9136: 'bool33' = s_672.find('25') >= 0
            def fn_9121() -> 'str27':
                return str_cat_9688('age rendered unquoted: ', s_672)
            test_42.assert_(t_9136, fn_9121)
        finally:
            test_42.soft_fail_to_hard()
class TestCase65(TestCase46):
    def test___toInsertSqlBubblesOnInvalidChangeset__1423(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_43: Test = Test()
        try:
            params_674: 'MappingProxyType32[str27, str27]' = map_constructor_9706(())
            t_9114: 'TableDef' = user_table_460()
            t_9115: 'SafeIdentifier' = csid_459('name')
            cs_675: 'Changeset' = changeset(t_9114, params_674).cast((t_9115,)).validate_required((csid_459('name'),))
            did_bubble_676: 'bool33'
            try:
                cs_675.to_insert_sql()
                did_bubble_676 = False
            except Exception37:
                did_bubble_676 = True
            def fn_9112() -> 'str27':
                return 'invalid changeset should bubble'
            test_43.assert_(did_bubble_676, fn_9112)
        finally:
            test_43.soft_fail_to_hard()
class TestCase66(TestCase46):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__1424(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_44: Test = Test()
        try:
            strict_table_678: 'TableDef' = TableDef(csid_459('posts'), (FieldDef(csid_459('title'), StringField(), False), FieldDef(csid_459('body'), StringField(), True)))
            params_679: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('body', 'hello'),))
            t_9105: 'SafeIdentifier' = csid_459('body')
            cs_680: 'Changeset' = changeset(strict_table_678, params_679).cast((t_9105,))
            t_9107: 'bool33' = cs_680.is_valid
            def fn_9094() -> 'str27':
                return 'changeset should appear valid (no explicit validation run)'
            test_44.assert_(t_9107, fn_9094)
            did_bubble_681: 'bool33'
            try:
                cs_680.to_insert_sql()
                did_bubble_681 = False
            except Exception37:
                did_bubble_681 = True
            def fn_9093() -> 'str27':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_44.assert_(did_bubble_681, fn_9093)
        finally:
            test_44.soft_fail_to_hard()
class TestCase67(TestCase46):
    def test___toUpdateSqlProducesCorrectSql__1425(self) -> None:
        'toUpdateSql produces correct SQL'
        test_45: Test = Test()
        try:
            params_683: 'MappingProxyType32[str27, str27]' = map_constructor_9706((pair_9710('name', 'Bob'),))
            t_9084: 'TableDef' = user_table_460()
            t_9085: 'SafeIdentifier' = csid_459('name')
            cs_684: 'Changeset' = changeset(t_9084, params_683).cast((t_9085,)).validate_required((csid_459('name'),))
            t_5009: 'SqlFragment'
            t_5009 = cs_684.to_update_sql(42)
            sql_frag_685: 'SqlFragment' = t_5009
            s_686: 'str27' = sql_frag_685.to_string()
            t_9091: 'bool33' = s_686 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_9081() -> 'str27':
                return str_cat_9688('got: ', s_686)
            test_45.assert_(t_9091, fn_9081)
        finally:
            test_45.soft_fail_to_hard()
class TestCase68(TestCase46):
    def test___toUpdateSqlBubblesOnInvalidChangeset__1426(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_46: Test = Test()
        try:
            params_688: 'MappingProxyType32[str27, str27]' = map_constructor_9706(())
            t_9074: 'TableDef' = user_table_460()
            t_9075: 'SafeIdentifier' = csid_459('name')
            cs_689: 'Changeset' = changeset(t_9074, params_688).cast((t_9075,)).validate_required((csid_459('name'),))
            did_bubble_690: 'bool33'
            try:
                cs_689.to_update_sql(1)
                did_bubble_690 = False
            except Exception37:
                did_bubble_690 = True
            def fn_9072() -> 'str27':
                return 'invalid changeset should bubble'
            test_46.assert_(did_bubble_690, fn_9072)
        finally:
            test_46.soft_fail_to_hard()
def sid_461(name_932: 'str27') -> 'SafeIdentifier':
    t_4603: 'SafeIdentifier'
    t_4603 = safe_identifier(name_932)
    return t_4603
class TestCase69(TestCase46):
    def test___bareFromProducesSelect__1475(self) -> None:
        'bare from produces SELECT *'
        test_47: Test = Test()
        try:
            q_935: 'Query' = from_(sid_461('users'))
            t_8681: 'bool33' = q_935.to_sql().to_string() == 'SELECT * FROM users'
            def fn_8676() -> 'str27':
                return 'bare query'
            test_47.assert_(t_8681, fn_8676)
        finally:
            test_47.soft_fail_to_hard()
class TestCase70(TestCase46):
    def test___selectRestrictsColumns__1476(self) -> None:
        'select restricts columns'
        test_48: Test = Test()
        try:
            t_8667: 'SafeIdentifier' = sid_461('users')
            t_8668: 'SafeIdentifier' = sid_461('id')
            t_8669: 'SafeIdentifier' = sid_461('name')
            q_937: 'Query' = from_(t_8667).select((t_8668, t_8669))
            t_8674: 'bool33' = q_937.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_8666() -> 'str27':
                return 'select columns'
            test_48.assert_(t_8674, fn_8666)
        finally:
            test_48.soft_fail_to_hard()
class TestCase71(TestCase46):
    def test___whereAddsConditionWithIntValue__1477(self) -> None:
        'where adds condition with int value'
        test_49: Test = Test()
        try:
            t_8655: 'SafeIdentifier' = sid_461('users')
            t_8656: 'SqlBuilder' = SqlBuilder()
            t_8656.append_safe('age > ')
            t_8656.append_int32(18)
            t_8659: 'SqlFragment' = t_8656.accumulated
            q_939: 'Query' = from_(t_8655).where(t_8659)
            t_8664: 'bool33' = q_939.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_8654() -> 'str27':
                return 'where int'
            test_49.assert_(t_8664, fn_8654)
        finally:
            test_49.soft_fail_to_hard()
class TestCase72(TestCase46):
    def test___whereAddsConditionWithBoolValue__1479(self) -> None:
        'where adds condition with bool value'
        test_50: Test = Test()
        try:
            t_8643: 'SafeIdentifier' = sid_461('users')
            t_8644: 'SqlBuilder' = SqlBuilder()
            t_8644.append_safe('active = ')
            t_8644.append_boolean(True)
            t_8647: 'SqlFragment' = t_8644.accumulated
            q_941: 'Query' = from_(t_8643).where(t_8647)
            t_8652: 'bool33' = q_941.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_8642() -> 'str27':
                return 'where bool'
            test_50.assert_(t_8652, fn_8642)
        finally:
            test_50.soft_fail_to_hard()
class TestCase73(TestCase46):
    def test___chainedWhereUsesAnd__1481(self) -> None:
        'chained where uses AND'
        test_51: Test = Test()
        try:
            t_8626: 'SafeIdentifier' = sid_461('users')
            t_8627: 'SqlBuilder' = SqlBuilder()
            t_8627.append_safe('age > ')
            t_8627.append_int32(18)
            t_8630: 'SqlFragment' = t_8627.accumulated
            t_8631: 'Query' = from_(t_8626).where(t_8630)
            t_8632: 'SqlBuilder' = SqlBuilder()
            t_8632.append_safe('active = ')
            t_8632.append_boolean(True)
            q_943: 'Query' = t_8631.where(t_8632.accumulated)
            t_8640: 'bool33' = q_943.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_8625() -> 'str27':
                return 'chained where'
            test_51.assert_(t_8640, fn_8625)
        finally:
            test_51.soft_fail_to_hard()
class TestCase74(TestCase46):
    def test___orderByAsc__1484(self) -> None:
        'orderBy ASC'
        test_52: Test = Test()
        try:
            t_8617: 'SafeIdentifier' = sid_461('users')
            t_8618: 'SafeIdentifier' = sid_461('name')
            q_945: 'Query' = from_(t_8617).order_by(t_8618, True)
            t_8623: 'bool33' = q_945.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_8616() -> 'str27':
                return 'order asc'
            test_52.assert_(t_8623, fn_8616)
        finally:
            test_52.soft_fail_to_hard()
class TestCase75(TestCase46):
    def test___orderByDesc__1485(self) -> None:
        'orderBy DESC'
        test_53: Test = Test()
        try:
            t_8608: 'SafeIdentifier' = sid_461('users')
            t_8609: 'SafeIdentifier' = sid_461('created_at')
            q_947: 'Query' = from_(t_8608).order_by(t_8609, False)
            t_8614: 'bool33' = q_947.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_8607() -> 'str27':
                return 'order desc'
            test_53.assert_(t_8614, fn_8607)
        finally:
            test_53.soft_fail_to_hard()
class TestCase76(TestCase46):
    def test___limitAndOffset__1486(self) -> None:
        'limit and offset'
        test_54: Test = Test()
        try:
            t_4537: 'Query'
            t_4537 = from_(sid_461('users')).limit(10)
            t_4538: 'Query'
            t_4538 = t_4537.offset(20)
            q_949: 'Query' = t_4538
            t_8605: 'bool33' = q_949.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_8600() -> 'str27':
                return 'limit/offset'
            test_54.assert_(t_8605, fn_8600)
        finally:
            test_54.soft_fail_to_hard()
class TestCase77(TestCase46):
    def test___limitBubblesOnNegative__1487(self) -> None:
        'limit bubbles on negative'
        test_55: Test = Test()
        try:
            did_bubble_951: 'bool33'
            try:
                from_(sid_461('users')).limit(-1)
                did_bubble_951 = False
            except Exception37:
                did_bubble_951 = True
            def fn_8596() -> 'str27':
                return 'negative limit should bubble'
            test_55.assert_(did_bubble_951, fn_8596)
        finally:
            test_55.soft_fail_to_hard()
class TestCase78(TestCase46):
    def test___offsetBubblesOnNegative__1488(self) -> None:
        'offset bubbles on negative'
        test_56: Test = Test()
        try:
            did_bubble_953: 'bool33'
            try:
                from_(sid_461('users')).offset(-1)
                did_bubble_953 = False
            except Exception37:
                did_bubble_953 = True
            def fn_8592() -> 'str27':
                return 'negative offset should bubble'
            test_56.assert_(did_bubble_953, fn_8592)
        finally:
            test_56.soft_fail_to_hard()
class TestCase79(TestCase46):
    def test___complexComposedQuery__1489(self) -> None:
        'complex composed query'
        test_57: Test = Test()
        try:
            min_age_955: 'int31' = 21
            t_8570: 'SafeIdentifier' = sid_461('users')
            t_8571: 'SafeIdentifier' = sid_461('id')
            t_8572: 'SafeIdentifier' = sid_461('name')
            t_8573: 'SafeIdentifier' = sid_461('email')
            t_8574: 'Query' = from_(t_8570).select((t_8571, t_8572, t_8573))
            t_8575: 'SqlBuilder' = SqlBuilder()
            t_8575.append_safe('age >= ')
            t_8575.append_int32(21)
            t_8579: 'Query' = t_8574.where(t_8575.accumulated)
            t_8580: 'SqlBuilder' = SqlBuilder()
            t_8580.append_safe('active = ')
            t_8580.append_boolean(True)
            t_4523: 'Query'
            t_4523 = t_8579.where(t_8580.accumulated).order_by(sid_461('name'), True).limit(25)
            t_4524: 'Query'
            t_4524 = t_4523.offset(0)
            q_956: 'Query' = t_4524
            t_8590: 'bool33' = q_956.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_8569() -> 'str27':
                return 'complex query'
            test_57.assert_(t_8590, fn_8569)
        finally:
            test_57.soft_fail_to_hard()
class TestCase80(TestCase46):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__1492(self) -> None:
        'safeToSql applies default limit when none set'
        test_58: Test = Test()
        try:
            q_958: 'Query' = from_(sid_461('users'))
            t_4500: 'SqlFragment'
            t_4500 = q_958.safe_to_sql(100)
            t_4501: 'SqlFragment' = t_4500
            s_959: 'str27' = t_4501.to_string()
            t_8567: 'bool33' = s_959 == 'SELECT * FROM users LIMIT 100'
            def fn_8563() -> 'str27':
                return str_cat_9688('should have limit: ', s_959)
            test_58.assert_(t_8567, fn_8563)
        finally:
            test_58.soft_fail_to_hard()
class TestCase81(TestCase46):
    def test___safeToSqlRespectsExplicitLimit__1493(self) -> None:
        'safeToSql respects explicit limit'
        test_59: Test = Test()
        try:
            t_4492: 'Query'
            t_4492 = from_(sid_461('users')).limit(5)
            q_961: 'Query' = t_4492
            t_4495: 'SqlFragment'
            t_4495 = q_961.safe_to_sql(100)
            t_4496: 'SqlFragment' = t_4495
            s_962: 'str27' = t_4496.to_string()
            t_8561: 'bool33' = s_962 == 'SELECT * FROM users LIMIT 5'
            def fn_8557() -> 'str27':
                return str_cat_9688('explicit limit preserved: ', s_962)
            test_59.assert_(t_8561, fn_8557)
        finally:
            test_59.soft_fail_to_hard()
class TestCase82(TestCase46):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__1494(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_60: Test = Test()
        try:
            did_bubble_964: 'bool33'
            try:
                from_(sid_461('users')).safe_to_sql(-1)
                did_bubble_964 = False
            except Exception37:
                did_bubble_964 = True
            def fn_8553() -> 'str27':
                return 'negative defaultLimit should bubble'
            test_60.assert_(did_bubble_964, fn_8553)
        finally:
            test_60.soft_fail_to_hard()
class TestCase83(TestCase46):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__1495(self) -> None:
        'where with injection attempt in string value is escaped'
        test_61: Test = Test()
        try:
            evil_966: 'str27' = "'; DROP TABLE users; --"
            t_8537: 'SafeIdentifier' = sid_461('users')
            t_8538: 'SqlBuilder' = SqlBuilder()
            t_8538.append_safe('name = ')
            t_8538.append_string("'; DROP TABLE users; --")
            t_8541: 'SqlFragment' = t_8538.accumulated
            q_967: 'Query' = from_(t_8537).where(t_8541)
            s_968: 'str27' = q_967.to_sql().to_string()
            t_8546: 'bool33' = s_968.find("''") >= 0
            def fn_8536() -> 'str27':
                return str_cat_9688('quotes must be doubled: ', s_968)
            test_61.assert_(t_8546, fn_8536)
            t_8550: 'bool33' = s_968.find('SELECT * FROM users WHERE name =') >= 0
            def fn_8535() -> 'str27':
                return str_cat_9688('structure intact: ', s_968)
            test_61.assert_(t_8550, fn_8535)
        finally:
            test_61.soft_fail_to_hard()
class TestCase84(TestCase46):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__1497(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_62: Test = Test()
        try:
            attack_970: 'str27' = 'users; DROP TABLE users; --'
            did_bubble_971: 'bool33'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_971 = False
            except Exception37:
                did_bubble_971 = True
            def fn_8532() -> 'str27':
                return 'metacharacter-containing name must be rejected at construction'
            test_62.assert_(did_bubble_971, fn_8532)
        finally:
            test_62.soft_fail_to_hard()
class TestCase85(TestCase46):
    def test___innerJoinProducesInnerJoin__1498(self) -> None:
        'innerJoin produces INNER JOIN'
        test_63: Test = Test()
        try:
            t_8521: 'SafeIdentifier' = sid_461('users')
            t_8522: 'SafeIdentifier' = sid_461('orders')
            t_8523: 'SqlBuilder' = SqlBuilder()
            t_8523.append_safe('users.id = orders.user_id')
            t_8525: 'SqlFragment' = t_8523.accumulated
            q_973: 'Query' = from_(t_8521).inner_join(t_8522, t_8525)
            t_8530: 'bool33' = q_973.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_8520() -> 'str27':
                return 'inner join'
            test_63.assert_(t_8530, fn_8520)
        finally:
            test_63.soft_fail_to_hard()
class TestCase86(TestCase46):
    def test___leftJoinProducesLeftJoin__1500(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_64: Test = Test()
        try:
            t_8509: 'SafeIdentifier' = sid_461('users')
            t_8510: 'SafeIdentifier' = sid_461('profiles')
            t_8511: 'SqlBuilder' = SqlBuilder()
            t_8511.append_safe('users.id = profiles.user_id')
            t_8513: 'SqlFragment' = t_8511.accumulated
            q_975: 'Query' = from_(t_8509).left_join(t_8510, t_8513)
            t_8518: 'bool33' = q_975.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_8508() -> 'str27':
                return 'left join'
            test_64.assert_(t_8518, fn_8508)
        finally:
            test_64.soft_fail_to_hard()
class TestCase87(TestCase46):
    def test___rightJoinProducesRightJoin__1502(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_65: Test = Test()
        try:
            t_8497: 'SafeIdentifier' = sid_461('orders')
            t_8498: 'SafeIdentifier' = sid_461('users')
            t_8499: 'SqlBuilder' = SqlBuilder()
            t_8499.append_safe('orders.user_id = users.id')
            t_8501: 'SqlFragment' = t_8499.accumulated
            q_977: 'Query' = from_(t_8497).right_join(t_8498, t_8501)
            t_8506: 'bool33' = q_977.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_8496() -> 'str27':
                return 'right join'
            test_65.assert_(t_8506, fn_8496)
        finally:
            test_65.soft_fail_to_hard()
class TestCase88(TestCase46):
    def test___fullJoinProducesFullOuterJoin__1504(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_66: Test = Test()
        try:
            t_8485: 'SafeIdentifier' = sid_461('users')
            t_8486: 'SafeIdentifier' = sid_461('orders')
            t_8487: 'SqlBuilder' = SqlBuilder()
            t_8487.append_safe('users.id = orders.user_id')
            t_8489: 'SqlFragment' = t_8487.accumulated
            q_979: 'Query' = from_(t_8485).full_join(t_8486, t_8489)
            t_8494: 'bool33' = q_979.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_8484() -> 'str27':
                return 'full join'
            test_66.assert_(t_8494, fn_8484)
        finally:
            test_66.soft_fail_to_hard()
class TestCase89(TestCase46):
    def test___chainedJoins__1506(self) -> None:
        'chained joins'
        test_67: Test = Test()
        try:
            t_8468: 'SafeIdentifier' = sid_461('users')
            t_8469: 'SafeIdentifier' = sid_461('orders')
            t_8470: 'SqlBuilder' = SqlBuilder()
            t_8470.append_safe('users.id = orders.user_id')
            t_8472: 'SqlFragment' = t_8470.accumulated
            t_8473: 'Query' = from_(t_8468).inner_join(t_8469, t_8472)
            t_8474: 'SafeIdentifier' = sid_461('profiles')
            t_8475: 'SqlBuilder' = SqlBuilder()
            t_8475.append_safe('users.id = profiles.user_id')
            q_981: 'Query' = t_8473.left_join(t_8474, t_8475.accumulated)
            t_8482: 'bool33' = q_981.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_8467() -> 'str27':
                return 'chained joins'
            test_67.assert_(t_8482, fn_8467)
        finally:
            test_67.soft_fail_to_hard()
class TestCase90(TestCase46):
    def test___joinWithWhereAndOrderBy__1509(self) -> None:
        'join with where and orderBy'
        test_68: Test = Test()
        try:
            t_8449: 'SafeIdentifier' = sid_461('users')
            t_8450: 'SafeIdentifier' = sid_461('orders')
            t_8451: 'SqlBuilder' = SqlBuilder()
            t_8451.append_safe('users.id = orders.user_id')
            t_8453: 'SqlFragment' = t_8451.accumulated
            t_8454: 'Query' = from_(t_8449).inner_join(t_8450, t_8453)
            t_8455: 'SqlBuilder' = SqlBuilder()
            t_8455.append_safe('orders.total > ')
            t_8455.append_int32(100)
            t_4407: 'Query'
            t_4407 = t_8454.where(t_8455.accumulated).order_by(sid_461('name'), True).limit(10)
            q_983: 'Query' = t_4407
            t_8465: 'bool33' = q_983.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_8448() -> 'str27':
                return 'join with where/order/limit'
            test_68.assert_(t_8465, fn_8448)
        finally:
            test_68.soft_fail_to_hard()
class TestCase91(TestCase46):
    def test___colHelperProducesQualifiedReference__1512(self) -> None:
        'col helper produces qualified reference'
        test_69: Test = Test()
        try:
            c_985: 'SqlFragment' = col(sid_461('users'), sid_461('id'))
            t_8446: 'bool33' = c_985.to_string() == 'users.id'
            def fn_8440() -> 'str27':
                return 'col helper'
            test_69.assert_(t_8446, fn_8440)
        finally:
            test_69.soft_fail_to_hard()
class TestCase92(TestCase46):
    def test___joinWithColHelper__1513(self) -> None:
        'join with col helper'
        test_70: Test = Test()
        try:
            on_cond_987: 'SqlFragment' = col(sid_461('users'), sid_461('id'))
            b_988: 'SqlBuilder' = SqlBuilder()
            b_988.append_fragment(on_cond_987)
            b_988.append_safe(' = ')
            b_988.append_fragment(col(sid_461('orders'), sid_461('user_id')))
            t_8431: 'SafeIdentifier' = sid_461('users')
            t_8432: 'SafeIdentifier' = sid_461('orders')
            t_8433: 'SqlFragment' = b_988.accumulated
            q_989: 'Query' = from_(t_8431).inner_join(t_8432, t_8433)
            t_8438: 'bool33' = q_989.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_8420() -> 'str27':
                return 'join with col'
            test_70.assert_(t_8438, fn_8420)
        finally:
            test_70.soft_fail_to_hard()
class TestCase93(TestCase46):
    def test___orWhereBasic__1514(self) -> None:
        'orWhere basic'
        test_71: Test = Test()
        try:
            t_8409: 'SafeIdentifier' = sid_461('users')
            t_8410: 'SqlBuilder' = SqlBuilder()
            t_8410.append_safe('status = ')
            t_8410.append_string('active')
            t_8413: 'SqlFragment' = t_8410.accumulated
            q_991: 'Query' = from_(t_8409).or_where(t_8413)
            t_8418: 'bool33' = q_991.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_8408() -> 'str27':
                return 'orWhere basic'
            test_71.assert_(t_8418, fn_8408)
        finally:
            test_71.soft_fail_to_hard()
class TestCase94(TestCase46):
    def test___whereThenOrWhere__1516(self) -> None:
        'where then orWhere'
        test_72: Test = Test()
        try:
            t_8392: 'SafeIdentifier' = sid_461('users')
            t_8393: 'SqlBuilder' = SqlBuilder()
            t_8393.append_safe('age > ')
            t_8393.append_int32(18)
            t_8396: 'SqlFragment' = t_8393.accumulated
            t_8397: 'Query' = from_(t_8392).where(t_8396)
            t_8398: 'SqlBuilder' = SqlBuilder()
            t_8398.append_safe('vip = ')
            t_8398.append_boolean(True)
            q_993: 'Query' = t_8397.or_where(t_8398.accumulated)
            t_8406: 'bool33' = q_993.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_8391() -> 'str27':
                return 'where then orWhere'
            test_72.assert_(t_8406, fn_8391)
        finally:
            test_72.soft_fail_to_hard()
class TestCase95(TestCase46):
    def test___multipleOrWhere__1519(self) -> None:
        'multiple orWhere'
        test_73: Test = Test()
        try:
            t_8370: 'SafeIdentifier' = sid_461('users')
            t_8371: 'SqlBuilder' = SqlBuilder()
            t_8371.append_safe('active = ')
            t_8371.append_boolean(True)
            t_8374: 'SqlFragment' = t_8371.accumulated
            t_8375: 'Query' = from_(t_8370).where(t_8374)
            t_8376: 'SqlBuilder' = SqlBuilder()
            t_8376.append_safe('role = ')
            t_8376.append_string('admin')
            t_8380: 'Query' = t_8375.or_where(t_8376.accumulated)
            t_8381: 'SqlBuilder' = SqlBuilder()
            t_8381.append_safe('role = ')
            t_8381.append_string('moderator')
            q_995: 'Query' = t_8380.or_where(t_8381.accumulated)
            t_8389: 'bool33' = q_995.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_8369() -> 'str27':
                return 'multiple orWhere'
            test_73.assert_(t_8389, fn_8369)
        finally:
            test_73.soft_fail_to_hard()
class TestCase96(TestCase46):
    def test___mixedWhereAndOrWhere__1523(self) -> None:
        'mixed where and orWhere'
        test_74: Test = Test()
        try:
            t_8348: 'SafeIdentifier' = sid_461('users')
            t_8349: 'SqlBuilder' = SqlBuilder()
            t_8349.append_safe('age > ')
            t_8349.append_int32(18)
            t_8352: 'SqlFragment' = t_8349.accumulated
            t_8353: 'Query' = from_(t_8348).where(t_8352)
            t_8354: 'SqlBuilder' = SqlBuilder()
            t_8354.append_safe('active = ')
            t_8354.append_boolean(True)
            t_8358: 'Query' = t_8353.where(t_8354.accumulated)
            t_8359: 'SqlBuilder' = SqlBuilder()
            t_8359.append_safe('vip = ')
            t_8359.append_boolean(True)
            q_997: 'Query' = t_8358.or_where(t_8359.accumulated)
            t_8367: 'bool33' = q_997.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_8347() -> 'str27':
                return 'mixed where and orWhere'
            test_74.assert_(t_8367, fn_8347)
        finally:
            test_74.soft_fail_to_hard()
class TestCase97(TestCase46):
    def test___whereNull__1527(self) -> None:
        'whereNull'
        test_75: Test = Test()
        try:
            t_8339: 'SafeIdentifier' = sid_461('users')
            t_8340: 'SafeIdentifier' = sid_461('deleted_at')
            q_999: 'Query' = from_(t_8339).where_null(t_8340)
            t_8345: 'bool33' = q_999.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_8338() -> 'str27':
                return 'whereNull'
            test_75.assert_(t_8345, fn_8338)
        finally:
            test_75.soft_fail_to_hard()
class TestCase98(TestCase46):
    def test___whereNotNull__1528(self) -> None:
        'whereNotNull'
        test_76: Test = Test()
        try:
            t_8330: 'SafeIdentifier' = sid_461('users')
            t_8331: 'SafeIdentifier' = sid_461('email')
            q_1001: 'Query' = from_(t_8330).where_not_null(t_8331)
            t_8336: 'bool33' = q_1001.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_8329() -> 'str27':
                return 'whereNotNull'
            test_76.assert_(t_8336, fn_8329)
        finally:
            test_76.soft_fail_to_hard()
class TestCase99(TestCase46):
    def test___whereNullChainedWithWhere__1529(self) -> None:
        'whereNull chained with where'
        test_77: Test = Test()
        try:
            t_8316: 'SafeIdentifier' = sid_461('users')
            t_8317: 'SqlBuilder' = SqlBuilder()
            t_8317.append_safe('active = ')
            t_8317.append_boolean(True)
            t_8320: 'SqlFragment' = t_8317.accumulated
            q_1003: 'Query' = from_(t_8316).where(t_8320).where_null(sid_461('deleted_at'))
            t_8327: 'bool33' = q_1003.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_8315() -> 'str27':
                return 'whereNull chained'
            test_77.assert_(t_8327, fn_8315)
        finally:
            test_77.soft_fail_to_hard()
class TestCase100(TestCase46):
    def test___whereNotNullChainedWithOrWhere__1531(self) -> None:
        'whereNotNull chained with orWhere'
        test_78: Test = Test()
        try:
            t_8302: 'SafeIdentifier' = sid_461('users')
            t_8303: 'SafeIdentifier' = sid_461('deleted_at')
            t_8304: 'Query' = from_(t_8302).where_null(t_8303)
            t_8305: 'SqlBuilder' = SqlBuilder()
            t_8305.append_safe('role = ')
            t_8305.append_string('admin')
            q_1005: 'Query' = t_8304.or_where(t_8305.accumulated)
            t_8313: 'bool33' = q_1005.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_8301() -> 'str27':
                return 'whereNotNull with orWhere'
            test_78.assert_(t_8313, fn_8301)
        finally:
            test_78.soft_fail_to_hard()
class TestCase101(TestCase46):
    def test___whereInWithIntValues__1533(self) -> None:
        'whereIn with int values'
        test_79: Test = Test()
        try:
            t_8290: 'SafeIdentifier' = sid_461('users')
            t_8291: 'SafeIdentifier' = sid_461('id')
            t_8292: 'SqlInt32' = SqlInt32(1)
            t_8293: 'SqlInt32' = SqlInt32(2)
            t_8294: 'SqlInt32' = SqlInt32(3)
            q_1007: 'Query' = from_(t_8290).where_in(t_8291, (t_8292, t_8293, t_8294))
            t_8299: 'bool33' = q_1007.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_8289() -> 'str27':
                return 'whereIn ints'
            test_79.assert_(t_8299, fn_8289)
        finally:
            test_79.soft_fail_to_hard()
class TestCase102(TestCase46):
    def test___whereInWithStringValuesEscaping__1534(self) -> None:
        'whereIn with string values escaping'
        test_80: Test = Test()
        try:
            t_8279: 'SafeIdentifier' = sid_461('users')
            t_8280: 'SafeIdentifier' = sid_461('name')
            t_8281: 'SqlString' = SqlString('Alice')
            t_8282: 'SqlString' = SqlString("Bob's")
            q_1009: 'Query' = from_(t_8279).where_in(t_8280, (t_8281, t_8282))
            t_8287: 'bool33' = q_1009.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_8278() -> 'str27':
                return 'whereIn strings'
            test_80.assert_(t_8287, fn_8278)
        finally:
            test_80.soft_fail_to_hard()
class TestCase103(TestCase46):
    def test___whereInWithEmptyListProduces1_0__1535(self) -> None:
        'whereIn with empty list produces 1=0'
        test_81: Test = Test()
        try:
            t_8270: 'SafeIdentifier' = sid_461('users')
            t_8271: 'SafeIdentifier' = sid_461('id')
            q_1011: 'Query' = from_(t_8270).where_in(t_8271, ())
            t_8276: 'bool33' = q_1011.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_8269() -> 'str27':
                return 'whereIn empty'
            test_81.assert_(t_8276, fn_8269)
        finally:
            test_81.soft_fail_to_hard()
class TestCase104(TestCase46):
    def test___whereInChained__1536(self) -> None:
        'whereIn chained'
        test_82: Test = Test()
        try:
            t_8254: 'SafeIdentifier' = sid_461('users')
            t_8255: 'SqlBuilder' = SqlBuilder()
            t_8255.append_safe('active = ')
            t_8255.append_boolean(True)
            t_8258: 'SqlFragment' = t_8255.accumulated
            q_1013: 'Query' = from_(t_8254).where(t_8258).where_in(sid_461('role'), (SqlString('admin'), SqlString('user')))
            t_8267: 'bool33' = q_1013.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_8253() -> 'str27':
                return 'whereIn chained'
            test_82.assert_(t_8267, fn_8253)
        finally:
            test_82.soft_fail_to_hard()
class TestCase105(TestCase46):
    def test___whereInSingleElement__1538(self) -> None:
        'whereIn single element'
        test_83: Test = Test()
        try:
            t_8244: 'SafeIdentifier' = sid_461('users')
            t_8245: 'SafeIdentifier' = sid_461('id')
            t_8246: 'SqlInt32' = SqlInt32(42)
            q_1015: 'Query' = from_(t_8244).where_in(t_8245, (t_8246,))
            t_8251: 'bool33' = q_1015.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_8243() -> 'str27':
                return 'whereIn single'
            test_83.assert_(t_8251, fn_8243)
        finally:
            test_83.soft_fail_to_hard()
class TestCase106(TestCase46):
    def test___whereNotBasic__1539(self) -> None:
        'whereNot basic'
        test_84: Test = Test()
        try:
            t_8232: 'SafeIdentifier' = sid_461('users')
            t_8233: 'SqlBuilder' = SqlBuilder()
            t_8233.append_safe('active = ')
            t_8233.append_boolean(True)
            t_8236: 'SqlFragment' = t_8233.accumulated
            q_1017: 'Query' = from_(t_8232).where_not(t_8236)
            t_8241: 'bool33' = q_1017.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_8231() -> 'str27':
                return 'whereNot'
            test_84.assert_(t_8241, fn_8231)
        finally:
            test_84.soft_fail_to_hard()
class TestCase107(TestCase46):
    def test___whereNotChained__1541(self) -> None:
        'whereNot chained'
        test_85: Test = Test()
        try:
            t_8215: 'SafeIdentifier' = sid_461('users')
            t_8216: 'SqlBuilder' = SqlBuilder()
            t_8216.append_safe('age > ')
            t_8216.append_int32(18)
            t_8219: 'SqlFragment' = t_8216.accumulated
            t_8220: 'Query' = from_(t_8215).where(t_8219)
            t_8221: 'SqlBuilder' = SqlBuilder()
            t_8221.append_safe('banned = ')
            t_8221.append_boolean(True)
            q_1019: 'Query' = t_8220.where_not(t_8221.accumulated)
            t_8229: 'bool33' = q_1019.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_8214() -> 'str27':
                return 'whereNot chained'
            test_85.assert_(t_8229, fn_8214)
        finally:
            test_85.soft_fail_to_hard()
class TestCase108(TestCase46):
    def test___whereBetweenIntegers__1544(self) -> None:
        'whereBetween integers'
        test_86: Test = Test()
        try:
            t_8204: 'SafeIdentifier' = sid_461('users')
            t_8205: 'SafeIdentifier' = sid_461('age')
            t_8206: 'SqlInt32' = SqlInt32(18)
            t_8207: 'SqlInt32' = SqlInt32(65)
            q_1021: 'Query' = from_(t_8204).where_between(t_8205, t_8206, t_8207)
            t_8212: 'bool33' = q_1021.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_8203() -> 'str27':
                return 'whereBetween ints'
            test_86.assert_(t_8212, fn_8203)
        finally:
            test_86.soft_fail_to_hard()
class TestCase109(TestCase46):
    def test___whereBetweenChained__1545(self) -> None:
        'whereBetween chained'
        test_87: Test = Test()
        try:
            t_8188: 'SafeIdentifier' = sid_461('users')
            t_8189: 'SqlBuilder' = SqlBuilder()
            t_8189.append_safe('active = ')
            t_8189.append_boolean(True)
            t_8192: 'SqlFragment' = t_8189.accumulated
            q_1023: 'Query' = from_(t_8188).where(t_8192).where_between(sid_461('age'), SqlInt32(21), SqlInt32(30))
            t_8201: 'bool33' = q_1023.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_8187() -> 'str27':
                return 'whereBetween chained'
            test_87.assert_(t_8201, fn_8187)
        finally:
            test_87.soft_fail_to_hard()
class TestCase110(TestCase46):
    def test___whereLikeBasic__1547(self) -> None:
        'whereLike basic'
        test_88: Test = Test()
        try:
            t_8179: 'SafeIdentifier' = sid_461('users')
            t_8180: 'SafeIdentifier' = sid_461('name')
            q_1025: 'Query' = from_(t_8179).where_like(t_8180, 'John%')
            t_8185: 'bool33' = q_1025.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_8178() -> 'str27':
                return 'whereLike'
            test_88.assert_(t_8185, fn_8178)
        finally:
            test_88.soft_fail_to_hard()
class TestCase111(TestCase46):
    def test___whereIlikeBasic__1548(self) -> None:
        'whereILike basic'
        test_89: Test = Test()
        try:
            t_8170: 'SafeIdentifier' = sid_461('users')
            t_8171: 'SafeIdentifier' = sid_461('email')
            q_1027: 'Query' = from_(t_8170).where_i_like(t_8171, '%@gmail.com')
            t_8176: 'bool33' = q_1027.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_8169() -> 'str27':
                return 'whereILike'
            test_89.assert_(t_8176, fn_8169)
        finally:
            test_89.soft_fail_to_hard()
class TestCase112(TestCase46):
    def test___whereLikeWithInjectionAttempt__1549(self) -> None:
        'whereLike with injection attempt'
        test_90: Test = Test()
        try:
            t_8156: 'SafeIdentifier' = sid_461('users')
            t_8157: 'SafeIdentifier' = sid_461('name')
            q_1029: 'Query' = from_(t_8156).where_like(t_8157, "'; DROP TABLE users; --")
            s_1030: 'str27' = q_1029.to_sql().to_string()
            t_8162: 'bool33' = s_1030.find("''") >= 0
            def fn_8155() -> 'str27':
                return str_cat_9688('like injection escaped: ', s_1030)
            test_90.assert_(t_8162, fn_8155)
            t_8166: 'bool33' = s_1030.find('LIKE') >= 0
            def fn_8154() -> 'str27':
                return str_cat_9688('like structure intact: ', s_1030)
            test_90.assert_(t_8166, fn_8154)
        finally:
            test_90.soft_fail_to_hard()
class TestCase113(TestCase46):
    def test___whereLikeWildcardPatterns__1550(self) -> None:
        'whereLike wildcard patterns'
        test_91: Test = Test()
        try:
            t_8146: 'SafeIdentifier' = sid_461('users')
            t_8147: 'SafeIdentifier' = sid_461('name')
            q_1032: 'Query' = from_(t_8146).where_like(t_8147, '%son%')
            t_8152: 'bool33' = q_1032.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_8145() -> 'str27':
                return 'whereLike wildcard'
            test_91.assert_(t_8152, fn_8145)
        finally:
            test_91.soft_fail_to_hard()
class TestCase114(TestCase46):
    def test___countAllProducesCount__1551(self) -> None:
        'countAll produces COUNT(*)'
        test_92: Test = Test()
        try:
            f_1034: 'SqlFragment' = count_all()
            t_8143: 'bool33' = f_1034.to_string() == 'COUNT(*)'
            def fn_8139() -> 'str27':
                return 'countAll'
            test_92.assert_(t_8143, fn_8139)
        finally:
            test_92.soft_fail_to_hard()
class TestCase115(TestCase46):
    def test___countColProducesCountField__1552(self) -> None:
        'countCol produces COUNT(field)'
        test_93: Test = Test()
        try:
            f_1036: 'SqlFragment' = count_col(sid_461('id'))
            t_8137: 'bool33' = f_1036.to_string() == 'COUNT(id)'
            def fn_8132() -> 'str27':
                return 'countCol'
            test_93.assert_(t_8137, fn_8132)
        finally:
            test_93.soft_fail_to_hard()
class TestCase116(TestCase46):
    def test___sumColProducesSumField__1553(self) -> None:
        'sumCol produces SUM(field)'
        test_94: Test = Test()
        try:
            f_1038: 'SqlFragment' = sum_col(sid_461('amount'))
            t_8130: 'bool33' = f_1038.to_string() == 'SUM(amount)'
            def fn_8125() -> 'str27':
                return 'sumCol'
            test_94.assert_(t_8130, fn_8125)
        finally:
            test_94.soft_fail_to_hard()
class TestCase117(TestCase46):
    def test___avgColProducesAvgField__1554(self) -> None:
        'avgCol produces AVG(field)'
        test_95: Test = Test()
        try:
            f_1040: 'SqlFragment' = avg_col(sid_461('price'))
            t_8123: 'bool33' = f_1040.to_string() == 'AVG(price)'
            def fn_8118() -> 'str27':
                return 'avgCol'
            test_95.assert_(t_8123, fn_8118)
        finally:
            test_95.soft_fail_to_hard()
class TestCase118(TestCase46):
    def test___minColProducesMinField__1555(self) -> None:
        'minCol produces MIN(field)'
        test_96: Test = Test()
        try:
            f_1042: 'SqlFragment' = min_col(sid_461('created_at'))
            t_8116: 'bool33' = f_1042.to_string() == 'MIN(created_at)'
            def fn_8111() -> 'str27':
                return 'minCol'
            test_96.assert_(t_8116, fn_8111)
        finally:
            test_96.soft_fail_to_hard()
class TestCase119(TestCase46):
    def test___maxColProducesMaxField__1556(self) -> None:
        'maxCol produces MAX(field)'
        test_97: Test = Test()
        try:
            f_1044: 'SqlFragment' = max_col(sid_461('score'))
            t_8109: 'bool33' = f_1044.to_string() == 'MAX(score)'
            def fn_8104() -> 'str27':
                return 'maxCol'
            test_97.assert_(t_8109, fn_8104)
        finally:
            test_97.soft_fail_to_hard()
class TestCase120(TestCase46):
    def test___selectExprWithAggregate__1557(self) -> None:
        'selectExpr with aggregate'
        test_98: Test = Test()
        try:
            t_8096: 'SafeIdentifier' = sid_461('orders')
            t_8097: 'SqlFragment' = count_all()
            q_1046: 'Query' = from_(t_8096).select_expr((t_8097,))
            t_8102: 'bool33' = q_1046.to_sql().to_string() == 'SELECT COUNT(*) FROM orders'
            def fn_8095() -> 'str27':
                return 'selectExpr count'
            test_98.assert_(t_8102, fn_8095)
        finally:
            test_98.soft_fail_to_hard()
class TestCase121(TestCase46):
    def test___selectExprWithMultipleExpressions__1558(self) -> None:
        'selectExpr with multiple expressions'
        test_99: Test = Test()
        try:
            name_frag_1048: 'SqlFragment' = col(sid_461('users'), sid_461('name'))
            t_8087: 'SafeIdentifier' = sid_461('users')
            t_8088: 'SqlFragment' = count_all()
            q_1049: 'Query' = from_(t_8087).select_expr((name_frag_1048, t_8088))
            t_8093: 'bool33' = q_1049.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users'
            def fn_8083() -> 'str27':
                return 'selectExpr multi'
            test_99.assert_(t_8093, fn_8083)
        finally:
            test_99.soft_fail_to_hard()
class TestCase122(TestCase46):
    def test___selectExprOverridesSelectedFields__1559(self) -> None:
        'selectExpr overrides selectedFields'
        test_100: Test = Test()
        try:
            t_8072: 'SafeIdentifier' = sid_461('users')
            t_8073: 'SafeIdentifier' = sid_461('id')
            t_8074: 'SafeIdentifier' = sid_461('name')
            q_1051: 'Query' = from_(t_8072).select((t_8073, t_8074)).select_expr((count_all(),))
            t_8081: 'bool33' = q_1051.to_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_8071() -> 'str27':
                return 'selectExpr overrides select'
            test_100.assert_(t_8081, fn_8071)
        finally:
            test_100.soft_fail_to_hard()
class TestCase123(TestCase46):
    def test___groupBySingleField__1560(self) -> None:
        'groupBy single field'
        test_101: Test = Test()
        try:
            t_8058: 'SafeIdentifier' = sid_461('orders')
            t_8061: 'SqlFragment' = col(sid_461('orders'), sid_461('status'))
            t_8062: 'SqlFragment' = count_all()
            q_1053: 'Query' = from_(t_8058).select_expr((t_8061, t_8062)).group_by(sid_461('status'))
            t_8069: 'bool33' = q_1053.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status'
            def fn_8057() -> 'str27':
                return 'groupBy single'
            test_101.assert_(t_8069, fn_8057)
        finally:
            test_101.soft_fail_to_hard()
class TestCase124(TestCase46):
    def test___groupByMultipleFields__1561(self) -> None:
        'groupBy multiple fields'
        test_102: Test = Test()
        try:
            t_8047: 'SafeIdentifier' = sid_461('orders')
            t_8048: 'SafeIdentifier' = sid_461('status')
            q_1055: 'Query' = from_(t_8047).group_by(t_8048).group_by(sid_461('category'))
            t_8055: 'bool33' = q_1055.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category'
            def fn_8046() -> 'str27':
                return 'groupBy multiple'
            test_102.assert_(t_8055, fn_8046)
        finally:
            test_102.soft_fail_to_hard()
class TestCase125(TestCase46):
    def test___havingBasic__1562(self) -> None:
        'having basic'
        test_103: Test = Test()
        try:
            t_8028: 'SafeIdentifier' = sid_461('orders')
            t_8031: 'SqlFragment' = col(sid_461('orders'), sid_461('status'))
            t_8032: 'SqlFragment' = count_all()
            t_8035: 'Query' = from_(t_8028).select_expr((t_8031, t_8032)).group_by(sid_461('status'))
            t_8036: 'SqlBuilder' = SqlBuilder()
            t_8036.append_safe('COUNT(*) > ')
            t_8036.append_int32(5)
            q_1057: 'Query' = t_8035.having(t_8036.accumulated)
            t_8044: 'bool33' = q_1057.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5'
            def fn_8027() -> 'str27':
                return 'having basic'
            test_103.assert_(t_8044, fn_8027)
        finally:
            test_103.soft_fail_to_hard()
class TestCase126(TestCase46):
    def test___orHaving__1564(self) -> None:
        'orHaving'
        test_104: Test = Test()
        try:
            t_8009: 'SafeIdentifier' = sid_461('orders')
            t_8010: 'SafeIdentifier' = sid_461('status')
            t_8011: 'Query' = from_(t_8009).group_by(t_8010)
            t_8012: 'SqlBuilder' = SqlBuilder()
            t_8012.append_safe('COUNT(*) > ')
            t_8012.append_int32(5)
            t_8016: 'Query' = t_8011.having(t_8012.accumulated)
            t_8017: 'SqlBuilder' = SqlBuilder()
            t_8017.append_safe('SUM(total) > ')
            t_8017.append_int32(1000)
            q_1059: 'Query' = t_8016.or_having(t_8017.accumulated)
            t_8025: 'bool33' = q_1059.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000'
            def fn_8008() -> 'str27':
                return 'orHaving'
            test_104.assert_(t_8025, fn_8008)
        finally:
            test_104.soft_fail_to_hard()
class TestCase127(TestCase46):
    def test___distinctBasic__1567(self) -> None:
        'distinct basic'
        test_105: Test = Test()
        try:
            t_7999: 'SafeIdentifier' = sid_461('users')
            t_8000: 'SafeIdentifier' = sid_461('name')
            q_1061: 'Query' = from_(t_7999).select((t_8000,)).distinct()
            t_8006: 'bool33' = q_1061.to_sql().to_string() == 'SELECT DISTINCT name FROM users'
            def fn_7998() -> 'str27':
                return 'distinct'
            test_105.assert_(t_8006, fn_7998)
        finally:
            test_105.soft_fail_to_hard()
class TestCase128(TestCase46):
    def test___distinctWithWhere__1568(self) -> None:
        'distinct with where'
        test_106: Test = Test()
        try:
            t_7984: 'SafeIdentifier' = sid_461('users')
            t_7985: 'SafeIdentifier' = sid_461('email')
            t_7986: 'Query' = from_(t_7984).select((t_7985,))
            t_7987: 'SqlBuilder' = SqlBuilder()
            t_7987.append_safe('active = ')
            t_7987.append_boolean(True)
            q_1063: 'Query' = t_7986.where(t_7987.accumulated).distinct()
            t_7996: 'bool33' = q_1063.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE'
            def fn_7983() -> 'str27':
                return 'distinct with where'
            test_106.assert_(t_7996, fn_7983)
        finally:
            test_106.soft_fail_to_hard()
class TestCase129(TestCase46):
    def test___countSqlBare__1570(self) -> None:
        'countSql bare'
        test_107: Test = Test()
        try:
            q_1065: 'Query' = from_(sid_461('users'))
            t_7981: 'bool33' = q_1065.count_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_7976() -> 'str27':
                return 'countSql bare'
            test_107.assert_(t_7981, fn_7976)
        finally:
            test_107.soft_fail_to_hard()
class TestCase130(TestCase46):
    def test___countSqlWithWhere__1571(self) -> None:
        'countSql with WHERE'
        test_108: Test = Test()
        try:
            t_7965: 'SafeIdentifier' = sid_461('users')
            t_7966: 'SqlBuilder' = SqlBuilder()
            t_7966.append_safe('active = ')
            t_7966.append_boolean(True)
            t_7969: 'SqlFragment' = t_7966.accumulated
            q_1067: 'Query' = from_(t_7965).where(t_7969)
            t_7974: 'bool33' = q_1067.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_7964() -> 'str27':
                return 'countSql with where'
            test_108.assert_(t_7974, fn_7964)
        finally:
            test_108.soft_fail_to_hard()
class TestCase131(TestCase46):
    def test___countSqlWithJoin__1573(self) -> None:
        'countSql with JOIN'
        test_109: Test = Test()
        try:
            t_7948: 'SafeIdentifier' = sid_461('users')
            t_7949: 'SafeIdentifier' = sid_461('orders')
            t_7950: 'SqlBuilder' = SqlBuilder()
            t_7950.append_safe('users.id = orders.user_id')
            t_7952: 'SqlFragment' = t_7950.accumulated
            t_7953: 'Query' = from_(t_7948).inner_join(t_7949, t_7952)
            t_7954: 'SqlBuilder' = SqlBuilder()
            t_7954.append_safe('orders.total > ')
            t_7954.append_int32(100)
            q_1069: 'Query' = t_7953.where(t_7954.accumulated)
            t_7962: 'bool33' = q_1069.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100'
            def fn_7947() -> 'str27':
                return 'countSql with join'
            test_109.assert_(t_7962, fn_7947)
        finally:
            test_109.soft_fail_to_hard()
class TestCase132(TestCase46):
    def test___countSqlDropsOrderByLimitOffset__1576(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_110: Test = Test()
        try:
            t_7934: 'SafeIdentifier' = sid_461('users')
            t_7935: 'SqlBuilder' = SqlBuilder()
            t_7935.append_safe('active = ')
            t_7935.append_boolean(True)
            t_7938: 'SqlFragment' = t_7935.accumulated
            t_3983: 'Query'
            t_3983 = from_(t_7934).where(t_7938).order_by(sid_461('name'), True).limit(10)
            t_3984: 'Query'
            t_3984 = t_3983.offset(20)
            q_1071: 'Query' = t_3984
            s_1072: 'str27' = q_1071.count_sql().to_string()
            t_7945: 'bool33' = s_1072 == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_7933() -> 'str27':
                return str_cat_9688('countSql drops extras: ', s_1072)
            test_110.assert_(t_7945, fn_7933)
        finally:
            test_110.soft_fail_to_hard()
class TestCase133(TestCase46):
    def test___fullAggregationQuery__1578(self) -> None:
        'full aggregation query'
        test_111: Test = Test()
        try:
            t_7901: 'SafeIdentifier' = sid_461('orders')
            t_7904: 'SqlFragment' = col(sid_461('orders'), sid_461('status'))
            t_7905: 'SqlFragment' = count_all()
            t_7907: 'SqlFragment' = sum_col(sid_461('total'))
            t_7908: 'Query' = from_(t_7901).select_expr((t_7904, t_7905, t_7907))
            t_7909: 'SafeIdentifier' = sid_461('users')
            t_7910: 'SqlBuilder' = SqlBuilder()
            t_7910.append_safe('orders.user_id = users.id')
            t_7913: 'Query' = t_7908.inner_join(t_7909, t_7910.accumulated)
            t_7914: 'SqlBuilder' = SqlBuilder()
            t_7914.append_safe('users.active = ')
            t_7914.append_boolean(True)
            t_7920: 'Query' = t_7913.where(t_7914.accumulated).group_by(sid_461('status'))
            t_7921: 'SqlBuilder' = SqlBuilder()
            t_7921.append_safe('COUNT(*) > ')
            t_7921.append_int32(3)
            q_1074: 'Query' = t_7920.having(t_7921.accumulated).order_by(sid_461('status'), True)
            expected_1075: 'str27' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            t_7931: 'bool33' = q_1074.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_7900() -> 'str27':
                return 'full aggregation'
            test_111.assert_(t_7931, fn_7900)
        finally:
            test_111.soft_fail_to_hard()
class TestCase134(TestCase46):
    def test___unionSql__1582(self) -> None:
        'unionSql'
        test_112: Test = Test()
        try:
            t_7883: 'SafeIdentifier' = sid_461('users')
            t_7884: 'SqlBuilder' = SqlBuilder()
            t_7884.append_safe('role = ')
            t_7884.append_string('admin')
            t_7887: 'SqlFragment' = t_7884.accumulated
            a_1077: 'Query' = from_(t_7883).where(t_7887)
            t_7889: 'SafeIdentifier' = sid_461('users')
            t_7890: 'SqlBuilder' = SqlBuilder()
            t_7890.append_safe('role = ')
            t_7890.append_string('moderator')
            t_7893: 'SqlFragment' = t_7890.accumulated
            b_1078: 'Query' = from_(t_7889).where(t_7893)
            s_1079: 'str27' = union_sql(a_1077, b_1078).to_string()
            t_7898: 'bool33' = s_1079 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')"
            def fn_7882() -> 'str27':
                return str_cat_9688('unionSql: ', s_1079)
            test_112.assert_(t_7898, fn_7882)
        finally:
            test_112.soft_fail_to_hard()
class TestCase135(TestCase46):
    def test___unionAllSql__1585(self) -> None:
        'unionAllSql'
        test_113: Test = Test()
        try:
            t_7871: 'SafeIdentifier' = sid_461('users')
            t_7872: 'SafeIdentifier' = sid_461('name')
            a_1081: 'Query' = from_(t_7871).select((t_7872,))
            t_7874: 'SafeIdentifier' = sid_461('contacts')
            t_7875: 'SafeIdentifier' = sid_461('name')
            b_1082: 'Query' = from_(t_7874).select((t_7875,))
            s_1083: 'str27' = union_all_sql(a_1081, b_1082).to_string()
            t_7880: 'bool33' = s_1083 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)'
            def fn_7870() -> 'str27':
                return str_cat_9688('unionAllSql: ', s_1083)
            test_113.assert_(t_7880, fn_7870)
        finally:
            test_113.soft_fail_to_hard()
class TestCase136(TestCase46):
    def test___intersectSql__1586(self) -> None:
        'intersectSql'
        test_114: Test = Test()
        try:
            t_7859: 'SafeIdentifier' = sid_461('users')
            t_7860: 'SafeIdentifier' = sid_461('email')
            a_1085: 'Query' = from_(t_7859).select((t_7860,))
            t_7862: 'SafeIdentifier' = sid_461('subscribers')
            t_7863: 'SafeIdentifier' = sid_461('email')
            b_1086: 'Query' = from_(t_7862).select((t_7863,))
            s_1087: 'str27' = intersect_sql(a_1085, b_1086).to_string()
            t_7868: 'bool33' = s_1087 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)'
            def fn_7858() -> 'str27':
                return str_cat_9688('intersectSql: ', s_1087)
            test_114.assert_(t_7868, fn_7858)
        finally:
            test_114.soft_fail_to_hard()
class TestCase137(TestCase46):
    def test___exceptSql__1587(self) -> None:
        'exceptSql'
        test_115: Test = Test()
        try:
            t_7847: 'SafeIdentifier' = sid_461('users')
            t_7848: 'SafeIdentifier' = sid_461('id')
            a_1089: 'Query' = from_(t_7847).select((t_7848,))
            t_7850: 'SafeIdentifier' = sid_461('banned')
            t_7851: 'SafeIdentifier' = sid_461('id')
            b_1090: 'Query' = from_(t_7850).select((t_7851,))
            s_1091: 'str27' = except_sql(a_1089, b_1090).to_string()
            t_7856: 'bool33' = s_1091 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)'
            def fn_7846() -> 'str27':
                return str_cat_9688('exceptSql: ', s_1091)
            test_115.assert_(t_7856, fn_7846)
        finally:
            test_115.soft_fail_to_hard()
class TestCase138(TestCase46):
    def test___subqueryWithAlias__1588(self) -> None:
        'subquery with alias'
        test_116: Test = Test()
        try:
            t_7832: 'SafeIdentifier' = sid_461('orders')
            t_7833: 'SafeIdentifier' = sid_461('user_id')
            t_7834: 'Query' = from_(t_7832).select((t_7833,))
            t_7835: 'SqlBuilder' = SqlBuilder()
            t_7835.append_safe('total > ')
            t_7835.append_int32(100)
            inner_1093: 'Query' = t_7834.where(t_7835.accumulated)
            s_1094: 'str27' = subquery(inner_1093, sid_461('big_orders')).to_string()
            t_7844: 'bool33' = s_1094 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders'
            def fn_7831() -> 'str27':
                return str_cat_9688('subquery: ', s_1094)
            test_116.assert_(t_7844, fn_7831)
        finally:
            test_116.soft_fail_to_hard()
class TestCase139(TestCase46):
    def test___existsSql__1590(self) -> None:
        'existsSql'
        test_117: Test = Test()
        try:
            t_7821: 'SafeIdentifier' = sid_461('orders')
            t_7822: 'SqlBuilder' = SqlBuilder()
            t_7822.append_safe('orders.user_id = users.id')
            t_7824: 'SqlFragment' = t_7822.accumulated
            inner_1096: 'Query' = from_(t_7821).where(t_7824)
            s_1097: 'str27' = exists_sql(inner_1096).to_string()
            t_7829: 'bool33' = s_1097 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_7820() -> 'str27':
                return str_cat_9688('existsSql: ', s_1097)
            test_117.assert_(t_7829, fn_7820)
        finally:
            test_117.soft_fail_to_hard()
class TestCase140(TestCase46):
    def test___whereInSubquery__1592(self) -> None:
        'whereInSubquery'
        test_118: Test = Test()
        try:
            t_7804: 'SafeIdentifier' = sid_461('orders')
            t_7805: 'SafeIdentifier' = sid_461('user_id')
            t_7806: 'Query' = from_(t_7804).select((t_7805,))
            t_7807: 'SqlBuilder' = SqlBuilder()
            t_7807.append_safe('total > ')
            t_7807.append_int32(1000)
            sub_1099: 'Query' = t_7806.where(t_7807.accumulated)
            t_7812: 'SafeIdentifier' = sid_461('users')
            t_7813: 'SafeIdentifier' = sid_461('id')
            q_1100: 'Query' = from_(t_7812).where_in_subquery(t_7813, sub_1099)
            s_1101: 'str27' = q_1100.to_sql().to_string()
            t_7818: 'bool33' = s_1101 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)'
            def fn_7803() -> 'str27':
                return str_cat_9688('whereInSubquery: ', s_1101)
            test_118.assert_(t_7818, fn_7803)
        finally:
            test_118.soft_fail_to_hard()
class TestCase141(TestCase46):
    def test___setOperationWithWhereOnEachSide__1594(self) -> None:
        'set operation with WHERE on each side'
        test_119: Test = Test()
        try:
            t_7781: 'SafeIdentifier' = sid_461('users')
            t_7782: 'SqlBuilder' = SqlBuilder()
            t_7782.append_safe('age > ')
            t_7782.append_int32(18)
            t_7785: 'SqlFragment' = t_7782.accumulated
            t_7786: 'Query' = from_(t_7781).where(t_7785)
            t_7787: 'SqlBuilder' = SqlBuilder()
            t_7787.append_safe('active = ')
            t_7787.append_boolean(True)
            a_1103: 'Query' = t_7786.where(t_7787.accumulated)
            t_7792: 'SafeIdentifier' = sid_461('users')
            t_7793: 'SqlBuilder' = SqlBuilder()
            t_7793.append_safe('role = ')
            t_7793.append_string('vip')
            t_7796: 'SqlFragment' = t_7793.accumulated
            b_1104: 'Query' = from_(t_7792).where(t_7796)
            s_1105: 'str27' = union_sql(a_1103, b_1104).to_string()
            t_7801: 'bool33' = s_1105 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')"
            def fn_7780() -> 'str27':
                return str_cat_9688('union with where: ', s_1105)
            test_119.assert_(t_7801, fn_7780)
        finally:
            test_119.soft_fail_to_hard()
class TestCase142(TestCase46):
    def test___whereInSubqueryChainedWithWhere__1598(self) -> None:
        'whereInSubquery chained with where'
        test_120: Test = Test()
        try:
            t_7764: 'SafeIdentifier' = sid_461('orders')
            t_7765: 'SafeIdentifier' = sid_461('user_id')
            sub_1107: 'Query' = from_(t_7764).select((t_7765,))
            t_7767: 'SafeIdentifier' = sid_461('users')
            t_7768: 'SqlBuilder' = SqlBuilder()
            t_7768.append_safe('active = ')
            t_7768.append_boolean(True)
            t_7771: 'SqlFragment' = t_7768.accumulated
            q_1108: 'Query' = from_(t_7767).where(t_7771).where_in_subquery(sid_461('id'), sub_1107)
            s_1109: 'str27' = q_1108.to_sql().to_string()
            t_7778: 'bool33' = s_1109 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)'
            def fn_7763() -> 'str27':
                return str_cat_9688('whereInSubquery chained: ', s_1109)
            test_120.assert_(t_7778, fn_7763)
        finally:
            test_120.soft_fail_to_hard()
class TestCase143(TestCase46):
    def test___existsSqlUsedInWhere__1600(self) -> None:
        'existsSql used in where'
        test_121: Test = Test()
        try:
            t_7750: 'SafeIdentifier' = sid_461('orders')
            t_7751: 'SqlBuilder' = SqlBuilder()
            t_7751.append_safe('orders.user_id = users.id')
            t_7753: 'SqlFragment' = t_7751.accumulated
            sub_1111: 'Query' = from_(t_7750).where(t_7753)
            t_7755: 'SafeIdentifier' = sid_461('users')
            t_7756: 'SqlFragment' = exists_sql(sub_1111)
            q_1112: 'Query' = from_(t_7755).where(t_7756)
            s_1113: 'str27' = q_1112.to_sql().to_string()
            t_7761: 'bool33' = s_1113 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_7749() -> 'str27':
                return str_cat_9688('exists in where: ', s_1113)
            test_121.assert_(t_7761, fn_7749)
        finally:
            test_121.soft_fail_to_hard()
class TestCase144(TestCase46):
    def test___safeIdentifierAcceptsValidNames__1602(self) -> None:
        'safeIdentifier accepts valid names'
        test_128: Test = Test()
        try:
            t_3806: 'SafeIdentifier'
            t_3806 = safe_identifier('user_name')
            id_1151: 'SafeIdentifier' = t_3806
            t_7747: 'bool33' = id_1151.sql_value == 'user_name'
            def fn_7744() -> 'str27':
                return 'value should round-trip'
            test_128.assert_(t_7747, fn_7744)
        finally:
            test_128.soft_fail_to_hard()
class TestCase145(TestCase46):
    def test___safeIdentifierRejectsEmptyString__1603(self) -> None:
        'safeIdentifier rejects empty string'
        test_129: Test = Test()
        try:
            did_bubble_1153: 'bool33'
            try:
                safe_identifier('')
                did_bubble_1153 = False
            except Exception37:
                did_bubble_1153 = True
            def fn_7741() -> 'str27':
                return 'empty string should bubble'
            test_129.assert_(did_bubble_1153, fn_7741)
        finally:
            test_129.soft_fail_to_hard()
class TestCase146(TestCase46):
    def test___safeIdentifierRejectsLeadingDigit__1604(self) -> None:
        'safeIdentifier rejects leading digit'
        test_130: Test = Test()
        try:
            did_bubble_1155: 'bool33'
            try:
                safe_identifier('1col')
                did_bubble_1155 = False
            except Exception37:
                did_bubble_1155 = True
            def fn_7738() -> 'str27':
                return 'leading digit should bubble'
            test_130.assert_(did_bubble_1155, fn_7738)
        finally:
            test_130.soft_fail_to_hard()
class TestCase147(TestCase46):
    def test___safeIdentifierRejectsSqlMetacharacters__1605(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_131: Test = Test()
        try:
            cases_1157: 'Sequence29[str27]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_7735(c_1158: 'str27') -> 'None':
                did_bubble_1159: 'bool33'
                try:
                    safe_identifier(c_1158)
                    did_bubble_1159 = False
                except Exception37:
                    did_bubble_1159 = True
                def fn_7732() -> 'str27':
                    return str_cat_9688('should reject: ', c_1158)
                test_131.assert_(did_bubble_1159, fn_7732)
            list_for_each_9680(cases_1157, fn_7735)
        finally:
            test_131.soft_fail_to_hard()
class TestCase148(TestCase46):
    def test___tableDefFieldLookupFound__1606(self) -> None:
        'TableDef field lookup - found'
        test_132: Test = Test()
        try:
            t_3783: 'SafeIdentifier'
            t_3783 = safe_identifier('users')
            t_3784: 'SafeIdentifier' = t_3783
            t_3785: 'SafeIdentifier'
            t_3785 = safe_identifier('name')
            t_3786: 'SafeIdentifier' = t_3785
            t_7722: 'StringField' = StringField()
            t_7723: 'FieldDef' = FieldDef(t_3786, t_7722, False)
            t_3789: 'SafeIdentifier'
            t_3789 = safe_identifier('age')
            t_3790: 'SafeIdentifier' = t_3789
            t_7724: 'IntField' = IntField()
            t_7725: 'FieldDef' = FieldDef(t_3790, t_7724, False)
            td_1161: 'TableDef' = TableDef(t_3784, (t_7723, t_7725))
            t_3794: 'FieldDef'
            t_3794 = td_1161.field('age')
            f_1162: 'FieldDef' = t_3794
            t_7730: 'bool33' = f_1162.name.sql_value == 'age'
            def fn_7721() -> 'str27':
                return 'should find age field'
            test_132.assert_(t_7730, fn_7721)
        finally:
            test_132.soft_fail_to_hard()
class TestCase149(TestCase46):
    def test___tableDefFieldLookupNotFoundBubbles__1607(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_133: Test = Test()
        try:
            t_3774: 'SafeIdentifier'
            t_3774 = safe_identifier('users')
            t_3775: 'SafeIdentifier' = t_3774
            t_3776: 'SafeIdentifier'
            t_3776 = safe_identifier('name')
            t_3777: 'SafeIdentifier' = t_3776
            t_7716: 'StringField' = StringField()
            t_7717: 'FieldDef' = FieldDef(t_3777, t_7716, False)
            td_1164: 'TableDef' = TableDef(t_3775, (t_7717,))
            did_bubble_1165: 'bool33'
            try:
                td_1164.field('nonexistent')
                did_bubble_1165 = False
            except Exception37:
                did_bubble_1165 = True
            def fn_7715() -> 'str27':
                return 'unknown field should bubble'
            test_133.assert_(did_bubble_1165, fn_7715)
        finally:
            test_133.soft_fail_to_hard()
class TestCase150(TestCase46):
    def test___fieldDefNullableFlag__1608(self) -> None:
        'FieldDef nullable flag'
        test_134: Test = Test()
        try:
            t_3762: 'SafeIdentifier'
            t_3762 = safe_identifier('email')
            t_3763: 'SafeIdentifier' = t_3762
            t_7704: 'StringField' = StringField()
            required_1167: 'FieldDef' = FieldDef(t_3763, t_7704, False)
            t_3766: 'SafeIdentifier'
            t_3766 = safe_identifier('bio')
            t_3767: 'SafeIdentifier' = t_3766
            t_7706: 'StringField' = StringField()
            optional_1168: 'FieldDef' = FieldDef(t_3767, t_7706, True)
            t_7710: 'bool33' = not required_1167.nullable
            def fn_7703() -> 'str27':
                return 'required field should not be nullable'
            test_134.assert_(t_7710, fn_7703)
            t_7712: 'bool33' = optional_1168.nullable
            def fn_7702() -> 'str27':
                return 'optional field should be nullable'
            test_134.assert_(t_7712, fn_7702)
        finally:
            test_134.soft_fail_to_hard()
class TestCase151(TestCase46):
    def test___stringEscaping__1609(self) -> None:
        'string escaping'
        test_138: Test = Test()
        try:
            def build_1294(name_1296: 'str27') -> 'str27':
                t_7684: 'SqlBuilder' = SqlBuilder()
                t_7684.append_safe('select * from hi where name = ')
                t_7684.append_string(name_1296)
                return t_7684.accumulated.to_string()
            def build_wrong_1295(name_1298: 'str27') -> 'str27':
                return str_cat_9688("select * from hi where name = '", name_1298, "'")
            actual_1611: 'str27' = build_1294('world')
            t_7694: 'bool33' = actual_1611 == "select * from hi where name = 'world'"
            def fn_7691() -> 'str27':
                return str_cat_9688('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_1611, ')')
            test_138.assert_(t_7694, fn_7691)
            bobby_tables_1300: 'str27' = "Robert'); drop table hi;--"
            actual_1613: 'str27' = build_1294("Robert'); drop table hi;--")
            t_7698: 'bool33' = actual_1613 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_7690() -> 'str27':
                return str_cat_9688('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_1613, ')')
            test_138.assert_(t_7698, fn_7690)
            def fn_7689() -> 'str27':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_138.assert_(True, fn_7689)
        finally:
            test_138.soft_fail_to_hard()
class TestCase152(TestCase46):
    def test___stringEdgeCases__1617(self) -> None:
        'string edge cases'
        test_139: Test = Test()
        try:
            t_7652: 'SqlBuilder' = SqlBuilder()
            t_7652.append_safe('v = ')
            t_7652.append_string('')
            actual_1618: 'str27' = t_7652.accumulated.to_string()
            t_7658: 'bool33' = actual_1618 == "v = ''"
            def fn_7651() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_1618, ')')
            test_139.assert_(t_7658, fn_7651)
            t_7660: 'SqlBuilder' = SqlBuilder()
            t_7660.append_safe('v = ')
            t_7660.append_string("a''b")
            actual_1621: 'str27' = t_7660.accumulated.to_string()
            t_7666: 'bool33' = actual_1621 == "v = 'a''''b'"
            def fn_7650() -> 'str27':
                return str_cat_9688("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_1621, ')')
            test_139.assert_(t_7666, fn_7650)
            t_7668: 'SqlBuilder' = SqlBuilder()
            t_7668.append_safe('v = ')
            t_7668.append_string('Hello \u4e16\u754c')
            actual_1624: 'str27' = t_7668.accumulated.to_string()
            t_7674: 'bool33' = actual_1624 == "v = 'Hello \u4e16\u754c'"
            def fn_7649() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_1624, ')')
            test_139.assert_(t_7674, fn_7649)
            t_7676: 'SqlBuilder' = SqlBuilder()
            t_7676.append_safe('v = ')
            t_7676.append_string('Line1\nLine2')
            actual_1627: 'str27' = t_7676.accumulated.to_string()
            t_7682: 'bool33' = actual_1627 == "v = 'Line1\nLine2'"
            def fn_7648() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_1627, ')')
            test_139.assert_(t_7682, fn_7648)
        finally:
            test_139.soft_fail_to_hard()
class TestCase153(TestCase46):
    def test___numbersAndBooleans__1630(self) -> None:
        'numbers and booleans'
        test_140: Test = Test()
        try:
            t_7623: 'SqlBuilder' = SqlBuilder()
            t_7623.append_safe('select ')
            t_7623.append_int32(42)
            t_7623.append_safe(', ')
            t_7623.append_int64(43)
            t_7623.append_safe(', ')
            t_7623.append_float64(19.99)
            t_7623.append_safe(', ')
            t_7623.append_boolean(True)
            t_7623.append_safe(', ')
            t_7623.append_boolean(False)
            actual_1631: 'str27' = t_7623.accumulated.to_string()
            t_7637: 'bool33' = actual_1631 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_7622() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_1631, ')')
            test_140.assert_(t_7637, fn_7622)
            t_3707: 'date26'
            t_3707 = date_9713(2024, 12, 25)
            date_1303: 'date26' = t_3707
            t_7639: 'SqlBuilder' = SqlBuilder()
            t_7639.append_safe('insert into t values (')
            t_7639.append_date(date_1303)
            t_7639.append_safe(')')
            actual_1634: 'str27' = t_7639.accumulated.to_string()
            t_7646: 'bool33' = actual_1634 == "insert into t values ('2024-12-25')"
            def fn_7621() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_1634, ')')
            test_140.assert_(t_7646, fn_7621)
        finally:
            test_140.soft_fail_to_hard()
class TestCase154(TestCase46):
    def test___lists__1637(self) -> None:
        'lists'
        test_141: Test = Test()
        try:
            t_7567: 'SqlBuilder' = SqlBuilder()
            t_7567.append_safe('v IN (')
            t_7567.append_string_list(('a', 'b', "c'd"))
            t_7567.append_safe(')')
            actual_1638: 'str27' = t_7567.accumulated.to_string()
            t_7574: 'bool33' = actual_1638 == "v IN ('a', 'b', 'c''d')"
            def fn_7566() -> 'str27':
                return str_cat_9688("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_1638, ')')
            test_141.assert_(t_7574, fn_7566)
            t_7576: 'SqlBuilder' = SqlBuilder()
            t_7576.append_safe('v IN (')
            t_7576.append_int32_list((1, 2, 3))
            t_7576.append_safe(')')
            actual_1641: 'str27' = t_7576.accumulated.to_string()
            t_7583: 'bool33' = actual_1641 == 'v IN (1, 2, 3)'
            def fn_7565() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_1641, ')')
            test_141.assert_(t_7583, fn_7565)
            t_7585: 'SqlBuilder' = SqlBuilder()
            t_7585.append_safe('v IN (')
            t_7585.append_int64_list((1, 2))
            t_7585.append_safe(')')
            actual_1644: 'str27' = t_7585.accumulated.to_string()
            t_7592: 'bool33' = actual_1644 == 'v IN (1, 2)'
            def fn_7564() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_1644, ')')
            test_141.assert_(t_7592, fn_7564)
            t_7594: 'SqlBuilder' = SqlBuilder()
            t_7594.append_safe('v IN (')
            t_7594.append_float64_list((1.0, 2.0))
            t_7594.append_safe(')')
            actual_1647: 'str27' = t_7594.accumulated.to_string()
            t_7601: 'bool33' = actual_1647 == 'v IN (1.0, 2.0)'
            def fn_7563() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_1647, ')')
            test_141.assert_(t_7601, fn_7563)
            t_7603: 'SqlBuilder' = SqlBuilder()
            t_7603.append_safe('v IN (')
            t_7603.append_boolean_list((True, False))
            t_7603.append_safe(')')
            actual_1650: 'str27' = t_7603.accumulated.to_string()
            t_7610: 'bool33' = actual_1650 == 'v IN (TRUE, FALSE)'
            def fn_7562() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_1650, ')')
            test_141.assert_(t_7610, fn_7562)
            t_3679: 'date26'
            t_3679 = date_9713(2024, 1, 1)
            t_3680: 'date26' = t_3679
            t_3681: 'date26'
            t_3681 = date_9713(2024, 12, 25)
            t_3682: 'date26' = t_3681
            dates_1305: 'Sequence29[date26]' = (t_3680, t_3682)
            t_7612: 'SqlBuilder' = SqlBuilder()
            t_7612.append_safe('v IN (')
            t_7612.append_date_list(dates_1305)
            t_7612.append_safe(')')
            actual_1653: 'str27' = t_7612.accumulated.to_string()
            t_7619: 'bool33' = actual_1653 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_7561() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_1653, ')')
            test_141.assert_(t_7619, fn_7561)
        finally:
            test_141.soft_fail_to_hard()
class TestCase155(TestCase46):
    def test___sqlFloat64_naNRendersAsNull__1656(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_142: Test = Test()
        try:
            nan_1307: 'float38'
            nan_1307 = 0.0 / 0.0
            t_7553: 'SqlBuilder' = SqlBuilder()
            t_7553.append_safe('v = ')
            t_7553.append_float64(nan_1307)
            actual_1657: 'str27' = t_7553.accumulated.to_string()
            t_7559: 'bool33' = actual_1657 == 'v = NULL'
            def fn_7552() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_1657, ')')
            test_142.assert_(t_7559, fn_7552)
        finally:
            test_142.soft_fail_to_hard()
class TestCase156(TestCase46):
    def test___sqlFloat64_infinityRendersAsNull__1660(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_143: Test = Test()
        try:
            inf_1309: 'float38'
            inf_1309 = 1.0 / 0.0
            t_7544: 'SqlBuilder' = SqlBuilder()
            t_7544.append_safe('v = ')
            t_7544.append_float64(inf_1309)
            actual_1661: 'str27' = t_7544.accumulated.to_string()
            t_7550: 'bool33' = actual_1661 == 'v = NULL'
            def fn_7543() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_1661, ')')
            test_143.assert_(t_7550, fn_7543)
        finally:
            test_143.soft_fail_to_hard()
class TestCase157(TestCase46):
    def test___sqlFloat64_negativeInfinityRendersAsNull__1664(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_144: Test = Test()
        try:
            ninf_1311: 'float38'
            ninf_1311 = -1.0 / 0.0
            t_7535: 'SqlBuilder' = SqlBuilder()
            t_7535.append_safe('v = ')
            t_7535.append_float64(ninf_1311)
            actual_1665: 'str27' = t_7535.accumulated.to_string()
            t_7541: 'bool33' = actual_1665 == 'v = NULL'
            def fn_7534() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_1665, ')')
            test_144.assert_(t_7541, fn_7534)
        finally:
            test_144.soft_fail_to_hard()
class TestCase158(TestCase46):
    def test___sqlFloat64_normalValuesStillWork__1668(self) -> None:
        'SqlFloat64 normal values still work'
        test_145: Test = Test()
        try:
            t_7510: 'SqlBuilder' = SqlBuilder()
            t_7510.append_safe('v = ')
            t_7510.append_float64(3.14)
            actual_1669: 'str27' = t_7510.accumulated.to_string()
            t_7516: 'bool33' = actual_1669 == 'v = 3.14'
            def fn_7509() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_1669, ')')
            test_145.assert_(t_7516, fn_7509)
            t_7518: 'SqlBuilder' = SqlBuilder()
            t_7518.append_safe('v = ')
            t_7518.append_float64(0.0)
            actual_1672: 'str27' = t_7518.accumulated.to_string()
            t_7524: 'bool33' = actual_1672 == 'v = 0.0'
            def fn_7508() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_1672, ')')
            test_145.assert_(t_7524, fn_7508)
            t_7526: 'SqlBuilder' = SqlBuilder()
            t_7526.append_safe('v = ')
            t_7526.append_float64(-42.5)
            actual_1675: 'str27' = t_7526.accumulated.to_string()
            t_7532: 'bool33' = actual_1675 == 'v = -42.5'
            def fn_7507() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_1675, ')')
            test_145.assert_(t_7532, fn_7507)
        finally:
            test_145.soft_fail_to_hard()
class TestCase159(TestCase46):
    def test___sqlDateRendersWithQuotes__1678(self) -> None:
        'SqlDate renders with quotes'
        test_146: Test = Test()
        try:
            t_3575: 'date26'
            t_3575 = date_9713(2024, 6, 15)
            d_1314: 'date26' = t_3575
            t_7499: 'SqlBuilder' = SqlBuilder()
            t_7499.append_safe('v = ')
            t_7499.append_date(d_1314)
            actual_1679: 'str27' = t_7499.accumulated.to_string()
            t_7505: 'bool33' = actual_1679 == "v = '2024-06-15'"
            def fn_7498() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_1679, ')')
            test_146.assert_(t_7505, fn_7498)
        finally:
            test_146.soft_fail_to_hard()
class TestCase160(TestCase46):
    def test___nesting__1682(self) -> None:
        'nesting'
        test_147: Test = Test()
        try:
            name_1316: 'str27' = 'Someone'
            t_7467: 'SqlBuilder' = SqlBuilder()
            t_7467.append_safe('where p.last_name = ')
            t_7467.append_string('Someone')
            condition_1317: 'SqlFragment' = t_7467.accumulated
            t_7471: 'SqlBuilder' = SqlBuilder()
            t_7471.append_safe('select p.id from person p ')
            t_7471.append_fragment(condition_1317)
            actual_1684: 'str27' = t_7471.accumulated.to_string()
            t_7477: 'bool33' = actual_1684 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_7466() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1684, ')')
            test_147.assert_(t_7477, fn_7466)
            t_7479: 'SqlBuilder' = SqlBuilder()
            t_7479.append_safe('select p.id from person p ')
            t_7479.append_part(condition_1317.to_source())
            actual_1687: 'str27' = t_7479.accumulated.to_string()
            t_7486: 'bool33' = actual_1687 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_7465() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1687, ')')
            test_147.assert_(t_7486, fn_7465)
            parts_1318: 'Sequence29[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_7490: 'SqlBuilder' = SqlBuilder()
            t_7490.append_safe('select ')
            t_7490.append_part_list(parts_1318)
            actual_1690: 'str27' = t_7490.accumulated.to_string()
            t_7496: 'bool33' = actual_1690 == "select 'a''b', 3"
            def fn_7464() -> 'str27':
                return str_cat_9688('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_1690, ')')
            test_147.assert_(t_7496, fn_7464)
        finally:
            test_147.soft_fail_to_hard()
