from temper_std.testing import Test
from builtins import str as str27, bool as bool33, Exception as Exception37, int as int31, float as float38
from unittest import TestCase as TestCase46
from types import MappingProxyType as MappingProxyType32
from typing import Sequence as Sequence29
from datetime import date as date26
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_8832, pair_8836, changeset, Changeset, mapped_has_8809, len_8812, list_get_8820, str_cat_8814, list_for_each_8806, SqlFragment, from_, Query, SqlBuilder, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, date_8839, SqlPart
def csid_441(name_586: 'str27') -> 'SafeIdentifier':
    t_4812: 'SafeIdentifier'
    t_4812 = safe_identifier(name_586)
    return t_4812
def user_table_442() -> 'TableDef':
    return TableDef(csid_441('users'), (FieldDef(csid_441('name'), StringField(), False), FieldDef(csid_441('email'), StringField(), False), FieldDef(csid_441('age'), IntField(), True), FieldDef(csid_441('score'), FloatField(), True), FieldDef(csid_441('active'), BoolField(), True)))
class TestCase45(TestCase46):
    def test___castWhitelistsAllowedFields__1320(self) -> None:
        'cast whitelists allowed fields'
        test_24: Test = Test()
        try:
            params_590: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'Alice'), pair_8836('email', 'alice@example.com'), pair_8836('admin', 'true')))
            t_8523: 'TableDef' = user_table_442()
            t_8524: 'SafeIdentifier' = csid_441('name')
            t_8525: 'SafeIdentifier' = csid_441('email')
            cs_591: 'Changeset' = changeset(t_8523, params_590).cast((t_8524, t_8525))
            t_8528: 'bool33' = mapped_has_8809(cs_591.changes, 'name')
            def fn_8518() -> 'str27':
                return 'name should be in changes'
            test_24.assert_(t_8528, fn_8518)
            t_8532: 'bool33' = mapped_has_8809(cs_591.changes, 'email')
            def fn_8517() -> 'str27':
                return 'email should be in changes'
            test_24.assert_(t_8532, fn_8517)
            t_8538: 'bool33' = not mapped_has_8809(cs_591.changes, 'admin')
            def fn_8516() -> 'str27':
                return 'admin must be dropped (not in whitelist)'
            test_24.assert_(t_8538, fn_8516)
            t_8540: 'bool33' = cs_591.is_valid
            def fn_8515() -> 'str27':
                return 'should still be valid'
            test_24.assert_(t_8540, fn_8515)
        finally:
            test_24.soft_fail_to_hard()
class TestCase47(TestCase46):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__1321(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_25: Test = Test()
        try:
            params_593: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'Alice'), pair_8836('email', 'alice@example.com')))
            t_8501: 'TableDef' = user_table_442()
            t_8502: 'SafeIdentifier' = csid_441('name')
            cs_594: 'Changeset' = changeset(t_8501, params_593).cast((t_8502,)).cast((csid_441('email'),))
            t_8509: 'bool33' = not mapped_has_8809(cs_594.changes, 'name')
            def fn_8497() -> 'str27':
                return 'name must be excluded by second cast'
            test_25.assert_(t_8509, fn_8497)
            t_8512: 'bool33' = mapped_has_8809(cs_594.changes, 'email')
            def fn_8496() -> 'str27':
                return 'email should be present'
            test_25.assert_(t_8512, fn_8496)
        finally:
            test_25.soft_fail_to_hard()
class TestCase48(TestCase46):
    def test___castIgnoresEmptyStringValues__1322(self) -> None:
        'cast ignores empty string values'
        test_26: Test = Test()
        try:
            params_596: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', ''), pair_8836('email', 'bob@example.com')))
            t_8483: 'TableDef' = user_table_442()
            t_8484: 'SafeIdentifier' = csid_441('name')
            t_8485: 'SafeIdentifier' = csid_441('email')
            cs_597: 'Changeset' = changeset(t_8483, params_596).cast((t_8484, t_8485))
            t_8490: 'bool33' = not mapped_has_8809(cs_597.changes, 'name')
            def fn_8479() -> 'str27':
                return 'empty name should not be in changes'
            test_26.assert_(t_8490, fn_8479)
            t_8493: 'bool33' = mapped_has_8809(cs_597.changes, 'email')
            def fn_8478() -> 'str27':
                return 'email should be in changes'
            test_26.assert_(t_8493, fn_8478)
        finally:
            test_26.soft_fail_to_hard()
class TestCase49(TestCase46):
    def test___validateRequiredPassesWhenFieldPresent__1323(self) -> None:
        'validateRequired passes when field present'
        test_27: Test = Test()
        try:
            params_599: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'Alice'),))
            t_8465: 'TableDef' = user_table_442()
            t_8466: 'SafeIdentifier' = csid_441('name')
            cs_600: 'Changeset' = changeset(t_8465, params_599).cast((t_8466,)).validate_required((csid_441('name'),))
            t_8470: 'bool33' = cs_600.is_valid
            def fn_8462() -> 'str27':
                return 'should be valid'
            test_27.assert_(t_8470, fn_8462)
            t_8476: 'bool33' = len_8812(cs_600.errors) == 0
            def fn_8461() -> 'str27':
                return 'no errors expected'
            test_27.assert_(t_8476, fn_8461)
        finally:
            test_27.soft_fail_to_hard()
class TestCase50(TestCase46):
    def test___validateRequiredFailsWhenFieldMissing__1324(self) -> None:
        'validateRequired fails when field missing'
        test_28: Test = Test()
        try:
            params_602: 'MappingProxyType32[str27, str27]' = map_constructor_8832(())
            t_8441: 'TableDef' = user_table_442()
            t_8442: 'SafeIdentifier' = csid_441('name')
            cs_603: 'Changeset' = changeset(t_8441, params_602).cast((t_8442,)).validate_required((csid_441('name'),))
            t_8448: 'bool33' = not cs_603.is_valid
            def fn_8439() -> 'str27':
                return 'should be invalid'
            test_28.assert_(t_8448, fn_8439)
            t_8453: 'bool33' = len_8812(cs_603.errors) == 1
            def fn_8438() -> 'str27':
                return 'should have one error'
            test_28.assert_(t_8453, fn_8438)
            t_8459: 'bool33' = list_get_8820(cs_603.errors, 0).field == 'name'
            def fn_8437() -> 'str27':
                return 'error should name the field'
            test_28.assert_(t_8459, fn_8437)
        finally:
            test_28.soft_fail_to_hard()
class TestCase51(TestCase46):
    def test___validateLengthPassesWithinRange__1325(self) -> None:
        'validateLength passes within range'
        test_29: Test = Test()
        try:
            params_605: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'Alice'),))
            t_8429: 'TableDef' = user_table_442()
            t_8430: 'SafeIdentifier' = csid_441('name')
            cs_606: 'Changeset' = changeset(t_8429, params_605).cast((t_8430,)).validate_length(csid_441('name'), 2, 50)
            t_8434: 'bool33' = cs_606.is_valid
            def fn_8426() -> 'str27':
                return 'should be valid'
            test_29.assert_(t_8434, fn_8426)
        finally:
            test_29.soft_fail_to_hard()
class TestCase52(TestCase46):
    def test___validateLengthFailsWhenTooShort__1326(self) -> None:
        'validateLength fails when too short'
        test_30: Test = Test()
        try:
            params_608: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'A'),))
            t_8417: 'TableDef' = user_table_442()
            t_8418: 'SafeIdentifier' = csid_441('name')
            cs_609: 'Changeset' = changeset(t_8417, params_608).cast((t_8418,)).validate_length(csid_441('name'), 2, 50)
            t_8424: 'bool33' = not cs_609.is_valid
            def fn_8414() -> 'str27':
                return 'should be invalid'
            test_30.assert_(t_8424, fn_8414)
        finally:
            test_30.soft_fail_to_hard()
class TestCase53(TestCase46):
    def test___validateLengthFailsWhenTooLong__1327(self) -> None:
        'validateLength fails when too long'
        test_31: Test = Test()
        try:
            params_611: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_8405: 'TableDef' = user_table_442()
            t_8406: 'SafeIdentifier' = csid_441('name')
            cs_612: 'Changeset' = changeset(t_8405, params_611).cast((t_8406,)).validate_length(csid_441('name'), 2, 10)
            t_8412: 'bool33' = not cs_612.is_valid
            def fn_8402() -> 'str27':
                return 'should be invalid'
            test_31.assert_(t_8412, fn_8402)
        finally:
            test_31.soft_fail_to_hard()
class TestCase54(TestCase46):
    def test___validateIntPassesForValidInteger__1328(self) -> None:
        'validateInt passes for valid integer'
        test_32: Test = Test()
        try:
            params_614: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('age', '30'),))
            t_8394: 'TableDef' = user_table_442()
            t_8395: 'SafeIdentifier' = csid_441('age')
            cs_615: 'Changeset' = changeset(t_8394, params_614).cast((t_8395,)).validate_int(csid_441('age'))
            t_8399: 'bool33' = cs_615.is_valid
            def fn_8391() -> 'str27':
                return 'should be valid'
            test_32.assert_(t_8399, fn_8391)
        finally:
            test_32.soft_fail_to_hard()
class TestCase55(TestCase46):
    def test___validateIntFailsForNonInteger__1329(self) -> None:
        'validateInt fails for non-integer'
        test_33: Test = Test()
        try:
            params_617: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('age', 'not-a-number'),))
            t_8382: 'TableDef' = user_table_442()
            t_8383: 'SafeIdentifier' = csid_441('age')
            cs_618: 'Changeset' = changeset(t_8382, params_617).cast((t_8383,)).validate_int(csid_441('age'))
            t_8389: 'bool33' = not cs_618.is_valid
            def fn_8379() -> 'str27':
                return 'should be invalid'
            test_33.assert_(t_8389, fn_8379)
        finally:
            test_33.soft_fail_to_hard()
class TestCase56(TestCase46):
    def test___validateFloatPassesForValidFloat__1330(self) -> None:
        'validateFloat passes for valid float'
        test_34: Test = Test()
        try:
            params_620: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('score', '9.5'),))
            t_8371: 'TableDef' = user_table_442()
            t_8372: 'SafeIdentifier' = csid_441('score')
            cs_621: 'Changeset' = changeset(t_8371, params_620).cast((t_8372,)).validate_float(csid_441('score'))
            t_8376: 'bool33' = cs_621.is_valid
            def fn_8368() -> 'str27':
                return 'should be valid'
            test_34.assert_(t_8376, fn_8368)
        finally:
            test_34.soft_fail_to_hard()
class TestCase57(TestCase46):
    def test___validateInt64_passesForValid64_bitInteger__1331(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_35: Test = Test()
        try:
            params_623: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('age', '9999999999'),))
            t_8360: 'TableDef' = user_table_442()
            t_8361: 'SafeIdentifier' = csid_441('age')
            cs_624: 'Changeset' = changeset(t_8360, params_623).cast((t_8361,)).validate_int64(csid_441('age'))
            t_8365: 'bool33' = cs_624.is_valid
            def fn_8357() -> 'str27':
                return 'should be valid'
            test_35.assert_(t_8365, fn_8357)
        finally:
            test_35.soft_fail_to_hard()
