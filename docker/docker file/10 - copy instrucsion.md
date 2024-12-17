# copy
- copy => menambahkan file dari source ke dalam folder destination di docker image
  - copy 
    - hanya melakukan copy file saja
  - add
    - selain melakukan copy add bisa mendowoald file dari url
    - dan secara otomatis melakukan extract file kompress
  - namun best practice sebisa mungkin menggunakan perintah copy saja
    - jika memang butuh extract kita bisa gunakan perintah
    - RUN dan jalankan aplikasi untuk extract

## copy
```bash
COPY world.txt hello
COPY hello/* hello
```