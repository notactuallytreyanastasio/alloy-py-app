from temper_std.testing import Test
from builtins import str as str27, bool as bool33, Exception as Exception37, int as int31, float as float38
from unittest import TestCase as TestCase46
from types import MappingProxyType as MappingProxyType32
from typing import Sequence as Sequence29
from datetime import date as date26
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_5137, pair_5141, changeset, Changeset, mapped_has_5114, len_5117, list_get_5125, str_cat_5119, list_for_each_5111, SqlFragment, from_, Query, SqlBuilder, date_5144, SqlString, SqlInt32, SqlPart
def csid_302(name_447: 'str27') -> 'SafeIdentifier':
    t_2783: 'SafeIdentifier'
    t_2783 = safe_identifier(name_447)
    return t_2783
def user_table_303() -> 'TableDef':
    return TableDef(csid_302('users'), (FieldDef(csid_302('name'), StringField(), False), FieldDef(csid_302('email'), StringField(), False), FieldDef(csid_302('age'), IntField(), True), FieldDef(csid_302('score'), FloatField(), True), FieldDef(csid_302('active'), BoolField(), True)))
class TestCase45(TestCase46):
    def test___castWhitelistsAllowedFields__908(self) -> None:
        'cast whitelists allowed fields'
        test_22: Test = Test()
        try:
            params_451: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'Alice'), pair_5141('email', 'alice@example.com'), pair_5141('admin', 'true')))
            t_4828: 'TableDef' = user_table_303()
            t_4829: 'SafeIdentifier' = csid_302('name')
            t_4830: 'SafeIdentifier' = csid_302('email')
            cs_452: 'Changeset' = changeset(t_4828, params_451).cast((t_4829, t_4830))
            t_4833: 'bool33' = mapped_has_5114(cs_452.changes, 'name')
            def fn_4823() -> 'str27':
                return 'name should be in changes'
            test_22.assert_(t_4833, fn_4823)
            t_4837: 'bool33' = mapped_has_5114(cs_452.changes, 'email')
            def fn_4822() -> 'str27':
                return 'email should be in changes'
            test_22.assert_(t_4837, fn_4822)
            t_4843: 'bool33' = not mapped_has_5114(cs_452.changes, 'admin')
            def fn_4821() -> 'str27':
                return 'admin must be dropped (not in whitelist)'
            test_22.assert_(t_4843, fn_4821)
            t_4845: 'bool33' = cs_452.is_valid
            def fn_4820() -> 'str27':
                return 'should still be valid'
            test_22.assert_(t_4845, fn_4820)
        finally:
            test_22.soft_fail_to_hard()
class TestCase47(TestCase46):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__909(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_23: Test = Test()
        try:
            params_454: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'Alice'), pair_5141('email', 'alice@example.com')))
            t_4806: 'TableDef' = user_table_303()
            t_4807: 'SafeIdentifier' = csid_302('name')
            cs_455: 'Changeset' = changeset(t_4806, params_454).cast((t_4807,)).cast((csid_302('email'),))
            t_4814: 'bool33' = not mapped_has_5114(cs_455.changes, 'name')
            def fn_4802() -> 'str27':
                return 'name must be excluded by second cast'
            test_23.assert_(t_4814, fn_4802)
            t_4817: 'bool33' = mapped_has_5114(cs_455.changes, 'email')
            def fn_4801() -> 'str27':
                return 'email should be present'
            test_23.assert_(t_4817, fn_4801)
        finally:
            test_23.soft_fail_to_hard()
class TestCase48(TestCase46):
    def test___castIgnoresEmptyStringValues__910(self) -> None:
        'cast ignores empty string values'
        test_24: Test = Test()
        try:
            params_457: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', ''), pair_5141('email', 'bob@example.com')))
            t_4788: 'TableDef' = user_table_303()
            t_4789: 'SafeIdentifier' = csid_302('name')
            t_4790: 'SafeIdentifier' = csid_302('email')
            cs_458: 'Changeset' = changeset(t_4788, params_457).cast((t_4789, t_4790))
            t_4795: 'bool33' = not mapped_has_5114(cs_458.changes, 'name')
            def fn_4784() -> 'str27':
                return 'empty name should not be in changes'
            test_24.assert_(t_4795, fn_4784)
            t_4798: 'bool33' = mapped_has_5114(cs_458.changes, 'email')
            def fn_4783() -> 'str27':
                return 'email should be in changes'
            test_24.assert_(t_4798, fn_4783)
        finally:
            test_24.soft_fail_to_hard()
class TestCase49(TestCase46):
    def test___validateRequiredPassesWhenFieldPresent__911(self) -> None:
        'validateRequired passes when field present'
        test_25: Test = Test()
        try:
            params_460: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'Alice'),))
            t_4770: 'TableDef' = user_table_303()
            t_4771: 'SafeIdentifier' = csid_302('name')
            cs_461: 'Changeset' = changeset(t_4770, params_460).cast((t_4771,)).validate_required((csid_302('name'),))
            t_4775: 'bool33' = cs_461.is_valid
            def fn_4767() -> 'str27':
                return 'should be valid'
            test_25.assert_(t_4775, fn_4767)
            t_4781: 'bool33' = len_5117(cs_461.errors) == 0
            def fn_4766() -> 'str27':
                return 'no errors expected'
            test_25.assert_(t_4781, fn_4766)
        finally:
            test_25.soft_fail_to_hard()
class TestCase50(TestCase46):
    def test___validateRequiredFailsWhenFieldMissing__912(self) -> None:
        'validateRequired fails when field missing'
        test_26: Test = Test()
        try:
            params_463: 'MappingProxyType32[str27, str27]' = map_constructor_5137(())
            t_4746: 'TableDef' = user_table_303()
            t_4747: 'SafeIdentifier' = csid_302('name')
            cs_464: 'Changeset' = changeset(t_4746, params_463).cast((t_4747,)).validate_required((csid_302('name'),))
            t_4753: 'bool33' = not cs_464.is_valid
            def fn_4744() -> 'str27':
                return 'should be invalid'
            test_26.assert_(t_4753, fn_4744)
            t_4758: 'bool33' = len_5117(cs_464.errors) == 1
            def fn_4743() -> 'str27':
                return 'should have one error'
            test_26.assert_(t_4758, fn_4743)
            t_4764: 'bool33' = list_get_5125(cs_464.errors, 0).field == 'name'
            def fn_4742() -> 'str27':
                return 'error should name the field'
            test_26.assert_(t_4764, fn_4742)
        finally:
            test_26.soft_fail_to_hard()
