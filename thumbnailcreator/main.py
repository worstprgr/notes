#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
This script creates a 1920x1080 thumbnail for LinkedIn
"""
import createthumbnail
import constants as const

if __name__ == '__main__':
    text_top = 'Pitfall: PyCharm & Sys.path'
    text_bot = 'ModuleNotFoundError'
    file_name = 'pitfall_pycharm_syspath'

    tc = createthumbnail.ThumbnailCreator(file_name, const.C_DARK_BLUE_GREY, debug=False)
    tc.create_text(
        text_top,
        const.C_WHITE,
        110,
        text_bot,
        const.C_LIGHT_BLUE_GREY,
        65
    )
