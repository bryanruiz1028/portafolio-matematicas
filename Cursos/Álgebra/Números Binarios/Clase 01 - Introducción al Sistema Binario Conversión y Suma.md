# Clase 01 — Introducción al Sistema Binario: Conversión y Suma

#algebra #binarynumbers

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> Próxima lección: [[Clase 02 — Resta y Multiplicación Binaria]]

## 1. ¿Por qué es importante esta clase?

El sistema binario es el lenguaje del "corazón" de la tecnología. Mientras nosotros usamos diez dígitos, las computadoras simplifican todo a impulsos eléctricos de **0 y 1** (encendido/apagado), permitiendo procesar información a velocidades increíbles.

*   **Aplicación $USD:** Cada vez que ves el saldo de tu cuenta bancaria digital, el sistema financiero está operando con largas cadenas de bits para asegurar que no se pierda ni un centavo en la traducción.
*   **Aplicación práctica:** Los circuitos electrónicos (hardware) interpretan el $1$ como paso de corriente y el $0$ como ausencia de ella.
*   **Situación cotidiana:** Tus fotos de Instagram o los mensajes de WhatsApp son, en realidad, millones de ceros y unos almacenados en la memoria de tu celular.

## 2. Concepto clave

> [!info] Definición: Sistema Binario
> Es un sistema de numeración posicional de **base 2**. Esto significa que el valor de cada cifra depende de su posición y solo existen dos símbolos: el $0$ y el $1$. Cada posición hacia la izquierda representa una potencia de 2 ($2^0, 2^1, 2^2 \dots$), lo que nos da la secuencia de "pesos": $1, 2, 4, 8, 16, 32 \dots$

> [!warning] Error Común de Lectura
> En binario, el número $10_2$ **no es "diez"**, es **dos**. Para evitar confusiones, leemos las cifras por separado ("uno-cero") o mencionamos su valor decimal.

> [!tip] Regla del Duplicado
> Para saber el valor de una posición, simplemente empieza desde la derecha con el $1$ y ve **duplicando** el valor hacia la izquierda: $1 \rightarrow 2 \rightarrow 4 \rightarrow 8 \rightarrow 16 \dots$ Esta lógica posicional es la clave para convertir cualquier número rápidamente.

## 3. Procedimiento paso a paso

### El Truco de la Mitad (Mental Shortcut)
Antes de dividir, el Profe Alex nos enseña a sacar mitades rápidamente:
1. Si la cifra es **par**, saca su mitad directamente.
2. Si la cifra es **impar**, réstale $1$, saca la mitad de lo que queda y "pasa" ese $1$ a la siguiente cifra (convirtiéndola en un número de dos dígitos).
   * *Ejemplo:* Para la mitad de $75$, el $7$ es impar. $7-1=6$ (mitad **3**). El $1$ pasa al $5$, formando un $15$. $15-1=14$ (mitad **7**). Sobra **1**. Resultado: $37$ y sobra $1$.

### Método 1: Conversión de Decimal a Binario
```text
1. Divide el número decimal entre 2 (usa el truco de la mitad).
2. Anota el residuo: 0 si es par, 1 si es impar.
3. Toma el cociente y vuelve a dividir entre 2.
4. Repite hasta que el último cociente sea 1.
5. IMPORTANTE: Lee el número de ABAJO hacia ARRIBA (empezando por el último cociente).
```

### Método 2: Reglas de la Suma Binaria
Al sumar columnas de derecha a izquierda, aplicamos estas reglas:
*   $0 + 0 = 0$
*   $0 + 1 = 1$
*   $1 + 1 = 0$ (y llevas $1$ de acarreo a la columna siguiente).
*   $1 + 1 + 1 = 1$ (y llevas $1$ de acarreo a la columna siguiente).
*   $1 + 1 + 1 + 1 = 0$ (y llevas **0** a la columna siguiente y **1** a la columna que está dos posiciones a la izquierda). *Nota: Esto equivale a $100_2$ (cuatro).*

## 4. Ejemplos detallados

