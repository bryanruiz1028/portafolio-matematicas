# Clase 05 — Conversión de la ecuación general de la elipse a su forma canónica y ordinaria

#algebra #ellipse

```ad-info
title: 🧭 Navegación
- **Anterior:** [[Clase 04 — La elipse: Conceptos básicos y elementos]]
- **Siguiente:** [[Clase 06 — Obtención de elementos a partir de la ecuación ordinaria]]
---
**Índice de Curso:** 1. Introducción | 2. Parábola | 3. Circunferencia | 4. **Elipse** | 5. Hipérbola
```

---

## 1. Relevancia y Aplicaciones: ¿Por qué abrir la "Caja Negra"?

Como expertos, debemos entender que la **ecuación general** ($Ax^2 + Cy^2 + Dx + Ey + F = 0$) es una "caja negra": sabemos que hay una elipse dentro, pero no podemos ver su corazón. Nuestro objetivo es transformarla a la **forma canónica**, que actúa como una radiografía revelando el centro $(h, k)$, los semiejes y la orientación.

### Aplicaciones de Alto Impacto
*   **Optimización Financiera en el Espacio ($USD):** Las órbitas de satélites comerciales son elípticas. Al convertir la ecuación general de una trayectoria, los ingenieros calculan el *perigeo* y el *apogeo*. Esto permite optimizar el encendido de motores, ahorrando millones de **$USD** en combustible al aprovechar la gravedad en puntos específicos.
*   **Arquitectura y Estructuras:** En la construcción de arcos elípticos, la forma canónica es indispensable para ubicar los puntos de apoyo exactos donde la carga se distribuye sin colapsar la estructura.
*   **Acústica Médica y Urbana:** En las "salas de los susurros" o en equipos de litotricia médica, se usa la propiedad de reflexión de los focos. Sin la forma canónica, sería imposible ubicar con precisión milimétrica dónde debe situarse el emisor y el receptor.

---

## 2. El Concepto Clave: El Círculo "Estirado"

Si tienes 12 años, imagina que una elipse es un círculo hecho de una liga de hule. Si clavas dos tachuelas (focos) en una tabla y estiras la liga alrededor de ellas, obtienes una elipse. La forma canónica es simplemente la instrucción matemática que nos dice qué tan lejos están las tachuelas y cuánto estiramos la liga en cada dirección.

```ad-warning
title: ¡Cuidado con la Balanza!
El error más catastrófico al completar el cuadrado es sumar un número en el lado derecho de la ecuación olvidando que, en el lado izquierdo, ese número está siendo **afectado por un factor común**. Si sumas 9 dentro de un paréntesis multiplicado por 4, ¡en realidad estás sumando 36! Debes sumar 36 en el lado derecho para mantener el equilibrio.
```

```ad-tip
title: El Truco de "La Mitad al Cuadrado"
Para completar cualquier trinomio cuadrado perfecto de la forma $x^2 + bx$, el término faltante siempre es:
$$\left(\frac{b}{2}\right)^2$$
Toma el coeficiente central, divídelo entre dos y elévalo al cuadrado. ¡Nunca falla!
```

---

## 3. Procedimiento Maestro Paso a Paso

Para extraer la información de la ecuación general, aplicaremos este algoritmo de precisión:

1.  **Agrupar y Transponer:** Reúne términos de $x$ con $x$, $y$ con $y$. Despeja el término independiente (el número sin letra) al lado derecho.
2.  **Factorizar Coeficientes (Dejar la variable sola):** Si $x^2$ o $y^2$ tienen un coeficiente distinto de 1, extráelo como factor común. **Ojo:** Solo factoriza el número, no la variable.
3.  **Completar y Balancear:** Aplica "la mitad al cuadrado" dentro de los paréntesis. Inmediatamente, suma el resultado en el lado derecho multiplicándolo por el factor común externo.
4.  **Binomios y Normalización:** Factoriza los trinomios en binomios al cuadrado $(x-h)^2$ y $(y-k)^2$. Finalmente, divide toda la ecuación por el número del lado derecho para igualar a 1.

