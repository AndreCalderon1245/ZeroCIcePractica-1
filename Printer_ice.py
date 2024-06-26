# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `Printer.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Example
_M_Example = Ice.openModule('Example')
__name__ = 'Example'

_M_Example._t_Printer = IcePy.defineValue('::Example::Printer', Ice.Value, -1, (), False, True, None, ())

if 'PrinterPrx' not in _M_Example.__dict__:
    _M_Example.PrinterPrx = Ice.createTempClass()
    class PrinterPrx(Ice.ObjectPrx):

        def write(self, message, context=None):
            return _M_Example.Printer._op_write.invoke(self, ((message, ), context))

        def writeAsync(self, message, context=None):
            return _M_Example.Printer._op_write.invokeAsync(self, ((message, ), context))

        def begin_write(self, message, _response=None, _ex=None, _sent=None, context=None):
            return _M_Example.Printer._op_write.begin(self, ((message, ), _response, _ex, _sent, context))

        def end_write(self, _r):
            return _M_Example.Printer._op_write.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Example.PrinterPrx.ice_checkedCast(proxy, '::Example::Printer', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Example.PrinterPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Example::Printer'
    _M_Example._t_PrinterPrx = IcePy.defineProxy('::Example::Printer', PrinterPrx)

    _M_Example.PrinterPrx = PrinterPrx
    del PrinterPrx

    _M_Example.Printer = Ice.createTempClass()
    class Printer(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Example::Printer', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Example::Printer'

        @staticmethod
        def ice_staticId():
            return '::Example::Printer'

        def write(self, message, current=None):
            raise NotImplementedError("servant method 'write' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Example._t_PrinterDisp)

        __repr__ = __str__

    _M_Example._t_PrinterDisp = IcePy.defineClass('::Example::Printer', Printer, (), None, ())
    Printer._ice_type = _M_Example._t_PrinterDisp

    Printer._op_write = IcePy.Operation('write', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_Example.Printer = Printer
    del Printer

# End of module Example
