import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Dados extraídos manualmente da página 4 do PDF
sla_data = [
    {'SLA': 'SLA01', 'Descrição': 'Aquisição de produtos nacionais entregues em até 2 dias úteis', 'Meta (%)': 95.0, 'Julho (%)': 98.21},
    {'SLA': 'SLA02', 'Descrição': 'Aquisição de produtos importados entregues em até 10 dias úteis', 'Meta (%)': 95.0, 'Julho (%)': 96.97},
    {'SLA': 'SLA04', 'Descrição': 'Atualização das informações de cobrança após 30 dias do chamado', 'Meta (%)': 100.0, 'Julho (%)': 99.61},
    {'SLA': 'SLA05', 'Descrição': 'Recolhimento em até 1 dia útil do equipamento antigo', 'Meta (%)': 100.0, 'Julho (%)': 100.0},
    {'SLA': 'SLA07', 'Descrição': 'Disponibilizar equipamentos de reposição em até 4 horas úteis', 'Meta (%)': 95.0, 'Julho (%)': 100.0},
    {'SLA': 'SLA09', 'Descrição': 'Nota de satisfação (Instant Feedback)', 'Meta (%)': 8.0, 'Julho (%)': 9.38},
    {'SLA': 'SLA11', 'Descrição': 'Ativos registrados no sistema de gestão de ativos e financeiro', 'Meta (%)': 100.0, 'Julho (%)': 100.0}
]

# Criar DataFrame
df = pd.DataFrame(sla_data)

# Filtrar SLAs fora da meta
df_nao_cumpridos = df[df['Julho (%)'] < df['Meta (%)']]

# Calcular diferença e acumulado como soma da meta de agosto + diferença de julho
df_nao_cumpridos['Diferença (%)'] = df_nao_cumpridos['Meta (%)'] - df_nao_cumpridos['Julho (%)']
df_nao_cumpridos['Acumulado Agosto (%)'] = df_nao_cumpridos['Meta (%)'] + df_nao_cumpridos['Diferença (%)']

# Função para enviar email com os dados dos SLAs
def enviar_email_slas(df, df_nao_cumpridos):
    remetente = "SEU_EMAIL_AQUI"
    destinatario = "DESTINATARIO_AQUI"
    assunto = "ASSUNTO EMAIL_AQUI"
    senha = "SUA_SENHA_AQUI"

    mensagem = "Relatório de SLAs - NOME DA EMPRESA\n\n"
    for _, row in df.iterrows():
        status = '✅ Cumprido' if row['Julho (%)'] >= row['Meta (%)'] else '❌ Fora da Meta'
        mensagem += (
            f"{row['SLA']} - {row['Descrição']}\n"
            f"Meta: {row['Meta (%)']}%\n"
            f"Julho: {row['Julho (%)']}%\n"
            f"{status}\n\n"
        )

    # Adicionar acumulado para o próximo mês no corpo do e-mail
    if not df_nao_cumpridos.empty:
        mensagem += "📊 Acumulado para o próximo mês dos SLAs fora da meta:\n"
        for _, row in df_nao_cumpridos.iterrows():
            mensagem += (
                f"{row['SLA']} - {row['Descrição']}: "
                f"Julho: {row['Julho (%)']}%, Faltou: {row['Diferença (%)']:.2f}%, "
                f"Meta Agosto: {row['Meta (%)']}%, "
                f"Acumulado Agosto (simulado): {row['Acumulado Agosto (%)']:.2f}%\n"
            )

    email = MIMEMultipart()
    email["From"] = remetente
    email["To"] = destinatario
    email["Subject"] = assunto
    email.attach(MIMEText(mensagem, "plain"))

    try:
        servidor = smtplib.SMTP("SMTP_SERVER_AQUI", 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, email.as_string())
        servidor.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar email: {e}")

# Enviar email com os dados
enviar_email_slas(df, df_nao_cumpridos)

# Exibir acumulado para o próximo mês dos SLAs fora da meta
if not df_nao_cumpridos.empty:
    print("\n📊 Acumulado para o próximo mês dos SLAs fora da meta:")
    for _, row in df_nao_cumpridos.iterrows():
        print(
            f"{row['SLA']} - {row['Descrição']}: "
            f"Julho: {row['Julho (%)']}%, Faltou: {row['Diferença (%)']:.2f}%, "
            f"Meta Agosto: {row['Meta (%)']}%, "
            f"Acumulado Agosto (simulado): {row['Acumulado Agosto (%)']:.2f}%"
        )