class TestCase51(TestCase46):
    def test___validateLengthPassesWithinRange__913(self) -> None:
        'validateLength passes within range'
        test_27: Test = Test()
        try:
            params_466: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'Alice'),))
            t_4734: 'TableDef' = user_table_303()
            t_4735: 'SafeIdentifier' = csid_302('name')
            cs_467: 'Changeset' = changeset(t_4734, params_466).cast((t_4735,)).validate_length(csid_302('name'), 2, 50)
            t_4739: 'bool33' = cs_467.is_valid
            def fn_4731() -> 'str27':
                return 'should be valid'
            test_27.assert_(t_4739, fn_4731)
        finally:
            test_27.soft_fail_to_hard()
class TestCase52(TestCase46):
    def test___validateLengthFailsWhenTooShort__914(self) -> None:
        'validateLength fails when too short'
        test_28: Test = Test()
        try:
            params_469: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'A'),))
            t_4722: 'TableDef' = user_table_303()
            t_4723: 'SafeIdentifier' = csid_302('name')
            cs_470: 'Changeset' = changeset(t_4722, params_469).cast((t_4723,)).validate_length(csid_302('name'), 2, 50)
            t_4729: 'bool33' = not cs_470.is_valid
            def fn_4719() -> 'str27':
                return 'should be invalid'
            test_28.assert_(t_4729, fn_4719)
        finally:
            test_28.soft_fail_to_hard()
class TestCase53(TestCase46):
    def test___validateLengthFailsWhenTooLong__915(self) -> None:
        'validateLength fails when too long'
        test_29: Test = Test()
        try:
            params_472: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_4710: 'TableDef' = user_table_303()
            t_4711: 'SafeIdentifier' = csid_302('name')
            cs_473: 'Changeset' = changeset(t_4710, params_472).cast((t_4711,)).validate_length(csid_302('name'), 2, 10)
            t_4717: 'bool33' = not cs_473.is_valid
            def fn_4707() -> 'str27':
                return 'should be invalid'
            test_29.assert_(t_4717, fn_4707)
        finally:
            test_29.soft_fail_to_hard()
class TestCase54(TestCase46):
    def test___validateIntPassesForValidInteger__916(self) -> None:
        'validateInt passes for valid integer'
        test_30: Test = Test()
        try:
            params_475: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('age', '30'),))
            t_4699: 'TableDef' = user_table_303()
            t_4700: 'SafeIdentifier' = csid_302('age')
            cs_476: 'Changeset' = changeset(t_4699, params_475).cast((t_4700,)).validate_int(csid_302('age'))
            t_4704: 'bool33' = cs_476.is_valid
            def fn_4696() -> 'str27':
                return 'should be valid'
            test_30.assert_(t_4704, fn_4696)
        finally:
            test_30.soft_fail_to_hard()
class TestCase55(TestCase46):
    def test___validateIntFailsForNonInteger__917(self) -> None:
        'validateInt fails for non-integer'
        test_31: Test = Test()
        try:
            params_478: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('age', 'not-a-number'),))
            t_4687: 'TableDef' = user_table_303()
            t_4688: 'SafeIdentifier' = csid_302('age')
            cs_479: 'Changeset' = changeset(t_4687, params_478).cast((t_4688,)).validate_int(csid_302('age'))
            t_4694: 'bool33' = not cs_479.is_valid
            def fn_4684() -> 'str27':
                return 'should be invalid'
            test_31.assert_(t_4694, fn_4684)
        finally:
            test_31.soft_fail_to_hard()
class TestCase56(TestCase46):
    def test___validateFloatPassesForValidFloat__918(self) -> None:
        'validateFloat passes for valid float'
        test_32: Test = Test()
        try:
            params_481: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('score', '9.5'),))
            t_4676: 'TableDef' = user_table_303()
            t_4677: 'SafeIdentifier' = csid_302('score')
            cs_482: 'Changeset' = changeset(t_4676, params_481).cast((t_4677,)).validate_float(csid_302('score'))
            t_4681: 'bool33' = cs_482.is_valid
            def fn_4673() -> 'str27':
                return 'should be valid'
            test_32.assert_(t_4681, fn_4673)
        finally:
            test_32.soft_fail_to_hard()
class TestCase57(TestCase46):
    def test___validateInt64_passesForValid64_bitInteger__919(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_33: Test = Test()
        try:
            params_484: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('age', '9999999999'),))
            t_4665: 'TableDef' = user_table_303()
            t_4666: 'SafeIdentifier' = csid_302('age')
            cs_485: 'Changeset' = changeset(t_4665, params_484).cast((t_4666,)).validate_int64(csid_302('age'))
            t_4670: 'bool33' = cs_485.is_valid
            def fn_4662() -> 'str27':
                return 'should be valid'
            test_33.assert_(t_4670, fn_4662)
        finally:
            test_33.soft_fail_to_hard()
class TestCase58(TestCase46):
    def test___validateInt64_failsForNonInteger__920(self) -> None:
        'validateInt64 fails for non-integer'
        test_34: Test = Test()
        try:
            params_487: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('age', 'not-a-number'),))
            t_4653: 'TableDef' = user_table_303()
            t_4654: 'SafeIdentifier' = csid_302('age')
            cs_488: 'Changeset' = changeset(t_4653, params_487).cast((t_4654,)).validate_int64(csid_302('age'))
            t_4660: 'bool33' = not cs_488.is_valid
            def fn_4650() -> 'str27':
                return 'should be invalid'
            test_34.assert_(t_4660, fn_4650)
        finally:
            test_34.soft_fail_to_hard()
class TestCase59(TestCase46):
    def test___validateBoolAcceptsTrue1_yesOn__921(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_35: Test = Test()
        try:
            def fn_4647(v_490: 'str27') -> 'None':
                params_491: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('active', v_490),))
                t_4639: 'TableDef' = user_table_303()
                t_4640: 'SafeIdentifier' = csid_302('active')
                cs_492: 'Changeset' = changeset(t_4639, params_491).cast((t_4640,)).validate_bool(csid_302('active'))
                t_4644: 'bool33' = cs_492.is_valid
                def fn_4636() -> 'str27':
                    return str_cat_5119('should accept: ', v_490)
                test_35.assert_(t_4644, fn_4636)
            list_for_each_5111(('true', '1', 'yes', 'on'), fn_4647)
        finally:
            test_35.soft_fail_to_hard()