---

## 4. Sección de Ejemplos Magistrales

### Ejemplo 1: Flujo de Trabajo Limpio
**Ecuación:** $3x^2 + 12x + 8y^2 + 48y + 60 = 0$

1.  **Agrupación:** $3(x^2 + 4x) + 8(y^2 + 6y) = -60$
2.  **Completar:** 
    - Para $x$: $(4/2)^2 = 4$. 
    - Para $y$: $(6/2)^2 = 9$.
3.  **Balanceo:** $3(x^2 + 4x + 4) + 8(y^2 + 6y + 9) = -60 + 3(4) + 8(9)$
    $$-60 + 12 + 72 = 24$$
4.  **Canónica:** $\frac{3(x+2)^2}{24} + \frac{8(y+3)^2}{24} = \frac{24}{24} \implies \mathbf{\frac{(x+2)^2}{8} + \frac{(y+3)^2}{3} = 1}$$

### Ejemplo 2: El Desafío de los Signos
**Ecuación:** $4x^2 - 40x + 9y^2 + 54y + 145 = 0$

Aquí el término $-40x$ requiere atención. Al factorizar el 4, mantenemos el signo: $4(x^2 - 10x)$. Al completar el cuadrado, $(-10/2)^2 = 25$.
$$4(x^2 - 10x + 25) + 9(y^2 + 6y + 9) = -145 + 100 + 81$$
$$4(x-5)^2 + 9(y+3)^2 = 36$$
Dividiendo entre 36: $$\mathbf{\frac{(x-5)^2}{9} + \frac{(y+3)^2}{4} = 1}$$

### Ejemplo 3: El "Coeficiente 1" (La Trampa de la Simplicidad)
**Ecuación:** $4x^2 - 16x + y^2 + 2y + 1 = 0$

**Nota del Docente:** Cuando el coeficiente es 1 (como en $y^2$), el factor común es implícito. No intentes inventar un proceso complejo; solo agrupa.
1. $4(x^2 - 4x) + (y^2 + 2y) = -1$
2. $4(x^2 - 4x + 4) + (y^2 + 2y + 1) = -1 + 16 + 1 = 16$
3. $4(x-2)^2 + (y+1)^2 = 16$
4. $$\mathbf{\frac{(x-2)^2}{4} + \frac{(y+1)^2}{16} = 1}$$

### Ejemplo 4: Análisis de Costos de Producción ($USD)
**Situación:** Una fábrica de microchips define su eficiencia mediante la variable $x$ (unidades producidas en miles) y $y$ (costo de materia prima). El punto de equilibrio operativo sigue la curva: $36x^2 - 216x + 5y^2 + 279 = 0$.

1.  **Factorización:** $36(x^2 - 6x) + 5y^2 = -279$
2.  **Completar:** $36(x^2 - 6x + 9) + 5y^2 = -279 + 324 = 45$
3.  **Factorizar:** $36(x-3)^2 + 5y^2 = 45$
4.  **División por 45:** $\frac{36(x-3)^2}{45} + \frac{5y^2}{45} = 1 \implies \frac{4(x-3)^2}{5} + \frac{y^2}{9} = 1$

```ad-abstract
title: Truco Avanzado: Fracción de Fracción
Cuando la simplificación no elimina el número de arriba (como el 4 sobre el 5), aplicamos la "ley de extremos y medios" a la inversa. El numerador del coeficiente baja como denominador del denominador.
**Resultado Final:**
$$\frac{(x-3)^2}{5/4} + \frac{y^2}{9} = 1$$
*Interpretación:* El centro $(3, 0)$ es el "Punto Operativo Ideal". Los denominadores representan la dispersión de costos en **$USD**.
```

---

## 5. Ejercicios de Práctica

### 🟢 Nivel Fácil (Estructuras Simples)
1. $x^2 + 4y^2 - 6x - 16y + 21 = 0$
2. $9x^2 + y^2 + 18x - 4y + 4 = 0$
3. $x^2 + 4y^2 - 10x - 8y + 25 = 0$
4. $4x^2 + 9y^2 - 8x + 36y + 4 = 0$

