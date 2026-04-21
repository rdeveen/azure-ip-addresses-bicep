# EventHub Bicep Module

Azure service tag: **EventHub**

## Overview

This directory contains Bicep variable files for the **EventHub** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **EventHub.bicep** - Global/cloud-wide IP address ranges
- **region/EventHub_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global EventHub module to access all IP ranges for this service tag:

```bicep
import * as eventhub from './EventHub.bicep'

// Use the variable in your template
var allowedIPs = eventhub.EventHub
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as eventhubEastUS from './region/EventHub_EastUS.bicep'

// Use the regional variable
var eastUSIPs = eventhubEastUS.EventHub_EastUS
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
- **Service Tag**: EventHub
- **Module Directory**: event-hub
