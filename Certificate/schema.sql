/* (Beta) Export of data model Certificate of the subject dataModel.ERA for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Certificate_type AS ENUM ('Certificate');
CREATE TABLE Certificate (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, state TEXT, type Certificate_type);