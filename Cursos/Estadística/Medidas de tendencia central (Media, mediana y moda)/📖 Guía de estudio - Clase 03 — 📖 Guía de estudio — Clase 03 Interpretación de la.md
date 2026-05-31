# 📖 Guía de estudio — Clase 03: Interpretación de las Medidas de Tendencia Central

> [!info] 📌 Conceptos clave
> En estadística, calcular un número es solo la mitad del trabajo. La verdadera magia ocurre cuando explicamos qué significa ese resultado en la vida real.
> - **Interpretación vs. Cálculo:** No basta con decir que el resultado es "15"; hay que explicar si son años, dólares o hermanos, y qué representan para el grupo.
> - **Media (Promedio):** Es el valor "equilibrado". A veces da decimales que parecen imposibles (como "2.5 hijos"), pero se mantiene así porque es un valor matemático. Siempre usamos la frase **"en promedio"** para explicarlo.
> - **Mediana:** Es el corazón de los datos. Divide al grupo en dos partes exactamente iguales: el 50% de los datos es menor o igual a ella, y el otro 50% es mayor o igual.
> - **Moda:** Es el dato que más se repite (el de mayor frecuencia). **¡Cuidado con la trampa!** Nunca digas "la mayoría". Por ejemplo: si en un grupo de 10 personas, 3 prefieren el color azul, 2 el rojo y 5 otros colores distintos, el azul es la moda porque es el más frecuente, pero *no es la mayoría* (ya que 7 personas prefieren otros colores).

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Media ($\bar{x}$)** | Es el promedio aritmético. Se suman todos los valores y se dividen por el total. <br> **Fórmula para datos agrupados:** $\frac{\sum (x_i \cdot f_i)}{n}$ <br> *(¡No te asustes por el símbolo $\sum$! Solo significa que debemos sumar los resultados de la columna).* |
| **Mediana ($Me$)** | Es el valor central que divide la muestra en dos partes de 50%. En tablas de intervalos, usamos el límite inferior ($L_i$) y la **frecuencia acumulada anterior ($F_{i-1}$)**. <br> **Nota vital:** No confundas $f_i$ (frecuencia simple) con $F_i$ (frecuencia acumulada, en mayúscula). |
| **Moda ($Mo$)** | Es el valor con más frecuencia absoluta. Un conjunto puede ser bimodal (dos modas) o multimodal (varias modas) si hay un empate en la frecuencia más alta. |

## Ejemplos Resueltos Adicionales

```ad-example
title: Interpretación de edades en un grupo
**Contexto:** Analizamos las edades de 9 amigos: 14, 14, 15, 15, 15, 16, 17, 17, 18.

**Valores obtenidos:**
- Media ($\bar{x}$): 15.6 años.
- Mediana ($Me$): 15 años.
- Moda ($Mo$): 15 años.

**Interpretaciones correctas:**
1. **Media:** "El promedio de las edades de estos nueve amigos es de 15.6 años".
2. **Mediana:** "El 50% de los amigos tiene una edad menor o igual a 15 años" (o también: "La mitad de los amigos tiene una edad superior o igual a 15 años").
3. **Moda:** "La edad con más frecuencia (la que más se repite) entre los amigos es 15 años".
```

```ad-example
title: Análisis de sueldos en una empresa
**Contexto:** Se realizó un estudio a 70 trabajadores para entender sus salarios.

**Valores obtenidos:**
- Media ($\bar{x}$): $1,000 USD.
- Mediana ($Me$): $947 USD.
- Moda ($Mo$): $950 USD.

**Interpretaciones correctas:**
1. **Media:** "Los trabajadores de la empresa ganan, en promedio, un sueldo de $1,000 USD".
2. **Mediana:** "La mitad de los empleados percibe un salario inferior o igual a $947 USD".
3. **Moda:** "El sueldo más frecuente entre los empleados es de $950 USD".
```

## Ejercicios de Repaso

```ad-abstract
title: Nivel 🟢 Fácil: Hermanos en el curso
Se preguntó a los estudiantes cuántos hermanos tienen y el resultado fue:
- **Media:** 3 hermanos.
- **Moda:** 2 hermanos.

**Tarea:** Redacta la interpretación de estos dos valores usando las frases aprendidas en clase.
```

```ad-abstract
title: Nivel 🟡 Medio: Crecimiento familiar
En una encuesta a 50 familias sobre el "número de hijos", los cálculos arrojaron:
- **Media:** 2.5
- **Mediana:** 2

**Tarea:** 
1. Redacta la interpretación de la media explicando por qué usamos la frase **"en promedio"** aunque no existan "medios hijos".
2. Redacta la interpretación de la mediana mencionando el concepto del 50%.
```

```ad-abstract
title: Nivel 🔴 Avanzado: Horas laboradas
Un análisis de las horas trabajadas por 130 empleados muestra:
- **Mediana:** 72.2 horas.
- **Moda:** 74.28 horas.

**Tarea:** 
1. Redacta la interpretación de la mediana con total precisión decimal.
2. Explica por qué sería un error decir que "la mayoría de los empleados trabaja 74.28 horas".
3. Redacta la forma técnicamente correcta de interpretar esa moda.
```

> [!tip] 💡 Consejo de estudio: La Prueba de Coherencia
> Al usar fórmulas complejas en tablas de intervalos, es fácil cometer un pequeño error (como le pasó al Profe Alex en el video al escribir un 5 en lugar de un 15). Para evitarlo, aplica siempre la **Prueba de Coherencia**: El resultado de tu Mediana o Moda **DEBE** estar dentro del rango del intervalo que seleccionaste. Si tu intervalo es [70 - 75] y tu resultado es 54, ¡detente! Algo salió mal en el cálculo. ¡Revisa siempre tus límites!