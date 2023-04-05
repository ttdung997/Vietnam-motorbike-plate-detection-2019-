import pathlib
import transpyle

path = pathlib.Path('plate.py')
code_reader = transpyle.CodeReader()
code = code_reader.read_file(path)

from_language = transpyle.Language.find('Python 3.6')
to_language = transpyle.Language.find('C')
translator = transpyle.AutoTranslator(from_language, to_language)
fortran_code = translator.translate(code, path)
print(fortran_code)