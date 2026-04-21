# ServiceFabric Bicep Module

Azure service tag: **ServiceFabric**

## Overview

This directory contains Bicep variable files for the **ServiceFabric** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **ServiceFabric.bicep** - Global/cloud-wide IP address ranges
- **region/ServiceFabric_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global ServiceFabric module to access all IP ranges for this service tag:

```bicep
import * as servicefabric from './ServiceFabric.bicep'

// Use the variable in your template
var allowedIPs = servicefabric.ServiceFabric
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as servicefabricEastUS from './region/ServiceFabric_EastUS.bicep'

// Use the regional variable
var eastUSIPs = servicefabricEastUS.ServiceFabric_EastUS
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
- **Service Tag**: ServiceFabric
- **Module Directory**: service-fabric
