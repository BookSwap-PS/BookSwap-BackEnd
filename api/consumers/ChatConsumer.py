import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = parse_qs(self.scope['query_string'].decode('utf8')).get('username')[-1]
        print(f"[CONNECT] USERNAME: {self.username}")

        self.room_group_name = f'chat_{self.username}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print(f"[DISCONNECT] USERNAME: {self.username}, CODE: {close_code}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        from api.models import Chat, ChatMessages  # Importação movida para dentro da função
        from django.contrib.auth.models import User
        
        # Log para depurar os dados recebidos no WebSocket
        print(f"[RECEIVE] Raw Data: {text_data}")

        try:
            text_data_json = json.loads(text_data)
        except json.JSONDecodeError as e:
            print(f"[ERROR] JSON Decode Error: {e}")
            await self.send(text_data=json.dumps({
                'error': 'Invalid JSON payload.'
            }))
            return

        chat_id = text_data_json.get('chat')
        message = text_data_json.get('message')

        if not chat_id or not message:
            print("[ERROR] Missing 'chat' or 'message' in payload.")
            await self.send(text_data=json.dumps({
                'error': 'Both chat ID and message content are required.'
            }))
            return

        try:
            chat = await Chat.objects.aget(id=chat_id)
        except Chat.DoesNotExist:
            print(f"[ERROR] Chat with ID {chat_id} does not exist.")
            await self.send(text_data=json.dumps({
                'error': 'Chat not found.'
            }))
            return

        user = await User.objects.aget(username=self.username)

        novaMensagem = ChatMessages(
            chat=chat,
            quemEnviou=user,
            conteudo=message
        )
        await sync_to_async(novaMensagem.save)()

        # Log para depuração da mensagem salva
        print(f"[MESSAGE SAVED] Chat ID: {chat_id}, Sender: {self.username}, Content: {message}")

        # Envia a mensagem para todos os usuários do chat
        for usuario in await sync_to_async(list)(chat.usuarios.all()):
            payload = {
                'type': 'chat_message',
                'chatId': str(chat.id),
                'message': novaMensagem.conteudo,
                'time': novaMensagem.dataEnvio.strftime("%Y-%m-%d %H:%M:%S"),
                'sender_username': self.username,
            }

            # Log do payload antes de enviar
            print(f"[SEND PAYLOAD] To: {usuario.username}, Payload: {payload}")

            await self.channel_layer.group_send(
                f'chat_{usuario.username}', payload
            )

            # Adiciona o destinatário à lista de quem recebeu a mensagem
            if usuario != user:
                await sync_to_async(novaMensagem.quemRecebeu.add)(usuario)

    async def chat_message(self, event):
        chat_id = event['chatId']
        message = event['message']
        sender_username = event['sender_username']
        time = event['time']

        # Log para verificar o evento que será enviado para o cliente
        print(f"[FORWARD TO CLIENT] Chat ID: {chat_id}, Sender: {sender_username}, Message: {message}, Time: {time}")

        # Envia a mensagem para o cliente conectado
        await self.send(text_data=json.dumps({
            'chatId': chat_id,
            'message': message,
            'sender_username': sender_username,
            'time': time,
        }))