class TestCase60(TestCase46):
    def test___validateBoolAcceptsFalse0_noOff__922(self) -> None:
        'validateBool accepts false/0/no/off'
        test_36: Test = Test()
        try:
            def fn_4633(v_494: 'str27') -> 'None':
                params_495: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('active', v_494),))
                t_4625: 'TableDef' = user_table_303()
                t_4626: 'SafeIdentifier' = csid_302('active')
                cs_496: 'Changeset' = changeset(t_4625, params_495).cast((t_4626,)).validate_bool(csid_302('active'))
                t_4630: 'bool33' = cs_496.is_valid
                def fn_4622() -> 'str27':
                    return str_cat_5119('should accept: ', v_494)
                test_36.assert_(t_4630, fn_4622)
            list_for_each_5111(('false', '0', 'no', 'off'), fn_4633)
        finally:
            test_36.soft_fail_to_hard()
class TestCase61(TestCase46):
    def test___validateBoolRejectsAmbiguousValues__923(self) -> None:
        'validateBool rejects ambiguous values'
        test_37: Test = Test()
        try:
            def fn_4619(v_498: 'str27') -> 'None':
                params_499: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('active', v_498),))
                t_4610: 'TableDef' = user_table_303()
                t_4611: 'SafeIdentifier' = csid_302('active')
                cs_500: 'Changeset' = changeset(t_4610, params_499).cast((t_4611,)).validate_bool(csid_302('active'))
                t_4617: 'bool33' = not cs_500.is_valid
                def fn_4607() -> 'str27':
                    return str_cat_5119('should reject ambiguous: ', v_498)
                test_37.assert_(t_4617, fn_4607)
            list_for_each_5111(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_4619)
        finally:
            test_37.soft_fail_to_hard()
class TestCase62(TestCase46):
    def test___toInsertSqlEscapesBobbyTables__924(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_38: Test = Test()
        try:
            params_502: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', "Robert'); DROP TABLE users;--"), pair_5141('email', 'bobby@evil.com')))
            t_4595: 'TableDef' = user_table_303()
            t_4596: 'SafeIdentifier' = csid_302('name')
            t_4597: 'SafeIdentifier' = csid_302('email')
            cs_503: 'Changeset' = changeset(t_4595, params_502).cast((t_4596, t_4597)).validate_required((csid_302('name'), csid_302('email')))
            t_2584: 'SqlFragment'
            t_2584 = cs_503.to_insert_sql()
            sql_frag_504: 'SqlFragment' = t_2584
            s_505: 'str27' = sql_frag_504.to_string()
            t_4604: 'bool33' = s_505.find("''") >= 0
            def fn_4591() -> 'str27':
                return str_cat_5119('single quote must be doubled: ', s_505)
            test_38.assert_(t_4604, fn_4591)
        finally:
            test_38.soft_fail_to_hard()
class TestCase63(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForStringField__925(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_39: Test = Test()
        try:
            params_507: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'Alice'), pair_5141('email', 'a@example.com')))
            t_4575: 'TableDef' = user_table_303()
            t_4576: 'SafeIdentifier' = csid_302('name')
            t_4577: 'SafeIdentifier' = csid_302('email')
            cs_508: 'Changeset' = changeset(t_4575, params_507).cast((t_4576, t_4577)).validate_required((csid_302('name'), csid_302('email')))
            t_2563: 'SqlFragment'
            t_2563 = cs_508.to_insert_sql()
            sql_frag_509: 'SqlFragment' = t_2563
            s_510: 'str27' = sql_frag_509.to_string()
            t_4584: 'bool33' = s_510.find('INSERT INTO users') >= 0
            def fn_4571() -> 'str27':
                return str_cat_5119('has INSERT INTO: ', s_510)
            test_39.assert_(t_4584, fn_4571)
            t_4588: 'bool33' = s_510.find("'Alice'") >= 0
            def fn_4570() -> 'str27':
                return str_cat_5119('has quoted name: ', s_510)
            test_39.assert_(t_4588, fn_4570)
        finally:
            test_39.soft_fail_to_hard()
class TestCase64(TestCase46):
    def test___toInsertSqlProducesCorrectSqlForIntField__926(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_40: Test = Test()
        try:
            params_512: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'Bob'), pair_5141('email', 'b@example.com'), pair_5141('age', '25')))
            t_4557: 'TableDef' = user_table_303()
            t_4558: 'SafeIdentifier' = csid_302('name')
            t_4559: 'SafeIdentifier' = csid_302('email')
            t_4560: 'SafeIdentifier' = csid_302('age')
            cs_513: 'Changeset' = changeset(t_4557, params_512).cast((t_4558, t_4559, t_4560)).validate_required((csid_302('name'), csid_302('email')))
            t_2546: 'SqlFragment'
            t_2546 = cs_513.to_insert_sql()
            sql_frag_514: 'SqlFragment' = t_2546
            s_515: 'str27' = sql_frag_514.to_string()
            t_4567: 'bool33' = s_515.find('25') >= 0
            def fn_4552() -> 'str27':
                return str_cat_5119('age rendered unquoted: ', s_515)
            test_40.assert_(t_4567, fn_4552)
        finally:
            test_40.soft_fail_to_hard()
class TestCase65(TestCase46):
    def test___toInsertSqlBubblesOnInvalidChangeset__927(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_41: Test = Test()
        try:
            params_517: 'MappingProxyType32[str27, str27]' = map_constructor_5137(())
            t_4545: 'TableDef' = user_table_303()
            t_4546: 'SafeIdentifier' = csid_302('name')
            cs_518: 'Changeset' = changeset(t_4545, params_517).cast((t_4546,)).validate_required((csid_302('name'),))
            did_bubble_519: 'bool33'
            try:
                cs_518.to_insert_sql()
                did_bubble_519 = False
            except Exception37:
                did_bubble_519 = True
            def fn_4543() -> 'str27':
                return 'invalid changeset should bubble'
            test_41.assert_(did_bubble_519, fn_4543)
        finally:
            test_41.soft_fail_to_hard()
class TestCase66(TestCase46):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__928(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_42: Test = Test()
        try:
            strict_table_521: 'TableDef' = TableDef(csid_302('posts'), (FieldDef(csid_302('title'), StringField(), False), FieldDef(csid_302('body'), StringField(), True)))
            params_522: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('body', 'hello'),))
            t_4536: 'SafeIdentifier' = csid_302('body')
            cs_523: 'Changeset' = changeset(strict_table_521, params_522).cast((t_4536,))
            t_4538: 'bool33' = cs_523.is_valid
            def fn_4525() -> 'str27':
                return 'changeset should appear valid (no explicit validation run)'
            test_42.assert_(t_4538, fn_4525)
            did_bubble_524: 'bool33'
            try:
                cs_523.to_insert_sql()
                did_bubble_524 = False
            except Exception37:
                did_bubble_524 = True
            def fn_4524() -> 'str27':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_42.assert_(did_bubble_524, fn_4524)
        finally:
            test_42.soft_fail_to_hard()
