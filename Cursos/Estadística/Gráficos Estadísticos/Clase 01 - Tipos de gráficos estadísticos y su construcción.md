# Clase 01 — Tipos de gráficos estadísticos y su construcción
tags: #algebra #tiposdegrficose
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

---

### 1. ¿Por qué es importante esta clase?

Visualizar datos no es simplemente hacer dibujos; es transformar una lista de números desordenados en una herramienta poderosa para entender la realidad. Al organizar la información visualmente, podemos identificar tendencias, comparar resultados de forma inmediata y tomar decisiones informadas basadas en hechos.

> [!info] 🌍 Relevancia y aplicaciones
> - 💸 **$USD y Negocios:** Analizar el crecimiento de suscriptores o la demanda de servicios para proyectar ingresos y presupuestos reales.
> - 🏗️ **Construcción y Manufactura:** Organizar medidas técnicas en intervalos para diseñar productos eficientes (por ejemplo, diseñar sillas ergonómicas calculadas para el rango de masa corporal de 33-51 kg).
> - 🏠 **Situaciones Cotidianas:** Interpretar encuestas sobre gustos personales o hábitos de salud para entender mejor el comportamiento de nuestra comunidad.

---

### 2. Concepto clave: Los gráficos estadísticos

Un gráfico estadístico es una representación visual de datos organizados previamente en una tabla de frecuencias. Para elegir el gráfico correcto, debemos observar cómo están agrupados nuestros datos:

*   **Gráfico de Barras:** Se usa cuando los datos son **cualitativos** (categorías como "deportes") o **cuantitativos discretos** (números puntuales como "13 años", "14 años"). Las barras representan categorías individuales y separadas.
*   **Histograma:** Se utiliza exclusivamente para datos **cuantitativos continuos** agrupados en **intervalos** (por ejemplo, "estudiantes que pesan entre 33kg y 36kg"). Aquí las barras representan continuidad.

> [!note] La Marca de Clase (Midpoint)
> En el histograma, existe un punto vital llamado **Marca de Clase**. Es el número que está justo en la mitad de cada intervalo (por ejemplo, entre 33 y 36, la marca es 34.5). Este punto es fundamental porque representa a todo el grupo y será la base para nuestros futuros gráficos de líneas.

> [!warning] ¡Error común de dibujo!
> Nunca pegues las barras en un gráfico de barras simple; deben estar separadas para mostrar que son categorías distintas. Por el contrario, en un histograma, las barras **deben ir pegadas** obligatoriamente para representar que donde termina un rango empieza el siguiente.

> [!tip] Regla mnemotécnica
> **B**arras = **B**astantes huecos (separadas).
> **H**istograma = **H**ermanadas (pegadas).

---

### 3. Procedimiento paso a paso: Construcción profesional

Para que un gráfico sea una herramienta útil y no solo un dibujo, debe seguir estándares profesionales de claridad:

```text
PASO 1: Dibujar los ejes
- Eje Horizontal (X): Ubicamos los datos o categorías (edades, marcas de clase o límites de peso).
- Eje Vertical (Y): Ubicamos las frecuencias (cantidad de personas, viajes, etc.).

PASO 2: Definir una escala constante
- Los números en el eje vertical deben ir en orden ascendente (0, 2, 4, 6...).
- La distancia entre números debe ser SIEMPRE la misma (si eliges ir de 3 en 3, mantén ese ritmo).
- Asegúrate de que la escala supere el valor más alto de tus datos.

PASO 3: Rotulado obligatorio (Identidad del gráfico)
- Escribe un título descriptivo.
- Etiqueta el eje horizontal (ej: "Masa corporal en kg").
- Etiqueta el eje vertical (ej: "Número de estudiantes").
- ¡IMPORTANTE!: Un gráfico sin etiquetas en los ejes es INÚTIL e ilegible para los demás.

PASO 4: Dibujo de barras
- Gráfico de barras: Barras del mismo ancho, centradas sobre el dato y separadas.
- Histograma: Barras pegadas, usando los límites de los intervalos (ej: del 33 al 36).
```

> [!warning] ¡Error de escala en el eje vertical!
> Un error muy común de principiante es escribir las frecuencias de tu tabla (ej: 1, 9, 14, 7...) directamente en el eje vertical. **¡No lo hagas!** Debes crear una escala regular (ej: de 2 en 2 o de 5 en 5) y luego subir la barra hasta donde corresponda según esa escala.

---

### 4. Ejemplos prácticos

