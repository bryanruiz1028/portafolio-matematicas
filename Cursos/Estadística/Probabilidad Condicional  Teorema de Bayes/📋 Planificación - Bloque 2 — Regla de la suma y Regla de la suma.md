# 📋 Planificación Didáctica — Regla de la suma y de la multiplicación

#planificacion #dua #probabilidad #regladelasumaymultiplicacion

**Nivel:** Básica Superior (12–15 años) | **Duración:** 80 minutos

## 1. Tema
Regla de la suma y Regla de la multiplicación (Teorema de la Probabilidad Total).

## 2. Metodología
Se implementará el **Aprendizaje Colaborativo Formal**, organizando el aula en estaciones de trabajo. Los estudiantes trabajarán en equipos para construir representaciones gráficas mediante diagramas de árbol, analizando experimentos de lanzamientos de monedas y extracción de esferas. El objetivo es que los grupos apliquen sistemáticamente las reglas de probabilidad para validar resultados teóricos frente a situaciones experimentales, asumiendo roles de analista y validador de datos.

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio: El reto de las monedas
> Se presenta el experimento del lanzamiento de dos monedas (Cara/Cruz o Sello). Los estudiantes deben predecir el espacio muestral visualmente en la pizarra.
> 1. Se identifican las ramas iniciales: Cara ($P=1/2$) y Sello ($P=1/2$).
> 2. Se introduce la **Regla de la Multiplicación**: para eventos independientes (lo que pase en la primera moneda no afecta a la segunda), multiplicamos las probabilidades de las ramas consecutivas. Ejemplo: P(Cara y Cara) = $1/2 \times 1/2 = 1/4$ (25%).
> 3. **Validación de experto:** Se enfatiza que la suma de todas las ramas que nacen de un mismo nodo debe ser siempre igual a 1 ($0.5 + 0.5 = 1$).

> [!note] Enfoque DUA
> **Qué:** Activación de conocimientos sobre el espacio muestral y eventos independientes.
> **Cómo:** Trabajo en parejas utilizando monedas físicas para realizar 10 lanzamientos rápidos. Los estudiantes registran frecuencias observadas para comparar el resultado empírico con el 25% teórico de obtener "doble cara".

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividades centrales: La Urna de Profe Alex
> Los estudiantes resolverán el escenario de una urna con **3 bolas rojas y 4 azules** (Total = 7).
> 1. **Escenario A (Con reemplazo):** Los eventos son independientes. P(Azul-Azul) = $4/7 \times 4/7 = 16/49$.
> 2. **Escenario B (Sin reemplazo) - El momento Eureka:** El docente guía a los estudiantes a notar que, al no devolver la bola, el denominador cambia para la segunda extracción ($7 \rightarrow 6$). Si salió azul primero, la probabilidad de la segunda azul es $3/6$.
> 3. **Diferenciación Didáctica:** Se explica que usamos la **Regla de la Multiplicación** (operación "Y") para recorrer el camino de una rama, y la **Regla de la Suma** (operación "O") para unir resultados finales que cumplen una condición. Ejemplo: P(Mismo color) = P(Azul-Azul) + P(Rojo-Rojo).

> [!note] Enfoque DUA
> **Qué:** Construcción de diagramas complejos y aplicación de la regla de la suma para eventos mutuamente excluyentes (uniones).
> **Cómo:** Los grupos de 4 personas utilizarán fichas de colores físicas para simular la extracción. Manipularán el material para visualizar por qué el denominador se reduce en el escenario "sin reemplazo" antes de realizar el cálculo abstracto.

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de cierre: Producción Industrial
> Se analiza el problema de las máquinas A, B y C con los siguientes datos:
> - **Producción:** Máquina A (10% = 0.1), Máquina B (30% = 0.3), Máquina C (60% = 0.6).
> - **Tasa de Defectuosos:** A (1% = 0.01), B (2% = 0.02), C (4% = 0.04).
>
> Los equipos deben aplicar el **Teorema de la Probabilidad Total** sumando los tres caminos que llevan a un producto defectuoso:
> $P(D) = (0.1 \times 0.01) + (0.3 \times 0.02) + (0.6 \times 0.04) = 0.001 + 0.006 + 0.024 = 0.031$ (3.1%).

> [!note] Enfoque DUA
> **Qué:** Síntesis del Teorema de Probabilidad Total e integración de datos complejos.
> **Cómo:** "Rutas de Probabilidad" en la pizarra. Cada grupo usará un marcador de color diferente para trazar el camino de cada máquina. Como reto final, se entregará una **Tabla de Contingencia** (Carrera Atlética: 200 participantes, 77 mujeres, 123 hombres) para que los alumnos identifiquen cómo los datos del diagrama de árbol se organizan de forma bidimensional.

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| **Pizarra** | Físico | Modelado de nodos raíz y verificación de que las ramas sumen 1. |
| **Marcadores de colores** | Físico | Diferenciación de rutas: Azul (Machine A), Verde (Machine B), Naranja (Machine C). |
| **Fichas de colores** | Impreso | 3 rojas y 4 azules para manipular el experimento de la urna (Ejemplo 3). |
| **Guía de Ejercicios** | Impreso | Incluye el problema de las máquinas y la **Tabla de Contingencia de la Carrera** (Ejemplo 6). |
| **Monedas reales** | Físico | Verificación empírica inicial de eventos independientes. |