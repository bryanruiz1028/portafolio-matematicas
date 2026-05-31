# Clase 02 — Regla de la suma y Unión de sucesos
tags: #algebra #regladelasuma
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 9

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La regla de la suma nos permite entender qué sucede cuando buscamos la probabilidad de que ocurra un evento, otro, o ambos a la vez. Es una herramienta esencial para organizar datos en la vida real:
> - 💵 **Cálculo de ingresos:** En una tienda de mascotas, permite proyectar ventas analizando la probabilidad de que un cliente compre un perro o un animal de color blanco.
> - 🏗️ **Planificación de suministros:** En eventos masivos (como una fiesta de $80$ personas), ayuda a prever gastos y comida según si los asistentes son extranjeros o mayores de edad.
> - 📊 **Toma de decisiones:** En salud y demografía, se usa para estudiar poblaciones combinando rasgos como el color de ojos o de cabello.

---

## Concepto clave

> [!note] 📌 ¿Qué es Regla de la suma?
> Es la regla que usamos para calcular la probabilidad de que ocurra el suceso $A$ **o** el suceso $B$. La clave para identificarla es la vocal **"o"**. Cuando veas un problema que pregunte por una opción "u" otra, estamos sumando posibilidades.

> [!warning] ⚠️ Error común
> **Contar dos veces lo mismo:** El error más frecuente es olvidar que hay elementos que pertenecen a ambos grupos a la vez (la intersección).
> - ❌ **Incorrecto:** Sumar todos los perros y todos los animales blancos, olvidando que algunos perros *ya son blancos* y los estarías contando dos veces.
> - ✅ **Correcto:** Sumar (Perros) + (Blancos) - (Perros que son blancos).

> [!tip] 💡 Truco para recordarlo
> Usa siempre esta frase en tu mente: **"Suma los grupos, pero resta lo que se repite"**. Si no restas la intersección, el resultado será mayor a la realidad.

---

## Procedimiento Paso a Paso

```text
1. Definir los sucesos: Identificar claramente el suceso A y el suceso B.
2. Calcular probabilidades individuales: Hallar P(A) y P(B) por separado.
3. Identificar la intersección: Buscar si existen elementos que cumplen A y B al mismo tiempo.
4. Aplicar la resta: Usar la fórmula P(A o B) = P(A) + P(B) - P(A y B).
```

---

## Ejemplos

> [!example] Ejemplo 1: Tienda de mascotas (Caso básico)
> En una tienda con $15$ animales, hay $7$ perros y $5$ animales blancos. Sabemos que $3$ de esos perros son blancos. ¿Cuál es la probabilidad de elegir un perro **o** un animal blanco?
> - $P(\text{Perro}) = \frac{7}{15}$
> - $P(\text{Blanco}) = \frac{5}{15}$
> - $P(\text{Perro y Blanco}) = \frac{3}{15}$
> - **Cálculo:** $\frac{7}{15} + \frac{5}{15} - \frac{3}{15} = \frac{9}{15}$
> - **Resultado:** La probabilidad es $\frac{9}{15}$, que simplificado es $\frac{3}{5}$ o $60\%$.

> [!example] Ejemplo 2: El dado (Visualización de conjuntos)
> Al lanzar un dado de $6$ caras, ¿cuál es la probabilidad de que caiga un número **par** ($A$) o un número **mayor que 3** ($B$)?
> - **Conjunto A (Pares):** $\{2, 4, 6\}$
> - **Conjunto B (>3):** $\{4, 5, 6\}$
> - **Intersección (A ∩ B):** $\{4, 6\}$ (estos dos números se repiten).
> - **Cálculo:** $P(A) = \frac{3}{6}$, $P(B) = \frac{3}{6}$, $P(A \cap B) = \frac{2}{6}$
> - **Fórmula:** $\frac{3}{6} + \frac{3}{6} - \frac{2}{6} = \frac{4}{6}$ o $66.6\%$.

> [!example] Ejemplo 3: Rasgos físicos (Porcentajes)
> En una ciudad, el $60\%$ tiene ojos negros, el $80\%$ tiene cabello negro y el $50\%$ tiene ambos rasgos.
> - $P(\text{Ojos}) = 60\%$
> - $P(\text{Cabello}) = 80\%$
> - $P(\text{Ambos}) = 50\%$
> - **Cálculo:** $60\% + 80\% - 50\% = 90\%$.
> - **Análisis:** El $90\%$ de las personas tiene al menos uno de los dos rasgos negros.

