# 🚀 Guia de Deploy na AWS EC2 (AWS Academy)

Este guia documenta o processo de hospedagem e publicação de uma aplicação web estática (HTML, CSS, JavaScript e Tailwind CSS) em uma instância EC2 da AWS.

---

## 🛠️ Tecnologias Utilizadas
* **AWS EC2** (Ubuntu Server 22.04 LTS)
* **Nginx** (Servidor Web Reverse Proxy)
* **Git & GitHub** (Controle de versão e código-fonte)

---

## 📋 Passo a Passo de Configuração Inicial

### 1. Configuração do Security Group na AWS
Certifique-se de que o Security Group da sua instância possui as seguintes regras de entrada (Inbound Rules):
* **SSH (Porta 22):** Para acesso remoto via terminal (`0.0.0.0/0`).
* **HTTP (Porta 80):** Para acesso ao site via navegador (`0.0.0.0/0`).

---

### 2. Acesso Remoto via PowerShell (Windows)

1. Abra o PowerShell na pasta onde está o arquivo de chave privada (`.pem`):
   ```powershell
   cd ~\Downloads
   ```

2. Configure as permissões de acesso da chave:
   ```powershell
   icacls 2ADS2026.pem /inheritance:r
   icacls 2ADS2026.pem /grant:r "SeuUsuario:R"
   ```

3. Conecte-se ao servidor Ubuntu:
   ```powershell
   ssh -i 2ADS2026.pem ubuntu@IP_PUBLICO_DA_EC2
   ```

---

### 3. Instalação e Deploy no Servidor

1. **Atualizar os pacotes do sistema e instalar o Nginx e Git:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install nginx git -y
   ```

2. **Clonar o repositório do GitHub:**
   ```bash
   git clone [https://github.com/Leonardo-gabsantos/tailwind-project.git](https://github.com/Leonardo-gabsantos/tailwind-project.git)
   ```

3. **Mover os arquivos para a pasta padrão do Nginx:**
   ```bash
   sudo rm -rf /var/www/html/*
   sudo cp -r tailwind-project/* /var/www/html/
   ```

4. **Reiniciar o serviço do Nginx:**
   ```bash
   sudo systemctl restart nginx
   ```

5. **Acessar a aplicação:**
   Abra o navegador e acesse: `http://IP_PUBLICO_DA_EC2`

---

## 🔄 Rotina para Próximos Acessos (AWS Academy)

Como o **AWS Academy** altera o IP público a cada nova sessão de laboratório:

1. **Ligar o Lab:** Clique em **Start Lab** e inicie a instância no painel do EC2.
2. **Obter o Novo IP:** Copie o novo **Endereço IPv4 público** gerado pela AWS.
3. **Acessar:** Digite `http://NOVO_IP_PUBLICO` no navegador. *(O Nginx e o site iniciam automaticamente).*

---

## ⚡ Como Atualizar o Site Após Modificações no Código

Quando fizer alterações e enviar para o GitHub (`git push`), execute estes comandos na EC2:

```bash
cd ~/tailwind-project
git pull
sudo cp -r * /var/www/html/
```
