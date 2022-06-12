import pytest

from src.student import StudentDB

## Conexión BD

# db = None

# def setup_module(module): # conectar a BD
#     print("iniciando db ...")
#     global db
#     db = StudentDB()
#     db.connect('data.json')
#
# def teardown_module(module): # cerrar la BD
#     print("cerrando db ...")
#     db.close()

## Reemplazamos código de conexión:
# En vez de que sea una variable global, que  sea un fixture
# valor fijo para todos los test
# en este caso sobre BD

@pytest.fixture(scope="module")
def db():
    print('---setup---')
    db = StudentDB()
    db.connect('data.json')
    yield db # keyword para que funcione
    print('---teardown---')
    db.close()

## Funciones

def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'