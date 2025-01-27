from translate import Translator
translator = Translator(to_lang="ne")

try:
    with open('test.txt', mode = "r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)

        print(translation)

        with open('./test_translated.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:
    print("File does not exist!")