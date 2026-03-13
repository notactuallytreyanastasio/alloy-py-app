from temper_std.testing import Test
from builtins import str as str34, bool as bool42, Exception as Exception46, int as int40, float as float36
from unittest import TestCase as TestCase53
from types import MappingProxyType as MappingProxyType41
from typing import Sequence as Sequence38, MutableSequence as MutableSequence43
from datetime import date as date33
from orm.src import SafeIdentifier, safe_identifier, TableDef, FieldDef, StringField, IntField, FloatField, BoolField, map_constructor_17421, pair_17422, changeset, Changeset, mapped_has_17388, len_17389, list_get_17397, str_cat_17392, list_for_each_17386, SqlFragment, NumberValidationOpts, SqlDefault, timestamps, list_17379, tuple_17381, delete_sql, int_to_string_17391, Int64Field, DateField, from_, Query, SqlBuilder, col, SqlInt32, SqlString, count_all, count_col, sum_col, avg_col, min_col, max_col, union_sql, union_all_sql, intersect_sql, except_sql, subquery, exists_sql, update, UpdateQuery, SqlBoolean, delete_from, DeleteQuery, NullsFirst, NullsLast, ForUpdate, ForShare, date_17423, SqlPart
def csid_703(name_985: 'str34') -> 'SafeIdentifier':
    t_9421: 'SafeIdentifier'
    t_9421 = safe_identifier(name_985)
    return t_9421
def user_table_704() -> 'TableDef':
    return TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('email'), StringField(), False, None, False), FieldDef(csid_703('age'), IntField(), True, None, False), FieldDef(csid_703('score'), FloatField(), True, None, False), FieldDef(csid_703('active'), BoolField(), True, None, False)), None)
class TestCase52(TestCase53):
    def test___castWhitelistsAllowedFields__2272(self) -> None:
        'cast whitelists allowed fields'
        test_32: Test = Test()
        try:
            params_989: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('email', 'alice@example.com'), pair_17422('admin', 'true')))
            t_16959: 'TableDef' = user_table_704()
            t_16960: 'SafeIdentifier' = csid_703('name')
            t_16961: 'SafeIdentifier' = csid_703('email')
            cs_990: 'Changeset' = changeset(t_16959, params_989).cast((t_16960, t_16961))
            t_16964: 'bool42' = mapped_has_17388(cs_990.changes, 'name')
            def fn_16954() -> 'str34':
                return 'name should be in changes'
            test_32.assert_(t_16964, fn_16954)
            t_16968: 'bool42' = mapped_has_17388(cs_990.changes, 'email')
            def fn_16953() -> 'str34':
                return 'email should be in changes'
            test_32.assert_(t_16968, fn_16953)
            t_16974: 'bool42' = not mapped_has_17388(cs_990.changes, 'admin')
            def fn_16952() -> 'str34':
                return 'admin must be dropped (not in whitelist)'
            test_32.assert_(t_16974, fn_16952)
            t_16976: 'bool42' = cs_990.is_valid
            def fn_16951() -> 'str34':
                return 'should still be valid'
            test_32.assert_(t_16976, fn_16951)
        finally:
            test_32.soft_fail_to_hard()
class TestCase54(TestCase53):
    def test___castIsReplacingNotAdditiveSecondCallResetsWhitelist__2273(self) -> None:
        'cast is replacing not additive \u2014 second call resets whitelist'
        test_33: Test = Test()
        try:
            params_992: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('email', 'alice@example.com')))
            t_16937: 'TableDef' = user_table_704()
            t_16938: 'SafeIdentifier' = csid_703('name')
            cs_993: 'Changeset' = changeset(t_16937, params_992).cast((t_16938,)).cast((csid_703('email'),))
            t_16945: 'bool42' = not mapped_has_17388(cs_993.changes, 'name')
            def fn_16933() -> 'str34':
                return 'name must be excluded by second cast'
            test_33.assert_(t_16945, fn_16933)
            t_16948: 'bool42' = mapped_has_17388(cs_993.changes, 'email')
            def fn_16932() -> 'str34':
                return 'email should be present'
            test_33.assert_(t_16948, fn_16932)
        finally:
            test_33.soft_fail_to_hard()
class TestCase55(TestCase53):
    def test___castIgnoresEmptyStringValues__2274(self) -> None:
        'cast ignores empty string values'
        test_34: Test = Test()
        try:
            params_995: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', ''), pair_17422('email', 'bob@example.com')))
            t_16919: 'TableDef' = user_table_704()
            t_16920: 'SafeIdentifier' = csid_703('name')
            t_16921: 'SafeIdentifier' = csid_703('email')
            cs_996: 'Changeset' = changeset(t_16919, params_995).cast((t_16920, t_16921))
            t_16926: 'bool42' = not mapped_has_17388(cs_996.changes, 'name')
            def fn_16915() -> 'str34':
                return 'empty name should not be in changes'
            test_34.assert_(t_16926, fn_16915)
            t_16929: 'bool42' = mapped_has_17388(cs_996.changes, 'email')
            def fn_16914() -> 'str34':
                return 'email should be in changes'
            test_34.assert_(t_16929, fn_16914)
        finally:
            test_34.soft_fail_to_hard()
class TestCase56(TestCase53):
    def test___validateRequiredPassesWhenFieldPresent__2275(self) -> None:
        'validateRequired passes when field present'
        test_35: Test = Test()
        try:
            params_998: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16901: 'TableDef' = user_table_704()
            t_16902: 'SafeIdentifier' = csid_703('name')
            cs_999: 'Changeset' = changeset(t_16901, params_998).cast((t_16902,)).validate_required((csid_703('name'),))
            t_16906: 'bool42' = cs_999.is_valid
            def fn_16898() -> 'str34':
                return 'should be valid'
            test_35.assert_(t_16906, fn_16898)
            t_16912: 'bool42' = len_17389(cs_999.errors) == 0
            def fn_16897() -> 'str34':
                return 'no errors expected'
            test_35.assert_(t_16912, fn_16897)
        finally:
            test_35.soft_fail_to_hard()
class TestCase57(TestCase53):
    def test___validateRequiredFailsWhenFieldMissing__2276(self) -> None:
        'validateRequired fails when field missing'
        test_36: Test = Test()
        try:
            params_1001: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_16877: 'TableDef' = user_table_704()
            t_16878: 'SafeIdentifier' = csid_703('name')
            cs_1002: 'Changeset' = changeset(t_16877, params_1001).cast((t_16878,)).validate_required((csid_703('name'),))
            t_16884: 'bool42' = not cs_1002.is_valid
            def fn_16875() -> 'str34':
                return 'should be invalid'
            test_36.assert_(t_16884, fn_16875)
            t_16889: 'bool42' = len_17389(cs_1002.errors) == 1
            def fn_16874() -> 'str34':
                return 'should have one error'
            test_36.assert_(t_16889, fn_16874)
            t_16895: 'bool42' = list_get_17397(cs_1002.errors, 0).field == 'name'
            def fn_16873() -> 'str34':
                return 'error should name the field'
            test_36.assert_(t_16895, fn_16873)
        finally:
            test_36.soft_fail_to_hard()
class TestCase58(TestCase53):
    def test___validateLengthPassesWithinRange__2277(self) -> None:
        'validateLength passes within range'
        test_37: Test = Test()
        try:
            params_1004: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16865: 'TableDef' = user_table_704()
            t_16866: 'SafeIdentifier' = csid_703('name')
            cs_1005: 'Changeset' = changeset(t_16865, params_1004).cast((t_16866,)).validate_length(csid_703('name'), 2, 50)
            t_16870: 'bool42' = cs_1005.is_valid
            def fn_16862() -> 'str34':
                return 'should be valid'
            test_37.assert_(t_16870, fn_16862)
        finally:
            test_37.soft_fail_to_hard()
class TestCase59(TestCase53):
    def test___validateLengthFailsWhenTooShort__2278(self) -> None:
        'validateLength fails when too short'
        test_38: Test = Test()
        try:
            params_1007: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'A'),))
            t_16853: 'TableDef' = user_table_704()
            t_16854: 'SafeIdentifier' = csid_703('name')
            cs_1008: 'Changeset' = changeset(t_16853, params_1007).cast((t_16854,)).validate_length(csid_703('name'), 2, 50)
            t_16860: 'bool42' = not cs_1008.is_valid
            def fn_16850() -> 'str34':
                return 'should be invalid'
            test_38.assert_(t_16860, fn_16850)
        finally:
            test_38.soft_fail_to_hard()
class TestCase60(TestCase53):
    def test___validateLengthFailsWhenTooLong__2279(self) -> None:
        'validateLength fails when too long'
        test_39: Test = Test()
        try:
            params_1010: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),))
            t_16841: 'TableDef' = user_table_704()
            t_16842: 'SafeIdentifier' = csid_703('name')
            cs_1011: 'Changeset' = changeset(t_16841, params_1010).cast((t_16842,)).validate_length(csid_703('name'), 2, 10)
            t_16848: 'bool42' = not cs_1011.is_valid
            def fn_16838() -> 'str34':
                return 'should be invalid'
            test_39.assert_(t_16848, fn_16838)
        finally:
            test_39.soft_fail_to_hard()
class TestCase61(TestCase53):
    def test___validateIntPassesForValidInteger__2280(self) -> None:
        'validateInt passes for valid integer'
        test_40: Test = Test()
        try:
            params_1013: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '30'),))
            t_16830: 'TableDef' = user_table_704()
            t_16831: 'SafeIdentifier' = csid_703('age')
            cs_1014: 'Changeset' = changeset(t_16830, params_1013).cast((t_16831,)).validate_int(csid_703('age'))
            t_16835: 'bool42' = cs_1014.is_valid
            def fn_16827() -> 'str34':
                return 'should be valid'
            test_40.assert_(t_16835, fn_16827)
        finally:
            test_40.soft_fail_to_hard()
class TestCase62(TestCase53):
    def test___validateIntFailsForNonInteger__2281(self) -> None:
        'validateInt fails for non-integer'
        test_41: Test = Test()
        try:
            params_1016: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', 'not-a-number'),))
            t_16818: 'TableDef' = user_table_704()
            t_16819: 'SafeIdentifier' = csid_703('age')
            cs_1017: 'Changeset' = changeset(t_16818, params_1016).cast((t_16819,)).validate_int(csid_703('age'))
            t_16825: 'bool42' = not cs_1017.is_valid
            def fn_16815() -> 'str34':
                return 'should be invalid'
            test_41.assert_(t_16825, fn_16815)
        finally:
            test_41.soft_fail_to_hard()
class TestCase63(TestCase53):
    def test___validateFloatPassesForValidFloat__2282(self) -> None:
        'validateFloat passes for valid float'
        test_42: Test = Test()
        try:
            params_1019: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '9.5'),))
            t_16807: 'TableDef' = user_table_704()
            t_16808: 'SafeIdentifier' = csid_703('score')
            cs_1020: 'Changeset' = changeset(t_16807, params_1019).cast((t_16808,)).validate_float(csid_703('score'))
            t_16812: 'bool42' = cs_1020.is_valid
            def fn_16804() -> 'str34':
                return 'should be valid'
            test_42.assert_(t_16812, fn_16804)
        finally:
            test_42.soft_fail_to_hard()
class TestCase64(TestCase53):
    def test___validateInt64_passesForValid64_bitInteger__2283(self) -> None:
        'validateInt64 passes for valid 64-bit integer'
        test_43: Test = Test()
        try:
            params_1022: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '9999999999'),))
            t_16796: 'TableDef' = user_table_704()
            t_16797: 'SafeIdentifier' = csid_703('age')
            cs_1023: 'Changeset' = changeset(t_16796, params_1022).cast((t_16797,)).validate_int64(csid_703('age'))
            t_16801: 'bool42' = cs_1023.is_valid
            def fn_16793() -> 'str34':
                return 'should be valid'
            test_43.assert_(t_16801, fn_16793)
        finally:
            test_43.soft_fail_to_hard()
class TestCase65(TestCase53):
    def test___validateInt64_failsForNonInteger__2284(self) -> None:
        'validateInt64 fails for non-integer'
        test_44: Test = Test()
        try:
            params_1025: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', 'not-a-number'),))
            t_16784: 'TableDef' = user_table_704()
            t_16785: 'SafeIdentifier' = csid_703('age')
            cs_1026: 'Changeset' = changeset(t_16784, params_1025).cast((t_16785,)).validate_int64(csid_703('age'))
            t_16791: 'bool42' = not cs_1026.is_valid
            def fn_16781() -> 'str34':
                return 'should be invalid'
            test_44.assert_(t_16791, fn_16781)
        finally:
            test_44.soft_fail_to_hard()
class TestCase66(TestCase53):
    def test___validateBoolAcceptsTrue1_yesOn__2285(self) -> None:
        'validateBool accepts true/1/yes/on'
        test_45: Test = Test()
        try:
            def fn_16778(v_1028: 'str34') -> 'None':
                params_1029: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('active', v_1028),))
                t_16770: 'TableDef' = user_table_704()
                t_16771: 'SafeIdentifier' = csid_703('active')
                cs_1030: 'Changeset' = changeset(t_16770, params_1029).cast((t_16771,)).validate_bool(csid_703('active'))
                t_16775: 'bool42' = cs_1030.is_valid
                def fn_16767() -> 'str34':
                    return str_cat_17392('should accept: ', v_1028)
                test_45.assert_(t_16775, fn_16767)
            list_for_each_17386(('true', '1', 'yes', 'on'), fn_16778)
        finally:
            test_45.soft_fail_to_hard()
class TestCase67(TestCase53):
    def test___validateBoolAcceptsFalse0_noOff__2286(self) -> None:
        'validateBool accepts false/0/no/off'
        test_46: Test = Test()
        try:
            def fn_16764(v_1032: 'str34') -> 'None':
                params_1033: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('active', v_1032),))
                t_16756: 'TableDef' = user_table_704()
                t_16757: 'SafeIdentifier' = csid_703('active')
                cs_1034: 'Changeset' = changeset(t_16756, params_1033).cast((t_16757,)).validate_bool(csid_703('active'))
                t_16761: 'bool42' = cs_1034.is_valid
                def fn_16753() -> 'str34':
                    return str_cat_17392('should accept: ', v_1032)
                test_46.assert_(t_16761, fn_16753)
            list_for_each_17386(('false', '0', 'no', 'off'), fn_16764)
        finally:
            test_46.soft_fail_to_hard()
class TestCase68(TestCase53):
    def test___validateBoolRejectsAmbiguousValues__2287(self) -> None:
        'validateBool rejects ambiguous values'
        test_47: Test = Test()
        try:
            def fn_16750(v_1036: 'str34') -> 'None':
                params_1037: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('active', v_1036),))
                t_16741: 'TableDef' = user_table_704()
                t_16742: 'SafeIdentifier' = csid_703('active')
                cs_1038: 'Changeset' = changeset(t_16741, params_1037).cast((t_16742,)).validate_bool(csid_703('active'))
                t_16748: 'bool42' = not cs_1038.is_valid
                def fn_16738() -> 'str34':
                    return str_cat_17392('should reject ambiguous: ', v_1036)
                test_47.assert_(t_16748, fn_16738)
            list_for_each_17386(('TRUE', 'Yes', 'maybe', '2', 'enabled'), fn_16750)
        finally:
            test_47.soft_fail_to_hard()
class TestCase69(TestCase53):
    def test___toInsertSqlEscapesBobbyTables__2288(self) -> None:
        'toInsertSql escapes Bobby Tables'
        test_48: Test = Test()
        try:
            params_1040: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', "Robert'); DROP TABLE users;--"), pair_17422('email', 'bobby@evil.com')))
            t_16726: 'TableDef' = user_table_704()
            t_16727: 'SafeIdentifier' = csid_703('name')
            t_16728: 'SafeIdentifier' = csid_703('email')
            cs_1041: 'Changeset' = changeset(t_16726, params_1040).cast((t_16727, t_16728)).validate_required((csid_703('name'), csid_703('email')))
            t_9222: 'SqlFragment'
            t_9222 = cs_1041.to_insert_sql()
            sql_frag_1042: 'SqlFragment' = t_9222
            s_1043: 'str34' = sql_frag_1042.to_string()
            t_16735: 'bool42' = s_1043.find("''") >= 0
            def fn_16722() -> 'str34':
                return str_cat_17392('single quote must be doubled: ', s_1043)
            test_48.assert_(t_16735, fn_16722)
        finally:
            test_48.soft_fail_to_hard()
class TestCase70(TestCase53):
    def test___toInsertSqlProducesCorrectSqlForStringField__2289(self) -> None:
        'toInsertSql produces correct SQL for string field'
        test_49: Test = Test()
        try:
            params_1045: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('email', 'a@example.com')))
            t_16706: 'TableDef' = user_table_704()
            t_16707: 'SafeIdentifier' = csid_703('name')
            t_16708: 'SafeIdentifier' = csid_703('email')
            cs_1046: 'Changeset' = changeset(t_16706, params_1045).cast((t_16707, t_16708)).validate_required((csid_703('name'), csid_703('email')))
            t_9201: 'SqlFragment'
            t_9201 = cs_1046.to_insert_sql()
            sql_frag_1047: 'SqlFragment' = t_9201
            s_1048: 'str34' = sql_frag_1047.to_string()
            t_16715: 'bool42' = s_1048.find('INSERT INTO users') >= 0
            def fn_16702() -> 'str34':
                return str_cat_17392('has INSERT INTO: ', s_1048)
            test_49.assert_(t_16715, fn_16702)
            t_16719: 'bool42' = s_1048.find("'Alice'") >= 0
            def fn_16701() -> 'str34':
                return str_cat_17392('has quoted name: ', s_1048)
            test_49.assert_(t_16719, fn_16701)
        finally:
            test_49.soft_fail_to_hard()
class TestCase71(TestCase53):
    def test___toInsertSqlProducesCorrectSqlForIntField__2290(self) -> None:
        'toInsertSql produces correct SQL for int field'
        test_50: Test = Test()
        try:
            params_1050: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Bob'), pair_17422('email', 'b@example.com'), pair_17422('age', '25')))
            t_16688: 'TableDef' = user_table_704()
            t_16689: 'SafeIdentifier' = csid_703('name')
            t_16690: 'SafeIdentifier' = csid_703('email')
            t_16691: 'SafeIdentifier' = csid_703('age')
            cs_1051: 'Changeset' = changeset(t_16688, params_1050).cast((t_16689, t_16690, t_16691)).validate_required((csid_703('name'), csid_703('email')))
            t_9184: 'SqlFragment'
            t_9184 = cs_1051.to_insert_sql()
            sql_frag_1052: 'SqlFragment' = t_9184
            s_1053: 'str34' = sql_frag_1052.to_string()
            t_16698: 'bool42' = s_1053.find('25') >= 0
            def fn_16683() -> 'str34':
                return str_cat_17392('age rendered unquoted: ', s_1053)
            test_50.assert_(t_16698, fn_16683)
        finally:
            test_50.soft_fail_to_hard()
class TestCase72(TestCase53):
    def test___toInsertSqlBubblesOnInvalidChangeset__2291(self) -> None:
        'toInsertSql bubbles on invalid changeset'
        test_51: Test = Test()
        try:
            params_1055: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_16676: 'TableDef' = user_table_704()
            t_16677: 'SafeIdentifier' = csid_703('name')
            cs_1056: 'Changeset' = changeset(t_16676, params_1055).cast((t_16677,)).validate_required((csid_703('name'),))
            did_bubble_1057: 'bool42'
            try:
                cs_1056.to_insert_sql()
                did_bubble_1057 = False
            except Exception46:
                did_bubble_1057 = True
            def fn_16674() -> 'str34':
                return 'invalid changeset should bubble'
            test_51.assert_(did_bubble_1057, fn_16674)
        finally:
            test_51.soft_fail_to_hard()
class TestCase73(TestCase53):
    def test___toInsertSqlEnforcesNonNullableFieldsIndependentlyOfIsValid__2292(self) -> None:
        'toInsertSql enforces non-nullable fields independently of isValid'
        test_52: Test = Test()
        try:
            strict_table_1059: 'TableDef' = TableDef(csid_703('posts'), (FieldDef(csid_703('title'), StringField(), False, None, False), FieldDef(csid_703('body'), StringField(), True, None, False)), None)
            params_1060: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('body', 'hello'),))
            t_16667: 'SafeIdentifier' = csid_703('body')
            cs_1061: 'Changeset' = changeset(strict_table_1059, params_1060).cast((t_16667,))
            t_16669: 'bool42' = cs_1061.is_valid
            def fn_16656() -> 'str34':
                return 'changeset should appear valid (no explicit validation run)'
            test_52.assert_(t_16669, fn_16656)
            did_bubble_1062: 'bool42'
            try:
                cs_1061.to_insert_sql()
                did_bubble_1062 = False
            except Exception46:
                did_bubble_1062 = True
            def fn_16655() -> 'str34':
                return 'toInsertSql should enforce nullable regardless of isValid'
            test_52.assert_(did_bubble_1062, fn_16655)
        finally:
            test_52.soft_fail_to_hard()
class TestCase74(TestCase53):
    def test___toUpdateSqlProducesCorrectSql__2293(self) -> None:
        'toUpdateSql produces correct SQL'
        test_53: Test = Test()
        try:
            params_1064: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Bob'),))
            t_16646: 'TableDef' = user_table_704()
            t_16647: 'SafeIdentifier' = csid_703('name')
            cs_1065: 'Changeset' = changeset(t_16646, params_1064).cast((t_16647,)).validate_required((csid_703('name'),))
            t_9144: 'SqlFragment'
            t_9144 = cs_1065.to_update_sql(42)
            sql_frag_1066: 'SqlFragment' = t_9144
            s_1067: 'str34' = sql_frag_1066.to_string()
            t_16653: 'bool42' = s_1067 == "UPDATE users SET name = 'Bob' WHERE id = 42"
            def fn_16643() -> 'str34':
                return str_cat_17392('got: ', s_1067)
            test_53.assert_(t_16653, fn_16643)
        finally:
            test_53.soft_fail_to_hard()
class TestCase75(TestCase53):
    def test___toUpdateSqlBubblesOnInvalidChangeset__2294(self) -> None:
        'toUpdateSql bubbles on invalid changeset'
        test_54: Test = Test()
        try:
            params_1069: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_16636: 'TableDef' = user_table_704()
            t_16637: 'SafeIdentifier' = csid_703('name')
            cs_1070: 'Changeset' = changeset(t_16636, params_1069).cast((t_16637,)).validate_required((csid_703('name'),))
            did_bubble_1071: 'bool42'
            try:
                cs_1070.to_update_sql(1)
                did_bubble_1071 = False
            except Exception46:
                did_bubble_1071 = True
            def fn_16634() -> 'str34':
                return 'invalid changeset should bubble'
            test_54.assert_(did_bubble_1071, fn_16634)
        finally:
            test_54.soft_fail_to_hard()
class TestCase76(TestCase53):
    def test___putChangeAddsANewField__2295(self) -> None:
        'putChange adds a new field'
        test_55: Test = Test()
        try:
            params_1073: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16620: 'TableDef' = user_table_704()
            t_16621: 'SafeIdentifier' = csid_703('name')
            cs_1074: 'Changeset' = changeset(t_16620, params_1073).cast((t_16621,)).put_change(csid_703('email'), 'alice@example.com')
            t_16626: 'bool42' = mapped_has_17388(cs_1074.changes, 'email')
            def fn_16617() -> 'str34':
                return 'email should be in changes'
            test_55.assert_(t_16626, fn_16617)
            t_16632: 'bool42' = cs_1074.changes.get('email', '') == 'alice@example.com'
            def fn_16616() -> 'str34':
                return 'email value'
            test_55.assert_(t_16632, fn_16616)
        finally:
            test_55.soft_fail_to_hard()
class TestCase77(TestCase53):
    def test___putChangeOverwritesExistingField__2296(self) -> None:
        'putChange overwrites existing field'
        test_56: Test = Test()
        try:
            params_1076: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16606: 'TableDef' = user_table_704()
            t_16607: 'SafeIdentifier' = csid_703('name')
            cs_1077: 'Changeset' = changeset(t_16606, params_1076).cast((t_16607,)).put_change(csid_703('name'), 'Bob')
            t_16614: 'bool42' = cs_1077.changes.get('name', '') == 'Bob'
            def fn_16603() -> 'str34':
                return 'name should be overwritten'
            test_56.assert_(t_16614, fn_16603)
        finally:
            test_56.soft_fail_to_hard()
class TestCase78(TestCase53):
    def test___putChangeValueAppearsInToInsertSql__2297(self) -> None:
        'putChange value appears in toInsertSql'
        test_57: Test = Test()
        try:
            params_1079: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('email', 'a@example.com')))
            t_16592: 'TableDef' = user_table_704()
            t_16593: 'SafeIdentifier' = csid_703('name')
            t_16594: 'SafeIdentifier' = csid_703('email')
            cs_1080: 'Changeset' = changeset(t_16592, params_1079).cast((t_16593, t_16594)).put_change(csid_703('name'), 'Bob')
            t_9099: 'SqlFragment'
            t_9099 = cs_1080.to_insert_sql()
            t_9100: 'SqlFragment' = t_9099
            s_1081: 'str34' = t_9100.to_string()
            t_16600: 'bool42' = s_1081.find("'Bob'") >= 0
            def fn_16588() -> 'str34':
                return str_cat_17392('should use putChange value: ', s_1081)
            test_57.assert_(t_16600, fn_16588)
        finally:
            test_57.soft_fail_to_hard()
class TestCase79(TestCase53):
    def test___getChangeReturnsValueForExistingField__2298(self) -> None:
        'getChange returns value for existing field'
        test_58: Test = Test()
        try:
            params_1083: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16581: 'TableDef' = user_table_704()
            t_16582: 'SafeIdentifier' = csid_703('name')
            cs_1084: 'Changeset' = changeset(t_16581, params_1083).cast((t_16582,))
            t_9087: 'str34'
            t_9087 = cs_1084.get_change(csid_703('name'))
            val_1085: 'str34' = t_9087
            t_16586: 'bool42' = val_1085 == 'Alice'
            def fn_16578() -> 'str34':
                return 'should return Alice'
            test_58.assert_(t_16586, fn_16578)
        finally:
            test_58.soft_fail_to_hard()
