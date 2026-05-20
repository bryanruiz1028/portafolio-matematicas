# Clase 09 — División de números decimales

#algebra #divisindenmeros

> [!info] 🧭 Navegación
> [Anterior: Clase 08]([[Clase08]]) | [🏠 Índice del Curso]([[Indice]]) | [Siguiente: Clase 10]([[Clase10]])

---

## 🌍 Relevancia y aplicaciones

La división de números decimales es una habilidad esencial que nos permite simplificar cálculos aparentemente complejos al convertirlos en operaciones con números naturales. Su utilidad es constante en diversos contextos reales:

> [!info] Aplicaciones prácticas
> - **Finanzas en $USD:** Fundamental para repartir presupuestos con precisión de centavos o calcular el precio unitario de productos (ej. cuánto cuesta un gramo de oro o una onza de plata).
> - **Dosificación y proporciones:** Es vital en la cocina y la construcción para medir dosis exactas de ingredientes o materiales cuando las cantidades no son enteras.
> - **Situaciones cotidianas:** Permite calcular el costo exacto por litro de combustible o dividir equitativamente una cuenta en un restaurante entre varios amigos.

---

## Concepto Clave y Reglas Nemotécnicas

> [!note] 📌 ¿Qué es la división de números decimales?
> Dividir decimales consiste en repartir una cantidad no entera. El método universal consiste en la **amplificación**: multiplicamos tanto el dividendo como el divisor por la misma potencia de 10 ($10, 100, 1000\dots$) para eliminar las comas. Matemáticamente, el cociente no varía si ambos términos se multiplican por el mismo número.

> [!warning] ⚠️ Error común
> Nunca multipliques el numerador y el denominador por potencias de 10 diferentes. Si multiplicas arriba por 10 y abajo por 100, estarías alterando la proporción de la fracción y el resultado será incorrecto. Para mantener la igualdad, **ambos términos deben multiplicarse siempre por el mismo número**.

> [!tip] 💡 Truco para recordarlo
> Para eliminar los decimales, "corre la coma hacia la derecha". Solo debes contar cuántos saltos da la cifra con más decimales y obligar a la otra cifra a dar la misma cantidad de saltos (añadiendo ceros si es necesario).

---

## Procedimiento Paso a Paso

Para aplicar el "método que sirve siempre", sigue este orden lógico:

1. **Expresar como fracción:** Escribe la división en forma de fracción para visualizar mejor la amplificación.
2. **Identificar el máximo de decimales:** Observa ambos números y determina cuál tiene la mayor cantidad de cifras decimales.
3. **Amplificar uniformemente:** Multiplica ambos términos por la potencia de 10 (10, 100, 1000) que corresponda a esa cantidad máxima de decimales. Esto garantiza que **todas** las comas desaparezcan.
4. **Dividir naturales:** Realiza la división de los números naturales resultantes. Si queda residuo, añade un cero y coloca una coma en el cociente para obtener decimales en el resultado final.

---

## Bloque de Ejemplos

```ad-example
title: Ejemplo 1 (Básico - Cantidad igual de decimales)
**Operación:** $4,8 \div 1,2$
1. Escribimos como fracción: $\frac{4,8}{1,2}$.
2. Ambos tienen 1 cifra decimal, multiplicamos por 10.
3. $4,8 \times 10 = 48$ y $1,2 \times 10 = 12$.
4. Dividimos: $48 \div 12 = 4$.
**Resultado:** 4
```

```ad-example
title: Ejemplo 2 (Diferente cantidad de decimales)
**Operación:** $6,3 \div 0,15$
1. El divisor ($0,15$) tiene **dos** decimales (el máximo), así que multiplicamos ambos por 100.
2. $6,3 \times 100 = 630$ (corremos la coma dos lugares, agregando un cero).
3. $0,15 \times 100 = 15$.
4. Dividimos: $630 \div 15 = 42$.
**Resultado:** 42
```