class TestCase67(TestCase46):
    def test___toUpdateSqlProducesCorrectSql__929(self) -> None:
        'toUpdateSql produces correct SQL'
        test_43: Test = Test()
        try:
            params_526: 'MappingProxyType32[str27, str27]' = map_constructor_5137((pair_5141('name', 'Bob'),))
            t_4515: 'TableDef' = user_table_303()
            t_4516: 'SafeIdentifier' = csid_302('name')
            cs_527: 'Changeset' = changeset(t_4515, params_526).cast((t_4516,)).validate_required((csid_302('name'),))
            t_2506: 'SqlFragment'
            t_2506 = cs_527.to_update_sql(42)
            sql_frag_528: 'SqlFragment' = t_2506
            s_529: 'str27' = sql_frag_528.to_string()
            t_4522: 'bool33' = s_529 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_4512() -> 'str27':
                return str_cat_5119('got: ', s_529)
            test_43.assert_(t_4522, fn_4512)
        finally:
            test_43.soft_fail_to_hard()
class TestCase68(TestCase46):
    def test___toUpdateSqlBubblesOnInvalidChangeset__930(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_44: Test = Test()
        try:
            params_531: 'MappingProxyType32[str27, str27]' = map_constructor_5137(())
            t_4505: 'TableDef' = user_table_303()
            t_4506: 'SafeIdentifier' = csid_302('name')
            cs_532: 'Changeset' = changeset(t_4505, params_531).cast((t_4506,)).validate_required((csid_302('name'),))
            did_bubble_533: 'bool33'
            try:
                cs_532.to_update_sql(1)
                did_bubble_533 = False
            except Exception37:
                did_bubble_533 = True
            def fn_4503() -> 'str27':
                return 'invalid changeset should bubble'
            test_44.assert_(did_bubble_533, fn_4503)
        finally:
            test_44.soft_fail_to_hard()
def sid_304(name_588: 'str27') -> 'SafeIdentifier':
    t_2420: 'SafeIdentifier'
    t_2420 = safe_identifier(name_588)
    return t_2420
class TestCase69(TestCase46):
    def test___bareFromProducesSelect__955(self) -> None:
        'bare from produces SELECT *'
        test_45: Test = Test()
        try:
            q_591: 'Query' = from_(sid_304('users'))
            t_4438: 'bool33' = q_591.to_sql().to_string() == 'SELECT * FROM users'
            def fn_4433() -> 'str27':
                return 'bare query'
            test_45.assert_(t_4438, fn_4433)
        finally:
            test_45.soft_fail_to_hard()
class TestCase70(TestCase46):
    def test___selectRestrictsColumns__956(self) -> None:
        'select restricts columns'
        test_46: Test = Test()
        try:
            t_4424: 'SafeIdentifier' = sid_304('users')
            t_4425: 'SafeIdentifier' = sid_304('id')
            t_4426: 'SafeIdentifier' = sid_304('name')
            q_593: 'Query' = from_(t_4424).select((t_4425, t_4426))
            t_4431: 'bool33' = q_593.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_4423() -> 'str27':
                return 'select columns'
            test_46.assert_(t_4431, fn_4423)
        finally:
            test_46.soft_fail_to_hard()
class TestCase71(TestCase46):
    def test___whereAddsConditionWithIntValue__957(self) -> None:
        'where adds condition with int value'
        test_47: Test = Test()
        try:
            t_4412: 'SafeIdentifier' = sid_304('users')
            t_4413: 'SqlBuilder' = SqlBuilder()
            t_4413.append_safe('age > ')
            t_4413.append_int32(18)
            t_4416: 'SqlFragment' = t_4413.accumulated
            q_595: 'Query' = from_(t_4412).where(t_4416)
            t_4421: 'bool33' = q_595.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_4411() -> 'str27':
                return 'where int'
            test_47.assert_(t_4421, fn_4411)
        finally:
            test_47.soft_fail_to_hard()
class TestCase72(TestCase46):
    def test___whereAddsConditionWithBoolValue__959(self) -> None:
        'where adds condition with bool value'
        test_48: Test = Test()
        try:
            t_4400: 'SafeIdentifier' = sid_304('users')
            t_4401: 'SqlBuilder' = SqlBuilder()
            t_4401.append_safe('active = ')
            t_4401.append_boolean(True)
            t_4404: 'SqlFragment' = t_4401.accumulated
            q_597: 'Query' = from_(t_4400).where(t_4404)
            t_4409: 'bool33' = q_597.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_4399() -> 'str27':
                return 'where bool'
            test_48.assert_(t_4409, fn_4399)
        finally:
            test_48.soft_fail_to_hard()
class TestCase73(TestCase46):
    def test___chainedWhereUsesAnd__961(self) -> None:
        'chained where uses AND'
        test_49: Test = Test()
        try:
            t_4383: 'SafeIdentifier' = sid_304('users')
            t_4384: 'SqlBuilder' = SqlBuilder()
            t_4384.append_safe('age > ')
            t_4384.append_int32(18)
            t_4387: 'SqlFragment' = t_4384.accumulated
            t_4388: 'Query' = from_(t_4383).where(t_4387)
            t_4389: 'SqlBuilder' = SqlBuilder()
            t_4389.append_safe('active = ')
            t_4389.append_boolean(True)
            q_599: 'Query' = t_4388.where(t_4389.accumulated)
            t_4397: 'bool33' = q_599.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_4382() -> 'str27':
                return 'chained where'
            test_49.assert_(t_4397, fn_4382)
        finally:
            test_49.soft_fail_to_hard()
class TestCase74(TestCase46):
    def test___orderByAsc__964(self) -> None:
        'orderBy ASC'
        test_50: Test = Test()
        try:
            t_4374: 'SafeIdentifier' = sid_304('users')
            t_4375: 'SafeIdentifier' = sid_304('name')
            q_601: 'Query' = from_(t_4374).order_by(t_4375, True)
            t_4380: 'bool33' = q_601.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_4373() -> 'str27':
                return 'order asc'
            test_50.assert_(t_4380, fn_4373)
        finally:
            test_50.soft_fail_to_hard()
class TestCase75(TestCase46):
    def test___orderByDesc__965(self) -> None:
        'orderBy DESC'
        test_51: Test = Test()
        try:
            t_4365: 'SafeIdentifier' = sid_304('users')
            t_4366: 'SafeIdentifier' = sid_304('created_at')
            q_603: 'Query' = from_(t_4365).order_by(t_4366, False)
            t_4371: 'bool33' = q_603.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_4364() -> 'str27':
                return 'order desc'
            test_51.assert_(t_4371, fn_4364)
        finally:
            test_51.soft_fail_to_hard()
class TestCase76(TestCase46):
    def test___limitAndOffset__966(self) -> None:
        'limit and offset'
        test_52: Test = Test()
        try:
            t_2354: 'Query'
            t_2354 = from_(sid_304('users')).limit(10)
            t_2355: 'Query'
            t_2355 = t_2354.offset(20)
            q_605: 'Query' = t_2355
            t_4362: 'bool33' = q_605.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_4357() -> 'str27':
                return 'limit/offset'
            test_52.assert_(t_4362, fn_4357)
        finally:
            test_52.soft_fail_to_hard()
class TestCase77(TestCase46):
    def test___limitBubblesOnNegative__967(self) -> None:
        'limit bubbles on negative'
        test_53: Test = Test()
        try:
            did_bubble_607: 'bool33'
            try:
                from_(sid_304('users')).limit(-1)
                did_bubble_607 = False
            except Exception37:
                did_bubble_607 = True
            def fn_4353() -> 'str27':
                return 'negative limit should bubble'
            test_53.assert_(did_bubble_607, fn_4353)
        finally:
            test_53.soft_fail_to_hard()
class TestCase78(TestCase46):
    def test___offsetBubblesOnNegative__968(self) -> None:
        'offset bubbles on negative'
        test_54: Test = Test()
        try:
            did_bubble_609: 'bool33'
            try:
                from_(sid_304('users')).offset(-1)
                did_bubble_609 = False
            except Exception37:
                did_bubble_609 = True
            def fn_4349() -> 'str27':
                return 'negative offset should bubble'
            test_54.assert_(did_bubble_609, fn_4349)
        finally:
            test_54.soft_fail_to_hard()
class TestCase79(TestCase46):
    def test___complexComposedQuery__969(self) -> None:
        'complex composed query'
        test_55: Test = Test()
        try:
            min_age_611: 'int31' = 21
            t_4327: 'SafeIdentifier' = sid_304('users')
            t_4328: 'SafeIdentifier' = sid_304('id')
            t_4329: 'SafeIdentifier' = sid_304('name')
            t_4330: 'SafeIdentifier' = sid_304('email')
            t_4331: 'Query' = from_(t_4327).select((t_4328, t_4329, t_4330))
            t_4332: 'SqlBuilder' = SqlBuilder()
            t_4332.append_safe('age >= ')
            t_4332.append_int32(21)
            t_4336: 'Query' = t_4331.where(t_4332.accumulated)
            t_4337: 'SqlBuilder' = SqlBuilder()
            t_4337.append_safe('active = ')
            t_4337.append_boolean(True)
            t_2340: 'Query'
            t_2340 = t_4336.where(t_4337.accumulated).order_by(sid_304('name'), True).limit(25)
            t_2341: 'Query'
            t_2341 = t_2340.offset(0)
            q_612: 'Query' = t_2341
            t_4347: 'bool33' = q_612.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_4326() -> 'str27':
                return 'complex query'
            test_55.assert_(t_4347, fn_4326)
        finally:
            test_55.soft_fail_to_hard()
class TestCase80(TestCase46):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__972(self) -> None:
        'safeToSql applies default limit when none set'
        test_56: Test = Test()
        try:
            q_614: 'Query' = from_(sid_304('users'))
            t_2317: 'SqlFragment'
            t_2317 = q_614.safe_to_sql(100)
            t_2318: 'SqlFragment' = t_2317
            s_615: 'str27' = t_2318.to_string()
            t_4324: 'bool33' = s_615 == 'SELECT * FROM users LIMIT 100'
            def fn_4320() -> 'str27':
                return str_cat_5119('should have limit: ', s_615)
            test_56.assert_(t_4324, fn_4320)
        finally:
            test_56.soft_fail_to_hard()
class TestCase81(TestCase46):
    def test___safeToSqlRespectsExplicitLimit__973(self) -> None:
        'safeToSql respects explicit limit'
        test_57: Test = Test()
        try:
            t_2309: 'Query'
            t_2309 = from_(sid_304('users')).limit(5)
            q_617: 'Query' = t_2309
            t_2312: 'SqlFragment'
            t_2312 = q_617.safe_to_sql(100)
            t_2313: 'SqlFragment' = t_2312
            s_618: 'str27' = t_2313.to_string()
            t_4318: 'bool33' = s_618 == 'SELECT * FROM users LIMIT 5'
            def fn_4314() -> 'str27':
                return str_cat_5119('explicit limit preserved: ', s_618)
            test_57.assert_(t_4318, fn_4314)
        finally:
            test_57.soft_fail_to_hard()
class TestCase82(TestCase46):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__974(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_58: Test = Test()
        try:
            did_bubble_620: 'bool33'
            try:
                from_(sid_304('users')).safe_to_sql(-1)
                did_bubble_620 = False
            except Exception37:
                did_bubble_620 = True
            def fn_4310() -> 'str27':
                return 'negative defaultLimit should bubble'
            test_58.assert_(did_bubble_620, fn_4310)
        finally:
            test_58.soft_fail_to_hard()
class TestCase83(TestCase46):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__975(self) -> None:
        'where with injection attempt in string value is escaped'
        test_59: Test = Test()
        try:
            evil_622: 'str27' = "'; DROP TABLE users; --"
            t_4294: 'SafeIdentifier' = sid_304('users')
            t_4295: 'SqlBuilder' = SqlBuilder()
            t_4295.append_safe('name = ')
            t_4295.append_string("'; DROP TABLE users; --")
            t_4298: 'SqlFragment' = t_4295.accumulated
            q_623: 'Query' = from_(t_4294).where(t_4298)
            s_624: 'str27' = q_623.to_sql().to_string()
            t_4303: 'bool33' = s_624.find("''") >= 0
            def fn_4293() -> 'str27':
                return str_cat_5119('quotes must be doubled: ', s_624)
            test_59.assert_(t_4303, fn_4293)
            t_4307: 'bool33' = s_624.find('SELECT * FROM users WHERE name =') >= 0
            def fn_4292() -> 'str27':
                return str_cat_5119('structure intact: ', s_624)
            test_59.assert_(t_4307, fn_4292)
        finally:
            test_59.soft_fail_to_hard()
class TestCase84(TestCase46):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__977(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_60: Test = Test()
        try:
            attack_626: 'str27' = 'users; DROP TABLE users; --'
            did_bubble_627: 'bool33'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_627 = False
            except Exception37:
                did_bubble_627 = True
            def fn_4289() -> 'str27':
                return 'metacharacter-containing name must be rejected at construction'
            test_60.assert_(did_bubble_627, fn_4289)
        finally:
            test_60.soft_fail_to_hard()
class TestCase85(TestCase46):
    def test___safeIdentifierAcceptsValidNames__978(self) -> None:
        'safeIdentifier accepts valid names'
        test_67: Test = Test()
        try:
            t_2282: 'SafeIdentifier'
            t_2282 = safe_identifier('user_name')
            id_665: 'SafeIdentifier' = t_2282
            t_4287: 'bool33' = id_665.sql_value == 'user_name'
            def fn_4284() -> 'str27':
                return 'value should round-trip'
            test_67.assert_(t_4287, fn_4284)
        finally:
            test_67.soft_fail_to_hard()
class TestCase86(TestCase46):
    def test___safeIdentifierRejectsEmptyString__979(self) -> None:
        'safeIdentifier rejects empty string'
        test_68: Test = Test()
        try:
            did_bubble_667: 'bool33'
            try:
                safe_identifier('')
                did_bubble_667 = False
            except Exception37:
                did_bubble_667 = True
            def fn_4281() -> 'str27':
                return 'empty string should bubble'
            test_68.assert_(did_bubble_667, fn_4281)
        finally:
            test_68.soft_fail_to_hard()
class TestCase87(TestCase46):
    def test___safeIdentifierRejectsLeadingDigit__980(self) -> None:
        'safeIdentifier rejects leading digit'
        test_69: Test = Test()
        try:
            did_bubble_669: 'bool33'
            try:
                safe_identifier('1col')
                did_bubble_669 = False
            except Exception37:
                did_bubble_669 = True
            def fn_4278() -> 'str27':
                return 'leading digit should bubble'
            test_69.assert_(did_bubble_669, fn_4278)
        finally:
            test_69.soft_fail_to_hard()
class TestCase88(TestCase46):
    def test___safeIdentifierRejectsSqlMetacharacters__981(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_70: Test = Test()
        try:
            cases_671: 'Sequence29[str27]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_4275(c_672: 'str27') -> 'None':
                did_bubble_673: 'bool33'
                try:
                    safe_identifier(c_672)
                    did_bubble_673 = False
                except Exception37:
                    did_bubble_673 = True
                def fn_4272() -> 'str27':
                    return str_cat_5119('should reject: ', c_672)
                test_70.assert_(did_bubble_673, fn_4272)
            list_for_each_5111(cases_671, fn_4275)
        finally:
            test_70.soft_fail_to_hard()
class TestCase89(TestCase46):
    def test___tableDefFieldLookupFound__982(self) -> None:
        'TableDef field lookup - found'
        test_71: Test = Test()
        try:
            t_2259: 'SafeIdentifier'
            t_2259 = safe_identifier('users')
            t_2260: 'SafeIdentifier' = t_2259
            t_2261: 'SafeIdentifier'
            t_2261 = safe_identifier('name')
            t_2262: 'SafeIdentifier' = t_2261
            t_4262: 'StringField' = StringField()
            t_4263: 'FieldDef' = FieldDef(t_2262, t_4262, False)
            t_2265: 'SafeIdentifier'
            t_2265 = safe_identifier('age')
            t_2266: 'SafeIdentifier' = t_2265
            t_4264: 'IntField' = IntField()
            t_4265: 'FieldDef' = FieldDef(t_2266, t_4264, False)
            td_675: 'TableDef' = TableDef(t_2260, (t_4263, t_4265))
            t_2270: 'FieldDef'
            t_2270 = td_675.field('age')
            f_676: 'FieldDef' = t_2270
            t_4270: 'bool33' = f_676.name.sql_value == 'age'
            def fn_4261() -> 'str27':
                return 'should find age field'
            test_71.assert_(t_4270, fn_4261)
        finally:
            test_71.soft_fail_to_hard()
class TestCase90(TestCase46):
    def test___tableDefFieldLookupNotFoundBubbles__983(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_72: Test = Test()
        try:
            t_2250: 'SafeIdentifier'
            t_2250 = safe_identifier('users')
            t_2251: 'SafeIdentifier' = t_2250
            t_2252: 'SafeIdentifier'
            t_2252 = safe_identifier('name')
            t_2253: 'SafeIdentifier' = t_2252
            t_4256: 'StringField' = StringField()
            t_4257: 'FieldDef' = FieldDef(t_2253, t_4256, False)
            td_678: 'TableDef' = TableDef(t_2251, (t_4257,))
            did_bubble_679: 'bool33'
            try:
                td_678.field('nonexistent')
                did_bubble_679 = False
            except Exception37:
                did_bubble_679 = True
            def fn_4255() -> 'str27':
                return 'unknown field should bubble'
            test_72.assert_(did_bubble_679, fn_4255)
        finally:
            test_72.soft_fail_to_hard()
class TestCase91(TestCase46):
    def test___fieldDefNullableFlag__984(self) -> None:
        'FieldDef nullable flag'
        test_73: Test = Test()
        try:
            t_2238: 'SafeIdentifier'
            t_2238 = safe_identifier('email')
            t_2239: 'SafeIdentifier' = t_2238
            t_4244: 'StringField' = StringField()
            required_681: 'FieldDef' = FieldDef(t_2239, t_4244, False)
            t_2242: 'SafeIdentifier'
            t_2242 = safe_identifier('bio')
            t_2243: 'SafeIdentifier' = t_2242
            t_4246: 'StringField' = StringField()
            optional_682: 'FieldDef' = FieldDef(t_2243, t_4246, True)
            t_4250: 'bool33' = not required_681.nullable
            def fn_4243() -> 'str27':
                return 'required field should not be nullable'
            test_73.assert_(t_4250, fn_4243)
            t_4252: 'bool33' = optional_682.nullable
            def fn_4242() -> 'str27':
                return 'optional field should be nullable'
            test_73.assert_(t_4252, fn_4242)
        finally:
            test_73.soft_fail_to_hard()
class TestCase92(TestCase46):
    def test___stringEscaping__985(self) -> None:
        'string escaping'
        test_77: Test = Test()
        try:
            def build_808(name_810: 'str27') -> 'str27':
                t_4224: 'SqlBuilder' = SqlBuilder()
                t_4224.append_safe('select * from hi where name = ')
                t_4224.append_string(name_810)
                return t_4224.accumulated.to_string()
            def build_wrong_809(name_812: 'str27') -> 'str27':
                return str_cat_5119("select * from hi where name = '", name_812, "'")
            actual_987: 'str27' = build_808('world')
            t_4234: 'bool33' = actual_987 == "select * from hi where name = 'world'"
            def fn_4231() -> 'str27':
                return str_cat_5119('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_987, ')')
            test_77.assert_(t_4234, fn_4231)
            bobby_tables_814: 'str27' = "Robert'); drop table hi;--"
            actual_989: 'str27' = build_808("Robert'); drop table hi;--")
            t_4238: 'bool33' = actual_989 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_4230() -> 'str27':
                return str_cat_5119('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_989, ')')
            test_77.assert_(t_4238, fn_4230)
            def fn_4229() -> 'str27':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_77.assert_(True, fn_4229)
        finally:
            test_77.soft_fail_to_hard()
class TestCase93(TestCase46):
    def test___stringEdgeCases__993(self) -> None:
        'string edge cases'
        test_78: Test = Test()
        try:
            t_4192: 'SqlBuilder' = SqlBuilder()
            t_4192.append_safe('v = ')
            t_4192.append_string('')
            actual_994: 'str27' = t_4192.accumulated.to_string()
            t_4198: 'bool33' = actual_994 == "v = ''"
            def fn_4191() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_994, ')')
            test_78.assert_(t_4198, fn_4191)
            t_4200: 'SqlBuilder' = SqlBuilder()
            t_4200.append_safe('v = ')
            t_4200.append_string("a''b")
            actual_997: 'str27' = t_4200.accumulated.to_string()
            t_4206: 'bool33' = actual_997 == "v = 'a''''b'"
            def fn_4190() -> 'str27':
                return str_cat_5119("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_997, ')')
            test_78.assert_(t_4206, fn_4190)
            t_4208: 'SqlBuilder' = SqlBuilder()
            t_4208.append_safe('v = ')
            t_4208.append_string('Hello \u4e16\u754c')
            actual_1000: 'str27' = t_4208.accumulated.to_string()
            t_4214: 'bool33' = actual_1000 == "v = 'Hello \u4e16\u754c'"
            def fn_4189() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_1000, ')')
            test_78.assert_(t_4214, fn_4189)
            t_4216: 'SqlBuilder' = SqlBuilder()
            t_4216.append_safe('v = ')
            t_4216.append_string('Line1\nLine2')
            actual_1003: 'str27' = t_4216.accumulated.to_string()
            t_4222: 'bool33' = actual_1003 == "v = 'Line1\nLine2'"
            def fn_4188() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_1003, ')')
            test_78.assert_(t_4222, fn_4188)
        finally:
            test_78.soft_fail_to_hard()
class TestCase94(TestCase46):
    def test___numbersAndBooleans__1006(self) -> None:
        'numbers and booleans'
        test_79: Test = Test()
        try:
            t_4163: 'SqlBuilder' = SqlBuilder()
            t_4163.append_safe('select ')
            t_4163.append_int32(42)
            t_4163.append_safe(', ')
            t_4163.append_int64(43)
            t_4163.append_safe(', ')
            t_4163.append_float64(19.99)
            t_4163.append_safe(', ')
            t_4163.append_boolean(True)
            t_4163.append_safe(', ')
            t_4163.append_boolean(False)
            actual_1007: 'str27' = t_4163.accumulated.to_string()
            t_4177: 'bool33' = actual_1007 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_4162() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_1007, ')')
            test_79.assert_(t_4177, fn_4162)
            t_2183: 'date26'
            t_2183 = date_5144(2024, 12, 25)
            date_817: 'date26' = t_2183
            t_4179: 'SqlBuilder' = SqlBuilder()
            t_4179.append_safe('insert into t values (')
            t_4179.append_date(date_817)
            t_4179.append_safe(')')
            actual_1010: 'str27' = t_4179.accumulated.to_string()
            t_4186: 'bool33' = actual_1010 == "insert into t values ('2024-12-25')"
            def fn_4161() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_1010, ')')
            test_79.assert_(t_4186, fn_4161)
        finally:
            test_79.soft_fail_to_hard()
class TestCase95(TestCase46):
    def test___lists__1013(self) -> None:
        'lists'
        test_80: Test = Test()
        try:
            t_4107: 'SqlBuilder' = SqlBuilder()
            t_4107.append_safe('v IN (')
            t_4107.append_string_list(('a', 'b', "c'd"))
            t_4107.append_safe(')')
            actual_1014: 'str27' = t_4107.accumulated.to_string()
            t_4114: 'bool33' = actual_1014 == "v IN ('a', 'b', 'c''d')"
            def fn_4106() -> 'str27':
                return str_cat_5119("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_1014, ')')
            test_80.assert_(t_4114, fn_4106)
            t_4116: 'SqlBuilder' = SqlBuilder()
            t_4116.append_safe('v IN (')
            t_4116.append_int32_list((1, 2, 3))
            t_4116.append_safe(')')
            actual_1017: 'str27' = t_4116.accumulated.to_string()
            t_4123: 'bool33' = actual_1017 == 'v IN (1, 2, 3)'
            def fn_4105() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_1017, ')')
            test_80.assert_(t_4123, fn_4105)
            t_4125: 'SqlBuilder' = SqlBuilder()
            t_4125.append_safe('v IN (')
            t_4125.append_int64_list((1, 2))
            t_4125.append_safe(')')
            actual_1020: 'str27' = t_4125.accumulated.to_string()
            t_4132: 'bool33' = actual_1020 == 'v IN (1, 2)'
            def fn_4104() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_1020, ')')
            test_80.assert_(t_4132, fn_4104)
            t_4134: 'SqlBuilder' = SqlBuilder()
            t_4134.append_safe('v IN (')
            t_4134.append_float64_list((1.0, 2.0))
            t_4134.append_safe(')')
            actual_1023: 'str27' = t_4134.accumulated.to_string()
            t_4141: 'bool33' = actual_1023 == 'v IN (1.0, 2.0)'
            def fn_4103() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_1023, ')')
            test_80.assert_(t_4141, fn_4103)
            t_4143: 'SqlBuilder' = SqlBuilder()
            t_4143.append_safe('v IN (')
            t_4143.append_boolean_list((True, False))
            t_4143.append_safe(')')
            actual_1026: 'str27' = t_4143.accumulated.to_string()
            t_4150: 'bool33' = actual_1026 == 'v IN (TRUE, FALSE)'
            def fn_4102() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_1026, ')')
            test_80.assert_(t_4150, fn_4102)
            t_2155: 'date26'
            t_2155 = date_5144(2024, 1, 1)
            t_2156: 'date26' = t_2155
            t_2157: 'date26'
            t_2157 = date_5144(2024, 12, 25)
            t_2158: 'date26' = t_2157
            dates_819: 'Sequence29[date26]' = (t_2156, t_2158)
            t_4152: 'SqlBuilder' = SqlBuilder()
            t_4152.append_safe('v IN (')
            t_4152.append_date_list(dates_819)
            t_4152.append_safe(')')
            actual_1029: 'str27' = t_4152.accumulated.to_string()
            t_4159: 'bool33' = actual_1029 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_4101() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_1029, ')')
            test_80.assert_(t_4159, fn_4101)
        finally:
            test_80.soft_fail_to_hard()
