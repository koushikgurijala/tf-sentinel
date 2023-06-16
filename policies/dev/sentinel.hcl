module "tfplan-functions" {
    source = "./common-functions/tfplan-functions/tfplan-functions.sentinel"
}

module "gcp-functions" {
    source = "./common-functions/gcp-functions/gcp-functions.sentinel"
}


policy "GCP-TFSENTINEL-GAR-120-001" {
  source = "./GCP-TFSENTINEL-GAR-120-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GCE-160-001" {
  source = "./GCP-TFSENTINEL-GCE-160-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GCS-120-001" {
  source = "./GCP-TFSENTINEL-GCS-120-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GCS-120-002" {
  source = "./GCP-TFSENTINEL-GCS-120-002.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GDF-090-001" {
  source = "./GCP-TFSENTINEL-GDF-090-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GDF-090-002" {
  source = "./GCP-TFSENTINEL-GDF-090-002.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GDF-090-003" {
  source = "./GCP-TFSENTINEL-GDF-090-003.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GDF-120-001" {
  source = "./GCP-TFSENTINEL-GDF-120-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GKE-120-001" {
  source = "./GCP-TFSENTINEL-GKE-120-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GKE-120-002" {
  source = "./GCP-TFSENTINEL-GKE-120-002.sentinel" 
  enforcement_level = "hard-mandatory" 
}

policy "GCP-TFSENTINEL-GKE-150-001" {
  source = "./GCP-TFSENTINEL-GKE-150-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GKE-160-001" {
  source = "./GCP-TFSENTINEL-GKE-160-001.sentinel" 
  enforcement_level = "hard-mandatory" 
}

policy "GCP-TFSENTINEL-GKE-160-002" {
  source = "./GCP-TFSENTINEL-GKE-160-002.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-GKE-160-003" {
  source = "./GCP-TFSENTINEL-GKE-160-003.sentinel" 
  enforcement_level = "hard-mandatory" 
}

policy "GCP-TFSENTINEL-GPS-120-001" {
  source = "./GCP-TFSENTINEL-GPS-120-001.sentinel" 
  enforcement_level = "advisory" 
}
  
policy "GCP-TFSENTINEL-Network-160-001" {
  source = "./GCP-TFSENTINEL-Network-160-001.sentinel" 
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-Network-160-002" {
  source = "./GCP-TFSENTINEL-Network-160-002.sentinel" 
  enforcement_level = "advisory" 
}


policy "GCP-TFSENTINEL-Network-160-003" {
  source = "./GCP-TFSENTINEL-Network-160-003.sentinel"
  enforcement_level = "advisory" 
}

policy "GCP-TFSENTINEL-Network-160-004" {
  source = "./GCP-TFSENTINEL-Network-160-004.sentinel"
  enforcement_level = "advisory" 
}


# policy "GCP-TFSENTINEL-GCS-140-001" {
#   source = "./GCP-TFSENTINEL-GCS-140-001.sentinel" 
#   enforcement_level = "advisory" 
# }

policy "enforce_cluster_integrity_monitoring" {
  source = "./enforce_cluster_integrity_monitoring.sentinel"
  enforcement_level = "advisory" 
}

# policy "require_cluster_release_channel" {
#   source = "./require_cluster_release_channel"
#   enforcement_level = "advisory" 
# }

policy "enforce_cluster_auto_upgrade_node" {
  source = "./enforce_cluster_auto_upgrade_node.sentinel"
  enforcement_level = "advisory" 
}