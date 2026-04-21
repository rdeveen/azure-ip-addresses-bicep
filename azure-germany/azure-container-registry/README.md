# AzureContainerRegistry Bicep Module

Azure service tag: **AzureContainerRegistry**

## Overview

This directory contains Bicep variable files for the **AzureContainerRegistry** service tag in the **Azure Germany Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureContainerRegistry.bicep** - Global/cloud-wide IP address ranges
- **region/AzureContainerRegistry_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureContainerRegistry module to access all IP ranges for this service tag:

```bicep
import * as azurecontainerregistry from './AzureContainerRegistry.bicep'

// Use the variable in your template
var allowedIPs = azurecontainerregistry.AzureContainerRegistry
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurecontainerregistryEastUS from './region/AzureContainerRegistry_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurecontainerregistryEastUS.AzureContainerRegistry_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `GermanyCentral`
- `GermanyNorthEast`

Total regional variants: 2


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Germany Cloud
- **Service Tag**: AzureContainerRegistry
- **Module Directory**: azure-container-registry
