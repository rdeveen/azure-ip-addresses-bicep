# AzureMachineLearningInference Bicep Module

Azure service tag: **AzureMachineLearningInference**

## Overview

This directory contains Bicep variable files for the **AzureMachineLearningInference** service tag in the **Azure China Cloud**.

These files contain IP address ranges published by Microsoft Azure for this service tag and cloud region.

## Files

- **AzureMachineLearningInference.bicep** - Global/cloud-wide IP address ranges
- **region/AzureMachineLearningInference_*.bicep** - Regional-specific IP address ranges

## How to Use

### Global Service Tag

Import the global AzureMachineLearningInference module to access all IP ranges for this service tag:

```bicep
import * as azuremachinelearninginference from './AzureMachineLearningInference.bicep'

// Use the variable in your template
var allowedIPs = azuremachinelearninginference.AzureMachineLearningInference
```

### Regional Variants

For region-specific IP ranges, import the regional variant:

```bicep
import * as azuremachinelearninginferenceEastUS from './region/AzureMachineLearningInference_EastUS.bicep'

// Use the regional variable
var eastUSIPs = azuremachinelearninginferenceEastUS.AzureMachineLearningInference_EastUS
```



## Generated Information

These files are automatically generated and updated regularly. They contain IP address ranges published by Microsoft for the specified service tag in this cloud region.

- **Cloud**: Azure China Cloud
- **Service Tag**: AzureMachineLearningInference
- **Module Directory**: azure-machine-learning-inference
