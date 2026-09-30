from builtins import bool as bool41, str as str36, Exception as Exception46, list as list14, int as int42, tuple as tuple19, len as len1
from typing import MutableSequence as MutableSequence47, Callable as Callable67, Sequence as Sequence45, Union as Union38
from temper_core import Pair as Pair64, Label as Label48, list_join as list_join63, list_map as list_map65, string_get as string_get21, str_cat as str_cat24, int_to_string as int_to_string5, string_next as string_next23, int_add as int_add3, listed_reduce_from as listed_reduce_from66, list_get as list_get2
_tuple_1379 = tuple19
_list_join_1381 = list_join63
_list_1382 = list14
_pair_1383 = Pair64
_list_map_1384 = list_map65
_len_1386 = len1
_string_get_1388 = string_get21
_str_cat_1389 = str_cat24
_int_to_string_1390 = int_to_string5
_string_next_1393 = string_next23
_int_add_1396 = int_add3
_listed_reduce_from_1397 = listed_reduce_from66
_list_get_1398 = list_get2
class Test:
    _failed_on_assert_65: 'bool41'
    _passing_66: 'bool41'
    _messages_67: 'MutableSequence47[str36]'
    __slots__ = ('_failed_on_assert_65', '_passing_66', '_messages_67')
    def assert_(this_8, success_43: 'bool41', message_44: 'Callable67[[], str36]', /) -> 'None':
        if not success_43:
            this_8._passing_66 = False
            this_8._messages_67.append(message_44())
    def assert_hard(this_9, success_47: 'bool41', message_48: 'Callable67[[], str36]', /) -> 'None':
        this_9.assert_(success_47, message_48)
        if not success_47:
            this_9._failed_on_assert_65 = True
            assert False, str36(this_9.messages_combined())
    def soft_fail_to_hard(this_10, /) -> 'None':
        if this_10.has_unhandled_fail:
            this_10._failed_on_assert_65 = True
            assert False, str36(this_10.messages_combined())
    @property
    def passing(this_12, /) -> 'bool41':
        return this_12._passing_66
    def messages(this_13, /) -> 'Sequence45[str36]':
        "Messages access is presented as a function because it likely allocates. Also,\nmessages might be automatically constructed in some cases, so it's possibly\nunwise to depend on their exact formatting.\n\nthis__13: Test\n"
        return _tuple_1379(this_13._messages_67)
    @property
    def failed_on_assert(this_14, /) -> 'bool41':
        return this_14._failed_on_assert_65
    @property
    def has_unhandled_fail(this_15, /) -> 'bool41':
        t_151: 'bool41'
        if this_15._failed_on_assert_65:
            t_151 = True
        else:
            t_151 = this_15._passing_66
        return not t_151
    def messages_combined(this_16, /) -> 'Union38[str36, None]':
        if not this_16._messages_67:
            return None
        else:
            def fn_158(it_64: 'str36', /) -> 'str36':
                return it_64
            return _list_join_1381(this_16._messages_67, ', ', fn_158)
    def __init__(this, /) -> None:
        this._failed_on_assert_65 = False
        this._passing_66 = True
        t_111: 'MutableSequence47[str36]' = _list_1382()
        this._messages_67 = t_111
def process_test_cases(test_cases_69: 'Sequence45[(Pair64[str36, (Callable67[[Test], None])])]', /) -> 'Sequence45[(Pair64[str36, (Sequence45[str36])])]':
    def fn_157(test_case_71: 'Pair64[str36, (Callable67[[Test], None])]', /) -> 'Pair64[str36, (Sequence45[str36])]':
        key_73: 'str36' = test_case_71.key
        fun_74: 'Callable67[[Test], None]' = test_case_71.value
        test_75: 'Test' = Test()
        had_bubble_76: 'bool41' = False
        try:
            fun_74(test_75)
        except Exception46:
            had_bubble_76 = True
        messages_77: 'Sequence45[str36]' = test_75.messages()
        failures_78: 'Sequence45[str36]'
        t_145: 'bool41'
        if test_75.passing:
            t_145 = not had_bubble_76
        else:
            t_145 = False
        if t_145:
            failures_78 = ()
        else:
            t_148: 'bool41'
            if had_bubble_76:
                t_148 = not test_75.failed_on_assert
            else:
                t_148 = False
            if t_148:
                all_messages_79: 'MutableSequence47[str36]' = _list_1382(messages_77)
                all_messages_79.append('Bubble')
                failures_78 = _tuple_1379(all_messages_79)
            else:
                failures_78 = messages_77
        return _pair_1383(key_73, failures_78)
    return _list_map_1384(test_cases_69, fn_157)