```ad-example
title: Ejemplo 3 (Avanzado - Con residuo y decimales en cociente)
**Operación:** $35,82 \div 2,5$
1. El número con más decimales es $35,82$ (dos cifras). Multiplicamos ambos por 100.
2. Obtenemos: $3582 \div 250$.
3. Proceso de división:
   - 250 cabe 14 veces en 3582, dejando un **residuo** de 82.
   - Ponemos coma en el cociente y agregamos un cero al residuo: 820 entre 250 = 3 (sobran 70).
   - Agregamos otro cero: 700 entre 250 = 2 (sobran 200).
   - Agregamos otro cero: 2000 entre 250 = 8 (sobra 0).
**Resultado:** 14,328
```

```ad-example
title: Ejemplo 4 (Aplicación en $USD)
**Problema:** Si 1,2 kg de un producto cuestan $4,8 USD, ¿cuál es el precio por kilogramo?
**Solución:**
Dividimos el costo total entre el peso: $4,8 \div 1,2$.
Convertimos a naturales multiplicando por 10: $48 \div 12 = 4$.
**Resultado:** El precio es de $4 USD por kilogramo.
```

---

## Ejercicios para el Estudiante

### 🟢 Nivel Fácil
1. $2,4 \div 0,6$
2. $5,5 \div 1,1$
3. $0,9 \div 0,3$
4. $1,2 \div 0,4$

### 🟡 Nivel Medio
1. $8,4 \div 0,21$
2. $12,5 \div 0,5$
3. $7,2 \div 0,08$
4. $0,5 \div 0,25$

### 🔴 Nivel Avanzado (Problemas contextualizados)
1. Un cliente pagó $15,6 USD por 1,2 kg de carne. ¿Cuál es el precio por kilo?
2. Si 2,5 litros de un químico cuestan $35,82 USD, ¿cuál es el costo de un solo litro?
3. Repartir un bono de $630 USD equitativamente entre 15 empleados.
4. Calcula el precio unitario si un paquete de 0,15 kg de especias cuesta $6,3 USD.

```ad-success
title: Respuestas para el docente
- **Nivel Fácil:** 1) 4; 2) 5; 3) 3; 4) 3.
- **Nivel Medio:** 1) 40; 2) 25; 3) 90; 4) 2.
- **Nivel Avanzado:** 1) $13 USD; 2) $14,328 USD; 3) $42 USD; 4) $42 USD.
```

---

## Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1
**¿Por qué es necesario multiplicar por potencias de 10 al dividir decimales siguiendo este método?**
a) Para aumentar el valor de los números y que la división sea más grande.
b) Para transformar los decimales en números naturales y facilitar la operación.
c) Porque las divisiones con comas son matemáticamente imposibles.
d) Para cambiar el cociente final de la operación.

**Respuesta:** b. La amplificación busca eliminar las comas para trabajar con naturales, manteniendo el resultado original.
```

```ad-question
title: Pregunta 2
**Si aplicamos la regla de "correr la coma", ¿qué resultado obtenemos al multiplicar 5,72 por 1000?**
a) 57,2
b) 572
c) 5720
d) 57200

**Respuesta:** c. Según el Profe Alex, correr la coma tres veces hacia la derecha (por los tres ceros del 1000) nos obliga a saltar el 7, el 2 y añadir un cero al final.
```

```ad-question
title: Pregunta 3
**Para resolver la división $6,3 \div 0,15$, ¿cuál es la potencia de 10 correcta para amplificar?**
a) 10, porque 6,3 tiene solo una cifra decimal.
b) 100, porque se elige la potencia según el número con más decimales (0,15).
c) 1000, para asegurar que sobren ceros.
d) No se debe amplificar si el divisor es menor que 1.

**Respuesta:** b. Siempre se debe amplificar por el número que tenga más cifras decimales para asegurar que ambos se conviertan en naturales.
```

---

> [!tip] 💡 En la próxima clase
> Has dominado la técnica de amplificación. En la **Clase 10**, daremos el siguiente paso: aprenderemos a manejar casos donde dividimos un número entero entre un decimal y cómo integrar todo en **operaciones combinadas**.

> [!info] 🧭 Navegación
> [Anterior: Clase 08]([[Clase08]]) | [🏠 Índice del Curso]([[Indice]]) | [Siguiente: Clase 10]([[Clase10]])