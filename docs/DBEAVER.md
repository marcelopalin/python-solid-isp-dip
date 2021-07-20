# INSTALL VISUALIZADOR DE BANCO DE DADOS

```
sudo apt -y  install openjdk-11-jdk openjdk-11-jre
```

```s
wget -O - https://dbeaver.io/debs/dbeaver.gpg.key | sudo apt-key add -
echo "deb https://dbeaver.io/debs/dbeaver-ce /" | sudo tee /etc/apt/sources.list.d/dbeaver.list
```

```s
sudo apt install dbeaver-ce
```
