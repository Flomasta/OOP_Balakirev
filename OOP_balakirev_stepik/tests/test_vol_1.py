from vol_1.task_1_4_vol_1 import media1, media2
from unittest import mock
import io


# тесты 1_4_1

def test_media(data='filemedia'):
    res = f'Воспроизведение {data}'
    media1.open(data)
    media2.open(data)
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        media1.play()
    assert fake_stdout.getvalue() == f'{res}\n'

    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        media2.play()
    assert fake_stdout.getvalue() == f'{res}\n'
