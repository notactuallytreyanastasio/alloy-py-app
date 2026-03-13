from temper_std.testing import Test
from builtins import str as str27, bool as bool33, Exception as Exception37, int as int31, float as float38
from unittest import TestCase as TestCase46
from types import MappingProxyType as MappingProxyType32
from typing import Sequence as Sequence29
from datetime import date as date26
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_5823, pair_5827, changeset, Changeset, mapped_has_5800, len_5803, list_get_5811, str_cat_5805, list_for_each_5797, SqlFragment, from_, Query, SqlBuilder, col, date_5830, SqlString, SqlInt32, SqlPart
def csid_342(name_487: 'str27') -> 'SafeIdentifier':
    t_3188: 'SafeIdentifier'
    t_3188 = safe_identifier(name_487)
    return t_3188
def user_table_343() -> 'TableDef':
    return TableDef(csid_342('users'), (FieldDef(csid_342('name'), StringField(), False), FieldDef(csid_342('email'), StringField(), False), FieldDef(csid_342('age'), IntField(), True), FieldDef(csid_342('score'), FloatField(), True), FieldDef(csid_342('active'), BoolField(), True)))
class TestCase45(TestCase46):
    def test___castWhitelistsAllowedFields__1020(self) -> None:
        'cast whitelists allowed fields'
        test_22: Test = Test()
        try:
            params_491: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'Alice'), pair_5827('email', 'alice@example.com'), pair_5827('admin', 'true')))
            t_5514: 'TableDef' = user_table_343()
            t_5515: 'SafeIdentifier' = csid_342('name')
            t_5516: 'SafeIdentifier' = csid_342('email')
            cs_492: 'Changeset' = changeset(t_5514, params_491).cast((t_5515, t_5516))
            t_5519: 'bool33' = mapped_has_5800(cs_492.changes, 'name')
            def fn_5509() -> 'str27':
                return 'name should be in changes'
            test_22.assert_(t_5519, fn_5509)
            t_5523: 'bool33' = mapped_has_5800(cs_492.changes, 'email')
            def fn_5508() -> 'str27':
                return 'email should be in changes'
            test_22.assert_(t_5523, fn_5508)
            t_5529: 'bool33' = not mapped_has_5800(cs_492.changes, 'admin')
            def fn_5507() -> 'str27':
                return 'admin must be dropped (not in whitelist)'
            test_22.assert_(t_5529, fn_5507)
            t_5531: 'bool33' = cs_492.is_valid
            def fn_5506() -> 'str27':
                return 'should still be valid'
            test_22.assert_(t_5531, fn_5506)
        finally:
            test_22.soft_fail_to_hard()
class TestCase47(TestCase46):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__1021(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_23: Test = Test()
        try:
            params_494: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'Alice'), pair_5827('email', 'alice@example.com')))
            t_5492: 'TableDef' = user_table_343()
            t_5493: 'SafeIdentifier' = csid_342('name')
            cs_495: 'Changeset' = changeset(t_5492, params_494).cast((t_5493,)).cast((csid_342('email'),))
            t_5500: 'bool33' = not mapped_has_5800(cs_495.changes, 'name')
            def fn_5488() -> 'str27':
                return 'name must be excluded by second cast'
            test_23.assert_(t_5500, fn_5488)
            t_5503: 'bool33' = mapped_has_5800(cs_495.changes, 'email')
            def fn_5487() -> 'str27':
                return 'email should be present'
            test_23.assert_(t_5503, fn_5487)
        finally:
            test_23.soft_fail_to_hard()
class TestCase48(TestCase46):
    def test___castIgnoresEmptyStringValues__1022(self) -> None:
        'cast ignores empty string values'
        test_24: Test = Test()
        try:
            params_497: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', ''), pair_5827('email', 'bob@example.com')))
            t_5474: 'TableDef' = user_table_343()
            t_5475: 'SafeIdentifier' = csid_342('name')
            t_5476: 'SafeIdentifier' = csid_342('email')
            cs_498: 'Changeset' = changeset(t_5474, params_497).cast((t_5475, t_5476))
            t_5481: 'bool33' = not mapped_has_5800(cs_498.changes, 'name')
            def fn_5470() -> 'str27':
                return 'empty name should not be in changes'
            test_24.assert_(t_5481, fn_5470)
            t_5484: 'bool33' = mapped_has_5800(cs_498.changes, 'email')
            def fn_5469() -> 'str27':
                return 'email should be in changes'
            test_24.assert_(t_5484, fn_5469)
        finally:
            test_24.soft_fail_to_hard()
class TestCase49(TestCase46):
    def test___validateRequiredPassesWhenFieldPresent__1023(self) -> None:
        'validateRequired passes when field present'
        test_25: Test = Test()
        try:
            params_500: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'Alice'),))
            t_5456: 'TableDef' = user_table_343()
            t_5457: 'SafeIdentifier' = csid_342('name')
            cs_501: 'Changeset' = changeset(t_5456, params_500).cast((t_5457,)).validate_required((csid_342('name'),))
            t_5461: 'bool33' = cs_501.is_valid
            def fn_5453() -> 'str27':
                return 'should be valid'
            test_25.assert_(t_5461, fn_5453)
            t_5467: 'bool33' = len_5803(cs_501.errors) == 0
            def fn_5452() -> 'str27':
                return 'no errors expected'
            test_25.assert_(t_5467, fn_5452)
        finally:
            test_25.soft_fail_to_hard()
class TestCase50(TestCase46):
    def test___validateRequiredFailsWhenFieldMissing__1024(self) -> None:
        'validateRequired fails when field missing'
        test_26: Test = Test()
        try:
            params_503: 'MappingProxyType32[str27, str27]' = map_constructor_5823(())
            t_5432: 'TableDef' = user_table_343()
            t_5433: 'SafeIdentifier' = csid_342('name')
            cs_504: 'Changeset' = changeset(t_5432, params_503).cast((t_5433,)).validate_required((csid_342('name'),))
            t_5439: 'bool33' = not cs_504.is_valid
            def fn_5430() -> 'str27':
                return 'should be invalid'
            test_26.assert_(t_5439, fn_5430)
            t_5444: 'bool33' = len_5803(cs_504.errors) == 1
            def fn_5429() -> 'str27':
                return 'should have one error'
            test_26.assert_(t_5444, fn_5429)
            t_5450: 'bool33' = list_get_5811(cs_504.errors, 0).field == 'name'
            def fn_5428() -> 'str27':
                return 'error should name the field'
            test_26.assert_(t_5450, fn_5428)
        finally:
            test_26.soft_fail_to_hard()
class TestCase51(TestCase46):
    def test___validateLengthPassesWithinRange__1025(self) -> None:
        'validateLength passes within range'
        test_27: Test = Test()
        try:
            params_506: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'Alice'),))
            t_5420: 'TableDef' = user_table_343()
            t_5421: 'SafeIdentifier' = csid_342('name')
            cs_507: 'Changeset' = changeset(t_5420, params_506).cast((t_5421,)).validate_length(csid_342('name'), 2, 50)
            t_5425: 'bool33' = cs_507.is_valid
            def fn_5417() -> 'str27':
                return 'should be valid'
            test_27.assert_(t_5425, fn_5417)
        finally:
            test_27.soft_fail_to_hard()