class TestCase80(TestCase53):
    def test___getChangeBubblesOnMissingField__2299(self) -> None:
        'getChange bubbles on missing field'
        test_59: Test = Test()
        try:
            params_1087: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16572: 'TableDef' = user_table_704()
            t_16573: 'SafeIdentifier' = csid_703('name')
            cs_1088: 'Changeset' = changeset(t_16572, params_1087).cast((t_16573,))
            did_bubble_1089: 'bool42'
            try:
                cs_1088.get_change(csid_703('email'))
                did_bubble_1089 = False
            except Exception46:
                did_bubble_1089 = True
            def fn_16569() -> 'str34':
                return 'should bubble for missing field'
            test_59.assert_(did_bubble_1089, fn_16569)
        finally:
            test_59.soft_fail_to_hard()
class TestCase81(TestCase53):
    def test___deleteChangeRemovesField__2300(self) -> None:
        'deleteChange removes field'
        test_60: Test = Test()
        try:
            params_1091: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('email', 'a@example.com')))
            t_16554: 'TableDef' = user_table_704()
            t_16555: 'SafeIdentifier' = csid_703('name')
            t_16556: 'SafeIdentifier' = csid_703('email')
            cs_1092: 'Changeset' = changeset(t_16554, params_1091).cast((t_16555, t_16556)).delete_change(csid_703('email'))
            t_16563: 'bool42' = not mapped_has_17388(cs_1092.changes, 'email')
            def fn_16550() -> 'str34':
                return 'email should be removed'
            test_60.assert_(t_16563, fn_16550)
            t_16566: 'bool42' = mapped_has_17388(cs_1092.changes, 'name')
            def fn_16549() -> 'str34':
                return 'name should remain'
            test_60.assert_(t_16566, fn_16549)
        finally:
            test_60.soft_fail_to_hard()
class TestCase82(TestCase53):
    def test___deleteChangeOnNonexistentFieldIsNoOp__2301(self) -> None:
        'deleteChange on nonexistent field is no-op'
        test_61: Test = Test()
        try:
            params_1094: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16537: 'TableDef' = user_table_704()
            t_16538: 'SafeIdentifier' = csid_703('name')
            cs_1095: 'Changeset' = changeset(t_16537, params_1094).cast((t_16538,)).delete_change(csid_703('email'))
            t_16543: 'bool42' = mapped_has_17388(cs_1095.changes, 'name')
            def fn_16534() -> 'str34':
                return 'name should still be present'
            test_61.assert_(t_16543, fn_16534)
            t_16546: 'bool42' = cs_1095.is_valid
            def fn_16533() -> 'str34':
                return 'should still be valid'
            test_61.assert_(t_16546, fn_16533)
        finally:
            test_61.soft_fail_to_hard()
class TestCase83(TestCase53):
    def test___validateInclusionPassesWhenValueInList__2302(self) -> None:
        'validateInclusion passes when value in list'
        test_62: Test = Test()
        try:
            params_1097: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'admin'),))
            t_16525: 'TableDef' = user_table_704()
            t_16526: 'SafeIdentifier' = csid_703('name')
            cs_1098: 'Changeset' = changeset(t_16525, params_1097).cast((t_16526,)).validate_inclusion(csid_703('name'), ('admin', 'user', 'guest'))
            t_16530: 'bool42' = cs_1098.is_valid
            def fn_16522() -> 'str34':
                return 'should be valid'
            test_62.assert_(t_16530, fn_16522)
        finally:
            test_62.soft_fail_to_hard()
class TestCase84(TestCase53):
    def test___validateInclusionFailsWhenValueNotInList__2303(self) -> None:
        'validateInclusion fails when value not in list'
        test_63: Test = Test()
        try:
            params_1100: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'hacker'),))
            t_16507: 'TableDef' = user_table_704()
            t_16508: 'SafeIdentifier' = csid_703('name')
            cs_1101: 'Changeset' = changeset(t_16507, params_1100).cast((t_16508,)).validate_inclusion(csid_703('name'), ('admin', 'user', 'guest'))
            t_16514: 'bool42' = not cs_1101.is_valid
            def fn_16504() -> 'str34':
                return 'should be invalid'
            test_63.assert_(t_16514, fn_16504)
            t_16520: 'bool42' = list_get_17397(cs_1101.errors, 0).field == 'name'
            def fn_16503() -> 'str34':
                return 'error on name'
            test_63.assert_(t_16520, fn_16503)
        finally:
            test_63.soft_fail_to_hard()
class TestCase85(TestCase53):
    def test___validateInclusionSkipsWhenFieldNotInChanges__2304(self) -> None:
        'validateInclusion skips when field not in changes'
        test_64: Test = Test()
        try:
            params_1103: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_16495: 'TableDef' = user_table_704()
            t_16496: 'SafeIdentifier' = csid_703('name')
            cs_1104: 'Changeset' = changeset(t_16495, params_1103).cast((t_16496,)).validate_inclusion(csid_703('name'), ('admin', 'user'))
            t_16500: 'bool42' = cs_1104.is_valid
            def fn_16493() -> 'str34':
                return 'should be valid when field absent'
            test_64.assert_(t_16500, fn_16493)
        finally:
            test_64.soft_fail_to_hard()
class TestCase86(TestCase53):
    def test___validateExclusionPassesWhenValueNotInList__2305(self) -> None:
        'validateExclusion passes when value not in list'
        test_65: Test = Test()
        try:
            params_1106: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16485: 'TableDef' = user_table_704()
            t_16486: 'SafeIdentifier' = csid_703('name')
            cs_1107: 'Changeset' = changeset(t_16485, params_1106).cast((t_16486,)).validate_exclusion(csid_703('name'), ('root', 'admin', 'superuser'))
            t_16490: 'bool42' = cs_1107.is_valid
            def fn_16482() -> 'str34':
                return 'should be valid'
            test_65.assert_(t_16490, fn_16482)
        finally:
            test_65.soft_fail_to_hard()
class TestCase87(TestCase53):
    def test___validateExclusionFailsWhenValueInList__2306(self) -> None:
        'validateExclusion fails when value in list'
        test_66: Test = Test()
        try:
            params_1109: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'admin'),))
            t_16467: 'TableDef' = user_table_704()
            t_16468: 'SafeIdentifier' = csid_703('name')
            cs_1110: 'Changeset' = changeset(t_16467, params_1109).cast((t_16468,)).validate_exclusion(csid_703('name'), ('root', 'admin', 'superuser'))
            t_16474: 'bool42' = not cs_1110.is_valid
            def fn_16464() -> 'str34':
                return 'should be invalid'
            test_66.assert_(t_16474, fn_16464)
            t_16480: 'bool42' = list_get_17397(cs_1110.errors, 0).field == 'name'
            def fn_16463() -> 'str34':
                return 'error on name'
            test_66.assert_(t_16480, fn_16463)
        finally:
            test_66.soft_fail_to_hard()
class TestCase88(TestCase53):
    def test___validateExclusionSkipsWhenFieldNotInChanges__2307(self) -> None:
        'validateExclusion skips when field not in changes'
        test_67: Test = Test()
        try:
            params_1112: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_16455: 'TableDef' = user_table_704()
            t_16456: 'SafeIdentifier' = csid_703('name')
            cs_1113: 'Changeset' = changeset(t_16455, params_1112).cast((t_16456,)).validate_exclusion(csid_703('name'), ('root', 'admin'))
            t_16460: 'bool42' = cs_1113.is_valid
            def fn_16453() -> 'str34':
                return 'should be valid when field absent'
            test_67.assert_(t_16460, fn_16453)
        finally:
            test_67.soft_fail_to_hard()
class TestCase89(TestCase53):
    def test___validateNumberGreaterThanPasses__2308(self) -> None:
        'validateNumber greaterThan passes'
        test_68: Test = Test()
        try:
            params_1115: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '25'),))
            t_16444: 'TableDef' = user_table_704()
            t_16445: 'SafeIdentifier' = csid_703('age')
            cs_1116: 'Changeset' = changeset(t_16444, params_1115).cast((t_16445,)).validate_number(csid_703('age'), NumberValidationOpts(18.0, None, None, None, None))
            t_16450: 'bool42' = cs_1116.is_valid
            def fn_16441() -> 'str34':
                return '25 > 18 should pass'
            test_68.assert_(t_16450, fn_16441)
        finally:
            test_68.soft_fail_to_hard()
class TestCase90(TestCase53):
    def test___validateNumberGreaterThanFails__2309(self) -> None:
        'validateNumber greaterThan fails'
        test_69: Test = Test()
        try:
            params_1118: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '15'),))
            t_16431: 'TableDef' = user_table_704()
            t_16432: 'SafeIdentifier' = csid_703('age')
            cs_1119: 'Changeset' = changeset(t_16431, params_1118).cast((t_16432,)).validate_number(csid_703('age'), NumberValidationOpts(18.0, None, None, None, None))
            t_16439: 'bool42' = not cs_1119.is_valid
            def fn_16428() -> 'str34':
                return '15 > 18 should fail'
            test_69.assert_(t_16439, fn_16428)
        finally:
            test_69.soft_fail_to_hard()
class TestCase91(TestCase53):
    def test___validateNumberLessThanPasses__2310(self) -> None:
        'validateNumber lessThan passes'
        test_70: Test = Test()
        try:
            params_1121: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '8.5'),))
            t_16419: 'TableDef' = user_table_704()
            t_16420: 'SafeIdentifier' = csid_703('score')
            cs_1122: 'Changeset' = changeset(t_16419, params_1121).cast((t_16420,)).validate_number(csid_703('score'), NumberValidationOpts(None, 10.0, None, None, None))
            t_16425: 'bool42' = cs_1122.is_valid
            def fn_16416() -> 'str34':
                return '8.5 < 10 should pass'
            test_70.assert_(t_16425, fn_16416)
        finally:
            test_70.soft_fail_to_hard()
class TestCase92(TestCase53):
    def test___validateNumberLessThanFails__2311(self) -> None:
        'validateNumber lessThan fails'
        test_71: Test = Test()
        try:
            params_1124: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '12.0'),))
            t_16406: 'TableDef' = user_table_704()
            t_16407: 'SafeIdentifier' = csid_703('score')
            cs_1125: 'Changeset' = changeset(t_16406, params_1124).cast((t_16407,)).validate_number(csid_703('score'), NumberValidationOpts(None, 10.0, None, None, None))
            t_16414: 'bool42' = not cs_1125.is_valid
            def fn_16403() -> 'str34':
                return '12 < 10 should fail'
            test_71.assert_(t_16414, fn_16403)
        finally:
            test_71.soft_fail_to_hard()
class TestCase93(TestCase53):
    def test___validateNumberGreaterThanOrEqualBoundary__2312(self) -> None:
        'validateNumber greaterThanOrEqual boundary'
        test_72: Test = Test()
        try:
            params_1127: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '18'),))
            t_16394: 'TableDef' = user_table_704()
            t_16395: 'SafeIdentifier' = csid_703('age')
            cs_1128: 'Changeset' = changeset(t_16394, params_1127).cast((t_16395,)).validate_number(csid_703('age'), NumberValidationOpts(None, None, 18.0, None, None))
            t_16400: 'bool42' = cs_1128.is_valid
            def fn_16391() -> 'str34':
                return '18 >= 18 should pass'
            test_72.assert_(t_16400, fn_16391)
        finally:
            test_72.soft_fail_to_hard()
class TestCase94(TestCase53):
    def test___validateNumberCombinedOptions__2313(self) -> None:
        'validateNumber combined options'
        test_73: Test = Test()
        try:
            params_1130: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '5.0'),))
            t_16382: 'TableDef' = user_table_704()
            t_16383: 'SafeIdentifier' = csid_703('score')
            cs_1131: 'Changeset' = changeset(t_16382, params_1130).cast((t_16383,)).validate_number(csid_703('score'), NumberValidationOpts(0.0, 10.0, None, None, None))
            t_16388: 'bool42' = cs_1131.is_valid
            def fn_16379() -> 'str34':
                return '5 > 0 and < 10 should pass'
            test_73.assert_(t_16388, fn_16379)
        finally:
            test_73.soft_fail_to_hard()
class TestCase95(TestCase53):
    def test___validateNumberNonNumericValue__2314(self) -> None:
        'validateNumber non-numeric value'
        test_74: Test = Test()
        try:
            params_1133: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', 'abc'),))
            t_16363: 'TableDef' = user_table_704()
            t_16364: 'SafeIdentifier' = csid_703('age')
            cs_1134: 'Changeset' = changeset(t_16363, params_1133).cast((t_16364,)).validate_number(csid_703('age'), NumberValidationOpts(0.0, None, None, None, None))
            t_16371: 'bool42' = not cs_1134.is_valid
            def fn_16360() -> 'str34':
                return 'non-numeric should fail'
            test_74.assert_(t_16371, fn_16360)
            t_16377: 'bool42' = list_get_17397(cs_1134.errors, 0).message == 'must be a number'
            def fn_16359() -> 'str34':
                return 'correct error message'
            test_74.assert_(t_16377, fn_16359)
        finally:
            test_74.soft_fail_to_hard()
class TestCase96(TestCase53):
    def test___validateNumberSkipsWhenFieldNotInChanges__2315(self) -> None:
        'validateNumber skips when field not in changes'
        test_75: Test = Test()
        try:
            params_1136: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_16350: 'TableDef' = user_table_704()
            t_16351: 'SafeIdentifier' = csid_703('age')
            cs_1137: 'Changeset' = changeset(t_16350, params_1136).cast((t_16351,)).validate_number(csid_703('age'), NumberValidationOpts(0.0, None, None, None, None))
            t_16356: 'bool42' = cs_1137.is_valid
            def fn_16348() -> 'str34':
                return 'should be valid when field absent'
            test_75.assert_(t_16356, fn_16348)
        finally:
            test_75.soft_fail_to_hard()
class TestCase97(TestCase53):
    def test___validateAcceptancePassesForTrueValues__2316(self) -> None:
        'validateAcceptance passes for true values'
        test_76: Test = Test()
        try:
            def fn_16345(v_1139: 'str34') -> 'None':
                params_1140: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('active', v_1139),))
                t_16337: 'TableDef' = user_table_704()
                t_16338: 'SafeIdentifier' = csid_703('active')
                cs_1141: 'Changeset' = changeset(t_16337, params_1140).cast((t_16338,)).validate_acceptance(csid_703('active'))
                t_16342: 'bool42' = cs_1141.is_valid
                def fn_16334() -> 'str34':
                    return str_cat_17392('should accept: ', v_1139)
                test_76.assert_(t_16342, fn_16334)
            list_for_each_17386(('true', '1', 'yes', 'on'), fn_16345)
        finally:
            test_76.soft_fail_to_hard()
class TestCase98(TestCase53):
    def test___validateAcceptanceFailsForNonTrueValues__2317(self) -> None:
        'validateAcceptance fails for non-true values'
        test_77: Test = Test()
        try:
            params_1143: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('active', 'false'),))
            t_16319: 'TableDef' = user_table_704()
            t_16320: 'SafeIdentifier' = csid_703('active')
            cs_1144: 'Changeset' = changeset(t_16319, params_1143).cast((t_16320,)).validate_acceptance(csid_703('active'))
            t_16326: 'bool42' = not cs_1144.is_valid
            def fn_16316() -> 'str34':
                return 'false should not be accepted'
            test_77.assert_(t_16326, fn_16316)
            t_16332: 'bool42' = list_get_17397(cs_1144.errors, 0).message == 'must be accepted'
            def fn_16315() -> 'str34':
                return 'correct message'
            test_77.assert_(t_16332, fn_16315)
        finally:
            test_77.soft_fail_to_hard()
class TestCase99(TestCase53):
    def test___validateConfirmationPassesWhenFieldsMatch__2318(self) -> None:
        'validateConfirmation passes when fields match'
        test_78: Test = Test()
        try:
            tbl_1146: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('password'), StringField(), False, None, False), FieldDef(csid_703('password_confirmation'), StringField(), True, None, False)), None)
            params_1147: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('password', 'secret123'), pair_17422('password_confirmation', 'secret123')))
            t_16306: 'SafeIdentifier' = csid_703('password')
            t_16307: 'SafeIdentifier' = csid_703('password_confirmation')
            cs_1148: 'Changeset' = changeset(tbl_1146, params_1147).cast((t_16306, t_16307)).validate_confirmation(csid_703('password'), csid_703('password_confirmation'))
            t_16312: 'bool42' = cs_1148.is_valid
            def fn_16294() -> 'str34':
                return 'matching fields should pass'
            test_78.assert_(t_16312, fn_16294)
        finally:
            test_78.soft_fail_to_hard()
class TestCase100(TestCase53):
    def test___validateConfirmationFailsWhenFieldsDiffer__2319(self) -> None:
        'validateConfirmation fails when fields differ'
        test_79: Test = Test()
        try:
            tbl_1150: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('password'), StringField(), False, None, False), FieldDef(csid_703('password_confirmation'), StringField(), True, None, False)), None)
            params_1151: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('password', 'secret123'), pair_17422('password_confirmation', 'wrong456')))
            t_16278: 'SafeIdentifier' = csid_703('password')
            t_16279: 'SafeIdentifier' = csid_703('password_confirmation')
            cs_1152: 'Changeset' = changeset(tbl_1150, params_1151).cast((t_16278, t_16279)).validate_confirmation(csid_703('password'), csid_703('password_confirmation'))
            t_16286: 'bool42' = not cs_1152.is_valid
            def fn_16266() -> 'str34':
                return 'mismatched fields should fail'
            test_79.assert_(t_16286, fn_16266)
            t_16292: 'bool42' = list_get_17397(cs_1152.errors, 0).field == 'password_confirmation'
            def fn_16265() -> 'str34':
                return 'error on confirmation field'
            test_79.assert_(t_16292, fn_16265)
        finally:
            test_79.soft_fail_to_hard()
class TestCase101(TestCase53):
    def test___validateConfirmationFailsWhenConfirmationMissing__2320(self) -> None:
        'validateConfirmation fails when confirmation missing'
        test_80: Test = Test()
        try:
            tbl_1154: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('password'), StringField(), False, None, False), FieldDef(csid_703('password_confirmation'), StringField(), True, None, False)), None)
            params_1155: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('password', 'secret123'),))
            t_16256: 'SafeIdentifier' = csid_703('password')
            cs_1156: 'Changeset' = changeset(tbl_1154, params_1155).cast((t_16256,)).validate_confirmation(csid_703('password'), csid_703('password_confirmation'))
            t_16263: 'bool42' = not cs_1156.is_valid
            def fn_16245() -> 'str34':
                return 'missing confirmation should fail'
            test_80.assert_(t_16263, fn_16245)
        finally:
            test_80.soft_fail_to_hard()
class TestCase102(TestCase53):
    def test___validateContainsPassesWhenSubstringFound__2321(self) -> None:
        'validateContains passes when substring found'
        test_81: Test = Test()
        try:
            params_1158: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('email', 'alice@example.com'),))
            t_16237: 'TableDef' = user_table_704()
            t_16238: 'SafeIdentifier' = csid_703('email')
            cs_1159: 'Changeset' = changeset(t_16237, params_1158).cast((t_16238,)).validate_contains(csid_703('email'), '@')
            t_16242: 'bool42' = cs_1159.is_valid
            def fn_16234() -> 'str34':
                return 'should pass when @ present'
            test_81.assert_(t_16242, fn_16234)
        finally:
            test_81.soft_fail_to_hard()
class TestCase103(TestCase53):
    def test___validateContainsFailsWhenSubstringNotFound__2322(self) -> None:
        'validateContains fails when substring not found'
        test_82: Test = Test()
        try:
            params_1161: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('email', 'alice-example.com'),))
            t_16225: 'TableDef' = user_table_704()
            t_16226: 'SafeIdentifier' = csid_703('email')
            cs_1162: 'Changeset' = changeset(t_16225, params_1161).cast((t_16226,)).validate_contains(csid_703('email'), '@')
            t_16232: 'bool42' = not cs_1162.is_valid
            def fn_16222() -> 'str34':
                return 'should fail when @ absent'
            test_82.assert_(t_16232, fn_16222)
        finally:
            test_82.soft_fail_to_hard()
class TestCase104(TestCase53):
    def test___validateContainsSkipsWhenFieldNotInChanges__2323(self) -> None:
        'validateContains skips when field not in changes'
        test_83: Test = Test()
        try:
            params_1164: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_16214: 'TableDef' = user_table_704()
            t_16215: 'SafeIdentifier' = csid_703('email')
            cs_1165: 'Changeset' = changeset(t_16214, params_1164).cast((t_16215,)).validate_contains(csid_703('email'), '@')
            t_16219: 'bool42' = cs_1165.is_valid
            def fn_16212() -> 'str34':
                return 'should be valid when field absent'
            test_83.assert_(t_16219, fn_16212)
        finally:
            test_83.soft_fail_to_hard()
class TestCase105(TestCase53):
    def test___validateStartsWithPasses__2324(self) -> None:
        'validateStartsWith passes'
        test_84: Test = Test()
        try:
            params_1167: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Dr. Smith'),))
            t_16204: 'TableDef' = user_table_704()
            t_16205: 'SafeIdentifier' = csid_703('name')
            cs_1168: 'Changeset' = changeset(t_16204, params_1167).cast((t_16205,)).validate_starts_with(csid_703('name'), 'Dr.')
            t_16209: 'bool42' = cs_1168.is_valid
            def fn_16201() -> 'str34':
                return 'should pass for Dr. prefix'
            test_84.assert_(t_16209, fn_16201)
        finally:
            test_84.soft_fail_to_hard()
class TestCase106(TestCase53):
    def test___validateStartsWithFails__2325(self) -> None:
        'validateStartsWith fails'
        test_85: Test = Test()
        try:
            params_1170: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Mr. Smith'),))
            t_16192: 'TableDef' = user_table_704()
            t_16193: 'SafeIdentifier' = csid_703('name')
            cs_1171: 'Changeset' = changeset(t_16192, params_1170).cast((t_16193,)).validate_starts_with(csid_703('name'), 'Dr.')
            t_16199: 'bool42' = not cs_1171.is_valid
            def fn_16189() -> 'str34':
                return 'should fail for Mr. prefix'
            test_85.assert_(t_16199, fn_16189)
        finally:
            test_85.soft_fail_to_hard()
class TestCase107(TestCase53):
    def test___validateEndsWithPasses__2326(self) -> None:
        'validateEndsWith passes'
        test_86: Test = Test()
        try:
            params_1173: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('email', 'alice@example.com'),))
            t_16181: 'TableDef' = user_table_704()
            t_16182: 'SafeIdentifier' = csid_703('email')
            cs_1174: 'Changeset' = changeset(t_16181, params_1173).cast((t_16182,)).validate_ends_with(csid_703('email'), '.com')
            t_16186: 'bool42' = cs_1174.is_valid
            def fn_16178() -> 'str34':
                return 'should pass for .com suffix'
            test_86.assert_(t_16186, fn_16178)
        finally:
            test_86.soft_fail_to_hard()
class TestCase108(TestCase53):
    def test___validateEndsWithFails__2327(self) -> None:
        'validateEndsWith fails'
        test_87: Test = Test()
        try:
            params_1176: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('email', 'alice@example.org'),))
            t_16169: 'TableDef' = user_table_704()
            t_16170: 'SafeIdentifier' = csid_703('email')
            cs_1177: 'Changeset' = changeset(t_16169, params_1176).cast((t_16170,)).validate_ends_with(csid_703('email'), '.com')
            t_16176: 'bool42' = not cs_1177.is_valid
            def fn_16166() -> 'str34':
                return 'should fail for .org when expecting .com'
            test_87.assert_(t_16176, fn_16166)
        finally:
            test_87.soft_fail_to_hard()
class TestCase109(TestCase53):
    def test___validateEndsWithHandlesRepeatedSuffixCorrectly__2328(self) -> None:
        'validateEndsWith handles repeated suffix correctly'
        test_88: Test = Test()
        try:
            params_1179: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'abcabc'),))
            t_16158: 'TableDef' = user_table_704()
            t_16159: 'SafeIdentifier' = csid_703('name')
            cs_1180: 'Changeset' = changeset(t_16158, params_1179).cast((t_16159,)).validate_ends_with(csid_703('name'), 'abc')
            t_16163: 'bool42' = cs_1180.is_valid
            def fn_16155() -> 'str34':
                return 'abcabc should end with abc'
            test_88.assert_(t_16163, fn_16155)
        finally:
            test_88.soft_fail_to_hard()
class TestCase110(TestCase53):
    def test___toInsertSqlUsesDefaultValueWhenFieldNotInChanges__2329(self) -> None:
        'toInsertSql uses default value when field not in changes'
        test_89: Test = Test()
        try:
            tbl_1182: 'TableDef' = TableDef(csid_703('posts'), (FieldDef(csid_703('title'), StringField(), False, None, False), FieldDef(csid_703('status'), StringField(), False, SqlDefault(), False)), None)
            params_1183: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('title', 'Hello'),))
            t_16139: 'SafeIdentifier' = csid_703('title')
            cs_1184: 'Changeset' = changeset(tbl_1182, params_1183).cast((t_16139,))
            t_8735: 'SqlFragment'
            t_8735 = cs_1184.to_insert_sql()
            t_8736: 'SqlFragment' = t_8735
            s_1185: 'str34' = t_8736.to_string()
            t_16143: 'bool42' = s_1185.find('INSERT INTO posts') >= 0
            def fn_16127() -> 'str34':
                return str_cat_17392('has INSERT INTO: ', s_1185)
            test_89.assert_(t_16143, fn_16127)
            t_16147: 'bool42' = s_1185.find("'Hello'") >= 0
            def fn_16126() -> 'str34':
                return str_cat_17392('has title value: ', s_1185)
            test_89.assert_(t_16147, fn_16126)
            t_16151: 'bool42' = s_1185.find('DEFAULT') >= 0
            def fn_16125() -> 'str34':
                return str_cat_17392('status should use DEFAULT: ', s_1185)
            test_89.assert_(t_16151, fn_16125)
        finally:
            test_89.soft_fail_to_hard()
