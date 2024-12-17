# user instruction
- user => intruksi yang digunakan untuk mengubah user atau group ketika Docker image dijalankan
  - secara default docker akan menggunakan user root, namun pada bbrp kasus
  - mungkin ada aplikasi yang tidak ingin dijalankan dalam user root
  - maka kita bisa mengubah user menggunakan intruksi USER

## user
```bash
USER <user> #mengubah user
USER <user>:<group> #mengubah user dan user group
```

## contoh
```bash
RUN addgroup -S harbas
RUN adduser -SDh /app ariafatah harbas
RUN chown -R ariafatah:harbas /app
USER ariafatah
```