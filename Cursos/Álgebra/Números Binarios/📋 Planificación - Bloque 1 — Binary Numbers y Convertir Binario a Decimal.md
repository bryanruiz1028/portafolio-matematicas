# Planificación Didáctica: Binary Numbers y Conversión de Sistemas de Numeración

**Nivel:** Básica Superior (12–15 años) | **Duración:** 80 minutos
**Tags:** #planificacion #dua #binarynumbers #didacticamatematica

---

## 1. Tema
**Binary Numbers y Conversión entre Sistema Binario y Decimal**

---

## 2. Metodología
**Aprendizaje Colaborativo Formal**
Se implementará una estructura de grupos cooperativos donde la interdependencia positiva se garantiza mediante la asignación de roles específicos: el **Operador Matemático** (encargado de los cálculos de división/suma) y el **Validador Posicional** (responsable de verificar que cada cifra corresponda a la potencia de base 2 correcta). Esta dinámica asegura la responsabilidad individual y el éxito colectivo.

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Activación de Conocimientos Previos
> Se inicia la sesión estableciendo una comparación estructural entre el sistema **Decimal (Base 10)** y el **Binario (Base 2)**. Se debe enfatizar que ambos son **sistemas posicionales**, pero su diferencia radica en el valor de sus casillas. Mientras que el sistema decimal se basa en potencias de 10, el binario se construye sobre la progresión geométrica del doble: $2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32, 2^6=64...$
>
> **Reto inicial:** El docente plantea la pregunta: "¿Cómo representaríamos el número 2 si solo tuviéramos los símbolos 0 y 1?". Se modela en la pizarra que, al llenarse la primera casilla ($2^0$), debemos saltar a la siguiente posición ($2^1$).

> [!note] Enfoque DUA
> - **Qué (Reconocimiento):** Identificación de patrones posicionales y la lógica de "encendido/apagado" (1/0).
> - **Cómo (Acción y Expresión):** Discusión guiada en parejas para formular hipótesis sobre la representación del número 2.

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Modelado y Estrategias de Conversión
> Siguiendo la didáctica del "Profe Alex", se presentan dos procesos técnicos:
> 
> 1. **De Binario a Decimal (Suma de Potencias):** 
>    Se utiliza el ejemplo del número $11001_2$. El estudiante debe ubicar las cifras bajo la tabla de potencias. Se enseña que el "1" actúa como un activador de la casilla:
>    *   $1 \cdot 16 + 1 \cdot 8 + 0 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 16 + 8 + 1 = 25_{10}$.
> 
> 2. **De Decimal a Binario (Divisiones Sucesivas y Truco Mental):** 
>    Para optimizar el cálculo en adolescentes, se introduce el **método de la mitad**: Si el número es impar, se resta 1 (residuo = 1) y se halla la mitad; si es par, el residuo es 0 y se divide directamente entre 2.
>    *   **Importante:** El número binario se construye iniciando con el **último cociente** y siguiendo con los residuos de **abajo hacia arriba**. Ejemplo con el 34: las divisiones nos llevan a la secuencia $100010_2$.
> 
> 3. **Método de la Tabla (Alternativa):** Para números menores a 40, se busca la potencia de 2 más cercana y se resta el valor, activando las casillas necesarias (ej. 34 es $32 + 2$).

> [!note] Enfoque DUA
> - **Qué:** Modelado físico y visual de las estrategias.
> - **Cómo:** Los grupos utilizarán **vasos de plástico** para modelar bits en sus escritorios (Vaso boca arriba = 1, Vaso boca abajo = 0). Realizarán ejercicios con fichas usando colores distintos para el último cociente y los residuos.
> - **Por qué (Compromiso):** Proporcionar múltiples medios de representación (físico con vasos, visual con colores y numérico con divisiones).

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de Cierre: Reto de Velocidad Binaria
> Se organiza una competencia de resolución de problemas. Cada grupo debe convertir los siguientes números y realizar la **comprobación** (convertir el resultado de vuelta a decimal para verificar):
> 1. **Decimal a Binario:** 141 y 225.
> 2. **Reflexión técnica:** Discusión sobre por qué el sistema binario es la base de la computación (estados físicos abierto/cerrado, verdadero/falso).

> [!tip] Guía para el Docente (Soluciones)
> - $141_{10} = 10001101_2$
> - $225_{10} = 11100001_2$

> [!note] Enfoque DUA
> - **Qué:** Demostración del aprendizaje.
> - **Cómo:** Un representante de grupo presenta la "comprobación" en la pizarra.
> - **Por qué:** Gamificación para aumentar el compromiso y fomentar la autoevaluación mediante la verificación del resultado.

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| **Pizarra** | Físico | Modelado de potencias $2^n$ ($2^0=1, 2^1=2, 2^2=4...$) y demostración de divisiones. |
| **Marcadores** | Físico | Uso de colores para diferenciar el último cociente (inicio del binario) de los residuos. |
| **Fichas de Ejercicios** | Impreso | Práctica de casos específicos del Profe Alex: números 34, 428, 25 y 511. |
| **Impresora** | Físico | Preparación de tablas de potencias de 2 como material de apoyo para los grupos. |
| **Vasos de plástico** | Físico | Representación cinestésica: Modelado de números binarios (1 = activo, 0 = inactivo). |