class TestCase52(TestCase46):
    def test___validateLengthFailsWhenTooShort__1026(self) -> None:
        'validateLength fails when too short'
        test_28: Test = Test()
        try:
            params_509: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'A'),))
            t_5408: 'TableDef' = user_table_343()
            t_5409: 'SafeIdentifier' = csid_342('name')
            cs_510: 'Changeset' = changeset(t_5408, params_509).cast((t_5409,)).validate_length(csid_342('name'), 2, 50)
            t_5415: 'bool33' = not cs_510.is_valid
            def fn_5405() -> 'str27':
                return 'should be invalid'
            test_28.assert_(t_5415, fn_5405)
        finally:
            test_28.soft_fail_to_hard()
class TestCase53(TestCase46):
    def test___validateLengthFailsWhenTooLong__1027(self) -> None:
        'validateLength fails when too long'
        test_29: Test = Test()
        try:
            params_512: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_5396: 'TableDef' = user_table_343()
            t_5397: 'SafeIdentifier' = csid_342('name')
            cs_513: 'Changeset' = changeset(t_5396, params_512).cast((t_5397,)).validate_length(csid_342('name'), 2, 10)
            t_5403: 'bool33' = not cs_513.is_valid
            def fn_5393() -> 'str27':
                return 'should be invalid'
            test_29.assert_(t_5403, fn_5393)
        finally:
            test_29.soft_fail_to_hard()
class TestCase54(TestCase46):
    def test___validateIntPassesForValidInteger__1028(self) -> None:
        'validateInt passes for valid integer'
        test_30: Test = Test()
        try:
            params_515: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('age', '30'),))
            t_5385: 'TableDef' = user_table_343()
            t_5386: 'SafeIdentifier' = csid_342('age')
            cs_516: 'Changeset' = changeset(t_5385, params_515).cast((t_5386,)).validate_int(csid_342('age'))
            t_5390: 'bool33' = cs_516.is_valid
            def fn_5382() -> 'str27':
                return 'should be valid'
            test_30.assert_(t_5390, fn_5382)
        finally:
            test_30.soft_fail_to_hard()
class TestCase55(TestCase46):
    def test___validateIntFailsForNonInteger__1029(self) -> None:
        'validateInt fails for non-integer'
        test_31: Test = Test()
        try:
            params_518: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('age', 'not-a-number'),))
            t_5373: 'TableDef' = user_table_343()
            t_5374: 'SafeIdentifier' = csid_342('age')
            cs_519: 'Changeset' = changeset(t_5373, params_518).cast((t_5374,)).validate_int(csid_342('age'))
            t_5380: 'bool33' = not cs_519.is_valid
            def fn_5370() -> 'str27':
                return 'should be invalid'
            test_31.assert_(t_5380, fn_5370)
        finally:
            test_31.soft_fail_to_hard()
class TestCase56(TestCase46):
    def test___validateFloatPassesForValidFloat__1030(self) -> None:
        'validateFloat passes for valid float'
        test_32: Test = Test()
        try:
            params_521: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('score', '9.5'),))
            t_5362: 'TableDef' = user_table_343()
            t_5363: 'SafeIdentifier' = csid_342('score')
            cs_522: 'Changeset' = changeset(t_5362, params_521).cast((t_5363,)).validate_float(csid_342('score'))
            t_5367: 'bool33' = cs_522.is_valid
            def fn_5359() -> 'str27':
                return 'should be valid'
            test_32.assert_(t_5367, fn_5359)
        finally:
            test_32.soft_fail_to_hard()
class TestCase57(TestCase46):
    def test___validateInt64_passesForValid64_bitInteger__1031(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_33: Test = Test()
        try:
            params_524: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('age', '9999999999'),))
            t_5351: 'TableDef' = user_table_343()
            t_5352: 'SafeIdentifier' = csid_342('age')
            cs_525: 'Changeset' = changeset(t_5351, params_524).cast((t_5352,)).validate_int64(csid_342('age'))
            t_5356: 'bool33' = cs_525.is_valid
            def fn_5348() -> 'str27':
                return 'should be valid'
            test_33.assert_(t_5356, fn_5348)
        finally:
            test_33.soft_fail_to_hard()
class TestCase58(TestCase46):
    def test___validateInt64_failsForNonInteger__1032(self) -> None:
        'validateInt64 fails for non-integer'
        test_34: Test = Test()
        try:
            params_527: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('age', 'not-a-number'),))
            t_5339: 'TableDef' = user_table_343()
            t_5340: 'SafeIdentifier' = csid_342('age')
            cs_528: 'Changeset' = changeset(t_5339, params_527).cast((t_5340,)).validate_int64(csid_342('age'))
            t_5346: 'bool33' = not cs_528.is_valid
            def fn_5336() -> 'str27':
                return 'should be invalid'
            test_34.assert_(t_5346, fn_5336)
        finally:
            test_34.soft_fail_to_hard()
class TestCase59(TestCase46):
    def test___validateBoolAcceptsTrue1_yesOn__1033(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_35: Test = Test()
        try:
            def fn_5333(v_530: 'str27') -> 'None':
                params_531: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('active', v_530),))
                t_5325: 'TableDef' = user_table_343()
                t_5326: 'SafeIdentifier' = csid_342('active')
                cs_532: 'Changeset' = changeset(t_5325, params_531).cast((t_5326,)).validate_bool(csid_342('active'))
                t_5330: 'bool33' = cs_532.is_valid
                def fn_5322() -> 'str27':
                    return str_cat_5805('should accept: ', v_530)
                test_35.assert_(t_5330, fn_5322)
            list_for_each_5797(('true', '1', 'yes', 'on'), fn_5333)
        finally:
            test_35.soft_fail_to_hard()
class TestCase60(TestCase46):
    def test___validateBoolAcceptsFalse0_noOff__1034(self) -> None:
        'validateBool accepts false/0/no/off'
        test_36: Test = Test()
        try:
            def fn_5319(v_534: 'str27') -> 'None':
                params_535: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('active', v_534),))
                t_5311: 'TableDef' = user_table_343()
                t_5312: 'SafeIdentifier' = csid_342('active')
                cs_536: 'Changeset' = changeset(t_5311, params_535).cast((t_5312,)).validate_bool(csid_342('active'))
                t_5316: 'bool33' = cs_536.is_valid
                def fn_5308() -> 'str27':
                    return str_cat_5805('should accept: ', v_534)
                test_36.assert_(t_5316, fn_5308)
            list_for_each_5797(('false', '0', 'no', 'off'), fn_5319)
        finally:
            test_36.soft_fail_to_hard()
class TestCase61(TestCase46):
    def test___validateBoolRejectsAmbiguousValues__1035(self) -> None:
        'validateBool rejects ambiguous values'
        test_37: Test = Test()
        try:
            def fn_5305(v_538: 'str27') -> 'None':
                params_539: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('active', v_538),))
                t_5296: 'TableDef' = user_table_343()
                t_5297: 'SafeIdentifier' = csid_342('active')
                cs_540: 'Changeset' = changeset(t_5296, params_539).cast((t_5297,)).validate_bool(csid_342('active'))
                t_5303: 'bool33' = not cs_540.is_valid
                def fn_5293() -> 'str27':
                    return str_cat_5805('should reject ambiguous: ', v_538)
                test_37.assert_(t_5303, fn_5293)
            list_for_each_5797(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_5305)
        finally:
            test_37.soft_fail_to_hard()