class TestCase111(TestCase53):
    def test___toInsertSqlChangeOverridesDefaultValue__2330(self) -> None:
        'toInsertSql change overrides default value'
        test_90: Test = Test()
        try:
            tbl_1187: 'TableDef' = TableDef(csid_703('posts'), (FieldDef(csid_703('title'), StringField(), False, None, False), FieldDef(csid_703('status'), StringField(), False, SqlDefault(), False)), None)
            params_1188: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('title', 'Hello'), pair_17422('status', 'published')))
            t_16117: 'SafeIdentifier' = csid_703('title')
            t_16118: 'SafeIdentifier' = csid_703('status')
            cs_1189: 'Changeset' = changeset(tbl_1187, params_1188).cast((t_16117, t_16118))
            t_8715: 'SqlFragment'
            t_8715 = cs_1189.to_insert_sql()
            t_8716: 'SqlFragment' = t_8715
            s_1190: 'str34' = t_8716.to_string()
            t_16122: 'bool42' = s_1190.find("'published'") >= 0
            def fn_16104() -> 'str34':
                return str_cat_17392('should use provided value: ', s_1190)
            test_90.assert_(t_16122, fn_16104)
        finally:
            test_90.soft_fail_to_hard()
class TestCase112(TestCase53):
    def test___toInsertSqlWithTimestampsUsesDefault__2331(self) -> None:
        'toInsertSql with timestamps uses DEFAULT'
        test_91: Test = Test()
        try:
            t_8662: 'Sequence38[FieldDef]'
            t_8662 = timestamps()
            ts_1192: 'Sequence38[FieldDef]' = t_8662
            fields_1193: 'MutableSequence43[FieldDef]' = list_17379()
            fields_1193.append(FieldDef(csid_703('title'), StringField(), False, None, False))
            def fn_16070(t_1194: 'FieldDef') -> 'None':
                fields_1193.append(t_1194)
            list_for_each_17386(ts_1192, fn_16070)
            tbl_1195: 'TableDef' = TableDef(csid_703('articles'), tuple_17381(fields_1193), None)
            params_1196: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('title', 'News'),))
            t_16083: 'SafeIdentifier' = csid_703('title')
            cs_1197: 'Changeset' = changeset(tbl_1195, params_1196).cast((t_16083,))
            t_8677: 'SqlFragment'
            t_8677 = cs_1197.to_insert_sql()
            t_8678: 'SqlFragment' = t_8677
            s_1198: 'str34' = t_8678.to_string()
            t_16087: 'bool42' = s_1198.find('inserted_at') >= 0
            def fn_16069() -> 'str34':
                return str_cat_17392('should include inserted_at: ', s_1198)
            test_91.assert_(t_16087, fn_16069)
            t_16091: 'bool42' = s_1198.find('updated_at') >= 0
            def fn_16068() -> 'str34':
                return str_cat_17392('should include updated_at: ', s_1198)
            test_91.assert_(t_16091, fn_16068)
            t_16095: 'bool42' = s_1198.find('DEFAULT') >= 0
            def fn_16067() -> 'str34':
                return str_cat_17392('timestamps should use DEFAULT: ', s_1198)
            test_91.assert_(t_16095, fn_16067)
        finally:
            test_91.soft_fail_to_hard()
class TestCase113(TestCase53):
    def test___toInsertSqlSkipsVirtualFields__2332(self) -> None:
        'toInsertSql skips virtual fields'
        test_92: Test = Test()
        try:
            tbl_1200: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('full_name'), StringField(), True, None, True)), None)
            params_1201: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('full_name', 'Alice Smith')))
            t_16053: 'SafeIdentifier' = csid_703('name')
            t_16054: 'SafeIdentifier' = csid_703('full_name')
            cs_1202: 'Changeset' = changeset(tbl_1200, params_1201).cast((t_16053, t_16054))
            t_8651: 'SqlFragment'
            t_8651 = cs_1202.to_insert_sql()
            t_8652: 'SqlFragment' = t_8651
            s_1203: 'str34' = t_8652.to_string()
            t_16058: 'bool42' = s_1203.find("'Alice'") >= 0
            def fn_16041() -> 'str34':
                return str_cat_17392('name should be included: ', s_1203)
            test_92.assert_(t_16058, fn_16041)
            t_16064: 'bool42' = not s_1203.find('full_name') >= 0
            def fn_16040() -> 'str34':
                return str_cat_17392('virtual field should be excluded: ', s_1203)
            test_92.assert_(t_16064, fn_16040)
        finally:
            test_92.soft_fail_to_hard()
class TestCase114(TestCase53):
    def test___toInsertSqlAllowsMissingNonNullableVirtualField__2333(self) -> None:
        'toInsertSql allows missing non-nullable virtual field'
        test_93: Test = Test()
        try:
            tbl_1205: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('computed'), StringField(), False, None, True)), None)
            params_1206: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'),))
            t_16033: 'SafeIdentifier' = csid_703('name')
            cs_1207: 'Changeset' = changeset(tbl_1205, params_1206).cast((t_16033,))
            t_8630: 'SqlFragment'
            t_8630 = cs_1207.to_insert_sql()
            t_8631: 'SqlFragment' = t_8630
            s_1208: 'str34' = t_8631.to_string()
            t_16037: 'bool42' = s_1208.find("'Alice'") >= 0
            def fn_16022() -> 'str34':
                return str_cat_17392('should succeed: ', s_1208)
            test_93.assert_(t_16037, fn_16022)
        finally:
            test_93.soft_fail_to_hard()
class TestCase115(TestCase53):
    def test___toUpdateSqlSkipsVirtualFields__2334(self) -> None:
        'toUpdateSql skips virtual fields'
        test_94: Test = Test()
        try:
            tbl_1210: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('display'), StringField(), True, None, True)), None)
            params_1211: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Bob'), pair_17422('display', 'Bobby')))
            t_16009: 'SafeIdentifier' = csid_703('name')
            t_16010: 'SafeIdentifier' = csid_703('display')
            cs_1212: 'Changeset' = changeset(tbl_1210, params_1211).cast((t_16009, t_16010))
            t_8607: 'SqlFragment'
            t_8607 = cs_1212.to_update_sql(1)
            t_8608: 'SqlFragment' = t_8607
            s_1213: 'str34' = t_8608.to_string()
            t_16014: 'bool42' = s_1213.find("name = 'Bob'") >= 0
            def fn_15997() -> 'str34':
                return str_cat_17392('name should be in SET: ', s_1213)
            test_94.assert_(t_16014, fn_15997)
            t_16020: 'bool42' = not s_1213.find('display') >= 0
            def fn_15996() -> 'str34':
                return str_cat_17392('virtual field excluded from UPDATE: ', s_1213)
            test_94.assert_(t_16020, fn_15996)
        finally:
            test_94.soft_fail_to_hard()
class TestCase116(TestCase53):
    def test___toUpdateSqlUsesCustomPrimaryKey__2335(self) -> None:
        'toUpdateSql uses custom primary key'
        test_95: Test = Test()
        try:
            tbl_1215: 'TableDef' = TableDef(csid_703('posts'), (FieldDef(csid_703('title'), StringField(), False, None, False),), csid_703('post_id'))
            params_1216: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('title', 'Updated'),))
            t_15990: 'SafeIdentifier' = csid_703('title')
            cs_1217: 'Changeset' = changeset(tbl_1215, params_1216).cast((t_15990,))
            t_8589: 'SqlFragment'
            t_8589 = cs_1217.to_update_sql(99)
            t_8590: 'SqlFragment' = t_8589
            s_1218: 'str34' = t_8590.to_string()
            t_15994: 'bool42' = s_1218 == "UPDATE posts SET title = 'Updated' WHERE post_id = 99"
            def fn_15980() -> 'str34':
                return str_cat_17392('got: ', s_1218)
            test_95.assert_(t_15994, fn_15980)
        finally:
            test_95.soft_fail_to_hard()
class TestCase117(TestCase53):
    def test___deleteSqlUsesCustomPrimaryKey__2336(self) -> None:
        'deleteSql uses custom primary key'
        test_96: Test = Test()
        try:
            tbl_1220: 'TableDef' = TableDef(csid_703('posts'), (FieldDef(csid_703('title'), StringField(), False, None, False),), csid_703('post_id'))
            s_1221: 'str34' = delete_sql(tbl_1220, 42).to_string()
            t_15967: 'bool42' = s_1221 == 'DELETE FROM posts WHERE post_id = 42'
            def fn_15956() -> 'str34':
                return str_cat_17392('got: ', s_1221)
            test_96.assert_(t_15967, fn_15956)
        finally:
            test_96.soft_fail_to_hard()
class TestCase118(TestCase53):
    def test___deleteSqlUsesDefaultIdWhenPrimaryKeyNull__2337(self) -> None:
        'deleteSql uses default id when primaryKey null'
        test_97: Test = Test()
        try:
            tbl_1223: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False),), None)
            s_1224: 'str34' = delete_sql(tbl_1223, 7).to_string()
            t_15954: 'bool42' = s_1224 == 'DELETE FROM users WHERE id = 7'
            def fn_15945() -> 'str34':
                return str_cat_17392('got: ', s_1224)
            test_97.assert_(t_15954, fn_15945)
        finally:
            test_97.soft_fail_to_hard()
class TestCase119(TestCase53):
    def test___alreadyInvalidChangesetSkipsSubsequentValidators__2338(self) -> None:
        'already-invalid changeset skips subsequent validators'
        test_98: Test = Test()
        try:
            params_1226: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'A'), pair_17422('email', 'alice@example.com')))
            t_15919: 'TableDef' = user_table_704()
            t_15920: 'SafeIdentifier' = csid_703('name')
            t_15921: 'SafeIdentifier' = csid_703('email')
            cs_1227: 'Changeset' = changeset(t_15919, params_1226).cast((t_15920, t_15921)).validate_length(csid_703('name'), 3, 50).validate_required((csid_703('name'), csid_703('email'))).validate_contains(csid_703('email'), '@')
            t_15932: 'bool42' = not cs_1227.is_valid
            def fn_15915() -> 'str34':
                return 'should be invalid from validateLength'
            test_98.assert_(t_15932, fn_15915)
            t_15937: 'bool42' = len_17389(cs_1227.errors) == 1
            def fn_15914() -> 'str34':
                return str_cat_17392('should have exactly 1 error, not accumulate: ', int_to_string_17391(len_17389(cs_1227.errors)))
            test_98.assert_(t_15937, fn_15914)
            t_15943: 'bool42' = list_get_17397(cs_1227.errors, 0).field == 'name'
            def fn_15913() -> 'str34':
                return 'error should be on name'
            test_98.assert_(t_15943, fn_15913)
        finally:
            test_98.soft_fail_to_hard()
class TestCase120(TestCase53):
    def test___validateNumberLessThanOrEqualPassesAtBoundary__2339(self) -> None:
        'validateNumber lessThanOrEqual passes at boundary'
        test_99: Test = Test()
        try:
            params_1229: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '10.0'),))
            t_15901: 'TableDef' = user_table_704()
            t_15902: 'SafeIdentifier' = csid_703('score')
            cs_1230: 'Changeset' = changeset(t_15901, params_1229).cast((t_15902,)).validate_number(csid_703('score'), NumberValidationOpts(None, None, None, 10.0, None))
            t_15907: 'bool42' = cs_1230.is_valid
            def fn_15898() -> 'str34':
                return '10.0 <= 10.0 should pass'
            test_99.assert_(t_15907, fn_15898)
        finally:
            test_99.soft_fail_to_hard()
class TestCase121(TestCase53):
    def test___validateNumberLessThanOrEqualFailsAboveBoundary__2340(self) -> None:
        'validateNumber lessThanOrEqual fails above boundary'
        test_100: Test = Test()
        try:
            params_1232: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '10.1'),))
            t_15882: 'TableDef' = user_table_704()
            t_15883: 'SafeIdentifier' = csid_703('score')
            cs_1233: 'Changeset' = changeset(t_15882, params_1232).cast((t_15883,)).validate_number(csid_703('score'), NumberValidationOpts(None, None, None, 10.0, None))
            t_15890: 'bool42' = not cs_1233.is_valid
            def fn_15879() -> 'str34':
                return '10.1 <= 10.0 should fail'
            test_100.assert_(t_15890, fn_15879)
            t_15896: 'bool42' = list_get_17397(cs_1233.errors, 0).message == 'must be less than or equal to 10.0'
            def fn_15878() -> 'str34':
                return 'correct message'
            test_100.assert_(t_15896, fn_15878)
        finally:
            test_100.soft_fail_to_hard()
class TestCase122(TestCase53):
    def test___validateNumberEqualToPassesWhenEqual__2341(self) -> None:
        'validateNumber equalTo passes when equal'
        test_101: Test = Test()
        try:
            params_1235: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '42.0'),))
            t_15869: 'TableDef' = user_table_704()
            t_15870: 'SafeIdentifier' = csid_703('score')
            cs_1236: 'Changeset' = changeset(t_15869, params_1235).cast((t_15870,)).validate_number(csid_703('score'), NumberValidationOpts(None, None, None, None, 42.0))
            t_15875: 'bool42' = cs_1236.is_valid
            def fn_15866() -> 'str34':
                return '42.0 == 42.0 should pass'
            test_101.assert_(t_15875, fn_15866)
        finally:
            test_101.soft_fail_to_hard()
class TestCase123(TestCase53):
    def test___validateNumberEqualToFailsWhenNotEqual__2342(self) -> None:
        'validateNumber equalTo fails when not equal'
        test_102: Test = Test()
        try:
            params_1238: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '41.9'),))
            t_15850: 'TableDef' = user_table_704()
            t_15851: 'SafeIdentifier' = csid_703('score')
            cs_1239: 'Changeset' = changeset(t_15850, params_1238).cast((t_15851,)).validate_number(csid_703('score'), NumberValidationOpts(None, None, None, None, 42.0))
            t_15858: 'bool42' = not cs_1239.is_valid
            def fn_15847() -> 'str34':
                return '41.9 == 42.0 should fail'
            test_102.assert_(t_15858, fn_15847)
            t_15864: 'bool42' = list_get_17397(cs_1239.errors, 0).message == 'must be equal to 42.0'
            def fn_15846() -> 'str34':
                return 'correct message'
            test_102.assert_(t_15864, fn_15846)
        finally:
            test_102.soft_fail_to_hard()
class TestCase124(TestCase53):
    def test___validateNumberGreaterThanFailsAtExactThreshold__2343(self) -> None:
        'validateNumber greaterThan fails at exact threshold'
        test_103: Test = Test()
        try:
            params_1241: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '18'),))
            t_15836: 'TableDef' = user_table_704()
            t_15837: 'SafeIdentifier' = csid_703('age')
            cs_1242: 'Changeset' = changeset(t_15836, params_1241).cast((t_15837,)).validate_number(csid_703('age'), NumberValidationOpts(18.0, None, None, None, None))
            t_15844: 'bool42' = not cs_1242.is_valid
            def fn_15833() -> 'str34':
                return '18 > 18 should fail (strict greater than)'
            test_103.assert_(t_15844, fn_15833)
        finally:
            test_103.soft_fail_to_hard()
class TestCase125(TestCase53):
    def test___validateNumberLessThanFailsAtExactThreshold__2344(self) -> None:
        'validateNumber lessThan fails at exact threshold'
        test_104: Test = Test()
        try:
            params_1244: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', '10.0'),))
            t_15823: 'TableDef' = user_table_704()
            t_15824: 'SafeIdentifier' = csid_703('score')
            cs_1245: 'Changeset' = changeset(t_15823, params_1244).cast((t_15824,)).validate_number(csid_703('score'), NumberValidationOpts(None, 10.0, None, None, None))
            t_15831: 'bool42' = not cs_1245.is_valid
            def fn_15820() -> 'str34':
                return '10.0 < 10.0 should fail (strict less than)'
            test_104.assert_(t_15831, fn_15820)
        finally:
            test_104.soft_fail_to_hard()
class TestCase126(TestCase53):
    def test___validateFloatFailsForNonFloatString__2345(self) -> None:
        'validateFloat fails for non-float string'
        test_105: Test = Test()
        try:
            params_1247: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('score', 'abc'),))
            t_15805: 'TableDef' = user_table_704()
            t_15806: 'SafeIdentifier' = csid_703('score')
            cs_1248: 'Changeset' = changeset(t_15805, params_1247).cast((t_15806,)).validate_float(csid_703('score'))
            t_15812: 'bool42' = not cs_1248.is_valid
            def fn_15802() -> 'str34':
                return 'abc should not parse as float'
            test_105.assert_(t_15812, fn_15802)
            t_15818: 'bool42' = list_get_17397(cs_1248.errors, 0).message == 'must be a number'
            def fn_15801() -> 'str34':
                return 'correct message'
            test_105.assert_(t_15818, fn_15801)
        finally:
            test_105.soft_fail_to_hard()
class TestCase127(TestCase53):
    def test___toInsertSqlWithAllSixFieldTypes__2346(self) -> None:
        'toInsertSql with all six field types'
        test_106: Test = Test()
        try:
            tbl_1250: 'TableDef' = TableDef(csid_703('records'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('count'), IntField(), False, None, False), FieldDef(csid_703('big_id'), Int64Field(), False, None, False), FieldDef(csid_703('rating'), FloatField(), False, None, False), FieldDef(csid_703('active'), BoolField(), False, None, False), FieldDef(csid_703('birthday'), DateField(), False, None, False)), None)
            params_1251: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('count', '42'), pair_17422('big_id', '9999999999'), pair_17422('rating', '3.14'), pair_17422('active', 'true'), pair_17422('birthday', '2000-01-15')))
            t_15769: 'SafeIdentifier' = csid_703('name')
            t_15770: 'SafeIdentifier' = csid_703('count')
            t_15771: 'SafeIdentifier' = csid_703('big_id')
            t_15772: 'SafeIdentifier' = csid_703('rating')
            t_15773: 'SafeIdentifier' = csid_703('active')
            t_15774: 'SafeIdentifier' = csid_703('birthday')
            cs_1252: 'Changeset' = changeset(tbl_1250, params_1251).cast((t_15769, t_15770, t_15771, t_15772, t_15773, t_15774))
            t_8416: 'SqlFragment'
            t_8416 = cs_1252.to_insert_sql()
            t_8417: 'SqlFragment' = t_8416
            s_1253: 'str34' = t_8417.to_string()
            t_15778: 'bool42' = s_1253.find("'Alice'") >= 0
            def fn_15741() -> 'str34':
                return str_cat_17392('string field: ', s_1253)
            test_106.assert_(t_15778, fn_15741)
            t_15782: 'bool42' = s_1253.find('42') >= 0
            def fn_15740() -> 'str34':
                return str_cat_17392('int field: ', s_1253)
            test_106.assert_(t_15782, fn_15740)
            t_15786: 'bool42' = s_1253.find('9999999999') >= 0
            def fn_15739() -> 'str34':
                return str_cat_17392('int64 field: ', s_1253)
            test_106.assert_(t_15786, fn_15739)
            t_15790: 'bool42' = s_1253.find('3.14') >= 0
            def fn_15738() -> 'str34':
                return str_cat_17392('float field: ', s_1253)
            test_106.assert_(t_15790, fn_15738)
            t_15794: 'bool42' = s_1253.find('TRUE') >= 0
            def fn_15737() -> 'str34':
                return str_cat_17392('bool field: ', s_1253)
            test_106.assert_(t_15794, fn_15737)
            t_15798: 'bool42' = s_1253.find("'2000-01-15'") >= 0
            def fn_15736() -> 'str34':
                return str_cat_17392('date field: ', s_1253)
            test_106.assert_(t_15798, fn_15736)
        finally:
            test_106.soft_fail_to_hard()
class TestCase128(TestCase53):
    def test___deleteChangeOnNonNullableFieldCausesToInsertSqlToBubble__2347(self) -> None:
        'deleteChange on non-nullable field causes toInsertSql to bubble'
        test_107: Test = Test()
        try:
            tbl_1255: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('email'), StringField(), False, None, False)), None)
            params_1256: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('email', 'a@b.com')))
            t_15729: 'SafeIdentifier' = csid_703('name')
            t_15730: 'SafeIdentifier' = csid_703('email')
            cs_1257: 'Changeset' = changeset(tbl_1255, params_1256).cast((t_15729, t_15730)).delete_change(csid_703('email'))
            did_bubble_1258: 'bool42'
            try:
                cs_1257.to_insert_sql()
                did_bubble_1258 = False
            except Exception46:
                did_bubble_1258 = True
            def fn_15717() -> 'str34':
                return 'removing non-nullable field should make toInsertSql bubble'
            test_107.assert_(did_bubble_1258, fn_15717)
        finally:
            test_107.soft_fail_to_hard()
class TestCase129(TestCase53):
    def test___validateLengthPassesAtExactMin__2348(self) -> None:
        'validateLength passes at exact min'
        test_108: Test = Test()
        try:
            params_1260: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'abc'),))
            t_15709: 'TableDef' = user_table_704()
            t_15710: 'SafeIdentifier' = csid_703('name')
            cs_1261: 'Changeset' = changeset(t_15709, params_1260).cast((t_15710,)).validate_length(csid_703('name'), 3, 10)
            t_15714: 'bool42' = cs_1261.is_valid
            def fn_15706() -> 'str34':
                return 'length 3 should pass for min 3'
            test_108.assert_(t_15714, fn_15706)
        finally:
            test_108.soft_fail_to_hard()
class TestCase130(TestCase53):
    def test___validateLengthPassesAtExactMax__2349(self) -> None:
        'validateLength passes at exact max'
        test_109: Test = Test()
        try:
            params_1263: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'abcdefghij'),))
            t_15698: 'TableDef' = user_table_704()
            t_15699: 'SafeIdentifier' = csid_703('name')
            cs_1264: 'Changeset' = changeset(t_15698, params_1263).cast((t_15699,)).validate_length(csid_703('name'), 1, 10)
            t_15703: 'bool42' = cs_1264.is_valid
            def fn_15695() -> 'str34':
                return 'length 10 should pass for max 10'
            test_109.assert_(t_15703, fn_15695)
        finally:
            test_109.soft_fail_to_hard()
class TestCase131(TestCase53):
    def test___validateAcceptanceSkipsWhenFieldNotInChanges__2350(self) -> None:
        'validateAcceptance skips when field not in changes'
        test_110: Test = Test()
        try:
            params_1266: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_15687: 'TableDef' = user_table_704()
            t_15688: 'SafeIdentifier' = csid_703('active')
            cs_1267: 'Changeset' = changeset(t_15687, params_1266).cast((t_15688,)).validate_acceptance(csid_703('active'))
            t_15692: 'bool42' = cs_1267.is_valid
            def fn_15685() -> 'str34':
                return 'should be valid when field absent'
            test_110.assert_(t_15692, fn_15685)
        finally:
            test_110.soft_fail_to_hard()
class TestCase132(TestCase53):
    def test___multipleValidatorsChainCorrectlyOnValidChangeset__2351(self) -> None:
        'multiple validators chain correctly on valid changeset'
        test_111: Test = Test()
        try:
            params_1269: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('email', 'alice@example.com'), pair_17422('age', '25')))
            t_15660: 'TableDef' = user_table_704()
            t_15661: 'SafeIdentifier' = csid_703('name')
            t_15662: 'SafeIdentifier' = csid_703('email')
            t_15663: 'SafeIdentifier' = csid_703('age')
            cs_1270: 'Changeset' = changeset(t_15660, params_1269).cast((t_15661, t_15662, t_15663)).validate_required((csid_703('name'), csid_703('email'))).validate_length(csid_703('name'), 2, 50).validate_contains(csid_703('email'), '@').validate_int(csid_703('age')).validate_number(csid_703('age'), NumberValidationOpts(0.0, 150.0, None, None, None))
            t_15677: 'bool42' = cs_1270.is_valid
            def fn_15655() -> 'str34':
                return 'all validators should pass'
            test_111.assert_(t_15677, fn_15655)
            t_15683: 'bool42' = len_17389(cs_1270.errors) == 0
            def fn_15654() -> 'str34':
                return 'no errors expected'
            test_111.assert_(t_15683, fn_15654)
        finally:
            test_111.soft_fail_to_hard()
class TestCase133(TestCase53):
    def test___toUpdateSqlWithMultipleNonVirtualFields__2352(self) -> None:
        'toUpdateSql with multiple non-virtual fields'
        test_112: Test = Test()
        try:
            tbl_1272: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('email'), StringField(), False, None, False)), None)
            params_1273: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Bob'), pair_17422('email', 'bob@example.com')))
            t_15638: 'SafeIdentifier' = csid_703('name')
            t_15639: 'SafeIdentifier' = csid_703('email')
            cs_1274: 'Changeset' = changeset(tbl_1272, params_1273).cast((t_15638, t_15639))
            t_8297: 'SqlFragment'
            t_8297 = cs_1274.to_update_sql(5)
            t_8298: 'SqlFragment' = t_8297
            s_1275: 'str34' = t_8298.to_string()
            t_15643: 'bool42' = s_1275.find("name = 'Bob'") >= 0
            def fn_15626() -> 'str34':
                return str_cat_17392('name in SET: ', s_1275)
            test_112.assert_(t_15643, fn_15626)
            t_15647: 'bool42' = s_1275.find("email = 'bob@example.com'") >= 0
            def fn_15625() -> 'str34':
                return str_cat_17392('email in SET: ', s_1275)
            test_112.assert_(t_15647, fn_15625)
            t_15651: 'bool42' = s_1275.find('WHERE id = 5') >= 0
            def fn_15624() -> 'str34':
                return str_cat_17392('WHERE clause: ', s_1275)
            test_112.assert_(t_15651, fn_15624)
        finally:
            test_112.soft_fail_to_hard()
