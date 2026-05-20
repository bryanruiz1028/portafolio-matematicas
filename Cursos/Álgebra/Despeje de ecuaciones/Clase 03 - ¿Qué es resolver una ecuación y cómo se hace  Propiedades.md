# Clase 03 — ¿Qué es resolver una ecuación y cómo se hace? | Propiedades e introducción al despeje

tags: #algebra #ecuaciones #despeje #matematicas
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 3

---

## 1. ENCABEZADO Y NAVEGACIÓN

« [[Clase 02]] | [[00 - Índice del curso]] »

---

## 2. RELEVANCIA Y APLICACIONES
Resolver una ecuación es el arte de equilibrar una balanza matemática para descubrir un valor que permanece oculto. No es un simple movimiento de números, sino un proceso para mantener la igualdad mientras aislamos nuestra incógnita.

**¿Dónde aplicamos esto?**
*   **Finanzas ($USD):** Para determinar el costo unitario ($v_i$) de productos en una factura masiva donde conocemos el total y los cargos fijos.
*   **Construcción y Física:** Para calcular la aceleración de una maquinaria o prever distancias de frenado seguras en una obra usando fórmulas de cinemática.
*   **Logística:** Para calcular el tiempo exacto de entrega basándose en una velocidad de transporte constante y una distancia determinada.

---

## 3. CONCEPTO CLAVE (Propiedades y Definición)

Como su profesor, quiero que visualicen la ecuación como una balanza de dos platos: el **Miembro de la izquierda** y el **Miembro de la derecha**.

*   **Definición de "Despejar":** Es el proceso de dejar la incógnita completamente sola en uno de los miembros.
*   **Propiedad Uniforme (La Regla de Oro):** Para que la balanza no se incline, cualquier operación que realices en el miembro de la izquierda **debe** realizarse exactamente igual en el miembro de la derecha. "Pasar un número" es solo un atajo mental de esta propiedad.
*   **Propiedad Simétrica:** Si logras que $5 = x$, por simetría es exactamente lo mismo que $x = 5$. Puedes "voltear" la balanza sin alterar la verdad.
*   **Nota sobre Notación ($v_i$):** En fórmulas de física, términos como $v_i$ representan una sola variable (Velocidad inicial). No intentes separar la "v" de la "i"; se mueven juntas como una unidad.
*   **Error Común:** Olvidar que un número no se "mueve" de lado, sino que cambia su operación a la inversa para anularse en el lado original.
*   **Truco Mnemotécnico:** *"La balanza siempre manda: si quitas de un lado, quitas del otro; si doblas un plato, doblas el otro"*.

---

## 4. PROCEDIMIENTO PASO A PASO

Para resolver ecuaciones complejas (como las de movimiento físico del material de estudio), siga estrictamente este orden pedagógico:

1.  **Sustitución:** Reemplace las variables (letras) por los valores numéricos conocidos según el problema.
2.  **Simplificación y "Truco del Denominador":** 
    *   Resuelva potencias y multiplicaciones inmediatas.
    *   **Pro-Tip:** Si hay una fracción que molesta, multiplique **todos** los términos de ambos miembros por el denominador para eliminar las fracciones y trabajar solo con enteros.
3.  **Identificación de términos:** Cuente cuántos términos hay en el miembro donde está la incógnita (recuerde que los signos $+$ y $-$ separan términos).
4.  **Despeje inverso (Propiedad Uniforme):**
    *   Primero, aplique la operación inversa a los términos que **no** contienen la variable (lo que suma pasa a restar).
    *   Al final, despeje los coeficientes que multiplican o dividen directamente a la incógnita.

---

## 5. EJEMPLOS PRÁCTICOS

```ad-example
title: Ejemplo 1: Hallar Velocidad Inicial ($v_i$)
**Problema:** En la fórmula $x = v_i \cdot t + \frac{a \cdot t^2}{2}$, halle $v_i$ si $x=39, t=3, a=6$.

1. **Sustituir:** $39 = v_i(3) + \frac{6(3^2)}{2}$
2. **Simplificar:** $3^2 = 9$. Luego $\frac{6 \cdot 9}{2} = 27$. La ecuación es: $39 = 3v_i + 27$.
3. **Restar términos:** El 27 está en el miembro de la derecha sumando. Aplicamos $-27$ a ambos lados: $39 - 27 = 3v_i \rightarrow 12 = 3v_i$.
4. **Dividir:** El 3 multiplica a $v_i$. Aplicamos división entre 3 en ambos miembros: $12 / 3 = v_i$.
**Resultado:** $v_i = 4$
```

