# mempersiapkan linux server
- seperti yang kita bahas dalam praktik kali ini server yang ingin coba automisasi adalah berbasis linux
- oleh karena itu kita perlu mempersiapkan beberapa hal terlebih dahulu sebelum kita dapat menggunakan ansbile seperti
  - pastikan server dapat di remote menggunakan SSH, biasanya menggunakan port 22
  - pastikan sudah ada python di server

## generate ssh key 
- saat kita meremote linux melalui ssh, biasanya ada 2 style autentikasi yang sering digunakan, yaitu menggunakan password atau sshkey
- untuk autentikasi menggunakan password penulis rasa sudah tidak asing lagi
  - karena umum dilakukan
- untuk melakukan autentikasi menggunakan ssh key kita perlu membuat key terlebih dahulu 
  - untuk membuatnya gunakan perintah ```ssh-keygetn -t rsa -f <lokasi>/namakey```
- saat menjalankan perintah di atas, akan diminta memasukan passpharse, itu bisa dikosongkan saja
  - nantinya akan terbuat 2 file yaitu private key (tanpa extensi) dan public key (extensi .pub)

## generate
```bash
ssh-keygen -t rsa -f ./belajar/id_rsa
```

## mendaftar ssh key
- agar ssh key yang sebelumnya kita buat dapat digunakan untuk autentikasi ssh
  - kita perlu mencopynya dari *.pub ke ~/.ssh/authorized_keys di server 

```bash
ssh-copy-id -f -i <file.pub> -p <port> <user>@<host>
# untuk mengecek
cat ~/.ssh/authorized_keys
```

## login dengan ssh-key
- setelah public key tercopy di server
  - kita dapat login ke server tanpa kita memasukan password
- sebagai penggantinya kita dapat menggunakan private key saat login ssh
- praktek login ssh menggunakan key ini sangat disarankan

```bash
ssh -i <private_key> -p <port> <user>@<host>
``` 

## memberikan akses sudoers
- selanjutnya kita akan mengizinkan user yang kita miliki untuk menggunakan sudo tanpa password
  - hal ini bertujuan agar nantinya dalam praktik menggunakan ansible jadi lebih mudah
- NOTE: mengizinkan user untuk menggunakan password sudo di semua command tanpa password tidak bagus
  - hanya gunakan untuk DMEO materi ini saja

```bash
sudo su
usermod -aG sudo <nama_user>
echo "<nama_user> ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/<nama_user>
```