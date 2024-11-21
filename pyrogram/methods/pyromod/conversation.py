import pyrogram
from typing import Union
from dataclasses import dataclass

@dataclass
class conversationData:
    user_id: int
    chat_id: int

class Check_Conversation:
    async def check_conversation(
        self: "pyrogram.Client",
        message : "pyrogram.types.Message",
    ):
        return Conversation.check(message)
    
class Add_Conversation:
    async def add_conversation(
        self: "pyrogram.Client",
        message: 'pyrogram.types.Message'
    ):
        return Conversation.add(self, message)
    
class Conversation:
    _data = []

    def exsit(cls,user_id,chat_id):
        return True if any(item["user_id"] == user_id and item["chat_id"] == chat_id for item in cls._data) else False

    @classmethod
    def add(cls, message: pyrogram.types.Message):
        cls._data.append({"user_id": message.from_user.id, "chat_id": message.chat.id})

    @classmethod
    def check(cls,message: pyrogram.types.Message) -> conversationData:
        return any(item["user_id"] == message.from_user.id and item["chat_id"] == message.chat.id for item in cls._data)

    @classmethod
    def clear(cls):
        cls._data.clear()