class TestCase58(TestCase46):
    def test___validateInt64_failsForNonInteger__1332(self) -> None:
        'validateInt64 fails for non-integer'
        test_36: Test = Test()
        try:
            params_626: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('age', 'not-a-number'),))
            t_8348: 'TableDef' = user_table_442()
            t_8349: 'SafeIdentifier' = csid_441('age')
            cs_627: 'Changeset' = changeset(t_8348, params_626).cast((t_8349,)).validate_int64(csid_441('age'))
            t_8355: 'bool33' = not cs_627.is_valid
            def fn_8345() -> 'str27':
                return 'should be invalid'
            test_36.assert_(t_8355, fn_8345)
        finally:
            test_36.soft_fail_to_hard()
class TestCase59(TestCase46):
    def test___validateBoolAcceptsTrue1_yesOn__1333(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_37: Test = Test()
        try:
            def fn_8342(v_629: 'str27') -> 'None':
                params_630: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('active', v_629),))
                t_8334: 'TableDef' = user_table_442()
                t_8335: 'SafeIdentifier' = csid_441('active')
                cs_631: 'Changeset' = changeset(t_8334, params_630).cast((t_8335,)).validate_bool(csid_441('active'))
                t_8339: 'bool33' = cs_631.is_valid
                def fn_8331() -> 'str27':
                    return str_cat_8814('should accept: ', v_629)
                test_37.assert_(t_8339, fn_8331)
            list_for_each_8806(('true', '1', 'yes', 'on'), fn_8342)
        finally:
            test_37.soft_fail_to_hard()
class TestCase60(TestCase46):
    def test___validateBoolAcceptsFalse0_noOff__1334(self) -> None:
        'validateBool accepts false/0/no/off'
        test_38: Test = Test()
        try:
            def fn_8328(v_633: 'str27') -> 'None':
                params_634: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('active', v_633),))
                t_8320: 'TableDef' = user_table_442()
                t_8321: 'SafeIdentifier' = csid_441('active')
                cs_635: 'Changeset' = changeset(t_8320, params_634).cast((t_8321,)).validate_bool(csid_441('active'))
                t_8325: 'bool33' = cs_635.is_valid
                def fn_8317() -> 'str27':
                    return str_cat_8814('should accept: ', v_633)
                test_38.assert_(t_8325, fn_8317)
            list_for_each_8806(('false', '0', 'no', 'off'), fn_8328)
        finally:
            test_38.soft_fail_to_hard()
class TestCase61(TestCase46):
    def test___validateBoolRejectsAmbiguousValues__1335(self) -> None:
        'validateBool rejects ambiguous values'
        test_39: Test = Test()
        try:
            def fn_8314(v_637: 'str27') -> 'None':
                params_638: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('active', v_637),))
                t_8305: 'TableDef' = user_table_442()
                t_8306: 'SafeIdentifier' = csid_441('active')
                cs_639: 'Changeset' = changeset(t_8305, params_638).cast((t_8306,)).validate_bool(csid_441('active'))
                t_8312: 'bool33' = not cs_639.is_valid
                def fn_8302() -> 'str27':
                    return str_cat_8814('should reject ambiguous: ', v_637)
                test_39.assert_(t_8312, fn_8302)
            list_for_each_8806(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_8314)
        finally:
            test_39.soft_fail_to_hard()
class TestCase62(TestCase46):
    def test___toInsertSqlEscapesBobbyTables__1336(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_40: Test = Test()
        try:
            params_641: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', "Robert'); DROP TABLE users;--"), pair_8836('email', 'bobby@evil.com')))
            t_8290: 'TableDef' = user_table_442()
            t_8291: 'SafeIdentifier' = csid_441('name')
            t_8292: 'SafeIdentifier' = csid_441('email')
            cs_642: 'Changeset' = changeset(t_8290, params_641).cast((t_8291, t_8292)).validate_required((csid_441('name'), csid_441('email')))
            t_4613: 'SqlFragment'
            t_4613 = cs_642.to_insert_sql()
            sql_frag_643: 'SqlFragment' = t_4613
            s_644: 'str27' = sql_frag_643.to_string()
            t_8299: 'bool33' = s_644.find("''") >= 0
            def fn_8286() -> 'str27':
                return str_cat_8814('single quote must be doubled: ', s_644)
            test_40.assert_(t_8299, fn_8286)
        finally:
            test_40.soft_fail_to_hard()
class TestCase63(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForStringField__1337(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_41: Test = Test()
        try:
            params_646: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'Alice'), pair_8836('email', 'a@example.com')))
            t_8270: 'TableDef' = user_table_442()
            t_8271: 'SafeIdentifier' = csid_441('name')
            t_8272: 'SafeIdentifier' = csid_441('email')
            cs_647: 'Changeset' = changeset(t_8270, params_646).cast((t_8271, t_8272)).validate_required((csid_441('name'), csid_441('email')))
            t_4592: 'SqlFragment'
            t_4592 = cs_647.to_insert_sql()
            sql_frag_648: 'SqlFragment' = t_4592
            s_649: 'str27' = sql_frag_648.to_string()
            t_8279: 'bool33' = s_649.find('INSERT INTO users') >= 0
            def fn_8266() -> 'str27':
                return str_cat_8814('has INSERT INTO: ', s_649)
            test_41.assert_(t_8279, fn_8266)
            t_8283: 'bool33' = s_649.find("'Alice'") >= 0
            def fn_8265() -> 'str27':
                return str_cat_8814('has quoted name: ', s_649)
            test_41.assert_(t_8283, fn_8265)
        finally:
            test_41.soft_fail_to_hard()
class TestCase64(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForIntField__1338(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_42: Test = Test()
        try:
            params_651: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'Bob'), pair_8836('email', 'b@example.com'), pair_8836('age', '25')))
            t_8252: 'TableDef' = user_table_442()
            t_8253: 'SafeIdentifier' = csid_441('name')
            t_8254: 'SafeIdentifier' = csid_441('email')
            t_8255: 'SafeIdentifier' = csid_441('age')
            cs_652: 'Changeset' = changeset(t_8252, params_651).cast((t_8253, t_8254, t_8255)).validate_required((csid_441('name'), csid_441('email')))
            t_4575: 'SqlFragment'
            t_4575 = cs_652.to_insert_sql()
            sql_frag_653: 'SqlFragment' = t_4575
            s_654: 'str27' = sql_frag_653.to_string()
            t_8262: 'bool33' = s_654.find('25') >= 0
            def fn_8247() -> 'str27':
                return str_cat_8814('age rendered unquoted: ', s_654)
            test_42.assert_(t_8262, fn_8247)
        finally:
            test_42.soft_fail_to_hard()
class TestCase65(TestCase46):
    def test___toInsertSqlBubblesOnInvalidChangeset__1339(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_43: Test = Test()
        try:
            params_656: 'MappingProxyType32[str27, str27]' = map_constructor_8832(())
            t_8240: 'TableDef' = user_table_442()
            t_8241: 'SafeIdentifier' = csid_441('name')
            cs_657: 'Changeset' = changeset(t_8240, params_656).cast((t_8241,)).validate_required((csid_441('name'),))
            did_bubble_658: 'bool33'
            try:
                cs_657.to_insert_sql()
                did_bubble_658 = False
            except Exception37:
                did_bubble_658 = True
            def fn_8238() -> 'str27':
                return 'invalid changeset should bubble'
            test_43.assert_(did_bubble_658, fn_8238)
        finally:
            test_43.soft_fail_to_hard()
class TestCase66(TestCase46):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__1340(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_44: Test = Test()
        try:
            strict_table_660: 'TableDef' = TableDef(csid_441('posts'), (FieldDef(csid_441('title'), StringField(), False), FieldDef(csid_441('body'), StringField(), True)))
            params_661: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('body', 'hello'),))
            t_8231: 'SafeIdentifier' = csid_441('body')
            cs_662: 'Changeset' = changeset(strict_table_660, params_661).cast((t_8231,))
            t_8233: 'bool33' = cs_662.is_valid
            def fn_8220() -> 'str27':
                return 'changeset should appear valid (no explicit validation run)'
            test_44.assert_(t_8233, fn_8220)
            did_bubble_663: 'bool33'
            try:
                cs_662.to_insert_sql()
                did_bubble_663 = False
            except Exception37:
                did_bubble_663 = True
            def fn_8219() -> 'str27':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_44.assert_(did_bubble_663, fn_8219)
        finally:
            test_44.soft_fail_to_hard()
class TestCase67(TestCase46):
    def test___toUpdateSqlProducesCorrectSql__1341(self) -> None:
        'toUpdateSql produces correct SQL'
        test_45: Test = Test()
        try:
            params_665: 'MappingProxyType32[str27, str27]' = map_constructor_8832((pair_8836('name', 'Bob'),))
            t_8210: 'TableDef' = user_table_442()
            t_8211: 'SafeIdentifier' = csid_441('name')
            cs_666: 'Changeset' = changeset(t_8210, params_665).cast((t_8211,)).validate_required((csid_441('name'),))
            t_4535: 'SqlFragment'
            t_4535 = cs_666.to_update_sql(42)
            sql_frag_667: 'SqlFragment' = t_4535
            s_668: 'str27' = sql_frag_667.to_string()
            t_8217: 'bool33' = s_668 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_8207() -> 'str27':
                return str_cat_8814('got: ', s_668)
            test_45.assert_(t_8217, fn_8207)
        finally:
            test_45.soft_fail_to_hard()
