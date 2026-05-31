# 📖 Guía de estudio — Clase 03: Uso correcto de la calculadora en trigonometría

> [!info] 📌 Conceptos clave
> Dominar la calculadora no es solo saber qué teclas presionar, sino entender las "órdenes" que le damos. Según las lecciones del Profe Alex, estos son los pilares fundamentales:
> * **Configuración de unidad angular:** El error más común es operar en el sistema equivocado. Debes elegir entre Grados (**D**), Radianes (**R**) o Gradianes (**G**).
> * **La Regla de Oro de $\pi$:** Siempre que veas el símbolo $\pi$ en un ángulo, es la señal estándar de que la calculadora **debe** estar en modo **Radianes**.
> * **Función Shift:** Activa los comandos en amarillo, esenciales para funciones inversas ($sin^{-1}$) y constantes.
> * **Modo de Entrada:** El modo "Matemático" (Classwiz/ES Plus) muestra las operaciones como en el cuaderno; el modo "Lineal" (modelos MS) requiere un uso estricto de paréntesis para evitar errores graves.
> * **Sistema Sexagesimal:** La tecla de grados, minutos y segundos (`° ' "`) sigue un orden posicional estricto.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Grados (Deg / Degree)** | Sistema sexagesimal (círculo = 360°). Se marca con una **D** en pantalla. |
| **Radianes (Rad)** | Unidad basada en el radio (círculo = $2\pi$). Se marca con una **R**. Indispensable si aparece $\pi$. |
| **Gradianes (Gra)** | Sistema centesimal (círculo = 400g). Se marca con una **G**. ¡Cuidado! No confundir con grados normales. |
| **Funciones Inversas ($sin^{-1}, cos^{-1}$)** | Llamadas también **Arcoseno** o **Arcocoseno**. No son potencias, se usan exclusivamente para **hallar el valor de un ángulo**. |
| **DMS (Grados, Minutos, Segundos)** | Tecla `° ' "`. La calculadora lee las posiciones en orden: 1° = grados, 2° = minutos, 3° = segundos. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Configuración según tu modelo
Calcula $cos(180)$ asegurando que la calculadora esté en modo **Grados (DEG)**.

**Pasos por modelo:**
1. **Modelos MS (82MS, 350MS):** Presiona `Mode` dos veces hasta ver "Deg, Rad, Gra". Elige **1** (Deg).
2. **Modelos ES Plus:** Presiona `Shift` + `Setup` y elige la opción **3** (Deg).
3. **Modelos Classwiz (991 LAX):** Presiona `Shift` + `Menu` → `2: Unidad Angular` → `1: Grado sexagesimal`.
**Operación:** Presiona `cos`, escribe `180` y cierra paréntesis.
✅ **Resultado:** $-1$
```

```ad-example
title: Ejemplo B — Aplicación de la Ley de Cosenos
Cálculo: $\sqrt{12^2 + 7^2 - 2 \cdot 12 \cdot 7 \cdot cos(40)}$

**⚠️ Advertencia crítica (Modelos Lineales/MS):**
Si usas una calculadora MS, **debes abrir un paréntesis inmediatamente después de la raíz** $\sqrt{(...}$. Si no lo haces, la calculadora solo sacará la raíz de $12^2$ y restará el resto, dándote un resultado totalmente erróneo.

**Instrucciones:**
1. Ingresa la raíz. En modo Matemático, verás cómo se alarga. En modo Lineal, escribe `√(`.
2. Escribe los valores respetando cuadrados y productos.
3. Cierra el paréntesis del ángulo y (en modo lineal) el de la raíz.
✅ **Resultado:** $8,01$
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Práctica de funciones simples
Configura tu calculadora en modo **Grados (D)** y resuelve:
1. $sen(30^{\circ})$  → *Resultado: 0,5 (o 1/2)*
2. $cos(0)$ → *Resultado: 1*
3. $tan(45^{\circ})$ → *Resultado: 1*
```

```ad-abstract
title: 🟡 Medio — Cambios de modo y DMS
Atención a las unidades y a la posición de los datos:
1. $sen(\pi/2)$: Configura en **Radianes (R)** antes de operar. → *Resultado: 1*
2. $cos(30^{\circ} 40' 15'')$: Usa la tecla `° ' "`. → *Resultado: 0,86*
3. $tan(20^{\circ} 0' 15'')$: **Regla del Cero:** Como no hay minutos, debes marcar `20 [°'"] 0 [°'"] 15 [°'"]`. Si saltas el cero, la calculadora pensará que 15 son minutos.
```

```ad-abstract
title: 🔴 Avanzado — Fórmulas y Funciones Inversas
**Tip:** Usa la tecla de fracción ($\frac{\square}{\square}$) para que la pantalla se vea igual al ejercicio; así evitarás errores de sintaxis.
1. **Fracción compleja:** $\frac{15 \cdot sen(48)}{sen(60)}$. → *Resultado: 12,87*
2. **Hallar ángulo (Inversa):** $sen^{-1}\left(\frac{10 \cdot sen(115)}{40}\right)$. Asegúrate de estar en modo **Grados (D)** para obtener el ángulo en el sistema común.
✅ **Resultado:** $13,09^{\circ}$
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> **Estrategia de verificación:** Antes de cualquier examen, mira la letra pequeña arriba (**D** o **R**). El error más común no es matemático, es de configuración. 
> 
> **¿"Syntax Error"?** No borres todo. Usa las flechas para ver dónde falló el cursor; usualmente es un paréntesis sin cerrar o un signo de operación mal puesto. **Recuerda:** $sin^{-1}$ no es una potencia, es una función; actívala siempre con `Shift`.