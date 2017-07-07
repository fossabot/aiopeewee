import pytest
import asyncio

from models import *

# @pytest.fixture
# async def loop(event_loop):
#     return event_loop


@pytest.yield_fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.yield_fixture(scope='session')
async def database():
    try:
        await db.connect()
        yield db
        #await db.create_tables(tables, safe=True)
        #yield tables
    finally:
        #await db.drop_tables(tables, safe=True)
        await db.close()


@pytest.yield_fixture
async def flushdb(database):
    tables = [User, Blog, BlogTwo, Comment, EmptyModel, NoPKModel,
              Category, UserCategory, UniqueMultiField,
              NonIntModel, Note, Flag, NoteFlagNullable, OrderedModel,
              Parent, Orphan, Child, GCModel, DefaultsModel]
    try:
        await db.create_tables(tables, safe=True)
        yield tables
    finally:
        await db.drop_tables(tables)
    # for table in reversed(tables):
    #     await table.delete()
    # return True
