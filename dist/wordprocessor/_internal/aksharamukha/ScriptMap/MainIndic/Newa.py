# -*- coding: utf-8 -*-

# Script Mapping for Devanagari

VowelMap =  [
            '\U00011400',
            '\U00011401',
            '\U00011402',
            '\U00011403',
            '\U00011404',
            '\U00011405',
            '\U00011406',
            '\U00011407',
            '\U00011408',
            '\U00011409',
            '\U0001140A',
            '\U0001140B',
            '\U0001140C',
            '\U0001140D',
            ]

SouthVowelMap = [
                '\U0001140A\u02BD',
                '\U0001140C\u02BD',
                ]

ModernVowelMap = [
                '\U0001140A\u02BD',
                 '\U00011401\u02BD',
                 ]

SinhalaVowelMap = [
                '\U0001140A\u02BD',
                  ]

VowelSignMap =  [
                '\U00011435',
                '\U00011436',
                '\U00011437',
                '\U00011438',
                '\U00011439',
                '\U0001143A',
                '\U0001143B',
                '\U0001143C',
                '\U0001143D',
                '\U0001143E',
                '\U0001143F',
                '\U00011440',
                '\U00011441',
                ]

SouthVowelSignMap = [
                    '\U0001143E\u02BD',
                    '\U00011440\u02BD',
                    ]

ModernVowelSignMap =[
                    '\U0001143E\u02BD',
                    '\U00011436\u02BD']

SinhalaVowelSignMap = [
                    '\U0001143E\u02BD',
                      ]

AyogavahaMap = [
               '\U00011443',
               '\U00011444',
               '\U00011445'
               ]

ViramaMap =  [
             '\U00011442'
             ]

ConsonantMap =  [
                '\U0001140E',
                '\U0001140F',
                '\U00011410',
                '\U00011411',
                '\U00011412',

                '\U00011414',
                '\U00011415',
                '\U00011416',
                '\U00011417',
                '\U00011418',

                '\U0001141A',
                '\U0001141B',
                '\U0001141C',
                '\U0001141D',
                '\U0001141E',

                '\U0001141F',
                '\U00011420',
                '\U00011421',
                '\U00011422',
                '\U00011423',

                '\U00011425',
                '\U00011426',
                '\U00011427',
                '\U00011428',
                '\U00011429',

                '\U0001142B',
                '\U0001142C',
                '\U0001142E',
                '\U00011430',

                '\U00011431',
                '\U00011432',
                '\U00011433',
                '\U00011434'
                ]

SouthConsonantMap = [
                    '𑐮𑑆',
                    '𑐲𑑆',
                    '𑐬𑑆',
                    '𑐣𑑆'
                    ]

NuktaConsonantMap =  [
                     '\U0001140E\U00011446',
                     '\U0001140F\U00011446',
                     '\U00011410\U00011446',
                     '\U00011416\U00011446',
                     '\U0001141C\U00011446',
                     '\U0001141D\U00011446',
                     '\U00011426\U00011446',
                     '\U0001142B\U00011446'
                     ]

SinhalaConsonantMap =[
                     '\U00011443𑐐\u02BD',
                     '\U00011443𑐖\u02BD',
                     '\U00011443𑐜\u02BD',
                     '\U00011443𑐡\u02BD',
                     '\U00011443𑐧\u02BD',
                      ]

NuktaMap = [
           '\U00011446'
           ]

OmMap = [
        '\U00011449'
        ]

SignMap =[
         '\U00011447',
         '\U0001144B',
         '\U0001144C'
         ]

Aytham =[AyogavahaMap[2]+'\u02BD']

NumeralMap = [
             '\U00011450',
             '\U00011451',
             '\U00011452',
             '\U00011453',
             '\U00011454',
             '\U00011455',
             '\U00011456',
             '\U00011457',
             '\U00011458',
             '\U00011459'
             ]

from ... import GeneralMap as GM

import os
GM.add_additional_chars(dict([(charlist, globals()[charlist]) for charlist in GM.CharmapLists]),
                        os.path.splitext(__file__)[0].split(os.path.sep)[-1])