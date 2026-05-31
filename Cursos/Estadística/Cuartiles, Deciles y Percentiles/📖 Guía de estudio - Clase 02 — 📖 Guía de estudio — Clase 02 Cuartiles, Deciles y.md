# 📖 Guía de estudio — Clase 02: Cuartiles, Deciles y Percentiles (Medidas de Posición)

> [!info] 📌 Conceptos clave
> 1. **¿Qué son las medidas de posición?**: Son indicadores (cuartiles, deciles y percentiles) que dividen un conjunto de datos ordenados en partes porcentuales iguales para identificar dónde se sitúa un valor respecto al total.
> 2. **La importancia de la frecuencia acumulada ($F_i$)**: Es nuestra brújula. Para localizar cualquier medida, siempre buscamos el valor de la "posición" en la columna de frecuencias acumuladas.
> 3. **Rango Intercuartílico ($IQR$)**: Se define como la diferencia entre el tercer y el primer cuartil ($Q_3 - Q_1$). Representa la dispersión del 50% central de los datos, eliminando la influencia de valores extremos.
> 4. **La Regla de Oro**: Si al calcular la posición el resultado coincide **exactamente** con un valor de la columna $F_i$, no es necesario aplicar la fórmula extensa. El resultado de la medida de posición es automáticamente el **límite superior ($L_s$)** de ese intervalo.

## 2. Fórmulas y definiciones importantes

Para dominar estas medidas, es vital distinguir entre la **posición** (el "localizador" o lugar que ocupa el dato) y el **valor** de la medida.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Posición (Cuartiles)** | $\frac{k \cdot n}{4}$ (Divide en 4 partes de 25% cada una) |
| **Posición (Deciles)** | $\frac{k \cdot n}{10}$ (Divide en 10 partes de 10% cada una) |
| **Posición (Percentiles)** | $\frac{k \cdot n}{100}$ (Divide en 100 partes de 1% cada una) |
| **Límite Inferior ($L_i$)** | Valor mínimo del intervalo donde se localizó la posición. |
| **Amplitud ($A$)** | Tamaño del intervalo ($L_s - L_i$). |
| **Frecuencias ($F_{i-1}, F_i$)** | $F_{i-1}$ es la frecuencia acumulada anterior al intervalo y $F_i$ es la del intervalo actual. Nota: $F_i - F_{i-1}$ equivale a la frecuencia absoluta ($f_i$). |

### Fórmula General para Datos Agrupados
$$Medida = L_i + A \cdot \left[ \frac{\text{Posición} - F_{i-1}}{F_i - F_{i-1}} \right]$$

---

## 3. Ejemplos resueltos adicionales

> [!example] Ejemplo A — Cálculo de Cuartiles (Edades)
> **Problema:** Hallar el primer cuartil ($Q_1$) en un estudio de 60 personas ($n=60$).
> 1. **Hallar posición:** $\frac{1 \cdot 60}{4} = 15$. 
>    *⚠️ ¡Atención! El 15 es el localizador, no la edad.*
> 2. **Identificar intervalo:** Buscamos 15 en la columna $F_i$. Al no estar exacto, tomamos el primer valor que lo contiene, que es **22**. Esto nos sitúa en el intervalo **40 - 45**.
>    * $L_i = 40$
>    * $A = 5$
>    * $F_{i-1} = 10$ (frecuencia acumulada anterior).
>    * $F_i = 22$ (frecuencia acumulada actual).
> 3. **Aplicar fórmula:**
>    $$Q_1 = 40 + 5 \cdot \left[ \frac{15 - 10}{22 - 10} \right] = 40 + 5 \cdot \left[ \frac{5}{12} \right] = 40 + 2,08$$
> 
> **✅ Resultado:** 42,08 años.

> [!example] Ejemplo B — Análisis de Salarios ($USD)
> **Problema:** Hallar el Percentil 40 ($P_{40}$) de 100 empleados ($n=100$) agrupados en intervalos.
> 1. **Hallar posición:** $\frac{40 \cdot 100}{100} = 40$.
> 2. **Identificar intervalo:** El valor 40 no está en $F_i$. El primer valor que lo contiene es **71**. El intervalo correspondiente es **30 - 40 USD**.
>    * $L_i = 30$
>    * $A = 10$
>    * $F_{i-1} = 39$
>    * $F_i = 71$
> 3. **Cálculo:**
>    $$P_{40} = 30 + 10 \cdot \left[ \frac{40 - 39}{71 - 39} \right] = 30 + 10 \cdot \left[ \frac{1}{32} \right] = 30 + 0,3125$$
> 
> **✅ Resultado:** 30,3 USD (Aproximado).

---

## 4. Ejercicios de repaso

> [!abstract] 🟢 Fácil (Localización)
> En una muestra de **50 personas**, determine únicamente el valor de la **posición** ($k \cdot n / 4$) para $Q_1$, $Q_2$ y $Q_3$.

> [!abstract] 🟡 Medio (Deciles)
> Utilizando una tabla de **100 alumnos**, calcule el **Decil 2 ($D_2$)**. 
> *   *Datos extra:* $L_i = 20$, $A = 10$, $F_{i-1} = 14$, $F_i = 39$.

> [!abstract] 🔴 Avanzado (Aplicación y Análisis)
> Se analizan los costos de producción de una empresa. Calcule el **Rango Intercuartílico ($IQR$)** si se sabe que $Q_3 = 67,36$ USD y $Q_1 = 51,66$ USD.
> **Reto:** Redacte una breve conclusión sobre qué significa este valor para la estabilidad de los costos del negocio.

---

## 5. 💡 Consejo de estudio

> [!tip] 💡 ¡Cuidado con el orden de las operaciones!
> Es el error más común en los exámenes. Para que el resultado sea correcto, respeta estrictamente esta jerarquía:
> 
> 1. **Primero los paréntesis:** Resuelve las restas internas y luego la división.
> 2. **Multiplicación por la Amplitud ($A$):** Toma el resultado del paréntesis y multiplícalo por $A$.
> 3. **Suma del Límite Inferior ($L_i$):** Este es siempre el **último paso**.
> 
> **🚫 Error a evitar:** Nunca sumes $L_i + A$ al principio del ejercicio.

---
### 🗝️ Clave de respuestas

*   **Nivel Verde:** Posición $Q_1 = 12,5$; Posición $Q_2 = 25$; Posición $Q_3 = 37,5$.
*   **Nivel Amarillo:** $D_2 = 22,4$ respuestas correctas.
*   **Nivel Rojo:** $IQR = 15,7$ USD. *Interpretación:* Indica que el 50% de los costos más frecuentes de la empresa oscilan en un rango de 15,7 USD, lo cual muestra la dispersión del "corazón" de la distribución sin verse afectado por costos extremadamente altos o bajos.