# AzureCosmosDB Bicep Module

Azure service tag: **AzureCosmosDB**

## Overview

This directory contains Bicep variable files for the **AzureCosmosDB** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureCosmosDB.bicep** - Global/cloud-wide IP address ranges
- **region/AzureCosmosDB_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureCosmosDB module to access all IP ranges for this service tag:

```bicep
import * as azurecosmosdb from './AzureCosmosDB.bicep'

// Use the variable in your template
var allowedIPs = azurecosmosdb.AzureCosmosDB
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurecosmosdbEastUS from './region/AzureCosmosDB_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurecosmosdbEastUS.AzureCosmosDB_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `USDoDCentral`
- `USDoDEast`
- `USGovArizona`
- `USGovIowa`
- `USGovTexas`
- `USGovVirginia`

Total regional variants: 6


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureCosmosDB
- **Module Directory**: azure-cosmos-db
