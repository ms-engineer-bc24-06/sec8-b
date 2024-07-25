from sqlalchemy.orm import Session # sqlalchemy.ormのsessionクラス: DB操作用
from app.models import ConversationHistory

# 会話を保存する
def save_conversation_history(db: Session, user_id: str, user_message: str, bot_response: str):
    print(f"🈴 保存するusr_id: {user_id}")
    print(f"🈴 保存するusr_message:{user_message}")
    print(f"🈴 保存するbot_response: {bot_response}")
    conversation = ConversationHistory(
        user_id=user_id, 
        user_message=user_message,
        bot_response=bot_response
    )
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation

# user_idで特定のユーザーの会話履歴のみを取得する（LLMに渡す用)
def get_conversation_history(db: Session, user_id: str):
    return db.query(ConversationHistory).filter(ConversationHistory.user_id == user_id).all()

# NOTE: 関数の解説
    # 関数save_conversation_history
        # 引数 db= sessionのインスタンス
        # 引数 user_idとmessageはLINEユーザーとメッセージのこと

    # line5
        # models.pyで定義したConversationHistoryモデルの新しいインスタンスを作成し、user_idカラムには引数のuser_id、messageカラムには引数のmessageを入れる
        # ConversationHistoryモデル =  会話履歴を保存していくテーブルを定義してる @models.py

    # line6
        # 一つ前で作成した db_conversation をデータベースセッションに追加する

    # line7
        # 新しいbd_conversationを追加した データベースセッションをコミットすることで
        # セッションにあったすべての変更内容がデータベースに保存される

    # line8、９
        # db_conversationオブジェクトをデータベースから再取得し、最新情報も保存された会話履歴を返す
        # つまりこの関数を呼び出した場所では保存された全ての会話履歴を取得できる