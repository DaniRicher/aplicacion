"""Create place table

Revision ID: 919b4daf5d8b
Revises: 
Create Date: 2021-12-09 11:42:42.474649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919b4daf5d8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('places',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_places_description'), 'places', ['description'], unique=False)
    op.create_index(op.f('ix_places_id'), 'places', ['id'], unique=False)
    op.create_index(op.f('ix_places_name'), 'places', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_places_name'), table_name='places')
    op.drop_index(op.f('ix_places_id'), table_name='places')
    op.drop_index(op.f('ix_places_description'), table_name='places')
    op.drop_table('places')
    # ### end Alembic commands ###
