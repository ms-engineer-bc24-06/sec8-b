from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ConversationHistory
import logging

# ロガーの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# データベースセッションの取得：データベースの操作を行うためのセッション
def get_db_session() -> Session:
    return SessionLocal()

# 会話履歴を取得する関数
def get_user_conversation_history(user_id: str):
    # データベースセッションを取得
    db = get_db_session()
    try:
        conversation_history = db.query(ConversationHistory).filter(ConversationHistory.user_id == user_id).all()
        logger.info(f"取得した会話履歴: {conversation_history}")
        return conversation_history
    except Exception as e:
        logger.error(f"会話履歴の取得中にエラーが発生しました: {e}")
        return []
    finally:
        db.close()

# サンプルの実行例
# if __name__ == "__main__":
#     user_id = "haruka_ku-min_meme"
#     conversation_history = get_user_conversation_history(user_id)
    
#     for history in conversation_history:
#         print(f"User Message: {history.user_message}, Bot Response: {history.bot_response}, Timestamp: {history.timestamp}")
