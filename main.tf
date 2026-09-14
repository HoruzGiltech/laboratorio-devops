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
