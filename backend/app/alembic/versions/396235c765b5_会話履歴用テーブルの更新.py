"""会話履歴用テーブルの更新

Revision ID: 396235c765b5
Revises: 443c0714645a
Create Date: 2024-07-24 20:18:16.625858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '396235c765b5'
down_revision: Union[str, None] = '443c0714645a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('conversation_history', 'user_message',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('conversation_history', 'bot_response',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('conversation_history', 'timestamp',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('conversation_history', 'timestamp',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('conversation_history', 'bot_response',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('conversation_history', 'user_message',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
