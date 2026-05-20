"""Re-sube fuentes faltantes al cuaderno de Números Decimales y actualiza meta.json."""
import json, subprocess, sys, time
from pathlib import Path

META = Path(r"C:\Users\braya\OneDrive\Documentos\4 portafolio\Cursos\Aritmetica\Números Decimales\.meta.json")
meta = json.loads(META.read_text(encoding="utf-8"))

NB_ID = meta["nb_id"]
videos = meta["videos"]
source_map = meta.get("source_map", {})

def nlm(*args):
    r = subprocess.run(["notebooklm"] + list(args), capture_output=True, text=True, encoding="utf-8", errors="replace")
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"raw": r.stdout + r.stderr}

# Obtener fuentes actuales en el cuaderno
print("Obteniendo fuentes actuales del cuaderno...")
actual = nlm("source", "list", "--notebook", NB_ID, "--json")
existing_ids = set()
if isinstance(actual, list):
    existing_ids = {s.get("id","") for s in actual}
elif isinstance(actual, dict) and "sources" in actual:
    existing_ids = {s.get("id","") for s in actual["sources"]}
print(f"  Fuentes activas en cuaderno: {len(existing_ids)}")

# Eliminar del source_map los IDs que ya no existen
source_map_int = {int(k): v for k, v in source_map.items()}
valid = {k: v for k, v in source_map_int.items() if v in existing_ids}
invalid = {k: v for k, v in source_map_int.items() if v not in existing_ids}
print(f"  IDs válidos: {len(valid)} | IDs inválidos/perdidos: {len(invalid)}")

# Re-subir los videos con IDs perdidos
new_source_map = dict(valid)
for vid in videos:
    n = vid["num"]
    if n in valid:
        print(f"  ⏭️  Video {n} ya tiene fuente válida, saltando")
        continue
    print(f"  📤 Subiendo video {n}: {vid['title'][:50]}...")
    r = nlm("source", "add", vid["url"], "--notebook", NB_ID, "--json")
    if isinstance(r, dict) and r.get("id"):
        new_source_map[n] = r["id"]
        print(f"     ✅ {r['id'][:8]}...")
    elif isinstance(r, list) and len(r) > 0 and r[0].get("id"):
        new_source_map[n] = r[0]["id"]
        print(f"     ✅ {r[0]['id'][:8]}...")
    else:
        print(f"     ❌ Error: {str(r)[:100]}")
    time.sleep(1)

# Guardar meta actualizado
meta["source_map"] = {str(k): v for k, v in new_source_map.items()}
META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\n✅ meta.json actualizado con {len(new_source_map)} fuentes válidas")
