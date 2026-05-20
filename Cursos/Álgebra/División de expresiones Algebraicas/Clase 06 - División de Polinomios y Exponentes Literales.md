# Clase 06 — División de Polinomios y Exponentes Literales
tags: #algebra #dividingpolynom
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 7

## 1. NAVEGACIÓN

| ANTERIOR | ÍNDICE | SIGUIENTE |
| :--- | :---: | :--- |
| [[Clase 05]] | [[00 - Índice del curso]] | [[Clase 07]] |

---

## 2. ¿POR QUÉ ES IMPORTANTE ESTA CLASE?

La división de polinomios constituye el pilar para la simplificación de funciones racionales y el análisis de variaciones proporcionales en sistemas algebraicos. Comprender el manejo de exponentes literales permite al estudiante generalizar soluciones matemáticas, aplicando reglas de potencias a niveles de abstracción técnica superior.

*   💵 **Aplicación en $USD:** Modelado de costos promedios en producción masiva, dividiendo la función de costo total entre la cantidad variable de unidades.
*   🏗️ **Aplicación práctica:** Determinación de dimensiones estructurales (base o altura) a partir de expresiones polinómicas de área superficial.
*   📊 **Situación cotidiana:** Distribución equitativa de recursos en la gestión de proyectos cuando las variables de entrada están sujetas a exponentes dinámicos.

---

## 3. CONCEPTO CLAVE

### Definición Técnica
La **división de polinomios** es una operación que consiste en desglosar una expresión compleja (dividendo) en partes proporcionales definidas por un divisor. Desde la didáctica, aplicamos la **analogía de los pantalones**: así como no podemos restar "3 camisas a 5 pantalones" porque no son artículos iguales, en álgebra solo operamos **términos semejantes** (aquellos con la misma parte literal y exponente).

> [!warning] **Diferencia Crítica de Operaciones**
> Es fundamental no confundir las reglas de los exponentes en la adición frente a la multiplicación:
> *   **Suma/Resta:** $x^2 + x^3 \neq x^5$. Aquí los exponentes NO se alteran; solo se operan coeficientes si los términos son semejantes.
> *   **Multiplicación:** $x^2 \cdot x^3 = x^5$. Se aplica la propiedad de **Producto de potencias de igual base**, donde se conserva la base y se suman los exponentes.

> [!tip] **Regla de Oro: "ORDENA Y EMPAREJA"**
> 1.  **Ordena:** Ambos polinomios deben estar en orden descendente respecto a una variable común.
> 2.  **Empareja:** Busca un término en el cociente que, al multiplicarse por el primer término del divisor, iguale exactamente al primer término del dividendo.

---

## 4. PROCEDIMIENTO PASO A PASO

```text
PASO 1 → Ordenar el dividendo y divisor de forma descendente respecto a una misma letra.
PASO 2 → Buscar el término del cociente que multiplicado por el primer término del divisor iguale al primero del dividendo.
PASO 3 → Multiplicar y RESTAR (¡OJO! Este es el paso donde más se cometen errores por olvido del cambio de signo).
PASO 4 → Bajar el siguiente término del dividendo y repetir hasta que el residuo sea cero o su grado sea menor al del divisor.
```

---

## 5. EJEMPLOS DE CLASE

> [!info] **Ejemplo 1: Lógica de Exponentes Literales**
> Para transformar $x^n$ en $x^{n+3}$ mediante una multiplicación, aplicamos la ley de exponentes:
> $$x^n \cdot (x^3) = x^{n+3}$$
> **Explicación técnica:** Identificamos que la *base* es $x$. Para que el *exponente* resultante sea $n+3$, debemos multiplicar por una potencia de igual base cuyo exponente complete la suma requerida.

```ad-example
title: Ejemplo 2: Caso con Signos y Dos Variables
Dividir $(6x^2 - xy - 2y^2) \div (2x + y)$

1. **Primer término:** $6x^2 \div 2x = \mathbf{3x}$.
2. **Multiplicación y resta:** $3x(2x + y) = 6x^2 + 3xy$. Al restar al dividendo, cambiamos signos: $-6x^2 - 3xy$.
3. **Reducción:** $(-xy) + (-3xy) = -4xy$. Bajamos el siguiente término: $-2y^2$.
4. **Segundo término:** $-4xy \div 2x = \mathbf{-2y}$.
5. **Multiplicación y resta:** $-2y(2x + y) = -4xy - 2y^2$. Al restar, cambiamos signos: $+4xy + 2y^2$.
6. **Resultado:** $3x - 2y$.
```

