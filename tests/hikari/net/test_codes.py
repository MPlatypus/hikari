#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekokatt 2019-2020
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.

from hikari.net import codes


def test_str_HTTPStatusCode():
    assert str(codes.HTTPStatusCode.TOO_MANY_REQUESTS) == "429 Too Many Requests"
    assert str(codes.HTTPStatusCode.IM_A_TEAPOT) == "418 I'm a teapot"


def test_str_GatewayCloseCode():
    assert str(codes.GatewayCloseCode.ABNORMAL_CLOSURE) == "1006 Abnormal Closure"


def test_str_GatewayOpcode():
    assert str(codes.GatewayOpcode.HEARTBEAT_ACK) == "11 Heartbeat Ack"


def test_str_JSONErrorCode():
    assert (
        str(codes.JSONErrorCode.CANNOT_EDIT_A_MESSAGE_AUTHORED_BY_ANOTHER_USER)
        == "50005 Cannot Edit A Message Authored By Another User"
    )