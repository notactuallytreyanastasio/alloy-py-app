from abc import ABCMeta as ABCMeta35
from builtins import str as str36, bool as bool41, int as int42, list as list14, isinstance as isinstance50, len as len1, tuple as tuple19
from typing import Callable as Callable67, Sequence as Sequence45, Union as Union38, Any as Any52, ClassVar as ClassVar39, MutableSequence as MutableSequence47
from types import MappingProxyType as MappingProxyType44
from temper_core import cast_by_type as cast_by_type51, Label as Label48, Pair as Pair64, map_constructor as map_constructor70, list_get as list_get2, string_from_code_point as string_from_code_point55, string_get as string_get21, string_next as string_next23, int_add as int_add3, str_cat as str_cat24, int_to_string as int_to_string5
from temper_core.regex import regex_compile_formatted as regex_compile_formatted71, regex_compiled_found as regex_compiled_found72, regex_compiled_find as regex_compiled_find73, regex_compiled_replace as regex_compiled_replace74, regex_compiled_split as regex_compiled_split75, regex_formatter_push_capture_name as regex_formatter_push_capture_name76, regex_formatter_push_code_to as regex_formatter_push_code_to77
_pair_1400 = Pair64
_map_constructor_1401 = map_constructor70
_regex_compile_formatted_1402 = regex_compile_formatted71
_regex_compiled_found_1403 = regex_compiled_found72
_regex_compiled_find_1404 = regex_compiled_find73
_regex_compiled_replace_1405 = regex_compiled_replace74
_regex_compiled_split_1406 = regex_compiled_split75
_regex_formatter_push_capture_name_1409 = regex_formatter_push_capture_name76
_list_get_1410 = list_get2
_string_from_code_point_1411 = string_from_code_point55
_regex_formatter_push_code_to_1412 = regex_formatter_push_code_to77
_string_get_1414 = string_get21
_string_next_1415 = string_next23
_len_1417 = len1
_int_add_1418 = int_add3
_str_cat_1419 = str_cat24
_int_to_string_1420 = int_to_string5
_list_1422 = list14
_tuple_1424 = tuple19
class RegexNode(metaclass = ABCMeta35):
    def compiled(this_11, /) -> 'Regex':
        return Regex(this_11)
    def found(this_12, text_172: 'str36', /) -> 'bool41':
        return this_12.compiled().found(text_172)
    def find(this_13, text_175: 'str36', /) -> 'Match':
        return this_13.compiled().find(text_175)
    def replace(this_14, text_178: 'str36', format_179: 'Callable67[[Match], str36]', /) -> 'str36':
        'Replace and split functions are also available. Both apply to all matches in\nthe string, replacing all or splitting at all.\n\nthis__14: RegexNode\n\ntext__178: String\n\nformat__179: fn (Match): String\n'
        return this_14.compiled().replace(text_178, format_179)
    def split(this_15, text_182: 'str36', /) -> 'Sequence45[str36]':
        return this_15.compiled().split(text_182)
class Capture(RegexNode):
    '`Capture` is a [group](#groups) that remembers the matched text for later\naccess. Temper supports only named matches, with current intended syntax\n`/(?name = ...)/`.'
    _name_184: 'str36'
    _item_185: 'RegexNode'
    __slots__ = ('_name_184', '_item_185')
    def __init__(this, /, name: 'str36', item: 'RegexNode') -> None:
        this._name_184 = name
        this._item_185 = item
    @property
    def name(this_446, /) -> 'str36':
        return this_446._name_184
    @property
    def item(this_449, /) -> 'RegexNode':
        return this_449._item_185
class CodePart(RegexNode, metaclass = ABCMeta35):
    pass
class CodePoints(CodePart):
    _value_189: 'str36'
    __slots__ = ('_value_189',)
    def __init__(this_91, /, value: 'str36') -> None:
        this_91._value_189 = value
    @property
    def value(this_452, /) -> 'str36':
        return this_452._value_189
class Special(RegexNode, metaclass = ABCMeta35):
    pass
class _BeginSpecial(Special):
    __slots__ = ()
    def __init__(this_93, /) -> None:
        pass
