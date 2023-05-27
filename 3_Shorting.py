import json
import os
import re
import argparse
import tqdm as tq
from shutil import move
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, help='未整理数据集目录', required=True)
parser.add_argument('--index', type=str, help='索引路径', required=True)
parser.add_argument('--dest', type=str, help='目标路径', required=True)
args = parser.parse_args()

source = str(args.source)
dest = str(args.dest)
index = str(args.index)

renameDict = {
    'none': 'none',
}

f = open(index, encoding='utf8')
data = json.load(f)
for k in tq.tqdm(data.keys()):
    try:
        text = data.get(k).get('ContentText')
        char_name = data.get(k).get('Speaker')
        if char_name is not None:
            char_name = char_name
        else:
            char_name = data.get(k).get('TitleText')
        path = data.get(k).get('VoiceName')
        wav_source = source + '/' + path
        wav_file = os.path.basename(path)
        if text is not None and char_name is not None:
            dest_dir = dest + '/' + char_name
            wav_path = dest_dir + '/' + wav_file
            if text is not None:
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                move(wav_source, wav_path)
    except:
        pass
f.close()