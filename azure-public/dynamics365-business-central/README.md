# Dynamics365BusinessCentral Bicep Module

Azure service tag: **Dynamics365BusinessCentral**

## Overview

This directory contains Bicep variable files for the **Dynamics365BusinessCentral** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **Dynamics365BusinessCentral.bicep** - Global/cloud-wide IP address ranges
- **region/Dynamics365BusinessCentral_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global Dynamics365BusinessCentral module to access all IP ranges for this service tag:

```bicep
import * as dynamics365businesscentral from './Dynamics365BusinessCentral.bicep'

// Use the variable in your template
var allowedIPs = dynamics365businesscentral.Dynamics365BusinessCentral
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as dynamics365businesscentralEastUS from './region/Dynamics365BusinessCentral_EastUS.bicep'

// Use the regional variable
var eastUSIPs = dynamics365businesscentralEastUS.Dynamics365BusinessCentral_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: Dynamics365BusinessCentral
- **Module Directory**: dynamics365-business-central
