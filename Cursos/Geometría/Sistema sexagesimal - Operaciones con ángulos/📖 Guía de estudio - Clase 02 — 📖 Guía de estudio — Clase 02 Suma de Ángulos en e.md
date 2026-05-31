# 📖 Guía de estudio — Clase 02: Suma de Ángulos en el Sistema Sexagesimal

> [!info] 📌 Conceptos clave
> - **Naturaleza del sistema:** El sistema sexagesimal se fundamenta en la base 60 y es el estándar utilizado universalmente tanto para la medición de ángulos como para la magnitud del tiempo.
> - **Alineación posicional:** Para operar, es imperativo alinear las magnitudes en columnas específicas: grados con grados, minutos con minutos y segundos con segundos.
> - **Restricción de normalización:** En el resultado final, los valores de los minutos ($'$) y segundos ($''$) deben estar estrictamente comprendidos en el rango $[0, 59]$.
> - **Transformación de niveles de unidad:** Cuando una columna alcanza o supera las 60 unidades, se realiza una transferencia al nivel superior inmediato (hacia la izquierda). Se deben restar múltiplos de 60 ($60, 120, 180, \dots$) para normalizar la unidad actual y sumar la cantidad correspondiente de unidades ($1, 2, 3, \dots$) al nivel superior.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Grado (°)** | Unidad de nivel superior en este sistema. A diferencia de los minutos y segundos, puede exceder el valor de 60 en el resultado. |
| **Minuto (')** | Subdivisión del grado que equivale a $1/60$ de este. |
| **Segundo ('')** | Subdivisión del minuto que equivale a $1/60$ de este. |
| **Conversión de segundos** | $60'' = 1'$ (60 unidades de segundo equivalen a 1 unidad de minuto). |
| **Conversión de minutos** | $60' = 1^\circ$ (60 unidades de minuto equivalen a 1 unidad de grado). |

## Ejemplos Resueltos

```ad-example
**Ejemplo A — Caso Básico (Sin acarreo)**
**Operación:** Calcular la suma de $10^\circ 20' 32''$ y $25^\circ 12' 14''$.

**Desarrollo instruccional:**
1. **Alineación y suma por columnas:**
   - **Segundos:** $32'' + 14'' = 46''$
   - **Minutos:** $20' + 12' = 32'$
   - **Grados:** $10^\circ + 25^\circ = 35^\circ$
2. **Evaluación de normalización:** Se verifica que $46 < 60$ y $32 < 60$. Al estar ambos resultados dentro del rango $[0, 59]$, no se requiere transformación de niveles.
3. **Resultado:** $35^\circ 32' 46''$.
```

```ad-example
**Ejemplo B — Caso con Aplicación Real (Ajuste de precisión)**
En disciplinas técnicas donde el "costo por grado de precisión" es elevado, la correcta normalización del sistema sexagesimal es crítica para la interpretación de planos.
**Operación:** Sumar $35^\circ 47' 53''$ + $42^\circ 25' 25''$.

**Desarrollo instruccional:**
1. **Suma inicial:** Obtenemos $77^\circ 72' 78''$.
2. **Transformación de segundos (Nivel 1):** Como $78''$ excede el límite, restamos 60 ($78 - 60 = 18$). Esas 60 unidades se transforman en $1'$ que se transfiere a la columna de minutos.
3. **Transformación de minutos (Nivel 2):** La columna de minutos ahora tiene $72' + 1' = 73'$. Nuevamente, excedemos el límite: restamos 60 ($73 - 60 = 13$) y transferimos $1^\circ$ a la columna de grados.
4. **Resultado normalizado:** $78^\circ 13' 18''$.
```

## Ejercicios de Repaso

```ad-abstract
**🟢 Nivel Inicial (Fácil)**
Realice la suma de los siguientes ángulos asegurándose de alinear correctamente las columnas:
$15^\circ 10' 20'' + 12^\circ 15' 10''$
*Meta: Confirmar que los subtotales no requieren procesos de acarreo.*
```

```ad-abstract
**🟡 Nivel Intermedio (Medio)**
Resuelva la operación utilizando **placeholders** (ceros de posición) para los valores ausentes:
$50' 45'' + 13^\circ 0' 55''$
*Nota pedagógica: Note que el primer término carece de grados y el segundo carecía de minutos en el planteamiento original. El uso del $0'$ facilita la alineación vertical.*
```

```ad-abstract
**🔴 Nivel Avanzado (Complejo)**
Opere con ángulos de signo negativo aplicando la propiedad de suma de valores absolutos:
$(-32^\circ 0' 15'') + (-50^\circ 25' 48'')$
*Estrategia: Al poseer signos idénticos, se procede a sumar sus magnitudes absolutas y se antepone el signo negativo al resultado final normalizado.*
```

> [!tip] 💡 Consejo de estudio
> Para dominar las conversiones de base 60, recurra a la **analogía cronológica**. Al igual que en la lectura de un cronómetro evitamos decir "80 segundos" y preferimos "1 minuto con 20 segundos", en geometría operamos bajo la misma lógica. Si un subtotal supera los 120 o 180, simplemente transfiera 2 o 3 unidades respectivamente al nivel de la izquierda.