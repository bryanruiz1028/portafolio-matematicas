# Clase 02 — Rule of 3 | How to identify if it's direct or inverse + Direct proportionality
tags: #algebra #ruleof

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 16

> [!info] 🧭 Navegación
> - ⬅️ **Clase anterior:** [[Clase 01 - Razones y Proporciones]]
> - 🏠 **Índice:** [[00 - Índice del curso]]
> - ➡️ **Siguiente clase:** [[Clase 03 - Proporcionalidad Inversa]]

---

## ¿Por qué es importante esta clase?

La proporcionalidad directa es el pilar para predecir resultados en sistemas donde dos magnitudes están vinculadas de forma que crecen o decrecen juntas manteniendo una relación constante. Dominar este concepto permite pasar de la intuición al cálculo técnico preciso.

- **💵 Aplicación $USD:** Determinar el costo total de una importación basándose en el precio unitario y el volumen de compra.
- **🏗️ Aplicación práctica:** Dimensionar recursos en obra, como calcular los metros de superficie cubiertos según los días de jornada laboral.
- **📊 Situación cotidiana:** Estandarizar la producción o el empaque, como calcular la cantidad de insumos necesarios para obtener un número exacto de productos terminados.

---

## Concepto Clave

Para un especialista en matemáticas, la Regla de Tres no es un "truco", sino la aplicación de la **Propiedad Fundamental de las Proporciones**.

> [!note] Definición Técnica
> **Magnitud:** Es toda propiedad medible que puede ser expresada mediante un número (ej. velocidad, masa, tiempo, precio).
> 
> **Proporcionalidad Directa:** Dos magnitudes son directamente proporcionales cuando su **cociente (división)** es constante. Esta constante se denomina **Constante de Proporcionalidad ($k$)**.
> $$ \frac{a}{b} = k $$
> Si una magnitud aumenta (ej. se duplica), la otra debe aumentar en la misma proporción (se duplica) para que $k$ no varíe.

> [!warning] Identificación Crítica
> El error más común es aplicar el procedimiento operativo sin realizar el **análisis de sentido**. Antes de calcular, se debe verificar si la relación es directa o inversa. Si se opera una relación inversa como directa, el resultado carecerá de sentido físico y matemático.

> [!tip] El Análisis de Signos (+/+)
> Para identificar una relación **Directa**, observa el comportamiento de las magnitudes:
> - **(+ A, + B):** Si a **más** gasolina, corresponden **más** kilómetros $\rightarrow$ **Directa**.
> - **(- A, - B):** Si a **menos** horas de trabajo, corresponden **menos** pantalones producidos $\rightarrow$ **Directa**.

---

## Procedimiento Paso a Paso

Sigue este protocolo de resolución técnica para evitar errores de planteamiento:

```text
PASO 1 → Definir Magnitudes: Identificar las propiedades medibles y sus unidades.
PASO 2 → Plantear la Proporción: Alinear los datos en columnas (Magnitud A | Magnitud B).
PASO 3 → Análisis de Relación: Determinar si es directa (+/+ o -/-).
PASO 4 → Propiedad Fundamental: Aplicar el producto cruzado (a · d = b · c).
PASO 5 → Despeje de Incógnita: Resolver para x dividiendo por el término restante.
```

---

## Ejemplos Detallados

### Ejemplo 1: Estandarización de Empaque (Básico)
En un centro logístico, se empacan 4 balones por cada caja. ¿Cuántas cajas se requieren para 24 balones?
- **Planteamiento:**
    - 4 balones $\rightarrow$ 1 caja
    - 24 balones $\rightarrow$ $x$ cajas
- **Resolución:**
    $$ x = \frac{24 \cdot 1}{4} = 6 $$
- **Resultado:** Se requieren 6 cajas.

### Ejemplo 2: Consumo de Combustible (Signos)
Un vehículo consume 10 litros de gasolina para recorrer 150 km. ¿Cuántos kilómetros recorrerá con 20 litros?
- **Análisis de Magnitudes:**
    - Magnitud A (Gasolina): Aumenta (+) de 10 a 20.
    - Magnitud B (Distancia): Aumentará (+) necesariamente.
    - **Relación:** Directa (+/+).
- **Cálculo:**
    $$ x = \frac{20 \cdot 150}{10} = \frac{3000}{10} = 300 $$
- **Resultado:** Recorrerá 300 km.

### Ejemplo 3: Producción Industrial (Cálculo de $k$)
Una fábrica produce 600 pantalones en 8 horas. ¿Cuántos pantalones se fabrican en 2 horas?
- **Análisis por Reducción a la Unidad ($k$):**
    $$ k = \frac{600 \text{ pantalones}}{8 \text{ horas}} = 75 \text{ pantalones/hora} $$