class _DotSpecial(Special):
    __slots__ = ()
    def __init__(this_95, /) -> None:
        pass
class _EndSpecial(Special):
    __slots__ = ()
    def __init__(this_97, /) -> None:
        pass
class _WordBoundarySpecial(Special):
    __slots__ = ()
    def __init__(this_99, /) -> None:
        pass
class SpecialSet(CodePart, Special, metaclass = ABCMeta35):
    pass
class _DigitSpecial(SpecialSet):
    __slots__ = ()
    def __init__(this_101, /) -> None:
        pass
    def compiled(inp_1370, /) -> 'Regex':
        return RegexNode.compiled(inp_1370)
    def found(inp_1371, text_1372: 'str36', /) -> 'bool41':
        return RegexNode.found(inp_1371, text_1372)
    def find(inp_1373, text_1374: 'str36', /) -> 'Match':
        return RegexNode.find(inp_1373, text_1374)
    def replace(inp_1375, text_1376: 'str36', format_1377: 'Callable67[[Match], str36]', /) -> 'str36':
        return RegexNode.replace(inp_1375, text_1376, format_1377)
    def split(inp_1378, text_1379: 'str36', /) -> 'Sequence45[str36]':
        return RegexNode.split(inp_1378, text_1379)
class _SpaceSpecial(SpecialSet):
    __slots__ = ()
    def __init__(this_103, /) -> None:
        pass
    def compiled(inp_1380, /) -> 'Regex':
        return RegexNode.compiled(inp_1380)
    def found(inp_1381, text_1382: 'str36', /) -> 'bool41':
        return RegexNode.found(inp_1381, text_1382)
    def find(inp_1383, text_1384: 'str36', /) -> 'Match':
        return RegexNode.find(inp_1383, text_1384)
    def replace(inp_1385, text_1386: 'str36', format_1387: 'Callable67[[Match], str36]', /) -> 'str36':
        return RegexNode.replace(inp_1385, text_1386, format_1387)
    def split(inp_1388, text_1389: 'str36', /) -> 'Sequence45[str36]':
        return RegexNode.split(inp_1388, text_1389)
class _WordSpecial(SpecialSet):
    __slots__ = ()
    def __init__(this_105, /) -> None:
        pass
    def compiled(inp_1390, /) -> 'Regex':
        return RegexNode.compiled(inp_1390)
    def found(inp_1391, text_1392: 'str36', /) -> 'bool41':
        return RegexNode.found(inp_1391, text_1392)
    def find(inp_1393, text_1394: 'str36', /) -> 'Match':
        return RegexNode.find(inp_1393, text_1394)
    def replace(inp_1395, text_1396: 'str36', format_1397: 'Callable67[[Match], str36]', /) -> 'str36':
        return RegexNode.replace(inp_1395, text_1396, format_1397)
    def split(inp_1398, text_1399: 'str36', /) -> 'Sequence45[str36]':
        return RegexNode.split(inp_1398, text_1399)
class CodeRange(CodePart):
    _min_206: 'int42'
    _max_207: 'int42'
    __slots__ = ('_min_206', '_max_207')
    def __init__(this_107, /, min: 'int42', max: 'int42') -> None:
        this_107._min_206 = min
        this_107._max_207 = max
    @property
    def min(this_455, /) -> 'int42':
        return this_455._min_206
    @property
    def max(this_458, /) -> 'int42':
        return this_458._max_207
class CodeSet(RegexNode):
    _items_211: 'Sequence45[CodePart]'
    _negated_212: 'bool41'
    __slots__ = ('_items_211', '_negated_212')
    def __init__(this_109, /, items: 'Sequence45[CodePart]', negated: 'Union38[bool41, None]' = None) -> None:
        _negated: 'Union38[bool41, None]' = negated
        negated_215: 'bool41'
        if _negated is None:
            negated_215 = False
        else:
            negated_215 = _negated
        this_109._items_211 = items
        this_109._negated_212 = negated_215
    @property
    def items(this_461, /) -> 'Sequence45[CodePart]':
        return this_461._items_211
    @property
    def negated(this_464, /) -> 'bool41':
        return this_464._negated_212
