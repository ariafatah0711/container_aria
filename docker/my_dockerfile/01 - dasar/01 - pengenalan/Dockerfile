FROM alpine:3

LABEL author="ariafatah"
LABEL compnay="smk harapan bangsa" website="https://s.id/arialink"
LABEL name="app1"

# build containe
RUN mkdir data_siswa
COPY add/* data_siswa/

# COPY data.tar.gz data_siswa/
# RUN tar xvz -f data_siswa/data.tar.gz -C data_siswa/

RUN ls data_siswa

# RUN container
# CMD cat "data_siswa/data-siswa.txt" & cat "data_siswa/umur-siswa.txt"
CMD ls data_siswa