```ad-example
title: Ejemplo 1: Edades de estudiantes (Barras)
Se registran edades puntuales: 13, 14, 15, 16 y 18 años. Al ser datos discretos, usamos un **Gráfico de Barras**. Si 11 personas tienen 14 años, la barra sobre el "14" subirá hasta el nivel 11 en tu escala vertical, dejando un espacio libre respecto a la barra de los 13 años.
```

```ad-example
title: Ejemplo 2: Demanda de viajes (El peligro de la escala)
En un gráfico de demanda, la barra del año 2020 llega al número "84". Sin embargo, el eje vertical indica "en miles". El error común es pensar que se vendieron 84 viajes. La realidad profesional es que se vendieron **84,000 viajes**. Siempre revisa las unidades del eje.
```

```ad-example
title: Ejemplo 3: Masa corporal (Histograma y Marca de Clase)
Para datos de peso entre 33kg y 51kg, agrupados en intervalos (33-36, 36-39...), usamos un **Histograma**. Las barras nacen en el 33 y mueren en el 36, donde inmediatamente nace la siguiente. En la mitad de cada barra (en el 34.5, 37.5, etc.) se ubica la **marca de clase**.
```

```ad-example
title: Ejemplo 4: Aplicación financiera ($USD)
Si el canal de "Matemáticas Profe Alex" tiene 125.1 "miles de suscriptores" en enero y cada suscripción valiera 1 $USD, el ingreso no es de 125 dólares. El cálculo correcto es: 
$125.1 \times 1,000 = \mathbf{125,100 \text{ USD}}$.
```

---

### 5. Ejercicios y solucionario

```ad-abstract
title: Nivel Fácil: Identificación
¿Qué tipo de gráfico (Barras o Histograma) usarías para representar:
1. Los deportes favoritos (fútbol, baloncesto, voleibol) de un grupo.
2. La estatura de personas agrupada en rangos de 150-160cm y 160-170cm.
```

```ad-abstract
title: Nivel Medio: Interpretación de datos
Basándote en los datos del Profe Alex: En enero de 2020 hubo 100 (en miles) de suscriptores y en enero de 2021 hubo 125.1 (en miles). ¿Cuál fue el aumento exacto de personas suscritas?
```

```ad-abstract
title: Nivel Avanzado: Aplicación financiera
En 2019 se vendieron 470 (en miles) viajes y en 2020 se vendieron 84 (en miles). Si cada viaje genera una ganancia de 10 $USD, ¿cuántos dólares **menos** ingresaron en 2020 en comparación con 2019?
```

```ad-success
title: Solucionario
**Fácil:** 1. Barras (cualitativo). 2. Histograma (intervalos).
**Medio:** $125,100 - 100,000 = \mathbf{25,100 \text{ suscriptores}}$.
**Avanzado:** 
Diferencia de viajes: $470,000 - 84,000 = 386,000 \text{ viajes menos}$.
Diferencia en dinero: $386,000 \times 10 = \mathbf{3,860,000 \text{ USD menos}}$.
```

---

### 6. Autoevaluación (Mini-prueba)

```ad-question
title: Pregunta 1
¿Cuál es la diferencia visual obligatoria entre un histograma y un gráfico de barras?
A) Los colores llamativos.
B) Que en el histograma las barras van pegadas para mostrar continuidad.
C) Que el histograma no necesita eje horizontal.

**Respuesta:** B. Las barras "hermanadas" indican que los intervalos son continuos.
```

```ad-question
title: Pregunta 2
¿Por qué es un error grave copiar los números de la tabla de frecuencias directamente en el eje vertical?
A) Porque el gráfico se vería desproporcionado y no seguiría una escala lógica.
B) Porque los números deben ser siempre negativos.
C) Porque solo se pueden usar números primos.

**Respuesta:** A. Un gráfico profesional requiere una escala constante (ej. de 2 en 2) para comparar alturas de forma real.
```

```ad-question
title: Pregunta 3
Si un gráfico muestra una barra en el número 379.2 y el eje dice "en miles", ¿cuál es la cifra real?
A) 3,792
B) 379,200
C) 37,920

**Respuesta:** B. $379.2 \times 1,000 = 379,200$.
```

---

### 7. Cierre y conexión

Dominar la construcción de barras e histogramas es la base de la estadística descriptiva. Estos gráficos nos permiten "ver" la realidad de un solo vistazo.

> [!tip] 💡 En la próxima clase
> Aprenderemos sobre el **Polígono de Frecuencias**. Para construirlo, usaremos las **marcas de clase** (los puntos medios de las barras) que mencionamos hoy. ¡Será el paso final para visualizar tendencias de crecimiento!

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]