- **Cálculo para 2 horas:**
    $$ x = 75 \cdot 2 = 150 $$
- **Resultado:** 150 pantalones. (Note que al disminuir el tiempo a la cuarta parte, la producción disminuye proporcionalmente).

### Ejemplo 4: Presupuesto en $USD
Si 5 balones profesionales tienen un costo de $25 USD, ¿cuál es el precio de 15 balones?
- **Planteamiento:**
    $$ \frac{5}{25} = \frac{15}{x} \implies 5x = 15 \cdot 25 $$
- **Despeje:**
    $$ x = \frac{375}{5} = 75 $$
- **Resultado:** El costo total es de $75 USD.

---

## Ejercicios para el Estudiante

### Nivel Fácil: Proporción Simple
1. Un paquete contiene 6 galletas. ¿Cuántas galletas hay en 8 paquetes?
2. Si en una caja caben 12 libros, ¿cuántas cajas se requieren para 48 libros?
3. 2 cajas contienen 20 chocolates. ¿Cuántos hay en 5 cajas?
4. Un sobre de cromos trae 5 unidades. ¿Cuántos sobres se necesitan para obtener 50 cromos?

### Nivel Medio: Identificación de Magnitudes
*Instrucción: Identifique si la relación es Directa. Si no lo es, justifique por qué.*
5. Un coche recorre 150 km con 10L de gasolina. ¿Cuánto recorre con 25L?
6. 4 obreros construyen una barda en 10 días. Si contrato 8 obreros, ¿tardarán más o menos días? ¿Es Directa?
7. Un pintor cubre 4 $m^2$ en 2 días. ¿Cuántos metros cubrirá en 10 días a ritmo constante?
8. Si un tren viaja a 100 km/h y tarda 2 horas en llegar, ¿qué pasa con el tiempo si aumenta la velocidad? ¿Es Directa?

### Nivel Avanzado: Producción y Finanzas ($USD)
9. Una planta produce 1,200 camisas en 10 horas. Calcule la producción en un turno de 3 horas.
10. El costo de 12 pantalones es de $240 USD. ¿Cuál es el precio de 5 pantalones?
11. Un consultor cobra $120 USD por 8 horas de asesoría. ¿Cuánto percibirá por 12 horas?
12. Una máquina llena 500 botellas en 2 horas. Determine la producción total en un turno de 7 horas.

> [!success] Respuestas para el docente
> 1. 48 galletas | 2. 4 cajas | 3. 50 chocolates | 4. 10 sobres.
> 5. 375 km | 6. Menos días (Relación INVERSA, no directa) | 7. 20 $m^2$ | 8. Menos tiempo (Relación INVERSA, no directa).
> 9. 360 camisas | 10. $100 USD | 11. $180 USD | 12. 1,750 botellas.

---

## Mini-Prueba de Autoevaluación

> [!question] Pregunta 1: Conceptual
> Si en una relación de proporcionalidad directa el valor de la Magnitud A se divide entre 3, ¿qué debe ocurrir con la Magnitud B para mantener la constante $k$?
> > [!check] Respuesta
> > La Magnitud B también debe dividirse entre 3, ya que la proporcionalidad directa exige que ambas varíen en la misma proporción y sentido.

> [!question] Pregunta 2: Procedimental
> Se sabe que 1 día equivale a 24 horas. ¿Cuántas horas hay en 0.75 días? Aplique el concepto de $k$.
> > [!check] Respuesta
> > 18 horas. 
> > Explicación: $k = \frac{24}{1} = 24$. Entonces, $0.75 \cdot 24 = 18$.

> [!question] Pregunta 3: Aplicación $USD
> Si 10 artículos cuestan $50 USD, ¿cuál es el costo de 3 artículos?
> A) $15 USD
> B) $20 USD
> C) $30 USD
> > [!check] Respuesta
> > **A) $15 USD**. 
> > Explicación: La constante de precio unitario es $k = \frac{50}{10} = 5$ USD/artículo. Por tanto, $3 \text{ artículos} \cdot 5 = 15$ USD.

---

## Notas Finales

> [!tip] Próximo tema
> En la siguiente sesión analizaremos la **Proporcionalidad Inversa**. Aprenderemos casos donde, al aumentar una magnitud, la otra disminuye (como la relación entre el número de trabajadores y el tiempo de entrega).

> [!info] 🧭 Navegación
> - ⬅️ **Clase anterior:** [[Clase 01 - Razones y Proporciones]]
> - 🏠 **Índice:** [[00 - Índice del curso]]
> - ➡️ **Siguiente clase:** [[Clase 03 - Proporcionalidad Inversa]]