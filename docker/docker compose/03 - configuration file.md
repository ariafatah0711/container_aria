## configuration
- docker compose menyimpan konfigurasinya dalam bentuk YAML
  - file YAML mirip JSON namun lebih sederhana (tidaka da {})
  - biasanya file konfigurasi disimpan dalam file bernama docker-compose.yaml
  - nama project secara default akan menggunakan nama folder lokasi docker-compose.yaml tersebut berada

## syntax
```bash
# create folder pengenalan, add file docker-compose.yaml

# docker-compose.yaml
version: "3.18" # versi konfigurasi konfigurasi yaml (ingat bukan versi docker nya)
```