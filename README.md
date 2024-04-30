# modern-botok
This respoditory offers a custamized dictionary (dictionary/tsikchen.tsv), and provides an explanation of how to integrate the customized dictionary.

## Files 
- src/clean_dictionary.py: it reads a dictionary file and removes explations after '|'.
- src/example.py: it toknizes a Tibetan sentence.
- src/integrate_dictionary.py: it combines dictionaries, and drops duplicate entries.
- src/reduce_syllables.py: it reduces the syllable number of dictionary entires.
- dictionary/tsikchen.tsv: a file of the custom dictionary.

## Dictionaries 
- Custom dictionary was compliled from [Christian Steinert's collection](https://github.com/christiansteinert/tibetan-dictionary/tree/master/_input/dictionaries/public) and contains the following dictionaries: 
  1. Grand Monlam Dictionary (default dictionary of Botok)
  2. [Jim Valby](https://github.com/christiansteinert/tibetan-dictionary/blob/master/_input/dictionaries/public/07-JimValby)
  2. [Ives Waldo](https://github.com/christiansteinert/tibetan-dictionary/blob/master/_input/dictionaries/public/08-IvesWaldo)
  3. [Dan Martin](https://github.com/christiansteinert/tibetan-dictionary/blob/master/_input/dictionaries/public/09-DanMartin)
  4. [Tshig mdzod chen mo](https://github.com/christiansteinert/tibetan-dictionary/blob/master/_input/dictionaries/public/25-tshig-mdzod-chen-mo-Tib)
  5. [Dung dkar](https://github.com/christiansteinert/tibetan-dictionary/blob/master/_input/dictionaries/public/34-dung-dkar-tshig-mdzod-chen-mo-Tib)
  6. [Tibetan Terminology Project](https://github.com/christiansteinert/tibetan-dictionary/blob/master/_input/dictionaries/public/48-TibTermProject
)

## How to use
1. Install botok in terminal:
```
pip install botok
```
2. Run the following code in console to generate the folder 'general':
```
config = Config()
wt = WordTokenizer(config=config)
```
* You can specify the folder in which the folder 'general' is created.
```
base_dir = '/your/path/dictionary'
config = Config(base_path= Path(base_dir))
config = Config()
wt = WordTokenizer(config=config)
```
3. Open the directory (/Documents/pybo/dialect_packs) in which the folder 'general' is located. 
4. Copy the folder 'general' and change the folder name into 'custom'.
5. Replace custom/dictionary/words/tsikchen.tsv with the file of the same name (tsikchen.tsv).
6. Run the following code to genearte custom_trie.pickled:
```
config = Config(dialect_name="custom")
wt = WordTokenizer(config=config)
```
7. Run src/example.py:
```
python3 src/example.py
```