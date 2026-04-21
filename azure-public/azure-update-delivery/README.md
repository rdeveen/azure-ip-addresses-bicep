# AzureUpdateDelivery Bicep Module

Azure service tag: **AzureUpdateDelivery**

## Overview

This directory contains Bicep variable files for the **AzureUpdateDelivery** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureUpdateDelivery.bicep** - Global/cloud-wide IP address ranges
- **region/AzureUpdateDelivery_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureUpdateDelivery module to access all IP ranges for this service tag:

```bicep
import * as azureupdatedelivery from './AzureUpdateDelivery.bicep'

// Use the variable in your template
var allowedIPs = azureupdatedelivery.AzureUpdateDelivery
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureupdatedeliveryEastUS from './region/AzureUpdateDelivery_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureupdatedeliveryEastUS.AzureUpdateDelivery_EastUS
```

## Available Regions

This module includes regional variants for the following Azure regions:

- `CentralUS`
- `EastAsia`
- `EastUS`
- `EastUS2`
- `NorthEurope`
- `SouthCentralUS`
- `WestCentralUS`
- `WestEurope`
- `WestUS2`

Total regional variants: 9


## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureUpdateDelivery
- **Module Directory**: azure-update-delivery