class TestCase62(TestCase46):
    def test___toInsertSqlEscapesBobbyTables__1036(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_38: Test = Test()
        try:
            params_542: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', "Robert'); DROP TABLE users;--"), pair_5827('email', 'bobby@evil.com')))
            t_5281: 'TableDef' = user_table_343()
            t_5282: 'SafeIdentifier' = csid_342('name')
            t_5283: 'SafeIdentifier' = csid_342('email')
            cs_543: 'Changeset' = changeset(t_5281, params_542).cast((t_5282, t_5283)).validate_required((csid_342('name'), csid_342('email')))
            t_2989: 'SqlFragment'
            t_2989 = cs_543.to_insert_sql()
            sql_frag_544: 'SqlFragment' = t_2989
            s_545: 'str27' = sql_frag_544.to_string()
            t_5290: 'bool33' = s_545.find("''") >= 0
            def fn_5277() -> 'str27':
                return str_cat_5805('single quote must be doubled: ', s_545)
            test_38.assert_(t_5290, fn_5277)
        finally:
            test_38.soft_fail_to_hard()
class TestCase63(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForStringField__1037(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_39: Test = Test()
        try:
            params_547: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'Alice'), pair_5827('email', 'a@example.com')))
            t_5261: 'TableDef' = user_table_343()
            t_5262: 'SafeIdentifier' = csid_342('name')
            t_5263: 'SafeIdentifier' = csid_342('email')
            cs_548: 'Changeset' = changeset(t_5261, params_547).cast((t_5262, t_5263)).validate_required((csid_342('name'), csid_342('email')))
            t_2968: 'SqlFragment'
            t_2968 = cs_548.to_insert_sql()
            sql_frag_549: 'SqlFragment' = t_2968
            s_550: 'str27' = sql_frag_549.to_string()
            t_5270: 'bool33' = s_550.find('INSERT INTO users') >= 0
            def fn_5257() -> 'str27':
                return str_cat_5805('has INSERT INTO: ', s_550)
            test_39.assert_(t_5270, fn_5257)
            t_5274: 'bool33' = s_550.find("'Alice'") >= 0
            def fn_5256() -> 'str27':
                return str_cat_5805('has quoted name: ', s_550)
            test_39.assert_(t_5274, fn_5256)
        finally:
            test_39.soft_fail_to_hard()
class TestCase64(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForIntField__1038(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_40: Test = Test()
        try:
            params_552: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'Bob'), pair_5827('email', 'b@example.com'), pair_5827('age', '25')))
            t_5243: 'TableDef' = user_table_343()
            t_5244: 'SafeIdentifier' = csid_342('name')
            t_5245: 'SafeIdentifier' = csid_342('email')
            t_5246: 'SafeIdentifier' = csid_342('age')
            cs_553: 'Changeset' = changeset(t_5243, params_552).cast((t_5244, t_5245, t_5246)).validate_required((csid_342('name'), csid_342('email')))
            t_2951: 'SqlFragment'
            t_2951 = cs_553.to_insert_sql()
            sql_frag_554: 'SqlFragment' = t_2951
            s_555: 'str27' = sql_frag_554.to_string()
            t_5253: 'bool33' = s_555.find('25') >= 0
            def fn_5238() -> 'str27':
                return str_cat_5805('age rendered unquoted: ', s_555)
            test_40.assert_(t_5253, fn_5238)
        finally:
            test_40.soft_fail_to_hard()
class TestCase65(TestCase46):
    def test___toInsertSqlBubblesOnInvalidChangeset__1039(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_41: Test = Test()
        try:
            params_557: 'MappingProxyType32[str27, str27]' = map_constructor_5823(())
            t_5231: 'TableDef' = user_table_343()
            t_5232: 'SafeIdentifier' = csid_342('name')
            cs_558: 'Changeset' = changeset(t_5231, params_557).cast((t_5232,)).validate_required((csid_342('name'),))
            did_bubble_559: 'bool33'
            try:
                cs_558.to_insert_sql()
                did_bubble_559 = False
            except Exception37:
                did_bubble_559 = True
            def fn_5229() -> 'str27':
                return 'invalid changeset should bubble'
            test_41.assert_(did_bubble_559, fn_5229)
        finally:
            test_41.soft_fail_to_hard()
class TestCase66(TestCase46):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__1040(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_42: Test = Test()
        try:
            strict_table_561: 'TableDef' = TableDef(csid_342('posts'), (FieldDef(csid_342('title'), StringField(), False), FieldDef(csid_342('body'), StringField(), True)))
            params_562: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('body', 'hello'),))
            t_5222: 'SafeIdentifier' = csid_342('body')
            cs_563: 'Changeset' = changeset(strict_table_561, params_562).cast((t_5222,))
            t_5224: 'bool33' = cs_563.is_valid
            def fn_5211() -> 'str27':
                return 'changeset should appear valid (no explicit validation run)'
            test_42.assert_(t_5224, fn_5211)
            did_bubble_564: 'bool33'
            try:
                cs_563.to_insert_sql()
                did_bubble_564 = False
            except Exception37:
                did_bubble_564 = True
            def fn_5210() -> 'str27':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_42.assert_(did_bubble_564, fn_5210)
        finally:
            test_42.soft_fail_to_hard()
class TestCase67(TestCase46):
    def test___toUpdateSqlProducesCorrectSql__1041(self) -> None:
        'toUpdateSql produces correct SQL'
        test_43: Test = Test()
        try:
            params_566: 'MappingProxyType32[str27, str27]' = map_constructor_5823((pair_5827('name', 'Bob'),))
            t_5201: 'TableDef' = user_table_343()
            t_5202: 'SafeIdentifier' = csid_342('name')
            cs_567: 'Changeset' = changeset(t_5201, params_566).cast((t_5202,)).validate_required((csid_342('name'),))
            t_2911: 'SqlFragment'
            t_2911 = cs_567.to_update_sql(42)
            sql_frag_568: 'SqlFragment' = t_2911
            s_569: 'str27' = sql_frag_568.to_string()
            t_5208: 'bool33' = s_569 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_5198() -> 'str27':
                return str_cat_5805('got: ', s_569)
            test_43.assert_(t_5208, fn_5198)
        finally:
            test_43.soft_fail_to_hard()
