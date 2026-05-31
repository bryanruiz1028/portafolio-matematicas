# Clase 08 — Probabilidad Condicional y Tablas de Contingencia

#algebra #probabilidadcon
[[Índice del curso]]

> [!info] 🧭 Navegación
> [[Clase 07]] | [[Índice]] | **Clase 08**

> [!info] 🌍 Relevancia y aplicaciones
> La probabilidad condicional es la herramienta fundamental para ajustar nuestras expectativas y decisiones ante nueva información. No solo es estadística; es eficiencia. Sus aplicaciones incluyen:
> 1. **Salud y Finanzas Veterinarias:** Optimizar presupuestos en $USD al predecir necesidades médicas basadas en la especie. (Ej: Si el paciente es un perro, la probabilidad de requerir vacuna antirrábica aumenta, permitiendo asignar fondos de forma inteligente).
> 2. **Rendimiento Académico:** Determinar cómo el éxito en una competencia (Matemáticas) correlaciona con otra (Inglés) para diseñar planes de refuerzo personalizados.
> 3. **Gestión de Riesgos en Eventos:** En carreras atléticas, permite calcular la logística de seguridad y suministros centrándose solo en subgrupos específicos (como la categoría Senior), evitando el desperdicio de recursos en el total general.

---

> [!note] 📌 ¿Qué es Probabilidad Condicional?
> Imagina que estás buscando a alguien en un edificio. Si te dicen que esa persona "está en el segundo piso", ya no la buscas en todo el edificio. Esa pista es la **condición**. En matemáticas, la probabilidad condicional es trabajar con una pista que **reduce el espacio muestral** (el total de casos), enfocándonos solo en el subgrupo que cumple la condición.

> [!warning] ⚠️ Error común
> El error más grave es no actualizar el denominador. 
> *   En una **probabilidad simple**, el total son todas las personas: $P(Mujer) = \frac{77}{200}$.
> *   En una **probabilidad condicional**, el total es solo el grupo de la pista: $P(Mujer | Adulto) = \frac{38}{90}$.
> Observa cómo el denominador cambió de 200 a 90 porque la condición "Adulto" descartó a todos los demás.

> [!tip] 💡 Truco para recordarlo
> Para no fallar nunca en la fórmula, aplica la regla de oro del Profe Alex: **"Lo que ya se sabe (la pista o condición) va abajo en el denominador"**.

---

### Procedimiento Lógico-Matemático

```text
PASO 1 → Identificar la condición (el dato que ya se conoce o "pista").
PASO 2 → Definir el nuevo total (denominador) basado exclusivamente en esa condición.
PASO 3 → Identificar los casos favorables que cumplen AMBAS condiciones (la intersección).
PASO 4 → Dividir el resultado y convertirlo a porcentaje para la interpretación final.
```

---

### Galería de Ejemplos Detallados

```ad-example
title: Ejemplo 1: Probabilidad Simple (Sin condiciones)
En una carrera atlética de 200 personas, participan 77 mujeres (femenino). ¿Cuál es la probabilidad de que al elegir un corredor al azar sea mujer?
* **Total de casos:** 200 (No hay pista previa).
* **Casos favorables:** 77.
* **Cálculo:** $77 / 200 = 0.385$.
* **Resultado:** **38.5%**.
```

```ad-example
title: Ejemplo 2: Uso de Negaciones
Un profesor analiza a 50 estudiantes. 10 de ellos **no entregaron** trabajos. De ese subgrupo de 10, se observa que 7 reprobaron (perdieron). ¿Cuál es la probabilidad de que un estudiante pierda dado que no entregó trabajos?
* **Condición (Abajo):** Estudiantes que no entregaron = 10.
* **Favorable (Arriba):** No entregó Y perdió = 7.
* **Cálculo:** $7 / 10 = 0.7$.
* **Resultado:** **70%**.
```

```ad-example
title: Ejemplo 3: Lectura de Tablas de Contingencia
Usando la tabla de la carrera atlética, calcula la probabilidad de que un corredor sea hombre (masculino) dado que pertenece a la categoría "Senior".
* **Datos de la Fila Senior:** Masculino (41), Femenino (19), Total Senior (60).
* **Condición (Abajo):** Total de la categoría Senior = 60.
* **Favorable (Arriba):** Masculinos dentro de Senior = 41.
* **Cálculo:** $41 / 60 = 0.6833...$
* **Resultado:** **68.3%**.
```

```ad-example
title: Ejemplo 4: Aplicación Financiera ($USD)
El 80% de los alumnos paga una suscripción de Matemáticas de $80 USD. El 90% de ellos también compra la de Inglés. Si el 75% del total tiene Inglés, ¿cuál es la probabilidad de que alguien que pagó Inglés también haya pagado Matemáticas?
* **Intersección (Ambas):** $0.80 \times 0.90 = 0.72$ (72% pagan ambas).
* **Condición (Abajo):** Los que pagan Inglés (0.75).
* **Cálculo:** $0.72 / 0.75 = 0.96$.
* **Resultado:** **96%**. (Es casi seguro que si tiene inglés, también compró matemáticas).
```

