#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background



class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):  # level1bg images number
                    list_bg.append(Background(f'City1_Bg{i}', (0, 0)))
                return list_bg

