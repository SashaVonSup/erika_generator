# erika_generator
##### Чтобы собрать модель из файлов с корпусами и сохранить её в файл, выполните в терминале:

```py build.py <модель> <корпус1> <корпус2> ... <корпусN>```

Например, `py build.py model.pickle corpus.txt`
создаст файл "model.pickle" и сохранит туда модель, созданную на основе корпуса из файла "corpus.txt"

##### Чтобы сгенерировать текст, выполните в терминале:

```py generate.py <модель> [необязательное начало]```

Например, `py generate.py model.pickle Однажды Колобок пошёл`
Выведет текст, сгенерированный из модели "model.pickle", начинающийся со слов "Однажды Колобок пошёл".
При составлении продолжения учитывается только последнее слово.
В нём не должно быть неалфавитных символов (в т.ч. оно не может кончаться запятой), но в нём могут быть заглавные буквы.
