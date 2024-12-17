# add instruction
- add instrucsion => intruksi yang dapat digunakan untuk menambahkan file dari source ke dalam folder destination di docker image
  - perintah ADD bisa mendeteksi apakah sebuah file source seperti tar.gz, gzip
    - maka secara otomatis file tersebut akan di extract ke di docker containernya ke dalam sebuah folder
  - perintah ADD juga bisa mendukung banyak penambahan file sekaligus
    - penambahana banyak file sekaligus di instruksi ADD menggunakan Pattern di GO-Lang :
      ```bash
      * => semua karakter
      ? singgle
      ```
   - bisas juga gunakan url dari luar nanti akan otomatis di add ke dalam folder di image

## add
```bash
ADD source destinatiom
```

## contoh
```bash
ADD world.txt hello # menambahkan file world.txt ke folder hello
ADD *.txt hello # maka semua file .txt ke folder hello
```