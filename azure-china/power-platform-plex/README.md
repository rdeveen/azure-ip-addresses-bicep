# PowerPlatformPlex Bicep Module

Azure service tag: **PowerPlatformPlex**

## Overview

This directory contains Bicep variable files for the **PowerPlatformPlex** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **PowerPlatformPlex.bicep** - Global/cloud-wide IP address ranges
- **region/PowerPlatformPlex_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global PowerPlatformPlex module to access all IP ranges for this service tag:

```bicep
import * as powerplatformplex from './PowerPlatformPlex.bicep'

// Use the variable in your template
var allowedIPs = powerplatformplex.PowerPlatformPlex
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as powerplatformplexEastUS from './region/PowerPlatformPlex_EastUS.bicep'

// Use the regional variable
var eastUSIPs = powerplatformplexEastUS.PowerPlatformPlex_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `ChinaEast2`
- `ChinaEast3`
- `ChinaNorth2`
- `ChinaNorth3`

Total regional variants: 4


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: PowerPlatformPlex
- **Module Directory**: power-platform-plex
