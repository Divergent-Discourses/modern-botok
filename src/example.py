# https://github.com/OpenPecha/Botok
# https://github.com/Esukhia/botok-data

from botok import WordTokenizer
from botok.config import Config
from pathlib import Path
import sys

def get_tokens(wt, text):
    tokens = wt.tokenize(text, split_affixes=False)
    return tokens

if __name__ == "__main__":
    base_dir = '/your/path/dictionary'
    config = Config(dialect_name="custom", base_path=Path(base_dir))
    wt = WordTokenizer(config=config)
    text = "།ལྷ་ས་ལས་ཁུངས་ཁག་གི་ཀུན་སྤྱོད་དག་ཐེར་གྱི་ལས་འགུལ་དེ་མཉམ་བཞད་འགྲན་སྡུར་གྱི་སྐབས་སུ་སླེབས་ཡོད་པ། བློ་མཐུན་པ་ཕའན་མིང་གིས་ཀྲུང་གུང་བོད་ལས་དོན་ཨུ་ཡོན་ལྷན་ཁང་གི་སྐུ་ཚབ་ཞུས་ཏེ་སྐུལ་སློང་གསུང་བཤད་གནང་བ། སྤྱི་ཚེས་ ༢༧ ཉིན་ཕའན་མིང་ཕུའུ་ཧྲུའུ་ཅིས་ཀྲུང་གུང་བོད་ལས་་དོན་ཨུ་ཡོན་ལྷན་ཁང་གི་སྐུ་ཚབ་ཞུས་ཏེ་གྲོང་ཁྱེར་ལྷ་སར་ཡོད་པའི་ཏང་མི་དང་།	ཏང་མི་མིན་པའི་ལས་བྱེད་པ་ཚོར་གསུང་བཤད་གནང་སྟེ་མཉམ་བཞད་འགྲན་སྡུར་ཆེན་མོ་བྱས་ནས་ཏང་གིས་ཀུན་སྤྱོད་དག་ཐེར་བྱེད་པར་རོགས་རམ་ཞུ་དགོས་པའི་འབོད་སྐུལ་གནང་འདུག"
    # text = sys.argv[1]
    tokens = get_tokens(wt, text)
    print('# text:', text)
    for token in tokens:
        print('----------------------------')
        print(token)