class TestCase96(TestCase46):
    def test___sqlFloat64_naNRendersAsNull__1032(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_81: Test = Test()
        try:
            nan_821: 'float38'
            nan_821 = 0.0 / 0.0
            t_4093: 'SqlBuilder' = SqlBuilder()
            t_4093.append_safe('v = ')
            t_4093.append_float64(nan_821)
            actual_1033: 'str27' = t_4093.accumulated.to_string()
            t_4099: 'bool33' = actual_1033 == 'v = NULL'
            def fn_4092() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_1033, ')')
            test_81.assert_(t_4099, fn_4092)
        finally:
            test_81.soft_fail_to_hard()
class TestCase97(TestCase46):
    def test___sqlFloat64_infinityRendersAsNull__1036(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_82: Test = Test()
        try:
            inf_823: 'float38'
            inf_823 = 1.0 / 0.0
            t_4084: 'SqlBuilder' = SqlBuilder()
            t_4084.append_safe('v = ')
            t_4084.append_float64(inf_823)
            actual_1037: 'str27' = t_4084.accumulated.to_string()
            t_4090: 'bool33' = actual_1037 == 'v = NULL'
            def fn_4083() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_1037, ')')
            test_82.assert_(t_4090, fn_4083)
        finally:
            test_82.soft_fail_to_hard()
