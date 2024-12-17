# yaml
- yaml => sebuah jenis file yang biasa digunakan untuk menyimpan konfigurasi
  - yaml mirip seprti json, hanya saja tidak menggunakan huruf kurang kurawal
  - yaml akan memiliki attribute dan value

## contoh yaml
```yaml
# yaml
firstName: aria; # titik kona tidak wajib
middleName: "fatah" # bisa string
lastName: anom
hobbies: # array
    - coding
    - reading
    - anime
    - gaming
address: # nested object
    Street: Gg bakti
    city: Depok
    country: Indonesia
wellet: # array nested object
    - type: cash
      mount: 100000
    - type: debit
      mount: 530000
```

## contoh json
```json
{
    "firstName": "aria",
    "middleName": "fatah",
    "lastName": "anom",
    "hobbies": [ // array
        "coding",
        "reading",
        "anime",
        "gaming"
    ],
    "Address": { // nested object
        "Street": "Gg bakti",
        "city": "Depok",
        "country": "Indonesia"
    },
    "wallet": [ // array nested object
        {
            "type": "cash",
            "mount": 100000
        },
        {
            "type": "debit"
            "mount": 530000
        }
    ]
}
```