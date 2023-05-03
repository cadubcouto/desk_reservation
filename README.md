# desk_reservation
Backend da applicação Desk Reservation

Este é um MVP para conclusão da sprint 1 do curso de pós graduação em engenharia de software pela PUC-Rio.

Desk Reservation é uma aplicação que permite o colaborador realizar a reserva de uma mesa de trabalho e/ou uma vaga de estacionamento.


1. Criar venv
python -m venv venv

2. Intalar pacotes
pip install -r requirements.txt

3. Configurar acesso ao Banco de Dados Postgres
Atualizar as credenciais no arquivo .env
DATABASE_IP_APP="localhost"
USER_DATABASE_APP="desk"
POSTGRES="postgresql+psycopg2://desk:@localhost/desk"

4. Criar os tabelas no bando de dados
python models.py

5. Iniciar aplicação
python main.py