class TestCase134(TestCase53):
    def test___toUpdateSqlBubblesWhenAllChangesAreVirtualFields__2353(self) -> None:
        'toUpdateSql bubbles when all changes are virtual fields'
        test_113: Test = Test()
        try:
            tbl_1277: 'TableDef' = TableDef(csid_703('users'), (FieldDef(csid_703('name'), StringField(), False, None, False), FieldDef(csid_703('computed'), StringField(), True, None, True)), None)
            params_1278: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'Alice'), pair_17422('computed', 'derived')))
            t_15620: 'SafeIdentifier' = csid_703('computed')
            cs_1279: 'Changeset' = changeset(tbl_1277, params_1278).cast((t_15620,))
            did_bubble_1280: 'bool42'
            try:
                cs_1279.to_update_sql(1)
                did_bubble_1280 = False
            except Exception46:
                did_bubble_1280 = True
            def fn_15608() -> 'str34':
                return 'should bubble when all changes are virtual'
            test_113.assert_(did_bubble_1280, fn_15608)
        finally:
            test_113.soft_fail_to_hard()
class TestCase135(TestCase53):
    def test___putChangeSatisfiesSubsequentValidateRequired__2354(self) -> None:
        'putChange satisfies subsequent validateRequired'
        test_114: Test = Test()
        try:
            params_1282: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_15598: 'TableDef' = user_table_704()
            t_15599: 'SafeIdentifier' = csid_703('name')
            cs_1283: 'Changeset' = changeset(t_15598, params_1282).cast((t_15599,)).put_change(csid_703('name'), 'Injected').validate_required((csid_703('name'),))
            t_15605: 'bool42' = cs_1283.is_valid
            def fn_15596() -> 'str34':
                return 'putChange should satisfy required'
            test_114.assert_(t_15605, fn_15596)
        finally:
            test_114.soft_fail_to_hard()
class TestCase136(TestCase53):
    def test___validateStartsWithSkipsWhenFieldNotInChanges__2355(self) -> None:
        'validateStartsWith skips when field not in changes'
        test_115: Test = Test()
        try:
            params_1285: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_15588: 'TableDef' = user_table_704()
            t_15589: 'SafeIdentifier' = csid_703('name')
            cs_1286: 'Changeset' = changeset(t_15588, params_1285).cast((t_15589,)).validate_starts_with(csid_703('name'), 'Dr.')
            t_15593: 'bool42' = cs_1286.is_valid
            def fn_15586() -> 'str34':
                return 'should be valid when field absent'
            test_115.assert_(t_15593, fn_15586)
        finally:
            test_115.soft_fail_to_hard()
class TestCase137(TestCase53):
    def test___validateEndsWithSkipsWhenFieldNotInChanges__2356(self) -> None:
        'validateEndsWith skips when field not in changes'
        test_116: Test = Test()
        try:
            params_1288: 'MappingProxyType41[str34, str34]' = map_constructor_17421(())
            t_15578: 'TableDef' = user_table_704()
            t_15579: 'SafeIdentifier' = csid_703('name')
            cs_1289: 'Changeset' = changeset(t_15578, params_1288).cast((t_15579,)).validate_ends_with(csid_703('name'), '.com')
            t_15583: 'bool42' = cs_1289.is_valid
            def fn_15576() -> 'str34':
                return 'should be valid when field absent'
            test_116.assert_(t_15583, fn_15576)
        finally:
            test_116.soft_fail_to_hard()
class TestCase138(TestCase53):
    def test___validateIntAcceptsZero__2357(self) -> None:
        'validateInt accepts zero'
        test_117: Test = Test()
        try:
            params_1291: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '0'),))
            t_15568: 'TableDef' = user_table_704()
            t_15569: 'SafeIdentifier' = csid_703('age')
            cs_1292: 'Changeset' = changeset(t_15568, params_1291).cast((t_15569,)).validate_int(csid_703('age'))
            t_15573: 'bool42' = cs_1292.is_valid
            def fn_15565() -> 'str34':
                return '0 should be a valid int'
            test_117.assert_(t_15573, fn_15565)
        finally:
            test_117.soft_fail_to_hard()
class TestCase139(TestCase53):
    def test___validateIntAcceptsNegative__2358(self) -> None:
        'validateInt accepts negative'
        test_118: Test = Test()
        try:
            params_1294: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('age', '-5'),))
            t_15557: 'TableDef' = user_table_704()
            t_15558: 'SafeIdentifier' = csid_703('age')
            cs_1295: 'Changeset' = changeset(t_15557, params_1294).cast((t_15558,)).validate_int(csid_703('age'))
            t_15562: 'bool42' = cs_1295.is_valid
            def fn_15554() -> 'str34':
                return '-5 should be a valid int'
            test_118.assert_(t_15562, fn_15554)
        finally:
            test_118.soft_fail_to_hard()
class TestCase140(TestCase53):
    def test___changesetImmutabilityValidatorsDoNotMutateBase__2359(self) -> None:
        'changeset immutability - validators do not mutate base'
        test_119: Test = Test()
        try:
            params_1297: 'MappingProxyType41[str34, str34]' = map_constructor_17421((pair_17422('name', 'A'), pair_17422('email', 'alice@example.com')))
            t_15538: 'TableDef' = user_table_704()
            t_15539: 'SafeIdentifier' = csid_703('name')
            t_15540: 'SafeIdentifier' = csid_703('email')
            base_1298: 'Changeset' = changeset(t_15538, params_1297).cast((t_15539, t_15540))
            failed_1299: 'Changeset' = base_1298.validate_length(csid_703('name'), 3, 50)
            passed_1300: 'Changeset' = base_1298.validate_required((csid_703('name'), csid_703('email')))
            t_15549: 'bool42' = not failed_1299.is_valid
            def fn_15534() -> 'str34':
                return 'failed branch should be invalid'
            test_119.assert_(t_15549, fn_15534)
            t_15551: 'bool42' = passed_1300.is_valid
            def fn_15533() -> 'str34':
                return 'passed branch should still be valid'
            test_119.assert_(t_15551, fn_15533)
        finally:
            test_119.soft_fail_to_hard()
def sid_709(name_1650: 'str34') -> 'SafeIdentifier':
    t_7743: 'SafeIdentifier'
    t_7743 = safe_identifier(name_1650)
    return t_7743
class TestCase141(TestCase53):
    def test___bareFromProducesSelect__2441(self) -> None:
        'bare from produces SELECT *'
        test_120: Test = Test()
        try:
            q_1653: 'Query' = from_(sid_709('users'))
            t_15091: 'bool42' = q_1653.to_sql().to_string() == 'SELECT * FROM users'
            def fn_15086() -> 'str34':
                return 'bare query'
            test_120.assert_(t_15091, fn_15086)
        finally:
            test_120.soft_fail_to_hard()
class TestCase142(TestCase53):
    def test___selectRestrictsColumns__2442(self) -> None:
        'select restricts columns'
        test_121: Test = Test()
        try:
            t_15077: 'SafeIdentifier' = sid_709('users')
            t_15078: 'SafeIdentifier' = sid_709('id')
            t_15079: 'SafeIdentifier' = sid_709('name')
            q_1655: 'Query' = from_(t_15077).select((t_15078, t_15079))
            t_15084: 'bool42' = q_1655.to_sql().to_string() == 'SELECT id, name FROM users'
            def fn_15076() -> 'str34':
                return 'select columns'
            test_121.assert_(t_15084, fn_15076)
        finally:
            test_121.soft_fail_to_hard()
class TestCase143(TestCase53):
    def test___whereAddsConditionWithIntValue__2443(self) -> None:
        'where adds condition with int value'
        test_122: Test = Test()
        try:
            t_15065: 'SafeIdentifier' = sid_709('users')
            t_15066: 'SqlBuilder' = SqlBuilder()
            t_15066.append_safe('age > ')
            t_15066.append_int32(18)
            t_15069: 'SqlFragment' = t_15066.accumulated
            q_1657: 'Query' = from_(t_15065).where(t_15069)
            t_15074: 'bool42' = q_1657.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18'
            def fn_15064() -> 'str34':
                return 'where int'
            test_122.assert_(t_15074, fn_15064)
        finally:
            test_122.soft_fail_to_hard()
class TestCase144(TestCase53):
    def test___whereAddsConditionWithBoolValue__2445(self) -> None:
        'where adds condition with bool value'
        test_123: Test = Test()
        try:
            t_15053: 'SafeIdentifier' = sid_709('users')
            t_15054: 'SqlBuilder' = SqlBuilder()
            t_15054.append_safe('active = ')
            t_15054.append_boolean(True)
            t_15057: 'SqlFragment' = t_15054.accumulated
            q_1659: 'Query' = from_(t_15053).where(t_15057)
            t_15062: 'bool42' = q_1659.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE'
            def fn_15052() -> 'str34':
                return 'where bool'
            test_123.assert_(t_15062, fn_15052)
        finally:
            test_123.soft_fail_to_hard()
class TestCase145(TestCase53):
    def test___chainedWhereUsesAnd__2447(self) -> None:
        'chained where uses AND'
        test_124: Test = Test()
        try:
            t_15036: 'SafeIdentifier' = sid_709('users')
            t_15037: 'SqlBuilder' = SqlBuilder()
            t_15037.append_safe('age > ')
            t_15037.append_int32(18)
            t_15040: 'SqlFragment' = t_15037.accumulated
            t_15041: 'Query' = from_(t_15036).where(t_15040)
            t_15042: 'SqlBuilder' = SqlBuilder()
            t_15042.append_safe('active = ')
            t_15042.append_boolean(True)
            q_1661: 'Query' = t_15041.where(t_15042.accumulated)
            t_15050: 'bool42' = q_1661.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE'
            def fn_15035() -> 'str34':
                return 'chained where'
            test_124.assert_(t_15050, fn_15035)
        finally:
            test_124.soft_fail_to_hard()
class TestCase146(TestCase53):
    def test___orderByAsc__2450(self) -> None:
        'orderBy ASC'
        test_125: Test = Test()
        try:
            t_15027: 'SafeIdentifier' = sid_709('users')
            t_15028: 'SafeIdentifier' = sid_709('name')
            q_1663: 'Query' = from_(t_15027).order_by(t_15028, True)
            t_15033: 'bool42' = q_1663.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC'
            def fn_15026() -> 'str34':
                return 'order asc'
            test_125.assert_(t_15033, fn_15026)
        finally:
            test_125.soft_fail_to_hard()
class TestCase147(TestCase53):
    def test___orderByDesc__2451(self) -> None:
        'orderBy DESC'
        test_126: Test = Test()
        try:
            t_15018: 'SafeIdentifier' = sid_709('users')
            t_15019: 'SafeIdentifier' = sid_709('created_at')
            q_1665: 'Query' = from_(t_15018).order_by(t_15019, False)
            t_15024: 'bool42' = q_1665.to_sql().to_string() == 'SELECT * FROM users ORDER BY created_at DESC'
            def fn_15017() -> 'str34':
                return 'order desc'
            test_126.assert_(t_15024, fn_15017)
        finally:
            test_126.soft_fail_to_hard()
class TestCase148(TestCase53):
    def test___limitAndOffset__2452(self) -> None:
        'limit and offset'
        test_127: Test = Test()
        try:
            t_7677: 'Query'
            t_7677 = from_(sid_709('users')).limit(10)
            t_7678: 'Query'
            t_7678 = t_7677.offset(20)
            q_1667: 'Query' = t_7678
            t_15015: 'bool42' = q_1667.to_sql().to_string() == 'SELECT * FROM users LIMIT 10 OFFSET 20'
            def fn_15010() -> 'str34':
                return 'limit/offset'
            test_127.assert_(t_15015, fn_15010)
        finally:
            test_127.soft_fail_to_hard()
class TestCase149(TestCase53):
    def test___limitBubblesOnNegative__2453(self) -> None:
        'limit bubbles on negative'
        test_128: Test = Test()
        try:
            did_bubble_1669: 'bool42'
            try:
                from_(sid_709('users')).limit(-1)
                did_bubble_1669 = False
            except Exception46:
                did_bubble_1669 = True
            def fn_15006() -> 'str34':
                return 'negative limit should bubble'
            test_128.assert_(did_bubble_1669, fn_15006)
        finally:
            test_128.soft_fail_to_hard()
class TestCase150(TestCase53):
    def test___offsetBubblesOnNegative__2454(self) -> None:
        'offset bubbles on negative'
        test_129: Test = Test()
        try:
            did_bubble_1671: 'bool42'
            try:
                from_(sid_709('users')).offset(-1)
                did_bubble_1671 = False
            except Exception46:
                did_bubble_1671 = True
            def fn_15002() -> 'str34':
                return 'negative offset should bubble'
            test_129.assert_(did_bubble_1671, fn_15002)
        finally:
            test_129.soft_fail_to_hard()
class TestCase151(TestCase53):
    def test___complexComposedQuery__2455(self) -> None:
        'complex composed query'
        test_130: Test = Test()
        try:
            min_age_1673: 'int40' = 21
            t_14980: 'SafeIdentifier' = sid_709('users')
            t_14981: 'SafeIdentifier' = sid_709('id')
            t_14982: 'SafeIdentifier' = sid_709('name')
            t_14983: 'SafeIdentifier' = sid_709('email')
            t_14984: 'Query' = from_(t_14980).select((t_14981, t_14982, t_14983))
            t_14985: 'SqlBuilder' = SqlBuilder()
            t_14985.append_safe('age >= ')
            t_14985.append_int32(21)
            t_14989: 'Query' = t_14984.where(t_14985.accumulated)
            t_14990: 'SqlBuilder' = SqlBuilder()
            t_14990.append_safe('active = ')
            t_14990.append_boolean(True)
            t_7663: 'Query'
            t_7663 = t_14989.where(t_14990.accumulated).order_by(sid_709('name'), True).limit(25)
            t_7664: 'Query'
            t_7664 = t_7663.offset(0)
            q_1674: 'Query' = t_7664
            t_15000: 'bool42' = q_1674.to_sql().to_string() == 'SELECT id, name, email FROM users WHERE age >= 21 AND active = TRUE ORDER BY name ASC LIMIT 25 OFFSET 0'
            def fn_14979() -> 'str34':
                return 'complex query'
            test_130.assert_(t_15000, fn_14979)
        finally:
            test_130.soft_fail_to_hard()
class TestCase152(TestCase53):
    def test___safeToSqlAppliesDefaultLimitWhenNoneSet__2458(self) -> None:
        'safeToSql applies default limit when none set'
        test_131: Test = Test()
        try:
            q_1676: 'Query' = from_(sid_709('users'))
            t_7640: 'SqlFragment'
            t_7640 = q_1676.safe_to_sql(100)
            t_7641: 'SqlFragment' = t_7640
            s_1677: 'str34' = t_7641.to_string()
            t_14977: 'bool42' = s_1677 == 'SELECT * FROM users LIMIT 100'
            def fn_14973() -> 'str34':
                return str_cat_17392('should have limit: ', s_1677)
            test_131.assert_(t_14977, fn_14973)
        finally:
            test_131.soft_fail_to_hard()
class TestCase153(TestCase53):
    def test___safeToSqlRespectsExplicitLimit__2459(self) -> None:
        'safeToSql respects explicit limit'
        test_132: Test = Test()
        try:
            t_7632: 'Query'
            t_7632 = from_(sid_709('users')).limit(5)
            q_1679: 'Query' = t_7632
            t_7635: 'SqlFragment'
            t_7635 = q_1679.safe_to_sql(100)
            t_7636: 'SqlFragment' = t_7635
            s_1680: 'str34' = t_7636.to_string()
            t_14971: 'bool42' = s_1680 == 'SELECT * FROM users LIMIT 5'
            def fn_14967() -> 'str34':
                return str_cat_17392('explicit limit preserved: ', s_1680)
            test_132.assert_(t_14971, fn_14967)
        finally:
            test_132.soft_fail_to_hard()
class TestCase154(TestCase53):
    def test___safeToSqlBubblesOnNegativeDefaultLimit__2460(self) -> None:
        'safeToSql bubbles on negative defaultLimit'
        test_133: Test = Test()
        try:
            did_bubble_1682: 'bool42'
            try:
                from_(sid_709('users')).safe_to_sql(-1)
                did_bubble_1682 = False
            except Exception46:
                did_bubble_1682 = True
            def fn_14963() -> 'str34':
                return 'negative defaultLimit should bubble'
            test_133.assert_(did_bubble_1682, fn_14963)
        finally:
            test_133.soft_fail_to_hard()
class TestCase155(TestCase53):
    def test___whereWithInjectionAttemptInStringValueIsEscaped__2461(self) -> None:
        'where with injection attempt in string value is escaped'
        test_134: Test = Test()
        try:
            evil_1684: 'str34' = "'; DROP TABLE users; --"
            t_14947: 'SafeIdentifier' = sid_709('users')
            t_14948: 'SqlBuilder' = SqlBuilder()
            t_14948.append_safe('name = ')
            t_14948.append_string("'; DROP TABLE users; --")
            t_14951: 'SqlFragment' = t_14948.accumulated
            q_1685: 'Query' = from_(t_14947).where(t_14951)
            s_1686: 'str34' = q_1685.to_sql().to_string()
            t_14956: 'bool42' = s_1686.find("''") >= 0
            def fn_14946() -> 'str34':
                return str_cat_17392('quotes must be doubled: ', s_1686)
            test_134.assert_(t_14956, fn_14946)
            t_14960: 'bool42' = s_1686.find('SELECT * FROM users WHERE name =') >= 0
            def fn_14945() -> 'str34':
                return str_cat_17392('structure intact: ', s_1686)
            test_134.assert_(t_14960, fn_14945)
        finally:
            test_134.soft_fail_to_hard()
class TestCase156(TestCase53):
    def test___safeIdentifierRejectsUserSuppliedTableNameWithMetacharacters__2463(self) -> None:
        'safeIdentifier rejects user-supplied table name with metacharacters'
        test_135: Test = Test()
        try:
            attack_1688: 'str34' = 'users; DROP TABLE users; --'
            did_bubble_1689: 'bool42'
            try:
                safe_identifier('users; DROP TABLE users; --')
                did_bubble_1689 = False
            except Exception46:
                did_bubble_1689 = True
            def fn_14942() -> 'str34':
                return 'metacharacter-containing name must be rejected at construction'
            test_135.assert_(did_bubble_1689, fn_14942)
        finally:
            test_135.soft_fail_to_hard()
class TestCase157(TestCase53):
    def test___innerJoinProducesInnerJoin__2464(self) -> None:
        'innerJoin produces INNER JOIN'
        test_136: Test = Test()
        try:
            t_14931: 'SafeIdentifier' = sid_709('users')
            t_14932: 'SafeIdentifier' = sid_709('orders')
            t_14933: 'SqlBuilder' = SqlBuilder()
            t_14933.append_safe('users.id = orders.user_id')
            t_14935: 'SqlFragment' = t_14933.accumulated
            q_1691: 'Query' = from_(t_14931).inner_join(t_14932, t_14935)
            t_14940: 'bool42' = q_1691.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_14930() -> 'str34':
                return 'inner join'
            test_136.assert_(t_14940, fn_14930)
        finally:
            test_136.soft_fail_to_hard()
class TestCase158(TestCase53):
    def test___leftJoinProducesLeftJoin__2466(self) -> None:
        'leftJoin produces LEFT JOIN'
        test_137: Test = Test()
        try:
            t_14919: 'SafeIdentifier' = sid_709('users')
            t_14920: 'SafeIdentifier' = sid_709('profiles')
            t_14921: 'SqlBuilder' = SqlBuilder()
            t_14921.append_safe('users.id = profiles.user_id')
            t_14923: 'SqlFragment' = t_14921.accumulated
            q_1693: 'Query' = from_(t_14919).left_join(t_14920, t_14923)
            t_14928: 'bool42' = q_1693.to_sql().to_string() == 'SELECT * FROM users LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_14918() -> 'str34':
                return 'left join'
            test_137.assert_(t_14928, fn_14918)
        finally:
            test_137.soft_fail_to_hard()
class TestCase159(TestCase53):
    def test___rightJoinProducesRightJoin__2468(self) -> None:
        'rightJoin produces RIGHT JOIN'
        test_138: Test = Test()
        try:
            t_14907: 'SafeIdentifier' = sid_709('orders')
            t_14908: 'SafeIdentifier' = sid_709('users')
            t_14909: 'SqlBuilder' = SqlBuilder()
            t_14909.append_safe('orders.user_id = users.id')
            t_14911: 'SqlFragment' = t_14909.accumulated
            q_1695: 'Query' = from_(t_14907).right_join(t_14908, t_14911)
            t_14916: 'bool42' = q_1695.to_sql().to_string() == 'SELECT * FROM orders RIGHT JOIN users ON orders.user_id = users.id'
            def fn_14906() -> 'str34':
                return 'right join'
            test_138.assert_(t_14916, fn_14906)
        finally:
            test_138.soft_fail_to_hard()
class TestCase160(TestCase53):
    def test___fullJoinProducesFullOuterJoin__2470(self) -> None:
        'fullJoin produces FULL OUTER JOIN'
        test_139: Test = Test()
        try:
            t_14895: 'SafeIdentifier' = sid_709('users')
            t_14896: 'SafeIdentifier' = sid_709('orders')
            t_14897: 'SqlBuilder' = SqlBuilder()
            t_14897.append_safe('users.id = orders.user_id')
            t_14899: 'SqlFragment' = t_14897.accumulated
            q_1697: 'Query' = from_(t_14895).full_join(t_14896, t_14899)
            t_14904: 'bool42' = q_1697.to_sql().to_string() == 'SELECT * FROM users FULL OUTER JOIN orders ON users.id = orders.user_id'
            def fn_14894() -> 'str34':
                return 'full join'
            test_139.assert_(t_14904, fn_14894)
        finally:
            test_139.soft_fail_to_hard()
class TestCase161(TestCase53):
    def test___chainedJoins__2472(self) -> None:
        'chained joins'
        test_140: Test = Test()
        try:
            t_14878: 'SafeIdentifier' = sid_709('users')
            t_14879: 'SafeIdentifier' = sid_709('orders')
            t_14880: 'SqlBuilder' = SqlBuilder()
            t_14880.append_safe('users.id = orders.user_id')
            t_14882: 'SqlFragment' = t_14880.accumulated
            t_14883: 'Query' = from_(t_14878).inner_join(t_14879, t_14882)
            t_14884: 'SafeIdentifier' = sid_709('profiles')
            t_14885: 'SqlBuilder' = SqlBuilder()
            t_14885.append_safe('users.id = profiles.user_id')
            q_1699: 'Query' = t_14883.left_join(t_14884, t_14885.accumulated)
            t_14892: 'bool42' = q_1699.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id LEFT JOIN profiles ON users.id = profiles.user_id'
            def fn_14877() -> 'str34':
                return 'chained joins'
            test_140.assert_(t_14892, fn_14877)
        finally:
            test_140.soft_fail_to_hard()
class TestCase162(TestCase53):
    def test___joinWithWhereAndOrderBy__2475(self) -> None:
        'join with where and orderBy'
        test_141: Test = Test()
        try:
            t_14859: 'SafeIdentifier' = sid_709('users')
            t_14860: 'SafeIdentifier' = sid_709('orders')
            t_14861: 'SqlBuilder' = SqlBuilder()
            t_14861.append_safe('users.id = orders.user_id')
            t_14863: 'SqlFragment' = t_14861.accumulated
            t_14864: 'Query' = from_(t_14859).inner_join(t_14860, t_14863)
            t_14865: 'SqlBuilder' = SqlBuilder()
            t_14865.append_safe('orders.total > ')
            t_14865.append_int32(100)
            t_7547: 'Query'
            t_7547 = t_14864.where(t_14865.accumulated).order_by(sid_709('name'), True).limit(10)
            q_1701: 'Query' = t_7547
            t_14875: 'bool42' = q_1701.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100 ORDER BY name ASC LIMIT 10'
            def fn_14858() -> 'str34':
                return 'join with where/order/limit'
            test_141.assert_(t_14875, fn_14858)
        finally:
            test_141.soft_fail_to_hard()
class TestCase163(TestCase53):
    def test___colHelperProducesQualifiedReference__2478(self) -> None:
        'col helper produces qualified reference'
        test_142: Test = Test()
        try:
            c_1703: 'SqlFragment' = col(sid_709('users'), sid_709('id'))
            t_14856: 'bool42' = c_1703.to_string() == 'users.id'
            def fn_14850() -> 'str34':
                return 'col helper'
            test_142.assert_(t_14856, fn_14850)
        finally:
            test_142.soft_fail_to_hard()
class TestCase164(TestCase53):
    def test___joinWithColHelper__2479(self) -> None:
        'join with col helper'
        test_143: Test = Test()
        try:
            on_cond_1705: 'SqlFragment' = col(sid_709('users'), sid_709('id'))
            b_1706: 'SqlBuilder' = SqlBuilder()
            b_1706.append_fragment(on_cond_1705)
            b_1706.append_safe(' = ')
            b_1706.append_fragment(col(sid_709('orders'), sid_709('user_id')))
            t_14841: 'SafeIdentifier' = sid_709('users')
            t_14842: 'SafeIdentifier' = sid_709('orders')
            t_14843: 'SqlFragment' = b_1706.accumulated
            q_1707: 'Query' = from_(t_14841).inner_join(t_14842, t_14843)
            t_14848: 'bool42' = q_1707.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id'
            def fn_14830() -> 'str34':
                return 'join with col'
            test_143.assert_(t_14848, fn_14830)
        finally:
            test_143.soft_fail_to_hard()
class TestCase165(TestCase53):
    def test___orWhereBasic__2480(self) -> None:
        'orWhere basic'
        test_144: Test = Test()
        try:
            t_14819: 'SafeIdentifier' = sid_709('users')
            t_14820: 'SqlBuilder' = SqlBuilder()
            t_14820.append_safe('status = ')
            t_14820.append_string('active')
            t_14823: 'SqlFragment' = t_14820.accumulated
            q_1709: 'Query' = from_(t_14819).or_where(t_14823)
            t_14828: 'bool42' = q_1709.to_sql().to_string() == "SELECT * FROM users WHERE status = 'active'"
            def fn_14818() -> 'str34':
                return 'orWhere basic'
            test_144.assert_(t_14828, fn_14818)
        finally:
            test_144.soft_fail_to_hard()
