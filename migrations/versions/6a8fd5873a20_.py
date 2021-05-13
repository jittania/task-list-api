"""empty message

Revision ID: 6a8fd5873a20
Revises: 01aa13e98a34
Create Date: 2021-05-12 21:30:55.370149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a8fd5873a20'
down_revision = '01aa13e98a34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.drop_constraint('task_matching_goal_id_fkey', 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    op.drop_column('task', 'matching_goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('matching_goal_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key('task_matching_goal_id_fkey', 'task', 'goal', ['matching_goal_id'], ['goal_id'])
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