---

### Sección de Práctica: Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Verde: Lectura de Tablas (Carrera Atlética)
Utilizando el total de 200 participantes, calcula:
1. ¿Cuál es la probabilidad de que un participante sea Niño?
2. ¿Cuál es la probabilidad de que un participante sea Adulto?
3. ¿Cuál es la probabilidad de elegir un hombre de la categoría Senior? (Sin condición previa).
4. ¿Cuál es la probabilidad de elegir una mujer de la categoría Niños? (Sin condición previa).
```

```ad-abstract
title: 🟡 Nivel Amarillo: Probabilidad Condicional (Clínica Veterinaria)
**Datos:** 60% de los pacientes son Perros, 30% son Blancos, y el 25% de los perros son blancos.
1. Si se elige un perro, ¿cuál es la probabilidad de que sea blanco? (Identifica si este dato ya es una condición dada).
2. Calcule la probabilidad de que un animal sea Perro Y Blanco (Intersección).
3. Si el animal seleccionado es blanco, ¿cuál es la probabilidad de que sea un perro?
4. ¿Cuál es la probabilidad de que un animal NO sea blanco?
```

```ad-abstract
title: 🔴 Nivel Rojo: Desafío de Gestión Escolar ($USD)
**Contexto:** Un colegio tiene 50 estudiantes. La inscripción cuesta $100 USD. 
- El 80% entrega documentos a tiempo. 
- De los que entregan a tiempo, el 87.5% paga la inscripción de $100 USD completa. 
- De los que entregan tarde, el 60% paga la inscripción completa.

1. Si un estudiante entregó a tiempo, ¿cuál es la probabilidad de que no haya pagado sus $100 USD?
2. Si un estudiante entregó tarde, ¿cuál es la probabilidad de que haya pagado sus $100 USD?
3. Si se sabe que un estudiante pagó los $100 USD, ¿cuál es la probabilidad de que haya entregado a tiempo?
4. Construya la tabla de contingencia completa para los 50 estudiantes (mostrando cantidades exactas de personas).
```

---

### Clave de Respuestas para el Docente

```ad-success
title: Soluciones Oficiales y Lógica
* **Nivel Verde:** 
  1. 50/200 (25%). 2. 90/200 (45%). 3. 41/200 (20.5%). 4. 20/200 (10%).
* **Nivel Amarillo:** 
  1. $P(Blanco|Perro) = 25\%$ (Ya dado en el enunciado). 
  2. Intersección: $0.60 \times 0.25 = 0.15$ (15%). 
  3. $P(Perro|Blanco) = 0.15 / 0.30 = 50\%$.
  4. $P(No Blanco) = 1 - 0.30 = 70\%$.
* **Nivel Rojo:** 
  1. $P(No Paga|Tiempo) = 12.5\%$. 
  2. $P(Paga|Tarde) = 60\%$. 
  3. $P(Tiempo|Paga) = 35 / 41 \approx 85.3\%$.
  4. **Tabla (50 personas):** 
     - Entregan a tiempo: 40 (35 pagan / 5 no).
     - Entregan tarde: 10 (6 pagan / 4 no).
     - Totales: 41 pagan / 9 no pagan.
```

---

### Autoevaluación (Mini-prueba)

```ad-question
title: Pregunta 1: Conceptual
¿Qué efecto produce una condición en el denominador de la fracción de probabilidad?
* a) Lo aumenta, pues hay más información.
* b) Lo mantiene igual, el total nunca cambia.
* c) Lo disminuye, pues nos enfocamos solo en el subgrupo que cumple la condición.
```

```ad-question
title: Pregunta 2: Procedimental
En la tabla de la carrera: Si seleccionamos un **Adulto** (90 personas), y sabemos que 38 son mujeres, ¿cuál es la probabilidad de que el adulto elegido sea **mujer**?
```

```ad-question
title: Pregunta 3: Aplicación y Costo
Una empresa gasta $100 USD en marketing por cada cliente. Sabe que la probabilidad de compra es del 72% si el cliente ya visitó la web (intersección), pero solo del 15% en el público general. ¿Por qué es más rentable (en términos de ahorro de $USD) usar probabilidad condicional para dirigir la publicidad? Justifique usando el concepto de reducción de espacio muestral.
```

---

> [!tip] 💡 En la próxima clase
> Veremos cómo organizar estas condiciones de forma visual utilizando **Diagramas de Árbol**, la herramienta definitiva para resolver problemas de Probabilidad Total y el Teorema de Bayes.

> [!info] 🧭 Navegación
> [[Clase 07]] | [[Índice]] | **Clase 08**