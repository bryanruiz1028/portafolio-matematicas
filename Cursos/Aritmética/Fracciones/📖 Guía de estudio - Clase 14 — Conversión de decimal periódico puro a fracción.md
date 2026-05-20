# 📖 Guía de estudio — Clase 14: Convertir un decimal periódico puro a fracción

> [!info] 📌 Conceptos clave
> *   **Decimal periódico puro:** Es aquel donde el periodo (la cifra que se repite) comienza inmediatamente después de la coma o punto decimal. Por ejemplo: $1,3636...$
> *   **Anatomía del número:** Identificamos la **parte entera** (a la izquierda del separador) y la **parte periódica** (las cifras que se repiten bajo el arco).
> *   **Equivalencia de signos:** Recuerda que la coma (,) y el punto (.) decimal son equivalentes; usa el que prefieras según tu país.
> *   **Poder de la simplificación:** Siempre debemos reducir la fracción a su mínima expresión para que el resultado sea elegante y profesional.

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Decimal periódico puro** | Número cuya parte decimal consiste exclusivamente en cifras que se repiten al infinito justo tras la coma. |
| **Numerador de la fracción** | Se calcula restando: **(Número completo sin coma) - (Parte entera)**. |
| **Denominador de la fracción** | Se colocan tantos **9** como cifras tenga el periodo. <br>*(Hint visual: # de nueves = # de cifras en el periodo)*. |

---

## Ejemplos Resueltos con Paso a Paso

```ad-example
title: Ejemplo A (Caso Básico)
**Convertir $1,36$ periódico a fracción**

¡Hola! Vamos a transformar este número paso a paso. Es más sencillo de lo que parece:

1. **Paso 1 (Numerador):** Tomamos el número sin la coma ($136$) y le restamos la parte entera ($1$).
   * $136 - 1 = 135$
2. **Paso 2 (Denominador):** Observamos que el periodo tiene dos cifras ($3$ y $6$), por lo tanto, escribimos dos nueves.
   * Denominador = $99$
3. **Paso 3 (Simplificación):** Nuestra fracción es $135/99$. 
   * **¿Podemos simplificar?** ¡Sí! Si sumas las cifras de $135$ ($1+3+5=9$), ves que es múltiplo de 3.
   * Dividimos entre 3: $135 \div 3 = 45$ y $99 \div 3 = 33 \rightarrow 45/33$.
   * Dividimos entre 3 otra vez: $45 \div 3 = 15$ y $33 \div 3 = 11 \rightarrow 15/11$.

**Resultado final:** $1,36... = \frac{15}{11}$
```

```ad-example
title: Ejemplo B (Aplicación Real $USD)
**¿Cuánto es $5,9$ periódico en dólares?**

A veces las matemáticas nos dan sorpresas. Imagina que un precio es de $5,999...$ USD. Vamos a convertirlo:

1. **Numerador:** El número sin coma ($59$) menos la parte entera ($5$).
   * $59 - 5 = 54$
2. **Denominador:** El periodo tiene una cifra ($9$), así que ponemos un nueve.
   * Denominador = $9$
3. **Resultado:** Al dividir $54 \div 9$, obtenemos **$6$**.

**Conclusión:** Matemáticamente, $5,9$ periódico es exactamente **6 USD**. Al igual que cuando vemos un precio de $999$ dólares y sabemos que prácticamente estamos pagando $1000$, en los decimales periódicos con "9", el valor se redondea al entero superior.
```

---

## Ejercicios de Repaso

¡Es tu turno de brillar! Practica con estos ejercicios diseñados para subir de nivel:

```ad-abstract
title: 🟢 Nivel: Fácil
Convierte estos decimales de una sola cifra periódica a fracción (simplifica si es posible):
1. $0,3$ periódico
2. $3,6$ periódico
3. $0,6$ periódico
```

```ad-abstract
title: 🟡 Nivel: Medio
Resuelve estos casos con periodos de dos cifras y partes enteras mayores a cero:
1. $1,12$ periódico
2. $34,36$ periódico
3. $5,16$ periódico
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Casos Especiales
Aplica el método en números grandes y observa los resultados curiosos:
1. $421,36$ periódico
2. $12,9$ periódico 
*💡 Pista: ¿Qué sucede cuando el periodo es 9? Aplica la regla y observa si obtienes un número entero.*
```

---

## Clave de Respuestas

Usa esta sección para verificar tu progreso. ¡No hagas trampa!

*   **Fácil:** 1) $1/3$ | 2) $11/3$ | 3) $2/3$
*   **Medio:** 1) $37/33$ | 2) $378/11$ | 3) $511/99$
*   **Avanzado:** 1) $4635/11$ | 2) $13$ (¡Un entero exacto!)

---

> [!tip] 💡 Consejo de estudio
> **¡Confía pero verifica!** Siempre puedes comprobar tu resultado dividiendo el numerador entre el denominador en una calculadora. Si el resultado decimal es igual al original, ¡lo lograste! Recuerda observar siempre que el periodo sea **puro** antes de empezar; si hay números "colados" entre la coma y el periodo, el método cambia ligeramente.