class TestCase166(TestCase53):
    def test___whereThenOrWhere__2482(self) -> None:
        'where then orWhere'
        test_145: Test = Test()
        try:
            t_14802: 'SafeIdentifier' = sid_709('users')
            t_14803: 'SqlBuilder' = SqlBuilder()
            t_14803.append_safe('age > ')
            t_14803.append_int32(18)
            t_14806: 'SqlFragment' = t_14803.accumulated
            t_14807: 'Query' = from_(t_14802).where(t_14806)
            t_14808: 'SqlBuilder' = SqlBuilder()
            t_14808.append_safe('vip = ')
            t_14808.append_boolean(True)
            q_1711: 'Query' = t_14807.or_where(t_14808.accumulated)
            t_14816: 'bool42' = q_1711.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 OR vip = TRUE'
            def fn_14801() -> 'str34':
                return 'where then orWhere'
            test_145.assert_(t_14816, fn_14801)
        finally:
            test_145.soft_fail_to_hard()
class TestCase167(TestCase53):
    def test___multipleOrWhere__2485(self) -> None:
        'multiple orWhere'
        test_146: Test = Test()
        try:
            t_14780: 'SafeIdentifier' = sid_709('users')
            t_14781: 'SqlBuilder' = SqlBuilder()
            t_14781.append_safe('active = ')
            t_14781.append_boolean(True)
            t_14784: 'SqlFragment' = t_14781.accumulated
            t_14785: 'Query' = from_(t_14780).where(t_14784)
            t_14786: 'SqlBuilder' = SqlBuilder()
            t_14786.append_safe('role = ')
            t_14786.append_string('admin')
            t_14790: 'Query' = t_14785.or_where(t_14786.accumulated)
            t_14791: 'SqlBuilder' = SqlBuilder()
            t_14791.append_safe('role = ')
            t_14791.append_string('moderator')
            q_1713: 'Query' = t_14790.or_where(t_14791.accumulated)
            t_14799: 'bool42' = q_1713.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE OR role = 'admin' OR role = 'moderator'"
            def fn_14779() -> 'str34':
                return 'multiple orWhere'
            test_146.assert_(t_14799, fn_14779)
        finally:
            test_146.soft_fail_to_hard()
class TestCase168(TestCase53):
    def test___mixedWhereAndOrWhere__2489(self) -> None:
        'mixed where and orWhere'
        test_147: Test = Test()
        try:
            t_14758: 'SafeIdentifier' = sid_709('users')
            t_14759: 'SqlBuilder' = SqlBuilder()
            t_14759.append_safe('age > ')
            t_14759.append_int32(18)
            t_14762: 'SqlFragment' = t_14759.accumulated
            t_14763: 'Query' = from_(t_14758).where(t_14762)
            t_14764: 'SqlBuilder' = SqlBuilder()
            t_14764.append_safe('active = ')
            t_14764.append_boolean(True)
            t_14768: 'Query' = t_14763.where(t_14764.accumulated)
            t_14769: 'SqlBuilder' = SqlBuilder()
            t_14769.append_safe('vip = ')
            t_14769.append_boolean(True)
            q_1715: 'Query' = t_14768.or_where(t_14769.accumulated)
            t_14777: 'bool42' = q_1715.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND active = TRUE OR vip = TRUE'
            def fn_14757() -> 'str34':
                return 'mixed where and orWhere'
            test_147.assert_(t_14777, fn_14757)
        finally:
            test_147.soft_fail_to_hard()
class TestCase169(TestCase53):
    def test___whereNull__2493(self) -> None:
        'whereNull'
        test_148: Test = Test()
        try:
            t_14749: 'SafeIdentifier' = sid_709('users')
            t_14750: 'SafeIdentifier' = sid_709('deleted_at')
            q_1717: 'Query' = from_(t_14749).where_null(t_14750)
            t_14755: 'bool42' = q_1717.to_sql().to_string() == 'SELECT * FROM users WHERE deleted_at IS NULL'
            def fn_14748() -> 'str34':
                return 'whereNull'
            test_148.assert_(t_14755, fn_14748)
        finally:
            test_148.soft_fail_to_hard()
class TestCase170(TestCase53):
    def test___whereNotNull__2494(self) -> None:
        'whereNotNull'
        test_149: Test = Test()
        try:
            t_14740: 'SafeIdentifier' = sid_709('users')
            t_14741: 'SafeIdentifier' = sid_709('email')
            q_1719: 'Query' = from_(t_14740).where_not_null(t_14741)
            t_14746: 'bool42' = q_1719.to_sql().to_string() == 'SELECT * FROM users WHERE email IS NOT NULL'
            def fn_14739() -> 'str34':
                return 'whereNotNull'
            test_149.assert_(t_14746, fn_14739)
        finally:
            test_149.soft_fail_to_hard()
class TestCase171(TestCase53):
    def test___whereNullChainedWithWhere__2495(self) -> None:
        'whereNull chained with where'
        test_150: Test = Test()
        try:
            t_14726: 'SafeIdentifier' = sid_709('users')
            t_14727: 'SqlBuilder' = SqlBuilder()
            t_14727.append_safe('active = ')
            t_14727.append_boolean(True)
            t_14730: 'SqlFragment' = t_14727.accumulated
            q_1721: 'Query' = from_(t_14726).where(t_14730).where_null(sid_709('deleted_at'))
            t_14737: 'bool42' = q_1721.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND deleted_at IS NULL'
            def fn_14725() -> 'str34':
                return 'whereNull chained'
            test_150.assert_(t_14737, fn_14725)
        finally:
            test_150.soft_fail_to_hard()
class TestCase172(TestCase53):
    def test___whereNotNullChainedWithOrWhere__2497(self) -> None:
        'whereNotNull chained with orWhere'
        test_151: Test = Test()
        try:
            t_14712: 'SafeIdentifier' = sid_709('users')
            t_14713: 'SafeIdentifier' = sid_709('deleted_at')
            t_14714: 'Query' = from_(t_14712).where_null(t_14713)
            t_14715: 'SqlBuilder' = SqlBuilder()
            t_14715.append_safe('role = ')
            t_14715.append_string('admin')
            q_1723: 'Query' = t_14714.or_where(t_14715.accumulated)
            t_14723: 'bool42' = q_1723.to_sql().to_string() == "SELECT * FROM users WHERE deleted_at IS NULL OR role = 'admin'"
            def fn_14711() -> 'str34':
                return 'whereNotNull with orWhere'
            test_151.assert_(t_14723, fn_14711)
        finally:
            test_151.soft_fail_to_hard()
class TestCase173(TestCase53):
    def test___whereInWithIntValues__2499(self) -> None:
        'whereIn with int values'
        test_152: Test = Test()
        try:
            t_14700: 'SafeIdentifier' = sid_709('users')
            t_14701: 'SafeIdentifier' = sid_709('id')
            t_14702: 'SqlInt32' = SqlInt32(1)
            t_14703: 'SqlInt32' = SqlInt32(2)
            t_14704: 'SqlInt32' = SqlInt32(3)
            q_1725: 'Query' = from_(t_14700).where_in(t_14701, (t_14702, t_14703, t_14704))
            t_14709: 'bool42' = q_1725.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (1, 2, 3)'
            def fn_14699() -> 'str34':
                return 'whereIn ints'
            test_152.assert_(t_14709, fn_14699)
        finally:
            test_152.soft_fail_to_hard()
class TestCase174(TestCase53):
    def test___whereInWithStringValuesEscaping__2500(self) -> None:
        'whereIn with string values escaping'
        test_153: Test = Test()
        try:
            t_14689: 'SafeIdentifier' = sid_709('users')
            t_14690: 'SafeIdentifier' = sid_709('name')
            t_14691: 'SqlString' = SqlString('Alice')
            t_14692: 'SqlString' = SqlString("Bob's")
            q_1727: 'Query' = from_(t_14689).where_in(t_14690, (t_14691, t_14692))
            t_14697: 'bool42' = q_1727.to_sql().to_string() == "SELECT * FROM users WHERE name IN ('Alice', 'Bob''s')"
            def fn_14688() -> 'str34':
                return 'whereIn strings'
            test_153.assert_(t_14697, fn_14688)
        finally:
            test_153.soft_fail_to_hard()
class TestCase175(TestCase53):
    def test___whereInWithEmptyListProduces1_0__2501(self) -> None:
        'whereIn with empty list produces 1=0'
        test_154: Test = Test()
        try:
            t_14680: 'SafeIdentifier' = sid_709('users')
            t_14681: 'SafeIdentifier' = sid_709('id')
            q_1729: 'Query' = from_(t_14680).where_in(t_14681, ())
            t_14686: 'bool42' = q_1729.to_sql().to_string() == 'SELECT * FROM users WHERE 1 = 0'
            def fn_14679() -> 'str34':
                return 'whereIn empty'
            test_154.assert_(t_14686, fn_14679)
        finally:
            test_154.soft_fail_to_hard()
class TestCase176(TestCase53):
    def test___whereInChained__2502(self) -> None:
        'whereIn chained'
        test_155: Test = Test()
        try:
            t_14664: 'SafeIdentifier' = sid_709('users')
            t_14665: 'SqlBuilder' = SqlBuilder()
            t_14665.append_safe('active = ')
            t_14665.append_boolean(True)
            t_14668: 'SqlFragment' = t_14665.accumulated
            q_1731: 'Query' = from_(t_14664).where(t_14668).where_in(sid_709('role'), (SqlString('admin'), SqlString('user')))
            t_14677: 'bool42' = q_1731.to_sql().to_string() == "SELECT * FROM users WHERE active = TRUE AND role IN ('admin', 'user')"
            def fn_14663() -> 'str34':
                return 'whereIn chained'
            test_155.assert_(t_14677, fn_14663)
        finally:
            test_155.soft_fail_to_hard()
class TestCase177(TestCase53):
    def test___whereInSingleElement__2504(self) -> None:
        'whereIn single element'
        test_156: Test = Test()
        try:
            t_14654: 'SafeIdentifier' = sid_709('users')
            t_14655: 'SafeIdentifier' = sid_709('id')
            t_14656: 'SqlInt32' = SqlInt32(42)
            q_1733: 'Query' = from_(t_14654).where_in(t_14655, (t_14656,))
            t_14661: 'bool42' = q_1733.to_sql().to_string() == 'SELECT * FROM users WHERE id IN (42)'
            def fn_14653() -> 'str34':
                return 'whereIn single'
            test_156.assert_(t_14661, fn_14653)
        finally:
            test_156.soft_fail_to_hard()
class TestCase178(TestCase53):
    def test___whereNotBasic__2505(self) -> None:
        'whereNot basic'
        test_157: Test = Test()
        try:
            t_14642: 'SafeIdentifier' = sid_709('users')
            t_14643: 'SqlBuilder' = SqlBuilder()
            t_14643.append_safe('active = ')
            t_14643.append_boolean(True)
            t_14646: 'SqlFragment' = t_14643.accumulated
            q_1735: 'Query' = from_(t_14642).where_not(t_14646)
            t_14651: 'bool42' = q_1735.to_sql().to_string() == 'SELECT * FROM users WHERE NOT (active = TRUE)'
            def fn_14641() -> 'str34':
                return 'whereNot'
            test_157.assert_(t_14651, fn_14641)
        finally:
            test_157.soft_fail_to_hard()
class TestCase179(TestCase53):
    def test___whereNotChained__2507(self) -> None:
        'whereNot chained'
        test_158: Test = Test()
        try:
            t_14625: 'SafeIdentifier' = sid_709('users')
            t_14626: 'SqlBuilder' = SqlBuilder()
            t_14626.append_safe('age > ')
            t_14626.append_int32(18)
            t_14629: 'SqlFragment' = t_14626.accumulated
            t_14630: 'Query' = from_(t_14625).where(t_14629)
            t_14631: 'SqlBuilder' = SqlBuilder()
            t_14631.append_safe('banned = ')
            t_14631.append_boolean(True)
            q_1737: 'Query' = t_14630.where_not(t_14631.accumulated)
            t_14639: 'bool42' = q_1737.to_sql().to_string() == 'SELECT * FROM users WHERE age > 18 AND NOT (banned = TRUE)'
            def fn_14624() -> 'str34':
                return 'whereNot chained'
            test_158.assert_(t_14639, fn_14624)
        finally:
            test_158.soft_fail_to_hard()
class TestCase180(TestCase53):
    def test___whereBetweenIntegers__2510(self) -> None:
        'whereBetween integers'
        test_159: Test = Test()
        try:
            t_14614: 'SafeIdentifier' = sid_709('users')
            t_14615: 'SafeIdentifier' = sid_709('age')
            t_14616: 'SqlInt32' = SqlInt32(18)
            t_14617: 'SqlInt32' = SqlInt32(65)
            q_1739: 'Query' = from_(t_14614).where_between(t_14615, t_14616, t_14617)
            t_14622: 'bool42' = q_1739.to_sql().to_string() == 'SELECT * FROM users WHERE age BETWEEN 18 AND 65'
            def fn_14613() -> 'str34':
                return 'whereBetween ints'
            test_159.assert_(t_14622, fn_14613)
        finally:
            test_159.soft_fail_to_hard()
class TestCase181(TestCase53):
    def test___whereBetweenChained__2511(self) -> None:
        'whereBetween chained'
        test_160: Test = Test()
        try:
            t_14598: 'SafeIdentifier' = sid_709('users')
            t_14599: 'SqlBuilder' = SqlBuilder()
            t_14599.append_safe('active = ')
            t_14599.append_boolean(True)
            t_14602: 'SqlFragment' = t_14599.accumulated
            q_1741: 'Query' = from_(t_14598).where(t_14602).where_between(sid_709('age'), SqlInt32(21), SqlInt32(30))
            t_14611: 'bool42' = q_1741.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE AND age BETWEEN 21 AND 30'
            def fn_14597() -> 'str34':
                return 'whereBetween chained'
            test_160.assert_(t_14611, fn_14597)
        finally:
            test_160.soft_fail_to_hard()
class TestCase182(TestCase53):
    def test___whereLikeBasic__2513(self) -> None:
        'whereLike basic'
        test_161: Test = Test()
        try:
            t_14589: 'SafeIdentifier' = sid_709('users')
            t_14590: 'SafeIdentifier' = sid_709('name')
            q_1743: 'Query' = from_(t_14589).where_like(t_14590, 'John%')
            t_14595: 'bool42' = q_1743.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE 'John%'"
            def fn_14588() -> 'str34':
                return 'whereLike'
            test_161.assert_(t_14595, fn_14588)
        finally:
            test_161.soft_fail_to_hard()
class TestCase183(TestCase53):
    def test___whereIlikeBasic__2514(self) -> None:
        'whereILike basic'
        test_162: Test = Test()
        try:
            t_14580: 'SafeIdentifier' = sid_709('users')
            t_14581: 'SafeIdentifier' = sid_709('email')
            q_1745: 'Query' = from_(t_14580).where_i_like(t_14581, '%@gmail.com')
            t_14586: 'bool42' = q_1745.to_sql().to_string() == "SELECT * FROM users WHERE email ILIKE '%@gmail.com'"
            def fn_14579() -> 'str34':
                return 'whereILike'
            test_162.assert_(t_14586, fn_14579)
        finally:
            test_162.soft_fail_to_hard()
class TestCase184(TestCase53):
    def test___whereLikeWithInjectionAttempt__2515(self) -> None:
        'whereLike with injection attempt'
        test_163: Test = Test()
        try:
            t_14566: 'SafeIdentifier' = sid_709('users')
            t_14567: 'SafeIdentifier' = sid_709('name')
            q_1747: 'Query' = from_(t_14566).where_like(t_14567, "'; DROP TABLE users; --")
            s_1748: 'str34' = q_1747.to_sql().to_string()
            t_14572: 'bool42' = s_1748.find("''") >= 0
            def fn_14565() -> 'str34':
                return str_cat_17392('like injection escaped: ', s_1748)
            test_163.assert_(t_14572, fn_14565)
            t_14576: 'bool42' = s_1748.find('LIKE') >= 0
            def fn_14564() -> 'str34':
                return str_cat_17392('like structure intact: ', s_1748)
            test_163.assert_(t_14576, fn_14564)
        finally:
            test_163.soft_fail_to_hard()
class TestCase185(TestCase53):
    def test___whereLikeWildcardPatterns__2516(self) -> None:
        'whereLike wildcard patterns'
        test_164: Test = Test()
        try:
            t_14556: 'SafeIdentifier' = sid_709('users')
            t_14557: 'SafeIdentifier' = sid_709('name')
            q_1750: 'Query' = from_(t_14556).where_like(t_14557, '%son%')
            t_14562: 'bool42' = q_1750.to_sql().to_string() == "SELECT * FROM users WHERE name LIKE '%son%'"
            def fn_14555() -> 'str34':
                return 'whereLike wildcard'
            test_164.assert_(t_14562, fn_14555)
        finally:
            test_164.soft_fail_to_hard()
class TestCase186(TestCase53):
    def test___countAllProducesCount__2517(self) -> None:
        'countAll produces COUNT(*)'
        test_165: Test = Test()
        try:
            f_1752: 'SqlFragment' = count_all()
            t_14553: 'bool42' = f_1752.to_string() == 'COUNT(*)'
            def fn_14549() -> 'str34':
                return 'countAll'
            test_165.assert_(t_14553, fn_14549)
        finally:
            test_165.soft_fail_to_hard()
class TestCase187(TestCase53):
    def test___countColProducesCountField__2518(self) -> None:
        'countCol produces COUNT(field)'
        test_166: Test = Test()
        try:
            f_1754: 'SqlFragment' = count_col(sid_709('id'))
            t_14547: 'bool42' = f_1754.to_string() == 'COUNT(id)'
            def fn_14542() -> 'str34':
                return 'countCol'
            test_166.assert_(t_14547, fn_14542)
        finally:
            test_166.soft_fail_to_hard()
class TestCase188(TestCase53):
    def test___sumColProducesSumField__2519(self) -> None:
        'sumCol produces SUM(field)'
        test_167: Test = Test()
        try:
            f_1756: 'SqlFragment' = sum_col(sid_709('amount'))
            t_14540: 'bool42' = f_1756.to_string() == 'SUM(amount)'
            def fn_14535() -> 'str34':
                return 'sumCol'
            test_167.assert_(t_14540, fn_14535)
        finally:
            test_167.soft_fail_to_hard()
class TestCase189(TestCase53):
    def test___avgColProducesAvgField__2520(self) -> None:
        'avgCol produces AVG(field)'
        test_168: Test = Test()
        try:
            f_1758: 'SqlFragment' = avg_col(sid_709('price'))
            t_14533: 'bool42' = f_1758.to_string() == 'AVG(price)'
            def fn_14528() -> 'str34':
                return 'avgCol'
            test_168.assert_(t_14533, fn_14528)
        finally:
            test_168.soft_fail_to_hard()
class TestCase190(TestCase53):
    def test___minColProducesMinField__2521(self) -> None:
        'minCol produces MIN(field)'
        test_169: Test = Test()
        try:
            f_1760: 'SqlFragment' = min_col(sid_709('created_at'))
            t_14526: 'bool42' = f_1760.to_string() == 'MIN(created_at)'
            def fn_14521() -> 'str34':
                return 'minCol'
            test_169.assert_(t_14526, fn_14521)
        finally:
            test_169.soft_fail_to_hard()
class TestCase191(TestCase53):
    def test___maxColProducesMaxField__2522(self) -> None:
        'maxCol produces MAX(field)'
        test_170: Test = Test()
        try:
            f_1762: 'SqlFragment' = max_col(sid_709('score'))
            t_14519: 'bool42' = f_1762.to_string() == 'MAX(score)'
            def fn_14514() -> 'str34':
                return 'maxCol'
            test_170.assert_(t_14519, fn_14514)
        finally:
            test_170.soft_fail_to_hard()
class TestCase192(TestCase53):
    def test___selectExprWithAggregate__2523(self) -> None:
        'selectExpr with aggregate'
        test_171: Test = Test()
        try:
            t_14506: 'SafeIdentifier' = sid_709('orders')
            t_14507: 'SqlFragment' = count_all()
            q_1764: 'Query' = from_(t_14506).select_expr((t_14507,))
            t_14512: 'bool42' = q_1764.to_sql().to_string() == 'SELECT COUNT(*) FROM orders'
            def fn_14505() -> 'str34':
                return 'selectExpr count'
            test_171.assert_(t_14512, fn_14505)
        finally:
            test_171.soft_fail_to_hard()
class TestCase193(TestCase53):
    def test___selectExprWithMultipleExpressions__2524(self) -> None:
        'selectExpr with multiple expressions'
        test_172: Test = Test()
        try:
            name_frag_1766: 'SqlFragment' = col(sid_709('users'), sid_709('name'))
            t_14497: 'SafeIdentifier' = sid_709('users')
            t_14498: 'SqlFragment' = count_all()
            q_1767: 'Query' = from_(t_14497).select_expr((name_frag_1766, t_14498))
            t_14503: 'bool42' = q_1767.to_sql().to_string() == 'SELECT users.name, COUNT(*) FROM users'
            def fn_14493() -> 'str34':
                return 'selectExpr multi'
            test_172.assert_(t_14503, fn_14493)
        finally:
            test_172.soft_fail_to_hard()
class TestCase194(TestCase53):
    def test___selectExprOverridesSelectedFields__2525(self) -> None:
        'selectExpr overrides selectedFields'
        test_173: Test = Test()
        try:
            t_14482: 'SafeIdentifier' = sid_709('users')
            t_14483: 'SafeIdentifier' = sid_709('id')
            t_14484: 'SafeIdentifier' = sid_709('name')
            q_1769: 'Query' = from_(t_14482).select((t_14483, t_14484)).select_expr((count_all(),))
            t_14491: 'bool42' = q_1769.to_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_14481() -> 'str34':
                return 'selectExpr overrides select'
            test_173.assert_(t_14491, fn_14481)
        finally:
            test_173.soft_fail_to_hard()
class TestCase195(TestCase53):
    def test___groupBySingleField__2526(self) -> None:
        'groupBy single field'
        test_174: Test = Test()
        try:
            t_14468: 'SafeIdentifier' = sid_709('orders')
            t_14471: 'SqlFragment' = col(sid_709('orders'), sid_709('status'))
            t_14472: 'SqlFragment' = count_all()
            q_1771: 'Query' = from_(t_14468).select_expr((t_14471, t_14472)).group_by(sid_709('status'))
            t_14479: 'bool42' = q_1771.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status'
            def fn_14467() -> 'str34':
                return 'groupBy single'
            test_174.assert_(t_14479, fn_14467)
        finally:
            test_174.soft_fail_to_hard()
class TestCase196(TestCase53):
    def test___groupByMultipleFields__2527(self) -> None:
        'groupBy multiple fields'
        test_175: Test = Test()
        try:
            t_14457: 'SafeIdentifier' = sid_709('orders')
            t_14458: 'SafeIdentifier' = sid_709('status')
            q_1773: 'Query' = from_(t_14457).group_by(t_14458).group_by(sid_709('category'))
            t_14465: 'bool42' = q_1773.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status, category'
            def fn_14456() -> 'str34':
                return 'groupBy multiple'
            test_175.assert_(t_14465, fn_14456)
        finally:
            test_175.soft_fail_to_hard()
class TestCase197(TestCase53):
    def test___havingBasic__2528(self) -> None:
        'having basic'
        test_176: Test = Test()
        try:
            t_14438: 'SafeIdentifier' = sid_709('orders')
            t_14441: 'SqlFragment' = col(sid_709('orders'), sid_709('status'))
            t_14442: 'SqlFragment' = count_all()
            t_14445: 'Query' = from_(t_14438).select_expr((t_14441, t_14442)).group_by(sid_709('status'))
            t_14446: 'SqlBuilder' = SqlBuilder()
            t_14446.append_safe('COUNT(*) > ')
            t_14446.append_int32(5)
            q_1775: 'Query' = t_14445.having(t_14446.accumulated)
            t_14454: 'bool42' = q_1775.to_sql().to_string() == 'SELECT orders.status, COUNT(*) FROM orders GROUP BY status HAVING COUNT(*) > 5'
            def fn_14437() -> 'str34':
                return 'having basic'
            test_176.assert_(t_14454, fn_14437)
        finally:
            test_176.soft_fail_to_hard()
class TestCase198(TestCase53):
    def test___orHaving__2530(self) -> None:
        'orHaving'
        test_177: Test = Test()
        try:
            t_14419: 'SafeIdentifier' = sid_709('orders')
            t_14420: 'SafeIdentifier' = sid_709('status')
            t_14421: 'Query' = from_(t_14419).group_by(t_14420)
            t_14422: 'SqlBuilder' = SqlBuilder()
            t_14422.append_safe('COUNT(*) > ')
            t_14422.append_int32(5)
            t_14426: 'Query' = t_14421.having(t_14422.accumulated)
            t_14427: 'SqlBuilder' = SqlBuilder()
            t_14427.append_safe('SUM(total) > ')
            t_14427.append_int32(1000)
            q_1777: 'Query' = t_14426.or_having(t_14427.accumulated)
            t_14435: 'bool42' = q_1777.to_sql().to_string() == 'SELECT * FROM orders GROUP BY status HAVING COUNT(*) > 5 OR SUM(total) > 1000'
            def fn_14418() -> 'str34':
                return 'orHaving'
            test_177.assert_(t_14435, fn_14418)
        finally:
            test_177.soft_fail_to_hard()
class TestCase199(TestCase53):
    def test___distinctBasic__2533(self) -> None:
        'distinct basic'
        test_178: Test = Test()
        try:
            t_14409: 'SafeIdentifier' = sid_709('users')
            t_14410: 'SafeIdentifier' = sid_709('name')
            q_1779: 'Query' = from_(t_14409).select((t_14410,)).distinct()
            t_14416: 'bool42' = q_1779.to_sql().to_string() == 'SELECT DISTINCT name FROM users'
            def fn_14408() -> 'str34':
                return 'distinct'
            test_178.assert_(t_14416, fn_14408)
        finally:
            test_178.soft_fail_to_hard()
