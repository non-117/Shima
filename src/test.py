# -*- coding: utf-8 -*-
from shima import Icon

if __name__ == "__main__":
    #command = u"@non_117 face 7 base ffffff 778899 dot cheek 3 ★ めがね きぐるみ"
    command = u"@non_117 face 3 clear きぐるみ すぽーん"
    icon = Icon()
    print icon.gen_icon(command)