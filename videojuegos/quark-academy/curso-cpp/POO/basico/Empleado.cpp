//
// Created by Tito on 4/04/2023.
//

/*
 * ENUNCIADO
 * Confeccionar una clase que represente un empleado. Definir como atributos su nombre y
 * su sueldo. Confeccionar los métodos para la carga, otro para imprimir sus datos y por
 * último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
 */

class Empleado {
private:
    string nombre;
    long sueldo;
public:
    inicializar();
    imprimirDatos();
    debePagarImpuestos();
};