class TestCase98(TestCase46):
    def test___sqlFloat64_negativeInfinityRendersAsNull__1040(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_83: Test = Test()
        try:
            ninf_825: 'float38'
            ninf_825 = -1.0 / 0.0
            t_4075: 'SqlBuilder' = SqlBuilder()
            t_4075.append_safe('v = ')
            t_4075.append_float64(ninf_825)
            actual_1041: 'str27' = t_4075.accumulated.to_string()
            t_4081: 'bool33' = actual_1041 == 'v = NULL'
            def fn_4074() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_1041, ')')
            test_83.assert_(t_4081, fn_4074)
        finally:
            test_83.soft_fail_to_hard()
class TestCase99(TestCase46):
    def test___sqlFloat64_normalValuesStillWork__1044(self) -> None:
        'SqlFloat64 normal values still work'
        test_84: Test = Test()
        try:
            t_4050: 'SqlBuilder' = SqlBuilder()
            t_4050.append_safe('v = ')
            t_4050.append_float64(3.14)
            actual_1045: 'str27' = t_4050.accumulated.to_string()
            t_4056: 'bool33' = actual_1045 == 'v = 3.14'
            def fn_4049() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_1045, ')')
            test_84.assert_(t_4056, fn_4049)
            t_4058: 'SqlBuilder' = SqlBuilder()
            t_4058.append_safe('v = ')
            t_4058.append_float64(0.0)
            actual_1048: 'str27' = t_4058.accumulated.to_string()
            t_4064: 'bool33' = actual_1048 == 'v = 0.0'
            def fn_4048() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_1048, ')')
            test_84.assert_(t_4064, fn_4048)
            t_4066: 'SqlBuilder' = SqlBuilder()
            t_4066.append_safe('v = ')
            t_4066.append_float64(-42.5)
            actual_1051: 'str27' = t_4066.accumulated.to_string()
            t_4072: 'bool33' = actual_1051 == 'v = -42.5'
            def fn_4047() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_1051, ')')
            test_84.assert_(t_4072, fn_4047)
        finally:
            test_84.soft_fail_to_hard()
