/* (Beta) Export of data model ETCSLevel of the subject dataModel.ERA for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ETCSLevel_type AS ENUM ('ETCSLevel');
CREATE TABLE ETCSLevel (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, etcsBaseline TEXT, etcsLevelType TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type ETCSLevel_type);