> [!example] Ejemplo 4: Recaudación en fiesta (Aplicación real $USD)
> En una fiesta de $80$ personas, se decide cobrar una entrada de $\$10$ USD a todo aquel que sea **extranjero o mayor de 20 años**. Sabemos que $42$ personas cumplen con esa condición ($P = \frac{42}{80}$).
> - **Ingreso esperado:** Si multiplicamos el total de personas por la probabilidad y el costo:
> - $P(\text{Cobro}) = \frac{42}{80}$
> - **Cálculo:** $(\frac{42}{80}) \times 80 \text{ personas} \times \$10 = \$420$ USD.
> - **Resultado:** La recaudación total prevista es de $\$420$ USD.

---

## Ejercicios para el estudiante

### 🟢 Nivel: Fácil
1. Lanzar un dado: ¿Probabilidad de que caiga un número par o impar?
2. Lanzar un dado: ¿Probabilidad de que caiga $1$ o $6$?
3. Tienda de mascotas ($15$ animales total): Si hay $7$ perros y $6$ gatos, ¿probabilidad de que sea perro o gato?
4. Lanzar un dado: ¿Probabilidad de que caiga un número menor que $2$ o mayor que $5$?

### 🟡 Nivel: Medio
Utiliza la siguiente **Tabla de Contingencia** sobre una cena de $60$ personas para resolver los ejercicios:

| Género | Flan | Torta | **Total** |
| :--- | :---: | :---: | :---: |
| Mujeres | $20$ | $12$ | **$32$** |
| Hombres | $16$ | $12$ | **$28$** |
| **Total** | **$36$** | **$24$** | **$60$** |

1. ¿Probabilidad de que sea mujer o haya comido flan?
2. ¿Probabilidad de ser hombre o haber comido torta?
3. ¿Probabilidad de ser mujer o haber comido torta?
4. ¿Probabilidad de ser hombre o haber comido flan?

### 🔴 Nivel: Avanzado
1. En una fiesta de $80$ personas, si el costo por ser mayor de $20$ años o extranjero es de $\$10$ USD y hay $42$ personas en ese grupo, ¿cuál es la probabilidad exacta en porcentaje?
2. En la tienda de mascotas ($15$ animales), si un animal "perro o blanco" cuesta $\$50$ USD de mantenimiento mensual, ¿cuál es el gasto total esperado para ese grupo? (Usa los datos del Ejemplo 1).
3. Si en la ciudad el $90\%$ tiene ojos o cabello negro, ¿cuál es la probabilidad de encontrar a alguien que no tenga ninguno de los dos rasgos negros?
4. En la fiesta de $80$ personas: Hay $40$ mayores de edad, $70$ nativos y $32$ personas que son mayores y nativas a la vez. Calcula la probabilidad de que una persona sea mayor de $20$ años **o** nativa.

> [!success] ✅ Respuestas
> - **Fáciles:** 1) $\frac{6}{6} (100\%)$ | 2) $\frac{2}{6} (33.3\%)$ | 3) $\frac{13}{15} (86.6\%)$ | 4) $\frac{2}{6} (33.3\%)$.
> - **Medios:** 1) $\frac{48}{60} (80\%)$ | 2) $\frac{40}{60} (66.6\%)$ | 3) $\frac{44}{60} (73.3\%)$ | 4) $\frac{48}{60} (80\%)$.
> - **Avanzados:** 1) $52.5\%$ | 2) $\$450$ USD | 3) $10\%$ | 4) $\frac{78}{80} (97.5\%)$.

---

## Mini-prueba de autoevaluación

> [!question] Pregunta 1
> ¿Por qué restamos la intersección en la regla de la suma?
> *Respuesta: Para no contar dos veces a los elementos que cumplen ambas condiciones.*

> [!question] Pregunta 2
> Si lanzas un dado, ¿cuál es la probabilidad de obtener un número **Primo** ($2, 3, 5$) o un número **Mayor que 2** ($3, 4, 5, 6$)?
> *Cálculo: $\frac{3}{6} + \frac{4}{6} - \frac{2}{6} = \frac{5}{6} (83.3\%)$.*

> [!question] Pregunta 3
> Si el $75\%$ de los clientes de una tienda son "Compradores frecuentes o Mayores de edad", y el grupo total es de $100$ personas, ¿cuántas personas recibirán un beneficio si este se aplica a dicho grupo?
> A) $25$ personas | B) $75$ personas | C) $100$ personas.
> *Respuesta: B) $75$ personas.*

---

> [!tip] 💡 En la próxima clase
> Veremos cómo identificar la unión de sucesos cuando la palabra "o" no aparece escrita, pero la lógica del problema nos obliga a usar esta regla.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]