class TestCase68(TestCase46):
    def test___toUpdateSqlBubblesOnInvalidChangeset__1042(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_44: Test = Test()
        try:
            params_571: 'MappingProxyType32[str27, str27]' = map_constructor_5823(())
            t_5191: 'TableDef' = user_table_343()
            t_5192: 'SafeIdentifier' = csid_342('name')
            cs_572: 'Changeset' = changeset(t_5191, params_571).cast((t_5192,)).validate_required((csid_342('name'),))
            did_bubble_573: 'bool33'
            try:
                cs_572.to_update_sql(1)
                did_bubble_573 = False
            except Exception37:
                did_bubble_573 = True
            def fn_5189() -> 'str27':
                return 'invalid changeset should bubble'
            test_44.assert_(did_bubble_573, fn_5189)
        finally:
            test_44.soft_fail_to_hard()
def sid_344(name_678: 'str27') -> 'SafeIdentifier':
    t_2781: 'SafeIdentifier'
    t_2781 = safe_identifier(name_678)
    return t_2781
class TestCase69(TestCase46):
    def test___bareFromProducesSelect__1079(self) -> None:
        'bare from produces SELECT *'
        test_45: Test = Test()
        try:
            q_681: 'Query' = from_(sid_344('users'))
            t_5084: 'bool33' = q_681.to_sql().to_string() == 'SELECT * FROM users'
            def fn_5079() -> 'str27':
                return 'bare query'
            test_45.assert_(t_5084, fn_5079)
        finally:
            test_45.soft_fail_to_hard()
class TestCase70(TestCase46):
    def test___selectRestrictsColumns__1080(self) -> None:
        'select restricts columns'
        test_46: Test = Test()
        try:
            t_5070: 'SafeIdentifier' = sid_344('users')
            t_5071: 'SafeIdentifier' = sid_344('id')
            t_5072: 'SafeIdentifier' = sid_344('name')
            q_683: 'Query' = from_(t_5070).select((t_5071, t_5072))
            t_5077: 'bool33' = q_683.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_5069() -> 'str27':
                return 'select columns'
            test_46.assert_(t_5077, fn_5069)
        finally:
            test_46.soft_fail_to_hard()
class TestCase71(TestCase46):
    def test___whereAddsConditionWithIntValue__1081(self) -> None:
        'where adds condition with int value'
        test_47: Test = Test()
        try:
            t_5058: 'SafeIdentifier' = sid_344('users')
            t_5059: 'SqlBuilder' = SqlBuilder()
            t_5059.append_safe('age > ')
            t_5059.append_int32(18)
            t_5062: 'SqlFragment' = t_5059.accumulated
            q_685: 'Query' = from_(t_5058).where(t_5062)
            t_5067: 'bool33' = q_685.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_5057() -> 'str27':
                return 'where int'
            test_47.assert_(t_5067, fn_5057)
        finally:
            test_47.soft_fail_to_hard()
class TestCase72(TestCase46):
    def test___whereAddsConditionWithBoolValue__1083(self) -> None:
        'where adds condition with bool value'
        test_48: Test = Test()
        try:
            t_5046: 'SafeIdentifier' = sid_344('users')
            t_5047: 'SqlBuilder' = SqlBuilder()
            t_5047.append_safe('active = ')
            t_5047.append_boolean(True)
            t_5050: 'SqlFragment' = t_5047.accumulated
            q_687: 'Query' = from_(t_5046).where(t_5050)
            t_5055: 'bool33' = q_687.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_5045() -> 'str27':
                return 'where bool'
            test_48.assert_(t_5055, fn_5045)
        finally:
            test_48.soft_fail_to_hard()
class TestCase73(TestCase46):
    def test___chainedWhereUsesAnd__1085(self) -> None:
        'chained where uses AND'
        test_49: Test = Test()
        try:
            t_5029: 'SafeIdentifier' = sid_344('users')
            t_5030: 'SqlBuilder' = SqlBuilder()
            t_5030.append_safe('age > ')
            t_5030.append_int32(18)
            t_5033: 'SqlFragment' = t_5030.accumulated
            t_5034: 'Query' = from_(t_5029).where(t_5033)
            t_5035: 'SqlBuilder' = SqlBuilder()
            t_5035.append_safe('active = ')
            t_5035.append_boolean(True)
            q_689: 'Query' = t_5034.where(t_5035.accumulated)
            t_5043: 'bool33' = q_689.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_5028() -> 'str27':
                return 'chained where'
            test_49.assert_(t_5043, fn_5028)
        finally:
            test_49.soft_fail_to_hard()
class TestCase74(TestCase46):
    def test___orderByAsc__1088(self) -> None:
        'orderBy ASC'
        test_50: Test = Test()
        try:
            t_5020: 'SafeIdentifier' = sid_344('users')
            t_5021: 'SafeIdentifier' = sid_344('name')
            q_691: 'Query' = from_(t_5020).order_by(t_5021, True)
            t_5026: 'bool33' = q_691.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_5019() -> 'str27':
                return 'order asc'
            test_50.assert_(t_5026, fn_5019)
        finally:
            test_50.soft_fail_to_hard()
class TestCase75(TestCase46):
    def test___orderByDesc__1089(self) -> None:
        'orderBy DESC'
        test_51: Test = Test()
        try:
            t_5011: 'SafeIdentifier' = sid_344('users')
            t_5012: 'SafeIdentifier' = sid_344('created_at')
            q_693: 'Query' = from_(t_5011).order_by(t_5012, False)
            t_5017: 'bool33' = q_693.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_5010() -> 'str27':
                return 'order desc'
            test_51.assert_(t_5017, fn_5010)
        finally:
            test_51.soft_fail_to_hard()
class TestCase76(TestCase46):
    def test___limitAndOffset__1090(self) -> None:
        'limit and offset'
        test_52: Test = Test()
        try:
            t_2715: 'Query'
            t_2715 = from_(sid_344('users')).limit(10)
            t_2716: 'Query'
            t_2716 = t_2715.offset(20)
            q_695: 'Query' = t_2716
            t_5008: 'bool33' = q_695.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_5003() -> 'str27':
                return 'limit/offset'
            test_52.assert_(t_5008, fn_5003)
        finally:
            test_52.soft_fail_to_hard()
class TestCase77(TestCase46):
    def test___limitBubblesOnNegative__1091(self) -> None:
        'limit bubbles on negative'
        test_53: Test = Test()
        try:
            did_bubble_697: 'bool33'
            try:
                from_(sid_344('users')).limit(-1)
                did_bubble_697 = False
            except Exception37:
                did_bubble_697 = True
            def fn_4999() -> 'str27':
                return 'negative limit should bubble'
            test_53.assert_(did_bubble_697, fn_4999)
        finally:
            test_53.soft_fail_to_hard()
class TestCase78(TestCase46):
    def test___offsetBubblesOnNegative__1092(self) -> None:
        'offset bubbles on negative'
        test_54: Test = Test()
        try:
            did_bubble_699: 'bool33'
            try:
                from_(sid_344('users')).offset(-1)
                did_bubble_699 = False
            except Exception37:
                did_bubble_699 = True
            def fn_4995() -> 'str27':
                return 'negative offset should bubble'
            test_54.assert_(did_bubble_699, fn_4995)
        finally:
            test_54.soft_fail_to_hard()
class TestCase79(TestCase46):
    def test___complexComposedQuery__1093(self) -> None:
        'complex composed query'
        test_55: Test = Test()
        try:
            min_age_701: 'int31' = 21
            t_4973: 'SafeIdentifier' = sid_344('users')
            t_4974: 'SafeIdentifier' = sid_344('id')
            t_4975: 'SafeIdentifier' = sid_344('name')
            t_4976: 'SafeIdentifier' = sid_344('email')
            t_4977: 'Query' = from_(t_4973).select((t_4974, t_4975, t_4976))
            t_4978: 'SqlBuilder' = SqlBuilder()
            t_4978.append_safe('age >= ')
            t_4978.append_int32(21)
            t_4982: 'Query' = t_4977.where(t_4978.accumulated)
            t_4983: 'SqlBuilder' = SqlBuilder()
            t_4983.append_safe('active = ')
            t_4983.append_boolean(True)
            t_2701: 'Query'
            t_2701 = t_4982.where(t_4983.accumulated).order_by(sid_344('name'), True).limit(25)
            t_2702: 'Query'
            t_2702 = t_2701.offset(0)
            q_702: 'Query' = t_2702
            t_4993: 'bool33' = q_702.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_4972() -> 'str27':
                return 'complex query'
            test_55.assert_(t_4993, fn_4972)
        finally:
            test_55.soft_fail_to_hard()
class TestCase80(TestCase46):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__1096(self) -> None:
        'safeToSql applies default limit when none set'
        test_56: Test = Test()
        try:
            q_704: 'Query' = from_(sid_344('users'))
            t_2678: 'SqlFragment'
            t_2678 = q_704.safe_to_sql(100)
            t_2679: 'SqlFragment' = t_2678
            s_705: 'str27' = t_2679.to_string()
            t_4970: 'bool33' = s_705 == 'SELECT * FROM users LIMIT 100'
            def fn_4966() -> 'str27':
                return str_cat_5805('should have limit: ', s_705)
            test_56.assert_(t_4970, fn_4966)
        finally:
            test_56.soft_fail_to_hard()
class TestCase81(TestCase46):
    def test___safeToSqlRespectsExplicitLimit__1097(self) -> None:
        'safeToSql respects explicit limit'
        test_57: Test = Test()
        try:
            t_2670: 'Query'
            t_2670 = from_(sid_344('users')).limit(5)
            q_707: 'Query' = t_2670
            t_2673: 'SqlFragment'
            t_2673 = q_707.safe_to_sql(100)
            t_2674: 'SqlFragment' = t_2673
            s_708: 'str27' = t_2674.to_string()
            t_4964: 'bool33' = s_708 == 'SELECT * FROM users LIMIT 5'
            def fn_4960() -> 'str27':
                return str_cat_5805('explicit limit preserved: ', s_708)
            test_57.assert_(t_4964, fn_4960)
        finally:
            test_57.soft_fail_to_hard()
class TestCase82(TestCase46):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__1098(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_58: Test = Test()
        try:
            did_bubble_710: 'bool33'
            try:
                from_(sid_344('users')).safe_to_sql(-1)
                did_bubble_710 = False
            except Exception37:
                did_bubble_710 = True
            def fn_4956() -> 'str27':
                return 'negative defaultLimit should bubble'
            test_58.assert_(did_bubble_710, fn_4956)
        finally:
            test_58.soft_fail_to_hard()
class TestCase83(TestCase46):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__1099(self) -> None:
        'where with injection attempt in string value is escaped'
        test_59: Test = Test()
        try:
            evil_712: 'str27' = "'; DROP TABLE users; --"
            t_4940: 'SafeIdentifier' = sid_344('users')
            t_4941: 'SqlBuilder' = SqlBuilder()
            t_4941.append_safe('name = ')
            t_4941.append_string("'; DROP TABLE users; --")
            t_4944: 'SqlFragment' = t_4941.accumulated
            q_713: 'Query' = from_(t_4940).where(t_4944)
            s_714: 'str27' = q_713.to_sql().to_string()
            t_4949: 'bool33' = s_714.find("''") >= 0
            def fn_4939() -> 'str27':
                return str_cat_5805('quotes must be doubled: ', s_714)
            test_59.assert_(t_4949, fn_4939)
            t_4953: 'bool33' = s_714.find('SELECT * FROM users WHERE name =') >= 0
            def fn_4938() -> 'str27':
                return str_cat_5805('structure intact: ', s_714)
            test_59.assert_(t_4953, fn_4938)
        finally:
            test_59.soft_fail_to_hard()
class TestCase84(TestCase46):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__1101(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_60: Test = Test()
        try:
            attack_716: 'str27' = 'users; DROP TABLE users; --'
            did_bubble_717: 'bool33'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_717 = False
            except Exception37:
                did_bubble_717 = True
            def fn_4935() -> 'str27':
                return 'metacharacter-containing name must be rejected at construction'
            test_60.assert_(did_bubble_717, fn_4935)
        finally:
            test_60.soft_fail_to_hard()
class TestCase85(TestCase46):
    def test___innerJoinProducesInnerJoin__1102(self) -> None:
        'innerJoin produces INNER JOIN'
        test_61: Test = Test()
        try:
            t_4924: 'SafeIdentifier' = sid_344('users')
            t_4925: 'SafeIdentifier' = sid_344('orders')
            t_4926: 'SqlBuilder' = SqlBuilder()
            t_4926.append_safe('users.id = orders.user_id')
            t_4928: 'SqlFragment' = t_4926.accumulated
            q_719: 'Query' = from_(t_4924).inner_join(t_4925, t_4928)
            t_4933: 'bool33' = q_719.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_4923() -> 'str27':
                return 'inner join'
            test_61.assert_(t_4933, fn_4923)
        finally:
            test_61.soft_fail_to_hard()
class TestCase86(TestCase46):
    def test___leftJoinProducesLeftJoin__1104(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_62: Test = Test()
        try:
            t_4912: 'SafeIdentifier' = sid_344('users')
            t_4913: 'SafeIdentifier' = sid_344('profiles')
            t_4914: 'SqlBuilder' = SqlBuilder()
            t_4914.append_safe('users.id = profiles.user_id')
            t_4916: 'SqlFragment' = t_4914.accumulated
            q_721: 'Query' = from_(t_4912).left_join(t_4913, t_4916)
            t_4921: 'bool33' = q_721.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_4911() -> 'str27':
                return 'left join'
            test_62.assert_(t_4921, fn_4911)
        finally:
            test_62.soft_fail_to_hard()
class TestCase87(TestCase46):
    def test___rightJoinProducesRightJoin__1106(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_63: Test = Test()
        try:
            t_4900: 'SafeIdentifier' = sid_344('orders')
            t_4901: 'SafeIdentifier' = sid_344('users')
            t_4902: 'SqlBuilder' = SqlBuilder()
            t_4902.append_safe('orders.user_id = users.id')
            t_4904: 'SqlFragment' = t_4902.accumulated
            q_723: 'Query' = from_(t_4900).right_join(t_4901, t_4904)
            t_4909: 'bool33' = q_723.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_4899() -> 'str27':
                return 'right join'
            test_63.assert_(t_4909, fn_4899)
        finally:
            test_63.soft_fail_to_hard()
class TestCase88(TestCase46):
    def test___fullJoinProducesFullOuterJoin__1108(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_64: Test = Test()
        try:
            t_4888: 'SafeIdentifier' = sid_344('users')
            t_4889: 'SafeIdentifier' = sid_344('orders')
            t_4890: 'SqlBuilder' = SqlBuilder()
            t_4890.append_safe('users.id = orders.user_id')
            t_4892: 'SqlFragment' = t_4890.accumulated
            q_725: 'Query' = from_(t_4888).full_join(t_4889, t_4892)
            t_4897: 'bool33' = q_725.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_4887() -> 'str27':
                return 'full join'
            test_64.assert_(t_4897, fn_4887)
        finally:
            test_64.soft_fail_to_hard()
class TestCase89(TestCase46):
    def test___chainedJoins__1110(self) -> None:
        'chained joins'
        test_65: Test = Test()
        try:
            t_4871: 'SafeIdentifier' = sid_344('users')
            t_4872: 'SafeIdentifier' = sid_344('orders')
            t_4873: 'SqlBuilder' = SqlBuilder()
            t_4873.append_safe('users.id = orders.user_id')
            t_4875: 'SqlFragment' = t_4873.accumulated
            t_4876: 'Query' = from_(t_4871).inner_join(t_4872, t_4875)
            t_4877: 'SafeIdentifier' = sid_344('profiles')
            t_4878: 'SqlBuilder' = SqlBuilder()
            t_4878.append_safe('users.id = profiles.user_id')
            q_727: 'Query' = t_4876.left_join(t_4877, t_4878.accumulated)
            t_4885: 'bool33' = q_727.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_4870() -> 'str27':
                return 'chained joins'
            test_65.assert_(t_4885, fn_4870)
        finally:
            test_65.soft_fail_to_hard()
class TestCase90(TestCase46):
    def test___joinWithWhereAndOrderBy__1113(self) -> None:
        'join with where and orderBy'
        test_66: Test = Test()
        try:
            t_4852: 'SafeIdentifier' = sid_344('users')
            t_4853: 'SafeIdentifier' = sid_344('orders')
            t_4854: 'SqlBuilder' = SqlBuilder()
            t_4854.append_safe('users.id = orders.user_id')
            t_4856: 'SqlFragment' = t_4854.accumulated
            t_4857: 'Query' = from_(t_4852).inner_join(t_4853, t_4856)
            t_4858: 'SqlBuilder' = SqlBuilder()
            t_4858.append_safe('orders.total > ')
            t_4858.append_int32(100)
            t_2585: 'Query'
            t_2585 = t_4857.where(t_4858.accumulated).order_by(sid_344('name'), True).limit(10)
            q_729: 'Query' = t_2585
            t_4868: 'bool33' = q_729.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_4851() -> 'str27':
                return 'join with where/order/limit'
            test_66.assert_(t_4868, fn_4851)
        finally:
            test_66.soft_fail_to_hard()
class TestCase91(TestCase46):
    def test___colHelperProducesQualifiedReference__1116(self) -> None:
        'col helper produces qualified reference'
        test_67: Test = Test()
        try:
            c_731: 'SqlFragment' = col(sid_344('users'), sid_344('id'))
            t_4849: 'bool33' = c_731.to_string() == 'users.id'
            def fn_4843() -> 'str27':
                return 'col helper'
            test_67.assert_(t_4849, fn_4843)
        finally:
            test_67.soft_fail_to_hard()
class TestCase92(TestCase46):
    def test___joinWithColHelper__1117(self) -> None:
        'join with col helper'
        test_68: Test = Test()
        try:
            on_cond_733: 'SqlFragment' = col(sid_344('users'), sid_344('id'))
            b_734: 'SqlBuilder' = SqlBuilder()
            b_734.append_fragment(on_cond_733)
            b_734.append_safe(' = ')
            b_734.append_fragment(col(sid_344('orders'), sid_344('user_id')))
            t_4834: 'SafeIdentifier' = sid_344('users')
            t_4835: 'SafeIdentifier' = sid_344('orders')
            t_4836: 'SqlFragment' = b_734.accumulated
            q_735: 'Query' = from_(t_4834).inner_join(t_4835, t_4836)
            t_4841: 'bool33' = q_735.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_4823() -> 'str27':
                return 'join with col'
            test_68.assert_(t_4841, fn_4823)
        finally:
            test_68.soft_fail_to_hard()
class TestCase93(TestCase46):
    def test___safeIdentifierAcceptsValidNames__1118(self) -> None:
        'safeIdentifier accepts valid names'
        test_75: Test = Test()
        try:
            t_2544: 'SafeIdentifier'
            t_2544 = safe_identifier('user_name')
            id_773: 'SafeIdentifier' = t_2544
            t_4821: 'bool33' = id_773.sql_value == 'user_name'
            def fn_4818() -> 'str27':
                return 'value should round-trip'
            test_75.assert_(t_4821, fn_4818)
        finally:
            test_75.soft_fail_to_hard()
class TestCase94(TestCase46):
    def test___safeIdentifierRejectsEmptyString__1119(self) -> None:
        'safeIdentifier rejects empty string'
        test_76: Test = Test()
        try:
            did_bubble_775: 'bool33'
            try:
                safe_identifier('')
                did_bubble_775 = False
            except Exception37:
                did_bubble_775 = True
            def fn_4815() -> 'str27':
                return 'empty string should bubble'
            test_76.assert_(did_bubble_775, fn_4815)
        finally:
            test_76.soft_fail_to_hard()
class TestCase95(TestCase46):
    def test___safeIdentifierRejectsLeadingDigit__1120(self) -> None:
        'safeIdentifier rejects leading digit'
        test_77: Test = Test()
        try:
            did_bubble_777: 'bool33'
            try:
                safe_identifier('1col')
                did_bubble_777 = False
            except Exception37:
                did_bubble_777 = True
            def fn_4812() -> 'str27':
                return 'leading digit should bubble'
            test_77.assert_(did_bubble_777, fn_4812)
        finally:
            test_77.soft_fail_to_hard()
class TestCase96(TestCase46):
    def test___safeIdentifierRejectsSqlMetacharacters__1121(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_78: Test = Test()
        try:
            cases_779: 'Sequence29[str27]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_4809(c_780: 'str27') -> 'None':
                did_bubble_781: 'bool33'
                try:
                    safe_identifier(c_780)
                    did_bubble_781 = False
                except Exception37:
                    did_bubble_781 = True
                def fn_4806() -> 'str27':
                    return str_cat_5805('should reject: ', c_780)
                test_78.assert_(did_bubble_781, fn_4806)
            list_for_each_5797(cases_779, fn_4809)
        finally:
            test_78.soft_fail_to_hard()
class TestCase97(TestCase46):
    def test___tableDefFieldLookupFound__1122(self) -> None:
        'TableDef field lookup - found'
        test_79: Test = Test()
        try:
            t_2521: 'SafeIdentifier'
            t_2521 = safe_identifier('users')
            t_2522: 'SafeIdentifier' = t_2521
            t_2523: 'SafeIdentifier'
            t_2523 = safe_identifier('name')
            t_2524: 'SafeIdentifier' = t_2523
            t_4796: 'StringField' = StringField()
            t_4797: 'FieldDef' = FieldDef(t_2524, t_4796, False)
            t_2527: 'SafeIdentifier'
            t_2527 = safe_identifier('age')
            t_2528: 'SafeIdentifier' = t_2527
            t_4798: 'IntField' = IntField()
            t_4799: 'FieldDef' = FieldDef(t_2528, t_4798, False)
            td_783: 'TableDef' = TableDef(t_2522, (t_4797, t_4799))
            t_2532: 'FieldDef'
            t_2532 = td_783.field('age')
            f_784: 'FieldDef' = t_2532
            t_4804: 'bool33' = f_784.name.sql_value == 'age'
            def fn_4795() -> 'str27':
                return 'should find age field'
            test_79.assert_(t_4804, fn_4795)
        finally:
            test_79.soft_fail_to_hard()
class TestCase98(TestCase46):
    def test___tableDefFieldLookupNotFoundBubbles__1123(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_80: Test = Test()
        try:
            t_2512: 'SafeIdentifier'
            t_2512 = safe_identifier('users')
            t_2513: 'SafeIdentifier' = t_2512
            t_2514: 'SafeIdentifier'
            t_2514 = safe_identifier('name')
            t_2515: 'SafeIdentifier' = t_2514
            t_4790: 'StringField' = StringField()
            t_4791: 'FieldDef' = FieldDef(t_2515, t_4790, False)
            td_786: 'TableDef' = TableDef(t_2513, (t_4791,))
            did_bubble_787: 'bool33'
            try:
                td_786.field('nonexistent')
                did_bubble_787 = False
            except Exception37:
                did_bubble_787 = True
            def fn_4789() -> 'str27':
                return 'unknown field should bubble'
            test_80.assert_(did_bubble_787, fn_4789)
        finally:
            test_80.soft_fail_to_hard()
class TestCase99(TestCase46):
    def test___fieldDefNullableFlag__1124(self) -> None:
        'FieldDef nullable flag'
        test_81: Test = Test()
        try:
            t_2500: 'SafeIdentifier'
            t_2500 = safe_identifier('email')
            t_2501: 'SafeIdentifier' = t_2500
            t_4778: 'StringField' = StringField()
            required_789: 'FieldDef' = FieldDef(t_2501, t_4778, False)
            t_2504: 'SafeIdentifier'
            t_2504 = safe_identifier('bio')
            t_2505: 'SafeIdentifier' = t_2504
            t_4780: 'StringField' = StringField()
            optional_790: 'FieldDef' = FieldDef(t_2505, t_4780, True)
            t_4784: 'bool33' = not required_789.nullable
            def fn_4777() -> 'str27':
                return 'required field should not be nullable'
            test_81.assert_(t_4784, fn_4777)
            t_4786: 'bool33' = optional_790.nullable
            def fn_4776() -> 'str27':
                return 'optional field should be nullable'
            test_81.assert_(t_4786, fn_4776)
        finally:
            test_81.soft_fail_to_hard()
class TestCase100(TestCase46):
    def test___stringEscaping__1125(self) -> None:
        'string escaping'
        test_85: Test = Test()
        try:
            def build_916(name_918: 'str27') -> 'str27':
                t_4758: 'SqlBuilder' = SqlBuilder()
                t_4758.append_safe('select * from hi where name = ')
                t_4758.append_string(name_918)
                return t_4758.accumulated.to_string()
            def build_wrong_917(name_920: 'str27') -> 'str27':
                return str_cat_5805("select * from hi where name = '", name_920, "'")
            actual_1127: 'str27' = build_916('world')
            t_4768: 'bool33' = actual_1127 == "select * from hi where name = 'world'"
            def fn_4765() -> 'str27':
                return str_cat_5805('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_1127, ')')
            test_85.assert_(t_4768, fn_4765)
            bobby_tables_922: 'str27' = "Robert'); drop table hi;--"
            actual_1129: 'str27' = build_916("Robert'); drop table hi;--")
            t_4772: 'bool33' = actual_1129 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_4764() -> 'str27':
                return str_cat_5805('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_1129, ')')
            test_85.assert_(t_4772, fn_4764)
            def fn_4763() -> 'str27':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_85.assert_(True, fn_4763)
        finally:
            test_85.soft_fail_to_hard()
class TestCase101(TestCase46):
    def test___stringEdgeCases__1133(self) -> None:
        'string edge cases'
        test_86: Test = Test()
        try:
            t_4726: 'SqlBuilder' = SqlBuilder()
            t_4726.append_safe('v = ')
            t_4726.append_string('')
            actual_1134: 'str27' = t_4726.accumulated.to_string()
            t_4732: 'bool33' = actual_1134 == "v = ''"
            def fn_4725() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_1134, ')')
            test_86.assert_(t_4732, fn_4725)
            t_4734: 'SqlBuilder' = SqlBuilder()
            t_4734.append_safe('v = ')
            t_4734.append_string("a''b")
            actual_1137: 'str27' = t_4734.accumulated.to_string()
            t_4740: 'bool33' = actual_1137 == "v = 'a''''b'"
            def fn_4724() -> 'str27':
                return str_cat_5805("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_1137, ')')
            test_86.assert_(t_4740, fn_4724)
            t_4742: 'SqlBuilder' = SqlBuilder()
            t_4742.append_safe('v = ')
            t_4742.append_string('Hello \u4e16\u754c')
            actual_1140: 'str27' = t_4742.accumulated.to_string()
            t_4748: 'bool33' = actual_1140 == "v = 'Hello \u4e16\u754c'"
            def fn_4723() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_1140, ')')
            test_86.assert_(t_4748, fn_4723)
            t_4750: 'SqlBuilder' = SqlBuilder()
            t_4750.append_safe('v = ')
            t_4750.append_string('Line1\nLine2')
            actual_1143: 'str27' = t_4750.accumulated.to_string()
            t_4756: 'bool33' = actual_1143 == "v = 'Line1\nLine2'"
            def fn_4722() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_1143, ')')
            test_86.assert_(t_4756, fn_4722)
        finally:
            test_86.soft_fail_to_hard()
class TestCase102(TestCase46):
    def test___numbersAndBooleans__1146(self) -> None:
        'numbers and booleans'
        test_87: Test = Test()
        try:
            t_4697: 'SqlBuilder' = SqlBuilder()
            t_4697.append_safe('select ')
            t_4697.append_int32(42)
            t_4697.append_safe(', ')
            t_4697.append_int64(43)
            t_4697.append_safe(', ')
            t_4697.append_float64(19.99)
            t_4697.append_safe(', ')
            t_4697.append_boolean(True)
            t_4697.append_safe(', ')
            t_4697.append_boolean(False)
            actual_1147: 'str27' = t_4697.accumulated.to_string()
            t_4711: 'bool33' = actual_1147 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_4696() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_1147, ')')
            test_87.assert_(t_4711, fn_4696)
            t_2445: 'date26'
            t_2445 = date_5830(2024, 12, 25)
            date_925: 'date26' = t_2445
            t_4713: 'SqlBuilder' = SqlBuilder()
            t_4713.append_safe('insert into t values (')
            t_4713.append_date(date_925)
            t_4713.append_safe(')')
            actual_1150: 'str27' = t_4713.accumulated.to_string()
            t_4720: 'bool33' = actual_1150 == "insert into t values ('2024-12-25')"
            def fn_4695() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_1150, ')')
            test_87.assert_(t_4720, fn_4695)
        finally:
            test_87.soft_fail_to_hard()
class TestCase103(TestCase46):
    def test___lists__1153(self) -> None:
        'lists'
        test_88: Test = Test()
        try:
            t_4641: 'SqlBuilder' = SqlBuilder()
            t_4641.append_safe('v IN (')
            t_4641.append_string_list(('a', 'b', "c'd"))
            t_4641.append_safe(')')
            actual_1154: 'str27' = t_4641.accumulated.to_string()
            t_4648: 'bool33' = actual_1154 == "v IN ('a', 'b', 'c''d')"
            def fn_4640() -> 'str27':
                return str_cat_5805("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_1154, ')')
            test_88.assert_(t_4648, fn_4640)
            t_4650: 'SqlBuilder' = SqlBuilder()
            t_4650.append_safe('v IN (')
            t_4650.append_int32_list((1, 2, 3))
            t_4650.append_safe(')')
            actual_1157: 'str27' = t_4650.accumulated.to_string()
            t_4657: 'bool33' = actual_1157 == 'v IN (1, 2, 3)'
            def fn_4639() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_1157, ')')
            test_88.assert_(t_4657, fn_4639)
            t_4659: 'SqlBuilder' = SqlBuilder()
            t_4659.append_safe('v IN (')
            t_4659.append_int64_list((1, 2))
            t_4659.append_safe(')')
            actual_1160: 'str27' = t_4659.accumulated.to_string()
            t_4666: 'bool33' = actual_1160 == 'v IN (1, 2)'
            def fn_4638() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_1160, ')')
            test_88.assert_(t_4666, fn_4638)
            t_4668: 'SqlBuilder' = SqlBuilder()
            t_4668.append_safe('v IN (')
            t_4668.append_float64_list((1.0, 2.0))
            t_4668.append_safe(')')
            actual_1163: 'str27' = t_4668.accumulated.to_string()
            t_4675: 'bool33' = actual_1163 == 'v IN (1.0, 2.0)'
            def fn_4637() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_1163, ')')
            test_88.assert_(t_4675, fn_4637)
            t_4677: 'SqlBuilder' = SqlBuilder()
            t_4677.append_safe('v IN (')
            t_4677.append_boolean_list((True, False))
            t_4677.append_safe(')')
            actual_1166: 'str27' = t_4677.accumulated.to_string()
            t_4684: 'bool33' = actual_1166 == 'v IN (TRUE, FALSE)'
            def fn_4636() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_1166, ')')
            test_88.assert_(t_4684, fn_4636)
            t_2417: 'date26'
            t_2417 = date_5830(2024, 1, 1)
            t_2418: 'date26' = t_2417
            t_2419: 'date26'
            t_2419 = date_5830(2024, 12, 25)
            t_2420: 'date26' = t_2419
            dates_927: 'Sequence29[date26]' = (t_2418, t_2420)
            t_4686: 'SqlBuilder' = SqlBuilder()
            t_4686.append_safe('v IN (')
            t_4686.append_date_list(dates_927)
            t_4686.append_safe(')')
            actual_1169: 'str27' = t_4686.accumulated.to_string()
            t_4693: 'bool33' = actual_1169 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_4635() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_1169, ')')
            test_88.assert_(t_4693, fn_4635)
        finally:
            test_88.soft_fail_to_hard()