class Or(RegexNode):
    '`Or` matches any one of multiple options, such as `/ab|cd|e*/`.'
    _items_216: 'Sequence45[RegexNode]'
    __slots__ = ('_items_216',)
    def __init__(this_112, /, items_218: 'Sequence45[RegexNode]') -> None:
        this_112._items_216 = items_218
    @property
    def items(this_467, /) -> 'Sequence45[RegexNode]':
        return this_467._items_216
class Repeat(RegexNode):
    _item_219: 'RegexNode'
    _min_220: 'int42'
    _max_221: 'Union38[int42, None]'
    _reluctant_222: 'bool41'
    __slots__ = ('_item_219', '_min_220', '_max_221', '_reluctant_222')
    def __init__(this_115, /, item_224: 'RegexNode', min_225: 'int42', max_226: 'Union38[int42, None]', reluctant: 'Union38[bool41, None]' = None) -> None:
        _reluctant: 'Union38[bool41, None]' = reluctant
        reluctant_227: 'bool41'
        if _reluctant is None:
            reluctant_227 = False
        else:
            reluctant_227 = _reluctant
        this_115._item_219 = item_224
        this_115._min_220 = min_225
        this_115._max_221 = max_226
        this_115._reluctant_222 = reluctant_227
    @property
    def item(this_470, /) -> 'RegexNode':
        return this_470._item_219
    @property
    def min(this_473, /) -> 'int42':
        return this_473._min_220
    @property
    def max(this_476, /) -> 'Union38[int42, None]':
        return this_476._max_221
    @property
    def reluctant(this_479, /) -> 'bool41':
        return this_479._reluctant_222
class Sequence(RegexNode):
    '`Sequence` strings along multiple other regexes in order.'
    _items_236: 'Sequence45[RegexNode]'
    __slots__ = ('_items_236',)
    def __init__(this_121, /, items_238: 'Sequence45[RegexNode]') -> None:
        this_121._items_236 = items_238
    @property
    def items(this_482, /) -> 'Sequence45[RegexNode]':
        return this_482._items_236
class Match:
    _full_239: 'Group'
    _groups_240: 'MappingProxyType44[str36, Group]'
    __slots__ = ('_full_239', '_groups_240')
    def __init__(this_124, /, full: 'Group', groups: 'MappingProxyType44[str36, Group]') -> None:
        this_124._full_239 = full
        this_124._groups_240 = groups
    @property
    def full(this_497, /) -> 'Group':
        return this_497._full_239
    @property
    def groups(this_500, /) -> 'MappingProxyType44[str36, Group]':
        return this_500._groups_240
class Group:
    _name_244: 'str36'
    _value_245: 'str36'
    _begin_246: 'int42'
    _end_247: 'int42'
    __slots__ = ('_name_244', '_value_245', '_begin_246', '_end_247')
    def __init__(this_127, /, name_249: 'str36', value_250: 'str36', begin: 'int42', end: 'int42') -> None:
        this_127._name_244 = name_249
        this_127._value_245 = value_250
        this_127._begin_246 = begin
        this_127._end_247 = end
    @property
    def name(this_485, /) -> 'str36':
        return this_485._name_244
    @property
    def value(this_488, /) -> 'str36':
        return this_488._value_245
    @property
    def begin(this_491, /) -> 'int42':
        return this_491._begin_246
    @property
    def end(this_494, /) -> 'int42':
        return this_494._end_247
