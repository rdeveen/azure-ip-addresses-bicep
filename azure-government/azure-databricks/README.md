# AzureDatabricks Bicep Module

Azure service tag: **AzureDatabricks**

## Overview

This directory contains Bicep variable files for the **AzureDatabricks** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureDatabricks.bicep** - Global/cloud-wide IP address ranges
- **region/AzureDatabricks_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureDatabricks module to access all IP ranges for this service tag:

```bicep
import * as azuredatabricks from './AzureDatabricks.bicep'

// Use the variable in your template
var allowedIPs = azuredatabricks.AzureDatabricks
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuredatabricksEastUS from './region/AzureDatabricks_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuredatabricksEastUS.AzureDatabricks_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureDatabricks
- **Module Directory**: azure-databricks
