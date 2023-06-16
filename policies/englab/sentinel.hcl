module "tfplan-functions" {
    source = "./common-functions/tfplan-functions/tfplan-functions.sentinel"
}

module "gcp-functions" {
    source = "./common-functions/gcp-functions/gcp-functions.sentinel"
}


policy "enforce_cluster_integrity_monitoring" {
  source = "./enforce_cluster_integrity_monitoring.sentinel"
  enforcement_level = "advisory" ß
}

policy "require_cluster_release_channel" {
  source = "./require_cluster_release_channel"
  enforcement_level = "advisory" 
}

policy "enforce_cluster_auto_upgrade_node" {
  source = "./enforce_cluster_auto_upgrade_node.sentinel"
  enforcement_level = "advisory" 
}