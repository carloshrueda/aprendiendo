
# 2.6.11  LAB Operadores y expresiones – 2

----------

## Escenario

La tarea es preparar un código simple para evaluar o encontrar el  **tiempo final**  de un periodo de tiempo dado, expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las  **12:17**  y dura  **59 minutos**, terminará a las  **13:16**.

No te preocupes si tu código no es perfecto - está bien si acepta una hora invalida - lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

Prueba el código cuidadosamente. Pista: utilizar el operador  %  puede ser clave para el éxito.

## Datos de Prueba

**Entrada de muestra:**

```
12
17
59
```

**Salida Esperada:**

```
13:16
```

**Entrada de muestra:**

```
23
58
642
```

**Salida Esperada:**

```
10:40
```

**Entrada de muestra:**

```
0
1
2939
```

**Salida Esperada:**

```
1:0
```