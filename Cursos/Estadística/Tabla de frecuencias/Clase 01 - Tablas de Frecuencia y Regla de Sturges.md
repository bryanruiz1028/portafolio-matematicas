# Clase 01 — Tablas de Frecuencia y Regla de Sturges

#algebra #simplefrequency

> [!info] 🧭 Navegación
> - **Anterior:** [[Índice]]
> - **Siguiente:** [[Clase 02 — Gráficos Estadísticos]]

> [!info] 🌍 Relevancia y aplicaciones
> ¡Qué tal, amigas y amigos! Espero que estén muy bien. En esta clase vamos a ver cómo las tablas de frecuencia nos permiten organizar datos dispersos para entender comportamientos grupales de forma rápida y profesional.
> 
> - 💵 **Precios en $USD:** Identifica el rango de costo más común para tomar decisiones de compra.
> - 🏗️ **Construcción:** Controla el peso de materiales para asegurar la calidad de la obra.
> - 📊 **Educación:** Analiza las edades de un salón para planificar actividades según el grupo predominante.

---

> [!note] 📌 ¿Qué es Simple Frequency Table?
> Es una herramienta estadística para organizar cuántas veces se repite cada dato (como edades o notas). Como siempre les digo: "La idea es organizar el desorden para poder analizarlo".

> [!warning] ⚠️ Error común
> ¡Para que no se me pierdan! La suma de todas las frecuencias absolutas ($f$) **debe ser igual** al total de datos ($n$). Si el total no coincide, es porque algún dato se quedó sin tachar o lo contaste dos veces. 

> [!tip] 💡 Truco para recordarlo
> **Regla de la Acumulación:** La frecuencia acumulada ($F$) siempre termina en el número total de datos ($n$). Si llegas al final y el número es distinto, ¡toca revisar el conteo!

---

### Procedimiento paso a paso

```text
PASO 1 → Identificar el dato menor y el mayor para ordenar la columna (x).
PASO 2 → Realizar el conteo (tarjado) para obtener la frecuencia absoluta (f).
PASO 3 → Calcular la frecuencia acumulada (F) sumando en zigzag.
PASO 4 → Calcular el porcentaje (%) usando la fórmula:
         % = \frac{f \cdot 100}{n}
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico (Edades)
> Tenemos las edades de 30 estudiantes ($n=30$). 
> **Dato importante:** Aunque no haya estudiantes de 17 años, el Profe Alex recomienda incluirlo con frecuencia **0** para que la tabla sea útil en estudios futuros.
> - **Conteo:** 13 años (6), 14 años (11), 15 años (8), 16 años (4), **17 años (0)**, 18 años (1).
> - **Validación:** $6 + 11 + 8 + 4 + 0 + 1 = 30$. Como coincide con $n$, ¡vamos por buen camino!

> [!example] Ejemplo 2: Trabajo de "Detective" (Notas)
> Supongamos que tienes 40 notas de matemáticas ($n=40$), pero al sumar tus frecuencias solo te da 37. ¡Faltan datos! Al revisar, detectas que no tachaste un 25, un 31 y un 32. 
> - **Ajuste:** La frecuencia de la nota 25 sube de 2 a 3; la de 31 sube de 5 a 6; y la de 32 sube de 3 a 4. 
> - **Resultado:** Ahora la suma es exactamente 40. Siempre verifiquen sus tachados, amigos.

> [!example] Ejemplo 3: El truco del $n=40$ (Masa en kg)
> Cuando $n=40$, Profe Alex nos enseña a simplificar la fracción $100/40 = 2.5$. 
> - **De frecuencia a %:** Multiplicas $f \cdot 2.5$. Ejemplo: $14 \cdot 2.5 = 35\%$.
> - **De % a frecuencia:** Divides $\% / 2.5$. Si un intervalo tiene $35\%$, entonces $35 / 2.5 = 14$. 
> ¡Es mucho más rápido que usar la regla de tres completa!

> [!example] Ejemplo 4: Aplicación Real ($USD)
> Precios de 20 calculadoras: $15, 20, 15, 25, 20, 15, 30, 20, 25, 15, 20, 20, 15, 25, 20, 15, 20, 30, 15, 20.
> - **$15:** $f=7 \rightarrow \% = \frac{7 \cdot 100}{20} = 35\%$.
> - **$20:** $f=8 \rightarrow \% = \frac{8 \cdot 100}{20} = 40\%$.
> - **Total:** $n=20$ y la suma de porcentajes da $100\%$.

---

### Ejercicios para el estudiante

> [!abstract] Niveles de Práctica
> **🟢 Verde (Fácil):** Tienes los datos de "Número de hermanos" de 10 amigos: 0, 1, 1, 2, 0, 1, 2, 3, 1, 0. Construye la tabla y halla $f$ y $F$.
> 
> **🟡 Amarillo (Medio):** En una encuesta de "Días de ejercicio" ($n=25$), falta completar:
> - 1 día: $f = 6$ | 3 días: $f = 8$ | 5 días: $f = 1$.
> - Si el porcentaje de quienes hacen 4 días es $16\%$, ¿cuántos días faltan para los que hacen ejercicio 2 días?
> 
> **🔴 Rojo (Avanzado):** Para un estudio de 40 datos de "Gastos en cafetería ($USD)":
> 1. Calcula el número de intervalos ($k$) con la Regla de Sturges: $k = 1 + 3.322 \log_{10}(40)$.
> 2. **Regla de Oro:** Redondea el resultado al **número impar más cercano**, sin importar si el decimal es bajo.

---

### Respuestas para el docente

> [!success] Solucionario
> - **Verde:** $x=\{0, 1, 2, 3\}$, $f=\{3, 4, 2, 1\}$, $F=\{3, 7, 9, 10\}$.
> - **Amarillo:** 
>   - Frecuencia 4 días: $\frac{16 \cdot 25}{100} = 4$.
>   - Frecuencia 2 días: $25 - (6 + 8 + 4 + 1) = 6$.
>   - Porcentajes: 24%, 24%, 32%, 16%, 4% (Suma: 100%).
> - **Rojo:** 
>   - $k = 1 + 3.322(1.602) = 6.32$. 
>   - **Respuesta:** $k=7$. (Se redondea a 7 por la recomendación de usar el impar más cercano para una mejor simetría en la tabla).

---

### Mini-prueba de autoevaluación

> [!question] Verifica lo aprendido
> 1. **¿Para qué sirve la Regla de Sturges?** (Para sugerir cuántos intervalos o "filas" debe tener nuestra tabla).
> 2. **¿Cómo calculo la frecuencia relativa?** (Dividiendo la frecuencia absoluta entre el total: $f/n$).
> 3. **Si $n=200$ y un producto se repite 40 veces, ¿qué porcentaje tiene?** ( $(\frac{40 \cdot 100}{200}) = 20\%$ ).

---

> [!tip] 💡 En la próxima clase
> ¡No se lo pierdan! Usaremos estas tablas para crear **Gráficos Estadísticos (Histogramas y Polígonos de Frecuencia)**. ¡Nos vemos allá!

> [!info] 🧭 Navegación
> - **Anterior:** [[Índice]]
> - **Siguiente:** [[Clase 02 — Gráficos Estadísticos]]