class TestCase68(TestCase46):
    def test___toUpdateSqlBubblesOnInvalidChangeset__1342(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_46: Test = Test()
        try:
            params_670: 'MappingProxyType32[str27, str27]' = map_constructor_8832(())
            t_8200: 'TableDef' = user_table_442()
            t_8201: 'SafeIdentifier' = csid_441('name')
            cs_671: 'Changeset' = changeset(t_8200, params_670).cast((t_8201,)).validate_required((csid_441('name'),))
            did_bubble_672: 'bool33'
            try:
                cs_671.to_update_sql(1)
                did_bubble_672 = False
            except Exception37:
                did_bubble_672 = True
            def fn_8198() -> 'str27':
                return 'invalid changeset should bubble'
            test_46.assert_(did_bubble_672, fn_8198)
        finally:
            test_46.soft_fail_to_hard()
def sid_443(name_886: 'str27') -> 'SafeIdentifier':
    t_4188: 'SafeIdentifier'
    t_4188 = safe_identifier(name_886)
    return t_4188
class TestCase69(TestCase46):
    def test___bareFromProducesSelect__1391(self) -> None:
        'bare from produces SELECT *'
        test_47: Test = Test()
        try:
            q_889: 'Query' = from_(sid_443('users'))
            t_7866: 'bool33' = q_889.to_sql().to_string() == 'SELECT * FROM users'
            def fn_7861() -> 'str27':
                return 'bare query'
            test_47.assert_(t_7866, fn_7861)
        finally:
            test_47.soft_fail_to_hard()
class TestCase70(TestCase46):
    def test___selectRestrictsColumns__1392(self) -> None:
        'select restricts columns'
        test_48: Test = Test()
        try:
            t_7852: 'SafeIdentifier' = sid_443('users')
            t_7853: 'SafeIdentifier' = sid_443('id')
            t_7854: 'SafeIdentifier' = sid_443('name')
            q_891: 'Query' = from_(t_7852).select((t_7853, t_7854))
            t_7859: 'bool33' = q_891.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_7851() -> 'str27':
                return 'select columns'
            test_48.assert_(t_7859, fn_7851)
        finally:
            test_48.soft_fail_to_hard()
class TestCase71(TestCase46):
    def test___whereAddsConditionWithIntValue__1393(self) -> None:
        'where adds condition with int value'
        test_49: Test = Test()
        try:
            t_7840: 'SafeIdentifier' = sid_443('users')
            t_7841: 'SqlBuilder' = SqlBuilder()
            t_7841.append_safe('age > ')
            t_7841.append_int32(18)
            t_7844: 'SqlFragment' = t_7841.accumulated
            q_893: 'Query' = from_(t_7840).where(t_7844)
            t_7849: 'bool33' = q_893.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_7839() -> 'str27':
                return 'where int'
            test_49.assert_(t_7849, fn_7839)
        finally:
            test_49.soft_fail_to_hard()
class TestCase72(TestCase46):
    def test___whereAddsConditionWithBoolValue__1395(self) -> None:
        'where adds condition with bool value'
        test_50: Test = Test()
        try:
            t_7828: 'SafeIdentifier' = sid_443('users')
            t_7829: 'SqlBuilder' = SqlBuilder()
            t_7829.append_safe('active = ')
            t_7829.append_boolean(True)
            t_7832: 'SqlFragment' = t_7829.accumulated
            q_895: 'Query' = from_(t_7828).where(t_7832)
            t_7837: 'bool33' = q_895.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_7827() -> 'str27':
                return 'where bool'
            test_50.assert_(t_7837, fn_7827)
        finally:
            test_50.soft_fail_to_hard()
class TestCase73(TestCase46):
    def test___chainedWhereUsesAnd__1397(self) -> None:
        'chained where uses AND'
        test_51: Test = Test()
        try:
            t_7811: 'SafeIdentifier' = sid_443('users')
            t_7812: 'SqlBuilder' = SqlBuilder()
            t_7812.append_safe('age > ')
            t_7812.append_int32(18)
            t_7815: 'SqlFragment' = t_7812.accumulated
            t_7816: 'Query' = from_(t_7811).where(t_7815)
            t_7817: 'SqlBuilder' = SqlBuilder()
            t_7817.append_safe('active = ')
            t_7817.append_boolean(True)
            q_897: 'Query' = t_7816.where(t_7817.accumulated)
            t_7825: 'bool33' = q_897.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_7810() -> 'str27':
                return 'chained where'
            test_51.assert_(t_7825, fn_7810)
        finally:
            test_51.soft_fail_to_hard()
class TestCase74(TestCase46):
    def test___orderByAsc__1400(self) -> None:
        'orderBy ASC'
        test_52: Test = Test()
        try:
            t_7802: 'SafeIdentifier' = sid_443('users')
            t_7803: 'SafeIdentifier' = sid_443('name')
            q_899: 'Query' = from_(t_7802).order_by(t_7803, True)
            t_7808: 'bool33' = q_899.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_7801() -> 'str27':
                return 'order asc'
            test_52.assert_(t_7808, fn_7801)
        finally:
            test_52.soft_fail_to_hard()
class TestCase75(TestCase46):
    def test___orderByDesc__1401(self) -> None:
        'orderBy DESC'
        test_53: Test = Test()
        try:
            t_7793: 'SafeIdentifier' = sid_443('users')
            t_7794: 'SafeIdentifier' = sid_443('created_at')
            q_901: 'Query' = from_(t_7793).order_by(t_7794, False)
            t_7799: 'bool33' = q_901.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_7792() -> 'str27':
                return 'order desc'
            test_53.assert_(t_7799, fn_7792)
        finally:
            test_53.soft_fail_to_hard()
class TestCase76(TestCase46):
    def test___limitAndOffset__1402(self) -> None:
        'limit and offset'
        test_54: Test = Test()
        try:
            t_4122: 'Query'
            t_4122 = from_(sid_443('users')).limit(10)
            t_4123: 'Query'
            t_4123 = t_4122.offset(20)
            q_903: 'Query' = t_4123
            t_7790: 'bool33' = q_903.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_7785() -> 'str27':
                return 'limit/offset'
            test_54.assert_(t_7790, fn_7785)
        finally:
            test_54.soft_fail_to_hard()
class TestCase77(TestCase46):
    def test___limitBubblesOnNegative__1403(self) -> None:
        'limit bubbles on negative'
        test_55: Test = Test()
        try:
            did_bubble_905: 'bool33'
            try:
                from_(sid_443('users')).limit(-1)
                did_bubble_905 = False
            except Exception37:
                did_bubble_905 = True
            def fn_7781() -> 'str27':
                return 'negative limit should bubble'
            test_55.assert_(did_bubble_905, fn_7781)
        finally:
            test_55.soft_fail_to_hard()
class TestCase78(TestCase46):
    def test___offsetBubblesOnNegative__1404(self) -> None:
        'offset bubbles on negative'
        test_56: Test = Test()
        try:
            did_bubble_907: 'bool33'
            try:
                from_(sid_443('users')).offset(-1)
                did_bubble_907 = False
            except Exception37:
                did_bubble_907 = True
            def fn_7777() -> 'str27':
                return 'negative offset should bubble'
            test_56.assert_(did_bubble_907, fn_7777)
        finally:
            test_56.soft_fail_to_hard()
class TestCase79(TestCase46):
    def test___complexComposedQuery__1405(self) -> None:
        'complex composed query'
        test_57: Test = Test()
        try:
            min_age_909: 'int31' = 21
            t_7755: 'SafeIdentifier' = sid_443('users')
            t_7756: 'SafeIdentifier' = sid_443('id')
            t_7757: 'SafeIdentifier' = sid_443('name')
            t_7758: 'SafeIdentifier' = sid_443('email')
            t_7759: 'Query' = from_(t_7755).select((t_7756, t_7757, t_7758))
            t_7760: 'SqlBuilder' = SqlBuilder()
            t_7760.append_safe('age >= ')
            t_7760.append_int32(21)
            t_7764: 'Query' = t_7759.where(t_7760.accumulated)
            t_7765: 'SqlBuilder' = SqlBuilder()
            t_7765.append_safe('active = ')
            t_7765.append_boolean(True)
            t_4108: 'Query'
            t_4108 = t_7764.where(t_7765.accumulated).order_by(sid_443('name'), True).limit(25)
            t_4109: 'Query'
            t_4109 = t_4108.offset(0)
            q_910: 'Query' = t_4109
            t_7775: 'bool33' = q_910.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_7754() -> 'str27':
                return 'complex query'
            test_57.assert_(t_7775, fn_7754)
        finally:
            test_57.soft_fail_to_hard()
class TestCase80(TestCase46):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__1408(self) -> None:
        'safeToSql applies default limit when none set'
        test_58: Test = Test()
        try:
            q_912: 'Query' = from_(sid_443('users'))
            t_4085: 'SqlFragment'
            t_4085 = q_912.safe_to_sql(100)
            t_4086: 'SqlFragment' = t_4085
            s_913: 'str27' = t_4086.to_string()
            t_7752: 'bool33' = s_913 == 'SELECT * FROM users LIMIT 100'
            def fn_7748() -> 'str27':
                return str_cat_8814('should have limit: ', s_913)
            test_58.assert_(t_7752, fn_7748)
        finally:
            test_58.soft_fail_to_hard()
class TestCase81(TestCase46):
    def test___safeToSqlRespectsExplicitLimit__1409(self) -> None:
        'safeToSql respects explicit limit'
        test_59: Test = Test()
        try:
            t_4077: 'Query'
            t_4077 = from_(sid_443('users')).limit(5)
            q_915: 'Query' = t_4077
            t_4080: 'SqlFragment'
            t_4080 = q_915.safe_to_sql(100)
            t_4081: 'SqlFragment' = t_4080
            s_916: 'str27' = t_4081.to_string()
            t_7746: 'bool33' = s_916 == 'SELECT * FROM users LIMIT 5'
            def fn_7742() -> 'str27':
                return str_cat_8814('explicit limit preserved: ', s_916)
            test_59.assert_(t_7746, fn_7742)
        finally:
            test_59.soft_fail_to_hard()
class TestCase82(TestCase46):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__1410(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_60: Test = Test()
        try:
            did_bubble_918: 'bool33'
            try:
                from_(sid_443('users')).safe_to_sql(-1)
                did_bubble_918 = False
            except Exception37:
                did_bubble_918 = True
            def fn_7738() -> 'str27':
                return 'negative defaultLimit should bubble'
            test_60.assert_(did_bubble_918, fn_7738)
        finally:
            test_60.soft_fail_to_hard()
class TestCase83(TestCase46):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__1411(self) -> None:
        'where with injection attempt in string value is escaped'
        test_61: Test = Test()
        try:
            evil_920: 'str27' = "'; DROP TABLE users; --"
            t_7722: 'SafeIdentifier' = sid_443('users')
            t_7723: 'SqlBuilder' = SqlBuilder()
            t_7723.append_safe('name = ')
            t_7723.append_string("'; DROP TABLE users; --")
            t_7726: 'SqlFragment' = t_7723.accumulated
            q_921: 'Query' = from_(t_7722).where(t_7726)
            s_922: 'str27' = q_921.to_sql().to_string()
            t_7731: 'bool33' = s_922.find("''") >= 0
            def fn_7721() -> 'str27':
                return str_cat_8814('quotes must be doubled: ', s_922)
            test_61.assert_(t_7731, fn_7721)
            t_7735: 'bool33' = s_922.find('SELECT * FROM users WHERE name =') >= 0
            def fn_7720() -> 'str27':
                return str_cat_8814('structure intact: ', s_922)
            test_61.assert_(t_7735, fn_7720)
        finally:
            test_61.soft_fail_to_hard()
class TestCase84(TestCase46):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__1413(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_62: Test = Test()
        try:
            attack_924: 'str27' = 'users; DROP TABLE users; --'
            did_bubble_925: 'bool33'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_925 = False
            except Exception37:
                did_bubble_925 = True
            def fn_7717() -> 'str27':
                return 'metacharacter-containing name must be rejected at construction'
            test_62.assert_(did_bubble_925, fn_7717)
        finally:
            test_62.soft_fail_to_hard()
class TestCase85(TestCase46):
    def test___innerJoinProducesInnerJoin__1414(self) -> None:
        'innerJoin produces INNER JOIN'
        test_63: Test = Test()
        try:
            t_7706: 'SafeIdentifier' = sid_443('users')
            t_7707: 'SafeIdentifier' = sid_443('orders')
            t_7708: 'SqlBuilder' = SqlBuilder()
            t_7708.append_safe('users.id = orders.user_id')
            t_7710: 'SqlFragment' = t_7708.accumulated
            q_927: 'Query' = from_(t_7706).inner_join(t_7707, t_7710)
            t_7715: 'bool33' = q_927.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_7705() -> 'str27':
                return 'inner join'
            test_63.assert_(t_7715, fn_7705)
        finally:
            test_63.soft_fail_to_hard()
class TestCase86(TestCase46):
    def test___leftJoinProducesLeftJoin__1416(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_64: Test = Test()
        try:
            t_7694: 'SafeIdentifier' = sid_443('users')
            t_7695: 'SafeIdentifier' = sid_443('profiles')
            t_7696: 'SqlBuilder' = SqlBuilder()
            t_7696.append_safe('users.id = profiles.user_id')
            t_7698: 'SqlFragment' = t_7696.accumulated
            q_929: 'Query' = from_(t_7694).left_join(t_7695, t_7698)
            t_7703: 'bool33' = q_929.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_7693() -> 'str27':
                return 'left join'
            test_64.assert_(t_7703, fn_7693)
        finally:
            test_64.soft_fail_to_hard()
class TestCase87(TestCase46):
    def test___rightJoinProducesRightJoin__1418(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_65: Test = Test()
        try:
            t_7682: 'SafeIdentifier' = sid_443('orders')
            t_7683: 'SafeIdentifier' = sid_443('users')
            t_7684: 'SqlBuilder' = SqlBuilder()
            t_7684.append_safe('orders.user_id = users.id')
            t_7686: 'SqlFragment' = t_7684.accumulated
            q_931: 'Query' = from_(t_7682).right_join(t_7683, t_7686)
            t_7691: 'bool33' = q_931.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_7681() -> 'str27':
                return 'right join'
            test_65.assert_(t_7691, fn_7681)
        finally:
            test_65.soft_fail_to_hard()
class TestCase88(TestCase46):
    def test___fullJoinProducesFullOuterJoin__1420(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_66: Test = Test()
        try:
            t_7670: 'SafeIdentifier' = sid_443('users')
            t_7671: 'SafeIdentifier' = sid_443('orders')
            t_7672: 'SqlBuilder' = SqlBuilder()
            t_7672.append_safe('users.id = orders.user_id')
            t_7674: 'SqlFragment' = t_7672.accumulated
            q_933: 'Query' = from_(t_7670).full_join(t_7671, t_7674)
            t_7679: 'bool33' = q_933.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_7669() -> 'str27':
                return 'full join'
            test_66.assert_(t_7679, fn_7669)
        finally:
            test_66.soft_fail_to_hard()
class TestCase89(TestCase46):
    def test___chainedJoins__1422(self) -> None:
        'chained joins'
        test_67: Test = Test()
        try:
            t_7653: 'SafeIdentifier' = sid_443('users')
            t_7654: 'SafeIdentifier' = sid_443('orders')
            t_7655: 'SqlBuilder' = SqlBuilder()
            t_7655.append_safe('users.id = orders.user_id')
            t_7657: 'SqlFragment' = t_7655.accumulated
            t_7658: 'Query' = from_(t_7653).inner_join(t_7654, t_7657)
            t_7659: 'SafeIdentifier' = sid_443('profiles')
            t_7660: 'SqlBuilder' = SqlBuilder()
            t_7660.append_safe('users.id = profiles.user_id')
            q_935: 'Query' = t_7658.left_join(t_7659, t_7660.accumulated)
            t_7667: 'bool33' = q_935.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_7652() -> 'str27':
                return 'chained joins'
            test_67.assert_(t_7667, fn_7652)
        finally:
            test_67.soft_fail_to_hard()
class TestCase90(TestCase46):
    def test___joinWithWhereAndOrderBy__1425(self) -> None:
        'join with where and orderBy'
        test_68: Test = Test()
        try:
            t_7634: 'SafeIdentifier' = sid_443('users')
            t_7635: 'SafeIdentifier' = sid_443('orders')
            t_7636: 'SqlBuilder' = SqlBuilder()
            t_7636.append_safe('users.id = orders.user_id')
            t_7638: 'SqlFragment' = t_7636.accumulated
            t_7639: 'Query' = from_(t_7634).inner_join(t_7635, t_7638)
            t_7640: 'SqlBuilder' = SqlBuilder()
            t_7640.append_safe('orders.total > ')
            t_7640.append_int32(100)
            t_3992: 'Query'
            t_3992 = t_7639.where(t_7640.accumulated).order_by(sid_443('name'), True).limit(10)
            q_937: 'Query' = t_3992
            t_7650: 'bool33' = q_937.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_7633() -> 'str27':
                return 'join with where/order/limit'
            test_68.assert_(t_7650, fn_7633)
        finally:
            test_68.soft_fail_to_hard()
class TestCase91(TestCase46):
    def test___colHelperProducesQualifiedReference__1428(self) -> None:
        'col helper produces qualified reference'
        test_69: Test = Test()
        try:
            c_939: 'SqlFragment' = col(sid_443('users'), sid_443('id'))
            t_7631: 'bool33' = c_939.to_string() == 'users.id'
            def fn_7625() -> 'str27':
                return 'col helper'
            test_69.assert_(t_7631, fn_7625)
        finally:
            test_69.soft_fail_to_hard()
class TestCase92(TestCase46):
    def test___joinWithColHelper__1429(self) -> None:
        'join with col helper'
        test_70: Test = Test()
        try:
            on_cond_941: 'SqlFragment' = col(sid_443('users'), sid_443('id'))
            b_942: 'SqlBuilder' = SqlBuilder()
            b_942.append_fragment(on_cond_941)
            b_942.append_safe(' = ')
            b_942.append_fragment(col(sid_443('orders'), sid_443('user_id')))
            t_7616: 'SafeIdentifier' = sid_443('users')
            t_7617: 'SafeIdentifier' = sid_443('orders')
            t_7618: 'SqlFragment' = b_942.accumulated
            q_943: 'Query' = from_(t_7616).inner_join(t_7617, t_7618)
            t_7623: 'bool33' = q_943.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_7605() -> 'str27':
                return 'join with col'
            test_70.assert_(t_7623, fn_7605)
        finally:
            test_70.soft_fail_to_hard()
class TestCase93(TestCase46):
    def test___orWhereBasic__1430(self) -> None:
        'orWhere basic'
        test_71: Test = Test()
        try:
            t_7594: 'SafeIdentifier' = sid_443('users')
            t_7595: 'SqlBuilder' = SqlBuilder()
            t_7595.append_safe('status = ')
            t_7595.append_string('active')
            t_7598: 'SqlFragment' = t_7595.accumulated
            q_945: 'Query' = from_(t_7594).or_where(t_7598)
            t_7603: 'bool33' = q_945.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_7593() -> 'str27':
                return 'orWhere basic'
            test_71.assert_(t_7603, fn_7593)
        finally:
            test_71.soft_fail_to_hard()
class TestCase94(TestCase46):
    def test___whereThenOrWhere__1432(self) -> None:
        'where then orWhere'
        test_72: Test = Test()
        try:
            t_7577: 'SafeIdentifier' = sid_443('users')
            t_7578: 'SqlBuilder' = SqlBuilder()
            t_7578.append_safe('age > ')
            t_7578.append_int32(18)
            t_7581: 'SqlFragment' = t_7578.accumulated
            t_7582: 'Query' = from_(t_7577).where(t_7581)
            t_7583: 'SqlBuilder' = SqlBuilder()
            t_7583.append_safe('vip = ')
            t_7583.append_boolean(True)
            q_947: 'Query' = t_7582.or_where(t_7583.accumulated)
            t_7591: 'bool33' = q_947.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_7576() -> 'str27':
                return 'where then orWhere'
            test_72.assert_(t_7591, fn_7576)
        finally:
            test_72.soft_fail_to_hard()
class TestCase95(TestCase46):
    def test___multipleOrWhere__1435(self) -> None:
        'multiple orWhere'
        test_73: Test = Test()
        try:
            t_7555: 'SafeIdentifier' = sid_443('users')
            t_7556: 'SqlBuilder' = SqlBuilder()
            t_7556.append_safe('active = ')
            t_7556.append_boolean(True)
            t_7559: 'SqlFragment' = t_7556.accumulated
            t_7560: 'Query' = from_(t_7555).where(t_7559)
            t_7561: 'SqlBuilder' = SqlBuilder()
            t_7561.append_safe('role = ')
            t_7561.append_string('admin')
            t_7565: 'Query' = t_7560.or_where(t_7561.accumulated)
            t_7566: 'SqlBuilder' = SqlBuilder()
            t_7566.append_safe('role = ')
            t_7566.append_string('moderator')
            q_949: 'Query' = t_7565.or_where(t_7566.accumulated)
            t_7574: 'bool33' = q_949.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_7554() -> 'str27':
                return 'multiple orWhere'
            test_73.assert_(t_7574, fn_7554)
        finally:
            test_73.soft_fail_to_hard()
class TestCase96(TestCase46):
    def test___mixedWhereAndOrWhere__1439(self) -> None:
        'mixed where and orWhere'
        test_74: Test = Test()
        try:
            t_7533: 'SafeIdentifier' = sid_443('users')
            t_7534: 'SqlBuilder' = SqlBuilder()
            t_7534.append_safe('age > ')
            t_7534.append_int32(18)
            t_7537: 'SqlFragment' = t_7534.accumulated
            t_7538: 'Query' = from_(t_7533).where(t_7537)
            t_7539: 'SqlBuilder' = SqlBuilder()
            t_7539.append_safe('active = ')
            t_7539.append_boolean(True)
            t_7543: 'Query' = t_7538.where(t_7539.accumulated)
            t_7544: 'SqlBuilder' = SqlBuilder()
            t_7544.append_safe('vip = ')
            t_7544.append_boolean(True)
            q_951: 'Query' = t_7543.or_where(t_7544.accumulated)
            t_7552: 'bool33' = q_951.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_7532() -> 'str27':
                return 'mixed where and orWhere'
            test_74.assert_(t_7552, fn_7532)
        finally:
            test_74.soft_fail_to_hard()
class TestCase97(TestCase46):
    def test___whereNull__1443(self) -> None:
        'whereNull'
        test_75: Test = Test()
        try:
            t_7524: 'SafeIdentifier' = sid_443('users')
            t_7525: 'SafeIdentifier' = sid_443('deleted_at')
            q_953: 'Query' = from_(t_7524).where_null(t_7525)
            t_7530: 'bool33' = q_953.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_7523() -> 'str27':
                return 'whereNull'
            test_75.assert_(t_7530, fn_7523)
        finally:
            test_75.soft_fail_to_hard()
class TestCase98(TestCase46):
    def test___whereNotNull__1444(self) -> None:
        'whereNotNull'
        test_76: Test = Test()
        try:
            t_7515: 'SafeIdentifier' = sid_443('users')
            t_7516: 'SafeIdentifier' = sid_443('email')
            q_955: 'Query' = from_(t_7515).where_not_null(t_7516)
            t_7521: 'bool33' = q_955.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_7514() -> 'str27':
                return 'whereNotNull'
            test_76.assert_(t_7521, fn_7514)
        finally:
            test_76.soft_fail_to_hard()
class TestCase99(TestCase46):
    def test___whereNullChainedWithWhere__1445(self) -> None:
        'whereNull chained with where'
        test_77: Test = Test()
        try:
            t_7501: 'SafeIdentifier' = sid_443('users')
            t_7502: 'SqlBuilder' = SqlBuilder()
            t_7502.append_safe('active = ')
            t_7502.append_boolean(True)
            t_7505: 'SqlFragment' = t_7502.accumulated
            q_957: 'Query' = from_(t_7501).where(t_7505).where_null(sid_443('deleted_at'))
            t_7512: 'bool33' = q_957.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_7500() -> 'str27':
                return 'whereNull chained'
            test_77.assert_(t_7512, fn_7500)
        finally:
            test_77.soft_fail_to_hard()
class TestCase100(TestCase46):
    def test___whereNotNullChainedWithOrWhere__1447(self) -> None:
        'whereNotNull chained with orWhere'
        test_78: Test = Test()
        try:
            t_7487: 'SafeIdentifier' = sid_443('users')
            t_7488: 'SafeIdentifier' = sid_443('deleted_at')
            t_7489: 'Query' = from_(t_7487).where_null(t_7488)
            t_7490: 'SqlBuilder' = SqlBuilder()
            t_7490.append_safe('role = ')
            t_7490.append_string('admin')
            q_959: 'Query' = t_7489.or_where(t_7490.accumulated)
            t_7498: 'bool33' = q_959.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_7486() -> 'str27':
                return 'whereNotNull with orWhere'
            test_78.assert_(t_7498, fn_7486)
        finally:
            test_78.soft_fail_to_hard()
class TestCase101(TestCase46):
    def test___whereInWithIntValues__1449(self) -> None:
        'whereIn with int values'
        test_79: Test = Test()
        try:
            t_7475: 'SafeIdentifier' = sid_443('users')
            t_7476: 'SafeIdentifier' = sid_443('id')
            t_7477: 'SqlInt32' = SqlInt32(1)
            t_7478: 'SqlInt32' = SqlInt32(2)
            t_7479: 'SqlInt32' = SqlInt32(3)
            q_961: 'Query' = from_(t_7475).where_in(t_7476, (t_7477, t_7478, t_7479))
            t_7484: 'bool33' = q_961.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_7474() -> 'str27':
                return 'whereIn ints'
            test_79.assert_(t_7484, fn_7474)
        finally:
            test_79.soft_fail_to_hard()
class TestCase102(TestCase46):
    def test___whereInWithStringValuesEscaping__1450(self) -> None:
        'whereIn with string values escaping'
        test_80: Test = Test()
        try:
            t_7464: 'SafeIdentifier' = sid_443('users')
            t_7465: 'SafeIdentifier' = sid_443('name')
            t_7466: 'SqlString' = SqlString('Alice')
            t_7467: 'SqlString' = SqlString("Bob's")
            q_963: 'Query' = from_(t_7464).where_in(t_7465, (t_7466, t_7467))
            t_7472: 'bool33' = q_963.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_7463() -> 'str27':
                return 'whereIn strings'
            test_80.assert_(t_7472, fn_7463)
        finally:
            test_80.soft_fail_to_hard()
class TestCase103(TestCase46):
    def test___whereInWithEmptyListProduces1_0__1451(self) -> None:
        'whereIn with empty list produces 1=0'
        test_81: Test = Test()
        try:
            t_7455: 'SafeIdentifier' = sid_443('users')
            t_7456: 'SafeIdentifier' = sid_443('id')
            q_965: 'Query' = from_(t_7455).where_in(t_7456, ())
            t_7461: 'bool33' = q_965.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_7454() -> 'str27':
                return 'whereIn empty'
            test_81.assert_(t_7461, fn_7454)
        finally:
            test_81.soft_fail_to_hard()
class TestCase104(TestCase46):
    def test___whereInChained__1452(self) -> None:
        'whereIn chained'
        test_82: Test = Test()
        try:
            t_7439: 'SafeIdentifier' = sid_443('users')
            t_7440: 'SqlBuilder' = SqlBuilder()
            t_7440.append_safe('active = ')
            t_7440.append_boolean(True)
            t_7443: 'SqlFragment' = t_7440.accumulated
            q_967: 'Query' = from_(t_7439).where(t_7443).where_in(sid_443('role'), (SqlString('admin'), SqlString('user')))
            t_7452: 'bool33' = q_967.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_7438() -> 'str27':
                return 'whereIn chained'
            test_82.assert_(t_7452, fn_7438)
        finally:
            test_82.soft_fail_to_hard()
class TestCase105(TestCase46):
    def test___whereInSingleElement__1454(self) -> None:
        'whereIn single element'
        test_83: Test = Test()
        try:
            t_7429: 'SafeIdentifier' = sid_443('users')
            t_7430: 'SafeIdentifier' = sid_443('id')
            t_7431: 'SqlInt32' = SqlInt32(42)
            q_969: 'Query' = from_(t_7429).where_in(t_7430, (t_7431,))
            t_7436: 'bool33' = q_969.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_7428() -> 'str27':
                return 'whereIn single'
            test_83.assert_(t_7436, fn_7428)
        finally:
            test_83.soft_fail_to_hard()
class TestCase106(TestCase46):
    def test___whereNotBasic__1455(self) -> None:
        'whereNot basic'
        test_84: Test = Test()
        try:
            t_7417: 'SafeIdentifier' = sid_443('users')
            t_7418: 'SqlBuilder' = SqlBuilder()
            t_7418.append_safe('active = ')
            t_7418.append_boolean(True)
            t_7421: 'SqlFragment' = t_7418.accumulated
            q_971: 'Query' = from_(t_7417).where_not(t_7421)
            t_7426: 'bool33' = q_971.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_7416() -> 'str27':
                return 'whereNot'
            test_84.assert_(t_7426, fn_7416)
        finally:
            test_84.soft_fail_to_hard()
class TestCase107(TestCase46):
    def test___whereNotChained__1457(self) -> None:
        'whereNot chained'
        test_85: Test = Test()
        try:
            t_7400: 'SafeIdentifier' = sid_443('users')
            t_7401: 'SqlBuilder' = SqlBuilder()
            t_7401.append_safe('age > ')
            t_7401.append_int32(18)
            t_7404: 'SqlFragment' = t_7401.accumulated
            t_7405: 'Query' = from_(t_7400).where(t_7404)
            t_7406: 'SqlBuilder' = SqlBuilder()
            t_7406.append_safe('banned = ')
            t_7406.append_boolean(True)
            q_973: 'Query' = t_7405.where_not(t_7406.accumulated)
            t_7414: 'bool33' = q_973.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_7399() -> 'str27':
                return 'whereNot chained'
            test_85.assert_(t_7414, fn_7399)
        finally:
            test_85.soft_fail_to_hard()
class TestCase108(TestCase46):
    def test___whereBetweenIntegers__1460(self) -> None:
        'whereBetween integers'
        test_86: Test = Test()
        try:
            t_7389: 'SafeIdentifier' = sid_443('users')
            t_7390: 'SafeIdentifier' = sid_443('age')
            t_7391: 'SqlInt32' = SqlInt32(18)
            t_7392: 'SqlInt32' = SqlInt32(65)
            q_975: 'Query' = from_(t_7389).where_between(t_7390, t_7391, t_7392)
            t_7397: 'bool33' = q_975.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_7388() -> 'str27':
                return 'whereBetween ints'
            test_86.assert_(t_7397, fn_7388)
        finally:
            test_86.soft_fail_to_hard()
class TestCase109(TestCase46):
    def test___whereBetweenChained__1461(self) -> None:
        'whereBetween chained'
        test_87: Test = Test()
        try:
            t_7373: 'SafeIdentifier' = sid_443('users')
            t_7374: 'SqlBuilder' = SqlBuilder()
            t_7374.append_safe('active = ')
            t_7374.append_boolean(True)
            t_7377: 'SqlFragment' = t_7374.accumulated
            q_977: 'Query' = from_(t_7373).where(t_7377).where_between(sid_443('age'), SqlInt32(21), SqlInt32(30))
            t_7386: 'bool33' = q_977.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_7372() -> 'str27':
                return 'whereBetween chained'
            test_87.assert_(t_7386, fn_7372)
        finally:
            test_87.soft_fail_to_hard()
class TestCase110(TestCase46):
    def test___whereLikeBasic__1463(self) -> None:
        'whereLike basic'
        test_88: Test = Test()
        try:
            t_7364: 'SafeIdentifier' = sid_443('users')
            t_7365: 'SafeIdentifier' = sid_443('name')
            q_979: 'Query' = from_(t_7364).where_like(t_7365, 'John%')
            t_7370: 'bool33' = q_979.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_7363() -> 'str27':
                return 'whereLike'
            test_88.assert_(t_7370, fn_7363)
        finally:
            test_88.soft_fail_to_hard()
class TestCase111(TestCase46):
    def test___whereIlikeBasic__1464(self) -> None:
        'whereILike basic'
        test_89: Test = Test()
        try:
            t_7355: 'SafeIdentifier' = sid_443('users')
            t_7356: 'SafeIdentifier' = sid_443('email')
            q_981: 'Query' = from_(t_7355).where_i_like(t_7356, '%@gmail.com')
            t_7361: 'bool33' = q_981.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_7354() -> 'str27':
                return 'whereILike'
            test_89.assert_(t_7361, fn_7354)
        finally:
            test_89.soft_fail_to_hard()
class TestCase112(TestCase46):
    def test___whereLikeWithInjectionAttempt__1465(self) -> None:
        'whereLike with injection attempt'
        test_90: Test = Test()
        try:
            t_7341: 'SafeIdentifier' = sid_443('users')
            t_7342: 'SafeIdentifier' = sid_443('name')
            q_983: 'Query' = from_(t_7341).where_like(t_7342, "'; DROP TABLE users; --")
            s_984: 'str27' = q_983.to_sql().to_string()
            t_7347: 'bool33' = s_984.find("''") >= 0
            def fn_7340() -> 'str27':
                return str_cat_8814('like injection escaped: ', s_984)
            test_90.assert_(t_7347, fn_7340)
            t_7351: 'bool33' = s_984.find('LIKE') >= 0
            def fn_7339() -> 'str27':
                return str_cat_8814('like structure intact: ', s_984)
            test_90.assert_(t_7351, fn_7339)
        finally:
            test_90.soft_fail_to_hard()
class TestCase113(TestCase46):
    def test___whereLikeWildcardPatterns__1466(self) -> None:
        'whereLike wildcard patterns'
        test_91: Test = Test()
        try:
            t_7331: 'SafeIdentifier' = sid_443('users')
            t_7332: 'SafeIdentifier' = sid_443('name')
            q_986: 'Query' = from_(t_7331).where_like(t_7332, '%son%')
            t_7337: 'bool33' = q_986.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_7330() -> 'str27':
                return 'whereLike wildcard'
            test_91.assert_(t_7337, fn_7330)
        finally:
            test_91.soft_fail_to_hard()
class TestCase114(TestCase46):
    def test___countAllProducesCount__1467(self) -> None:
        'countAll produces COUNT(*)'
        test_92: Test = Test()
        try:
            f_988: 'SqlFragment' = count_all()
            t_7328: 'bool33' = f_988.to_string() == 'COUNT(*)'
            def fn_7324() -> 'str27':
                return 'countAll'
            test_92.assert_(t_7328, fn_7324)
        finally:
            test_92.soft_fail_to_hard()
class TestCase115(TestCase46):
    def test___countColProducesCountField__1468(self) -> None:
        'countCol produces COUNT(field)'
        test_93: Test = Test()
        try:
            f_990: 'SqlFragment' = count_col(sid_443('id'))
            t_7322: 'bool33' = f_990.to_string() == 'COUNT(id)'
            def fn_7317() -> 'str27':
                return 'countCol'
            test_93.assert_(t_7322, fn_7317)
        finally:
            test_93.soft_fail_to_hard()
class TestCase116(TestCase46):
    def test___sumColProducesSumField__1469(self) -> None:
        'sumCol produces SUM(field)'
        test_94: Test = Test()
        try:
            f_992: 'SqlFragment' = sum_col(sid_443('amount'))
            t_7315: 'bool33' = f_992.to_string() == 'SUM(amount)'
            def fn_7310() -> 'str27':
                return 'sumCol'
            test_94.assert_(t_7315, fn_7310)
        finally:
            test_94.soft_fail_to_hard()
class TestCase117(TestCase46):
    def test___avgColProducesAvgField__1470(self) -> None:
        'avgCol produces AVG(field)'
        test_95: Test = Test()
        try:
            f_994: 'SqlFragment' = avg_col(sid_443('price'))
            t_7308: 'bool33' = f_994.to_string() == 'AVG(price)'
            def fn_7303() -> 'str27':
                return 'avgCol'
            test_95.assert_(t_7308, fn_7303)
        finally:
            test_95.soft_fail_to_hard()
class TestCase118(TestCase46):
    def test___minColProducesMinField__1471(self) -> None:
        'minCol produces MIN(field)'
        test_96: Test = Test()
        try:
            f_996: 'SqlFragment' = min_col(sid_443('created_at'))
            t_7301: 'bool33' = f_996.to_string() == 'MIN(created_at)'
            def fn_7296() -> 'str27':
                return 'minCol'
            test_96.assert_(t_7301, fn_7296)
        finally:
            test_96.soft_fail_to_hard()
class TestCase119(TestCase46):
    def test___maxColProducesMaxField__1472(self) -> None:
        'maxCol produces MAX(field)'
        test_97: Test = Test()
        try:
            f_998: 'SqlFragment' = max_col(sid_443('score'))
            t_7294: 'bool33' = f_998.to_string() == 'MAX(score)'
            def fn_7289() -> 'str27':
                return 'maxCol'
            test_97.assert_(t_7294, fn_7289)
        finally:
            test_97.soft_fail_to_hard()
class TestCase120(TestCase46):
    def test___selectExprWithAggregate__1473(self) -> None:
        'selectExpr with aggregate'
        test_98: Test = Test()
        try:
            t_7281: 'SafeIdentifier' = sid_443('orders')
            t_7282: 'SqlFragment' = count_all()
            q_1000: 'Query' = from_(t_7281).select_expr((t_7282,))
            t_7287: 'bool33' = q_1000.to_sql().to_string() == 'SELECT COUNT(*) FROM orders'
            def fn_7280() -> 'str27':
                return 'selectExpr count'
            test_98.assert_(t_7287, fn_7280)
        finally:
            test_98.soft_fail_to_hard()
class TestCase121(TestCase46):
    def test___selectExprWithMultipleExpressions__1474(self) -> None:
        'selectExpr with multiple expressions'
        test_99: Test = Test()
        try:
            name_frag_1002: 'SqlFragment' = col(sid_443('users'), sid_443('name'))
            t_7272: 'SafeIdentifier' = sid_443('users')
            t_7273: 'SqlFragment' = count_all()
            q_1003: 'Query' = from_(t_7272).select_expr((name_frag_1002, t_7273))
            t_7278: 'bool33' = q_1003.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users'
            def fn_7268() -> 'str27':
                return 'selectExpr multi'
            test_99.assert_(t_7278, fn_7268)
        finally:
            test_99.soft_fail_to_hard()
class TestCase122(TestCase46):
    def test___selectExprOverridesSelectedFields__1475(self) -> None:
        'selectExpr overrides selectedFields'
        test_100: Test = Test()
        try:
            t_7257: 'SafeIdentifier' = sid_443('users')
            t_7258: 'SafeIdentifier' = sid_443('id')
            t_7259: 'SafeIdentifier' = sid_443('name')
            q_1005: 'Query' = from_(t_7257).select((t_7258, t_7259)).select_expr((count_all(),))
            t_7266: 'bool33' = q_1005.to_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_7256() -> 'str27':
                return 'selectExpr overrides select'
            test_100.assert_(t_7266, fn_7256)
        finally:
            test_100.soft_fail_to_hard()
class TestCase123(TestCase46):
    def test___groupBySingleField__1476(self) -> None:
        'groupBy single field'
        test_101: Test = Test()
        try:
            t_7243: 'SafeIdentifier' = sid_443('orders')
            t_7246: 'SqlFragment' = col(sid_443('orders'), sid_443('status'))
            t_7247: 'SqlFragment' = count_all()
            q_1007: 'Query' = from_(t_7243).select_expr((t_7246, t_7247)).group_by(sid_443('status'))
            t_7254: 'bool33' = q_1007.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status'
            def fn_7242() -> 'str27':
                return 'groupBy single'
            test_101.assert_(t_7254, fn_7242)
        finally:
            test_101.soft_fail_to_hard()
class TestCase124(TestCase46):
    def test___groupByMultipleFields__1477(self) -> None:
        'groupBy multiple fields'
        test_102: Test = Test()
        try:
            t_7232: 'SafeIdentifier' = sid_443('orders')
            t_7233: 'SafeIdentifier' = sid_443('status')
            q_1009: 'Query' = from_(t_7232).group_by(t_7233).group_by(sid_443('category'))
            t_7240: 'bool33' = q_1009.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category'
            def fn_7231() -> 'str27':
                return 'groupBy multiple'
            test_102.assert_(t_7240, fn_7231)
        finally:
            test_102.soft_fail_to_hard()
class TestCase125(TestCase46):
    def test___havingBasic__1478(self) -> None:
        'having basic'
        test_103: Test = Test()
        try:
            t_7213: 'SafeIdentifier' = sid_443('orders')
            t_7216: 'SqlFragment' = col(sid_443('orders'), sid_443('status'))
            t_7217: 'SqlFragment' = count_all()
            t_7220: 'Query' = from_(t_7213).select_expr((t_7216, t_7217)).group_by(sid_443('status'))
            t_7221: 'SqlBuilder' = SqlBuilder()
            t_7221.append_safe('COUNT(*) > ')
            t_7221.append_int32(5)
            q_1011: 'Query' = t_7220.having(t_7221.accumulated)
            t_7229: 'bool33' = q_1011.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5'
            def fn_7212() -> 'str27':
                return 'having basic'
            test_103.assert_(t_7229, fn_7212)
        finally:
            test_103.soft_fail_to_hard()
class TestCase126(TestCase46):
    def test___orHaving__1480(self) -> None:
        'orHaving'
        test_104: Test = Test()
        try:
            t_7194: 'SafeIdentifier' = sid_443('orders')
            t_7195: 'SafeIdentifier' = sid_443('status')
            t_7196: 'Query' = from_(t_7194).group_by(t_7195)
            t_7197: 'SqlBuilder' = SqlBuilder()
            t_7197.append_safe('COUNT(*) > ')
            t_7197.append_int32(5)
            t_7201: 'Query' = t_7196.having(t_7197.accumulated)
            t_7202: 'SqlBuilder' = SqlBuilder()
            t_7202.append_safe('SUM(total) > ')
            t_7202.append_int32(1000)
            q_1013: 'Query' = t_7201.or_having(t_7202.accumulated)
            t_7210: 'bool33' = q_1013.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000'
            def fn_7193() -> 'str27':
                return 'orHaving'
            test_104.assert_(t_7210, fn_7193)
        finally:
            test_104.soft_fail_to_hard()
class TestCase127(TestCase46):
    def test___distinctBasic__1483(self) -> None:
        'distinct basic'
        test_105: Test = Test()
        try:
            t_7184: 'SafeIdentifier' = sid_443('users')
            t_7185: 'SafeIdentifier' = sid_443('name')
            q_1015: 'Query' = from_(t_7184).select((t_7185,)).distinct()
            t_7191: 'bool33' = q_1015.to_sql().to_string() == 'SELECT DISTINCT name FROM users'
            def fn_7183() -> 'str27':
                return 'distinct'
            test_105.assert_(t_7191, fn_7183)
        finally:
            test_105.soft_fail_to_hard()
class TestCase128(TestCase46):
    def test___distinctWithWhere__1484(self) -> None:
        'distinct with where'
        test_106: Test = Test()
        try:
            t_7169: 'SafeIdentifier' = sid_443('users')
            t_7170: 'SafeIdentifier' = sid_443('email')
            t_7171: 'Query' = from_(t_7169).select((t_7170,))
            t_7172: 'SqlBuilder' = SqlBuilder()
            t_7172.append_safe('active = ')
            t_7172.append_boolean(True)
            q_1017: 'Query' = t_7171.where(t_7172.accumulated).distinct()
            t_7181: 'bool33' = q_1017.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE'
            def fn_7168() -> 'str27':
                return 'distinct with where'
            test_106.assert_(t_7181, fn_7168)
        finally:
            test_106.soft_fail_to_hard()
class TestCase129(TestCase46):
    def test___countSqlBare__1486(self) -> None:
        'countSql bare'
        test_107: Test = Test()
        try:
            q_1019: 'Query' = from_(sid_443('users'))
            t_7166: 'bool33' = q_1019.count_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_7161() -> 'str27':
                return 'countSql bare'
            test_107.assert_(t_7166, fn_7161)
        finally:
            test_107.soft_fail_to_hard()
class TestCase130(TestCase46):
    def test___countSqlWithWhere__1487(self) -> None:
        'countSql with WHERE'
        test_108: Test = Test()
        try:
            t_7150: 'SafeIdentifier' = sid_443('users')
            t_7151: 'SqlBuilder' = SqlBuilder()
            t_7151.append_safe('active = ')
            t_7151.append_boolean(True)
            t_7154: 'SqlFragment' = t_7151.accumulated
            q_1021: 'Query' = from_(t_7150).where(t_7154)
            t_7159: 'bool33' = q_1021.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_7149() -> 'str27':
                return 'countSql with where'
            test_108.assert_(t_7159, fn_7149)
        finally:
            test_108.soft_fail_to_hard()
class TestCase131(TestCase46):
    def test___countSqlWithJoin__1489(self) -> None:
        'countSql with JOIN'
        test_109: Test = Test()
        try:
            t_7133: 'SafeIdentifier' = sid_443('users')
            t_7134: 'SafeIdentifier' = sid_443('orders')
            t_7135: 'SqlBuilder' = SqlBuilder()
            t_7135.append_safe('users.id = orders.user_id')
            t_7137: 'SqlFragment' = t_7135.accumulated
            t_7138: 'Query' = from_(t_7133).inner_join(t_7134, t_7137)
            t_7139: 'SqlBuilder' = SqlBuilder()
            t_7139.append_safe('orders.total > ')
            t_7139.append_int32(100)
            q_1023: 'Query' = t_7138.where(t_7139.accumulated)
            t_7147: 'bool33' = q_1023.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100'
            def fn_7132() -> 'str27':
                return 'countSql with join'
            test_109.assert_(t_7147, fn_7132)
        finally:
            test_109.soft_fail_to_hard()
class TestCase132(TestCase46):
    def test___countSqlDropsOrderByLimitOffset__1492(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_110: Test = Test()
        try:
            t_7119: 'SafeIdentifier' = sid_443('users')
            t_7120: 'SqlBuilder' = SqlBuilder()
            t_7120.append_safe('active = ')
            t_7120.append_boolean(True)
            t_7123: 'SqlFragment' = t_7120.accumulated
            t_3568: 'Query'
            t_3568 = from_(t_7119).where(t_7123).order_by(sid_443('name'), True).limit(10)
            t_3569: 'Query'
            t_3569 = t_3568.offset(20)
            q_1025: 'Query' = t_3569
            s_1026: 'str27' = q_1025.count_sql().to_string()
            t_7130: 'bool33' = s_1026 == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_7118() -> 'str27':
                return str_cat_8814('countSql drops extras: ', s_1026)
            test_110.assert_(t_7130, fn_7118)
        finally:
            test_110.soft_fail_to_hard()
class TestCase133(TestCase46):
    def test___fullAggregationQuery__1494(self) -> None:
        'full aggregation query'
        test_111: Test = Test()
        try:
            t_7086: 'SafeIdentifier' = sid_443('orders')
            t_7089: 'SqlFragment' = col(sid_443('orders'), sid_443('status'))
            t_7090: 'SqlFragment' = count_all()
            t_7092: 'SqlFragment' = sum_col(sid_443('total'))
            t_7093: 'Query' = from_(t_7086).select_expr((t_7089, t_7090, t_7092))
            t_7094: 'SafeIdentifier' = sid_443('users')
            t_7095: 'SqlBuilder' = SqlBuilder()
            t_7095.append_safe('orders.user_id = users.id')
            t_7098: 'Query' = t_7093.inner_join(t_7094, t_7095.accumulated)
            t_7099: 'SqlBuilder' = SqlBuilder()
            t_7099.append_safe('users.active = ')
            t_7099.append_boolean(True)
            t_7105: 'Query' = t_7098.where(t_7099.accumulated).group_by(sid_443('status'))
            t_7106: 'SqlBuilder' = SqlBuilder()
            t_7106.append_safe('COUNT(*) > ')
            t_7106.append_int32(3)
            q_1028: 'Query' = t_7105.having(t_7106.accumulated).order_by(sid_443('status'), True)
            expected_1029: 'str27' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            t_7116: 'bool33' = q_1028.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_7085() -> 'str27':
                return 'full aggregation'
            test_111.assert_(t_7116, fn_7085)
        finally:
            test_111.soft_fail_to_hard()
class TestCase134(TestCase46):
    def test___safeIdentifierAcceptsValidNames__1498(self) -> None:
        'safeIdentifier accepts valid names'
        test_118: Test = Test()
        try:
            t_3522: 'SafeIdentifier'
            t_3522 = safe_identifier('user_name')
            id_1067: 'SafeIdentifier' = t_3522
            t_7083: 'bool33' = id_1067.sql_value == 'user_name'
            def fn_7080() -> 'str27':
                return 'value should round-trip'
            test_118.assert_(t_7083, fn_7080)
        finally:
            test_118.soft_fail_to_hard()
class TestCase135(TestCase46):
    def test___safeIdentifierRejectsEmptyString__1499(self) -> None:
        'safeIdentifier rejects empty string'
        test_119: Test = Test()
        try:
            did_bubble_1069: 'bool33'
            try:
                safe_identifier('')
                did_bubble_1069 = False
            except Exception37:
                did_bubble_1069 = True
            def fn_7077() -> 'str27':
                return 'empty string should bubble'
            test_119.assert_(did_bubble_1069, fn_7077)
        finally:
            test_119.soft_fail_to_hard()
class TestCase136(TestCase46):
    def test___safeIdentifierRejectsLeadingDigit__1500(self) -> None:
        'safeIdentifier rejects leading digit'
        test_120: Test = Test()
        try:
            did_bubble_1071: 'bool33'
            try:
                safe_identifier('1col')
                did_bubble_1071 = False
            except Exception37:
                did_bubble_1071 = True
            def fn_7074() -> 'str27':
                return 'leading digit should bubble'
            test_120.assert_(did_bubble_1071, fn_7074)
        finally:
            test_120.soft_fail_to_hard()
class TestCase137(TestCase46):
    def test___safeIdentifierRejectsSqlMetacharacters__1501(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_121: Test = Test()
        try:
            cases_1073: 'Sequence29[str27]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_7071(c_1074: 'str27') -> 'None':
                did_bubble_1075: 'bool33'
                try:
                    safe_identifier(c_1074)
                    did_bubble_1075 = False
                except Exception37:
                    did_bubble_1075 = True
                def fn_7068() -> 'str27':
                    return str_cat_8814('should reject: ', c_1074)
                test_121.assert_(did_bubble_1075, fn_7068)
            list_for_each_8806(cases_1073, fn_7071)
        finally:
            test_121.soft_fail_to_hard()
class TestCase138(TestCase46):
    def test___tableDefFieldLookupFound__1502(self) -> None:
        'TableDef field lookup - found'
        test_122: Test = Test()
        try:
            t_3499: 'SafeIdentifier'
            t_3499 = safe_identifier('users')
            t_3500: 'SafeIdentifier' = t_3499
            t_3501: 'SafeIdentifier'
            t_3501 = safe_identifier('name')
            t_3502: 'SafeIdentifier' = t_3501
            t_7058: 'StringField' = StringField()
            t_7059: 'FieldDef' = FieldDef(t_3502, t_7058, False)
            t_3505: 'SafeIdentifier'
            t_3505 = safe_identifier('age')
            t_3506: 'SafeIdentifier' = t_3505
            t_7060: 'IntField' = IntField()
            t_7061: 'FieldDef' = FieldDef(t_3506, t_7060, False)
            td_1077: 'TableDef' = TableDef(t_3500, (t_7059, t_7061))
            t_3510: 'FieldDef'
            t_3510 = td_1077.field('age')
            f_1078: 'FieldDef' = t_3510
            t_7066: 'bool33' = f_1078.name.sql_value == 'age'
            def fn_7057() -> 'str27':
                return 'should find age field'
            test_122.assert_(t_7066, fn_7057)
        finally:
            test_122.soft_fail_to_hard()
class TestCase139(TestCase46):
    def test___tableDefFieldLookupNotFoundBubbles__1503(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_123: Test = Test()
        try:
            t_3490: 'SafeIdentifier'
            t_3490 = safe_identifier('users')
            t_3491: 'SafeIdentifier' = t_3490
            t_3492: 'SafeIdentifier'
            t_3492 = safe_identifier('name')
            t_3493: 'SafeIdentifier' = t_3492
            t_7052: 'StringField' = StringField()
            t_7053: 'FieldDef' = FieldDef(t_3493, t_7052, False)
            td_1080: 'TableDef' = TableDef(t_3491, (t_7053,))
            did_bubble_1081: 'bool33'
            try:
                td_1080.field('nonexistent')
                did_bubble_1081 = False
            except Exception37:
                did_bubble_1081 = True
            def fn_7051() -> 'str27':
                return 'unknown field should bubble'
            test_123.assert_(did_bubble_1081, fn_7051)
        finally:
            test_123.soft_fail_to_hard()
class TestCase140(TestCase46):
    def test___fieldDefNullableFlag__1504(self) -> None:
        'FieldDef nullable flag'
        test_124: Test = Test()
        try:
            t_3478: 'SafeIdentifier'
            t_3478 = safe_identifier('email')
            t_3479: 'SafeIdentifier' = t_3478
            t_7040: 'StringField' = StringField()
            required_1083: 'FieldDef' = FieldDef(t_3479, t_7040, False)
            t_3482: 'SafeIdentifier'
            t_3482 = safe_identifier('bio')
            t_3483: 'SafeIdentifier' = t_3482
            t_7042: 'StringField' = StringField()
            optional_1084: 'FieldDef' = FieldDef(t_3483, t_7042, True)
            t_7046: 'bool33' = not required_1083.nullable
            def fn_7039() -> 'str27':
                return 'required field should not be nullable'
            test_124.assert_(t_7046, fn_7039)
            t_7048: 'bool33' = optional_1084.nullable
            def fn_7038() -> 'str27':
                return 'optional field should be nullable'
            test_124.assert_(t_7048, fn_7038)
        finally:
            test_124.soft_fail_to_hard()
class TestCase141(TestCase46):
    def test___stringEscaping__1505(self) -> None:
        'string escaping'
        test_128: Test = Test()
        try:
            def build_1210(name_1212: 'str27') -> 'str27':
                t_7020: 'SqlBuilder' = SqlBuilder()
                t_7020.append_safe('select * from hi where name = ')
                t_7020.append_string(name_1212)
                return t_7020.accumulated.to_string()
            def build_wrong_1211(name_1214: 'str27') -> 'str27':
                return str_cat_8814("select * from hi where name = '", name_1214, "'")
            actual_1507: 'str27' = build_1210('world')
            t_7030: 'bool33' = actual_1507 == "select * from hi where name = 'world'"
            def fn_7027() -> 'str27':
                return str_cat_8814('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_1507, ')')
            test_128.assert_(t_7030, fn_7027)
            bobby_tables_1216: 'str27' = "Robert'); drop table hi;--"
            actual_1509: 'str27' = build_1210("Robert'); drop table hi;--")
            t_7034: 'bool33' = actual_1509 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_7026() -> 'str27':
                return str_cat_8814('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_1509, ')')
            test_128.assert_(t_7034, fn_7026)
            def fn_7025() -> 'str27':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_128.assert_(True, fn_7025)
        finally:
            test_128.soft_fail_to_hard()
class TestCase142(TestCase46):
    def test___stringEdgeCases__1513(self) -> None:
        'string edge cases'
        test_129: Test = Test()
        try:
            t_6988: 'SqlBuilder' = SqlBuilder()
            t_6988.append_safe('v = ')
            t_6988.append_string('')
            actual_1514: 'str27' = t_6988.accumulated.to_string()
            t_6994: 'bool33' = actual_1514 == "v = ''"
            def fn_6987() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_1514, ')')
            test_129.assert_(t_6994, fn_6987)
            t_6996: 'SqlBuilder' = SqlBuilder()
            t_6996.append_safe('v = ')
            t_6996.append_string("a''b")
            actual_1517: 'str27' = t_6996.accumulated.to_string()
            t_7002: 'bool33' = actual_1517 == "v = 'a''''b'"
            def fn_6986() -> 'str27':
                return str_cat_8814("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_1517, ')')
            test_129.assert_(t_7002, fn_6986)
            t_7004: 'SqlBuilder' = SqlBuilder()
            t_7004.append_safe('v = ')
            t_7004.append_string('Hello \u4e16\u754c')
            actual_1520: 'str27' = t_7004.accumulated.to_string()
            t_7010: 'bool33' = actual_1520 == "v = 'Hello \u4e16\u754c'"
            def fn_6985() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_1520, ')')
            test_129.assert_(t_7010, fn_6985)
            t_7012: 'SqlBuilder' = SqlBuilder()
            t_7012.append_safe('v = ')
            t_7012.append_string('Line1\nLine2')
            actual_1523: 'str27' = t_7012.accumulated.to_string()
            t_7018: 'bool33' = actual_1523 == "v = 'Line1\nLine2'"
            def fn_6984() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_1523, ')')
            test_129.assert_(t_7018, fn_6984)
        finally:
            test_129.soft_fail_to_hard()
class TestCase143(TestCase46):
    def test___numbersAndBooleans__1526(self) -> None:
        'numbers and booleans'
        test_130: Test = Test()
        try:
            t_6959: 'SqlBuilder' = SqlBuilder()
            t_6959.append_safe('select ')
            t_6959.append_int32(42)
            t_6959.append_safe(', ')
            t_6959.append_int64(43)
            t_6959.append_safe(', ')
            t_6959.append_float64(19.99)
            t_6959.append_safe(', ')
            t_6959.append_boolean(True)
            t_6959.append_safe(', ')
            t_6959.append_boolean(False)
            actual_1527: 'str27' = t_6959.accumulated.to_string()
            t_6973: 'bool33' = actual_1527 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_6958() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_1527, ')')
            test_130.assert_(t_6973, fn_6958)
            t_3423: 'date26'
            t_3423 = date_8839(2024, 12, 25)
            date_1219: 'date26' = t_3423
            t_6975: 'SqlBuilder' = SqlBuilder()
            t_6975.append_safe('insert into t values (')
            t_6975.append_date(date_1219)
            t_6975.append_safe(')')
            actual_1530: 'str27' = t_6975.accumulated.to_string()
            t_6982: 'bool33' = actual_1530 == "insert into t values ('2024-12-25')"
            def fn_6957() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_1530, ')')
            test_130.assert_(t_6982, fn_6957)
        finally:
            test_130.soft_fail_to_hard()
class TestCase144(TestCase46):
    def test___lists__1533(self) -> None:
        'lists'
        test_131: Test = Test()
        try:
            t_6903: 'SqlBuilder' = SqlBuilder()
            t_6903.append_safe('v IN (')
            t_6903.append_string_list(('a', 'b', "c'd"))
            t_6903.append_safe(')')
            actual_1534: 'str27' = t_6903.accumulated.to_string()
            t_6910: 'bool33' = actual_1534 == "v IN ('a', 'b', 'c''d')"
            def fn_6902() -> 'str27':
                return str_cat_8814("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_1534, ')')
            test_131.assert_(t_6910, fn_6902)
            t_6912: 'SqlBuilder' = SqlBuilder()
            t_6912.append_safe('v IN (')
            t_6912.append_int32_list((1, 2, 3))
            t_6912.append_safe(')')
            actual_1537: 'str27' = t_6912.accumulated.to_string()
            t_6919: 'bool33' = actual_1537 == 'v IN (1, 2, 3)'
            def fn_6901() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_1537, ')')
            test_131.assert_(t_6919, fn_6901)
            t_6921: 'SqlBuilder' = SqlBuilder()
            t_6921.append_safe('v IN (')
            t_6921.append_int64_list((1, 2))
            t_6921.append_safe(')')
            actual_1540: 'str27' = t_6921.accumulated.to_string()
            t_6928: 'bool33' = actual_1540 == 'v IN (1, 2)'
            def fn_6900() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_1540, ')')
            test_131.assert_(t_6928, fn_6900)
            t_6930: 'SqlBuilder' = SqlBuilder()
            t_6930.append_safe('v IN (')
            t_6930.append_float64_list((1.0, 2.0))
            t_6930.append_safe(')')
            actual_1543: 'str27' = t_6930.accumulated.to_string()
            t_6937: 'bool33' = actual_1543 == 'v IN (1.0, 2.0)'
            def fn_6899() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_1543, ')')
            test_131.assert_(t_6937, fn_6899)
            t_6939: 'SqlBuilder' = SqlBuilder()
            t_6939.append_safe('v IN (')
            t_6939.append_boolean_list((True, False))
            t_6939.append_safe(')')
            actual_1546: 'str27' = t_6939.accumulated.to_string()
            t_6946: 'bool33' = actual_1546 == 'v IN (TRUE, FALSE)'
            def fn_6898() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_1546, ')')
            test_131.assert_(t_6946, fn_6898)
            t_3395: 'date26'
            t_3395 = date_8839(2024, 1, 1)
            t_3396: 'date26' = t_3395
            t_3397: 'date26'
            t_3397 = date_8839(2024, 12, 25)
            t_3398: 'date26' = t_3397
            dates_1221: 'Sequence29[date26]' = (t_3396, t_3398)
            t_6948: 'SqlBuilder' = SqlBuilder()
            t_6948.append_safe('v IN (')
            t_6948.append_date_list(dates_1221)
            t_6948.append_safe(')')
            actual_1549: 'str27' = t_6948.accumulated.to_string()
            t_6955: 'bool33' = actual_1549 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_6897() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_1549, ')')
            test_131.assert_(t_6955, fn_6897)
        finally:
            test_131.soft_fail_to_hard()
class TestCase145(TestCase46):
    def test___sqlFloat64_naNRendersAsNull__1552(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_132: Test = Test()
        try:
            nan_1223: 'float38'
            nan_1223 = 0.0 / 0.0
            t_6889: 'SqlBuilder' = SqlBuilder()
            t_6889.append_safe('v = ')
            t_6889.append_float64(nan_1223)
            actual_1553: 'str27' = t_6889.accumulated.to_string()
            t_6895: 'bool33' = actual_1553 == 'v = NULL'
            def fn_6888() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_1553, ')')
            test_132.assert_(t_6895, fn_6888)
        finally:
            test_132.soft_fail_to_hard()
class TestCase146(TestCase46):
    def test___sqlFloat64_infinityRendersAsNull__1556(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_133: Test = Test()
        try:
            inf_1225: 'float38'
            inf_1225 = 1.0 / 0.0
            t_6880: 'SqlBuilder' = SqlBuilder()
            t_6880.append_safe('v = ')
            t_6880.append_float64(inf_1225)
            actual_1557: 'str27' = t_6880.accumulated.to_string()
            t_6886: 'bool33' = actual_1557 == 'v = NULL'
            def fn_6879() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_1557, ')')
            test_133.assert_(t_6886, fn_6879)
        finally:
            test_133.soft_fail_to_hard()
class TestCase147(TestCase46):
    def test___sqlFloat64_negativeInfinityRendersAsNull__1560(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_134: Test = Test()
        try:
            ninf_1227: 'float38'
            ninf_1227 = -1.0 / 0.0
            t_6871: 'SqlBuilder' = SqlBuilder()
            t_6871.append_safe('v = ')
            t_6871.append_float64(ninf_1227)
            actual_1561: 'str27' = t_6871.accumulated.to_string()
            t_6877: 'bool33' = actual_1561 == 'v = NULL'
            def fn_6870() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_1561, ')')
            test_134.assert_(t_6877, fn_6870)
        finally:
            test_134.soft_fail_to_hard()
class TestCase148(TestCase46):
    def test___sqlFloat64_normalValuesStillWork__1564(self) -> None:
        'SqlFloat64 normal values still work'
        test_135: Test = Test()
        try:
            t_6846: 'SqlBuilder' = SqlBuilder()
            t_6846.append_safe('v = ')
            t_6846.append_float64(3.14)
            actual_1565: 'str27' = t_6846.accumulated.to_string()
            t_6852: 'bool33' = actual_1565 == 'v = 3.14'
            def fn_6845() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_1565, ')')
            test_135.assert_(t_6852, fn_6845)
            t_6854: 'SqlBuilder' = SqlBuilder()
            t_6854.append_safe('v = ')
            t_6854.append_float64(0.0)
            actual_1568: 'str27' = t_6854.accumulated.to_string()
            t_6860: 'bool33' = actual_1568 == 'v = 0.0'
            def fn_6844() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_1568, ')')
            test_135.assert_(t_6860, fn_6844)
            t_6862: 'SqlBuilder' = SqlBuilder()
            t_6862.append_safe('v = ')
            t_6862.append_float64(-42.5)
            actual_1571: 'str27' = t_6862.accumulated.to_string()
            t_6868: 'bool33' = actual_1571 == 'v = -42.5'
            def fn_6843() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_1571, ')')
            test_135.assert_(t_6868, fn_6843)
        finally:
            test_135.soft_fail_to_hard()
