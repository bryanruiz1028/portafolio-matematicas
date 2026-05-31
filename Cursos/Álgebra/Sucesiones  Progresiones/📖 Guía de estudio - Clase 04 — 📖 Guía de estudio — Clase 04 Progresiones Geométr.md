# 📖 Guía de estudio — Clase 04: Progresiones Geométricas

> [!info] 📌 Conceptos clave
> - **Progresión Geométrica:** Es una secuencia de números donde cada término (después del primero) se obtiene multiplicando el anterior por una cantidad constante llamada **razón**. ¡Es como un salto que siempre multiplica!
> - **Razón ($r$):** Es el factor constante de la progresión. Podemos hallarla dividiendo cualquier término para el anterior.
> - **Interpolar medios geométricos:** ¡No te asustes con el nombre! Solo significa "meter" una cantidad de números entre otros dos para que todos juntos formen una progresión geométrica. 
> - **Lógica del número de términos ($n$):** Para interpolar, recuerda que el número total de términos siempre será $n = k + 2$ (donde $k$ es la cantidad de medios que quieres insertar).

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Progresión Geométrica** | Sucesión donde el siguiente término se halla multiplicando el actual por una razón constante ($r$). |
| **Razón ($r$) — Caso 1** | Cuando conoces términos consecutivos: $r = \frac{a_n}{a_{n-1}}$ |
| **Razón ($r$) — Caso 2** | Cuando conoces el primero ($a_1$) y el último ($a_n$): $r = \sqrt[n-1]{\frac{a_n}{a_1}}$ <br> *¡Ojo! Si el índice ($n-1$) es **par**, la raíz tiene dos soluciones: $\pm r$.* |
| **Término General ($a_n$)** | Para encontrar cualquier posición: $a_n = a_1 \cdot r^{n-1}$ |
| **Suma de Términos ($S_n$)** | Para sumar los primeros $n$ términos: $S_n = \frac{a_1(r^n - 1)}{r - 1}$ <br> *(Válido solo si $r \neq 1$)* |
| **Medios Geométricos** | Son los términos que se encuentran entre los extremos de una progresión. |

## Ejemplos resueltos adicionales

```ad-example
**Ejemplo A — Caso Básico (Interpolación)**
¡Vamos a interpolar 3 medios geométricos entre 3 y 48! 

- **Paso 1: ¡Identifiquemos nuestros datos!** 
  El primer término es $a_1=3$. El último es $a_n=48$. Como queremos meter 3 medios, usamos nuestra lógica: $n = 3 + 2 = 5$ términos en total.
- **Paso 2: Aplicar la fórmula de la razón.**
  $r = \sqrt[5-1]{\frac{48}{3}} = \sqrt[4]{16}$
- **Paso 3: ¡Pilas con la raíz par!** 
  Como el índice es 4 (par), el resultado puede ser $2$ o $-2$. 

✅ **Resultado:** ¡Tenemos dos soluciones posibles!
1. Si $r=2$: **(3, 6, 12, 24, 48)**
2. Si $r=-2$: **(3, -6, 12, -24, 48)**
```

```ad-example
**Ejemplo B — Aplicación con $USD**
Imagina que empiezas un ahorro con $2 USD y decides triplicar esa cantidad cada mes. ¿Cuánto dinero tendrás exactamente en el mes 4?

- **Paso 1: ¿Qué información tenemos?** 
  Empezamos con $a_1=2$. Como se triplica, la razón es $r=3$. Queremos el mes $n=4$.
- **Paso 2: Usemos la fórmula del término general.**
  $a_4 = 2 \cdot 3^{4-1}$
  $a_4 = 2 \cdot 3^3 = 2 \cdot 27 = 54$

✅ **Resultado:** En el mes 4 tendrás **$54 USD**. ¡Nada mal para empezar con dos pesitos!
```

## Ejercicios de repaso

```ad-abstract
**🟢 Fácil**
1. ¡A simple vista! Identifica la razón ($r$) en esta secuencia: 4, 12, 36...
2. Si tenemos 1, 3, 9... ¿Cuál será el valor del término $a_5$? (Pista: ¡puedes hacerlo multiplicando!).
3. Investiga: ¿Es la sucesión 5, 10, 15, 20 una progresión geométrica? Justifica tu respuesta.
```

```ad-abstract
**🟡 Medio**
1. Interpolar 2 medios geométricos entre 5 y 40. ¡No olvides revisar si hay más de una solución!
2. Halla la razón ($r$) si el primer término es $a_1=10$ y el tercero es $a_3=90$.
3. Encuentra el término $a_9$ de la progresión descendente: 96, 48, 24... (¡Aquí la razón es una fracción!).
```

```ad-abstract
**🔴 Avanzado — Aplicación con $USD**
1. Inviertes $5 USD y el monto se duplica cada periodo. ¿Cuál es la suma total ($S_{10}$) al final de 10 periodos?
2. Un ahorro acumulado sigue la progresión 5, 10, 20... USD. Usa la fórmula de la suma para hallar el total en el décimo término.
3. ¡El reto final! Calcula el valor total de una serie de 7 pagos que empiezan en $2 USD y se triplican en cada cuota.
```

> [!tip] 💡 Consejo de estudio
> **¡La lógica manda sobre la memoria!** Como dice el Profe Alex, si la progresión es cortita, no te compliques: verifica tus resultados multiplicando manualmente por la razón. Además, un truco de experto: cuando calcules la razón con la raíz, **simplifica la fracción al máximo** antes de operar. ¡Te ahorrará muchos dolores de cabeza y las raíces saldrán mucho más fácil!