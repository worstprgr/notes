#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import io
import platform
import pathlib
from PIL import Image, ImageDraw, ImageFont
import constants as const


class ThumbnailCreator:
    def __init__(
            self,
            file_name: str,
            bg_color: tuple[int, int, int],
            brightness=0,
            file_path=None,
            debug=False
    ) -> None:
        """
        Creates an image with a desired background color and a text in front of it.

        :param file_name: custom file name
        :param bg_color: RGB values for the background
        :param brightness: Brightness value between 0 - 100 for the background color (Default: 0)
        :param file_path: (optional) a custom file path.
                It also creates the whole path, if it's not existing (Default: ./output/)
        :param debug: True -> Only show image, don't export ist. False -> Only export image, don't show it.
        """
        # basic init
        self.current_os = platform.system()
        self.BASE_DIR: str = '.'
        self.EXPORT_DIR: str = 'thumbnails'
        self.size_px: tuple[int, int] = (1920, 1080)
        self.file_ex: str = 'jpg'
        self.xy_mid: tuple[int, int] = (round(self.size_px[0] / 2), round(self.size_px[1] / 2))
        self.font = 'verdana.ttf'
        self.ttf_path = self._get_font_by_os(self.font)

        # params
        self.file_name = file_name
        self.bg_color = self._brightness(bg_color, brightness)
        self.file_path = self._custom_path(file_path)
        self.debug = debug

        # create folders (if exist)
        self._create_folders(self.file_path)

    def create_text(
            self,
            top_text: str,
            top_color: tuple[int, int, int],
            top_size: int,
            bot_text: str,
            bot_color: tuple[int, int, int],
            bot_size: int
    ) -> None:
        """
        Creates two lines of text. They can be configured separately by color and size

        :param top_text: the first text
        :param top_color: color of the first text
        :param top_size: font size of the first text (not sure if it's in pixel)
        :param bot_text: the second text (under the first one)
        :param bot_color: color of the second text
        :param bot_size: font size of the second text
        :return: None
        """
        def init_font(font_size: int) -> object:
            """
            Converts the font into an object and modifies the font size

            :param font_size:
            :return: PIL.ImageFont.FreeTypeFont
            """
            return ImageFont.truetype(self.ttf_path, size=font_size)

        bg_image = self._create_background()
        img = Image.open(bg_image)
        draw = ImageDraw.Draw(img)

        # top text
        draw.text(self.xy_mid, top_text, fill=top_color, anchor='md', font=init_font(top_size))
        # bottom text
        draw.text(self.xy_mid, bot_text, fill=bot_color, anchor='ma', font=init_font(bot_size))

        export_path = f'{self.file_path}/{self.file_name}.{self.file_ex}'

        if self.debug:
            img.show()
        else:
            img.save(export_path)

    def _create_background(self) -> bytes:
        """
        Creates an image in a solid color and saves it into the RAM as byte array

        :return: image/bytes
        """
        img = Image.new(mode="RGB", size=self.size_px, color=self.bg_color)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='jpeg')
        img_byte_arr = img_byte_arr
        return img_byte_arr

    def _custom_path(self, fp: str) -> str:
        """
        Switch, between a custom path or the default path.

        :param fp: path to your export directory
        :return: new path
        """
        if fp:
            return fp
        else:
            return f'{self.BASE_DIR}/{self.EXPORT_DIR}'

    def _create_folders(self, path: str) -> None:
        """
        Creates all folders (if they don't exist) along the whole path.
        E.g. 'foo/bar/waz' creates the whole structure.

        :param path: path structure
        :return: None
        """
        temp_folder: str = ''
        path: str = path.strip('/').strip('\\')

        if '\\' in path:
            path = path.replace('\\', '/')

        folders: list[str] = path.split('/')

        for index, x in enumerate(folders):
            if index == 0 or index == len(folders):
                temp_folder += x
            else:
                temp_folder += '/' + x
            self._create_folder(temp_folder)


    @staticmethod
    def _create_folder(folder: str) -> None:
        pathlib.Path(folder).mkdir(exist_ok=True)

    @staticmethod
    def _brightness(rgb_val: tuple[int, int, int], brightness=0) -> tuple[int, int, int]:
        """
        Calculate the brightness of an RGB value, relative to the highest RGB value.
        If an RGB value is zero, it will be ignored. So it doesn't introduce new
        color hues.

        :param rgb_val: Red, Green, Blue, Brightness
        :return: Modified Red, Green, Blue values
        """
        def add_offset(integer: int, _offset: int) -> int:
            """
            Check if a value is zero. If True, return zero.
            If False, add an offset to it.

            :param integer: one of the RBG values
            :param _offset: offset value
            :return: the new RGB value with or without an offset value
            """
            if integer == 0:
                return 0
            else:
                return integer + _offset

        # private constants
        R: int = rgb_val[0]
        G: int = rgb_val[1]
        B: int = rgb_val[2]

        # check boundaries
        if brightness < const.MIN_OFFSET or brightness > const.MAX_OFFSET:
            assert False, f'The brightness value can not be over {const.MAX_OFFSET} or below {const.MIN_OFFSET}.'

        # check for null in the brightness param
        if brightness == 0:
            return rgb_val
        else:
            # Find the highest value in all RGB constants
            highest_value = [R, G, B]
            highest_value.sort(reverse=True)

            # Calculate the delta between the highest RGB value and the max value constant
            # And calculate the 1% of it
            delta_rgb = const.MAX_RGB - highest_value[0]
            P1_delta_rgb = delta_rgb / 100

            # floor, so no "overflow" occurs, if it's hitting int: 100
            offset = math.floor(P1_delta_rgb * brightness)

            # Add the (1% * brightness value) to the RGB values
            out = (
                add_offset(R, offset),
                add_offset(G, offset),
                add_offset(B, offset)
            )
            return out

    def _get_font_by_os(self, font_file):
        """
        (Not fully implemented)
        Adapts the path to the OS font folder.

        :param font_file: name of the font file. With file extension.
        :return: full path to the font
        """
        if self.current_os == 'Windows':
            return f'C:/Windows/Fonts/{font_file}'
        elif self.current_os == 'Linux':
            assert False, 'Not implemented'
        else:
            assert False, 'Unknown Error'


if __name__ == '__main__':
    text_top = ''
    text_bot = ''

    tc = ThumbnailCreator('filename', const.C_DARK_BLUE_GREY, debug=True)
    tc.create_text(
        text_top,
        const.C_WHITE,
        180,
        text_bot,
        const.C_BLACK,
        80
    )
