from abc import ABCMeta as ABCMeta35, abstractmethod as abstractmethod40
from builtins import str as str36, RuntimeError as RuntimeError37, bool as bool41, int as int42, float as float43, Exception as Exception46, list as list14, isinstance as isinstance50, len as len1, tuple as tuple19
from typing import Union as Union38, ClassVar as ClassVar39, Sequence as Sequence45, MutableSequence as MutableSequence47, Dict as Dict49, Any as Any52, TypeVar as TypeVar53, Generic as Generic54
from types import MappingProxyType as MappingProxyType44
from temper_core import Label as Label48, cast_by_type as cast_by_type51, string_from_code_point as string_from_code_point55, int_sub as int_sub0, list_get as list_get2, int_add as int_add3, mapped_for_each as mapped_for_each4, int_to_string as int_to_string5, int64_to_int32 as int64_to_int326, int64_to_float64 as int64_to_float647, float64_to_string as float64_to_string8, float64_to_int as float64_to_int9, float64_to_int64 as float64_to_int6410, string_to_int32 as string_to_int3211, string_to_float64 as string_to_float6412, string_to_int64 as string_to_int6413, list_get_or as list_get_or15, list_builder_set as list_builder_set16, mapped_has as mapped_has17, map_builder_set as map_builder_set18, mapped_to_map as mapped_to_map20, string_get as string_get21, int_div as int_div22, string_next as string_next23, str_cat as str_cat24, int_mul as int_mul25, string_has_at_least as string_has_at_least26, require_string_index as require_string_index27, int64_add as int64_add28, int64_mul as int64_mul29, int64_cmp as int64_cmp30, int64_sub as int64_sub31, int64_negate as int64_negate32, int64_to_int32_unsafe as int64_to_int32_unsafe33, float_eq as float_eq34
from math import nan as nan56, inf as inf57
_int_sub_1313 = int_sub0
_len_1314 = len1
_list_get_1315 = list_get2
_int_add_1316 = int_add3
_mapped_for_each_1317 = mapped_for_each4
_int_to_string_1318 = int_to_string5
_int64_to_int32_1321 = int64_to_int326
_int64_to_float64_1322 = int64_to_float647
_float64_to_string_1323 = float64_to_string8
_float64_to_int_1324 = float64_to_int9
_float64_to_int64_1325 = float64_to_int6410
_string_to_int32_1326 = string_to_int3211
_string_to_float64_1327 = string_to_float6412
_string_to_int64_1328 = string_to_int6413
_list_1330 = list14
_list_get_or_1332 = list_get_or15
_list_builder_set_1333 = list_builder_set16
_mapped_has_1339 = mapped_has17
_map_builder_set_1341 = map_builder_set18
_tuple_1342 = tuple19
_mapped_to_map_1343 = mapped_to_map20
_string_get_1345 = string_get21
_int_div_1346 = int_div22
_string_next_1347 = string_next23
_str_cat_1349 = str_cat24
_int_mul_1352 = int_mul25
_string_has_at_least_1353 = string_has_at_least26
_require_string_index_1356 = require_string_index27
_int64_add_1357 = int64_add28
_int64_mul_1358 = int64_mul29
_int64_cmp_1359 = int64_cmp30
_int64_sub_1360 = int64_sub31
_int64_negate_1361 = int64_negate32
_int64_to_int32_unsafe_1363 = int64_to_int32_unsafe33
_float_eq_1364 = float_eq34
class InterchangeContext(metaclass = ABCMeta35):
    def get_header(this_36, header_name_389: 'str36', /) -> 'Union38[str36, None]':
        raise RuntimeError37()
class NullInterchangeContext(InterchangeContext):
    instance: ClassVar39['NullInterchangeContext']
    __slots__ = ()
    def get_header(this_37, header_name_392: 'str36', /) -> 'Union38[str36, None]':
        return None
    def __init__(this, /) -> None:
        pass
NullInterchangeContext.instance = NullInterchangeContext()
class JsonProducer(metaclass = ABCMeta35):
    @property
    @abstractmethod40
    def interchange_context(self) -> 'InterchangeContext':
        pass
    def start_object(this_38, /) -> 'None':
        raise RuntimeError37()
    def end_object(this_39, /) -> 'None':
        raise RuntimeError37()
    def object_key(this_40, key_402: 'str36', /) -> 'None':
        raise RuntimeError37()
    def start_array(this_41, /) -> 'None':
        raise RuntimeError37()
    def end_array(this_42, /) -> 'None':
        raise RuntimeError37()
    def null_value(this_43, /) -> 'None':
        raise RuntimeError37()
    def boolean_value(this_44, x_411: 'bool41', /) -> 'None':
        raise RuntimeError37()
    def int32_value(this_45, x_414: 'int42', /) -> 'None':
        raise RuntimeError37()
    def int64_value(this_46, x_417: '_int64', /) -> 'None':
        raise RuntimeError37()
    def float64_value(this_47, x_420: 'float43', /) -> 'None':
        raise RuntimeError37()
    def numeric_token_value(this_48, x_423: 'str36', /) -> 'None':
        'A number that fits the JSON number grammar to allow\ninterchange of numbers that are not easily representible\nusing numeric types that Temper connects to.\n\nthis__48: JsonProducer\n\nx__423: String\n'
        raise RuntimeError37()
    def string_value(this_49, x_426: 'str36', /) -> 'None':
        raise RuntimeError37()
    @property
    def parse_error_receiver(this_50, /) -> 'Union38[JsonParseErrorReceiver, None]':
        return None
class JsonSyntaxTree(metaclass = ABCMeta35):
    def produce(this_51, p_431: 'JsonProducer', /) -> 'None':
        raise RuntimeError37()
class JsonObject(JsonSyntaxTree):
    _properties_433: 'MappingProxyType44[str36, (Sequence45[JsonSyntaxTree])]'
    __slots__ = ('_properties_433',)
    def property_value_or_null(this_52, property_key_435: 'str36', /) -> 'Union38[JsonSyntaxTree, None]':
        "The JSON value tree associated with the given property key or null\nif there is no such value.\n\nThe properties map contains a list of sub-trees because JSON\nallows duplicate properties.  ECMA-404 \xa76 notes (emphasis added):\n\n> The JSON syntax does not impose any restrictions on the strings\n> used as names, **does not require that name strings be unique**,\n> and does not assign any significance to the ordering of\n> name/value pairs.\n\nWhen widely used JSON parsers need to relate a property key\nto a single value, they tend to prefer the last key/value pair\nfrom a JSON object.  For example:\n\nJS:\n\n    JSON.parse('{\"x\":\"first\",\"x\":\"last\"}').x === 'last'\n\nPython:\n\n    import json\n    json.loads('{\"x\":\"first\",\"x\":\"last\"}')['x'] == 'last'\n\nC#:\n\n   using System.Text.Json;\n\t\tJsonDocument d = JsonDocument.Parse(\n\t\t\t\"\"\"\n\t\t\t{\"x\":\"first\",\"x\":\"last\"}\n\t\t\t\"\"\"\n\t\t);\n\t\td.RootElement.GetProperty(\"x\").GetString() == \"last\"\n\nthis__52: JsonObject\n\npropertyKey__435: String\n"
        tree_list_437: 'Sequence45[JsonSyntaxTree]' = this_52._properties_433.get(property_key_435, ())
        last_index_438: 'int42' = _int_sub_1313(_len_1314(tree_list_437), 1)
        if last_index_438 >= 0:
            return _list_get_1315(tree_list_437, last_index_438)
        else:
            return None
    def property_value_or_bubble(this_53, property_key_440: 'str36', /) -> 'JsonSyntaxTree':
        t_1142: 'Union38[JsonSyntaxTree, None]' = this_53.property_value_or_null(property_key_440)
        if t_1142 is None:
            raise RuntimeError37()
        else:
            return t_1142
    def produce(this_54, p_443: 'JsonProducer', /) -> 'None':
        p_443.start_object()
        def fn_1163(k_445: 'str36', vs_446: 'Sequence45[JsonSyntaxTree]', /) -> 'None':
            this_1144: 'Sequence45[JsonSyntaxTree]' = vs_446
            n_1146: 'int42' = _len_1314(this_1144)
            i_1147: 'int42' = 0
            while i_1147 < n_1146:
                el_1148: 'JsonSyntaxTree' = _list_get_1315(this_1144, i_1147)
                i_1147 = _int_add_1316(i_1147, 1)
                v_447: 'JsonSyntaxTree' = el_1148
                p_443.object_key(k_445)
                v_447.produce(p_443)
        _mapped_for_each_1317(this_54._properties_433, fn_1163)
        p_443.end_object()
    def __init__(this_212, /, properties: 'MappingProxyType44[str36, (Sequence45[JsonSyntaxTree])]') -> None:
        this_212._properties_433 = properties
    @property
    def properties(this_900, /) -> 'MappingProxyType44[str36, (Sequence45[JsonSyntaxTree])]':
        return this_900._properties_433
