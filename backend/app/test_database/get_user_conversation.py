import aiohttp
from app.logging_config import logger

# async def get_conversation_history(conversation_data, user_id):
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get("http://localhost:8000/api/conversation/{user_id}", params=conversation_data, timeout=10) as response:
#                 if response.status == 200:
#                     logger.info("🙆会話履歴が正常に取得されました。")
#                     data = await response.json()
#                     return data
#                 else:
#                     logger.error(f"🙅会話履歴の取得に失敗しました: {response.status} - {await response.text()}")
#     except Exception as e:
#         logger.error(f"❌ エラー発生: {e}")


import asyncio
import aiohttp
from app.logging_config import logger

async def get_conversation_history(user_id):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://localhost:8000/api/conversation/{user_id}", timeout=10) as response:
                if response.status == 200:
                    logger.info("🙆会話履歴が正常に取得されました。")
                    data = await response.json()
                    return data
                else:
                    logger.error(f"🙅会話履歴の取得に失敗しました: {response.status} - {await response.text()}")
    except Exception as e:
        logger.error(f"❌ エラー発生: {e}")

# LLM処理の関数に入れるには# 非同期関数を同期関数の中で呼び出す
loop = asyncio.get_event_loop()
# 既存のイベントループ内で非同期関数を実行
conversation_history = loop.run_until_complete(get_conversation_history("取得したいuser_idを入れる"))

# 使用例
async def main():
    # user_id を指定してデータを取得
    conversation_history = await get_conversation_history("haruka_ku-min_meme")
    print(conversation_history)

# asyncioのイベントループで関数を実行
if __name__ == "__main__":
    asyncio.run(main())
