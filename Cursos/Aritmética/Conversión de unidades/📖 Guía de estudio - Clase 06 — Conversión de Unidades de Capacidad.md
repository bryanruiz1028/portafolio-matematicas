# 📖 Guía de estudio — Clase 06: Conversión de Unidades de Capacidad

**1. Resumen de Conceptos Clave**

> [!info] 📌 Conceptos clave
> 1. **Factor de conversión:** Es una operación matemática que consiste en multiplicar una cantidad por una razón o fracción cuyo numerador y denominador son equivalentes (valen lo mismo). Esto permite cambiar la unidad de medida sin alterar el valor real de la cantidad.
> 2. **Método de la "escalera":** En el sistema de unidades de capacidad, cada vez que bajamos un escalón en la jerarquía (ej. de litros a decilitros), se debe multiplicar la cantidad por 10.
> 3. **Regla de oro (Homogeneidad):** Para realizar cualquier operación matemática (comparar, sumar o dividir), es estrictamente necesario que todas las cantidades estén expresadas en la misma unidad de medida.
> 4. **Lógica de redondeo en aplicaciones reales:** En problemas de envasado o compras, si el resultado matemático arroja decimales (ej. 352.9 botellas), se debe aplicar una lógica práctica y redondear al número entero superior (353). Esto se debe a que no es posible adquirir o utilizar una fracción física de un envase en la realidad.

**2. Fórmulas y Definiciones Importantes**

| Término | Definición | Ejemplo |
| :--- | :--- | :--- |
| **Factor de conversión** | Multiplicación por una razón donde el numerador y el denominador representan la misma cantidad en distintas unidades. | $10 \text{ L} \times \frac{100 \text{ cl}}{1 \text{ L}}$ |
| **Escalón de capacidad** | Relación decimal entre unidades contiguas de capacidad; se multiplica o divide por 10 según el sentido del movimiento. | $1 \text{ dal} \to 10 \text{ L}$ (bajar 1 escalón) |
| **Equivalencia** | Relación de igualdad entre dos medidas que expresan la misma cantidad en diferentes unidades de capacidad. | $1 \text{ hl} = 100 \text{ L}$ o $1 \text{ L} = 1,000 \text{ ml}$ |

**3. Ejemplos Resueltos Adicionales**

```ad-example
title: Ejemplo A — Conversión de unidades mayores a menores
**Enunciado:** Convertir 3 Hectolitros (hl) a Centilitros (cl).

**Paso 1: Identificar los escalones.**
Para pasar de hectolitros (hl) a centilitros (cl) debemos descender por la escala: hl → dal → L → dl → cl. Esto representa bajar 4 escalones.

**Paso 2: Realizar la multiplicación.**
Cada escalón equivale a multiplicar por 10. Bajar 4 escalones equivale a multiplicar por 10,000 ($10 \times 10 \times 10 \times 10$).
$3 \text{ hl} \times 10,000 = 30,000 \text{ cl}$

**Resultado:** $\mathbf{30,000\ cl}$
```

```ad-example
title: Ejemplo B — Cálculo de precio de venta y ganancia
**Enunciado:** Un comerciante compra vino por un total de $27,000 USD, pagando $180 USD por cada decalitro (dal). ¿A cuánto debe vender el litro (L) para obtener una ganancia total de $3,000 USD?

**Paso 1: Hallar la cantidad comprada.**
Dividimos el costo total entre el precio por unidad:
$27,000 \div 180 = 150 \text{ dal}$

**Paso 2: Convertir a la unidad de venta (Litros).**
Como se venderá por litro, convertimos los decalitros multiplicando por 10 (un escalón abajo):
$150 \text{ dal} \times 10 = 1,500 \text{ L}$

**Paso 3: Calcular el ingreso total necesario.**
Suma del costo original más la ganancia deseada:
$27,000 \text{ USD} + 3,000 \text{ USD} = 30,000 \text{ USD}$

**Paso 4: Calcular el precio unitario de venta.**
Dividimos el ingreso total entre la cantidad de litros disponibles:
$30,000 \div 1,500 = 20$

**Resultado:** Debe vender cada litro a $\mathbf{\$20\ USD}$.
```

**4. Ejercicios de Repaso**

```ad-abstract
title: 🟢 Nivel Fácil
1. Convertir 5 hectolitros (hl) a litros (L) usando factores de conversión.
2. Convertir 8 decilitros (dl) a centilitros (cl).
3. ¿A cuántos mililitros (ml) equivalen 4.5 litros (L)?
```

```ad-abstract
title: 🟡 Nivel Medio
Se desea envasar 4 decilitros (dl) de un jarabe en botellas pequeñas cuya capacidad individual es de 70 centilitros (cl).
* ¿Cuántas botellas se necesitan para contener todo el líquido? 
*(Pista: Compare el volumen total convertido a cl con la capacidad del envase y aplique la lógica de contenedores).*
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicación con $USD
Un distribuidor compra aceite a un precio de $250 USD por cada decalitro (dal). Si desea obtener una ganancia total de $5,000 USD sobre una inversión inicial de $27,000 USD:
1. Calcule cuántos decalitros (dal) compró originalmente.
2. Determine a qué precio debe vender cada **decilitro (dl)** para alcanzar dicha ganancia total.
*(Nota: Requiere conversión de dal a L y luego a dl).*
```

**5. Consejo de Estudio**

> [!tip] 💡 Consejo de estudio
> Para que el factor de conversión sea infalible, utiliza la técnica de "cancelación de unidades" al **plantear la razón de conversión**. La unidad que deseas eliminar siempre debe colocarse en la posición inversa a la original: si la unidad de partida está en el numerador (arriba), colócala en el denominador (abajo) de tu fracción de conversión. Esto asegura que las unidades se anulen matemáticamente y el resultado final sea técnicamente preciso.