class TestCase104(TestCase46):
    def test___sqlFloat64_naNRendersAsNull__1172(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_89: Test = Test()
        try:
            nan_929: 'float38'
            nan_929 = 0.0 / 0.0
            t_4627: 'SqlBuilder' = SqlBuilder()
            t_4627.append_safe('v = ')
            t_4627.append_float64(nan_929)
            actual_1173: 'str27' = t_4627.accumulated.to_string()
            t_4633: 'bool33' = actual_1173 == 'v = NULL'
            def fn_4626() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_1173, ')')
            test_89.assert_(t_4633, fn_4626)
        finally:
            test_89.soft_fail_to_hard()
class TestCase105(TestCase46):
    def test___sqlFloat64_infinityRendersAsNull__1176(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_90: Test = Test()
        try:
            inf_931: 'float38'
            inf_931 = 1.0 / 0.0
            t_4618: 'SqlBuilder' = SqlBuilder()
            t_4618.append_safe('v = ')
            t_4618.append_float64(inf_931)
            actual_1177: 'str27' = t_4618.accumulated.to_string()
            t_4624: 'bool33' = actual_1177 == 'v = NULL'
            def fn_4617() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_1177, ')')
            test_90.assert_(t_4624, fn_4617)
        finally:
            test_90.soft_fail_to_hard()