class JsonArray(JsonSyntaxTree):
    _elements_450: 'Sequence45[JsonSyntaxTree]'
    __slots__ = ('_elements_450',)
    def produce(this_55, p_452: 'JsonProducer', /) -> 'None':
        p_452.start_array()
        this_1149: 'Sequence45[JsonSyntaxTree]' = this_55._elements_450
        n_1151: 'int42' = _len_1314(this_1149)
        i_1152: 'int42' = 0
        while i_1152 < n_1151:
            el_1153: 'JsonSyntaxTree' = _list_get_1315(this_1149, i_1152)
            i_1152 = _int_add_1316(i_1152, 1)
            v_454: 'JsonSyntaxTree' = el_1153
            v_454.produce(p_452)
        p_452.end_array()
    def __init__(this_218, /, elements: 'Sequence45[JsonSyntaxTree]') -> None:
        this_218._elements_450 = elements
    @property
    def elements(this_903, /) -> 'Sequence45[JsonSyntaxTree]':
        return this_903._elements_450
class JsonBoolean(JsonSyntaxTree):
    _content_457: 'bool41'
    __slots__ = ('_content_457',)
    def produce(this_56, p_459: 'JsonProducer', /) -> 'None':
        p_459.boolean_value(this_56._content_457)
    def __init__(this_222, /, content: 'bool41') -> None:
        this_222._content_457 = content
    @property
    def content(this_906, /) -> 'bool41':
        return this_906._content_457
class JsonNull(JsonSyntaxTree):
    __slots__ = ()
    def produce(this_57, p_464: 'JsonProducer', /) -> 'None':
        p_464.null_value()
    def __init__(this_225, /) -> None:
        pass
class JsonString(JsonSyntaxTree):
    _content_467: 'str36'
    __slots__ = ('_content_467',)
    def produce(this_58, p_469: 'JsonProducer', /) -> 'None':
        p_469.string_value(this_58._content_467)
    def __init__(this_228, /, content_472: 'str36') -> None:
        this_228._content_467 = content_472
    @property
    def content(this_909, /) -> 'str36':
        return this_909._content_467
class JsonNumeric(JsonSyntaxTree, metaclass = ABCMeta35):
    def as_json_numeric_token(this_59, /) -> 'str36':
        raise RuntimeError37()
    def as_int32(this_60, /) -> 'int42':
        raise RuntimeError37()
    def as_int64(this_61, /) -> '_int64':
        raise RuntimeError37()
    def as_float64(this_62, /) -> 'float43':
        raise RuntimeError37()
class JsonInt32(JsonNumeric):
    _content_481: 'int42'
    __slots__ = ('_content_481',)
    def produce(this_63, p_483: 'JsonProducer', /) -> 'None':
        p_483.int32_value(this_63._content_481)
    def as_json_numeric_token(this_64, /) -> 'str36':
        return _int_to_string_1318(this_64._content_481)
    def as_int32(this_65, /) -> 'int42':
        return this_65._content_481
    def as_int32_safe(this_66, /) -> 'int42':
        return this_66._content_481
    def as_int64(this_67, /) -> '_int64':
        return this_67.as_int64_safe()
    def as_int64_safe(this_68, /) -> '_int64':
        return this_68._content_481
    def as_float64(this_69, /) -> 'float43':
        return this_69.as_float64_safe()
    def as_float64_safe(this_70, /) -> 'float43':
        return float(this_70._content_481)
    def __init__(this_235, /, content_500: 'int42') -> None:
        this_235._content_481 = content_500
    @property
    def content(this_912, /) -> 'int42':
        return this_912._content_481
class JsonInt64(JsonNumeric):
    _content_501: '_int64'
    __slots__ = ('_content_501',)
    def produce(this_71, p_503: 'JsonProducer', /) -> 'None':
        p_503.int64_value(this_71._content_501)
    def as_json_numeric_token(this_72, /) -> 'str36':
        return _int_to_string_1318(this_72._content_501)
    def as_int32(this_73, /) -> 'int42':
        return _int64_to_int32_1321(this_73._content_501)
    def as_int64(this_74, /) -> '_int64':
        return this_74._content_501
    def as_int64_safe(this_75, /) -> '_int64':
        return this_75._content_501
    def as_float64(this_76, /) -> 'float43':
        return _int64_to_float64_1322(this_76._content_501)
    def __init__(this_245, /, content_516: '_int64') -> None:
        this_245._content_501 = content_516
    @property
    def content(this_915, /) -> '_int64':
        return this_915._content_501
class JsonFloat64(JsonNumeric):
    _content_517: 'float43'
    __slots__ = ('_content_517',)
    def produce(this_77, p_519: 'JsonProducer', /) -> 'None':
        p_519.float64_value(this_77._content_517)
    def as_json_numeric_token(this_78, /) -> 'str36':
        return _float64_to_string_1323(this_78._content_517)
    def as_int32(this_79, /) -> 'int42':
        return _float64_to_int_1324(this_79._content_517)
    def as_int64(this_80, /) -> '_int64':
        return _float64_to_int64_1325(this_80._content_517)
    def as_float64(this_81, /) -> 'float43':
        return this_81._content_517
    def as_float64_safe(this_82, /) -> 'float43':
        return this_82._content_517
    def __init__(this_253, /, content_532: 'float43') -> None:
        this_253._content_517 = content_532
    @property
    def content(this_918, /) -> 'float43':
        return this_918._content_517
class JsonNumericToken(JsonNumeric):
    _content_533: 'str36'
    __slots__ = ('_content_533',)
    def produce(this_83, p_535: 'JsonProducer', /) -> 'None':
        p_535.numeric_token_value(this_83._content_533)
    def as_json_numeric_token(this_84, /) -> 'str36':
        return this_84._content_533
    def as_int32(this_85, /) -> 'int42':
        try:
            return _string_to_int32_1326(this_85._content_533)
        except Exception46:
            t_1161: 'float43' = _string_to_float64_1327(this_85._content_533)
            return _float64_to_int_1324(t_1161)
    def as_int64(this_86, /) -> '_int64':
        try:
            return _string_to_int64_1328(this_86._content_533)
        except Exception46:
            t_1160: 'float43' = _string_to_float64_1327(this_86._content_533)
            return _float64_to_int64_1325(t_1160)
    def as_float64(this_87, /) -> 'float43':
        return _string_to_float64_1327(this_87._content_533)
    def __init__(this_261, /, content_546: 'str36') -> None:
        this_261._content_533 = content_546
    @property
    def content(this_921, /) -> 'str36':
        return this_921._content_533