```ad-example
title: Ejemplo 2: Hallar Aceleración ($a$)
**Problema:** Halle el valor de $a$ con los datos $x=50, v_i=10, t=2$.

1. **Sustituir:** $50 = (10)(2) + \frac{a(2^2)}{2}$
2. **Simplificar:** $50 = 20 + \frac{a \cdot 4}{2}$. Simplificamos la fracción: $4/2 = 2$. Queda: $50 = 20 + 2a$.
3. **Despejar suma:** El 20 (término independiente) pasa al miembro de la izquierda restando: $50 - 20 = 2a \rightarrow 30 = 2a$.
4. **Despejar multiplicación:** El 2 divide al 30: $30 / 2 = a$.
**Resultado:** $a = 15$
```

```ad-example
title: Ejemplo 3: El Caso de la Ecuación Cuadrática (Concepto)
¿Qué ocurre si buscamos el tiempo ($t$) y aparece como $t$ y como $t^2$?
* **Términos no semejantes:** Como $t$ y $t^2$ no se pueden sumar ni simplificar entre sí, no podemos "aislar" la letra de forma lineal. 
* **Procedimiento:** Debemos **igualar a cero** el miembro de la izquierda para formar una ecuación cuadrática (ej. $0 = 5t^2 + 40t - 100$).
* **Truco del Denominador:** Si tenemos una fracción sobre 2, multiplicamos todo por 2 antes de igualar a cero para facilitar el cálculo.
```

```ad-example
title: Ejemplo 4: Aplicación Real en Presupuestos ($USD)
**Problema:** Una inversión total ($x$) de $500 USD cubre la compra de 10 unidades ($t$) a un costo inicial unitario ($v_i$) más un cargo fijo de logística de $200 USD. Halle $v_i$.

1. **Ecuación:** $500 = v_i(10) + 200$.
2. **Despeje:** Restamos el cargo fijo: $500 - 200 = 10v_i \rightarrow 300 = 10v_i$.
3. **Costo Unitario:** $300 / 10 = v_i$.
**Resultado:** El costo inicial unitario ($v_i$) es de $30 USD.
```

---

## 6. EJERCICIOS PARA EL ESTUDIANTE

```ad-abstract
title: Nivel Fácil: Despeje Lineal Simple
Aplique la propiedad uniforme para hallar $x$:
1. $x + 7 = 15$
2. $x - 12 = 20$
3. $5x = 30$
4. $\frac{x}{4} = 5$
```

```ad-abstract
title: Nivel Medio: Operaciones Combinadas
Resuelva buscando el equilibrio de la balanza:
1. $\frac{x}{2} + 10 = 25$
2. $3x - 5 = 16$
3. $10 + 2x = 40$
4. $\frac{x}{5} - 2 = 8$
```

```ad-abstract
title: Nivel Avanzado: Aplicación de Fórmulas ($USD)
Use la fórmula de espacio $x = v_i \cdot t + \frac{a \cdot t^2}{2}$ para resolver:
1. **Inversión Logística:** Presupuesto $x=80$, tiempo $t=2$, costo base $v_i=25$. Calcule el factor de costo variable $a$.
2. **Costo de Producción:** Presupuesto total $x=600$, factor de aceleración $a=10$, tiempo $t=8$. Calcule el costo inicial $v_i$.
```

---

## 7. RESPUESTAS PARA EL DOCENTE

```ad-success
title: Solucionario Oficial
**Nivel Fácil:**
1. $x = 8$ | 2. $x = 32$ | 3. $x = 6$ | 4. $x = 20$

**Nivel Medio:**
1. $x = 30$ | 2. $x = 7$ | 3. $x = 15$ | 4. $x = 50$

**Nivel Avanzado:**
1. $a = 15$ (Se resta 50, queda 30. Se divide por 2).
2. $v_i = 35$ (Se resta 320, queda 280. Se divide por 8).
```

---

## 8. MINI-PRUEBA DE AUTOEVALUACIÓN

```ad-question
title: Autoevaluación de Conceptos
1. **La Balanza:** Si obtengo como resultado final que $24 = x$, ¿qué propiedad me permite escribir $x = 24$ sin cometer un error?
2. **Inversión:** Para despejar la incógnita en $\frac{x}{12} = 3$, ¿qué operación debo aplicar en ambos miembros de la balanza?
3. **Lógica USD:** Un proyecto cuesta $x$ dólares. Si se le aplica un descuento de $15 USD y el precio final es de $85 USD, ¿cuál era el valor original de $x$ aplicando la propiedad uniforme?
```

---

## 9. NOTAS FINALES Y CIERRE

*   **Próximo tema:** Entraremos de lleno en las **Ecuaciones Cuadráticas**, aprendiendo a resolver casos donde la incógnita aparece elevada al cuadrado y no puede simplificarse con los métodos de hoy.
*   **Consejo del Docente:** Siempre verifique su solución sustituyendo el número hallado en la ecuación original. Si ambos miembros resultan iguales, su balance es perfecto.

« [[Clase 02]] | [[00 - Índice del curso]] »