class _RegexRefs:
    _code_points_253: 'CodePoints'
    _group_254: 'Group'
    _match_255: 'Match'
    _or_object_256: 'Or'
    __slots__ = ('_code_points_253', '_group_254', '_match_255', '_or_object_256')
    def __init__(this_129, /, code_points: 'Union38[CodePoints, None]' = None, group: 'Union38[Group, None]' = None, match_: 'Union38[Match, None]' = None, or_object: 'Union38[Or, None]' = None) -> None:
        _code_points: 'Union38[CodePoints, None]' = code_points
        _group: 'Union38[Group, None]' = group
        _match_: 'Union38[Match, None]' = match_
        _or_object: 'Union38[Or, None]' = or_object
        code_points_258: 'CodePoints'
        if _code_points is None:
            code_points_258 = CodePoints('')
        else:
            code_points_258 = _code_points
        group_259: 'Group'
        if _group is None:
            group_259 = Group('', '', 0, 0)
        else:
            group_259 = _group
        match_260: 'Match'
        if _match_ is None:
            match_260 = Match(group_259, _map_constructor_1401((_pair_1400('', group_259),)))
        else:
            match_260 = _match_
        or_object_261: 'Or'
        if _or_object is None:
            or_object_261 = Or(())
        else:
            or_object_261 = _or_object
        this_129._code_points_253 = code_points_258
        this_129._group_254 = group_259
        this_129._match_255 = match_260
        this_129._or_object_256 = or_object_261
    @property
    def code_points(this_503, /) -> 'CodePoints':
        return this_503._code_points_253
    @property
    def group(this_506, /) -> 'Group':
        return this_506._group_254
    @property
    def match_(this_509, /) -> 'Match':
        return this_509._match_255
    @property
    def or_object(this_512, /) -> 'Or':
        return this_512._or_object_256
class Regex:
    _data_262: 'RegexNode'
    _compiled_281: 'Any52'
    __slots__ = ('_data_262', '_compiled_281')
    def __init__(this_24, /, data: 'RegexNode') -> None:
        t_421: 'RegexNode' = data
        this_24._data_262 = t_421
        formatted_266: 'str36' = _RegexFormatter.regex_format(data)
        t_420: 'Any52' = _regex_compile_formatted_1402(data, formatted_266)
        this_24._compiled_281 = t_420
    def found(this_25, text_268: 'str36', /) -> 'bool41':
        return _regex_compiled_found_1403(this_25, this_25._compiled_281, text_268)
    def find(this_26, text_271: 'str36', begin_550: 'Union38[int42, None]' = None, /) -> 'Match':
        _begin_550: 'Union38[int42, None]' = begin_550
        begin_272: 'int42'
        if _begin_550 is None:
            begin_272 = 0
        else:
            begin_272 = _begin_550
        return _regex_compiled_find_1404(this_26, this_26._compiled_281, text_271, begin_272, _regex_refs)
    def replace(this_27, text_275: 'str36', format_276: 'Callable67[[Match], str36]', /) -> 'str36':
        return _regex_compiled_replace_1405(this_27, this_27._compiled_281, text_275, format_276, _regex_refs)
    def split(this_28, text_279: 'str36', /) -> 'Sequence45[str36]':
        return _regex_compiled_split_1406(this_28, this_28._compiled_281, text_279, _regex_refs)
    @property
    def data(this_539, /) -> 'RegexNode':
        return this_539._data_262