class JsonTextProducer(JsonProducer):
    _interchange_context_547: 'InterchangeContext'
    _buffer_548: 'list14[str36]'
    _stack_549: 'MutableSequence47[int42]'
    _well_formed_550: 'bool41'
    __slots__ = ('_interchange_context_547', '_buffer_548', '_stack_549', '_well_formed_550')
    def __init__(this_88, /, interchange_context: 'Union38[InterchangeContext, None]' = None) -> None:
        _interchange_context: 'Union38[InterchangeContext, None]' = interchange_context
        interchange_context_552: 'InterchangeContext'
        if _interchange_context is None:
            interchange_context_552 = NullInterchangeContext.instance
        else:
            interchange_context_552 = _interchange_context
        this_88._interchange_context_547 = interchange_context_552
        t_889: 'list14[str36]' = ['']
        this_88._buffer_548 = t_889
        t_888: 'MutableSequence47[int42]' = _list_1330()
        this_88._stack_549 = t_888
        this_88._stack_549.append(5)
        this_88._well_formed_550 = True
    def _state_554(this_89, /) -> 'int42':
        return _list_get_or_1332(this_89._stack_549, _int_sub_1313(_len_1314(this_89._stack_549), 1), -1)
    def _before_value_556(this_90, /) -> 'None':
        current_state_558: 'int42' = this_90._state_554()
        if current_state_558 == 3:
            _list_builder_set_1333(this_90._stack_549, _int_sub_1313(_len_1314(this_90._stack_549), 1), 4)
        elif current_state_558 == 4:
            this_90._buffer_548.append(',')
        elif current_state_558 == 1:
            _list_builder_set_1333(this_90._stack_549, _int_sub_1313(_len_1314(this_90._stack_549), 1), 2)
        elif current_state_558 == 5:
            _list_builder_set_1333(this_90._stack_549, _int_sub_1313(_len_1314(this_90._stack_549), 1), 6)
        else:
            t_1135: 'bool41'
            if current_state_558 == 6:
                t_1135 = True
            else:
                t_1135 = current_state_558 == 2
            if t_1135:
                this_90._well_formed_550 = False
    def start_object(this_91, /) -> 'None':
        this_91._before_value_556()
        this_91._buffer_548.append('{')
        this_91._stack_549.append(0)
    def end_object(this_92, /) -> 'None':
        this_92._buffer_548.append('}')
        current_state_563: 'int42' = this_92._state_554()
        t_1133: 'bool41'
        if 0 == current_state_563:
            t_1133 = True
        else:
            t_1133 = 2 == current_state_563
        if t_1133:
            this_92._stack_549.pop()
        else:
            this_92._well_formed_550 = False
    def object_key(this_93, key_565: 'str36', /) -> 'None':
        current_state_567: 'int42' = this_93._state_554()
        if not current_state_567 == 0:
            if current_state_567 == 2:
                this_93._buffer_548.append(',')
            else:
                this_93._well_formed_550 = False
        _encode_json_string(key_565, this_93._buffer_548)
        this_93._buffer_548.append(':')
        if current_state_567 >= 0:
            _list_builder_set_1333(this_93._stack_549, _int_sub_1313(_len_1314(this_93._stack_549), 1), 1)
    def start_array(this_94, /) -> 'None':
        this_94._before_value_556()
        this_94._buffer_548.append('[')
        this_94._stack_549.append(3)
    def end_array(this_95, /) -> 'None':
        this_95._buffer_548.append(']')
        current_state_572: 'int42' = this_95._state_554()
        t_1131: 'bool41'
        if 3 == current_state_572:
            t_1131 = True
        else:
            t_1131 = 4 == current_state_572
        if t_1131:
            this_95._stack_549.pop()
        else:
            this_95._well_formed_550 = False
    def null_value(this_96, /) -> 'None':
        this_96._before_value_556()
        this_96._buffer_548.append('null')
    def boolean_value(this_97, x_576: 'bool41', /) -> 'None':
        t_1129: 'str36'
        this_97._before_value_556()
        t_1130: 'list14[str36]' = this_97._buffer_548
        if x_576:
            t_1129 = 'true'
        else:
            t_1129 = 'false'
        t_1130.append(t_1129)
    def int32_value(this_98, x_579: 'int42', /) -> 'None':
        this_98._before_value_556()
        this_98._buffer_548.append(_int_to_string_1318(x_579))
    def int64_value(this_99, x_582: '_int64', /) -> 'None':
        this_99._before_value_556()
        this_99._buffer_548.append(_int_to_string_1318(x_582))
    def float64_value(this_100, x_585: 'float43', /) -> 'None':
        this_100._before_value_556()
        this_100._buffer_548.append(_float64_to_string_1323(x_585))
    def numeric_token_value(this_101, x_588: 'str36', /) -> 'None':
        this_101._before_value_556()
        this_101._buffer_548.append(x_588)
    def string_value(this_102, x_591: 'str36', /) -> 'None':
        this_102._before_value_556()
        _encode_json_string(x_591, this_102._buffer_548)
    def to_json_string(this_103, /) -> 'str36':
        t_1126: 'bool41'
        if this_103._well_formed_550:
            if _len_1314(this_103._stack_549) == 1:
                t_1126 = this_103._state_554() == 6
            else:
                t_1126 = False
        else:
            t_1126 = False
        if t_1126:
            return ''.join(this_103._buffer_548)
        else:
            raise RuntimeError37()
    @property
    def interchange_context(this_931, /) -> 'InterchangeContext':
        return this_931._interchange_context_547
class JsonParseErrorReceiver(metaclass = ABCMeta35):
    def explain_json_error(this_110, explanation_611: 'str36', /) -> 'None':
        raise RuntimeError37()
