"""V1_Migration

Revision ID: 3adcea6baeb2
Revises: 
Create Date: 2025-03-18 15:23:05.852527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3adcea6baeb2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('plan', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('generations',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('content_type', sa.String(), nullable=True),
    sa.Column('content_context', sa.String(), nullable=True),
    sa.Column('user_context', sa.String(), nullable=True),
    sa.Column('generated_content', sa.JSON(), nullable=True),
    sa.Column('tokens', sa.JSON(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_generations_content_type'), 'generations', ['content_type'], unique=False)
    op.create_index(op.f('ix_generations_id'), 'generations', ['id'], unique=False)
    op.create_index(op.f('ix_generations_time_created'), 'generations', ['time_created'], unique=False)
    op.create_index(op.f('ix_generations_time_updated'), 'generations', ['time_updated'], unique=False)
    op.create_index(op.f('ix_generations_user_id'), 'generations', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_generations_user_id'), table_name='generations')
    op.drop_index(op.f('ix_generations_time_updated'), table_name='generations')
    op.drop_index(op.f('ix_generations_time_created'), table_name='generations')
    op.drop_index(op.f('ix_generations_id'), table_name='generations')
    op.drop_index(op.f('ix_generations_content_type'), table_name='generations')
    op.drop_table('generations')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