class _RegexFormatter:
    _out_303: 'list14[str36]'
    __slots__ = ('_out_303',)
    @staticmethod
    def regex_format(data_309: 'RegexNode', /) -> 'str36':
        return _RegexFormatter().format(data_309)
    def format(this_34, regex_312: 'RegexNode', /) -> 'str36':
        this_34._push_regex_314(regex_312)
        return ''.join(this_34._out_303)
    def _push_regex_314(this_35, regex_315: 'RegexNode', /) -> 'None':
        if isinstance50(regex_315, Capture):
            t_639: 'Capture' = cast_by_type51(regex_315, Capture)
            this_35._push_capture_317(t_639)
        elif isinstance50(regex_315, CodePoints):
            t_642: 'CodePoints' = cast_by_type51(regex_315, CodePoints)
            this_35._push_code_points_335(t_642, False)
        elif isinstance50(regex_315, CodeRange):
            t_645: 'CodeRange' = cast_by_type51(regex_315, CodeRange)
            this_35._push_code_range_341(t_645)
        elif isinstance50(regex_315, CodeSet):
            t_648: 'CodeSet' = cast_by_type51(regex_315, CodeSet)
            this_35._push_code_set_347(t_648)
        elif isinstance50(regex_315, Or):
            t_651: 'Or' = cast_by_type51(regex_315, Or)
            this_35._push_or_359(t_651)
        elif isinstance50(regex_315, Repeat):
            t_654: 'Repeat' = cast_by_type51(regex_315, Repeat)
            this_35._push_repeat_363(t_654)
        elif isinstance50(regex_315, Sequence):
            t_657: 'Sequence' = cast_by_type51(regex_315, Sequence)
            this_35._push_sequence_368(t_657)
        elif isinstance50(regex_315, _BeginSpecial):
            this_35._out_303.append('^')
        elif isinstance50(regex_315, _DotSpecial):
            this_35._out_303.append('.')
        elif isinstance50(regex_315, _EndSpecial):
            this_35._out_303.append('$')
        elif isinstance50(regex_315, _WordBoundarySpecial):
            this_35._out_303.append('\\b')
        elif isinstance50(regex_315, _DigitSpecial):
            this_35._out_303.append('\\d')
        elif isinstance50(regex_315, _SpaceSpecial):
            this_35._out_303.append('\\s')
        elif isinstance50(regex_315, _WordSpecial):
            this_35._out_303.append('\\w')
    def _push_capture_317(this_36, capture_318: 'Capture', /) -> 'None':
        this_36._out_303.append('(')
        _regex_formatter_push_capture_name_1409(this_36, this_36._out_303, capture_318.name)
        this_36._push_regex_314(capture_318.item)
        this_36._out_303.append(')')
    def _push_code_324(this_38, code_325: 'int42', inside_code_set_326: 'bool41', /) -> 'None':
        with Label48() as fn_327:
            special_escape_328: 'str36'
            if code_325 == _Codes.carriage_return:
                special_escape_328 = 'r'
            elif code_325 == _Codes.newline:
                special_escape_328 = 'n'
            elif code_325 == _Codes.tab:
                special_escape_328 = 't'
            else:
                special_escape_328 = ''
            if not special_escape_328 == '':
                this_38._out_303.append('\\')
                this_38._out_303.append(special_escape_328)
                fn_327.break_()
            if code_325 <= 127:
                escape_need_329: 'int42' = _list_get_1410(_escape_needs, code_325)
                t_627: 'bool41'
                if escape_need_329 == 2:
                    t_627 = True
                elif inside_code_set_326:
                    t_627 = code_325 == _Codes.dash
                else:
                    t_627 = False
                if t_627:
                    this_38._out_303.append('\\')
                    t_711: 'list14[str36]' = this_38._out_303
                    t_710: 'str36' = _string_from_code_point_1411(code_325)
                    t_711.append(t_710)
                    fn_327.break_()
                elif escape_need_329 == 0:
                    t_713: 'list14[str36]' = this_38._out_303
                    t_712: 'str36' = _string_from_code_point_1411(code_325)
                    t_713.append(t_712)
                    fn_327.break_()
            t_634: 'bool41'
            if code_325 >= _Codes.supplemental_min:
                t_634 = True
            elif code_325 > _Codes.high_control_max:
                t_632: 'bool41'
                t_630: 'bool41'
                if _Codes.surrogate_min <= code_325:
                    t_630 = code_325 <= _Codes.surrogate_max
                else:
                    t_630 = False
                if t_630:
                    t_632 = True
                else:
                    t_632 = code_325 == _Codes.uint16_max
                t_634 = not t_632
            else:
                t_634 = False
            if t_634:
                t_715: 'list14[str36]' = this_38._out_303
                t_714: 'str36' = _string_from_code_point_1411(code_325)
                t_715.append(t_714)
            else:
                _regex_formatter_push_code_to_1412(this_38, this_38._out_303, code_325, inside_code_set_326)
    def _push_code_points_335(this_40, code_points_336: 'CodePoints', inside_code_set_337: 'bool41', /) -> 'None':
        value_339: 'str36' = code_points_336.value
        index_340: 'int42' = 0
        while len1(value_339) > index_340:
            this_40._push_code_324(_string_get_1414(value_339, index_340), inside_code_set_337)
            index_340 = _string_next_1415(value_339, index_340)
    def _push_code_range_341(this_41, code_range_342: 'CodeRange', /) -> 'None':
        this_41._out_303.append('[')
        this_41._push_code_range_unwrapped_344(code_range_342)
        this_41._out_303.append(']')
    def _push_code_range_unwrapped_344(this_42, code_range_345: 'CodeRange', /) -> 'None':
        this_42._push_code_324(code_range_345.min, True)
        this_42._out_303.append('-')
        this_42._push_code_324(code_range_345.max, True)
    def _push_code_set_347(this_43, code_set_348: 'CodeSet', /) -> 'None':
        adjusted_350: 'RegexNode' = this_43._adjust_code_set_352(code_set_348, _regex_refs)
        if isinstance50(adjusted_350, CodeSet):
            t_623: 'CodeSet' = cast_by_type51(adjusted_350, CodeSet)
            if not t_623.items:
                if t_623.negated:
                    this_43._out_303.append('[\\s\\S]')
                else:
                    this_43._out_303.append('(?:$.)')
            else:
                this_43._out_303.append('[')
                if t_623.negated:
                    this_43._out_303.append('^')
                i_351: 'int42' = 0
                while i_351 < _len_1417(t_623.items):
                    this_43._push_code_set_item_356(_list_get_1410(t_623.items, i_351))
                    i_351 = _int_add_1418(i_351, 1)
                this_43._out_303.append(']')
        else:
            this_43._push_regex_314(adjusted_350)
    def _adjust_code_set_352(this_44, code_set_353: 'CodeSet', regex_refs_354: '_RegexRefs', /) -> 'RegexNode':
        return code_set_353
    def _push_code_set_item_356(this_45, code_part_357: 'CodePart', /) -> 'None':
        if isinstance50(code_part_357, CodePoints):
            t_614: 'CodePoints' = cast_by_type51(code_part_357, CodePoints)
            this_45._push_code_points_335(t_614, True)
        elif isinstance50(code_part_357, CodeRange):
            t_617: 'CodeRange' = cast_by_type51(code_part_357, CodeRange)
            this_45._push_code_range_unwrapped_344(t_617)
        elif isinstance50(code_part_357, SpecialSet):
            t_620: 'SpecialSet' = cast_by_type51(code_part_357, SpecialSet)
            this_45._push_regex_314(t_620)
    def _push_or_359(this_46, or_360: 'Or', /) -> 'None':
        if not (not or_360.items):
            this_46._out_303.append('(?:')
            this_46._push_regex_314(_list_get_1410(or_360.items, 0))
            i_362: 'int42' = 1
            while i_362 < _len_1417(or_360.items):
                this_46._out_303.append('|')
                this_46._push_regex_314(_list_get_1410(or_360.items, i_362))
                i_362 = _int_add_1418(i_362, 1)
            this_46._out_303.append(')')
    def _push_repeat_363(this_47, repeat_364: 'Repeat', /) -> 'None':
        this_47._out_303.append('(?:')
        this_47._push_regex_314(repeat_364.item)
        this_47._out_303.append(')')
        min_366: 'int42' = repeat_364.min
        max_367: 'Union38[int42, None]' = repeat_364.max
        t_606: 'bool41'
        if min_366 == 0:
            t_716: 'bool41'
            if max_367 is None:
                t_716 = False
            else:
                t_716 = max_367 == 1
            t_606 = t_716
        else:
            t_606 = False
        if t_606:
            this_47._out_303.append('?')
        else:
            t_608: 'bool41'
            if min_366 == 0:
                t_608 = max_367 is None
            else:
                t_608 = False
            if t_608:
                this_47._out_303.append('*')
            else:
                t_610: 'bool41'
                if min_366 == 1:
                    t_610 = max_367 is None
                else:
                    t_610 = False
                if t_610:
                    this_47._out_303.append('+')
                else:
                    t_718: 'bool41'
                    this_47._out_303.append(_str_cat_1419('{', _int_to_string_1420(min_366)))
                    if max_367 is None:
                        t_718 = False
                    else:
                        t_718 = min_366 == max_367
                    if not t_718:
                        this_47._out_303.append(',')
                        if not max_367 is None:
                            max_578: 'int42' = max_367
                            this_47._out_303.append(_int_to_string_1420(max_578))
                    this_47._out_303.append('}')
        if repeat_364.reluctant:
            this_47._out_303.append('?')
    def _push_sequence_368(this_48, sequence_369: 'Sequence', /) -> 'None':
        i_371: 'int42' = 0
        while i_371 < _len_1417(sequence_369.items):
            this_48._push_regex_314(_list_get_1410(sequence_369.items, i_371))
            i_371 = _int_add_1418(i_371, 1)
    def max_code(this_49, code_part_373: 'CodePart', /) -> 'Union38[int42, None]':
        if isinstance50(code_part_373, CodePoints):
            t_596: 'CodePoints' = cast_by_type51(code_part_373, CodePoints)
            value_375: 'str36' = t_596.value
            if not value_375:
                return None
            else:
                max_376: 'int42' = 0
                index_377: 'int42' = 0
                while len1(value_375) > index_377:
                    next_378: 'int42' = _string_get_1414(value_375, index_377)
                    if next_378 > max_376:
                        max_376 = next_378
                    index_377 = _string_next_1415(value_375, index_377)
                return max_376
        elif isinstance50(code_part_373, CodeRange):
            return cast_by_type51(code_part_373, CodeRange).max
        elif isinstance50(code_part_373, _DigitSpecial):
            return _Codes.digit9
        elif isinstance50(code_part_373, _SpaceSpecial):
            return _Codes.space
        elif isinstance50(code_part_373, _WordSpecial):
            return _Codes.lower_z
        else:
            return None
    def __init__(this_140, /) -> None:
        t_419: 'list14[str36]' = ['']
        this_140._out_303 = t_419
