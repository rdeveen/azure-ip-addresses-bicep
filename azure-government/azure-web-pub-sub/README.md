# AzureWebPubSub Bicep Module

Azure service tag: **AzureWebPubSub**

## Overview

This directory contains Bicep variable files for the **AzureWebPubSub** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureWebPubSub.bicep** - Global/cloud-wide IP address ranges
- **region/AzureWebPubSub_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureWebPubSub module to access all IP ranges for this service tag:

```bicep
import * as azurewebpubsub from './AzureWebPubSub.bicep'

// Use the variable in your template
var allowedIPs = azurewebpubsub.AzureWebPubSub
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azurewebpubsubEastUS from './region/AzureWebPubSub_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azurewebpubsubEastUS.AzureWebPubSub_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: AzureWebPubSub
- **Module Directory**: azure-web-pub-sub