### 🟡 Nivel Medio (Manejo de Coeficientes)
5. $4x^2 + 9y^2 - 16x + 18y - 11 = 0$
6. $10x^2 + 3y^2 - 100x + 18y + 247 = 0$
7. $4x^2 + y^2 - 16x + 2y + 1 = 0$
8. $9x^2 + 4y^2 - 54x + 16y + 61 = 0$

### 🔴 Nivel Avanzado (Aplicaciones Financieras $USD)
9. **Costo de Infraestructura:** $45x^2 + 2y^2 + 8y - 37 = 0$ (Utiliza "fracción de fracción").
10. **Presupuesto de Mercadeo:** $15x^2 + y^2 + 4y + 1 = 0$ (Iguala a 1 dividiendo entre 30).
11. **Riesgo Logístico:** $3x^2 + 24x + 2y^2 - 4y + 44 = 0$
12. **Inversión de Capital:** $4x^2 + 2y^2 + 8y + 5 = 0$. Si el resultado es $\frac{x^2}{3/4} + \frac{(y+2)^2}{3/2} = 1$, ¿qué significa físicamente el denominador $3/4$ si $x$ representa miles de **$USD**?

---

## 6. Respuestas para el Docente

1. $\frac{(x-3)^2}{4} + \frac{(y-2)^2}{1} = 1$
2. $\frac{(x+1)^2}{1} + \frac{(y-2)^2}{9} = 1$
3. $\frac{(x-5)^2}{4} + \frac{(y-1)^2}{1} = 1$
4. $\frac{(x-1)^2}{9} + \frac{(y+2)^2}{4} = 1$
5. $\frac{(x-2)^2}{9} + \frac{(y+1)^2}{4} = 1$
6. $\frac{(x-5)^2}{3} + \frac{(y+3)^2}{10} = 1$
7. $\frac{(x-2)^2}{4} + \frac{(y+1)^2}{16} = 1$
8. $\frac{(x-3)^2}{4} + \frac{(y+2)^2}{9} = 1$
9. $\frac{x^2}{1} + \frac{(y+2)^2}{45/2} = 1$
10. $\frac{x^2}{1/15} + \frac{(y+2)^2}{3} = 1$
11. $\frac{(x+4)^2}{2} + \frac{(y-1)^2}{3} = 1$
12. $\frac{x^2}{3/4} + \frac{(y+2)^2}{3/2} = 1$. *Interpretación:* Significa que la varianza de la inversión en el eje $x$ es de $0.75$ unidades de millar de **$USD**.

---

## 7. Mini-Prueba de Autoevaluación

```ad-question
title: Autoevaluación de Conceptos
1. **Poder de Balanceo:** Si factorizas un $6$ y dentro del paréntesis sumas un $16$ para completar el trinomio, ¿qué valor exacto debes sumar al otro lado para no arruinar la ecuación?
   *(Respuesta: 96)*

2. **La Regla:** Para la expresión $y^2 + 18y$, ¿qué número completa el trinomio cuadrado perfecto?
   *(Respuesta: 81)*

3. **Interpretación $USD:** En un modelo de costos elíptico, si el denominador $b^2$ es $49$, ¿cuántas unidades de costo representa el semieje vertical?
   *(Respuesta: 7 unidades)*
```

---

## 8. Notas Finales y Puente Educativo

¡Enhorabuena! Has pasado de ver una cadena de números sin sentido a interpretar la geometría oculta en una ecuación general. Este es el paso más técnico en el estudio de las cónicas. En la siguiente clase, utilizaremos estos resultados para dibujar la elipse y predecir su comportamiento en el plano cartesiano.

```ad-info
title: 🧭 Navegación Final
- **Anterior:** [[Clase 04 — La elipse: Conceptos básicos y elementos]]
- **Siguiente:** [[Clase 06 — Obtención de elementos a partir de la ecuación ordinaria]]
```