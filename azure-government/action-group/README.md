# ActionGroup Bicep Module

Azure service tag: **ActionGroup**

## Overview

This directory contains Bicep variable files for the **ActionGroup** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **ActionGroup.bicep** - Global/cloud-wide IP address ranges
- **region/ActionGroup_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global ActionGroup module to access all IP ranges for this service tag:

```bicep
import * as actiongroup from './ActionGroup.bicep'

// Use the variable in your template
var allowedIPs = actiongroup.ActionGroup
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as actiongroupEastUS from './region/ActionGroup_EastUS.bicep'

// Use the regional variable
var eastUSIPs = actiongroupEastUS.ActionGroup_EastUS
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
- **Service Tag**: ActionGroup
- **Module Directory**: action-group