def _escape_xml(s_103: 'str36', /) -> 'str36':
    'escapeXml takes a string and escapes it so that it has the same meaning as an\nXML text node or attribute value.\n\ns__103: String\n'
    sb_105: 'list14[str36]' = ['']
    end_106: 'int42' = _len_1386(s_103)
    emitted_107: 'int42' = 0
    i_108: 'int42' = 0
    while i_108 < end_106:
        with Label48() as continue_159:
            c_109: 'int42' = _string_get_1388(s_103, i_108)
            esc_110: 'str36'
            if c_109 == 38:
                esc_110 = '&amp;'
            elif c_109 == 60:
                esc_110 = '&lt;'
            elif c_109 == 62:
                esc_110 = '&gt;'
            elif c_109 == 39:
                esc_110 = '&#39;'
            elif c_109 == 34:
                esc_110 = '&#34;'
            else:
                t_132: 'bool41'
                if c_109 == 10:
                    t_132 = True
                elif c_109 == 13:
                    t_132 = True
                else:
                    t_132 = c_109 == 9
                if t_132:
                    continue_159.break_()
                else:
                    t_136: 'bool41'
                    if c_109 < 32:
                        t_136 = True
                    elif c_109 == 65534:
                        t_136 = True
                    else:
                        t_136 = c_109 == 65535
                    if t_136:
                        esc_110 = _str_cat_1389('[0x', _int_to_string_1390(c_109, 16), ']')
                    else:
                        continue_159.break_()
            sb_105.append(s_103[emitted_107 : i_108])
            sb_105.append(esc_110)
            emitted_107 = _string_next_1393(s_103, i_108)
        i_108 = _string_next_1393(s_103, i_108)
    if emitted_107 == 0:
        return s_103
    else:
        sb_105.append(s_103[emitted_107 : end_106])
        return ''.join(sb_105)
def report_test_results(test_results_80: 'Sequence45[(Pair64[str36, (Sequence45[str36])])]', write_line_81: 'Callable67[[str36], None]', /) -> 'None':
    write_line_81('<testsuites>')
    total_83: 'str36' = _int_to_string_1390(_len_1386(test_results_80))
    def fn_156(fails_85: 'int42', test_result_86: 'Pair64[str36, (Sequence45[str36])]', /) -> 'int42':
        t_131: 'int42'
        if not test_result_86.value:
            t_131 = 0
        else:
            t_131 = 1
        return _int_add_1396(fails_85, t_131)
    fails_84: 'str36' = _int_to_string_1390(_listed_reduce_from_1397(test_results_80, 0, fn_156))
    totals_88: 'str36' = _str_cat_1389("tests='", total_83, "' failures='", fails_84, "'")
    write_line_81(_str_cat_1389("  <testsuite name='suite' ", totals_88, " time='0.0'>"))
    i_89: 'int42' = 0
    while i_89 < _len_1386(test_results_80):
        test_result_90: 'Pair64[str36, (Sequence45[str36])]' = _list_get_1398(test_results_80, i_89)
        failure_messages_91: 'Sequence45[str36]' = test_result_90.value
        name_92: 'str36' = _escape_xml(test_result_90.key)
        basics_93: 'str36' = _str_cat_1389("name='", name_92, "' classname='", name_92, "' time='0.0'")
        if not failure_messages_91:
            write_line_81(_str_cat_1389('    <testcase ', basics_93, ' />'))
        else:
            write_line_81(_str_cat_1389('    <testcase ', basics_93, '>'))
            def fn_155(it_95: 'str36', /) -> 'str36':
                return it_95
            message_94: 'str36' = _escape_xml(_list_join_1381(failure_messages_91, ', ', fn_155))
            write_line_81(_str_cat_1389("      <failure message='", message_94, "' />"))
            write_line_81('    </testcase>')
        i_89 = _int_add_1396(i_89, 1)
    write_line_81('  </testsuite>')
    write_line_81('</testsuites>')
def run_test_cases(test_cases_96: 'Sequence45[(Pair64[str36, (Callable67[[Test], None])])]', /) -> 'str36':
    report_98: 'list14[str36]' = ['']
    def fn_154(line_99: 'str36', /) -> 'None':
        report_98.append(line_99)
        report_98.append('\n')
    report_test_results(process_test_cases(test_cases_96), fn_154)
    return ''.join(report_98)
def run_test(test_fun_100: 'Callable67[[Test], None]', /) -> 'None':
    test_102: 'Test' = Test()
    try:
        test_fun_100(test_102)
    except Exception46:
        def fn_153() -> 'str36':
            return 'bubble during test running'
        test_102.assert_(False, fn_153)
    test_102.soft_fail_to_hard()
