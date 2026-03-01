from main import Producto

def test_valor_total():
    p = Producto("Laptop", 1000, 3)
    assert p.calcular_valor_total() == 3000

def test_stock_vacio():
    p = Producto("Webcam", 50, 0)
    assert p.calcular_valor_total() == 0