class JsonSyntaxTreeProducer(JsonProducer, JsonParseErrorReceiver):
    _stack_613: 'MutableSequence47[(MutableSequence47[JsonSyntaxTree])]'
    _error_614: 'Union38[str36, None]'
    __slots__ = ('_stack_613', '_error_614')
    @property
    def interchange_context(this_111, /) -> 'InterchangeContext':
        return NullInterchangeContext.instance
    def __init__(this_112, /) -> None:
        t_882: 'MutableSequence47[(MutableSequence47[JsonSyntaxTree])]' = _list_1330()
        this_112._stack_613 = t_882
        this_112._stack_613.append(_list_1330())
        this_112._error_614 = None
    def _store_value_619(this_113, v_620: 'JsonSyntaxTree', /) -> 'None':
        if not (not this_113._stack_613):
            _list_get_1315(this_113._stack_613, _int_sub_1313(_len_1314(this_113._stack_613), 1)).append(v_620)
    def start_object(this_114, /) -> 'None':
        this_114._stack_613.append(_list_1330())
    def end_object(this_115, /) -> 'None':
        with Label48() as fn_625:
            if not this_115._stack_613:
                fn_625.break_()
            ls_626: 'MutableSequence47[JsonSyntaxTree]' = this_115._stack_613.pop()
            m_627: 'Dict49[str36, (Sequence45[JsonSyntaxTree])]' = {}
            multis_628: 'Union38[(Dict49[str36, (MutableSequence47[JsonSyntaxTree])]), None]' = None
            i_629: 'int42' = 0
            n_630: 'int42' = _len_1314(ls_626) & -2
            while i_629 < n_630:
                postfix_return_34: 'int42' = i_629
                i_629 = _int_add_1316(postfix_return_34, 1)
                key_tree_631: 'JsonSyntaxTree' = _list_get_1315(ls_626, postfix_return_34)
                if not isinstance50(key_tree_631, JsonString):
                    break
                t_1122: 'JsonString' = cast_by_type51(key_tree_631, JsonString)
                key_632: 'str36' = t_1122.content
                postfix_return_35: 'int42' = i_629
                i_629 = _int_add_1316(postfix_return_35, 1)
                value_633: 'JsonSyntaxTree' = _list_get_1315(ls_626, postfix_return_35)
                if _mapped_has_1339(m_627, key_632):
                    if multis_628 is None:
                        multis_628 = {}
                    mb_634: 'Dict49[str36, (MutableSequence47[JsonSyntaxTree])]'
                    if multis_628 is None:
                        raise RuntimeError37()
                    else:
                        mb_634 = multis_628
                    if not _mapped_has_1339(mb_634, key_632):
                        t_1124: 'Sequence45[JsonSyntaxTree]' = m_627[key_632]
                        _map_builder_set_1341(mb_634, key_632, _list_1330(t_1124))
                    t_1125: 'MutableSequence47[JsonSyntaxTree]' = mb_634[key_632]
                    t_1125.append(value_633)
                else:
                    _map_builder_set_1341(m_627, key_632, (value_633,))
            multis_635: 'Union38[(Dict49[str36, (MutableSequence47[JsonSyntaxTree])]), None]' = multis_628
            if not multis_635 is None:
                def fn_1162(k_636: 'str36', vs_637: 'MutableSequence47[JsonSyntaxTree]', /) -> 'None':
                    _map_builder_set_1341(m_627, k_636, _tuple_1342(vs_637))
                _mapped_for_each_1317(multis_635, fn_1162)
            this_115._store_value_619(JsonObject(_mapped_to_map_1343(m_627)))
    def object_key(this_116, key_639: 'str36', /) -> 'None':
        this_116._store_value_619(JsonString(key_639))
    def start_array(this_117, /) -> 'None':
        this_117._stack_613.append(_list_1330())
    def end_array(this_118, /) -> 'None':
        with Label48() as fn_644:
            if not this_118._stack_613:
                fn_644.break_()
            ls_645: 'MutableSequence47[JsonSyntaxTree]' = this_118._stack_613.pop()
            this_118._store_value_619(JsonArray(_tuple_1342(ls_645)))
    def null_value(this_119, /) -> 'None':
        this_119._store_value_619(JsonNull())
    def boolean_value(this_120, x_649: 'bool41', /) -> 'None':
        this_120._store_value_619(JsonBoolean(x_649))
    def int32_value(this_121, x_652: 'int42', /) -> 'None':
        this_121._store_value_619(JsonInt32(x_652))
    def int64_value(this_122, x_655: '_int64', /) -> 'None':
        this_122._store_value_619(JsonInt64(x_655))
    def float64_value(this_123, x_658: 'float43', /) -> 'None':
        this_123._store_value_619(JsonFloat64(x_658))
    def numeric_token_value(this_124, x_661: 'str36', /) -> 'None':
        this_124._store_value_619(JsonNumericToken(x_661))
    def string_value(this_125, x_664: 'str36', /) -> 'None':
        this_125._store_value_619(JsonString(x_664))
    def to_json_syntax_tree(this_126, /) -> 'JsonSyntaxTree':
        t_1118: 'bool41'
        if not _len_1314(this_126._stack_613) == 1:
            t_1118 = True
        else:
            t_1118 = not this_126._error_614 is None
        if t_1118:
            raise RuntimeError37()
        ls_668: 'MutableSequence47[JsonSyntaxTree]' = _list_get_1315(this_126._stack_613, 0)
        if not _len_1314(ls_668) == 1:
            raise RuntimeError37()
        return _list_get_1315(ls_668, 0)
    @property
    def json_error(this_127, /) -> 'Union38[str36, None]':
        return this_127._error_614
    @property
    def parse_error_receiver(this_128, /) -> 'Union38[JsonParseErrorReceiver, None]':
        return this_128
    @property
    def parse_error_receiver_safe(this_129, /) -> 'JsonParseErrorReceiver':
        return this_129
    def explain_json_error(this_130, error_676: 'str36', /) -> 'None':
        this_130._error_614 = error_676
def _parse_json_value(source_text_695: 'str36', i_696: 'int42', out_697: 'JsonProducer', /) -> 'int42':
    return_315: 'int42'
    with Label48() as fn_698:
        i_696 = _skip_json_spaces(source_text_695, i_696)
        if not len1(source_text_695) > i_696:
            _expected_token_error(source_text_695, i_696, out_697, 'JSON value')
            return_315 = -1
            fn_698.break_()
        subject_956: 'int42' = _string_get_1345(source_text_695, i_696)
        if subject_956 == 123:
            return _parse_json_object(source_text_695, i_696, out_697)
        elif subject_956 == 91:
            return _parse_json_array(source_text_695, i_696, out_697)
        elif subject_956 == 34:
            return _parse_json_string(source_text_695, i_696, out_697)
        else:
            t_1007: 'bool41'
            if subject_956 == 116:
                t_1007 = True
            else:
                t_1007 = subject_956 == 102
            if t_1007:
                return _parse_json_boolean(source_text_695, i_696, out_697)
            elif subject_956 == 110:
                return _parse_json_null(source_text_695, i_696, out_697)
            else:
                return _parse_json_number(source_text_695, i_696, out_697)
    return return_315
T_167 = TypeVar53('T_167', bound = Any52, covariant = True)
class JsonAdapter(Generic54[T_167], metaclass = ABCMeta35):
    def encode_to_json(this_168, x_790: 'T_167', p_791: 'JsonProducer', /) -> 'None':
        raise RuntimeError37()
    def decode_from_json(this_169, t_794: 'JsonSyntaxTree', ic_795: 'InterchangeContext', /) -> 'T_167':
        raise RuntimeError37()
class _BooleanJsonAdapter(JsonAdapter['bool41']):
    __slots__ = ()
    def encode_to_json(this_171, x_798: 'bool41', p_799: 'JsonProducer', /) -> 'None':
        p_799.boolean_value(x_798)
    def decode_from_json(this_172, t_802: 'JsonSyntaxTree', ic_803: 'InterchangeContext', /) -> 'bool41':
        t_1001: 'JsonBoolean' = cast_by_type51(t_802, JsonBoolean)
        return t_1001.content
    def __init__(this_328, /) -> None:
        pass
class _Float64JsonAdapter(JsonAdapter['float43']):
    __slots__ = ()
    def encode_to_json(this_174, x_808: 'float43', p_809: 'JsonProducer', /) -> 'None':
        p_809.float64_value(x_808)
    def decode_from_json(this_175, t_812: 'JsonSyntaxTree', ic_813: 'InterchangeContext', /) -> 'float43':
        t_1000: 'JsonNumeric' = cast_by_type51(t_812, JsonNumeric)
        return t_1000.as_float64()
    def __init__(this_333, /) -> None:
        pass
class _Int32JsonAdapter(JsonAdapter['int42']):
    __slots__ = ()
    def encode_to_json(this_177, x_818: 'int42', p_819: 'JsonProducer', /) -> 'None':
        p_819.int32_value(x_818)
    def decode_from_json(this_178, t_822: 'JsonSyntaxTree', ic_823: 'InterchangeContext', /) -> 'int42':
        t_999: 'JsonNumeric' = cast_by_type51(t_822, JsonNumeric)
        return t_999.as_int32()
    def __init__(this_338, /) -> None:
        pass
