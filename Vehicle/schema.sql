/* (Beta) Export of data model Vehicle of the subject dataModel.ERA for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Vehicle_type AS ENUM ('Vehicle');
CREATE TABLE Vehicle (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "compositeBrakeBlockRetrofitted" BOOLEAN,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "manufacturingCountry" TEXT,
  "name" TEXT,
  "operationalRestriction" TEXT,
  "owner" JSON,
  "quieterRoutesExemptedCountry" TEXT,
  "seeAlso" JSON,
  "source" TEXT,
  "type" Vehicle_type,
  "vehicleKeeper" TEXT,
  "vehicleNumber" TEXT,
  "vehicleSeries" TEXT,
  "vehicleType" TEXT
);