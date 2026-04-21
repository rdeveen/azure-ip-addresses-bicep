# ServiceBus Bicep Module

Azure service tag: **ServiceBus**

## Overview

This directory contains Bicep variable files for the **ServiceBus** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **ServiceBus.bicep** - Global/cloud-wide IP address ranges
- **region/ServiceBus_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global ServiceBus module to access all IP ranges for this service tag:

```bicep
import * as servicebus from './ServiceBus.bicep'

// Use the variable in your template
var allowedIPs = servicebus.ServiceBus
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as servicebusEastUS from './region/ServiceBus_EastUS.bicep'

// Use the regional variable
var eastUSIPs = servicebusEastUS.ServiceBus_EastUS
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
- **Service Tag**: ServiceBus
- **Module Directory**: service-bus
