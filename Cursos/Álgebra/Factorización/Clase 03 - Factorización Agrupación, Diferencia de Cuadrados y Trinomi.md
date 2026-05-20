# Clase 03 — Factorización: Agrupación, Diferencia de Cuadrados y Trinomios $x^2+bx+c$

#algebra #commonfactorbyg

[[Clase 02]] | [[Indice]] | [[Clase 04]]

---

¿Qué tal, amigas y amigos? Espero que estén muy bien. En esta clase vamos a entrar de lleno al fascinante mundo de la factorización. Factorizar no es más que "desarmar" una expresión para ver de qué piezas (factores) está hecha. Si entiendes cómo se multiplican las cosas, ¡factorizar te parecerá pan comido porque es simplemente hacer el proceso al revés!

> [!info] ¿Por qué es tan importante factorizar?
> La factorización simplifica la vida. Al transformar sumas complejas en multiplicaciones, podemos cancelar términos y resolver problemas que de otro modo serían imposibles.
> 
> *   💵 **Finanzas:** Para optimizar costos de producción en proyectos valuados en USD, simplificando las fórmulas de rendimiento.
> *   🏗️ **Ingeniería:** Para calcular dimensiones exactas de estructuras (como plazas o edificios) a partir de expresiones de área.
> *   📊 **Distribución de Recursos:** Para organizar conjuntos de datos y repartir insumos de forma equitativa identificando patrones comunes.

---

### 3. Fundamentos Teóricos: Agrupación y Raíces

#### Factor Común por Agrupación de Términos
Cuando tenemos muchos términos (como 4 o 6) y no hay algo que se repita en **todos**, usamos la estrategia de "formar equipos". Podemos agrupar de 2 en 2 o de 3 en 3. El secreto es que, tras sacar el factor común de cada equipo, el paréntesis que quede debe ser **idéntico** en todos los grupos.

#### Las Raíces Cuadradas: Números vs. Letras
Para la Diferencia de Cuadrados, necesitamos extraer raíces exactas. Ojo aquí, que el procedimiento cambia:
1.  **Números:** Buscamos un número que multiplicado por sí mismo nos dé el total. ¡Debes grabarte los primeros 12! ($1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144$).
2.  **Letras:** ¡Es más fácil! Solo tienes que **dividir el exponente entre 2**.
    *   *Ejemplo:* $\sqrt{x^{10}} = x^5$ porque $x^5 \cdot x^5 = x^{10}$.

> [!warning] La Regla de Exclusión y el Error Común
> *   **El exponente impar:** Si una letra tiene un exponente que no se puede dividir entre 2 exactamente (como $m^{13}$), **no tiene raíz exacta** y, por tanto, no se puede factorizar por diferencia de cuadrados.
> *   **Confusión raíz vs. mitad:** No confundas la raíz de un número con su mitad. La raíz de 100 no es 50, es 10 (porque $10 \times 10 = 100$).

> [!tip] Regla mnemotécnica del Profe Alex
> "A la letra le partes el exponente a la mitad; al número búscale su pareja que multiplicada dé el total".

---

### 4. Procedimientos Paso a Paso

#### Bloque 1: Factorización por Agrupación (4 Pasos)
```text
1. Identificar grupos: Forma equipos de igual tamaño (2-2 o 3-3) que compartan factores.
2. Extraer factor común: Aplica factor común simple a cada grupo.
3. El Paso Clave (Signos): Si los paréntesis no son iguales, extrae un signo negativo (-) para que los términos internos cambien de signo y coincidan.
4. Factor final: Escribe el paréntesis repetido una vez y, en otro paréntesis, agrupa los términos que quedaron afuera.
```

#### Bloque 2: Diferencia de Cuadrados (Checklist de Identificación)
Antes de resolver, verifica estas 3 condiciones:
1. ¿Son exactamente **2 términos**?
2. ¿Hay una **resta** entre ellos?
3. ¿Tienen **raíz cuadrada exacta** (números perfectos y exponentes pares)?

**Procedimiento:**
```text
1. Calcula las raíces cuadradas de ambos términos.
2. Abre dos paréntesis (binomios conjugados).
3. Escribe las raíces en ambos: uno con signo (+) y otro con signo (-).
*Nota: Este es el proceso inverso al producto de binomios conjugados.*
```

---

### 5. Sección de Ejemplos Resueltos

```ad-example
title: Ejemplo 1: Diferencia de cuadrados básica
**Factorizar:** $m^2 - n^2$
1. Raíz de $m^2 = m$. Raíz de $n^2 = n$.
2. **Resultado:** $(m + n)(m - n)$
*(Recuerda: si multiplicas esto, volverás a la expresión original).*
```

```ad-example
title: Ejemplo 2: Agrupación de 6 términos con cambio de signo
**Factorizar:** $2am - 2an + 2a - m + n - 1$
1. Agrupamos los primeros tres (tienen $2a$): $2a(m - n + 1)$.
2. Agrupamos los últimos tres: $(-m + n - 1)$.
3. **Paso Clave:** Los signos del segundo grupo son opuestos al primero. Extraemos el "-": $-(m - n + 1)$.
4. **Resultado final:** $(m - n + 1)(2a - 1)$
```