class _Int64JsonAdapter(JsonAdapter['_int64']):
    __slots__ = ()
    def encode_to_json(this_180, x_828: '_int64', p_829: 'JsonProducer', /) -> 'None':
        p_829.int64_value(x_828)
    def decode_from_json(this_181, t_832: 'JsonSyntaxTree', ic_833: 'InterchangeContext', /) -> '_int64':
        t_998: 'JsonNumeric' = cast_by_type51(t_832, JsonNumeric)
        return t_998.as_int64()
    def __init__(this_343, /) -> None:
        pass
class _StringJsonAdapter(JsonAdapter['str36']):
    __slots__ = ()
    def encode_to_json(this_183, x_838: 'str36', p_839: 'JsonProducer', /) -> 'None':
        p_839.string_value(x_838)
    def decode_from_json(this_184, t_842: 'JsonSyntaxTree', ic_843: 'InterchangeContext', /) -> 'str36':
        t_997: 'JsonString' = cast_by_type51(t_842, JsonString)
        return t_997.content
    def __init__(this_348, /) -> None:
        pass
T_186 = TypeVar53('T_186', bound = Any52)
class _ListJsonAdapter(JsonAdapter['Sequence45[T_186]']):
    _adapter_for_t_847: 'JsonAdapter[T_186]'
    __slots__ = ('_adapter_for_t_847',)
    def encode_to_json(this_187, x_849: 'Sequence45[T_186]', p_850: 'JsonProducer', /) -> 'None':
        p_850.start_array()
        this_1154: 'Sequence45[T_186]' = x_849
        n_1156: 'int42' = _len_1314(this_1154)
        i_1157: 'int42' = 0
        while i_1157 < n_1156:
            el_1158: 'T_186' = _list_get_1315(this_1154, i_1157)
            i_1157 = _int_add_1316(i_1157, 1)
            el_852: 'T_186' = el_1158
            this_187._adapter_for_t_847.encode_to_json(el_852, p_850)
        p_850.end_array()
    def decode_from_json(this_188, t_854: 'JsonSyntaxTree', ic_855: 'InterchangeContext', /) -> 'Sequence45[T_186]':
        b_857: 'MutableSequence47[T_186]' = _list_1330()
        t_996: 'JsonArray' = cast_by_type51(t_854, JsonArray)
        elements_858: 'Sequence45[JsonSyntaxTree]' = t_996.elements
        n_859: 'int42' = _len_1314(elements_858)
        i_860: 'int42' = 0
        while i_860 < n_859:
            el_861: 'JsonSyntaxTree' = _list_get_1315(elements_858, i_860)
            i_860 = _int_add_1316(i_860, 1)
            t_1159: 'T_186' = this_188._adapter_for_t_847.decode_from_json(el_861, ic_855)
            b_857.append(t_1159)
        return _tuple_1342(b_857)
    def __init__(this_353, /, adapter_for_t: 'JsonAdapter[T_186]') -> None:
        this_353._adapter_for_t_847 = adapter_for_t
T_190 = TypeVar53('T_190', bound = Any52)
class OrNullJsonAdapter(JsonAdapter['Union38[T_190, None]']):
    _adapter_for_t_866: 'JsonAdapter[T_190]'
    __slots__ = ('_adapter_for_t_866',)
    def encode_to_json(this_191, x_868: 'Union38[T_190, None]', p_869: 'JsonProducer', /) -> 'None':
        if x_868 is None:
            p_869.null_value()
        else:
            x_986: 'T_190' = x_868
            this_191._adapter_for_t_866.encode_to_json(x_986, p_869)
    def decode_from_json(this_192, t_872: 'JsonSyntaxTree', ic_873: 'InterchangeContext', /) -> 'Union38[T_190, None]':
        if isinstance50(t_872, JsonNull):
            return None
        else:
            return this_192._adapter_for_t_866.decode_from_json(t_872, ic_873)
    def __init__(this_359, /, adapter_for_t_876: 'JsonAdapter[T_190]') -> None:
        this_359._adapter_for_t_866 = adapter_for_t_876
_hex_digits: 'Sequence45[str36]' = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
def _encode_hex4(cp_603: 'int42', buffer_604: 'list14[str36]', /) -> 'None':
    b0_606: 'int42' = _int_div_1346(cp_603, 4096) & 15
    b1_607: 'int42' = _int_div_1346(cp_603, 256) & 15
    b2_608: 'int42' = _int_div_1346(cp_603, 16) & 15
    b3_609: 'int42' = cp_603 & 15
    buffer_604.append(_list_get_1315(_hex_digits, b0_606))
    buffer_604.append(_list_get_1315(_hex_digits, b1_607))
    buffer_604.append(_list_get_1315(_hex_digits, b2_608))
    buffer_604.append(_list_get_1315(_hex_digits, b3_609))
def _encode_json_string(x_595: 'str36', buffer_596: 'list14[str36]', /) -> 'None':
    buffer_596.append('"')
    i_598: 'int42' = 0
    emitted_599: 'int42' = i_598
    while len1(x_595) > i_598:
        cp_600: 'int42' = _string_get_1345(x_595, i_598)
        replacement_601: 'str36'
        if cp_600 == 8:
            replacement_601 = '\\b'
        elif cp_600 == 9:
            replacement_601 = '\\t'
        elif cp_600 == 10:
            replacement_601 = '\\n'
        elif cp_600 == 12:
            replacement_601 = '\\f'
        elif cp_600 == 13:
            replacement_601 = '\\r'
        elif cp_600 == 34:
            replacement_601 = '\\"'
        elif cp_600 == 92:
            replacement_601 = '\\\\'
        else:
            t_1138: 'bool41'
            if cp_600 < 32:
                t_1138 = True
            elif 55296 <= cp_600:
                t_1138 = cp_600 <= 57343
            else:
                t_1138 = False
            if t_1138:
                replacement_601 = '\\u'
            else:
                replacement_601 = ''
        next_i_602: 'int42' = _string_next_1347(x_595, i_598)
        if not replacement_601 == '':
            buffer_596.append(x_595[emitted_599 : i_598])
            buffer_596.append(replacement_601)
            if replacement_601 == '\\u':
                _encode_hex4(cp_600, buffer_596)
            emitted_599 = next_i_602
        i_598 = next_i_602
    buffer_596.append(x_595[emitted_599 : i_598])
    buffer_596.append('"')
def _store_json_error(out_684: 'JsonProducer', explanation_685: 'str36', /) -> 'None':
    subject_879: 'Union38[JsonParseErrorReceiver, None]' = out_684.parse_error_receiver
    if not subject_879 is None:
        subject_879.explain_json_error(explanation_685)
def _expected_token_error(source_text_678: 'str36', i_679: 'int42', out_680: 'JsonProducer', short_explanation_681: 'str36', /) -> 'None':
    gotten_683: 'str36'
    if len1(source_text_678) > i_679:
        gotten_683 = _str_cat_1349('`', source_text_678[i_679 : _len_1314(source_text_678)], '`')
    else:
        gotten_683 = 'end-of-file'
    _store_json_error(out_680, _str_cat_1349('Expected ', short_explanation_681, ', but got ', gotten_683))
def _skip_json_spaces(source_text_692: 'str36', i_693: 'int42', /) -> 'int42':
    while len1(source_text_692) > i_693:
        subject_940: 'int42' = _string_get_1345(source_text_692, i_693)
        t_1112: 'bool41'
        if subject_940 == 9:
            t_1112 = True
        elif subject_940 == 10:
            t_1112 = True
        elif subject_940 == 13:
            t_1112 = True
        else:
            t_1112 = subject_940 == 32
        if not t_1112:
            break
        i_693 = _string_next_1347(source_text_692, i_693)
    return i_693