class TestCase200(TestCase53):
    def test___distinctWithWhere__2534(self) -> None:
        'distinct with where'
        test_179: Test = Test()
        try:
            t_14394: 'SafeIdentifier' = sid_709('users')
            t_14395: 'SafeIdentifier' = sid_709('email')
            t_14396: 'Query' = from_(t_14394).select((t_14395,))
            t_14397: 'SqlBuilder' = SqlBuilder()
            t_14397.append_safe('active = ')
            t_14397.append_boolean(True)
            q_1781: 'Query' = t_14396.where(t_14397.accumulated).distinct()
            t_14406: 'bool42' = q_1781.to_sql().to_string() == 'SELECT DISTINCT email FROM users WHERE active = TRUE'
            def fn_14393() -> 'str34':
                return 'distinct with where'
            test_179.assert_(t_14406, fn_14393)
        finally:
            test_179.soft_fail_to_hard()
class TestCase201(TestCase53):
    def test___countSqlBare__2536(self) -> None:
        'countSql bare'
        test_180: Test = Test()
        try:
            q_1783: 'Query' = from_(sid_709('users'))
            t_14391: 'bool42' = q_1783.count_sql().to_string() == 'SELECT COUNT(*) FROM users'
            def fn_14386() -> 'str34':
                return 'countSql bare'
            test_180.assert_(t_14391, fn_14386)
        finally:
            test_180.soft_fail_to_hard()
class TestCase202(TestCase53):
    def test___countSqlWithWhere__2537(self) -> None:
        'countSql with WHERE'
        test_181: Test = Test()
        try:
            t_14375: 'SafeIdentifier' = sid_709('users')
            t_14376: 'SqlBuilder' = SqlBuilder()
            t_14376.append_safe('active = ')
            t_14376.append_boolean(True)
            t_14379: 'SqlFragment' = t_14376.accumulated
            q_1785: 'Query' = from_(t_14375).where(t_14379)
            t_14384: 'bool42' = q_1785.count_sql().to_string() == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_14374() -> 'str34':
                return 'countSql with where'
            test_181.assert_(t_14384, fn_14374)
        finally:
            test_181.soft_fail_to_hard()
class TestCase203(TestCase53):
    def test___countSqlWithJoin__2539(self) -> None:
        'countSql with JOIN'
        test_182: Test = Test()
        try:
            t_14358: 'SafeIdentifier' = sid_709('users')
            t_14359: 'SafeIdentifier' = sid_709('orders')
            t_14360: 'SqlBuilder' = SqlBuilder()
            t_14360.append_safe('users.id = orders.user_id')
            t_14362: 'SqlFragment' = t_14360.accumulated
            t_14363: 'Query' = from_(t_14358).inner_join(t_14359, t_14362)
            t_14364: 'SqlBuilder' = SqlBuilder()
            t_14364.append_safe('orders.total > ')
            t_14364.append_int32(100)
            q_1787: 'Query' = t_14363.where(t_14364.accumulated)
            t_14372: 'bool42' = q_1787.count_sql().to_string() == 'SELECT COUNT(*) FROM users INNER JOIN orders ON users.id = orders.user_id WHERE orders.total > 100'
            def fn_14357() -> 'str34':
                return 'countSql with join'
            test_182.assert_(t_14372, fn_14357)
        finally:
            test_182.soft_fail_to_hard()
class TestCase204(TestCase53):
    def test___countSqlDropsOrderByLimitOffset__2542(self) -> None:
        'countSql drops orderBy/limit/offset'
        test_183: Test = Test()
        try:
            t_14344: 'SafeIdentifier' = sid_709('users')
            t_14345: 'SqlBuilder' = SqlBuilder()
            t_14345.append_safe('active = ')
            t_14345.append_boolean(True)
            t_14348: 'SqlFragment' = t_14345.accumulated
            t_7123: 'Query'
            t_7123 = from_(t_14344).where(t_14348).order_by(sid_709('name'), True).limit(10)
            t_7124: 'Query'
            t_7124 = t_7123.offset(20)
            q_1789: 'Query' = t_7124
            s_1790: 'str34' = q_1789.count_sql().to_string()
            t_14355: 'bool42' = s_1790 == 'SELECT COUNT(*) FROM users WHERE active = TRUE'
            def fn_14343() -> 'str34':
                return str_cat_17392('countSql drops extras: ', s_1790)
            test_183.assert_(t_14355, fn_14343)
        finally:
            test_183.soft_fail_to_hard()
class TestCase205(TestCase53):
    def test___fullAggregationQuery__2544(self) -> None:
        'full aggregation query'
        test_184: Test = Test()
        try:
            t_14311: 'SafeIdentifier' = sid_709('orders')
            t_14314: 'SqlFragment' = col(sid_709('orders'), sid_709('status'))
            t_14315: 'SqlFragment' = count_all()
            t_14317: 'SqlFragment' = sum_col(sid_709('total'))
            t_14318: 'Query' = from_(t_14311).select_expr((t_14314, t_14315, t_14317))
            t_14319: 'SafeIdentifier' = sid_709('users')
            t_14320: 'SqlBuilder' = SqlBuilder()
            t_14320.append_safe('orders.user_id = users.id')
            t_14323: 'Query' = t_14318.inner_join(t_14319, t_14320.accumulated)
            t_14324: 'SqlBuilder' = SqlBuilder()
            t_14324.append_safe('users.active = ')
            t_14324.append_boolean(True)
            t_14330: 'Query' = t_14323.where(t_14324.accumulated).group_by(sid_709('status'))
            t_14331: 'SqlBuilder' = SqlBuilder()
            t_14331.append_safe('COUNT(*) > ')
            t_14331.append_int32(3)
            q_1792: 'Query' = t_14330.having(t_14331.accumulated).order_by(sid_709('status'), True)
            expected_1793: 'str34' = 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            t_14341: 'bool42' = q_1792.to_sql().to_string() == 'SELECT orders.status, COUNT(*), SUM(total) FROM orders INNER JOIN users ON orders.user_id = users.id WHERE users.active = TRUE GROUP BY status HAVING COUNT(*) > 3 ORDER BY status ASC'
            def fn_14310() -> 'str34':
                return 'full aggregation'
            test_184.assert_(t_14341, fn_14310)
        finally:
            test_184.soft_fail_to_hard()
class TestCase206(TestCase53):
    def test___unionSql__2548(self) -> None:
        'unionSql'
        test_185: Test = Test()
        try:
            t_14293: 'SafeIdentifier' = sid_709('users')
            t_14294: 'SqlBuilder' = SqlBuilder()
            t_14294.append_safe('role = ')
            t_14294.append_string('admin')
            t_14297: 'SqlFragment' = t_14294.accumulated
            a_1795: 'Query' = from_(t_14293).where(t_14297)
            t_14299: 'SafeIdentifier' = sid_709('users')
            t_14300: 'SqlBuilder' = SqlBuilder()
            t_14300.append_safe('role = ')
            t_14300.append_string('moderator')
            t_14303: 'SqlFragment' = t_14300.accumulated
            b_1796: 'Query' = from_(t_14299).where(t_14303)
            s_1797: 'str34' = union_sql(a_1795, b_1796).to_string()
            t_14308: 'bool42' = s_1797 == "(SELECT * FROM users WHERE role = 'admin') UNION (SELECT * FROM users WHERE role = 'moderator')"
            def fn_14292() -> 'str34':
                return str_cat_17392('unionSql: ', s_1797)
            test_185.assert_(t_14308, fn_14292)
        finally:
            test_185.soft_fail_to_hard()
class TestCase207(TestCase53):
    def test___unionAllSql__2551(self) -> None:
        'unionAllSql'
        test_186: Test = Test()
        try:
            t_14281: 'SafeIdentifier' = sid_709('users')
            t_14282: 'SafeIdentifier' = sid_709('name')
            a_1799: 'Query' = from_(t_14281).select((t_14282,))
            t_14284: 'SafeIdentifier' = sid_709('contacts')
            t_14285: 'SafeIdentifier' = sid_709('name')
            b_1800: 'Query' = from_(t_14284).select((t_14285,))
            s_1801: 'str34' = union_all_sql(a_1799, b_1800).to_string()
            t_14290: 'bool42' = s_1801 == '(SELECT name FROM users) UNION ALL (SELECT name FROM contacts)'
            def fn_14280() -> 'str34':
                return str_cat_17392('unionAllSql: ', s_1801)
            test_186.assert_(t_14290, fn_14280)
        finally:
            test_186.soft_fail_to_hard()
class TestCase208(TestCase53):
    def test___intersectSql__2552(self) -> None:
        'intersectSql'
        test_187: Test = Test()
        try:
            t_14269: 'SafeIdentifier' = sid_709('users')
            t_14270: 'SafeIdentifier' = sid_709('email')
            a_1803: 'Query' = from_(t_14269).select((t_14270,))
            t_14272: 'SafeIdentifier' = sid_709('subscribers')
            t_14273: 'SafeIdentifier' = sid_709('email')
            b_1804: 'Query' = from_(t_14272).select((t_14273,))
            s_1805: 'str34' = intersect_sql(a_1803, b_1804).to_string()
            t_14278: 'bool42' = s_1805 == '(SELECT email FROM users) INTERSECT (SELECT email FROM subscribers)'
            def fn_14268() -> 'str34':
                return str_cat_17392('intersectSql: ', s_1805)
            test_187.assert_(t_14278, fn_14268)
        finally:
            test_187.soft_fail_to_hard()
class TestCase209(TestCase53):
    def test___exceptSql__2553(self) -> None:
        'exceptSql'
        test_188: Test = Test()
        try:
            t_14257: 'SafeIdentifier' = sid_709('users')
            t_14258: 'SafeIdentifier' = sid_709('id')
            a_1807: 'Query' = from_(t_14257).select((t_14258,))
            t_14260: 'SafeIdentifier' = sid_709('banned')
            t_14261: 'SafeIdentifier' = sid_709('id')
            b_1808: 'Query' = from_(t_14260).select((t_14261,))
            s_1809: 'str34' = except_sql(a_1807, b_1808).to_string()
            t_14266: 'bool42' = s_1809 == '(SELECT id FROM users) EXCEPT (SELECT id FROM banned)'
            def fn_14256() -> 'str34':
                return str_cat_17392('exceptSql: ', s_1809)
            test_188.assert_(t_14266, fn_14256)
        finally:
            test_188.soft_fail_to_hard()
class TestCase210(TestCase53):
    def test___subqueryWithAlias__2554(self) -> None:
        'subquery with alias'
        test_189: Test = Test()
        try:
            t_14242: 'SafeIdentifier' = sid_709('orders')
            t_14243: 'SafeIdentifier' = sid_709('user_id')
            t_14244: 'Query' = from_(t_14242).select((t_14243,))
            t_14245: 'SqlBuilder' = SqlBuilder()
            t_14245.append_safe('total > ')
            t_14245.append_int32(100)
            inner_1811: 'Query' = t_14244.where(t_14245.accumulated)
            s_1812: 'str34' = subquery(inner_1811, sid_709('big_orders')).to_string()
            t_14254: 'bool42' = s_1812 == '(SELECT user_id FROM orders WHERE total > 100) AS big_orders'
            def fn_14241() -> 'str34':
                return str_cat_17392('subquery: ', s_1812)
            test_189.assert_(t_14254, fn_14241)
        finally:
            test_189.soft_fail_to_hard()
class TestCase211(TestCase53):
    def test___existsSql__2556(self) -> None:
        'existsSql'
        test_190: Test = Test()
        try:
            t_14231: 'SafeIdentifier' = sid_709('orders')
            t_14232: 'SqlBuilder' = SqlBuilder()
            t_14232.append_safe('orders.user_id = users.id')
            t_14234: 'SqlFragment' = t_14232.accumulated
            inner_1814: 'Query' = from_(t_14231).where(t_14234)
            s_1815: 'str34' = exists_sql(inner_1814).to_string()
            t_14239: 'bool42' = s_1815 == 'EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_14230() -> 'str34':
                return str_cat_17392('existsSql: ', s_1815)
            test_190.assert_(t_14239, fn_14230)
        finally:
            test_190.soft_fail_to_hard()
class TestCase212(TestCase53):
    def test___whereInSubquery__2558(self) -> None:
        'whereInSubquery'
        test_191: Test = Test()
        try:
            t_14214: 'SafeIdentifier' = sid_709('orders')
            t_14215: 'SafeIdentifier' = sid_709('user_id')
            t_14216: 'Query' = from_(t_14214).select((t_14215,))
            t_14217: 'SqlBuilder' = SqlBuilder()
            t_14217.append_safe('total > ')
            t_14217.append_int32(1000)
            sub_1817: 'Query' = t_14216.where(t_14217.accumulated)
            t_14222: 'SafeIdentifier' = sid_709('users')
            t_14223: 'SafeIdentifier' = sid_709('id')
            q_1818: 'Query' = from_(t_14222).where_in_subquery(t_14223, sub_1817)
            s_1819: 'str34' = q_1818.to_sql().to_string()
            t_14228: 'bool42' = s_1819 == 'SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 1000)'
            def fn_14213() -> 'str34':
                return str_cat_17392('whereInSubquery: ', s_1819)
            test_191.assert_(t_14228, fn_14213)
        finally:
            test_191.soft_fail_to_hard()
class TestCase213(TestCase53):
    def test___setOperationWithWhereOnEachSide__2560(self) -> None:
        'set operation with WHERE on each side'
        test_192: Test = Test()
        try:
            t_14191: 'SafeIdentifier' = sid_709('users')
            t_14192: 'SqlBuilder' = SqlBuilder()
            t_14192.append_safe('age > ')
            t_14192.append_int32(18)
            t_14195: 'SqlFragment' = t_14192.accumulated
            t_14196: 'Query' = from_(t_14191).where(t_14195)
            t_14197: 'SqlBuilder' = SqlBuilder()
            t_14197.append_safe('active = ')
            t_14197.append_boolean(True)
            a_1821: 'Query' = t_14196.where(t_14197.accumulated)
            t_14202: 'SafeIdentifier' = sid_709('users')
            t_14203: 'SqlBuilder' = SqlBuilder()
            t_14203.append_safe('role = ')
            t_14203.append_string('vip')
            t_14206: 'SqlFragment' = t_14203.accumulated
            b_1822: 'Query' = from_(t_14202).where(t_14206)
            s_1823: 'str34' = union_sql(a_1821, b_1822).to_string()
            t_14211: 'bool42' = s_1823 == "(SELECT * FROM users WHERE age > 18 AND active = TRUE) UNION (SELECT * FROM users WHERE role = 'vip')"
            def fn_14190() -> 'str34':
                return str_cat_17392('union with where: ', s_1823)
            test_192.assert_(t_14211, fn_14190)
        finally:
            test_192.soft_fail_to_hard()
class TestCase214(TestCase53):
    def test___whereInSubqueryChainedWithWhere__2564(self) -> None:
        'whereInSubquery chained with where'
        test_193: Test = Test()
        try:
            t_14174: 'SafeIdentifier' = sid_709('orders')
            t_14175: 'SafeIdentifier' = sid_709('user_id')
            sub_1825: 'Query' = from_(t_14174).select((t_14175,))
            t_14177: 'SafeIdentifier' = sid_709('users')
            t_14178: 'SqlBuilder' = SqlBuilder()
            t_14178.append_safe('active = ')
            t_14178.append_boolean(True)
            t_14181: 'SqlFragment' = t_14178.accumulated
            q_1826: 'Query' = from_(t_14177).where(t_14181).where_in_subquery(sid_709('id'), sub_1825)
            s_1827: 'str34' = q_1826.to_sql().to_string()
            t_14188: 'bool42' = s_1827 == 'SELECT * FROM users WHERE active = TRUE AND id IN (SELECT user_id FROM orders)'
            def fn_14173() -> 'str34':
                return str_cat_17392('whereInSubquery chained: ', s_1827)
            test_193.assert_(t_14188, fn_14173)
        finally:
            test_193.soft_fail_to_hard()
class TestCase215(TestCase53):
    def test___existsSqlUsedInWhere__2566(self) -> None:
        'existsSql used in where'
        test_194: Test = Test()
        try:
            t_14160: 'SafeIdentifier' = sid_709('orders')
            t_14161: 'SqlBuilder' = SqlBuilder()
            t_14161.append_safe('orders.user_id = users.id')
            t_14163: 'SqlFragment' = t_14161.accumulated
            sub_1829: 'Query' = from_(t_14160).where(t_14163)
            t_14165: 'SafeIdentifier' = sid_709('users')
            t_14166: 'SqlFragment' = exists_sql(sub_1829)
            q_1830: 'Query' = from_(t_14165).where(t_14166)
            s_1831: 'str34' = q_1830.to_sql().to_string()
            t_14171: 'bool42' = s_1831 == 'SELECT * FROM users WHERE EXISTS (SELECT * FROM orders WHERE orders.user_id = users.id)'
            def fn_14159() -> 'str34':
                return str_cat_17392('exists in where: ', s_1831)
            test_194.assert_(t_14171, fn_14159)
        finally:
            test_194.soft_fail_to_hard()
class TestCase216(TestCase53):
    def test___updateQueryBasic__2568(self) -> None:
        'UpdateQuery basic'
        test_195: Test = Test()
        try:
            t_14146: 'SafeIdentifier' = sid_709('users')
            t_14147: 'SafeIdentifier' = sid_709('name')
            t_14148: 'SqlString' = SqlString('Alice')
            t_14149: 'UpdateQuery' = update(t_14146).set(t_14147, t_14148)
            t_14150: 'SqlBuilder' = SqlBuilder()
            t_14150.append_safe('id = ')
            t_14150.append_int32(1)
            t_6945: 'SqlFragment'
            t_6945 = t_14149.where(t_14150.accumulated).to_sql()
            q_1833: 'SqlFragment' = t_6945
            t_14157: 'bool42' = q_1833.to_string() == "UPDATE users SET name = 'Alice' WHERE id = 1"
            def fn_14145() -> 'str34':
                return 'update basic'
            test_195.assert_(t_14157, fn_14145)
        finally:
            test_195.soft_fail_to_hard()
class TestCase217(TestCase53):
    def test___updateQueryMultipleSet__2570(self) -> None:
        'UpdateQuery multiple SET'
        test_196: Test = Test()
        try:
            t_14129: 'SafeIdentifier' = sid_709('users')
            t_14130: 'SafeIdentifier' = sid_709('name')
            t_14131: 'SqlString' = SqlString('Bob')
            t_14135: 'UpdateQuery' = update(t_14129).set(t_14130, t_14131).set(sid_709('age'), SqlInt32(30))
            t_14136: 'SqlBuilder' = SqlBuilder()
            t_14136.append_safe('id = ')
            t_14136.append_int32(2)
            t_6930: 'SqlFragment'
            t_6930 = t_14135.where(t_14136.accumulated).to_sql()
            q_1835: 'SqlFragment' = t_6930
            t_14143: 'bool42' = q_1835.to_string() == "UPDATE users SET name = 'Bob', age = 30 WHERE id = 2"
            def fn_14128() -> 'str34':
                return 'update multi set'
            test_196.assert_(t_14143, fn_14128)
        finally:
            test_196.soft_fail_to_hard()
class TestCase218(TestCase53):
    def test___updateQueryMultipleWhere__2572(self) -> None:
        'UpdateQuery multiple WHERE'
        test_197: Test = Test()
        try:
            t_14110: 'SafeIdentifier' = sid_709('users')
            t_14111: 'SafeIdentifier' = sid_709('active')
            t_14112: 'SqlBoolean' = SqlBoolean(False)
            t_14113: 'UpdateQuery' = update(t_14110).set(t_14111, t_14112)
            t_14114: 'SqlBuilder' = SqlBuilder()
            t_14114.append_safe('age < ')
            t_14114.append_int32(18)
            t_14118: 'UpdateQuery' = t_14113.where(t_14114.accumulated)
            t_14119: 'SqlBuilder' = SqlBuilder()
            t_14119.append_safe('role = ')
            t_14119.append_string('guest')
            t_6912: 'SqlFragment'
            t_6912 = t_14118.where(t_14119.accumulated).to_sql()
            q_1837: 'SqlFragment' = t_6912
            t_14126: 'bool42' = q_1837.to_string() == "UPDATE users SET active = FALSE WHERE age < 18 AND role = 'guest'"
            def fn_14109() -> 'str34':
                return 'update multi where'
            test_197.assert_(t_14126, fn_14109)
        finally:
            test_197.soft_fail_to_hard()
class TestCase219(TestCase53):
    def test___updateQueryOrWhere__2575(self) -> None:
        'UpdateQuery orWhere'
        test_198: Test = Test()
        try:
            t_14091: 'SafeIdentifier' = sid_709('users')
            t_14092: 'SafeIdentifier' = sid_709('status')
            t_14093: 'SqlString' = SqlString('banned')
            t_14094: 'UpdateQuery' = update(t_14091).set(t_14092, t_14093)
            t_14095: 'SqlBuilder' = SqlBuilder()
            t_14095.append_safe('spam_count > ')
            t_14095.append_int32(10)
            t_14099: 'UpdateQuery' = t_14094.where(t_14095.accumulated)
            t_14100: 'SqlBuilder' = SqlBuilder()
            t_14100.append_safe('reported = ')
            t_14100.append_boolean(True)
            t_6891: 'SqlFragment'
            t_6891 = t_14099.or_where(t_14100.accumulated).to_sql()
            q_1839: 'SqlFragment' = t_6891
            t_14107: 'bool42' = q_1839.to_string() == "UPDATE users SET status = 'banned' WHERE spam_count > 10 OR reported = TRUE"
            def fn_14090() -> 'str34':
                return 'update orWhere'
            test_198.assert_(t_14107, fn_14090)
        finally:
            test_198.soft_fail_to_hard()
class TestCase220(TestCase53):
    def test___updateQueryBubblesWithoutWhere__2578(self) -> None:
        'UpdateQuery bubbles without WHERE'
        test_199: Test = Test()
        try:
            t_14084: 'SafeIdentifier'
            t_14085: 'SafeIdentifier'
            t_14086: 'SqlInt32'
            did_bubble_1841: 'bool42'
            try:
                t_14084 = sid_709('users')
                t_14085 = sid_709('x')
                t_14086 = SqlInt32(1)
                update(t_14084).set(t_14085, t_14086).to_sql()
                did_bubble_1841 = False
            except Exception46:
                did_bubble_1841 = True
            def fn_14083() -> 'str34':
                return 'update without WHERE should bubble'
            test_199.assert_(did_bubble_1841, fn_14083)
        finally:
            test_199.soft_fail_to_hard()
class TestCase221(TestCase53):
    def test___updateQueryBubblesWithoutSet__2579(self) -> None:
        'UpdateQuery bubbles without SET'
        test_200: Test = Test()
        try:
            t_14075: 'SafeIdentifier'
            t_14076: 'SqlBuilder'
            t_14079: 'SqlFragment'
            did_bubble_1843: 'bool42'
            try:
                t_14075 = sid_709('users')
                t_14076 = SqlBuilder()
                t_14076.append_safe('id = ')
                t_14076.append_int32(1)
                t_14079 = t_14076.accumulated
                update(t_14075).where(t_14079).to_sql()
                did_bubble_1843 = False
            except Exception46:
                did_bubble_1843 = True
            def fn_14074() -> 'str34':
                return 'update without SET should bubble'
            test_200.assert_(did_bubble_1843, fn_14074)
        finally:
            test_200.soft_fail_to_hard()
class TestCase222(TestCase53):
    def test___updateQueryWithLimit__2581(self) -> None:
        'UpdateQuery with limit'
        test_201: Test = Test()
        try:
            t_14061: 'SafeIdentifier' = sid_709('users')
            t_14062: 'SafeIdentifier' = sid_709('active')
            t_14063: 'SqlBoolean' = SqlBoolean(False)
            t_14064: 'UpdateQuery' = update(t_14061).set(t_14062, t_14063)
            t_14065: 'SqlBuilder' = SqlBuilder()
            t_14065.append_safe('last_login < ')
            t_14065.append_string('2024-01-01')
            t_6854: 'UpdateQuery'
            t_6854 = t_14064.where(t_14065.accumulated).limit(100)
            t_6855: 'SqlFragment'
            t_6855 = t_6854.to_sql()
            q_1845: 'SqlFragment' = t_6855
            t_14072: 'bool42' = q_1845.to_string() == "UPDATE users SET active = FALSE WHERE last_login < '2024-01-01' LIMIT 100"
            def fn_14060() -> 'str34':
                return 'update limit'
            test_201.assert_(t_14072, fn_14060)
        finally:
            test_201.soft_fail_to_hard()
class TestCase223(TestCase53):
    def test___updateQueryEscaping__2583(self) -> None:
        'UpdateQuery escaping'
        test_202: Test = Test()
        try:
            t_14047: 'SafeIdentifier' = sid_709('users')
            t_14048: 'SafeIdentifier' = sid_709('bio')
            t_14049: 'SqlString' = SqlString("It's a test")
            t_14050: 'UpdateQuery' = update(t_14047).set(t_14048, t_14049)
            t_14051: 'SqlBuilder' = SqlBuilder()
            t_14051.append_safe('id = ')
            t_14051.append_int32(1)
            t_6839: 'SqlFragment'
            t_6839 = t_14050.where(t_14051.accumulated).to_sql()
            q_1847: 'SqlFragment' = t_6839
            t_14058: 'bool42' = q_1847.to_string() == "UPDATE users SET bio = 'It''s a test' WHERE id = 1"
            def fn_14046() -> 'str34':
                return 'update escaping'
            test_202.assert_(t_14058, fn_14046)
        finally:
            test_202.soft_fail_to_hard()
