from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from datetime import datetime, timezone
import os
from sqlalchemy.orm import sessionmaker
from app.models import ConversationHistory

# 環境変数からデータベースのURLを取得
DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# データベースエンジンの作成
engine = create_engine(DATABASE_URL)

# データベースセッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データの挿入
def create_test_data():
    session = SessionLocal()
    timestamp = datetime.now(timezone.utc)
    try:
        for i in range(10):
            new_conversation = ConversationHistory(
                user_id=f"haruka_ku-min_meme",
                timestamp=timestamp,
                user_message=f"会話履歴の取得はできますか",
                bot_response=f"会話履歴の取得はできますよ"
            )
            session.add(new_conversation)
        session.commit()
        print("データの挿入が完了しました。")
    except Exception as e:
        session.rollback()
        print(f"エラーが発生しました: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    create_test_data()
