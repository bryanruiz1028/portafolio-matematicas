# Clase 03 — Conversión de unidades de TIEMPO

#algebra #conversionofunits

[« Clase Anterior](enlace_clase_anterior) | [Siguiente Clase »](enlace_siguiente_clase)

---

### ¿POR QUÉ ES IMPORTANTE ESTA CLASE?

Dominar la conversión de unidades de tiempo no es solo un ejercicio matemático; es la herramienta que nos permite coordinar el mundo, desde la precisión de un experimento científico hasta la gestión de nuestro recurso más valioso: el tiempo.

*   **Punto de $USD:** En el mundo profesional, el tiempo es dinero. Si cobras por hora de consultoría, necesitas convertir minutos exactos a decimales de hora para emitir facturas correctas y transparentes.
*   **Construcción:** Los proyectos se planifican en meses o semanas, pero la ejecución y el pago de nóminas se calculan en días. Un error de conversión puede arruinar un presupuesto de obra.
*   **Cotidiano:** Desde calcular cuánto falta para que aterrice un avión hasta organizar una agenda de eventos, saber moverte entre horas, minutos y segundos es vital para la puntualidad.

---

### CONCEPTO CLAVE

La **Conversión de Unidades de Tiempo** es el proceso de cambiar la unidad de medida de una cantidad sin alterar su valor real. Para lograrlo, utilizamos el **Factor de Conversión**.

> [!abstract] **El secreto del Factor de Conversión**
> Matemáticamente, el factor de conversión es una fracción que vale **1**. Como el numerador y el denominador representan la misma cantidad (ej. $60 \text{ min} = 1 \text{ hora}$), al multiplicar cualquier cifra por esta fracción, su valor no cambia, solo se transforma su "apellido" (la unidad).

#### Tabla de Equivalencias (Referencia Profe Alex)
Para trabajar con éxito, debemos tener claras estas igualdades fundamentales:
*   **1 año:** $365 \text{ días} = 12 \text{ meses} = 2 \text{ semestres} = 3 \text{ cuatrimestres} = 4 \text{ trimestres}$.
*   **1 semestre:** $6 \text{ meses} = 2 \text{ trimestres}$.
*   **1 cuatrimestre:** $4 \text{ meses}$.
*   **1 trimestre:** $3 \text{ meses}$.
*   **1 semana:** $7 \text{ días}$.
*   **1 día:** $24 \text{ horas}$.
*   **1 hora:** $60 \text{ minutos} = 3600 \text{ segundos}$.
*   **1 minuto:** $60 \text{ segundos}$.

> [!CAUTION] **Error común: El mito decimal**
> Un error muy frecuente en mis estudiantes es creer que los decimales funcionan igual que el tiempo. **$15,6 \text{ horas}$ NO son $15 \text{ horas y } 6 \text{ minutos}$.** El $,6$ es una fracción decimal que debe convertirse a base 60.

> [!TIP] **Truco: Cancelación Diagonal**
> Para que el factor de conversión funcione, la unidad que quieres eliminar **debe estar en el lado opuesto** de la fracción. Si tu unidad original está "arriba", ponla "abajo" en el factor de conversión. ¡Así podrás simplificarlas como si fueran números!

---

### PROCEDIMIENTO PASO A PASO

Sigue este método sistemático para no fallar nunca:

```text
PASO 1: Identificar la equivalencia necesaria entre las dos unidades.
PASO 2: Escribir la cantidad inicial seguida de un signo de multiplicación.
PASO 3: Plantear la fracción (Factor de Conversión), colocando la unidad a 
        eliminar abajo y la unidad deseada arriba.
PASO 4: Multiplicar los números y simplificar las unidades repetidas.
```

---

### EJEMPLOS

> [!example] **Ejemplo 1: Conversión Básica ($5 \text{ horas a minutos}$)**
> 1. **Equivalencia:** $1 \text{ hora} = 60 \text{ min}$.
> 2. **Planteamiento:** $5 \text{ horas} \times \frac{60 \text{ min}}{1 \text{ hora}}$
> 3. **Resolución:** Simplificamos "horas". Multiplicamos $5 \times 60 = 300$.
> 4. **Resultado:** $300 \text{ minutos}$.

> [!example] **Ejemplo 2: Pasos Múltiples ($12 \text{ días a segundos}$)**
> Cuando no hay una equivalencia directa, creamos una cadena de fracciones:
> $$12 \text{ días} \times \frac{24 \text{ horas}}{1 \text{ día}} \times \frac{3600 \text{ segundos}}{1 \text{ hora}}$$
> *   **Simplificación:** Los "días" se van con "días", las "horas" con "horas".
> *   **Cálculo:** $12 \times 24 \times 3600 = 1.036.800$.
> *   **Resultado:** $1.036.800 \text{ segundos}$.

