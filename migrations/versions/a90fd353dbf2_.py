"""empty message

Revision ID: a90fd353dbf2
Revises: 
Create Date: 2021-03-12 15:47:24.741475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a90fd353dbf2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('map_points',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pointX', sa.Float(), nullable=True),
    sa.Column('pointY', sa.Float(), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_map_points_name'), 'map_points', ['name'], unique=True)
    op.create_index(op.f('ix_map_points_pointX'), 'map_points', ['pointX'], unique=True)
    op.create_index(op.f('ix_map_points_pointY'), 'map_points', ['pointY'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_map_points_pointY'), table_name='map_points')
    op.drop_index(op.f('ix_map_points_pointX'), table_name='map_points')
    op.drop_index(op.f('ix_map_points_name'), table_name='map_points')
    op.drop_table('map_points')
    # ### end Alembic commands ###
