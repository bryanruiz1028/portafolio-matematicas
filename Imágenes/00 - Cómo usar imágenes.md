# 🖼️ Guía rápida — Imágenes en Obsidian

---

## 📁 Estructura de carpetas

```
Imágenes/
├── Aritmética/
│   └── Números decimales/    ← imágenes para esas clases
├── Geometría/
└── Álgebra/
```

---

## ✅ Cómo pegar una imagen

### Opción 1 — Arrastrar y soltar
1. Abre la nota donde quieres la imagen
2. Arrastra el archivo de imagen desde el Explorador de Windows
3. Suéltalo dentro de la nota
4. Obsidian la copia automáticamente a la carpeta `Imágenes/`

### Opción 2 — Copiar y pegar
1. Copia la imagen (Ctrl+C desde cualquier lugar)
2. Ve a tu nota en Obsidian
3. Pega con Ctrl+V
4. Se guarda automáticamente en `Imágenes/`

### Opción 3 — Captura de pantalla directa
1. Toma captura con Windows (Win+Shift+S)
2. Pega en Obsidian con Ctrl+V
3. ¡Listo! Ya está incrustada

---

## 📝 Sintaxis para mostrar imágenes

```markdown
![[nombre.png]]               ← tamaño original
![[nombre.png|500]]           ← 500px de ancho
![[nombre.png|300x200]]       ← ancho x alto exacto
```

---

## 💡 Ejemplos para clases de matemáticas

```markdown
## Recta decimal

![[recta-decimal.png|600]]

## Diagrama de fracciones

![[fracciones-equivalentes.png|400]]

## Ejercicio resuelto (foto de pizarra)

![[pizarra-clase06.jpg|500]]
```

---

## 🎨 Crear diagramas con Excalidraw

1. Presiona **Ctrl+Shift+P**
2. Busca: `Excalidraw: Create new drawing`
3. Dibuja tu diagrama
4. Para incrustar en una nota: `![[mi-diagrama.excalidraw]]`
