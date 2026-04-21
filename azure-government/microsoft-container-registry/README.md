# MicrosoftContainerRegistry Bicep Module

Azure service tag: **MicrosoftContainerRegistry**

## Overview

This directory contains Bicep variable files for the **MicrosoftContainerRegistry** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **MicrosoftContainerRegistry.bicep** - Global/cloud-wide IP address ranges
- **region/MicrosoftContainerRegistry_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global MicrosoftContainerRegistry module to access all IP ranges for this service tag:

```bicep
import * as microsoftcontainerregistry from './MicrosoftContainerRegistry.bicep'

// Use the variable in your template
var allowedIPs = microsoftcontainerregistry.MicrosoftContainerRegistry
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as microsoftcontainerregistryEastUS from './region/MicrosoftContainerRegistry_EastUS.bicep'

// Use the regional variable
var eastUSIPs = microsoftcontainerregistryEastUS.MicrosoftContainerRegistry_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `USDoDCentral`
- `USDoDEast`
- `USGovArizona`
- `USGovTexas`
- `USGovVirginia`

Total regional variants: 5


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: MicrosoftContainerRegistry
- **Module Directory**: microsoft-container-registry
