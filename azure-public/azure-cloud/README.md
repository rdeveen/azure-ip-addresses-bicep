# AzureCloud Bicep Module

Azure service tag: **AzureCloud**

## Overview

This directory contains Bicep variable files for the **AzureCloud** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureCloud.bicep** - Global/cloud-wide IP address ranges
- **region/AzureCloud_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureCloud module to access all IP ranges for this service tag:

```bicep
import * as azurecloud from './AzureCloud.bicep'

// Use the variable in your template
var allowedIPs = azurecloud.AzureCloud
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurecloudEastUS from './region/AzureCloud_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurecloudEastUS.AzureCloud_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `australiacentral`
- `australiacentral2`
- `australiaeast`
- `australiasoutheast`
- `austriaeast`
- `belgiumcentral`
- `brazilne`
- `brazilse`
- `brazilsouth`
- `canadacentral`
- `canadaeast`
- `centralfrance`
- `centralindia`
- `centralus`
- `centraluseuap`
- `chilec`
- `denmarkeast`
- `eastasia`
- `eastus`
- `eastus2`
- `eastus2euap`
- `eastus3`
- `germanyn`
- `germanywc`
- `indonesiacentral`
- `israelcentral`
- `israelnorthwest`
- `italynorth`
- `japaneast`
- `japanwest`
- `jioindiacentral`
- `jioindiawest`
- `koreacentral`
- `koreasouth`
- `malaysiasouth`
- `malaysiawest`
- `mexicocentral`
- `newzealandnorth`
- `northcentralus`
- `northeurope`
- `northeurope2`
- `norwaye`
- `norwayw`
- `polandcentral`
- `qatarcentral`
- `southafricanorth`
- `southafricawest`
- `southcentralus`
- `southcentralus2`
- `southeastasia`
- `southeastus`
- `southeastus3`
- `southfrance`
- `southindia`
- `spaincentral`
- `swedencentral`
- `swedensouth`
- `switzerlandn`
- `switzerlandw`
- `taiwannorth`
- `taiwannorthwest`
- `uaecentral`
- `uaenorth`
- `uksouth`
- `ukwest`
- `usstagec`
- `usstagee`
- `westcentralus`
- `westeurope`
- `westindia`
- `westus`
- `westus2`
- `westus3`

Total regional variants: 73


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureCloud
- **Module Directory**: azure-cloud
