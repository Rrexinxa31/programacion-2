import numpy as np
import matplotlib.pyplot as plt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Parámetros del oscilador nzpc ndfm styt hpln
m = 1.0  # masa (kg)
k = 10.0  # constante del resorte (N/m)
omega = np.sqrt(k / m)  # frecuencia angular

# Condiciones iniciales
A = 1.0  # amplitud (m)
phi = 0.0  # fase inicial (rad)

# Tiempo de simulación
t = np.linspace(0, 10, 1000)  # de 0 a 10 segundos

# Solución de la ecuación
x = A * np.cos(omega * t + phi)

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Posición $x(t)$', color='b')
plt.title('Movimiento de un Oscilador Armónico Simple')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()

# Guardar la gráfica
plt.savefig('oscillator.png')
plt.close()

# Configuración del correo
from_email = 'danielitorueda31@gmail.com'
to_email = 'rrexinxa31@gmail.com'
password = 'nzpc ndfm styt hpln'

# Crear el mensaje
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'Gráfica del Oscilador Armónico Simple'

# Cuerpo del correo
body = '''\
Hola,

Adjunto la gráfica del movimiento de un oscilador armónico simple.

La ecuación diferencial es:
d²x/dt² + (k/m)x = 0

Donde:
- m = masa (kg)
- k = constante del resorte (N/m)
- A = amplitud (m)
- φ = fase inicial (rad)

Saludos,
'''

msg.attach(MIMEText(body, 'plain'))

# Adjuntar la imagen
with open('oscillator.png', 'rb') as img:
    img_attachment = MIMEImage(img.read())
    msg.attach(img_attachment)

# Enviar el correo
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        print("Correo enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")