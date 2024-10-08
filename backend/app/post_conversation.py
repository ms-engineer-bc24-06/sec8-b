import aiohttp
import logging

# ログ設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def post_conversation_history(conversation_data):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("http://localhost:8000/api/conversation/", json=conversation_data, timeout=10) as response:
                if response.status == 200:
                    logger.info("🙆会話履歴が正常に保存されました。")
                else:
                    logger.error(f"🙅会話履歴の保存に失敗しました: {response.status} - {await response.text()}")
    except Exception as e:
        logger.debug(f"❌ エラー発生: {e}")
