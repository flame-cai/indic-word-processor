# -*- coding: utf-8 -*-

# Script Mapping for Devanagari

VowelMap =  [
            '\U00011900',
            '\U00011901',
            '\U00011902',
            '\U00011903',
            '\U00011904',
            '\U00011905',
            '\U00011927\U00011933',
            '\U00011927\U00011934',
            '\U00011928\U00011933',
            '\U00011928\U00011934',
            '\U00011906',
            '\U00011906\U00011935',
            '\U00011909',
            '\U00011900\U00011904\u02BD',
            ]

SouthVowelMap = [
                '\U00011906\u02BD',
                '\U00011909\u02BD',
                ]

ModernVowelMap = [
                 '\U00011906\u02BD',
                 '\U00011901\u02BD',
                 ]

SinhalaVowelMap = [
                  '\U00011906\u02BD',
                  ]

VowelSignMap =  [
                '\U00011930',
                '\U00011931',
                '\U00011932',
                '\U00011933',
                '\U00011934',
                '\U00011942\U00011933\u02BD',
                '\U00011942\U00011934\u02BD',
                '\U0001193E\U00011928\U00011933\u02BD',
                '\U0001193E\U00011928\U00011934\u02BD',
                '\U00011935',
                '\U00011937',
                '\U00011938',
                '\U00011904\u02BD',
                ]

SouthVowelSignMap = [
                    '\U00011935\u02BD',
                    '\U00011938\u02BD',
                    ]

ModernVowelSignMap =[
                    '\U00011935\u02BD',
                    '\U00011930\u02BD']

SinhalaVowelSignMap = [
                      '\U00011935\u02BD'
                      ]

AyogavahaMap = [
               '\U0001193C',
               '\U0001193B',
               '\U0001192D\U0001193D\u02BD'
               ]

ViramaMap =  [
             '\U0001193D'
             ]

ConsonantMap =  [
                '\U0001190C',
                '\U0001190D',
                '\U0001190E',
                '\U0001190F',
                '\U00011910',

                '\U00011911',
                '\U00011912',
                '\U00011913',
                '\U00011913\u02BD',
                '\U00011915',

                '\U00011916',
                '\U00011916\u02BD',
                '\U00011918',
                '\U00011919',
                '\U0001191A',

                '\U0001191B',
                '\U0001191C',
                '\U0001191D',
                '\U0001191E',
                '\U0001191F',

                '\U00011920',
                '\U00011921',
                '\U00011922',
                '\U00011923',
                '\U00011924',

                '\U00011925',
                '\U00011927',
                '\U00011928',
                '\U00011929',

                '\U0001192A',
                '\U0001192B',
                '\U0001192C',
                '\U0001192D'
                ]

SouthConsonantMap = [
                    '\U0001192E',
                    '\U0001192E\U00011943',
                    '\U00011927\U00011943',
                    '\U0001191F\U00011943'
                    ]

NuktaConsonantMap =  [
                     '\U0001190C\U00011943',
                     '\U0001190D\U00011943',
                     '\U0001190E\U00011943',
                     '\U0001192F',
                     '\U00011918\U00011943',
                     '\U00011919\U00011943',
                     '\U00011921\U00011943',
                     '\U00011925\U00011943'
                     ]

SinhalaConsonantMap =[
                     '\U0001193F\U0001190E\u02BD',
                     '\U0001193F\U00011913\u02BD',
                     '\U0001193F\U00011918\u02BD',
                     '\U0001193F\U0001191D\u02BD',
                     '\U0001193F\U00011922\u02BD',
                      ]

NuktaMap = [
           '\U00011943'
           ]

OmMap = [
        '\U00011909\U0001193C'
        ]

SignMap =[
         '\u02BD\u02BD\u02BD',
         '\U00011946\u02BD',
         '\U00011946'
         ]

Aytham =[AyogavahaMap[2]+'\u02BD']


NumeralMap = [
             '\U00011950',
             '\U00011951',
             '\U00011952',
             '\U00011953',
             '\U00011954',
             '\U00011955',
             '\U00011956',
             '\U00011957',
             '\U00011958',
             '\U00011959',
             ]

from ... import GeneralMap as GM

import os
GM.add_additional_chars(dict([(charlist, globals()[charlist]) for charlist in GM.CharmapLists]),
                        os.path.splitext(__file__)[0].split(os.path.sep)[-1])