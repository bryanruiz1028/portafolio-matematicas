# 📖 Guía de estudio — Clase 10: Teorema de la Probabilidad Total

> [!info] 📌 Conceptos clave
> El Teorema de la Probabilidad Total es una herramienta fundamental para calcular la probabilidad de un evento que puede ocurrir a través de múltiples condiciones o caminos. Basándonos en las enseñanzas del Profe Alex, los pilares para dominar este tema son:
> *   **Visualización con Diagramas de Árbol:** Es la mejor estrategia para organizar gráficamente todas las posibilidades de un experimento y no olvidar ningún escenario.
> *   **Importancia del Orden:** Si el problema define un orden específico (ej. "Primero Azul, luego Verde"), usamos la Regla de la Multiplicación. Sin embargo, si el orden **no está especificado** (ej. "Sacar una Azul y una Verde"), debemos aplicar la Probabilidad Total para sumar todos los órdenes posibles (Azul-Verde + Verde-Azul).
> *   **Caminos y Sumatorias:** Cuando un resultado puede ocurrir de varias formas, calculamos la probabilidad de cada "camino" y luego sumamos esos resultados.
> *   **Regla de la Multiplicación:** Para hallar la probabilidad de un camino específico (una rama seguida de otra), multiplicamos las probabilidades a lo largo de esas ramas.
> *   **Independencia vs. Dependencia:**
>     *   **Con reemplazo:** Eventos independientes; la probabilidad se mantiene igual en cada extracción.
>     *   **Sin reemplazo:** Eventos dependientes; la probabilidad cambia (el denominador disminuye) porque el espacio muestral se reduce.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Laplace** | Probabilidad en condiciones de **equiprobabilidad**: $P = \frac{\text{Casos favorables}}{\text{Casos totales}}$ |
| **Teorema de la Probabilidad Total** | Suma de las probabilidades de todas las intersecciones que llevan al evento: $P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \dots$ |
| **Eventos Dependientes** | Común en extracciones "sin reemplazo", donde el primer resultado altera las probabilidades del segundo. |
| **Diagrama de Árbol** | Herramienta gráfica que desglosa un experimento compuesto en ramas para identificar cada resultado y su probabilidad. |

## Ejemplos resueltos adicionales

````ad-example
**Ejemplo A — Extracción de esferas (Caso Básico)**
**Problema:** En una urna hay 5 esferas azules, 2 rojas y 1 verde (Total: 8). Si se extraen dos esferas **con reemplazo**, ¿cuál es la probabilidad de sacar una azul y una verde?

**Pasos:**
1.  **Identificar opciones:** Como no se especifica el orden, los caminos válidos son (Azul-Verde) o (Verde-Azul).
2.  **Calcular probabilidades individuales:**
    *   $P(\text{Azul y Verde}) = P(\text{Azul}) \times P(\text{Verde}) = \frac{5}{8} \times \frac{1}{8} = \frac{5}{64}$
    *   $P(\text{Verde y Azul}) = P(\text{Verde}) \times P(\text{Azul}) = \frac{1}{8} \times \frac{5}{8} = \frac{5}{64}$
3.  **Sumar resultados (Probabilidad Total):**
    *   $\frac{5}{64} + \frac{5}{64} = \frac{10}{64}$

**Resultado final:**
*   **Fracción:** $\frac{5}{32}$ (simplificado)
*   **Decimal:** $0.15625$
*   **Porcentaje:** $15.62\%$
````

````ad-example
**Ejemplo B — Producción Industrial y Costos (Aplicación Real)**
**Contexto:** Una fábrica utiliza tres máquinas: A (produce el 10%), B (30%) y C (60%). Las tasas de defectos son: A (1%), B (2%) y C (4%). Cada pieza defectuosa genera una pérdida de $1 USD.

**Pasos para hallar la Probabilidad Total de una pieza defectuosa:**
1.  **Datos en decimales:** $P(A)=0.1$, $P(B)=0.3$, $P(C)=0.6$. Defectos: $P(D|A)=0.01$, $P(D|B)=0.02$, $P(D|C)=0.04$.
2.  **Cálculo por ramas (Multiplicación):**
    *   Rama A: $0.1 \times 0.01 = 0.001$
    *   Rama B: $0.3 \times 0.02 = 0.006$
    *   Rama C: $0.6 \times 0.04 = 0.024$
3.  **Suma de probabilidades:** $0.001 + 0.006 + 0.024 = 0.031$
4.  **Conversión a porcentaje:** $0.031 \times 100 = 3.1\%$

✅ **Resultado final:** La probabilidad total de defecto es del **3.1%**. En términos económicos, la empresa espera perder $0.031 USD por cada pieza producida en promedio.
````

## Ejercicios de repaso

````ad-abstract
**🟢 Nivel Fácil**
Basándote en una urna con 5 esferas azules, 2 rojas y 1 verde:
1. ¿Cuál es la probabilidad de sacar una esfera roja en una única extracción expresada en porcentaje?
2. Si se sacan dos esferas con reemplazo, ¿cuál es la probabilidad de que la primera sea azul y la segunda también sea azul?
3. Según la regla de oro del diagrama de árbol, ¿cuánto debe sumar el total de las probabilidades que salen de un mismo nodo?
````

````ad-abstract
**🟡 Nivel Medio**
1. En un grupo de 15 estudiantes (9 niñas y 6 niños), se eligen dos al azar **sin reemplazo**. ¿Cuál es la probabilidad de que el primero sea niño y la segunda sea niña? $P = (\frac{6}{15} \times \frac{9}{14})$.
2. Si en una urna de 8 esferas realizas una extracción **sin reemplazo**, explica por qué el denominador de la segunda probabilidad debe ser $7$.
3. Calcula la probabilidad total de obtener dos esferas azules de la urna original (5A, 2R, 1V) si la extracción es **sin reemplazo**.
````

````ad-abstract
**🔴 Nivel Avanzado — Aplicación Económica**
1. El señor Gómez tiene una probabilidad total del **46%** ($0.46$) de ser nombrado gerente. Si el bono por el nombramiento es de **$1,000 USD**, ¿cuál es el valor esperado del bono? (Multiplica la probabilidad por el monto).
2. En una clase donde la probabilidad total de aprobación es del **86%**, un patrocinador donará **$10 USD** por cada alumno que apruebe. En un salón de 50 estudiantes, ¿cuál es el monto total que el patrocinador espera pagar?
3. En el caso del señor Gómez, si la probabilidad de que la empresa abra la sucursal bajara del 60% al 50%, explica cualitativamente si su probabilidad total de ser gerente aumentaría o disminuiría y por qué.
````

> [!tip] 💡 Consejo de estudio
> Para asegurar el éxito, sigue el consejo del **Profe Alex**: dibuja siempre el diagrama de árbol completo, aunque parezca laborioso. Esto te permite visualizar todos los caminos sin errores. **Regla de oro:** Verifica que la suma de las ramas que nacen de un mismo punto sea siempre igual a **1 (o 100%)**. Si no suma 1, revisa tus cálculos antes de continuar.