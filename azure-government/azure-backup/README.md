# AzureBackup Bicep Module

Azure service tag: **AzureBackup**

## Overview

This directory contains Bicep variable files for the **AzureBackup** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureBackup.bicep** - Global/cloud-wide IP address ranges
- **region/AzureBackup_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureBackup module to access all IP ranges for this service tag:

```bicep
import * as azurebackup from './AzureBackup.bicep'

// Use the variable in your template
var allowedIPs = azurebackup.AzureBackup
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurebackupEastUS from './region/AzureBackup_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurebackupEastUS.AzureBackup_EastUS
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
- **Service Tag**: AzureBackup
- **Module Directory**: azure-backup
