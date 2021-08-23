#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import os

TOKEN = os.environ.get("tokenbot")
WORKERS = os.environ.get("workers", 32)
ADMIN_LIST = os.environ.get("admin", None)
OPEN_LOBBY = os.environ.get("open_lobby", True)
ENABLE_TRANSLATIONS = os.environ.get("enable_translations", False)
DEFAULT_GAMEMODE = os.environ.get("default_gamemode", "fast")
WAITING_TIME = os.environ.get("waiting_time", 120)
TIME_REMOVAL_AFTER_SKIP = os.environ.get("time_removal_after_skip", 0)
MIN_FAST_TURN_TIME = os.environ.get("min_fast_turn_time", 15)
MIN_PLAYERS = os.environ.get("min_players", 2)
