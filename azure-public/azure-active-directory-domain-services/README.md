# AzureActiveDirectoryDomainServices Bicep Module

Azure service tag: **AzureActiveDirectoryDomainServices**

## Overview

This directory contains Bicep variable files for the **AzureActiveDirectoryDomainServices** service tag in the **Azure Public Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureActiveDirectoryDomainServices.bicep** - Global/cloud-wide IP address ranges
- **region/AzureActiveDirectoryDomainServices_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureActiveDirectoryDomainServices module to access all IP ranges for this service tag:

```bicep
import * as azureactivedirectorydomainservices from './AzureActiveDirectoryDomainServices.bicep'

// Use the variable in your template
var allowedIPs = azureactivedirectorydomainservices.AzureActiveDirectoryDomainServices
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azureactivedirectorydomainservicesEastUS from './region/AzureActiveDirectoryDomainServices_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azureactivedirectorydomainservicesEastUS.AzureActiveDirectoryDomainServices_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure Public Cloud
- **Service Tag**: AzureActiveDirectoryDomainServices
- **Module Directory**: azure-active-directory-domain-services
