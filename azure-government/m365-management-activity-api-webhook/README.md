# M365ManagementActivityApiWebhook Bicep Module

Azure service tag: **M365ManagementActivityApiWebhook**

## Overview

This directory contains Bicep variable files for the **M365ManagementActivityApiWebhook** service tag in the **Azure US Government Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **M365ManagementActivityApiWebhook.bicep** - Global/cloud-wide IP address ranges
- **region/M365ManagementActivityApiWebhook_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global M365ManagementActivityApiWebhook module to access all IP ranges for this service tag:

```bicep
import * as m365managementactivityapiwebhook from './M365ManagementActivityApiWebhook.bicep'

// Use the variable in your template
var allowedIPs = m365managementactivityapiwebhook.M365ManagementActivityApiWebhook
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as m365managementactivityapiwebhookEastUS from './region/M365ManagementActivityApiWebhook_EastUS.bicep'

// Use the regional variable
var eastUSIPs = m365managementactivityapiwebhookEastUS.M365ManagementActivityApiWebhook_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure US Government Cloud
- **Service Tag**: M365ManagementActivityApiWebhook
- **Module Directory**: m365-management-activity-api-webhook
