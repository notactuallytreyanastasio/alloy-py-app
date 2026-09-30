from builtins import str as str36, int as int42, RuntimeError as RuntimeError37
from typing import Union as Union38
from concurrent.futures import Future as Future69
from abc import ABCMeta as ABCMeta35, abstractmethod as abstractmethod40
from temper_core import std_net_send as std_net_send68
_std_net_send_1399 = std_net_send68
class NetRequest:
    '*NetRequest* is a builder class for an HTTP send.\nNone of the methods except *send* actually initiate anything.'
    _url_17: 'str36'
    _method_18: 'str36'
    _body_content_19: 'Union38[str36, None]'
    _body_mime_type_20: 'Union38[str36, None]'
    __slots__ = ('_url_17', '_method_18', '_body_content_19', '_body_mime_type_20')
    def post(this_0, content_22: 'str36', mime_type_23: 'str36', /) -> 'None':
        '*Post* switches the HTTP method to "POST" and makes sure that\na body with the given textual content and mime-type will be sent\nalong.\n\nthis__0: NetRequest\n\ncontent__22: String\n\nmimeType__23: String\n'
        this_0._method_18 = 'POST'
        this_0._body_content_19 = content_22
        t_43: 'Union38[str36, None]' = this_0._body_mime_type_20
        this_0._body_mime_type_20 = t_43
    def send(this_1, /) -> 'Future69[NetResponse]':
        '*Send* makes a best effort to actual send an HTTP method.\nBackends may or may not support all request features in which\ncase, send should return a broken promise.\n\nthis__1: NetRequest\n'
        return _std_net_send_1399(this_1._url_17, this_1._method_18, this_1._body_content_19, this_1._body_mime_type_20)
    def __init__(this, /, url: 'str36') -> None:
        this._url_17 = url
        this._method_18 = 'GET'
        this._body_content_19 = None
        this._body_mime_type_20 = None
class NetResponse(metaclass = ABCMeta35):
    @property
    @abstractmethod40
    def status(self) -> 'int42':
        pass
    @property
    @abstractmethod40
    def content_type(self) -> 'Union38[str36, None]':
        pass
    @property
    @abstractmethod40
    def body_content(self) -> 'Future69[(Union38[str36, None])]':
        pass
def _send_request(url_35: 'str36', method_36: 'str36', body_content_37: 'Union38[str36, None]', body_mime_type_38: 'Union38[str36, None]', /) -> 'Future69[NetResponse]':
    raise RuntimeError37()
