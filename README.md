## Créditos

Este bot funciona gracias a la API desarrollada por [hotheadhacker](https://github.com/hotheadhacker/no-as-a-service). Todo el crédito por la lógica de las respuestas generadas va para su excelente trabajo.

## Bot
Para usar este bot primero hay que tener el contenedor de Libre Translate, lo puedes ejecutar con:

```bash
sudo chmod +x install.sh
./install.sh
```

Despues debemos crear un bot con el BotFather y obtener el token de este. 
Luego de obtener el token del bot y exportarlo en la terminal con el comando:


```bash
export TELEGRAM_TOKEN="TU_TOKEN_DEL_BOT"

```
Despues debemos obtener el token de tu chat de telegram que se hace con el código llamado bot.py, para
que no de error debemos haber exportado el token del bot con el comando anterior y este nos arrojara el id de 
nuestro chat. Si no te aparece nada o te da error, envia un mensaje a tu bot y espera unos 5 segundos y vuelve
a intentarlo. Cuando obtengas el codigo debemos exportarlo con el comando:


```bash
export TELEGRAM_CHAT_ID="TU_CHAT_ID"


```
Una vez con esto podemos ejecutarlo con 

```bash
python No_Mejorado.py 
```

Una vez corriendo debemos inicalizarlo con `/start` y nos dara la bienvenida y para solicitar una respuesta utilizamos `/check` o `/no`
