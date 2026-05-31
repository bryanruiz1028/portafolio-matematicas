# Clase 05 — Probabilidad Condicional y Tablas de Contingencia

#algebra #probabilidadcon
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 9

> [!info] 🧭 Navegación
> [[Clase 04 — Introducción a la Probabilidad]] | [[00 - Índice del curso|Índice]] | **Clase 05 — Probabilidad Condicional**

---

## 1. RELEVANCIA
La probabilidad condicional es la herramienta que nos permite ajustar nuestras expectativas cuando recibimos "pistas" o información previa. En lugar de mirar el panorama completo, nos enfocamos únicamente en el grupo que cumple con una condición específica para tomar decisiones más precisas basadas en evidencias.

*   💵 **Riesgos Financieros:** Evaluación de la probabilidad de pago de un bono o retorno de inversión en $USD basado en el cumplimiento de hitos financieros previos.
*   🏗️ **Gestión de Proyectos:** Cálculo de tasas de éxito en la entrega de proyectos condicionados a la superación de pruebas técnicas iniciales.
*   📊 **Análisis de Datos:** Clasificación eficiente en censos o encuestas mediante el cruce de categorías (edad, género, ubicación) para predecir comportamientos.

---

## 2. CONCEPTO CLAVE

**Definición para el estudiante:**
Es calcular la posibilidad de que algo pase, pero sabiendo de antemano que ya ocurrió otra cosa (una pista). Es como reducir tu "universo" de búsqueda solo a los elementos que cumplen con esa condición.

### El lenguaje de las probabilidades
En matemáticas, usamos una notación específica para no escribir frases largas. La probabilidad de que ocurra el evento **A** dado que ya sabemos que ocurrió el evento **B** se escribe:
$$P(A|B)$$
La **barra vertical (|)** significa "dado que" o "sabiendo que".

> [!warning] Error Común
> El error más frecuente es usar el **total general** de la muestra cuando existe una condición. 
> *   **Incorrecto:** Dividir el subgrupo entre el total de todos los participantes (200).
> *   **Correcto:** Ignorar el total general y usar únicamente el total del **subgrupo de la condición** como nuevo denominador.

**Truco Pedagógico:**
Para que nunca se te olvide cómo armar la fracción, recuerda siempre:
> [!important]
> **"LO QUE YA SÉ VA DEBAJO"** (El dato de la condición es siempre el denominador).

---

## 3. PROCEDIMIENTO PASO A PASO

```text
PASO 1 → Identificar la condición (lo que ya se sabe). Busca palabras clave 
         como "si...", "dado que...", o "sabiendo que..." para definir el denominador.
PASO 2 → Identificar la intersección (los que cumplen AMBAS cosas) para el numerador.
PASO 3 → Realizar la división (frecuencia favorable / frecuencia de la condición).
PASO 4 → Convertir el resultado a decimal y porcentaje (multiplicar por 100).
```

---

## 4. EJEMPLOS PRÁCTICOS

> [!example] Ejemplo 1: Caso Básico (Lectura de Tabla)
> En una carrera de 200 participantes, queremos saber la probabilidad de que un corredor sea "niña" ($P(Femenino)$ en categoría Niños) sin condiciones previas.
> *   **Total:** 200
> *   **Femeninos en Niños:** 20
> *   **Cálculo:** $20 / 200 = 0.1$
> *   **Resultado:** 10%

> [!example] Ejemplo 2: Caso con Negación (Complemento)
> Si un estudiante "no entregó trabajos", ¿cuál es la probabilidad de que "no apruebe"? ($P(NoAprobó | NoEntregó)$)
> *   **Condición:** No entregó (Total de este grupo: 10 estudiantes).
> *   **Favorable:** No aprobó y no entregó (7 estudiantes).
> *   **Cálculo:** $7 / 10 = 0.7$
> *   **Resultado:** 70%

> [!example] Ejemplo 3: Caso Avanzado (Regla de la Multiplicación)
> Hallar la probabilidad de aprobar Matemáticas ($M$) dado que se aprobó Inglés ($I$). 
> Datos: $P(I) = 0.75$, $P(M) = 0.80$ y $P(I|M) = 0.90$.
> 1.  **Hallar Intersección:** $P(M \cap I) = P(M) \times P(I|M) = 0.80 \times 0.90 = 0.72$.
> 2.  **Aplicar Condicional:** $P(M|I) = 0.72 / 0.75 = 0.96$.
> *   **Resultado:** 96%

> [!example] Ejemplo 4: Aplicación en Inversión ($USD)
> Un proyecto de inversión cuesta $1,000 USD. Si no se cumple un hito técnico, el proyecto fracasa en 7 de cada 10 casos. ¿Cuál es la probabilidad de pérdida dado que falló el hito?
> *   **Denominador (Falla de hito):** 10
> *   **Numerador (Pérdida):** 7
> *   **Cálculo:** $7 / 10 = 0.7$
> *   **Resultado:** 70% de probabilidad de pérdida de la inversión.

