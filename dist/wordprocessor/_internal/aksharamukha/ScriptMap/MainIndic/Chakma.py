# -*- coding: utf-8 -*-

# Script Mapping for Chakma

# Map oi to ai or something else.. check Chakma

VowelMap =  [
            '\U00011103',
            '\U00011103\U00011127',
            '\U00011103\U00011128',
            '\U00011103\U00011129',
            '\U00011103\U0001112A',
            '\U00011103\U0001112B',
            '𑄢𑄨\u02BD',
            '𑄢𑄩\u02BD',
            '𑅄𑄨\u02BD',
            '𑅄𑄩\u02BD',
            '\U00011103\U0001112C',
            '\U00011103\U00011130',
            '\U00011103\U0001112E',
            '\U00011103\U0001112F',
            ]

SouthVowelMap = [
                '\U00011103\U0001112C\u02BD',
                '\U00011103\U0001112E\u02BD',
                ]

ModernVowelMap = [
                 '\U00011103\U0001112C\U0001112C\u02BD',
                 '\U00011103\U00011145',
                 ]

SinhalaVowelMap = [
                  '\U00011103\U0001112C\u02BD',
                  ]

VowelSignMap =  [
                '\U00011127',
                '\U00011128',
                '\U00011129',
                '\U0001112A',
                '\U0001112B',
                '\U00011133\U00011122\U00011128\u02BD',
                '\U00011133\U00011122\U00011129\u02BD',
                '\U00011133𑅄𑄨\u02BD',
                '\U00011133𑅄𑄩\u02BD',
                '\U0001112C',
                '\U00011130',
                '\U0001112E',
                '\U0001112F',
                ]

SouthVowelSignMap = [
                    '\U0001112C\u02BD',
                    '\U0001112E\u02BD',
                    ]

ModernVowelSignMap =[
                    '\U0001112C\U0001112C',
                    '\U00011145']

SinhalaVowelSignMap = [
                      '\U0001112C\u02BD'
                      ]

AyogavahaMap = [
               '\U00011100',
               '\U00011101',
               '\U00011102'
               ]

ViramaMap =  [
             '\U00011134'
             ]

ConsonantMap =  [
                '\U00011107',
                '\U00011108',
                '\U00011109',
                '\U0001110A',
                '\U0001110B',

                '\U0001110C',
                '\U0001110D',
                '\U0001110E',
                '\U0001110F',
                '\U00011110',

                '\U00011111',
                '\U00011112',
                '\U00011113',
                '\U00011114',
                '\U00011115',

                '\U00011116',
                '\U00011117',
                '\U00011118',
                '\U00011119',
                '\U0001111A',

                '\U0001111B',
                '\U0001111C',
                '\U0001111D',
                '\U0001111E',
                '\U0001111F',

                '\U00011121',
                '\U00011122',
                '\U00011123',
                '\U00011124',

                '\U00011125\u02BD',
                '\U00011125\u02BD',
                '\U00011125',
                '\U00011126'
                ]

SouthConsonantMap = [
                    '\U00011123\u02BD',
                    '\U00011123\u02BD',
                    '\U00011122\u02BD',
                    '\U0001111A\u02BD'
                    ]

NuktaConsonantMap =  [
                     '\U00011107\u02BD',
                     '\U00011108\u02BD',
                     '\U00011109\u02BD',
                     '\U0001110E\u02BD',
                     '\U00011113\u02BD',
                     '\U00011114\u02BD',
                     '\U0001111C\u02BD',
                     '\U00011120',
                     ]

SinhalaConsonantMap =[
                     '\U00011100\U00011109\u02BD',
                     '\U00011100\U0001110E\u02BD',
                     '\U00011100\U00011113\u02BD',
                     '\U00011100\U00011118\u02BD',
                     '\U00011100\U0001111D\u02BD',
                      ]

NuktaMap = [
           '\u02BD\u02BD\u02BD\u02BD'
           ]

OmMap = [
        '\U00011103\U0001112E\U00011100'
        ]

SignMap =[
         "'",
         '\U00011141',
         '\U00011142'
         ]

Aytham =[AyogavahaMap[2]+'\u02BC']

NumeralMap = [
             '\U00011136',
             '\U00011137',
             '\U00011138',
             '\U00011139',
             '\U0001113A',
             '\U0001113B',
             '\U0001113C',
             '\U0001113D',
             '\U0001113E',
             '\U0001113F'
             ]

from ... import GeneralMap as GM

import os
GM.add_additional_chars(dict([(charlist, globals()[charlist]) for charlist in GM.CharmapLists]),
                        os.path.splitext(__file__)[0].split(os.path.sep)[-1])