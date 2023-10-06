
## Bases de datos

1. **Campaigns (Campañas)**: Esta tabla almacena información general sobre las campañas de envío de mensajes o correos electrónicos.

   - `id` (Clave primaria): Un identificador único para cada campaña.
   - `message`: El mensaje que se enviará en la campaña.
   - `message_variables`: La cantidad de variables en el mensaje.
   - `campaign_type`: El tipo de campaña (SMS o email).

2. **SMS_Campaign (Campaña de SMS)**: Esta tabla almacena los datos específicos de la campaña de SMS.

   - `id` (Clave primaria): Un identificador único para cada campaña de SMS.
   - `campaign_id` (Clave foránea): Una referencia a la campaña general a la que pertenece esta campaña de SMS.
   - `phone_number`: El número de teléfono al que se enviará el SMS.
   - `dni`: El número de identificación (DNI) de la cuenta a la que se enviará el SMS.
   - `message_variables_data`: Las variables específicas del mensaje de SMS.
   - `is_sent`: Un indicador que indica si el SMS fue enviado o no.

3. **Email_Campaign (Campaña de Email)**: Esta tabla almacena los datos específicos de la campaña de correo electrónico.

   - `id` (Clave primaria): Un identificador único para cada campaña de correo electrónico.
   - `campaign_id` (Clave foránea): Una referencia a la campaña general a la que pertenece esta campaña de correo electrónico.
   - `email_address`: La dirección de correo electrónico a la que se enviará el correo electrónico.
   - `dni`: El número de identificación (DNI) de la cuenta a la que se enviará el correo electrónico.
   - `message_variables_data`: Las variables específicas del mensaje de correo electrónico.
   - `is_sent`: Un indicador que indica si el correo electrónico fue enviado o no.