> [!example] Ejemplo 1: Convertir $11001_2$ a decimal
> Usamos la tabla de pesos de derecha a izquierda:
> | 16 | 8 | 4 | 2 | 1 |
> | :---: | :---: | :---: | :---: | :---: |
> | 1 | 1 | 0 | 0 | 1 |
> 
> Sumamos solo donde hay un $1$: $16 + 8 + 1 = 25$.
> **Resultado:** $11001_2 = 25_{10}$.

> [!example] Ejemplo 2: Notación de bases
> Es vital usar subíndices para no confundir los sistemas:
> - $34_{10}$: Treinta y cuatro en base decimal.
> - $100010_2$: Su equivalente en base binaria.
> El subíndice indica si contamos en grupos de $10$ o de $2$.

> [!example] Ejemplo 3: Convertir $428_{10}$ a binario (Divisiones)
> | Dividendo | Mitad (Cociente) | ¿Sobró? (Residuo) |
> | :--- | :--- | :--- |
> | 428 | 214 | **0** |
> | 214 | 107 | **0** |
> | 107 | 53 | **1** |
> | 53 | 26 | **1** |
> | 26 | 13 | **0** |
> | 13 | 6 | **1** |
> | 6 | 3 | **0** |
> | 3 | **1** (Fin) | **1** |
> 
> **Resultado (leído hacia arriba):** $110101100_2$.

> [!example] Ejemplo 4: Aplicación $USD (Método de la Tabla)
> Un artículo cuesta **$25 USD**. Para convertirlo rápido, buscamos qué potencias de 2 suman 25:
> $16 + 8 + 1 = 25$.
> - Ponemos $1$ en las posiciones de 16, 8 y 1.
> - Ponemos $0$ en las posiciones de 4 y 2.
> **Resultado:** $11001_2$.

## 5. Ejercicios para el estudiante

> [!abstract] Práctica de clase
> **Nivel Fácil (Binario a Decimal):**
> 1. Convertir $10_2$
> 2. Convertir $11_2$
> 3. Convertir $101_2$
> 
> **Nivel Medio (Decimal a Binario):**
> 1. Convertir $84_{10}$
> 2. Convertir $25_{10}$
> 
> **Nivel Avanzado ($USD):**
> 1. Suma estos tres precios: $111_2 + 101_2 + 110_2$.

> [!success] Solucionario (Solo Docente)
> **Resultados de conversión:**
> - $10_2 = 2$
> - $11_2 = 3$
> - $101_2 = 5$
> - $84_{10} = 1010100_2$
> - $25_{10} = 11001_2$
> 
> **Resultado de la suma:**
> - $111_2 + 101_2 + 110_2 = 10010_2$ (Equivale a $7 + 5 + 6 = 18$).
> 
> **Dato Extra:** La suma de $50_{10} + 52_{10}$ resulta en $1100110_2$ ($102_{10}$).

## 6. Mini-prueba de autoevaluación

1. **¿Por qué el sistema binario se llama de "Base 2"?**
   - *Respuesta:* Porque solo utiliza dos símbolos ($0$ y $1$) y el valor de cada posición es una potencia de $2$.

2. **Si el valor de una posición es $128$, ¿cuál es el valor de la posición inmediatamente a su izquierda?**
   - *Respuesta:* $256$. (Cada posición es el doble de la anterior).

3. **Resuelve la suma $11_2 + 11_2$ (Tres + Tres). ¿Cuál es el resultado en binario?**
   - *Explicación:* $1+1=0$ y llevo $1$. En la siguiente columna tengo $1+1+1=1$ y llevo $1$.
   - *Respuesta:* $110_2$ (que es $6_{10}$).

## 7. Notas para el próximo tema

> [!tip] Conexión lógica
> Todo lo que aprendiste hoy sobre **valor posicional** y **acarreos** será la base para la **Clase 02 — Resta y Multiplicación Binaria**. Si dominas la suma de $1+1$, ¡ya tienes medio camino ganado para el siguiente nivel!

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> Próxima lección: [[Clase 02 — Resta y Multiplicación Binaria]]