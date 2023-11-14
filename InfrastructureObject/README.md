[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
# InfrastructureObject
Version: 0.0.1

## Description 

This class encompasses all those classes that represent features that are  implemented in the European railway infrastructure. It is a subclass of the ERA Feature that has a spatial representation. It covers tracks, platforms, signals, tunnels, operational points, and sections of line.
A feature that belongs to the infrastructure can be abstracted (hasAbstraction) as a topological object. It also is related to the infrastructure manager through the property infrastructureMgr.

data model mapped from ERA ontology https://data-interop.era.europa.eu/era-vocabulary (European Union Agency for Railways)
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.ERA/InfrastructureObject/swagger.yaml)

Link to the [specification](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec.md)

Enlace a la [Especificación en español](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec_ES.md)

Lien vers le [spécification en français](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec_FR.md)

Link zur [deutschen Spezifikation](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec_DE.md)

Link alla [specifica](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec_IT.md)

[仕様へのリンク](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec_JA.md)

[链接到规范](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec_ZH.md)

[사양 링크](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/doc/spec_KO.md)
### Examples

Link to the [example](https://smart-data-models.github.io/dataModel.ERA/InfrastructureObject/examples/example.json) (keyvalues) for NGSI v2

Link to the [example](https://smart-data-models.github.io/dataModel.ERA/InfrastructureObject/examples/example.jsonld) (keyvalues) for NGSI-LD

Link to the [example](https://smart-data-models.github.io/dataModel.ERA/InfrastructureObject/examples/example-normalized.json) (normalized) for NGSI-V2

Link to the [example](https://smart-data-models.github.io/dataModel.ERA/InfrastructureObject/examples/example-normalized.jsonld) (normalized) for NGSI-LD
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/InfrastructureObject/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/InfrastructureObject/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/geojson_features_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/InfrastructureObject/schema.json&email=info@smartdatamodels.org) of geojson feature format payloads compliant with this data model. Refresh for new values
### PostgreSQL schema
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.ERA/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.ERA/pulls)

 If you wish to develop your own data model you can start from [contribution manual](https://bit.ly/contribution_manual). Several services have been developed to help with: 
 - [Test data model repository](https://smartdatamodels.org/index.php/data-models-contribution-api/) including the schema and example payloads, etc
 - [Generate PostgreSQL schema](https://smartdatamodels.org/index.php/sql-service/) to help create a table, create type, etc