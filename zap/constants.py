#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2020 Srevin Saju

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

-----------------------------
This file is part of Zap AppImage Package Manager
"""
from colorama import Fore


MIRRORS = {
    "0": [
        "https://srevinsaju.me/get-appimage/{}/core.json",
        "Stable AppImage Database. Updated hourly"],
    "1": [
        "http://zapacman.pythonanywhere.com/core/{}",
        "Live AppImage Database. Update on request (beta)"]}

URL_SHOWCASE = "https://srevinsaju.me/get-appimage/{}/"
YES_RESPONSES = ("yes", "y", "yea", "yup", "ye")

ZAP_PATH_RC_PATCH = \
    """# ========================
# auto generated by Zap AppImage Package Manager: do not remove!
# Add the path to ZAP bin to PATH environment variable
export ZAP_PATH={path_to_bin}
export PATH=$PATH:$ZAP_PATH
# ========================"""

COMMAND_WRAPPER = \
    """#!/bin/sh
{path_to_appimage} "$@" """

COLORS = {
    'g': Fore.GREEN,
    'rst': Fore.RESET,
    'y': Fore.YELLOW,
    'r': Fore.RED
}

BUG_TRACKER = "https://github.com/srevinsaju/zap/issues"
