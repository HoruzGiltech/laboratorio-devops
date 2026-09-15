terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  region = "us-central1"
}

resource "google_storage_bucket" "mi_bucket" {
  name                        = "mi-bucket-devops-lab-1234"
  location                    = "US"
  force_destroy               = true
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true

  labels = {
    env = "dev"
  }
}

# Configuración del clúster de GKE
resource "google_container_cluster" "primary" {
  name     = "mi-cluster-devops"
  location = "us-central1-a"

  initial_node_count = 1

  node_config {
    machine_type = "e2-medium"

    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
