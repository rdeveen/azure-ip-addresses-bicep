# MicrosoftDefenderForEndpoint Bicep Module

Azure service tag: **MicrosoftDefenderForEndpoint**

## Overview

This directory contains Bicep variable files for the **MicrosoftDefenderForEndpoint** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **MicrosoftDefenderForEndpoint.bicep** - Global/cloud-wide IP address ranges
- **region/MicrosoftDefenderForEndpoint_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global MicrosoftDefenderForEndpoint module to access all IP ranges for this service tag:

```bicep
import * as microsoftdefenderforendpoint from './MicrosoftDefenderForEndpoint.bicep'

// Use the variable in your template
var allowedIPs = microsoftdefenderforendpoint.MicrosoftDefenderForEndpoint
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as microsoftdefenderforendpointEastUS from './region/MicrosoftDefenderForEndpoint_EastUS.bicep'

// Use the regional variable
var eastUSIPs = microsoftdefenderforendpointEastUS.MicrosoftDefenderForEndpoint_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: MicrosoftDefenderForEndpoint
- **Module Directory**: microsoft-defender-for-endpoint
