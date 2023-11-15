/* (Beta) Export of data model OperationalPoint of the subject dataModel.ERA for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE OperationalPoint_type AS ENUM ('OperationalPoint');
CREATE TABLE OperationalPoint (address JSON, alternateName TEXT, areaServed TEXT, borderPointOf TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, digitalSchematicOverview TEXT, hasSchematicOverviewOPDigitalForm BOOLEAN, id TEXT PRIMARY KEY, localRulesOrRestrictions BOOLEAN, localRulesOrRestrictionsDoc TEXT, location JSON, name TEXT, opInfoPerCountry TEXT, opName TEXT, opType TEXT, opTypeGaugeChangeover TEXT, owner JSON, schematicOverviewOP TEXT, seeAlso JSON, siding TEXT, source TEXT, tafTAPCode TEXT, track TEXT, type OperationalPoint_type, uopid TEXT);