class _Codes:
    ampersand: ClassVar39['int42']
    backslash: ClassVar39['int42']
    caret: ClassVar39['int42']
    carriage_return: ClassVar39['int42']
    curly_left: ClassVar39['int42']
    curly_right: ClassVar39['int42']
    dash: ClassVar39['int42']
    dot: ClassVar39['int42']
    high_control_min: ClassVar39['int42']
    high_control_max: ClassVar39['int42']
    digit0: ClassVar39['int42']
    digit9: ClassVar39['int42']
    lower_a: ClassVar39['int42']
    lower_z: ClassVar39['int42']
    newline: ClassVar39['int42']
    peso: ClassVar39['int42']
    pipe: ClassVar39['int42']
    plus: ClassVar39['int42']
    question: ClassVar39['int42']
    round_left: ClassVar39['int42']
    round_right: ClassVar39['int42']
    slash: ClassVar39['int42']
    square_left: ClassVar39['int42']
    square_right: ClassVar39['int42']
    star: ClassVar39['int42']
    tab: ClassVar39['int42']
    tilde: ClassVar39['int42']
    upper_a: ClassVar39['int42']
    upper_z: ClassVar39['int42']
    space: ClassVar39['int42']
    surrogate_min: ClassVar39['int42']
    surrogate_max: ClassVar39['int42']
    supplemental_min: ClassVar39['int42']
    uint16_max: ClassVar39['int42']
    underscore: ClassVar39['int42']
    __slots__ = ()
    def __init__(this_161, /) -> None:
        pass