```ad-example
title: Ejemplo 3: Coeficientes y potencias
**Factorizar:** $16x^2 - 25y^4$
1. Raíz de $16x^2$: $\sqrt{16}=4$ y $\sqrt{x^2}=x \rightarrow 4x$.
2. Raíz de $25y^4$: $\sqrt{25}=5$ y $\sqrt{y^4}=y^2 \rightarrow 5y^2$.
3. **Resultado:** $(4x + 5y^2)(4x - 5y^2)$
```

```ad-example
title: Ejemplo 4: Aplicación Inmobiliaria (USD)
El costo de instalación de baldosas para una plaza se define por la diferencia de áreas de dos secciones cuadradas: $16x^2 - 25$. Si el precio por metro cuadrado es de 1 USD, ¿cómo factorizamos para hallar las dimensiones necesarias para el presupuesto?
1. Verificamos: 2 términos, resta, raíces exactas ($\sqrt{16x^2}=4x$, $\sqrt{25}=5$).
2. Factorizamos: $(4x + 5)(4x - 5)$.
*Esto nos dice que el área total es el producto de la suma y la diferencia de los lados de las secciones.*
```

---

### 6. Práctica para el Estudiante

Amigas y amigos, ¡llegó el momento de practicar! Recuerden que en matemáticas, la práctica es lo que hace al maestro. Intenten resolverlos primero por su cuenta.

```ad-abstract
title: Ejercicios Propuestos
**🟢 Fácil (Raíces e Identificación)**
1. $\sqrt{x^{10}y^4}$
2. $\sqrt{121m^8}$
3. ¿Se puede factorizar $x^2 + 16$ por diferencia de cuadrados? ¿Por qué?
4. $\sqrt{144a^{12}}$

**🟡 Medio (Aplicación de casos)**
5. $x^2 - 81$
6. $49a^2 - 1$
7. $ax + ay + bx + by$
8. $2x - 2y + mx - my$

**🔴 Avanzado (El Reto)**
9. $100a^2 - 64b^6$
10. $x^{2n} - y^{4n}$
11. $x^{13} - 25$ (Analiza si es posible por este método).
12. La utilidad de una tienda en USD está dada por $625x^2 - 400$. Factoriza la expresión para simplificar el reporte contable.
```

```ad-success
title: Respuestas (Para el Docente)
1. $x^5y^2$ | 2. $11m^4$ | 3. No, porque es una suma y debe ser resta. | 4. $12a^6$
5. $(x+9)(x-9)$ | 6. $(7a+1)(7a-1)$ | 7. $(a+b)(x+y)$ | 8. $(2+m)(x-y)$
9. $(10a+8b^3)(10a-8b^3)$ | 10. $(x^n + y^{2n})(x^n - y^{2n})$ | 11. No es posible (exponente impar 13). | 12. $(25x+20)(25x-20)$
```

---

### 7. Mini-prueba de Autoevaluación

```ad-question
title: Pregunta 1
¿Cuáles son las condiciones para un trinomio de la forma $x^2+bx+c$?
a) 3 términos, $x^2$ debe tener un coeficiente mayor a 1.
b) 2 términos y una resta.
c) 3 términos, el coeficiente de $x^2$ debe ser 1 y el exponente mayor debe ser par.
d) 4 términos agrupados.
*Respuesta: c. Debe ser un trinomio con coeficiente principal 1 y potencias descendentes (ej. $x^2, x^1, x^0$).*
```

```ad-question
title: Pregunta 2
¿Cuál es el resultado de factorizar $36 - m^{10}$?
a) $(6 - m^5)(6 - m^5)$
b) $(18 - m^5)(18 + m^5)$
c) $(6 + m^5)(6 - m^5)$
d) No se puede factorizar.
*Respuesta: c. Raíz de 36 es 6 y raíz de $m^{10}$ es $m^5$. Se aplica el binomio conjugado.*
```

```ad-question
title: Pregunta 3
Un terreno tiene un área de $x^2 - 144$ metros cuadrados. Si $x = 20$, ¿cuál es el valor del área usando la forma factorizada en USD?
a) $(20+12)(20-12) = 32 \times 8 = 256$
b) $(20-12)(20-12) = 64$
c) $400 - 144 = 256$
d) Las opciones a y c son correctas, pero la 'a' muestra el proceso de factorización.
*Respuesta: d. Ambas dan el mismo valor, pero la factorización facilita el cálculo mental: $32 \times 8 = 256$.*
```

---

### 8. Cierre y Conexión

> [!tip] Próximo paso: Trinomio $x^2+bx+c$
> En la Clase 04 aprenderemos a factorizar trinomios. El truco es buscar dos números que **multiplicados den 'c'** y que **sumados o restados den 'b'**. ¡Es como un juego de detectives numéricos!

> [!info] Tip Maestro del Profe Alex
> Si te dan un número muy grande para el término 'c' (como 120), no adivines. **Descomponlo en sus factores primos** (mitad, tercera, etc.). Cualquier combinación de esos factores multiplicará 120; solo tendrás que probar combinaciones hasta que la suma te dé 'b'. Por ejemplo, para 120 y suma 23, la combinación es $8 \times 15$.

---
[[Clase 02]] | [[Indice]] | [[Clase 04]]