# GuestAndHybridManagement Bicep Module

Azure service tag: **GuestAndHybridManagement**

## Overview

This directory contains Bicep variable files for the **GuestAndHybridManagement** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **GuestAndHybridManagement.bicep** - Global/cloud-wide IP address ranges
- **region/GuestAndHybridManagement_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global GuestAndHybridManagement module to access all IP ranges for this service tag:

```bicep
import * as guestandhybridmanagement from './GuestAndHybridManagement.bicep'

// Use the variable in your template
var allowedIPs = guestandhybridmanagement.GuestAndHybridManagement
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as guestandhybridmanagementEastUS from './region/GuestAndHybridManagement_EastUS.bicep'

// Use the regional variable
var eastUSIPs = guestandhybridmanagementEastUS.GuestAndHybridManagement_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: GuestAndHybridManagement
- **Module Directory**: guest-and-hybrid-management