```ad-abstract
title: Ejemplo 3: Caso Avanzado (Doble Eliminación)
Al resolver $(15m^5 - 5m^4n - 9m^3n^2 + 3m^2n^3 + 3mn^4 - n^5) \div (3m - n)$:

* **Doble eliminación inicial:** El primer término del cociente $5m^4$ elimina simultáneamente a $15m^5$ y $-5m^4n$ tras el cambio de signo.
* **Acción técnica:** Como se eliminaron dos términos, la regla didáctica nos indica **bajar los siguientes dos términos** del dividendo ($-9m^3n^2 + 3m^2n^3$) para continuar la operación.
* **Resultado final:** $5m^4 - 3m^2n^2 + n^4$.
```

```ad-example
title: Ejemplo 4: Aplicación en Finanzas ($USD)
Si el costo total de adquisición para una empresa está dado por $6x^2 - xy - 2y^2$ dólares y la cantidad de unidades compradas es de $2x + y$, ¿cuál es el costo unitario?

**Solución:** Al realizar la división técnica (ver procedimiento del Ejemplo 2), determinamos que el costo unitario por cada artículo es de:
$$\mathbf{(3x - 2y) \text{ dólares.}}$$
```

---

## 6. EJERCICIOS PARA EL ESTUDIANTE

### 🟢 Verde (Fácil - Propiedades de Potencias)
1. ¿Por qué factor multiplicar $x^n$ para obtener $x^{n+2}$?
2. ¿Por qué factor multiplicar $x^a$ para obtener $x^{a+5}$?
3. ¿Por qué factor multiplicar $x^{2n}$ para obtener $x^{2n+1}$?
4. ¿Por qué factor multiplicar $x^n$ para obtener $x^{2n}$?

### 🟡 Amarillo (Medio - Divisiones Estándar)
1. $(x^2 + 5x + 6) \div (x + 2)$
2. $(a^2 - 5a + 6) \div (a - 3)$
3. $(-15x^2 + 22x - 8) \div (-3x + 2)$
4. $(6x^2 - xy - 2y^2) \div (3x - 2y)$

### 🔴 Rojo (Avanzado - Exponentes Literales y Aplicaciones)
1. $(x^{2a} + 5x^a + 6) \div (x^a + 2)$
2. Determinar el precio unitario si el costo total es $15x^{3n} - 5x^{2n}$ para una cantidad de $5x^{2n}$ artículos.
3. $(x^{n+2} + 3x^{n+1} + 2x^n) \div (x + 1)$
4. $(m^{2a} - n^{2b}) \div (m^a - n^b)$

```ad-success
title: Respuestas para el Docente
**Nivel Verde:** 
1. $x^2$ | 2. $x^5$ | 3. $x^1$ (o simplemente $x$) | 4. $x^n$

**Nivel Amarillo:** 
1. $x+3$ | 2. $a-2$ | 3. $5x-4$ | 4. $2x+y$

**Nivel Rojo:** 
1. $x^a+3$ | 2. $3x^n-1$ | 3. $x^{n+1}+2x^n$ | 4. $m^a+n^b$
```

---

## 7. MINI-PRUEBA DE AUTOEVALUACIÓN

```ad-question
title: Autoevaluación Rápida
1. **¿Cuál es el pre-requisito obligatorio antes de ejecutar el algoritmo de división?**
   * *Respuesta:* Ordenar el dividendo y el divisor de forma descendente respecto a una misma variable.

2. **¿Qué sucede con los exponentes literales durante la división cuando multiplicamos el cociente por el divisor?**
   * *Respuesta:* Se suman (Producto de potencias de igual base).

3. **Problema de Aplicación:** Si el área de un terreno rectangular está expresada por $x^2 + 5x + 6$ y su base es $x+2$, ¿cuál es la expresión de su altura?
   * *Respuesta:* $x+3$.
```

---

## 8. NOTAS FINALES Y NAVEGACIÓN

> [!note] **Próxima Clase**
> En la **Clase 07**, exploraremos la **División Sintética (Regla de Ruffini)**, un método optimizado para dividir polinomios entre binomios de la forma $(x \pm a)$, y cómo manejar residuos no nulos.

| ANTERIOR | ÍNDICE | SIGUIENTE |
| :--- | :---: | :--- |
| [[Clase 05]] | [[00 - Índice del curso]] | [[Clase 07]] |