def _decode_hex_unsigned(source_text_733: 'str36', start_734: 'int42', limit_735: 'int42', /) -> 'int42':
    return_320: 'int42'
    with Label48() as fn_736:
        n_737: 'int42' = 0
        i_738: 'int42' = start_734
        while i_738 - limit_735 < 0:
            cp_739: 'int42' = _string_get_1345(source_text_733, i_738)
            digit_740: 'int42'
            t_1104: 'bool41'
            if 48 <= cp_739:
                t_1104 = cp_739 <= 57
            else:
                t_1104 = False
            if t_1104:
                digit_740 = _int_sub_1313(cp_739, 48)
            else:
                t_1107: 'bool41'
                if 65 <= cp_739:
                    t_1107 = cp_739 <= 70
                else:
                    t_1107 = False
                if t_1107:
                    digit_740 = _int_add_1316(_int_sub_1313(cp_739, 65), 10)
                else:
                    t_1109: 'bool41'
                    if 97 <= cp_739:
                        t_1109 = cp_739 <= 102
                    else:
                        t_1109 = False
                    if t_1109:
                        digit_740 = _int_add_1316(_int_sub_1313(cp_739, 97), 10)
                    else:
                        return_320 = -1
                        fn_736.break_()
            n_737 = _int_add_1316(_int_mul_1352(n_737, 16), digit_740)
            i_738 = _string_next_1347(source_text_733, i_738)
        return n_737
    return return_320
def _parse_json_string_to(source_text_717: 'str36', i_718: 'int42', sb_719: 'list14[str36]', err_out_720: 'JsonProducer', /) -> 'int42':
    return_319: 'int42'
    with Label48() as fn_721:
        t_1081: 'bool41'
        if not len1(source_text_717) > i_718:
            t_1081 = True
        else:
            t_1081 = not _string_get_1345(source_text_717, i_718) == 34
        if t_1081:
            _expected_token_error(source_text_717, i_718, err_out_720, '"')
            return_319 = -1
            fn_721.break_()
        i_718 = _string_next_1347(source_text_717, i_718)
        lead_surrogate_722: 'int42' = -1
        consumed_723: 'int42' = i_718
        while len1(source_text_717) > i_718:
            t_1088: 'int42'
            cp_724: 'int42' = _string_get_1345(source_text_717, i_718)
            if cp_724 == 34:
                break
            i_next_725: 'int42' = _string_next_1347(source_text_717, i_718)
            end_726: 'int42' = _len_1314(source_text_717)
            need_to_flush_727: 'bool41' = False
            if not cp_724 == 92:
                t_1088 = cp_724
            else:
                need_to_flush_727 = True
                if not len1(source_text_717) > i_next_725:
                    _expected_token_error(source_text_717, i_next_725, err_out_720, 'escape sequence')
                    return_319 = -1
                    fn_721.break_()
                esc0_729: 'int42' = _string_get_1345(source_text_717, i_next_725)
                i_next_725 = _string_next_1347(source_text_717, i_next_725)
                t_1083: 'bool41'
                if esc0_729 == 34:
                    t_1083 = True
                elif esc0_729 == 92:
                    t_1083 = True
                else:
                    t_1083 = esc0_729 == 47
                if t_1083:
                    t_1088 = esc0_729
                elif esc0_729 == 98:
                    t_1088 = 8
                elif esc0_729 == 102:
                    t_1088 = 12
                elif esc0_729 == 110:
                    t_1088 = 10
                elif esc0_729 == 114:
                    t_1088 = 13
                elif esc0_729 == 116:
                    t_1088 = 9
                elif esc0_729 == 117:
                    hex_730: 'int42'
                    if _string_has_at_least_1353(source_text_717, i_next_725, end_726, 4):
                        start_hex_731: 'int42' = i_next_725
                        i_next_725 = _string_next_1347(source_text_717, i_next_725)
                        i_next_725 = _string_next_1347(source_text_717, i_next_725)
                        i_next_725 = _string_next_1347(source_text_717, i_next_725)
                        i_next_725 = _string_next_1347(source_text_717, i_next_725)
                        hex_730 = _decode_hex_unsigned(source_text_717, start_hex_731, i_next_725)
                    else:
                        hex_730 = -1
                    if hex_730 < 0:
                        _expected_token_error(source_text_717, i_next_725, err_out_720, 'four hex digits')
                        return_319 = -1
                        fn_721.break_()
                    t_1088 = hex_730
                else:
                    _expected_token_error(source_text_717, i_next_725, err_out_720, 'escape sequence')
                    return_319 = -1
                    fn_721.break_()
            decoded_cp_728: 'int42' = t_1088
            if lead_surrogate_722 >= 0:
                need_to_flush_727 = True
                lead_732: 'int42' = lead_surrogate_722
                t_1096: 'bool41'
                if 56320 <= decoded_cp_728:
                    t_1096 = decoded_cp_728 <= 57343
                else:
                    t_1096 = False
                if t_1096:
                    lead_surrogate_722 = -1
                    decoded_cp_728 = _int_add_1316(65536, _int_mul_1352(_int_sub_1313(lead_732, 55296), 1024) | _int_sub_1313(decoded_cp_728, 56320))
            else:
                t_1098: 'bool41'
                if 55296 <= decoded_cp_728:
                    t_1098 = decoded_cp_728 <= 56319
                else:
                    t_1098 = False
                if t_1098:
                    need_to_flush_727 = True
            if need_to_flush_727:
                sb_719.append(source_text_717[consumed_723 : i_718])
                if lead_surrogate_722 >= 0:
                    sb_719.append(string_from_code_point55(lead_surrogate_722))
                t_1100: 'bool41'
                if 55296 <= decoded_cp_728:
                    t_1100 = decoded_cp_728 <= 56319
                else:
                    t_1100 = False
                if t_1100:
                    lead_surrogate_722 = decoded_cp_728
                else:
                    lead_surrogate_722 = -1
                    sb_719.append(string_from_code_point55(decoded_cp_728))
                consumed_723 = i_next_725
            i_718 = i_next_725
        t_1102: 'bool41'
        if not len1(source_text_717) > i_718:
            t_1102 = True
        else:
            t_1102 = not _string_get_1345(source_text_717, i_718) == 34
        if t_1102:
            _expected_token_error(source_text_717, i_718, err_out_720, '"')
            return -1
        else:
            if lead_surrogate_722 >= 0:
                sb_719.append(string_from_code_point55(lead_surrogate_722))
            else:
                sb_719.append(source_text_717[consumed_723 : i_718])
            i_718 = _string_next_1347(source_text_717, i_718)
            return i_718
    return return_319