class TestCase149(TestCase46):
    def test___sqlDateRendersWithQuotes__1574(self) -> None:
        'SqlDate renders with quotes'
        test_136: Test = Test()
        try:
            t_3291: 'date26'
            t_3291 = date_8839(2024, 6, 15)
            d_1230: 'date26' = t_3291
            t_6835: 'SqlBuilder' = SqlBuilder()
            t_6835.append_safe('v = ')
            t_6835.append_date(d_1230)
            actual_1575: 'str27' = t_6835.accumulated.to_string()
            t_6841: 'bool33' = actual_1575 == "v = '2024-06-15'"
            def fn_6834() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_1575, ')')
            test_136.assert_(t_6841, fn_6834)
        finally:
            test_136.soft_fail_to_hard()
class TestCase150(TestCase46):
    def test___nesting__1578(self) -> None:
        'nesting'
        test_137: Test = Test()
        try:
            name_1232: 'str27' = 'Someone'
            t_6803: 'SqlBuilder' = SqlBuilder()
            t_6803.append_safe('where p.last_name = ')
            t_6803.append_string('Someone')
            condition_1233: 'SqlFragment' = t_6803.accumulated
            t_6807: 'SqlBuilder' = SqlBuilder()
            t_6807.append_safe('select p.id from person p ')
            t_6807.append_fragment(condition_1233)
            actual_1580: 'str27' = t_6807.accumulated.to_string()
            t_6813: 'bool33' = actual_1580 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_6802() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1580, ')')
            test_137.assert_(t_6813, fn_6802)
            t_6815: 'SqlBuilder' = SqlBuilder()
            t_6815.append_safe('select p.id from person p ')
            t_6815.append_part(condition_1233.to_source())
            actual_1583: 'str27' = t_6815.accumulated.to_string()
            t_6822: 'bool33' = actual_1583 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_6801() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1583, ')')
            test_137.assert_(t_6822, fn_6801)
            parts_1234: 'Sequence29[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_6826: 'SqlBuilder' = SqlBuilder()
            t_6826.append_safe('select ')
            t_6826.append_part_list(parts_1234)
            actual_1586: 'str27' = t_6826.accumulated.to_string()
            t_6832: 'bool33' = actual_1586 == "select 'a''b', 3"
            def fn_6800() -> 'str27':
                return str_cat_8814('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_1586, ')')
            test_137.assert_(t_6832, fn_6800)
        finally:
            test_137.soft_fail_to_hard()