_Codes.ampersand = 38
_Codes.backslash = 92
_Codes.caret = 94
_Codes.carriage_return = 13
_Codes.curly_left = 123
_Codes.curly_right = 125
_Codes.dash = 45
_Codes.dot = 46
_Codes.high_control_min = 127
_Codes.high_control_max = 159
_Codes.digit0 = 48
_Codes.digit9 = 57
_Codes.lower_a = 97
_Codes.lower_z = 122
_Codes.newline = 10
_Codes.peso = 36
_Codes.pipe = 124
_Codes.plus = 43
_Codes.question = 63
_Codes.round_left = 40
_Codes.round_right = 41
_Codes.slash = 47
_Codes.square_left = 91
_Codes.square_right = 93
_Codes.star = 42
_Codes.tab = 9
_Codes.tilde = 42
_Codes.upper_a = 65
_Codes.upper_z = 90
_Codes.space = 32
_Codes.surrogate_min = 55296
_Codes.surrogate_max = 57343
_Codes.supplemental_min = 65536
_Codes.uint16_max = 65535
_Codes.underscore = 95
def _build_escape_needs() -> 'Sequence45[int42]':
    escape_needs_381: 'MutableSequence47[int42]' = _list_1422()
    code_382: 'int42' = 0
    while code_382 <= 127:
        t_704: 'int42'
        t_680: 'bool41'
        if code_382 == _Codes.dash:
            t_680 = True
        elif code_382 == _Codes.space:
            t_680 = True
        elif code_382 == _Codes.underscore:
            t_680 = True
        else:
            t_676: 'bool41'
            if _Codes.digit0 <= code_382:
                t_676 = code_382 <= _Codes.digit9
            else:
                t_676 = False
            if t_676:
                t_680 = True
            else:
                t_678: 'bool41'
                if _Codes.upper_a <= code_382:
                    t_678 = code_382 <= _Codes.upper_z
                else:
                    t_678 = False
                if t_678:
                    t_680 = True
                elif _Codes.lower_a <= code_382:
                    t_680 = code_382 <= _Codes.lower_z
                else:
                    t_680 = False
        if t_680:
            t_704 = 0
        else:
            t_687: 'bool41'
            if code_382 == _Codes.ampersand:
                t_687 = True
            elif code_382 == _Codes.backslash:
                t_687 = True
            elif code_382 == _Codes.caret:
                t_687 = True
            elif code_382 == _Codes.curly_left:
                t_687 = True
            elif code_382 == _Codes.curly_right:
                t_687 = True
            elif code_382 == _Codes.dot:
                t_687 = True
            elif code_382 == _Codes.peso:
                t_687 = True
            elif code_382 == _Codes.pipe:
                t_687 = True
            elif code_382 == _Codes.plus:
                t_687 = True
            elif code_382 == _Codes.question:
                t_687 = True
            elif code_382 == _Codes.round_left:
                t_687 = True
            elif code_382 == _Codes.round_right:
                t_687 = True
            elif code_382 == _Codes.slash:
                t_687 = True
            elif code_382 == _Codes.square_left:
                t_687 = True
            elif code_382 == _Codes.square_right:
                t_687 = True
            elif code_382 == _Codes.star:
                t_687 = True
            else:
                t_687 = code_382 == _Codes.tilde
            if t_687:
                t_704 = 2
            else:
                t_704 = 1
        escape_needs_381.append(t_704)
        code_382 = _int_add_1418(code_382, 1)
    return _tuple_1424(escape_needs_381)
