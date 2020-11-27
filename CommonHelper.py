#!/usr/bin/env python
# coding=utf-8
__author__ = 'Xie_JianHua'

class CommonHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r', encoding='utf-8') as f:
            return f.read()


