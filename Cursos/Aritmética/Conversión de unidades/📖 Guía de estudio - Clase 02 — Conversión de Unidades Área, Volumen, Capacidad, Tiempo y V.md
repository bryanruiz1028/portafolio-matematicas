# 📖 Guía de estudio — Clase 02: Conversión de Unidades de Área

> [!info] 📌 Conceptos clave
> La **magnitud de superficie** o área se diferencia de la longitud por su naturaleza bidimensional. Basándonos en las lecciones del Profe Alex, debemos dominar estos fundamentos:
> * **Naturaleza de las unidades:** Las unidades de superficie siempre se expresan con el **exponente 2** ($m^2, cm^2$), lo cual indica que trabajamos con dos dimensiones (largo y ancho).
> * **La Escalera de Conversión:** Existe una jerarquía estricta que debemos memorizar para desplazarnos correctamente:
>   $$km^2 \text{ (Kilómetro)} \rightarrow hm^2 \text{ (Hectómetro)} \rightarrow dam^2 \text{ (Decámetro)} \rightarrow m^2 \text{ (Metro)} \rightarrow dm^2 \text{ (Decímetro)} \rightarrow cm^2 \text{ (Centímetro)} \rightarrow mm^2 \text{ (Milímetro)}$$
> * **La Regla del 100 ($10^2$):** Debido a que son unidades cuadradas, cada escalón representa un factor de $100$. Esto significa que por cada paso que demos, agregamos o quitamos **dos ceros**, o desplazamos la coma **dos posiciones**.

---

## 2. Tabla de Fórmulas y Definiciones Importantes

| Término | Abreviación | Definición / Lógica | Dirección |
| :--- | :--- | :--- | :--- |
| **Metro cuadrado** | $m^2$ | Unidad central de superficie. | **Base** |
| **Bajar escalones** | $\downarrow$ | Multiplicar por $100$ por cada nivel. Desplaza la coma a la **derecha**. | **Multiplicación** |
| **Subir escalones** | $\uparrow$ | Dividir entre $100$ por cada nivel. Desplaza la coma a la **izquierda**. | **División** |
| **Coma Implícita** | `,` | Si un número no tiene coma visible (entero), esta se ubica al **final**. | **Nota Especial** |
| **Limpieza de Ceros** | $0$ | Los ceros al final de una cifra decimal (a la derecha) deben eliminarse. | **Regla Alex** |

---

## 3. Sección de Ejemplos Resueltos

```ad-example
title: Ejemplo A: Conversión Básica (Hacia abajo)
**Problema:** Convertir $5$ hectómetros cuadrados ($hm^2$) a metros cuadrados ($m^2$).

**Paso a paso:**
1. **Identificar trayectoria:** Estamos en $hm^2$ y descendemos hacia $m^2$.
2. **Contar saltos:** Bajamos $2$ escalones ($hm^2 \to dam^2$ y $dam^2 \to m^2$).
3. **Cálculo de posiciones:** Como son $2$ escalones y cada uno vale $2$ ceros: $2 \times 2 = 4$ ceros.
4. **Aplicar operación:** 
   $$\text{Operación: } 5 \times 10,000 = 50,000$$

**Resultado:** $5 \text{ hm}^2$ equivalen a **$50,000 \text{ m}^2$**.
```

```ad-example
title: Ejemplo B: Aplicación Práctica (Costo de Superficie)
**Problema:** Un material cubre una superficie de $320,000 \text{ cm}^2$. Si el costo por metro cuadrado ($m^2$) es de $10 \text{ USD}$, ¿cuál es el presupuesto total?

**Paso a paso:**
1. **Conversión de unidad:** Pasamos de $cm^2$ a $m^2$. Subimos $2$ escalones.
2. **Desplazamiento:** Al subir $2$ escalones, dividimos por $10,000$ (quitamos $4$ ceros o movemos la coma $4$ lugares a la izquierda).
   $$320,000 \div 100 \div 100 = 32 \text{ m}^2$$
3. **Cálculo Financiero:** Multiplicamos el área resultante por el costo unitario.
   $$32 \text{ m}^2 \times 10 \text{ USD} = 320 \text{ USD}$$

**Resultado:** El costo total es de **$320 \text{ USD}$**.
```

---

## 4. Ejercicios de Repaso Graduados

```ad-abstract
title: 🟢 Nivel: Fácil (Descenso Directo)
**Instrucción:** Realiza las conversiones multiplicando por potencias de 100.
1. Convierte $12 \text{ m}^2$ a $mm^2$.
2. Convierte $7 \text{ km}^2$ a $hm^2$.

*Respuesta:*
1. $12,000,000 \text{ mm}^2$ (3 saltos = 6 ceros).
2. $700 \text{ hm}^2$ (1 salto = 2 ceros).
```

```ad-abstract
title: 🟡 Nivel: Medio (Uso de Coma Decimal)
**Instrucción:** Convierte **$580 \text{ cm}^2$ a $dam^2$**. 
*Recuerda:* Ubica la coma al final del número y desplázala hacia la izquierda. Aplica la regla de "Limpieza de Ceros" de Profe Alex.

*Solución:*
1. Identificar saltos: $cm^2 \to dm^2 \to m^2 \to dam^2$ ($3$ escalones).
2. Espacios a mover: $3 \times 2 = 6$ lugares a la izquierda.
3. Movimiento: $580,0 \to 0.000580$.
4. Limpieza: **$0.00058 \text{ dam}^2$**.
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Reto de Presupuesto)
**Instrucción:** Un ingeniero debe impermeabilizar una terraza de **$52.31 \text{ m}^2$**.
1. Convierte la superficie a milímetros cuadrados ($mm^2$).
2. Si el producto sellador cuesta **$0.0005 \text{ USD}$** por cada $mm^2$, calcula el costo total.

*Solución paso a paso:*
1. De $m^2$ a $mm^2$ hay $3$ escalones hacia abajo $\to$ $6$ espacios a la derecha.
   $52.31 \to 52,310,000 \text{ mm}^2$.
2. Multiplicar por costo: $52,310,000 \times 0.0005 = 26,155$.
**Resultado Final:** El presupuesto es de **$26,155 \text{ USD}$**.
```

---

> [!tip] 💡 Consejo de estudio del Profe Alex
> Para no fallar en la conversión de área, utiliza siempre la fórmula técnica:
> **(Número de escalones) $\times$ 2 = Número de espacios que se mueve la coma.**
> * Si **bajas**, la coma busca la derecha (multiplicas).
> * Si **subes**, la coma busca la izquierda (divides).
> No olvides eliminar los ceros sobrantes al final de tus decimales para mantener la precisión académica.