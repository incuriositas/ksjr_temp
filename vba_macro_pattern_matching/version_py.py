import json
from oletools.olevba import VBA_Parser, TYPE_OLE, TYPE_OpenXML, TYPE_Word2003_XML, TYPE_MHTML
import argparse
import os

import warning_window as ww

import urllib.request

parser = argparse.ArgumentParser("VBA 매크로 PATH")
parser.add_argument('--check_file', required=True, help="악성매크로를 확인할 파일입력")
args = parser.parse_args()
check_file = args.check_file

filedata = open(check_file, 'rb').read()
vbaparser = VBA_Parser(check_file, data=filedata)
results = vbaparser.analyze_macros()

if vbaparser.detect_vba_macros():
    if not results:
        ww.run("NO VBA macros found", "VBA악성매크로가 확인되지 않았습니다.")

    else:
        with urllib.request.urlopen('https://raw.githubusercontent.com/hgrgr/INFINITY_VBA/main/blacklist.json') as response:
            black_list = json.loads(response.read())

        for(filename, stream_path, vba_filename, vba_code) in vbaparser.extract_macros():
            for key in black_list.keys():
                if key in vba_code.lower():
                    ww.run('VBA macros found', black_list[key])
                    break
else:
    ww.run("NO VBA macros found", "VBA악성매크로가 확인되지 않았습니다.")