class TestCase106(TestCase46):
    def test___sqlFloat64_negativeInfinityRendersAsNull__1180(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_91: Test = Test()
        try:
            ninf_933: 'float38'
            ninf_933 = -1.0 / 0.0
            t_4609: 'SqlBuilder' = SqlBuilder()
            t_4609.append_safe('v = ')
            t_4609.append_float64(ninf_933)
            actual_1181: 'str27' = t_4609.accumulated.to_string()
            t_4615: 'bool33' = actual_1181 == 'v = NULL'
            def fn_4608() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_1181, ')')
            test_91.assert_(t_4615, fn_4608)
        finally:
            test_91.soft_fail_to_hard()
class TestCase107(TestCase46):
    def test___sqlFloat64_normalValuesStillWork__1184(self) -> None:
        'SqlFloat64 normal values still work'
        test_92: Test = Test()
        try:
            t_4584: 'SqlBuilder' = SqlBuilder()
            t_4584.append_safe('v = ')
            t_4584.append_float64(3.14)
            actual_1185: 'str27' = t_4584.accumulated.to_string()
            t_4590: 'bool33' = actual_1185 == 'v = 3.14'
            def fn_4583() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_1185, ')')
            test_92.assert_(t_4590, fn_4583)
            t_4592: 'SqlBuilder' = SqlBuilder()
            t_4592.append_safe('v = ')
            t_4592.append_float64(0.0)
            actual_1188: 'str27' = t_4592.accumulated.to_string()
            t_4598: 'bool33' = actual_1188 == 'v = 0.0'
            def fn_4582() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_1188, ')')
            test_92.assert_(t_4598, fn_4582)
            t_4600: 'SqlBuilder' = SqlBuilder()
            t_4600.append_safe('v = ')
            t_4600.append_float64(-42.5)
            actual_1191: 'str27' = t_4600.accumulated.to_string()
            t_4606: 'bool33' = actual_1191 == 'v = -42.5'
            def fn_4581() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_1191, ')')
            test_92.assert_(t_4606, fn_4581)
        finally:
            test_92.soft_fail_to_hard()
