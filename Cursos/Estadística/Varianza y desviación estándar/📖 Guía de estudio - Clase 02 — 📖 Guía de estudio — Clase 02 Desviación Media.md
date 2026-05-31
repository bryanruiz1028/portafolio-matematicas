# 📖 Guía de estudio — Clase 02: Desviación Media

> [!info] 📌 Conceptos clave
> - **Desviación respecto a la media:** Es la diferencia o distancia que existe entre un dato específico de la variable $x$ y el promedio ($\bar{x}$) del conjunto. Se expresa siempre en valor absoluto para medir la distancia pura, sin importar si el dato es mayor o menor a la media.
> - **Desviación Media ($DM$):** Es una medida de dispersión que indica el promedio de todas las desviaciones de los datos. Nos permite entender qué tan alejados están, en promedio, los valores respecto a su media aritmética.
> - **Importancia del valor absoluto ($| \dots |$):** Se utiliza para convertir resultados negativos en positivos. Esto evita que las distancias se "anulen" entre sí al sumarlas, lo cual daría un error en la interpretación de la dispersión.
> - **La Media aritmética ($\bar{x}$) como referencia:** Es el "punto de equilibrio" del conjunto de datos. Es obligatorio calcularla primero, ya que sin ella no tenemos el punto de comparación para hallar las desviaciones.

---

## 2. FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición y Fórmula |
| :--- | :--- |
| **Media aritmética ($\bar{x}$)** | **Datos no agrupados:** $\bar{x} = \frac{\sum x}{n}$ <br> **Datos agrupados:** $\bar{x} = \frac{\sum x \cdot f}{n}$ |
| **Marca de clase ($x$)** | Punto medio de un intervalo: $x = \frac{\text{Límite inferior} + \text{Límite superior}}{2}$ |
| **Desviación Media ($DM$)** | Promedio de las desviaciones absolutas: $DM = \frac{\sum |x - \bar{x}| \cdot f}{n}$ |
| **Número de datos ($n$)** | Tamaño total de la muestra: $n = \sum f$ |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A: Caso de edades (Datos agrupados puntualmente)
**Contexto:** Análisis de las edades de $n=60$ estudiantes.

**Proceso:**
1. **Cálculo de la media ($\bar{x}$):** Multiplicamos cada edad por su frecuencia. La suma de estos productos ($\sum x \cdot f$) fue $916$. 
   $\bar{x} = \frac{916}{60} = 15.26$ años.
2. **Cálculo de desviaciones ponderadas:** Restamos cada edad menos la media, aplicamos valor absoluto y multiplicamos por su frecuencia ($|x - \bar{x}| \cdot f$). La suma de esta columna resultó en $61.2$.
3. **Aplicación de la fórmula final:** $DM = \frac{61.2}{60}$.

**Resultado:** $DM = 1.02$ años. Esto indica que, en promedio, las edades de los estudiantes se separan de la media apenas un año.
```

```ad-example
title: Ejemplo B: Caso de rangos de edad (Datos en intervalos)
**Contexto:** Edades de $n=20$ personas organizadas en rangos (ej. 30-35 años).

**Proceso:**
1. **Hallar Marcas de clase ($x$):** Calculamos el punto medio de cada intervalo. 
   *Ejemplo para el rango 30-35:* $x = \frac{30+35}{2} = 32.5$.
2. **Cálculo de la media ($\bar{x}$):** Multiplicamos cada marca de clase por su frecuencia. La suma total fue $845$.
   $\bar{x} = \frac{845}{20} = 42.25$ años.
3. **Suma de desviaciones:** Calculamos $|x - \bar{x}| \cdot f$ para cada fila. La suma total de estas desviaciones ponderadas dio $77$.
4. **Cálculo final:** $DM = \frac{77}{20} = 3.85$.

**Resultado:** $DM = 3.85$ años.
```

---

## 4. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Nivel Fácil: Datos No Agrupados
**Problema:** Se preguntó el número de hermanos a 7 personas: $3, 0, 1, 0, 2, 0, 1$.
**Tarea:** Hallar primero el promedio ($\bar{x}$) y luego la Desviación Media ($DM$).
*(Referencia: $DM = 0.85$)*
```

```ad-abstract
title: 🟡 Nivel Medio: Datos Agrupados Puntualmente
**Problema:** Completa la tabla de frecuencias para un total de $n=17$ datos:
- Datos ($x$): $5, 6, 7, 8, 9$
- Frecuencias ($f$): $3, 4, 2, 5, 3$
**Tarea:** Calcula la media aritmética $\bar{x}$ y aplica la fórmula de $DM$ paso a paso.
*(Referencia: $DM = 0.79$)*
```

```ad-abstract
title: 🔴 Nivel Avanzado: Datos en Intervalos
**Problema:** En un estudio con $n=20$ personas, se registraron edades en intervalos de 10 en 10: ($0-10, 10-20, 20-30, 30-40, 40-50$) con frecuencias $f$ de $1, 3, 9, 5, 2$ respectivamente.
**Tarea:** Realiza el proceso completo: determina marcas de clase $x$, calcula la media $\bar{x}$ y halla la $DM$.
*(Referencia: $DM = 6.95$)*
```

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Estrategia de organización
> Para dominar la estadística, el orden en tus tablas es fundamental. Sigue siempre este flujo de trabajo:
> 1.  **Suma las frecuencias ($f$):** Confirma siempre el valor de $n$ antes de empezar.
> 2.  **Calcula la media ($\bar{x}$) primero:** Es imposible hallar la desviación sin este valor central.
> 3.  **Verifica el valor absoluto:** Al llenar la columna $|x - \bar{x}|$, asegúrate de que **ningún** número sea negativo. Una sola resta negativa arruinará la suma final.
> 
> ¡Sigue practicando, verás que con cada ejercicio te vuelves más rápido y preciso! ¡Tú puedes!