_escape_needs: 'Sequence45[int42]' = _build_escape_needs()
_regex_refs: '_RegexRefs' = _RegexRefs()
begin: 'Special' = _BeginSpecial()
dot: 'Special' = _DotSpecial()
end: 'Special' = _EndSpecial()
word_boundary: 'Special' = _WordBoundarySpecial()
digit: 'SpecialSet' = _DigitSpecial()
space: 'SpecialSet' = _SpaceSpecial()
word: 'SpecialSet' = _WordSpecial()
def entire(item_228: 'RegexNode', /) -> 'RegexNode':
    return Sequence((begin, item_228, end))
def one_or_more(item_230: 'RegexNode', reluctant_551: 'Union38[bool41, None]' = None, /) -> 'Repeat':
    _reluctant_551: 'Union38[bool41, None]' = reluctant_551
    reluctant_231: 'bool41'
    if _reluctant_551 is None:
        reluctant_231 = False
    else:
        reluctant_231 = _reluctant_551
    return Repeat(item_230, 1, None, reluctant_231)
def optional(item_233: 'RegexNode', reluctant_552: 'Union38[bool41, None]' = None, /) -> 'Repeat':
    _reluctant_552: 'Union38[bool41, None]' = reluctant_552
    reluctant_234: 'bool41'
    if _reluctant_552 is None:
        reluctant_234 = False
    else:
        reluctant_234 = _reluctant_552
    return Repeat(item_233, 0, 1, reluctant_234)
