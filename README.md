This TFE Policy set is for the following JIRA ticket:
https://track.td.com/browse/DEEDP-3195

# Sentinel Dev environment setup
1. Need linux VM. I used Ubuntu 18.04.5 LTS (Bionic Beaver)
2. Download sentinel tool from hashicorp
   https://docs.hashicorp.com/sentinel/downloads
3. create a new policy in Sentinel policy repo. 
  * create policy folder in repo. The folder structure will be like
    ```
    /<policy name>
        test/
        test-data/
    ```
4. add a policy control file
```
  /<policy name>/sentinel.hcl
  ```
  content will be like
  ```
  policy "restrict-lob-run-lob-module" {
  source            = "./restrict-lob-run-lob-module.sentinel"
  enforcement_level = "hard-mandatory"
  }
  ```
5. create test Terraform workspace
6. link policy repo/path to your workspace. Make sure you point the path your policy specific for easily target tests. 
7. After a successful Terraform plan, download mock data from workspace and put in test-data folder. and copy/change it according to your test needs. 

# Run unit tests
```
   cd <policy name>
   sentinel test <policy name>
```
# Release Steps

1. Check **master** branch for new commits since laster release.
2. Run *Release-Artifact-Cycle*:
   1. Navigate to the Actions tab and invoke `lob-selection` workflow with the following inputs:
      1. EDP Cycle: `release-artifact-cycle`
      2. Git Tag: `1.x.0` (i.e. `1.1.0`). In the event of an error related to a tag already existing, increment the patch number once. (i.e. `1.1.1`)
      3. Branch: `master`
      4. Run workflow
   2. This will trigger the following workflows in order `lob-selection-cycle -> its-selection-cycle -> release-artifact-cycle`
3. Run *Release-Cycle*:
   1. Navigate to the Actions tab and invoke `lob-selection` workflow with the following inputs:
      1. EDP Cycle: `release-cycle`
      2. Git Tag: Tag created in `release-artifact-cycle` (i.e. `1.1.0`)
      3. EDP Environment: `sit`
      4. Run Workflow
   2.  This will trigger the following workflows in order: `lob-selection-cycle -> its-selection-cycle -> release-cycle`

   # Policy Naming Conventions and Metadata

   ### Policy name: 
   `GCP-TFSENTINEL-[CATEGORY]-[DOMAIN_NO(3 Digits)]-[POLICY_NO(3digits)].sentinel`
   `CATEGORY:` GKE, GCP, GDF, GCE, GAR, etc. <br />
   `DOMAIN_NO:` Please look into the table below for Platform/CCM and STIGS based on TD Standards <br />
   `POLICY_NO:` In the same category, let us start with 1 and keep incrementing <br />

   #### Example:
   For a policy requirement below whose JIRA Ticket Id is `IFPUCGCP-839`
   Ensure to create a new service account with only the roles and permissions that are required for the Dataflow worker
   The name will be `GCP-TFSENTINEL-GDF-060-001.sentinel`

   ### DOMAIN_NO determination:

   **Note:** If the TD Standard (STIG) is not mapped / present then take the Platform / CCM Number mapping

   [TD Standards Document](https://w3.td.com/td/myintranet/technology/techbu/epnav/techEP/ps/!ut/p/z1/dYtBDsIgEEXP4glmRlPArbCwqdXQGiNsDCoxpAYaRY2e3vYAXf733gcLR7DRvcPN5ZCiuw_bWHYSukISSFsspETNNaNqU5NgCGYI-GSwJmjBglU7WSow-6YuWyUbmhfIlwtBbJRX_-xy6sHkx8uPQKaYfcyH4D-rr0qXiWvfufPPm9kfUiMPzA!!/?desktop=true)

   <br /> 
   
   |DOMAIN                                      |Number Mapping      |Type                      |
   |:----------------------------------------   |:-----------------  |:------------------------ |
   | API Security	                              | 010	               | TD Standards (STIG)      |
   | Application Security	                     | 020	               | TD Standards (STIG)      |
   | Availability Management	                  | 030	               | TD Standards (STIG)      |
   | Awareness & Training	                     | 040	               | TD Standards (STIG)      |
   | Business Managed Technology	               | 050	               | TD Standards (STIG)      |
   | Change/Asset and Configuration Management	| 060	               | TD Standards (STIG)      |
   | Control Effectiveness Testing	            | 070	               | TD Standards (STIG)      |
   | Cyber Security Incident Management	      | 080	               | TD Standards (STIG)      |
   | Data Security Classify and Protection	   | 090	               | TD Standards (STIG)      |
   | Digital Crown Jewels and Enhanced Controls	| 100	               | TD Standards (STIG)      |
   | Disaster Recovery	                        | 110	               | TD Standards (STIG)      |
   | Global Identity and Access Management	   | 120	               | TD Standards (STIG)      |
   | Information Technology Currency	         | 130	               | TD Standards (STIG)      |
   | Public Cloud Security	                     | 140	               | TD Standards (STIG)      |
   | Security Logging and Monitoring	         | 150	               | TD Standards (STIG)      |
   | System Defense	                           | 160	               | TD Standards (STIG)      |
   | SDLC Technology	                           | 170	               | TD Standards (STIG)      |
   | Technology Cybersecurity Risk Management	| 180	               | TD Standards (STIG)      |
   | Third Party Cybersecurity Risk Management	| 190	               | TD Standards (STIG)	   |
   

   ## Metadata block in policies

   Metada in policies should follow the below model.
   <p> policyName means Policy Name </p>
   <p> <isn>PolicyDescription:</isn> will be a brief description of what the policy does </p>
   <p> <isn>priority:</isn> will be found in the JIRA/ASCA Ticket </p>
   <p> <isn>customComplianceCacRef:</isn> is the id mentioned in JIRA/ASCA ticket created for development, if not it will be a CCM/Platform requirement, So update that id </p>

   ```
   metadata = {
      "version": "1.0.0",
      "category": "GPS",
      "priority": "High",
      "customComplianceCacRef": "GCPPLAT-GPS-02",
      "createdBy": "td-cac-team",
      "policyDescription": "Ensure GCP Pub/Sub Topic is not anonymously or publicly accessible",
      "policyName": "GCP-TFSENTINEL-GPS-120-001.sentinel",
   }

   ```
