# MicrosoftAzureFluidRelay Bicep Module

Azure service tag: **MicrosoftAzureFluidRelay**

## Overview

This directory contains Bicep variable files for the **MicrosoftAzureFluidRelay** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **MicrosoftAzureFluidRelay.bicep** - Global/cloud-wide IP address ranges
- **region/MicrosoftAzureFluidRelay_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global MicrosoftAzureFluidRelay module to access all IP ranges for this service tag:

```bicep
import * as microsoftazurefluidrelay from './MicrosoftAzureFluidRelay.bicep'

// Use the variable in your template
var allowedIPs = microsoftazurefluidrelay.MicrosoftAzureFluidRelay
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as microsoftazurefluidrelayEastUS from './region/MicrosoftAzureFluidRelay_EastUS.bicep'

// Use the regional variable
var eastUSIPs = microsoftazurefluidrelayEastUS.MicrosoftAzureFluidRelay_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: MicrosoftAzureFluidRelay
- **Module Directory**: microsoft-azure-fluid-relay
