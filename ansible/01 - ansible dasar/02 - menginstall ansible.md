# menginstall ansible
- ansible berjalan di atas pemograman python
  - karena python bisa di jalankan di banyak system operasi (linux, mac, window)
- khusus untuk yang install ansible di windows
  - ansible menyarankan untuk menggunakan WSL
  - karena memang direkomendasikan menggunakan UNIX-system saat menjalankan ansible
- jadi pastikan kita sudah menginstall python
  - berdasarkan dokumentasi ansible saat ini, versi python yang disarankan adalah minimal versi 3.9
- cara menginstallnya cukup ikuti dokumentasi [disini](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-and-upgrading-ansible)
- setelah berhasil menginstall ansible, kita dapat mengeceknya dengan perintah ```ansible --version```

## install in wsl
```bash
sudo apt install pipx
pipx install --include-deps ansible
## or
pipx install ansible-core
```

## after install
- setelah berhasil menginstall ansible, biasanya secara default akan ada beberapa command yang di install juga seperti 
  ```ansible-inventory``` atau ```ansible-playbook``` 
- yang dimana beberapa command tersebut akan kita gunakan dan bahas di materi selanjutnya