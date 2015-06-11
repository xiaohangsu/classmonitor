# -*- coding: utf-8 -*-
# Author: young
# Email: sujy_passion@qq.com
# Date: 2015-6-8
# Description: public function for operation


def checkItem(data, requireList):
    for item in requireList:
        if item not in data:
            return False
    return True

