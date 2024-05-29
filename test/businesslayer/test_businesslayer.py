import common.backends
from datalayer.dataaccess_sqlite import DataAccessSqlite
from datalayer.dataaccess_pandas import DataAccessPandas
from datalayer.dataaccess_rest import DataAccessRest
from businesslayer.businesslayer import BusinessLayer


def test_business_layer():
    b1 = BusinessLayer(data_access_type=common.backends.DATA_ACCESS_TYPE_SQLITE)
    assert type(b1.data_access) is DataAccessSqlite

    b2 = BusinessLayer(data_access_type=common.backends.DATA_ACCESS_TYPE_PANDAS)
    assert type(b2.data_access) is DataAccessPandas

    b3 = BusinessLayer(data_access_type=common.backends.DATA_ACCESS_TYPE_REST)
    assert type(b3.data_access) is DataAccessRest

    b4 = BusinessLayer(data_access_type="unknown")
    assert b4.data_access is None