class TestCase224(TestCase53):
    def test___deleteQueryBasic__2585(self) -> None:
        'DeleteQuery basic'
        test_203: Test = Test()
        try:
            t_14036: 'SafeIdentifier' = sid_709('users')
            t_14037: 'SqlBuilder' = SqlBuilder()
            t_14037.append_safe('id = ')
            t_14037.append_int32(1)
            t_14040: 'SqlFragment' = t_14037.accumulated
            t_6824: 'SqlFragment'
            t_6824 = delete_from(t_14036).where(t_14040).to_sql()
            q_1849: 'SqlFragment' = t_6824
            t_14044: 'bool42' = q_1849.to_string() == 'DELETE FROM users WHERE id = 1'
            def fn_14035() -> 'str34':
                return 'delete basic'
            test_203.assert_(t_14044, fn_14035)
        finally:
            test_203.soft_fail_to_hard()
class TestCase225(TestCase53):
    def test___deleteQueryMultipleWhere__2587(self) -> None:
        'DeleteQuery multiple WHERE'
        test_204: Test = Test()
        try:
            t_14020: 'SafeIdentifier' = sid_709('logs')
            t_14021: 'SqlBuilder' = SqlBuilder()
            t_14021.append_safe('created_at < ')
            t_14021.append_string('2024-01-01')
            t_14024: 'SqlFragment' = t_14021.accumulated
            t_14025: 'DeleteQuery' = delete_from(t_14020).where(t_14024)
            t_14026: 'SqlBuilder' = SqlBuilder()
            t_14026.append_safe('level = ')
            t_14026.append_string('debug')
            t_6812: 'SqlFragment'
            t_6812 = t_14025.where(t_14026.accumulated).to_sql()
            q_1851: 'SqlFragment' = t_6812
            t_14033: 'bool42' = q_1851.to_string() == "DELETE FROM logs WHERE created_at < '2024-01-01' AND level = 'debug'"
            def fn_14019() -> 'str34':
                return 'delete multi where'
            test_204.assert_(t_14033, fn_14019)
        finally:
            test_204.soft_fail_to_hard()
class TestCase226(TestCase53):
    def test___deleteQueryBubblesWithoutWhere__2590(self) -> None:
        'DeleteQuery bubbles without WHERE'
        test_205: Test = Test()
        try:
            did_bubble_1853: 'bool42'
            try:
                delete_from(sid_709('users')).to_sql()
                did_bubble_1853 = False
            except Exception46:
                did_bubble_1853 = True
            def fn_14015() -> 'str34':
                return 'delete without WHERE should bubble'
            test_205.assert_(did_bubble_1853, fn_14015)
        finally:
            test_205.soft_fail_to_hard()
class TestCase227(TestCase53):
    def test___deleteQueryOrWhere__2591(self) -> None:
        'DeleteQuery orWhere'
        test_206: Test = Test()
        try:
            t_14000: 'SafeIdentifier' = sid_709('sessions')
            t_14001: 'SqlBuilder' = SqlBuilder()
            t_14001.append_safe('expired = ')
            t_14001.append_boolean(True)
            t_14004: 'SqlFragment' = t_14001.accumulated
            t_14005: 'DeleteQuery' = delete_from(t_14000).where(t_14004)
            t_14006: 'SqlBuilder' = SqlBuilder()
            t_14006.append_safe('created_at < ')
            t_14006.append_string('2023-01-01')
            t_6791: 'SqlFragment'
            t_6791 = t_14005.or_where(t_14006.accumulated).to_sql()
            q_1855: 'SqlFragment' = t_6791
            t_14013: 'bool42' = q_1855.to_string() == "DELETE FROM sessions WHERE expired = TRUE OR created_at < '2023-01-01'"
            def fn_13999() -> 'str34':
                return 'delete orWhere'
            test_206.assert_(t_14013, fn_13999)
        finally:
            test_206.soft_fail_to_hard()
class TestCase228(TestCase53):
    def test___deleteQueryWithLimit__2594(self) -> None:
        'DeleteQuery with limit'
        test_207: Test = Test()
        try:
            t_13989: 'SafeIdentifier' = sid_709('logs')
            t_13990: 'SqlBuilder' = SqlBuilder()
            t_13990.append_safe('level = ')
            t_13990.append_string('debug')
            t_13993: 'SqlFragment' = t_13990.accumulated
            t_6772: 'DeleteQuery'
            t_6772 = delete_from(t_13989).where(t_13993).limit(1000)
            t_6773: 'SqlFragment'
            t_6773 = t_6772.to_sql()
            q_1857: 'SqlFragment' = t_6773
            t_13997: 'bool42' = q_1857.to_string() == "DELETE FROM logs WHERE level = 'debug' LIMIT 1000"
            def fn_13988() -> 'str34':
                return 'delete limit'
            test_207.assert_(t_13997, fn_13988)
        finally:
            test_207.soft_fail_to_hard()
class TestCase229(TestCase53):
    def test___orderByNullsNullsFirst__2596(self) -> None:
        'orderByNulls NULLS FIRST'
        test_208: Test = Test()
        try:
            t_13979: 'SafeIdentifier' = sid_709('users')
            t_13980: 'SafeIdentifier' = sid_709('email')
            t_13981: 'NullsFirst' = NullsFirst()
            q_1859: 'Query' = from_(t_13979).order_by_nulls(t_13980, True, t_13981)
            t_13986: 'bool42' = q_1859.to_sql().to_string() == 'SELECT * FROM users ORDER BY email ASC NULLS FIRST'
            def fn_13978() -> 'str34':
                return 'nulls first'
            test_208.assert_(t_13986, fn_13978)
        finally:
            test_208.soft_fail_to_hard()
class TestCase230(TestCase53):
    def test___orderByNullsNullsLast__2597(self) -> None:
        'orderByNulls NULLS LAST'
        test_209: Test = Test()
        try:
            t_13969: 'SafeIdentifier' = sid_709('users')
            t_13970: 'SafeIdentifier' = sid_709('score')
            t_13971: 'NullsLast' = NullsLast()
            q_1861: 'Query' = from_(t_13969).order_by_nulls(t_13970, False, t_13971)
            t_13976: 'bool42' = q_1861.to_sql().to_string() == 'SELECT * FROM users ORDER BY score DESC NULLS LAST'
            def fn_13968() -> 'str34':
                return 'nulls last'
            test_209.assert_(t_13976, fn_13968)
        finally:
            test_209.soft_fail_to_hard()
class TestCase231(TestCase53):
    def test___mixedOrderByAndOrderByNulls__2598(self) -> None:
        'mixed orderBy and orderByNulls'
        test_210: Test = Test()
        try:
            t_13957: 'SafeIdentifier' = sid_709('users')
            t_13958: 'SafeIdentifier' = sid_709('name')
            q_1863: 'Query' = from_(t_13957).order_by(t_13958, True).order_by_nulls(sid_709('email'), True, NullsFirst())
            t_13966: 'bool42' = q_1863.to_sql().to_string() == 'SELECT * FROM users ORDER BY name ASC, email ASC NULLS FIRST'
            def fn_13956() -> 'str34':
                return 'mixed order'
            test_210.assert_(t_13966, fn_13956)
        finally:
            test_210.soft_fail_to_hard()
class TestCase232(TestCase53):
    def test___crossJoin__2599(self) -> None:
        'crossJoin'
        test_211: Test = Test()
        try:
            t_13948: 'SafeIdentifier' = sid_709('users')
            t_13949: 'SafeIdentifier' = sid_709('colors')
            q_1865: 'Query' = from_(t_13948).cross_join(t_13949)
            t_13954: 'bool42' = q_1865.to_sql().to_string() == 'SELECT * FROM users CROSS JOIN colors'
            def fn_13947() -> 'str34':
                return 'cross join'
            test_211.assert_(t_13954, fn_13947)
        finally:
            test_211.soft_fail_to_hard()
class TestCase233(TestCase53):
    def test___crossJoinCombinedWithOtherJoins__2600(self) -> None:
        'crossJoin combined with other joins'
        test_212: Test = Test()
        try:
            t_13934: 'SafeIdentifier' = sid_709('users')
            t_13935: 'SafeIdentifier' = sid_709('orders')
            t_13936: 'SqlBuilder' = SqlBuilder()
            t_13936.append_safe('users.id = orders.user_id')
            t_13938: 'SqlFragment' = t_13936.accumulated
            q_1867: 'Query' = from_(t_13934).inner_join(t_13935, t_13938).cross_join(sid_709('colors'))
            t_13945: 'bool42' = q_1867.to_sql().to_string() == 'SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id CROSS JOIN colors'
            def fn_13933() -> 'str34':
                return 'cross + inner join'
            test_212.assert_(t_13945, fn_13933)
        finally:
            test_212.soft_fail_to_hard()
class TestCase234(TestCase53):
    def test___lockForUpdate__2602(self) -> None:
        'lock FOR UPDATE'
        test_213: Test = Test()
        try:
            t_13920: 'SafeIdentifier' = sid_709('users')
            t_13921: 'SqlBuilder' = SqlBuilder()
            t_13921.append_safe('id = ')
            t_13921.append_int32(1)
            t_13924: 'SqlFragment' = t_13921.accumulated
            q_1869: 'Query' = from_(t_13920).where(t_13924).lock(ForUpdate())
            t_13931: 'bool42' = q_1869.to_sql().to_string() == 'SELECT * FROM users WHERE id = 1 FOR UPDATE'
            def fn_13919() -> 'str34':
                return 'for update'
            test_213.assert_(t_13931, fn_13919)
        finally:
            test_213.soft_fail_to_hard()
class TestCase235(TestCase53):
    def test___lockForShare__2604(self) -> None:
        'lock FOR SHARE'
        test_214: Test = Test()
        try:
            t_13909: 'SafeIdentifier' = sid_709('users')
            t_13910: 'SafeIdentifier' = sid_709('name')
            q_1871: 'Query' = from_(t_13909).select((t_13910,)).lock(ForShare())
            t_13917: 'bool42' = q_1871.to_sql().to_string() == 'SELECT name FROM users FOR SHARE'
            def fn_13908() -> 'str34':
                return 'for share'
            test_214.assert_(t_13917, fn_13908)
        finally:
            test_214.soft_fail_to_hard()
class TestCase236(TestCase53):
    def test___lockWithFullQuery__2605(self) -> None:
        'lock with full query'
        test_215: Test = Test()
        try:
            t_13895: 'SafeIdentifier' = sid_709('accounts')
            t_13896: 'SqlBuilder' = SqlBuilder()
            t_13896.append_safe('id = ')
            t_13896.append_int32(42)
            t_13899: 'SqlFragment' = t_13896.accumulated
            t_6696: 'Query'
            t_6696 = from_(t_13895).where(t_13899).limit(1)
            t_13902: 'Query' = t_6696.lock(ForUpdate())
            q_1873: 'Query' = t_13902
            t_13906: 'bool42' = q_1873.to_sql().to_string() == 'SELECT * FROM accounts WHERE id = 42 LIMIT 1 FOR UPDATE'
            def fn_13894() -> 'str34':
                return 'lock full query'
            test_215.assert_(t_13906, fn_13894)
        finally:
            test_215.soft_fail_to_hard()
class TestCase237(TestCase53):
    def test___queryBuilderImmutabilityTwoQueriesFromSameBase__2607(self) -> None:
        'query builder immutability - two queries from same base'
        test_216: Test = Test()
        try:
            t_13878: 'SafeIdentifier' = sid_709('users')
            t_13879: 'SqlBuilder' = SqlBuilder()
            t_13879.append_safe('active = ')
            t_13879.append_boolean(True)
            t_13882: 'SqlFragment' = t_13879.accumulated
            base_1875: 'Query' = from_(t_13878).where(t_13882)
            t_6677: 'Query'
            t_6677 = base_1875.limit(10)
            q1_1876: 'Query' = t_6677
            t_6680: 'Query'
            t_6680 = base_1875.limit(20)
            q2_1877: 'Query' = t_6680
            t_13887: 'bool42' = q1_1876.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE LIMIT 10'
            def fn_13877() -> 'str34':
                return 'q1'
            test_216.assert_(t_13887, fn_13877)
            t_13892: 'bool42' = q2_1877.to_sql().to_string() == 'SELECT * FROM users WHERE active = TRUE LIMIT 20'
            def fn_13876() -> 'str34':
                return 'q2'
            test_216.assert_(t_13892, fn_13876)
        finally:
            test_216.soft_fail_to_hard()
class TestCase238(TestCase53):
    def test___limitZeroProducesLimit0__2609(self) -> None:
        'limit zero produces LIMIT 0'
        test_217: Test = Test()
        try:
            t_6664: 'Query'
            t_6664 = from_(sid_709('users')).limit(0)
            q_1879: 'Query' = t_6664
            t_13874: 'bool42' = q_1879.to_sql().to_string() == 'SELECT * FROM users LIMIT 0'
            def fn_13869() -> 'str34':
                return 'limit 0'
            test_217.assert_(t_13874, fn_13869)
        finally:
            test_217.soft_fail_to_hard()
class TestCase239(TestCase53):
    def test___safeToSqlWithZeroDefaultLimit__2610(self) -> None:
        'safeToSql with zero defaultLimit'
        test_218: Test = Test()
        try:
            q_1881: 'Query' = from_(sid_709('users'))
            t_6658: 'SqlFragment'
            t_6658 = q_1881.safe_to_sql(0)
            s_1882: 'SqlFragment' = t_6658
            t_13867: 'bool42' = s_1882.to_string() == 'SELECT * FROM users LIMIT 0'
            def fn_13863() -> 'str34':
                return 'safeToSql 0'
            test_218.assert_(t_13867, fn_13863)
        finally:
            test_218.soft_fail_to_hard()
class TestCase240(TestCase53):
    def test___updateQueryLimitBubblesOnNegative__2611(self) -> None:
        'UpdateQuery limit bubbles on negative'
        test_219: Test = Test()
        try:
            t_13852: 'SafeIdentifier'
            t_13853: 'SafeIdentifier'
            t_13854: 'SqlString'
            t_13855: 'UpdateQuery'
            t_13856: 'SqlBuilder'
            did_bubble_1884: 'bool42'
            try:
                t_13852 = sid_709('users')
                t_13853 = sid_709('name')
                t_13854 = SqlString('x')
                t_13855 = update(t_13852).set(t_13853, t_13854)
                t_13856 = SqlBuilder()
                t_13856.append_safe('id = ')
                t_13856.append_int32(1)
                t_13855.where(t_13856.accumulated).limit(-1)
                did_bubble_1884 = False
            except Exception46:
                did_bubble_1884 = True
            def fn_13851() -> 'str34':
                return 'UpdateQuery negative limit should bubble'
            test_219.assert_(did_bubble_1884, fn_13851)
        finally:
            test_219.soft_fail_to_hard()
class TestCase241(TestCase53):
    def test___deleteQueryLimitBubblesOnNegative__2613(self) -> None:
        'DeleteQuery limit bubbles on negative'
        test_220: Test = Test()
        try:
            t_13843: 'SafeIdentifier'
            t_13844: 'SqlBuilder'
            t_13847: 'SqlFragment'
            did_bubble_1886: 'bool42'
            try:
                t_13843 = sid_709('users')
                t_13844 = SqlBuilder()
                t_13844.append_safe('id = ')
                t_13844.append_int32(1)
                t_13847 = t_13844.accumulated
                delete_from(t_13843).where(t_13847).limit(-1)
                did_bubble_1886 = False
            except Exception46:
                did_bubble_1886 = True
            def fn_13842() -> 'str34':
                return 'DeleteQuery negative limit should bubble'
            test_220.assert_(did_bubble_1886, fn_13842)
        finally:
            test_220.soft_fail_to_hard()
class TestCase242(TestCase53):
    def test___updateQueryImmutabilityTwoFromSameBase__2615(self) -> None:
        'UpdateQuery immutability - two from same base'
        test_221: Test = Test()
        try:
            t_13812: 'SafeIdentifier' = sid_709('users')
            t_13813: 'SafeIdentifier' = sid_709('name')
            t_13814: 'SqlString' = SqlString('Alice')
            t_13815: 'UpdateQuery' = update(t_13812).set(t_13813, t_13814)
            t_13816: 'SqlBuilder' = SqlBuilder()
            t_13816.append_safe('id = ')
            t_13816.append_int32(1)
            base_1888: 'UpdateQuery' = t_13815.where(t_13816.accumulated)
            q1_1889: 'UpdateQuery' = base_1888.set(sid_709('age'), SqlInt32(25))
            q2_1890: 'UpdateQuery' = base_1888.set(sid_709('age'), SqlInt32(30))
            t_6618: 'SqlFragment'
            t_6618 = q1_1889.to_sql()
            t_6619: 'SqlFragment' = t_6618
            s1_1891: 'str34' = t_6619.to_string()
            t_6621: 'SqlFragment'
            t_6621 = q2_1890.to_sql()
            t_6622: 'SqlFragment' = t_6621
            s2_1892: 'str34' = t_6622.to_string()
            t_13830: 'bool42' = s1_1891.find('25') >= 0
            def fn_13811() -> 'str34':
                return str_cat_17392('q1 should have 25: ', s1_1891)
            test_221.assert_(t_13830, fn_13811)
            t_13834: 'bool42' = s2_1892.find('30') >= 0
            def fn_13810() -> 'str34':
                return str_cat_17392('q2 should have 30: ', s2_1892)
            test_221.assert_(t_13834, fn_13810)
            t_13840: 'bool42' = not s1_1891.find('30') >= 0
            def fn_13809() -> 'str34':
                return str_cat_17392('q1 should NOT have 30: ', s1_1891)
            test_221.assert_(t_13840, fn_13809)
        finally:
            test_221.soft_fail_to_hard()
class TestCase243(TestCase53):
    def test___deleteQueryImmutability__2617(self) -> None:
        'DeleteQuery immutability'
        test_222: Test = Test()
        try:
            t_13778: 'SafeIdentifier' = sid_709('users')
            t_13779: 'SqlBuilder' = SqlBuilder()
            t_13779.append_safe('active = ')
            t_13779.append_boolean(False)
            t_13782: 'SqlFragment' = t_13779.accumulated
            base_1894: 'DeleteQuery' = delete_from(t_13778).where(t_13782)
            t_13784: 'SqlBuilder' = SqlBuilder()
            t_13784.append_safe('age < ')
            t_13784.append_int32(18)
            q1_1895: 'DeleteQuery' = base_1894.where(t_13784.accumulated)
            t_13789: 'SqlBuilder' = SqlBuilder()
            t_13789.append_safe('age > ')
            t_13789.append_int32(65)
            q2_1896: 'DeleteQuery' = base_1894.where(t_13789.accumulated)
            t_6584: 'SqlFragment'
            t_6584 = q1_1895.to_sql()
            t_6585: 'SqlFragment' = t_6584
            s1_1897: 'str34' = t_6585.to_string()
            t_6587: 'SqlFragment'
            t_6587 = q2_1896.to_sql()
            t_6588: 'SqlFragment' = t_6587
            s2_1898: 'str34' = t_6588.to_string()
            t_13797: 'bool42' = s1_1897.find('age < 18') >= 0
            def fn_13777() -> 'str34':
                return str_cat_17392('q1: ', s1_1897)
            test_222.assert_(t_13797, fn_13777)
            t_13801: 'bool42' = s2_1898.find('age > 65') >= 0
            def fn_13776() -> 'str34':
                return str_cat_17392('q2: ', s2_1898)
            test_222.assert_(t_13801, fn_13776)
            t_13807: 'bool42' = not s1_1897.find('age > 65') >= 0
            def fn_13775() -> 'str34':
                return str_cat_17392('q1 should not have q2 condition: ', s1_1897)
            test_222.assert_(t_13807, fn_13775)
        finally:
            test_222.soft_fail_to_hard()
class TestCase244(TestCase53):
    def test___safeIdentifierAcceptsValidNames__2621(self) -> None:
        'safeIdentifier accepts valid names'
        test_229: Test = Test()
        try:
            t_6561: 'SafeIdentifier'
            t_6561 = safe_identifier('user_name')
            id_1946: 'SafeIdentifier' = t_6561
            t_13773: 'bool42' = id_1946.sql_value == 'user_name'
            def fn_13770() -> 'str34':
                return 'value should round-trip'
            test_229.assert_(t_13773, fn_13770)
        finally:
            test_229.soft_fail_to_hard()
class TestCase245(TestCase53):
    def test___safeIdentifierRejectsEmptyString__2622(self) -> None:
        'safeIdentifier rejects empty string'
        test_230: Test = Test()
        try:
            did_bubble_1948: 'bool42'
            try:
                safe_identifier('')
                did_bubble_1948 = False
            except Exception46:
                did_bubble_1948 = True
            def fn_13767() -> 'str34':
                return 'empty string should bubble'
            test_230.assert_(did_bubble_1948, fn_13767)
        finally:
            test_230.soft_fail_to_hard()
class TestCase246(TestCase53):
    def test___safeIdentifierRejectsLeadingDigit__2623(self) -> None:
        'safeIdentifier rejects leading digit'
        test_231: Test = Test()
        try:
            did_bubble_1950: 'bool42'
            try:
                safe_identifier('1col')
                did_bubble_1950 = False
            except Exception46:
                did_bubble_1950 = True
            def fn_13764() -> 'str34':
                return 'leading digit should bubble'
            test_231.assert_(did_bubble_1950, fn_13764)
        finally:
            test_231.soft_fail_to_hard()
class TestCase247(TestCase53):
    def test___safeIdentifierRejectsSqlMetacharacters__2624(self) -> None:
        'safeIdentifier rejects SQL metacharacters'
        test_232: Test = Test()
        try:
            cases_1952: 'Sequence38[str34]' = ('name); DROP TABLE', "col'", 'a b', 'a-b', 'a.b', 'a;b')
            def fn_13761(c_1953: 'str34') -> 'None':
                did_bubble_1954: 'bool42'
                try:
                    safe_identifier(c_1953)
                    did_bubble_1954 = False
                except Exception46:
                    did_bubble_1954 = True
                def fn_13758() -> 'str34':
                    return str_cat_17392('should reject: ', c_1953)
                test_232.assert_(did_bubble_1954, fn_13758)
            list_for_each_17386(cases_1952, fn_13761)
        finally:
            test_232.soft_fail_to_hard()
class TestCase248(TestCase53):
    def test___tableDefFieldLookupFound__2625(self) -> None:
        'TableDef field lookup - found'
        test_233: Test = Test()
        try:
            t_6538: 'SafeIdentifier'
            t_6538 = safe_identifier('users')
            t_6539: 'SafeIdentifier' = t_6538
            t_6540: 'SafeIdentifier'
            t_6540 = safe_identifier('name')
            t_6541: 'SafeIdentifier' = t_6540
            t_13748: 'StringField' = StringField()
            t_13749: 'FieldDef' = FieldDef(t_6541, t_13748, False, None, False)
            t_6544: 'SafeIdentifier'
            t_6544 = safe_identifier('age')
            t_6545: 'SafeIdentifier' = t_6544
            t_13750: 'IntField' = IntField()
            t_13751: 'FieldDef' = FieldDef(t_6545, t_13750, False, None, False)
            td_1956: 'TableDef' = TableDef(t_6539, (t_13749, t_13751), None)
            t_6549: 'FieldDef'
            t_6549 = td_1956.field('age')
            f_1957: 'FieldDef' = t_6549
            t_13756: 'bool42' = f_1957.name.sql_value == 'age'
            def fn_13747() -> 'str34':
                return 'should find age field'
            test_233.assert_(t_13756, fn_13747)
        finally:
            test_233.soft_fail_to_hard()
class TestCase249(TestCase53):
    def test___tableDefFieldLookupNotFoundBubbles__2626(self) -> None:
        'TableDef field lookup - not found bubbles'
        test_234: Test = Test()
        try:
            t_6529: 'SafeIdentifier'
            t_6529 = safe_identifier('users')
            t_6530: 'SafeIdentifier' = t_6529
            t_6531: 'SafeIdentifier'
            t_6531 = safe_identifier('name')
            t_6532: 'SafeIdentifier' = t_6531
            t_13742: 'StringField' = StringField()
            t_13743: 'FieldDef' = FieldDef(t_6532, t_13742, False, None, False)
            td_1959: 'TableDef' = TableDef(t_6530, (t_13743,), None)
            did_bubble_1960: 'bool42'
            try:
                td_1959.field('nonexistent')
                did_bubble_1960 = False
            except Exception46:
                did_bubble_1960 = True
            def fn_13741() -> 'str34':
                return 'unknown field should bubble'
            test_234.assert_(did_bubble_1960, fn_13741)
        finally:
            test_234.soft_fail_to_hard()
class TestCase250(TestCase53):
    def test___fieldDefNullableFlag__2627(self) -> None:
        'FieldDef nullable flag'
        test_235: Test = Test()
        try:
            t_6517: 'SafeIdentifier'
            t_6517 = safe_identifier('email')
            t_6518: 'SafeIdentifier' = t_6517
            t_13730: 'StringField' = StringField()
            required_1962: 'FieldDef' = FieldDef(t_6518, t_13730, False, None, False)
            t_6521: 'SafeIdentifier'
            t_6521 = safe_identifier('bio')
            t_6522: 'SafeIdentifier' = t_6521
            t_13732: 'StringField' = StringField()
            optional_1963: 'FieldDef' = FieldDef(t_6522, t_13732, True, None, False)
            t_13736: 'bool42' = not required_1962.nullable
            def fn_13729() -> 'str34':
                return 'required field should not be nullable'
            test_235.assert_(t_13736, fn_13729)
            t_13738: 'bool42' = optional_1963.nullable
            def fn_13728() -> 'str34':
                return 'optional field should be nullable'
            test_235.assert_(t_13738, fn_13728)
        finally:
            test_235.soft_fail_to_hard()
