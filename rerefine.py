#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys
from pathlib import Path
from string import digits, ascii_letters
import re

re_txt = re.compile(r"^[a-zA-Z\n0-9]+$")

tr = {
        r"[\(]": "\n",
        r"[’_,\.♀♂: \-–'\)!]": "",
        "[ấàẩậặầāäâẫắạăãáằả]": "a",
        "[Þß]": "b",
        "[čç]": "c",
        "ð": "d",
        r"[éęèềễēếểėệæêë]": "e",
        r"[ģ]": "g",
        "[ìĩīïịîí]" : "i",
        "[ķ]" : "k",
        "[łļ]": "l",
        "[ņñ]": "n",
        r"[óõốớởỗòờộọợơồōôœøö]": "o",
        "[šś]": "s",
        "[ửūúüứữừụũưùûủ]" : "u",
        "[ÿỹýỳ]": "y",
        r"[žżŻŽ]": "z",
        "[ÅÂÁẨĀ]": "A",
        "[ČÇ]": "C",
        r"[ÐĐ]": "D",
        "[ĒÉÆÈ]": "E",
        "[Ģ]": "G",
        "[ÎÏĪ]": "I",
        "[Ķ]": "K",
        "[ŁĻ]": "L",
        "[Ņ]": "N",
        "[ŌØÖÓǪÔ]": "O",
        "[ŠŚ]": "S",
        "[ÚŪ]": "U",
        "[Ý]": "Y"
        }
a = "".join(list(tr.keys()) + list(digits) + list(ascii_letters))

err_char = set()

def parse_file(f):
    if "katakana" in f.name:
        return
    print(f, file=sys.stderr)
    for l in f.read_text().splitlines():
        l = l.strip()
        if not l:
            continue
        if not re_txt.match(l):
            for k, v in tr.items():
                l = re.sub(k, v, l)
            if not re_txt.match(l):
                print("err", l, file=sys.stderr)
                err_char.update([c for c in l if c not in a])
                continue
        print(l)

def main():

    if len(sys.argv) > 1:
        for fn in sys.argv[1:]:
            fp = Path(fn)
            if fp.is_file():
                parse_file(fp)
            elif fp.is_dir():
                for f in fp.glob("**/*.txt"):
                    parse_file(f)
    else:
        for f in Path('.').glob("**/*.txt"):
            parse_file(f)

    print(*err_char, file=sys.stderr)

if __name__ == "__main__":
    main()