def _parse_json_object(source_text_699: 'str36', i_700: 'int42', out_701: 'JsonProducer', /) -> 'int42':
    return_316: 'int42'
    with Label48() as fn_702:
        t_1065: 'bool41'
        if not len1(source_text_699) > i_700:
            t_1065 = True
        else:
            t_1065 = not _string_get_1345(source_text_699, i_700) == 123
        if t_1065:
            _expected_token_error(source_text_699, i_700, out_701, "'{'")
            return_316 = -1
            fn_702.break_()
        out_701.start_object()
        i_700 = _skip_json_spaces(source_text_699, _string_next_1347(source_text_699, i_700))
        t_1067: 'bool41'
        if len1(source_text_699) > i_700:
            t_1067 = not _string_get_1345(source_text_699, i_700) == 125
        else:
            t_1067 = False
        if t_1067:
            while True:
                key_buffer_703: 'list14[str36]' = ['']
                after_key_704: 'int42' = _parse_json_string_to(source_text_699, i_700, key_buffer_703, out_701)
                if not after_key_704 >= 0:
                    return_316 = -1
                    fn_702.break_()
                out_701.object_key(''.join(key_buffer_703))
                t_1071: 'int42' = _require_string_index_1356(after_key_704)
                i_700 = _skip_json_spaces(source_text_699, t_1071)
                t_1072: 'bool41'
                if len1(source_text_699) > i_700:
                    t_1072 = _string_get_1345(source_text_699, i_700) == 58
                else:
                    t_1072 = False
                if t_1072:
                    i_700 = _string_next_1347(source_text_699, i_700)
                    after_property_value_705: 'int42' = _parse_json_value(source_text_699, i_700, out_701)
                    if not after_property_value_705 >= 0:
                        return_316 = -1
                        fn_702.break_()
                    t_1076: 'int42' = _require_string_index_1356(after_property_value_705)
                    i_700 = t_1076
                else:
                    _expected_token_error(source_text_699, i_700, out_701, "':'")
                    return_316 = -1
                    fn_702.break_()
                i_700 = _skip_json_spaces(source_text_699, i_700)
                t_1077: 'bool41'
                if len1(source_text_699) > i_700:
                    t_1077 = _string_get_1345(source_text_699, i_700) == 44
                else:
                    t_1077 = False
                if t_1077:
                    i_700 = _skip_json_spaces(source_text_699, _string_next_1347(source_text_699, i_700))
                else:
                    break
        t_1079: 'bool41'
        if len1(source_text_699) > i_700:
            t_1079 = _string_get_1345(source_text_699, i_700) == 125
        else:
            t_1079 = False
        if t_1079:
            out_701.end_object()
            return _string_next_1347(source_text_699, i_700)
        else:
            _expected_token_error(source_text_699, i_700, out_701, "'}'")
            return -1
    return return_316
def _parse_json_array(source_text_706: 'str36', i_707: 'int42', out_708: 'JsonProducer', /) -> 'int42':
    return_317: 'int42'
    with Label48() as fn_709:
        t_1054: 'bool41'
        if not len1(source_text_706) > i_707:
            t_1054 = True
        else:
            t_1054 = not _string_get_1345(source_text_706, i_707) == 91
        if t_1054:
            _expected_token_error(source_text_706, i_707, out_708, "'['")
            return_317 = -1
            fn_709.break_()
        out_708.start_array()
        i_707 = _skip_json_spaces(source_text_706, _string_next_1347(source_text_706, i_707))
        t_1056: 'bool41'
        if len1(source_text_706) > i_707:
            t_1056 = not _string_get_1345(source_text_706, i_707) == 93
        else:
            t_1056 = False
        if t_1056:
            while True:
                after_element_value_710: 'int42' = _parse_json_value(source_text_706, i_707, out_708)
                if not after_element_value_710 >= 0:
                    return_317 = -1
                    fn_709.break_()
                t_1060: 'int42' = _require_string_index_1356(after_element_value_710)
                i_707 = t_1060
                i_707 = _skip_json_spaces(source_text_706, i_707)
                t_1061: 'bool41'
                if len1(source_text_706) > i_707:
                    t_1061 = _string_get_1345(source_text_706, i_707) == 44
                else:
                    t_1061 = False
                if t_1061:
                    i_707 = _skip_json_spaces(source_text_706, _string_next_1347(source_text_706, i_707))
                else:
                    break
        t_1063: 'bool41'
        if len1(source_text_706) > i_707:
            t_1063 = _string_get_1345(source_text_706, i_707) == 93
        else:
            t_1063 = False
        if t_1063:
            out_708.end_array()
            return _string_next_1347(source_text_706, i_707)
        else:
            _expected_token_error(source_text_706, i_707, out_708, "']'")
            return -1
    return return_317
def _parse_json_string(source_text_711: 'str36', i_712: 'int42', out_713: 'JsonProducer', /) -> 'int42':
    sb_715: 'list14[str36]' = ['']
    after_716: 'int42' = _parse_json_string_to(source_text_711, i_712, sb_715, out_713)
    if after_716 >= 0:
        out_713.string_value(''.join(sb_715))
    return after_716
def _after_substring(string_755: 'str36', in_string_756: 'int42', substring_757: 'str36', /) -> 'int42':
    return_323: 'int42'
    with Label48() as fn_758:
        i_759: 'int42' = in_string_756
        j_760: 'int42' = 0
        while len1(substring_757) > j_760:
            if not len1(string_755) > i_759:
                return_323 = -1
                fn_758.break_()
            if not _string_get_1345(string_755, i_759) == _string_get_1345(substring_757, j_760):
                return_323 = -1
                fn_758.break_()
            i_759 = _string_next_1347(string_755, i_759)
            j_760 = _string_next_1347(substring_757, j_760)
        return i_759
    return return_323
def _parse_json_boolean(source_text_741: 'str36', i_742: 'int42', out_743: 'JsonProducer', /) -> 'int42':
    return_321: 'int42'
    with Label48() as fn_744:
        ch0_745: 'int42'
        if len1(source_text_741) > i_742:
            ch0_745 = _string_get_1345(source_text_741, i_742)
        else:
            ch0_745 = 0
        end_746: 'int42' = _len_1314(source_text_741)
        keyword_747: 'Union38[str36, None]'
        n_748: 'int42'
        if ch0_745 == 102:
            keyword_747 = 'false'
            n_748 = 5
        elif ch0_745 == 116:
            keyword_747 = 'true'
            n_748 = 4
        else:
            keyword_747 = None
            n_748 = 0
        if not keyword_747 is None:
            keyword_982: 'str36' = keyword_747
            if _string_has_at_least_1353(source_text_741, i_742, end_746, n_748):
                after_749: 'int42' = _after_substring(source_text_741, i_742, keyword_982)
                if after_749 >= 0:
                    return_321 = _require_string_index_1356(after_749)
                    out_743.boolean_value(n_748 == 4)
                    fn_744.break_()
        _expected_token_error(source_text_741, i_742, out_743, '`false` or `true`')
        return -1
    return return_321
def _parse_json_null(source_text_750: 'str36', i_751: 'int42', out_752: 'JsonProducer', /) -> 'int42':
    return_322: 'int42'
    with Label48() as fn_753:
        after_754: 'int42' = _after_substring(source_text_750, i_751, 'null')
        if after_754 >= 0:
            return_322 = _require_string_index_1356(after_754)
            out_752.null_value()
            fn_753.break_()
        _expected_token_error(source_text_750, i_751, out_752, '`null`')
        return -1
    return return_322