class TestCase100(TestCase46):
    def test___sqlDateRendersWithQuotes__1054(self) -> None:
        'SqlDate renders with quotes'
        test_85: Test = Test()
        try:
            t_2051: 'date26'
            t_2051 = date_5144(2024, 6, 15)
            d_828: 'date26' = t_2051
            t_4039: 'SqlBuilder' = SqlBuilder()
            t_4039.append_safe('v = ')
            t_4039.append_date(d_828)
            actual_1055: 'str27' = t_4039.accumulated.to_string()
            t_4045: 'bool33' = actual_1055 == "v = '2024-06-15'"
            def fn_4038() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_1055, ')')
            test_85.assert_(t_4045, fn_4038)
        finally:
            test_85.soft_fail_to_hard()
class TestCase101(TestCase46):
    def test___nesting__1058(self) -> None:
        'nesting'
        test_86: Test = Test()
        try:
            name_830: 'str27' = 'Someone'
            t_4007: 'SqlBuilder' = SqlBuilder()
            t_4007.append_safe('where p.last_name = ')
            t_4007.append_string('Someone')
            condition_831: 'SqlFragment' = t_4007.accumulated
            t_4011: 'SqlBuilder' = SqlBuilder()
            t_4011.append_safe('select p.id from person p ')
            t_4011.append_fragment(condition_831)
            actual_1060: 'str27' = t_4011.accumulated.to_string()
            t_4017: 'bool33' = actual_1060 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_4006() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1060, ')')
            test_86.assert_(t_4017, fn_4006)
            t_4019: 'SqlBuilder' = SqlBuilder()
            t_4019.append_safe('select p.id from person p ')
            t_4019.append_part(condition_831.to_source())
            actual_1063: 'str27' = t_4019.accumulated.to_string()
            t_4026: 'bool33' = actual_1063 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_4005() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_1063, ')')
            test_86.assert_(t_4026, fn_4005)
            parts_832: 'Sequence29[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_4030: 'SqlBuilder' = SqlBuilder()
            t_4030.append_safe('select ')
            t_4030.append_part_list(parts_832)
            actual_1066: 'str27' = t_4030.accumulated.to_string()
            t_4036: 'bool33' = actual_1066 == "select 'a''b', 3"
            def fn_4004() -> 'str27':
                return str_cat_5119('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_1066, ')')
            test_86.assert_(t_4036, fn_4004)
        finally:
            test_86.soft_fail_to_hard()
