/* (Beta) Export of data model SpecialArea of the subject dataModel.ERA for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SpecialArea_type AS ENUM ('SpecialArea');
CREATE TABLE SpecialArea (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, specialAreaType TEXT, type SpecialArea_type);