class TestCase108(TestCase46):
    def test___sqlDateRendersWithQuotes__1194(self) -> None:
        'SqlDate renders with quotes'
        test_93: Test = Test()
        try:
            t_2313: 'date26'
            t_2313 = date_5830(2024, 6, 15)
            d_936: 'date26' = t_2313
            t_4573: 'SqlBuilder' = SqlBuilder()
            t_4573.append_safe('v = ')
            t_4573.append_date(d_936)
            actual_1195: 'str27' = t_4573.accumulated.to_string()
            t_4579: 'bool33' = actual_1195 == "v = '2024-06-15'"
            def fn_4572() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_1195, ')')
            test_93.assert_(t_4579, fn_4572)
        finally:
            test_93.soft_fail_to_hard()
class TestCase109(TestCase46):
    def test___nesting__1198(self) -> None:
        'nesting'
        test_94: Test = Test()
        try:
            name_938: 'str27' = 'Someone'
            t_4541: 'SqlBuilder' = SqlBuilder()
            t_4541.append_safe('where p.last_name = ')
            t_4541.append_string('Someone')
            condition_939: 'SqlFragment' = t_4541.accumulated
            t_4545: 'SqlBuilder' = SqlBuilder()
            t_4545.append_safe('select p.id from person p ')
            t_4545.append_fragment(condition_939)
            actual_1200: 'str27' = t_4545.accumulated.to_string()
            t_4551: 'bool33' = actual_1200 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_4540() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1200, ')')
            test_94.assert_(t_4551, fn_4540)
            t_4553: 'SqlBuilder' = SqlBuilder()
            t_4553.append_safe('select p.id from person p ')
            t_4553.append_part(condition_939.to_source())
            actual_1203: 'str27' = t_4553.accumulated.to_string()
            t_4560: 'bool33' = actual_1203 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_4539() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1203, ')')
            test_94.assert_(t_4560, fn_4539)
            parts_940: 'Sequence29[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_4564: 'SqlBuilder' = SqlBuilder()
            t_4564.append_safe('select ')
            t_4564.append_part_list(parts_940)
            actual_1206: 'str27' = t_4564.accumulated.to_string()
            t_4570: 'bool33' = actual_1206 == "select 'a''b', 3"
            def fn_4538() -> 'str27':
                return str_cat_5805('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_1206, ')')
            test_94.assert_(t_4570, fn_4538)
        finally:
            test_94.soft_fail_to_hard()
