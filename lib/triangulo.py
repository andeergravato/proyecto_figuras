def get_identificador() -> str:
	return "triangulo"
def get_area(base:int, altura:int) -> float:
	area = (base*altura)/2
	return (f"El triángulo de base= {base} y altura= {altura} es area= {area}")
def get_perimetro(lado_a:int, lado_b:int, lado_c:int) -> int:
	return lado_a + lado_b + lado_c