def _parse_json_number(source_text_761: 'str36', i_762: 'int42', out_763: 'JsonProducer', /) -> 'int42':
    return_324: 'int42'
    with Label48() as fn_764:
        is_negative_765: 'bool41' = False
        start_of_number_766: 'int42' = i_762
        t_1009: 'bool41'
        if len1(source_text_761) > i_762:
            t_1009 = _string_get_1345(source_text_761, i_762) == 45
        else:
            t_1009 = False
        if t_1009:
            is_negative_765 = True
            i_762 = _string_next_1347(source_text_761, i_762)
        digit0_767: 'int42'
        if len1(source_text_761) > i_762:
            digit0_767 = _string_get_1345(source_text_761, i_762)
        else:
            digit0_767 = -1
        t_1013: 'bool41'
        if digit0_767 < 48:
            t_1013 = True
        else:
            t_1013 = 57 < digit0_767
        if t_1013:
            error_768: 'str36'
            t_1015: 'bool41'
            if not is_negative_765:
                t_1015 = not digit0_767 == 46
            else:
                t_1015 = False
            if t_1015:
                error_768 = 'JSON value'
            else:
                error_768 = 'digit'
            _expected_token_error(source_text_761, i_762, out_763, error_768)
            return_324 = -1
            fn_764.break_()
        i_762 = _string_next_1347(source_text_761, i_762)
        n_digits_769: 'int42' = 1
        tentative_float64_770: 'float43' = float(_int_sub_1313(digit0_767, 48))
        tentative_int64_771: '_int64' = _int_sub_1313(digit0_767, 48)
        overflow_int64_772: 'bool41' = False
        if not 48 == digit0_767:
            while len1(source_text_761) > i_762:
                possible_digit_773: 'int42' = _string_get_1345(source_text_761, i_762)
                t_1018: 'bool41'
                if 48 <= possible_digit_773:
                    t_1018 = possible_digit_773 <= 57
                else:
                    t_1018 = False
                if t_1018:
                    i_762 = _string_next_1347(source_text_761, i_762)
                    n_digits_769 = _int_add_1316(n_digits_769, 1)
                    next_digit_774: 'int42' = _int_sub_1313(possible_digit_773, 48)
                    tentative_float64_770 = tentative_float64_770 * 10.0 + float(next_digit_774)
                    old_int64_775: '_int64' = tentative_int64_771
                    tentative_int64_771 = _int64_add_1357(_int64_mul_1358(tentative_int64_771, 10), next_digit_774)
                    if tentative_int64_771 < old_int64_775:
                        t_1020: 'bool41'
                        if _int64_sub_1360(-9223372036854775808, old_int64_775) == _int64_negate_1361(next_digit_774):
                            if is_negative_765:
                                t_1020 = old_int64_775 > 0
                            else:
                                t_1020 = False
                        else:
                            t_1020 = False
                        if not t_1020:
                            overflow_int64_772 = True
                else:
                    break
        n_digits_after_point_776: 'int42' = 0
        t_1023: 'bool41'
        if len1(source_text_761) > i_762:
            t_1023 = 46 == _string_get_1345(source_text_761, i_762)
        else:
            t_1023 = False
        if t_1023:
            i_762 = _string_next_1347(source_text_761, i_762)
            after_point_777: 'int42' = i_762
            while len1(source_text_761) > i_762:
                possible_digit_778: 'int42' = _string_get_1345(source_text_761, i_762)
                t_1025: 'bool41'
                if 48 <= possible_digit_778:
                    t_1025 = possible_digit_778 <= 57
                else:
                    t_1025 = False
                if t_1025:
                    i_762 = _string_next_1347(source_text_761, i_762)
                    n_digits_769 = _int_add_1316(n_digits_769, 1)
                    n_digits_after_point_776 = _int_add_1316(n_digits_after_point_776, 1)
                    tentative_float64_770 = tentative_float64_770 * 10.0 + float(_int_sub_1313(possible_digit_778, 48))
                else:
                    break
            if i_762 == after_point_777:
                _expected_token_error(source_text_761, i_762, out_763, 'digit')
                return_324 = -1
                fn_764.break_()
        n_exponent_digits_779: 'int42' = 0
        t_1027: 'bool41'
        if len1(source_text_761) > i_762:
            t_1027 = 101 == _string_get_1345(source_text_761, i_762) | 32
        else:
            t_1027 = False
        if t_1027:
            i_762 = _string_next_1347(source_text_761, i_762)
            if not len1(source_text_761) > i_762:
                _expected_token_error(source_text_761, i_762, out_763, 'sign or digit')
                return_324 = -1
                fn_764.break_()
            after_e_780: 'int42' = _string_get_1345(source_text_761, i_762)
            t_1029: 'bool41'
            if after_e_780 == 43:
                t_1029 = True
            else:
                t_1029 = after_e_780 == 45
            if t_1029:
                i_762 = _string_next_1347(source_text_761, i_762)
            while len1(source_text_761) > i_762:
                possible_digit_781: 'int42' = _string_get_1345(source_text_761, i_762)
                t_1031: 'bool41'
                if 48 <= possible_digit_781:
                    t_1031 = possible_digit_781 <= 57
                else:
                    t_1031 = False
                if t_1031:
                    i_762 = _string_next_1347(source_text_761, i_762)
                    n_exponent_digits_779 = _int_add_1316(n_exponent_digits_779, 1)
                else:
                    break
            if n_exponent_digits_779 == 0:
                _expected_token_error(source_text_761, i_762, out_763, 'exponent digit')
                return_324 = -1
                fn_764.break_()
        after_exponent_782: 'int42' = i_762
        t_1033: 'bool41'
        if n_exponent_digits_779 == 0:
            if n_digits_after_point_776 == 0:
                t_1033 = not overflow_int64_772
            else:
                t_1033 = False
        else:
            t_1033 = False
        if t_1033:
            value_783: '_int64'
            if is_negative_765:
                value_783 = _int64_negate_1361(tentative_int64_771)
            else:
                value_783 = tentative_int64_771
            t_1037: 'bool41'
            if -2147483648 <= value_783:
                t_1037 = value_783 <= 2147483647
            else:
                t_1037 = False
            if t_1037:
                out_763.int32_value(_int64_to_int32_unsafe_1363(value_783))
            else:
                out_763.int64_value(value_783)
            return_324 = i_762
            fn_764.break_()
        numeric_token_string_784: 'str36' = source_text_761[start_of_number_766 : i_762]
        double_value_785: 'float43' = nan56
        t_1039: 'bool41'
        if not n_exponent_digits_779 == 0:
            t_1039 = True
        else:
            t_1039 = not n_digits_after_point_776 == 0
        if t_1039:
            try:
                double_value_785 = _string_to_float64_1327(numeric_token_string_784)
            except Exception46:
                pass
        t_1041: 'bool41'
        if not _float_eq_1364(double_value_785, -inf57):
            if not _float_eq_1364(double_value_785, inf57):
                t_1041 = not _float_eq_1364(double_value_785, nan56)
            else:
                t_1041 = False
        else:
            t_1041 = False
        if t_1041:
            out_763.float64_value(double_value_785)
        else:
            out_763.numeric_token_value(numeric_token_string_784)
        return i_762
    return return_324
def parse_json_to_producer(source_text_687: 'str36', out_688: 'JsonProducer', /) -> 'None':
    i_690: 'int42' = 0
    after_value_691: 'int42' = _parse_json_value(source_text_687, i_690, out_688)
    if after_value_691 >= 0:
        t_1004: 'int42' = _require_string_index_1356(after_value_691)
        i_690 = _skip_json_spaces(source_text_687, t_1004)
        t_1005: 'bool41'
        if len1(source_text_687) > i_690:
            t_1005 = not out_688.parse_error_receiver is None
        else:
            t_1005 = False
        if t_1005:
            _store_json_error(out_688, _str_cat_1349('Extraneous JSON `', source_text_687[i_690 : _len_1314(source_text_687)], '`'))
def parse_json(source_text_786: 'str36', /) -> 'JsonSyntaxTree':
    p_788: 'JsonSyntaxTreeProducer' = JsonSyntaxTreeProducer()
    parse_json_to_producer(source_text_786, p_788)
    return p_788.to_json_syntax_tree()
def boolean_json_adapter() -> 'JsonAdapter[bool41]':
    return _BooleanJsonAdapter()
def float64_json_adapter() -> 'JsonAdapter[float43]':
    return _Float64JsonAdapter()
def int32_json_adapter() -> 'JsonAdapter[int42]':
    return _Int32JsonAdapter()
def int64_json_adapter() -> 'JsonAdapter[_int64]':
    return _Int64JsonAdapter()
def string_json_adapter() -> 'JsonAdapter[str36]':
    return _StringJsonAdapter()
T_189 = TypeVar53('T_189', bound = Any52)
def list_json_adapter(adapter_for_t_864: 'JsonAdapter[T_189]', /) -> 'JsonAdapter[(Sequence45[T_189])]':
    return _ListJsonAdapter(adapter_for_t_864)
