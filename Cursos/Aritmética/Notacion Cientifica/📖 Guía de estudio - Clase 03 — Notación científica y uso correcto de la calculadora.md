# 📖 Guía de estudio — Clase 03: Notación científica y uso de la calculadora

> [!info] 📌 Conceptos clave
> * **Configuración orientada al resultado:** La calculadora debe prepararse según el formato en el que se necesite la respuesta (Científica o Normal). No importa cómo se ingresen los datos, el dispositivo transformará el resultado al modo configurado.
> * **Diferencia entre Sci y Norm 2:** El modo **Sci** (Scientific) obliga a mostrar potencias de 10. El modo **Norm 2** es preferible para el trabajo diario porque mantiene la visualización decimal lo más posible, evitando que números pequeños (como 0.001) se conviertan prematuramente a notación científica.
> * **Uso de la tecla de potencia (`x10^x`):** Para evitar errores de jerarquía, utilice siempre la tecla dedicada para la base 10. No es necesario escribir manualmente la base ni el símbolo de potencia.
> * **Signo Negativo vs. Resta:** Existe una distinción crítica entre la tecla de operación resta (`-`) y la tecla de valor negativo `(-)`. Usar la tecla de resta en un exponente provocará un **"Syntax Error"**.
> * **El separador decimal (Punto vs. Comma):** La interpretación varía según el modelo. En la **Classwiz**, la coma se visualiza y lee como coma decimal. En los modelos **ES/LA PLUS**, el punto físico en pantalla debe leerse como la coma decimal, según la convención regional.

## 2. Tabla de Fórmulas y Definiciones

| Término | Definición / Ruta de acceso |
| :--- | :--- |
| **Notación Científica (Modo Sci)** | Formato $a \times 10^n$. <br> **Classwiz:** `Setup -> 3 (Formato de número) -> 2 (Sci)`. <br> **ES Plus:** `Shift + Mode -> 7 (Sci)`. |
| **Notación Normal (Modo Norm 2)** | Formato decimal estándar. Se elige la opción **2** para que solo los números extremadamente pequeños se muestren en notación científica, facilitando la lectura a estudiantes. |
| **Cifras Significativas** | Al activar el modo Sci, se elige un rango (0-9). Se recomienda seleccionar entre **5 y 9** para evitar la pérdida de precisión por redondeo excesivo. |
| **Tecla [S-D]** | Función esencial para alternar entre el "Modo Matemático" (fracciones o resultados con $\pi$) y el "Modo Lineal/Decimal" (notación científica o decimales). |

## 3. Configuración de la Calculadora (Guía Rápida)

Siga estas secuencias precisas para configurar su herramienta de trabajo:

### Modelos Classwiz (570/911 LAX)
1.  Presione `Shift + Setup`.
2.  Seleccione **3 (Formato de número)**.
3.  Elija el modo:
    *   **2 (Sci):** Luego presione un número del **5 al 9** (cantidad de dígitos de precisión).
    *   **3 (Norm):** Seleccione siempre la opción **2** para priorizar decimales.

### Modelos ES/LA PLUS (82/350/570)
1.  Presione `Shift + Mode`.
2.  Seleccione el modo deseado:
    *   **7 (Sci):** Indique la precisión (se recomienda **5** o **6**).
    *   **8 (Norm):** Presione **2** para confirmar el modo normal extendido.

## 4. Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A: Conversión de decimal a científica**
**Problema:** Convertir el valor `0.000012` a notación científica.
1. Configure en modo **Sci** (precisión 5).
2. Ingrese `0.000012` y presione `=`.
3. Si el resultado es una fracción, presione `[S-D]`.
**Resultado:** $1.2000 \times 10^{-5}$
*Nota: Los ceros finales aparecen porque configuramos 5 cifras significativas.*
```

```ad-example
**Ejemplo B: Suma mixta en modo Normal**
**Problema:** Calcular $32,000 + 5.42 \times 10^9$ y ver el resultado decimal.
1. Configure en modo **Norm 2**.
2. Ingrese: `32000 + 5.42 [x10^x] 9`.
3. Presione `=`.
**Resultado en pantalla:** `5420032000`
**Interpretación:** La calculadora muestra el número completo (5,420,032,000) porque en Norm 2 todavía hay espacio físico en pantalla para representar la magnitud sin recurrir a la potencia de 10.
```

## 5. Ejercicios de Repaso Graduados

```ad-abstract
**🟢 Nivel Fácil: Conversión Directa**
Configure su calculadora en modo **Sci** y convierta los siguientes valores:
1.  450,000  *(Resp: $4.5000 \times 10^5$)*
2.  0.00000089 *(Resp: $8.9000 \times 10^{-7}$)*
3.  1,250,000,000 *(Resp: $1.2500 \times 10^9$)*
```

```ad-abstract
**🟡 Nivel Medio: Operaciones en Formato Decimal**
Realice las siguientes sumas y restas en **Modo Norm 2**:
1.  $(2.5 \times 10^4) + 15,000$ *(Resp: 40000)*
2.  $0.0005 - (1.2 \times 10^{-4})$ *(Resp: 0.00038)*
3.  $(3.2 \times 10^5) + (4.8 \times 10^5)$ *(Resp: 800000)*
```

```ad-abstract
**🔴 Nivel Avanzado: Magnitudes y Límites**
Calcule los casos expresando el resultado final en **Notación Científica**:
1.  Multiplicar $5,420,000,000 \times 1.5$. *(Resp: $8.1300 \times 10^9$)*
2.  Dividir una deuda de 987,000,000 USD entre 1,000,000 de personas. *(Resp: $9.8700 \times 10^2$)*
3.  Multiplicar $98,000,000 \times 987,000,000$. Observe cómo la calculadora gestiona el exceso de dígitos. *(Resp: $9.6726 \times 10^{16}$)*
```

## 6. Consejo de Estudio Final

> [!tip] 💡 Gestión de límites de pantalla
> Si su calculadora muestra un resultado en notación científica a pesar de estar configurada en modo **Norm**, no se trata de un error. Esto ocurre porque el número es tan grande (exceso de ceros a la derecha) o tan pequeño (exceso de ceros a la izquierda) que **no cabe físicamente en el visor**. En esos límites de magnitud, la calculadora siempre recurrirá a la notación científica para garantizar que usted pueda leer un valor exacto.