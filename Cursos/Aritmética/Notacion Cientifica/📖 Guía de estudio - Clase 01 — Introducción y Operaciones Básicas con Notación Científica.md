# 📖 Guía de estudio — Clase 01: Introducción a la Notación Científica

> [!info] 📌 Conceptos clave
> La notación científica es la forma abreviada de escribir números muy grandes o muy pequeños para facilitar su manejo. ¡No se confundan! La clave está en observar cómo empieza el número:
> - **Números Pequeños:** Son aquellos que inician con **0.** (cero coma o cero punto). Su potencia de 10 siempre tendrá un **exponente negativo**.
> - **Números Grandes:** Son todos los demás (los que no empiezan con 0.). Su potencia de 10 tendrá un **exponente positivo**.
> - **El Coeficiente ($a$):** Debe ser un número entre 1 y 10. Puede ser 1, pero **nunca** puede llegar a ser 10.
> - **Dato importante:** La potencia $10^1$ es simplemente $10$; el exponente 1 suele ser "invisible". Además, aunque aquí usemos el punto decimal (.), recuerda que en muchos países se usa la coma (,).

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Notación Científica** | Estructura $a \times 10^n$, donde $1 \le a < 10$. |
| **Multiplicación** | Se multiplican los coeficientes y se **suman** los exponentes. |
| **División** | Se dividen los coeficientes y se **restan** los exponentes (arriba menos abajo). |
| **Exponentes Negativos** | Indican estrictamente que se trata de un **Número Pequeño** (inicia con 0.). |
| **Punto Decimal** | Debe ubicarse de modo que quede **un solo número (distinto de cero)** a su izquierda. |

## 3. Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A: Conversión de un número pequeño**
**Problema:** Convertir $0.005$ a notación científica.
1. **Identificación:** Es un **Número Pequeño** (empieza con 0.), por lo tanto, el exponente será **negativo**.
2. **Movimiento del punto:** Movemos el punto hacia la **derecha** hasta que quede después de la primera cifra que no sea cero (el 5).
   - $0.005 \to 0005.$ (el punto se movió **3 lugares**).
3. **Lógica:** Como lo movimos 3 veces y es un número pequeño, el exponente es $-3$.
4. **Resultado Final:** **$5 \times 10^{-3}$** (Los ceros a la izquierda desaparecen).
```

```ad-example
**Ejemplo B: Aplicación con dinero ($USD) y Compensación**
**Problema:** Expresar un presupuesto de $5,000,000 USD en notación científica.
1. **Identificación:** Es un **Número Grande**. El punto decimal está "invisible" al final: $5,000,000.$
2. **Movimiento del punto:** Movemos el punto hacia la **izquierda** hasta que solo quede el 5 a su izquierda.
   - $5,000,000. \to 5.000000$ (se movió **6 lugares**).
3. **Lógica de Compensación:** Al mover el punto a la izquierda, el coeficiente se hizo "más pequeño" ($5,000,000 \to 5$), por lo tanto, para equilibrar, el exponente debe ser un número positivo grande.
4. **Resultado Final:** **$5 \times 10^6$ USD**.
```

## 4. Ejercicios de Repaso

```ad-abstract
**🟢 Nivel: Fácil (Basados en Profe Alex)**
1. Convierte $5000$ a notación científica (recuerda que el punto está al final).
2. Convierte $0.003$ a notación científica.
3. Convierte $7.95$ a notación científica (¡Ojo! El punto ya está en su lugar, ¿qué pasa con el exponente?).
```

```ad-abstract
**🟡 Nivel: Medio (Operaciones y Signos)**
1. Resuelve: $(2 \times 10^3) \times (3 \times 10^2)$.
2. Resuelve: $(8 \times 10^6) \div (4 \times 10^2)$.
3. Multiplica $(5 \times 10^4) \times (2 \times 10^3)$. ¡Cuidado! Si el resultado es $10 \times 10^7$, debes ajustarlo a la forma correcta.
```

```ad-abstract
**🔴 Nivel: Avanzado (Aplicación Financiera)**
1. Un informe contable muestra un gasto de $15 \times 10^4$ USD. Aplica la **Lógica de Compensación** para mover la coma hacia la izquierda y corregir el coeficiente.
2. Divide una deuda masiva de $1.2 \times 10^9$ USD entre 400 personas. (Tip: Primero convierte 400 a $4 \times 10^2$ y luego divide).
3. Ajusta el resultado de una ganancia de $0.5 \times 10^6$ USD. Como vas a mover la coma a la derecha para que sea $5$, el número se "agranda", por lo que debes restar 1 al exponente.
```

## 5. Consejo de Estudio

> [!tip] 💡 ¡Cuidado con la "Doble Resta"!
> En la **división**, el error más común de los estudiantes es ignorar la ley de signos cuando el exponente de abajo es negativo.
> Si tienes $10^6 \div 10^{-5}$, la regla dice: "exponente de arriba **menos** exponente de abajo".
> Esto crea un choque de signos: $6 - (-5)$.
> Por ley de signos, menos por menos da más: $6 + 5 = 11$.
> **¡No restes por inercia, aplica siempre la ley de los signos!**