class TestCase251(TestCase53):
    def test___pkNameDefaultsToIdWhenPrimaryKeyIsNull__2628(self) -> None:
        'pkName defaults to id when primaryKey is null'
        test_236: Test = Test()
        try:
            t_6508: 'SafeIdentifier'
            t_6508 = safe_identifier('users')
            t_6509: 'SafeIdentifier' = t_6508
            t_6510: 'SafeIdentifier'
            t_6510 = safe_identifier('name')
            t_6511: 'SafeIdentifier' = t_6510
            t_13721: 'StringField' = StringField()
            t_13722: 'FieldDef' = FieldDef(t_6511, t_13721, False, None, False)
            td_1965: 'TableDef' = TableDef(t_6509, (t_13722,), None)
            t_13726: 'bool42' = td_1965.pk_name() == 'id'
            def fn_13720() -> 'str34':
                return 'default pk should be id'
            test_236.assert_(t_13726, fn_13720)
        finally:
            test_236.soft_fail_to_hard()
class TestCase252(TestCase53):
    def test___pkNameReturnsCustomPrimaryKey__2629(self) -> None:
        'pkName returns custom primary key'
        test_237: Test = Test()
        try:
            t_6496: 'SafeIdentifier'
            t_6496 = safe_identifier('users')
            t_6497: 'SafeIdentifier' = t_6496
            t_6498: 'SafeIdentifier'
            t_6498 = safe_identifier('user_id')
            t_6499: 'SafeIdentifier' = t_6498
            t_13713: 'IntField' = IntField()
            t_6504: 'Sequence38[FieldDef]' = (FieldDef(t_6499, t_13713, False, None, False),)
            t_6502: 'SafeIdentifier'
            t_6502 = safe_identifier('user_id')
            t_6503: 'SafeIdentifier' = t_6502
            td_1967: 'TableDef' = TableDef(t_6497, t_6504, t_6503)
            t_13718: 'bool42' = td_1967.pk_name() == 'user_id'
            def fn_13712() -> 'str34':
                return 'custom pk should be user_id'
            test_237.assert_(t_13718, fn_13712)
        finally:
            test_237.soft_fail_to_hard()
class TestCase253(TestCase53):
    def test___timestampsReturnsTwoDateFieldDefs__2630(self) -> None:
        'timestamps returns two DateField defs'
        test_238: Test = Test()
        try:
            t_6472: 'Sequence38[FieldDef]'
            t_6472 = timestamps()
            ts_1969: 'Sequence38[FieldDef]' = t_6472
            t_13680: 'bool42' = len_17389(ts_1969) == 2
            def fn_13677() -> 'str34':
                return 'should return 2 fields'
            test_238.assert_(t_13680, fn_13677)
            t_13686: 'bool42' = list_get_17397(ts_1969, 0).name.sql_value == 'inserted_at'
            def fn_13676() -> 'str34':
                return 'first should be inserted_at'
            test_238.assert_(t_13686, fn_13676)
            t_13692: 'bool42' = list_get_17397(ts_1969, 1).name.sql_value == 'updated_at'
            def fn_13675() -> 'str34':
                return 'second should be updated_at'
            test_238.assert_(t_13692, fn_13675)
            t_13695: 'bool42' = list_get_17397(ts_1969, 0).nullable
            def fn_13674() -> 'str34':
                return 'inserted_at should be nullable'
            test_238.assert_(t_13695, fn_13674)
            t_13699: 'bool42' = list_get_17397(ts_1969, 1).nullable
            def fn_13673() -> 'str34':
                return 'updated_at should be nullable'
            test_238.assert_(t_13699, fn_13673)
            t_13705: 'bool42' = not list_get_17397(ts_1969, 0).default_value is None
            def fn_13672() -> 'str34':
                return 'inserted_at should have default'
            test_238.assert_(t_13705, fn_13672)
            t_13710: 'bool42' = not list_get_17397(ts_1969, 1).default_value is None
            def fn_13671() -> 'str34':
                return 'updated_at should have default'
            test_238.assert_(t_13710, fn_13671)
        finally:
            test_238.soft_fail_to_hard()
class TestCase254(TestCase53):
    def test___fieldDefDefaultValueField__2631(self) -> None:
        'FieldDef defaultValue field'
        test_239: Test = Test()
        try:
            t_6459: 'SafeIdentifier'
            t_6459 = safe_identifier('status')
            t_6460: 'SafeIdentifier' = t_6459
            t_13658: 'StringField' = StringField()
            t_13659: 'SqlDefault' = SqlDefault()
            with_default_1971: 'FieldDef' = FieldDef(t_6460, t_13658, False, t_13659, False)
            t_6464: 'SafeIdentifier'
            t_6464 = safe_identifier('name')
            t_6465: 'SafeIdentifier' = t_6464
            t_13661: 'StringField' = StringField()
            without_default_1972: 'FieldDef' = FieldDef(t_6465, t_13661, False, None, False)
            t_13665: 'bool42' = not with_default_1971.default_value is None
            def fn_13657() -> 'str34':
                return 'should have default'
            test_239.assert_(t_13665, fn_13657)
            t_13669: 'bool42' = without_default_1972.default_value is None
            def fn_13656() -> 'str34':
                return 'should not have default'
            test_239.assert_(t_13669, fn_13656)
        finally:
            test_239.soft_fail_to_hard()
class TestCase255(TestCase53):
    def test___fieldDefVirtualFlag__2632(self) -> None:
        'FieldDef virtual flag'
        test_240: Test = Test()
        try:
            t_6447: 'SafeIdentifier'
            t_6447 = safe_identifier('name')
            t_6448: 'SafeIdentifier' = t_6447
            t_13645: 'StringField' = StringField()
            normal_1974: 'FieldDef' = FieldDef(t_6448, t_13645, False, None, False)
            t_6451: 'SafeIdentifier'
            t_6451 = safe_identifier('full_name')
            t_6452: 'SafeIdentifier' = t_6451
            t_13647: 'StringField' = StringField()
            virt_1975: 'FieldDef' = FieldDef(t_6452, t_13647, True, None, True)
            t_13651: 'bool42' = not normal_1974.virtual
            def fn_13644() -> 'str34':
                return 'normal field should not be virtual'
            test_240.assert_(t_13651, fn_13644)
            t_13653: 'bool42' = virt_1975.virtual
            def fn_13643() -> 'str34':
                return 'virtual field should be virtual'
            test_240.assert_(t_13653, fn_13643)
        finally:
            test_240.soft_fail_to_hard()
class TestCase256(TestCase53):
    def test___safeIdentifierAcceptsSingleCharacterNames__2633(self) -> None:
        'safeIdentifier accepts single character names'
        test_241: Test = Test()
        try:
            t_6439: 'SafeIdentifier'
            t_6439 = safe_identifier('a')
            a_1977: 'SafeIdentifier' = t_6439
            t_13637: 'bool42' = a_1977.sql_value == 'a'
            def fn_13634() -> 'str34':
                return 'single letter should work'
            test_241.assert_(t_13637, fn_13634)
            t_6443: 'SafeIdentifier'
            t_6443 = safe_identifier('_')
            u_1978: 'SafeIdentifier' = t_6443
            t_13641: 'bool42' = u_1978.sql_value == '_'
            def fn_13633() -> 'str34':
                return 'single underscore should work'
            test_241.assert_(t_13641, fn_13633)
        finally:
            test_241.soft_fail_to_hard()
class TestCase257(TestCase53):
    def test___safeIdentifierAcceptsAllUnderscoreNames__2634(self) -> None:
        'safeIdentifier accepts all-underscore names'
        test_242: Test = Test()
        try:
            t_6435: 'SafeIdentifier'
            t_6435 = safe_identifier('___')
            id_1980: 'SafeIdentifier' = t_6435
            t_13631: 'bool42' = id_1980.sql_value == '___'
            def fn_13628() -> 'str34':
                return 'all underscores should work'
            test_242.assert_(t_13631, fn_13628)
        finally:
            test_242.soft_fail_to_hard()
class TestCase258(TestCase53):
    def test___tableDefWithEmptyFieldList__2635(self) -> None:
        'TableDef with empty field list'
        test_243: Test = Test()
        try:
            t_6430: 'SafeIdentifier'
            t_6430 = safe_identifier('empty')
            t_6431: 'SafeIdentifier' = t_6430
            tbl_1982: 'TableDef' = TableDef(t_6431, (), None)
            did_bubble_1983: 'bool42'
            try:
                tbl_1982.field('anything')
                did_bubble_1983 = False
            except Exception46:
                did_bubble_1983 = True
            def fn_13624() -> 'str34':
                return 'field lookup on empty table should bubble'
            test_243.assert_(did_bubble_1983, fn_13624)
        finally:
            test_243.soft_fail_to_hard()
class TestCase259(TestCase53):
    def test___stringEscaping__2636(self) -> None:
        'string escaping'
        test_247: Test = Test()
        try:
            def build_2113(name_2115: 'str34') -> 'str34':
                t_13606: 'SqlBuilder' = SqlBuilder()
                t_13606.append_safe('select * from hi where name = ')
                t_13606.append_string(name_2115)
                return t_13606.accumulated.to_string()
            def build_wrong_2114(name_2117: 'str34') -> 'str34':
                return str_cat_17392("select * from hi where name = '", name_2117, "'")
            actual_2638: 'str34' = build_2113('world')
            t_13616: 'bool42' = actual_2638 == "select * from hi where name = 'world'"
            def fn_13613() -> 'str34':
                return str_cat_17392('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_2638, ')')
            test_247.assert_(t_13616, fn_13613)
            bobby_tables_2119: 'str34' = "Robert'); drop table hi;--"
            actual_2640: 'str34' = build_2113("Robert'); drop table hi;--")
            t_13620: 'bool42' = actual_2640 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_13612() -> 'str34':
                return str_cat_17392('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_2640, ')')
            test_247.assert_(t_13620, fn_13612)
            def fn_13611() -> 'str34':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_247.assert_(True, fn_13611)
        finally:
            test_247.soft_fail_to_hard()
class TestCase260(TestCase53):
    def test___stringEdgeCases__2644(self) -> None:
        'string edge cases'
        test_248: Test = Test()
        try:
            t_13574: 'SqlBuilder' = SqlBuilder()
            t_13574.append_safe('v = ')
            t_13574.append_string('')
            actual_2645: 'str34' = t_13574.accumulated.to_string()
            t_13580: 'bool42' = actual_2645 == "v = ''"
            def fn_13573() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_2645, ')')
            test_248.assert_(t_13580, fn_13573)
            t_13582: 'SqlBuilder' = SqlBuilder()
            t_13582.append_safe('v = ')
            t_13582.append_string("a''b")
            actual_2648: 'str34' = t_13582.accumulated.to_string()
            t_13588: 'bool42' = actual_2648 == "v = 'a''''b'"
            def fn_13572() -> 'str34':
                return str_cat_17392("expected stringExpr(`-work//src/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_2648, ')')
            test_248.assert_(t_13588, fn_13572)
            t_13590: 'SqlBuilder' = SqlBuilder()
            t_13590.append_safe('v = ')
            t_13590.append_string('Hello \u4e16\u754c')
            actual_2651: 'str34' = t_13590.accumulated.to_string()
            t_13596: 'bool42' = actual_2651 == "v = 'Hello \u4e16\u754c'"
            def fn_13571() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_2651, ')')
            test_248.assert_(t_13596, fn_13571)
            t_13598: 'SqlBuilder' = SqlBuilder()
            t_13598.append_safe('v = ')
            t_13598.append_string('Line1\nLine2')
            actual_2654: 'str34' = t_13598.accumulated.to_string()
            t_13604: 'bool42' = actual_2654 == "v = 'Line1\nLine2'"
            def fn_13570() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_2654, ')')
            test_248.assert_(t_13604, fn_13570)
        finally:
            test_248.soft_fail_to_hard()
class TestCase261(TestCase53):
    def test___numbersAndBooleans__2657(self) -> None:
        'numbers and booleans'
        test_249: Test = Test()
        try:
            t_13545: 'SqlBuilder' = SqlBuilder()
            t_13545.append_safe('select ')
            t_13545.append_int32(42)
            t_13545.append_safe(', ')
            t_13545.append_int64(43)
            t_13545.append_safe(', ')
            t_13545.append_float64(19.99)
            t_13545.append_safe(', ')
            t_13545.append_boolean(True)
            t_13545.append_safe(', ')
            t_13545.append_boolean(False)
            actual_2658: 'str34' = t_13545.accumulated.to_string()
            t_13559: 'bool42' = actual_2658 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_13544() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_2658, ')')
            test_249.assert_(t_13559, fn_13544)
            t_6375: 'date33'
            t_6375 = date_17423(2024, 12, 25)
            date_2122: 'date33' = t_6375
            t_13561: 'SqlBuilder' = SqlBuilder()
            t_13561.append_safe('insert into t values (')
            t_13561.append_date(date_2122)
            t_13561.append_safe(')')
            actual_2661: 'str34' = t_13561.accumulated.to_string()
            t_13568: 'bool42' = actual_2661 == "insert into t values ('2024-12-25')"
            def fn_13543() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_2661, ')')
            test_249.assert_(t_13568, fn_13543)
        finally:
            test_249.soft_fail_to_hard()
class TestCase262(TestCase53):
    def test___lists__2664(self) -> None:
        'lists'
        test_250: Test = Test()
        try:
            t_13489: 'SqlBuilder' = SqlBuilder()
            t_13489.append_safe('v IN (')
            t_13489.append_string_list(('a', 'b', "c'd"))
            t_13489.append_safe(')')
            actual_2665: 'str34' = t_13489.accumulated.to_string()
            t_13496: 'bool42' = actual_2665 == "v IN ('a', 'b', 'c''d')"
            def fn_13488() -> 'str34':
                return str_cat_17392("expected stringExpr(`-work//src/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_2665, ')')
            test_250.assert_(t_13496, fn_13488)
            t_13498: 'SqlBuilder' = SqlBuilder()
            t_13498.append_safe('v IN (')
            t_13498.append_int32_list((1, 2, 3))
            t_13498.append_safe(')')
            actual_2668: 'str34' = t_13498.accumulated.to_string()
            t_13505: 'bool42' = actual_2668 == 'v IN (1, 2, 3)'
            def fn_13487() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_2668, ')')
            test_250.assert_(t_13505, fn_13487)
            t_13507: 'SqlBuilder' = SqlBuilder()
            t_13507.append_safe('v IN (')
            t_13507.append_int64_list((1, 2))
            t_13507.append_safe(')')
            actual_2671: 'str34' = t_13507.accumulated.to_string()
            t_13514: 'bool42' = actual_2671 == 'v IN (1, 2)'
            def fn_13486() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_2671, ')')
            test_250.assert_(t_13514, fn_13486)
            t_13516: 'SqlBuilder' = SqlBuilder()
            t_13516.append_safe('v IN (')
            t_13516.append_float64_list((1.0, 2.0))
            t_13516.append_safe(')')
            actual_2674: 'str34' = t_13516.accumulated.to_string()
            t_13523: 'bool42' = actual_2674 == 'v IN (1.0, 2.0)'
            def fn_13485() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_2674, ')')
            test_250.assert_(t_13523, fn_13485)
            t_13525: 'SqlBuilder' = SqlBuilder()
            t_13525.append_safe('v IN (')
            t_13525.append_boolean_list((True, False))
            t_13525.append_safe(')')
            actual_2677: 'str34' = t_13525.accumulated.to_string()
            t_13532: 'bool42' = actual_2677 == 'v IN (TRUE, FALSE)'
            def fn_13484() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_2677, ')')
            test_250.assert_(t_13532, fn_13484)
            t_6347: 'date33'
            t_6347 = date_17423(2024, 1, 1)
            t_6348: 'date33' = t_6347
            t_6349: 'date33'
            t_6349 = date_17423(2024, 12, 25)
            t_6350: 'date33' = t_6349
            dates_2124: 'Sequence38[date33]' = (t_6348, t_6350)
            t_13534: 'SqlBuilder' = SqlBuilder()
            t_13534.append_safe('v IN (')
            t_13534.append_date_list(dates_2124)
            t_13534.append_safe(')')
            actual_2680: 'str34' = t_13534.accumulated.to_string()
            t_13541: 'bool42' = actual_2680 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_13483() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_2680, ')')
            test_250.assert_(t_13541, fn_13483)
        finally:
            test_250.soft_fail_to_hard()
class TestCase263(TestCase53):
    def test___sqlFloat64_naNRendersAsNull__2683(self) -> None:
        'SqlFloat64 NaN renders as NULL'
        test_251: Test = Test()
        try:
            nan_2126: 'float36'
            nan_2126 = 0.0 / 0.0
            t_13475: 'SqlBuilder' = SqlBuilder()
            t_13475.append_safe('v = ')
            t_13475.append_float64(nan_2126)
            actual_2684: 'str34' = t_13475.accumulated.to_string()
            t_13481: 'bool42' = actual_2684 == 'v = NULL'
            def fn_13474() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, nan).toString() == (', 'v = NULL', ') not (', actual_2684, ')')
            test_251.assert_(t_13481, fn_13474)
        finally:
            test_251.soft_fail_to_hard()
class TestCase264(TestCase53):
    def test___sqlFloat64_infinityRendersAsNull__2687(self) -> None:
        'SqlFloat64 Infinity renders as NULL'
        test_252: Test = Test()
        try:
            inf_2128: 'float36'
            inf_2128 = 1.0 / 0.0
            t_13466: 'SqlBuilder' = SqlBuilder()
            t_13466.append_safe('v = ')
            t_13466.append_float64(inf_2128)
            actual_2688: 'str34' = t_13466.accumulated.to_string()
            t_13472: 'bool42' = actual_2688 == 'v = NULL'
            def fn_13465() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, inf).toString() == (', 'v = NULL', ') not (', actual_2688, ')')
            test_252.assert_(t_13472, fn_13465)
        finally:
            test_252.soft_fail_to_hard()
class TestCase265(TestCase53):
    def test___sqlFloat64_negativeInfinityRendersAsNull__2691(self) -> None:
        'SqlFloat64 negative Infinity renders as NULL'
        test_253: Test = Test()
        try:
            ninf_2130: 'float36'
            ninf_2130 = -1.0 / 0.0
            t_13457: 'SqlBuilder' = SqlBuilder()
            t_13457.append_safe('v = ')
            t_13457.append_float64(ninf_2130)
            actual_2692: 'str34' = t_13457.accumulated.to_string()
            t_13463: 'bool42' = actual_2692 == 'v = NULL'
            def fn_13456() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, ninf).toString() == (', 'v = NULL', ') not (', actual_2692, ')')
            test_253.assert_(t_13463, fn_13456)
        finally:
            test_253.soft_fail_to_hard()
class TestCase266(TestCase53):
    def test___sqlFloat64_normalValuesStillWork__2695(self) -> None:
        'SqlFloat64 normal values still work'
        test_254: Test = Test()
        try:
            t_13432: 'SqlBuilder' = SqlBuilder()
            t_13432.append_safe('v = ')
            t_13432.append_float64(3.14)
            actual_2696: 'str34' = t_13432.accumulated.to_string()
            t_13438: 'bool42' = actual_2696 == 'v = 3.14'
            def fn_13431() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 3.14).toString() == (', 'v = 3.14', ') not (', actual_2696, ')')
            test_254.assert_(t_13438, fn_13431)
            t_13440: 'SqlBuilder' = SqlBuilder()
            t_13440.append_safe('v = ')
            t_13440.append_float64(0.0)
            actual_2699: 'str34' = t_13440.accumulated.to_string()
            t_13446: 'bool42' = actual_2699 == 'v = 0.0'
            def fn_13430() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, 0.0).toString() == (', 'v = 0.0', ') not (', actual_2699, ')')
            test_254.assert_(t_13446, fn_13430)
            t_13448: 'SqlBuilder' = SqlBuilder()
            t_13448.append_safe('v = ')
            t_13448.append_float64(-42.5)
            actual_2702: 'str34' = t_13448.accumulated.to_string()
            t_13454: 'bool42' = actual_2702 == 'v = -42.5'
            def fn_13429() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, -42.5).toString() == (', 'v = -42.5', ') not (', actual_2702, ')')
            test_254.assert_(t_13454, fn_13429)
        finally:
            test_254.soft_fail_to_hard()
class TestCase267(TestCase53):
    def test___sqlDateRendersWithQuotes__2705(self) -> None:
        'SqlDate renders with quotes'
        test_255: Test = Test()
        try:
            t_6243: 'date33'
            t_6243 = date_17423(2024, 6, 15)
            d_2133: 'date33' = t_6243
            t_13421: 'SqlBuilder' = SqlBuilder()
            t_13421.append_safe('v = ')
            t_13421.append_date(d_2133)
            actual_2706: 'str34' = t_13421.accumulated.to_string()
            t_13427: 'bool42' = actual_2706 == "v = '2024-06-15'"
            def fn_13420() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "v = ", \\interpolate, d).toString() == (', "v = '2024-06-15'", ') not (', actual_2706, ')')
            test_255.assert_(t_13427, fn_13420)
        finally:
            test_255.soft_fail_to_hard()
class TestCase268(TestCase53):
    def test___nesting__2709(self) -> None:
        'nesting'
        test_256: Test = Test()
        try:
            name_2135: 'str34' = 'Someone'
            t_13389: 'SqlBuilder' = SqlBuilder()
            t_13389.append_safe('where p.last_name = ')
            t_13389.append_string('Someone')
            condition_2136: 'SqlFragment' = t_13389.accumulated
            t_13393: 'SqlBuilder' = SqlBuilder()
            t_13393.append_safe('select p.id from person p ')
            t_13393.append_fragment(condition_2136)
            actual_2711: 'str34' = t_13393.accumulated.to_string()
            t_13399: 'bool42' = actual_2711 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_13388() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2711, ')')
            test_256.assert_(t_13399, fn_13388)
            t_13401: 'SqlBuilder' = SqlBuilder()
            t_13401.append_safe('select p.id from person p ')
            t_13401.append_part(condition_2136.to_source())
            actual_2714: 'str34' = t_13401.accumulated.to_string()
            t_13408: 'bool42' = actual_2714 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_13387() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_2714, ')')
            test_256.assert_(t_13408, fn_13387)
            parts_2137: 'Sequence38[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_13412: 'SqlBuilder' = SqlBuilder()
            t_13412.append_safe('select ')
            t_13412.append_part_list(parts_2137)
            actual_2717: 'str34' = t_13412.accumulated.to_string()
            t_13418: 'bool42' = actual_2717 == "select 'a''b', 3"
            def fn_13386() -> 'str34':
                return str_cat_17392('expected stringExpr(`-work//src/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_2717, ')')
            test_256.assert_(t_13418, fn_13386)
        finally:
            test_256.soft_fail_to_hard()
class TestCase269(TestCase53):
    def test___sqlInt32_negativeAndZeroValues__2720(self) -> None:
        'SqlInt32 negative and zero values'
        test_257: Test = Test()
        try:
            t_13370: 'SqlBuilder' = SqlBuilder()
            t_13370.append_safe('v = ')
            t_13370.append_int32(-42)
            t_13376: 'bool42' = t_13370.accumulated.to_string() == 'v = -42'
            def fn_13369() -> 'str34':
                return 'negative int'
            test_257.assert_(t_13376, fn_13369)
            t_13378: 'SqlBuilder' = SqlBuilder()
            t_13378.append_safe('v = ')
            t_13378.append_int32(0)
            t_13384: 'bool42' = t_13378.accumulated.to_string() == 'v = 0'
            def fn_13368() -> 'str34':
                return 'zero int'
            test_257.assert_(t_13384, fn_13368)
        finally:
            test_257.soft_fail_to_hard()
class TestCase270(TestCase53):
    def test___sqlInt64_negativeValue__2723(self) -> None:
        'SqlInt64 negative value'
        test_258: Test = Test()
        try:
            t_13360: 'SqlBuilder' = SqlBuilder()
            t_13360.append_safe('v = ')
            t_13360.append_int64(-99)
            t_13366: 'bool42' = t_13360.accumulated.to_string() == 'v = -99'
            def fn_13359() -> 'str34':
                return 'negative int64'
            test_258.assert_(t_13366, fn_13359)
        finally:
            test_258.soft_fail_to_hard()
class TestCase271(TestCase53):
    def test___singleElementListRendering__2725(self) -> None:
        'single element list rendering'
        test_259: Test = Test()
        try:
            t_13341: 'SqlBuilder' = SqlBuilder()
            t_13341.append_safe('v IN (')
            t_13341.append_int32_list((42,))
            t_13341.append_safe(')')
            t_13348: 'bool42' = t_13341.accumulated.to_string() == 'v IN (42)'
            def fn_13340() -> 'str34':
                return 'single int'
            test_259.assert_(t_13348, fn_13340)
            t_13350: 'SqlBuilder' = SqlBuilder()
            t_13350.append_safe('v IN (')
            t_13350.append_string_list(('only',))
            t_13350.append_safe(')')
            t_13357: 'bool42' = t_13350.accumulated.to_string() == "v IN ('only')"
            def fn_13339() -> 'str34':
                return 'single string'
            test_259.assert_(t_13357, fn_13339)
        finally:
            test_259.soft_fail_to_hard()
class TestCase272(TestCase53):
    def test___sqlDefaultRendersDefaultKeyword__2728(self) -> None:
        'SqlDefault renders DEFAULT keyword'
        test_260: Test = Test()
        try:
            b_2142: 'SqlBuilder' = SqlBuilder()
            b_2142.append_safe('v = ')
            b_2142.append_part(SqlDefault())
            t_13337: 'bool42' = b_2142.accumulated.to_string() == 'v = DEFAULT'
            def fn_13329() -> 'str34':
                return 'default keyword'
            test_260.assert_(t_13337, fn_13329)
        finally:
            test_260.soft_fail_to_hard()
class TestCase273(TestCase53):
    def test___sqlStringWithBackslash__2729(self) -> None:
        'SqlString with backslash'
        test_261: Test = Test()
        try:
            t_13321: 'SqlBuilder' = SqlBuilder()
            t_13321.append_safe('v = ')
            t_13321.append_string('a\\b')
            t_13327: 'bool42' = t_13321.accumulated.to_string() == "v = 'a\\b'"
            def fn_13320() -> 'str34':
                return 'backslash passthrough'
            test_261.assert_(t_13327, fn_13320)
        finally:
            test_261.soft_fail_to_hard()
