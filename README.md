# monitoramento_sla_service_level_agreement with python
Este projeto tem como objetivo automatizar o monitoramento de indicadores de SLA (Service Level Agreement), facilitando a análise de desempenho mensal e a comunicação com as partes interessadas por meio de envio automático de relatórios por e-mail.

# 📈 Monitoramento de Indicadores de SLA com Python

Este projeto tem como objetivo automatizar o monitoramento de indicadores de SLA (Service Level Agreement), facilitando a análise de desempenho mensal e a comunicação com as partes interessadas por meio de envio automático de relatórios por e-mail.

## 🔧 Funcionalidades

- Leitura e estruturação de dados de SLAs em um DataFrame.
- Identificação automática dos SLAs que não atingiram a meta no mês analisado.
- Cálculo da diferença percentual e projeção do acumulado necessário para o próximo mês.
- Geração de relatório textual com status de cada SLA (cumprido ou fora da meta).
- Envio automático do relatório por e-mail com os dados detalhados.

## 📬 Tecnologias Utilizadas

- Python 3
- Pandas
- smtplib
- email.mime

## 📌 Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

Instale as dependências (se necessário):
Shellpip install pandasShow more lines


Atualize os seguintes campos no script:

remetente: seu e-mail.
destinatario: e-mail do destinatário.
senha: sua senha ou token de aplicativo.
SMTP_SERVER: servidor SMTP do seu provedor de e-mail.
assunto: título do e-mail.
NOME DA EMPRESA: nome da empresa no corpo do e-mail.

Execute o script:
Shellpython sla_monitor.pyShow more lines

💡 Motivação
Este projeto foi inspirado em uma necessidade real de monitorar os SLAs de atendimento de uma grande empresa, com foco em garantir a qualidade dos serviços prestados e facilitar a tomada de decisão por parte da gestão.
📄 Exemplo de Saída
📊 Acumulado para o próximo mês dos SLAs fora da meta:
4 - Atualização das informações de cobrança após 30d do chamado: Julho: 99.61%, Faltou: 0.39%, Meta Agosto: 100.0%, Acumulado Agosto (simulado): 100.39%

📫 Contato
Rafael Rocha Gorgonio
LinkedIn:www.linkedin.com/in/rafael-gorgonio | Email: rafaelrgorgonio@gmail.com

Sinta-se à vontade para contribuir ou sugerir melhorias!
