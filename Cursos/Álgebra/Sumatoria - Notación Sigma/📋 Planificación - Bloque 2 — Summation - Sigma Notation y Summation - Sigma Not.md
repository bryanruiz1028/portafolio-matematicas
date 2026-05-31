# 📋 Planificación Didáctica — Summation - Sigma Notation y Cambio de Índices

tags: #planificación #dua #summationsigman #matemáticas
Nivel: Básica Superior (12–15 años) | Duración: 80 minutos

---

## 1. Tema
Summation - Sigma Notation y Cambio de Índices.

---

## 2. Metodología
**Aprendizaje Colaborativo Formal:** Los estudiantes trabajarán en grupos de tres con roles definidos: el **Líder** coordina los pasos, el **Secretario** registra el proceso y el **Verificador** asegura que las constantes se extraigan correctamente antes de aplicar fórmulas y que no se caiga en la "trampa de la constante" durante el cambio de índices, fomentando la precisión técnica y la discusión conceptual.

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio: El Genio de Gauss
> Se relata la historia de Gauss, quien a los 9 años sumó los números del 1 al 100 en segundos. Los alumnos intentarán el reto mentalmente. Luego, modelaremos su método: sumar extremos ($1+100, 2+99$) para obtener parejas de $101$. Al ser 100 números, hay $100/2 = 50$ parejas. El resultado es $50 \times 101 = 5050$. Introduciremos la Notación Sigma ($\sum$) como el lenguaje profesional para abreviar esta suma: $\sum_{i=1}^{100} i$.

> [!note] Enfoque DUA
> - **Qué:** Activación de conocimientos previos y representación táctil.
> - **Cómo:** Los estudiantes usarán **semillas o granos** en sus mesas para representar sumas más pequeñas (del 1 al 10) organizándolas en filas de extremos pares para visualizar la simetría del método de Gauss.
> - **Por qué:** Proporcionar opciones para la percepción física y el compromiso mediante un reto histórico y manipulativo.

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividades centrales: Fórmulas y Propiedades
> Como especialistas, no solo memorizamos, entendemos relaciones. Presentamos los tres pilares:
> 
> **1. Fórmulas Fundamentales (Inicio en $i=1$):**
> - **Naturales:** $\sum i = \frac{n(n+1)}{2}$
> - **Cuadrados:** $\sum i^2 = \frac{n(n+1)(2n+1)}{6}$
> - **Cubos:** $\sum i^3 = \left[ \frac{n(n+1)}{2} \right]^2$
> 
> > [!tip] Mnemotecnias del Profe Alex
> > - **El Tercer Factor:** En la fórmula de cuadrados, el término $(2n+1)$ es simplemente la **suma de los dos primeros factores** ($n + (n+1)$).
> > - **Relación de Cubos:** La suma de cubos es exactamente la suma de naturales, pero **elevada al cuadrado**. ¡Si te sabes una, te sabes la otra!
> 
> **2. Propiedades de Linealidad:**
> - **Separación:** $\sum (a_i \pm b_i) = \sum a_i \pm \sum b_i$.
> - **Extracción de constante:** El número que multiplica sale de la sigma (ej. $\sum 5i^2 = 5 \sum i^2$).
> 
> **3. Cambio de Índice (La "Operación Contraria"):**
> Para usar las fórmulas, el límite inferior debe ser 1. Si restamos $p$ a los límites, sumamos $p$ a la variable $i$.
> *Ejemplo:* Para $\sum_{i=5}^{15} 3i$, restamos 4 a los límites ($5-4=1$ e $15-4=11$) y reemplazamos $i$ por $(i+4)$.
> Resulta: $\sum_{i=1}^{11} 3(i+4) = \sum_{i=1}^{11} (3i + 12)$.
> 
> > [!warning] La Trampa de la Constante
> > Al hacer el cambio de índice, **solo se afecta a la letra $i$**. Si hay un número solo (constante), este no cambia. En $\sum (i+10)$, el $i$ se vuelve $(i+p)$, pero el $10$ permanece igual.

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de cierre: El Desafío Maestro
> En sus grupos colaborativos, resuelvan el siguiente ejercicio que integra todos los niveles de dificultad:
> $$\sum_{i=6}^{40} [2i^3 - 3i^2 - 5i - 10]$$
> **Pasos requeridos:**
> 1. Aplicar cambio de índice para iniciar en $i=1$ (restar 5 a límites, sumar 5 a cada $i$).
> 2. Distribuir términos y extraer constantes.
> 3. Aplicar las mnemotecnias para las fórmulas de cubos, cuadrados y naturales.
> 4. El **Verificador** debe confirmar que el $-10$ final no fue alterado por el $+5$ del índice.

> [!note] Enfoque DUA
> - **Qué:** Evaluación de maestría y expresión de conocimientos.
> - **Cómo:** Los grupos socializan su estrategia en la pizarra. Aquellos con dificultades motoras pueden usar las fichas de fórmulas para guiar el proceso verbalmente.
> - **Por qué:** Fomentar la colaboración y ofrecer múltiples medios de acción y expresión.

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase (Enfoque DUA) |
| :--- | :--- | :--- |
| **Pizarra y Marcadores** | Físico | Modelado visual de la sustitución "contraria" en el cambio de índices usando colores para diferenciar límites de variables. |
| **Fichas Impresas** | Impreso | Apoyo de memoria para reducir carga cognitiva; contiene las fórmulas y las mnemotecnias de "suma de factores". |
| **Semillas o Granos** | Físico | **Representación Kinestésica:** Permite a estudiantes con estilos de aprendizaje táctiles palpar la formación de parejas de Gauss. |
| **Guía de Ejercicios** | Impreso | Problemas graduados desde aplicación directa hasta desafíos multinivel para andamiaje. |

**Profesor de Álgebra Superior:** *"La notación sigma no es solo un símbolo, es la herramienta que nos permite compactar el infinito en la palma de nuestra mano."*