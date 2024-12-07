from Table import Table
from Recogniser import Recogniser


def test_recogniser_and_convert_to_table1():
    result = [['МЗ0-212Б-22\n', '11 сентября\n', '18 сентября\n', '25 сентября\n', '2 октября\n'],
              ['Абдуллин Тимур\n', '\n', '\n', '\n', '\n'],
              ['Антонов Илья\n', '\n', '\n', '\n', '\n'],
              ['Астрихинская Арина\n', '\n', '\n', '\n', '\n'],
              ['Барденков Тимофей\n', 'Н\n', '\n', 'Н\n', '\n'],
              ['Григорьев Григорий\n', '\n', 'Н\n', '\n', '\n'],
              ['Заболотнов Семён\n', '\n', '\n', '\n', 'Н\n'],
              ['Кирюшин Артём\n', '\n', '\n', 'Н\n', '\n'],
              ['Кодиров Азиз\n', '\n', '\n', '\n', '\n'],
              ['Корнилова Ангелина\n', 'Н\n', '\n', '\n', 'Н\n'],
              ['Косолапова Анастасия\n', '\n', 'Н\n', '\n', '\n'],
              ['Кудряшев Дмитрий\n', '\n', '\n', '\n', '\n'],
              ['Пильнов Артём\n', 'Н\n', '\n', '\n', '\n'],
              ['Попов Виталий\n', '\n', '\n', '\n', '\n'],
              ['Путивцева Анна\n', '\n', '\n', 'Н\n', '\n'],
              ['Сакульцанов Вадим\n', '\n', 'Н\n', '\n', '\n'],
              ['Синицин Андрей\n', '\n', '\n', '\n', '\n'],
              ['Теленков Константин\n', '\n', '\n', '\n', 'Н\n'],
              ['Файзуллин Артур\n', '\n', '\n', '\n', '\n'],
              ['Федоров Николай\n', '\n', 'Н\n', '\n', '\n'],
              ['Фетисов Семён\n', '\n', '\n', 'Н\n', '\n'],
              ['Фоменко Глеб\n', '\n', '\n', '\n', '\n']]
    table = Table(22, 5)
    path_to_image = "./image/example.jpg"
    recogniser = Recogniser(path_to_image)
    recogniser.rects_recognition_without_storage_steps()
    recogniser.crop_image_to_cells_with_storage()
    recogniser.text_recognition_from_cells()
    table.text_array = recogniser.get_text()
    table.fill_table()
    table.fill_table()
    assert table.get_table() == result, "Test failed"


def test_recogniser_and_convert_to_table2():
    result = []
    table = Table(0, 0)
    path_to_image = "./image/example1.jpg"
    recogniser = Recogniser(path_to_image)
    recogniser.rects_recognition_without_storage_steps()
    recogniser.crop_image_to_cells_with_storage()
    recogniser.text_recognition_from_cells()
    table.text_array = recogniser.get_text()
    table.fill_table()
    table.fill_table()
    assert table.get_table() == result, "Test failed"