---

## 5. EJERCICIOS PARA EL ESTUDIANTE

Usa la siguiente **Tabla de Contingencia (Carrera Atlética)** para los niveles fácil y medio:

| Categoría | Masculino (M) | Femenino (F) | **Total** |
| :--- | :---: | :---: | :---: |
| Niños | 30 | 20 | 50 |
| Adultos | 52 | 38 | 90 |
| Senior (>40-60 años) | 41 | 19 | 60 |
| **Total** | **123** | **77** | **200** |

> [!abstract] Ejercicios de Práctica
>
> **🟢 Nivel Fácil (Probabilidad Simple)**
> 1. ¿Cuál es la $P(Masculino)$ en la carrera?
> 2. ¿Cuál es la $P(Adulto)$ de un corredor al azar?
> 3. ¿Cuál es la $P(Niño)$ (específicamente varón) sobre el total?
> 4. ¿Cuál es la $P(Senior)$ entre todos los participantes?
>
> **🟡 Nivel Medio (Probabilidad Condicional)**
> 1. Si se seleccionó un hombre, ¿cuál es la $P(Niño | Masculino)$?
> 2. Dado que el corredor es de la categoría Senior, ¿cuál es la $P(Femenino | Senior)$?
> 3. Si el corredor es mujer, ¿cuál es la $P(Adulto | Femenino)$?
> 4. Dado que es un Adulto, ¿cuál es la $P(Masculino | Adulto)$?
>
> **🔴 Nivel Avanzado (Aplicación Financiera)**
> 1. Un bono de $500 USD tiene un 80% de probabilidad de pagarse si la empresa crece. La empresa tiene un 75% de probabilidad total de crecer. Si la probabilidad de que crezca Y pague el bono es del 72%, calcula $P(Pago | Crecimiento)$.
> 2. Inversión en tecnología: El 60% de los proyectos son de software. De los de software, el 25% son de IA. Si eliges un proyecto al azar y es de software, ¿cuál es la $P(IA | Software)$?
> 3. Un fondo de $1,200 USD se otorga a un grupo de 50 estudiantes. Se sabe que 41 aprobaron el examen y, de esos que aprobaron, 35 habían entregado todos sus trabajos. Si elegimos a un estudiante que aprobó, ¿cuál es la $P(Entregó | Aprobó)$?
> 4. Calcule la probabilidad de pérdida financiera total si se sabe que el 30% de los negocios fallan y, de esos que fallan, el 70% no tenían seguro. Hallar $P(NoSeguro | Fallo)$.

---

## 6. RESPUESTAS

> [!success] Solucionario
> *   **Nivel Fácil:** 1) 123/200 (61.5%), 2) 90/200 (45%), 3) 30/200 (15%), 4) 60/200 (30%).
> *   **Nivel Medio:** 1) 30/123 (24.3%), 2) 19/60 (31.6%), 3) 38/77 (49.3%), 4) 52/90 (57.7%).
> *   **Nivel Avanzado:** 1) 96% (0.72 / 0.75), 2) 25% (Lectura directa de la condición), 3) 85.3% (35/41), 4) 70% (Dato directo de la condición de fallo).

---

## 7. AUTOEVALUACIÓN

> [!question] Comprueba tu aprendizaje
> 1. **Conceptual:** ¿Qué sucede con el espacio muestral (denominador) cuando pasamos de una probabilidad simple a una condicional?
>    *(R: Se reduce; ya no es el total general, sino solo el total del grupo que cumple la condición).*
> 2. **Procedimental:** En la tabla de 200 personas, si hay 60 Seniors y de ellos 41 son hombres, ¿cuál es el valor de $P(M | Senior)$?
>    *(R: 41/60 = 0.683 o 68.3%).*
> 3. **Aplicación:** Para una beca de $1,200 USD, la probabilidad de éxito es condicionada. Si 6 de cada 10 estudiantes que asisten a clases logran la beca, ¿cuál es la $P(Beca | Asistencia)$?
>    *(R: 6/10 = 60%).*

---

## 8. CIERRE Y NAVEGACIÓN

**Tip para la Clase 06:** En la siguiente lección veremos cómo las Tablas de Contingencia no solo organizan datos, sino que nos permiten visualizar todas las probabilidades (simples, conjuntas y condicionales) de un solo vistazo. ¡No te lo pierdas!

> [!info] 🧭 Navegación
> [[Clase 04 — Introducción a la Probabilidad]] | [[00 - Índice del curso|Índice]] | **Clase 05 — Probabilidad Condicional**