> [!example] **Ejemplo 3: El Caso Decimal ($15,6 \text{ horas}$)**
> Para dar una respuesta clara, separamos la parte entera de la decimal:
> 1. **Parte entera:** $15 \text{ horas}$ (ya las tenemos).
> 2. **Parte decimal:** Convertimos $0,6 \text{ horas}$ a minutos:
>    $$0,6 \text{ horas} \times \frac{60 \text{ min}}{1 \text{ hora}} = 36 \text{ min}$$
> 3. **Resultado Final:** $15 \text{ horas y } 36 \text{ minutos}$.

> [!example] **Ejemplo 4: Aplicación Financiera ($USD$)**
> **Problema:** Si un consultor cobra $\$50 \text{ USD}$ por hora, ¿cuánto cobrará por un trabajo de $150 \text{ minutos}$?
> 1. **Convertir tiempo a horas:** $150 \text{ min} \times \frac{1 \text{ hora}}{60 \text{ min}} = 2,5 \text{ horas}$.
> 2. **Calcular costo:** $2,5 \text{ horas} \times \$50 \text{ USD/hora} = \$125$.
> 3. **Resultado:** El consultor debe cobrar $\$125 \text{ USD}$.

---

### EJERCICIOS PARA EL ESTUDIANTE

**🟢 Nivel Fácil (Conversión Simple)**
1. Convertir $5$ semanas a días.
2. Convertir $3$ años a meses.
3. Convertir $4$ semestres a meses.
4. Convertir $240$ minutos a horas.

**🟡 Nivel Medio (Múltiples Pasos y Decimales)**
1. Convertir $1,5$ días a minutos.
2. Convertir $0,5$ años a meses (usa la equivalencia exacta).
3. Convertir $3$ cuatrimestres a meses.
4. Convertir $2$ trimestres a meses.

**🔴 Nivel Avanzado (Aplicación y Costos $USD$)**
1. Un especialista cobra $\$60 \text{ USD}$ por hora. ¿Cuánto cobra por una sesión de $45 \text{ minutos}$?
2. Una licencia de software cuesta $\$15 \text{ USD}$ al mes. ¿Cuál es el costo por día? (Considera $1 \text{ mes} = 30 \text{ días}$).
3. Un servidor web cuesta $\$0,10 \text{ USD}$ por cada hora de encendido. ¿Cuánto costará tenerlo activo durante $30$ días?
4. Si un equipo se alquila por $\$20 \text{ USD}$ la hora, ¿cuánto pagas por $150 \text{ minutos}$ de uso?

> [!success] **Solucionario**
> **Fácil:** 1) $35 \text{ días}$ | 2) $36 \text{ meses}$ | 3) $24 \text{ meses}$ | 4) $4 \text{ horas}$.
> **Medio:** 1) $2.160 \text{ min}$ | 2) $6 \text{ meses}$ | 3) $12 \text{ meses}$ | 4) $6 \text{ meses}$.
> **Avanzado:** 1) $\$45 \text{ USD}$ | 2) $\$0,50 \text{ USD}$ | 3) $\$72 \text{ USD}$ | 4) $\$50 \text{ USD}$.

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] **Pregunta 1**
> ¿Por qué decimos que el factor de conversión no cambia el valor de la medida original?
> *   a) Porque suma unidades iguales.
> *   b) Porque equivale a multiplicar por 1.
> *   c) Porque solo se usa con números enteros.

> [!question] **Pregunta 2**
> Si conviertes $4,5$ días a un formato de días y horas, obtienes:
> *   a) $4 \text{ días y } 5 \text{ horas}$.
> *   b) $4 \text{ días y } 12 \text{ horas}$.
> *   c) $4 \text{ días y } 50 \text{ horas}$.

> [!question] **Pregunta 3**
> Una máquina consume $\$4 \text{ USD}$ de combustible por hora. ¿Cuánto gasta en $15$ minutos?
> *   a) $\$1 \text{ USD}$.
> *   b) $\$2 \text{ USD}$.
> *   c) $\$0,50 \text{ USD}$.

---

### NOTAS PARA EL PRÓXIMO TEMA

¡Excelente trabajo! Has dominado el arte de convertir el tiempo. En la próxima clase, aplicaremos este mismo método de **"Cancelación Diagonal"** a las **Unidades de Longitud (metros, kilómetros, etc.)**. Verás que una vez que entiendes que el factor de conversión es simplemente multiplicar por 1, ¡puedes convertir cualquier unidad del universo!

---
[« Clase Anterior](enlace_clase_anterior) | [Siguiente Clase »](enlace_siguiente_clase)