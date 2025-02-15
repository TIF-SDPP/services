variable "region" {
  type    = string
  default = "us-east1"
}

variable "zone" {
  type    = string
  default = "us-east1-b"
}

variable "credentials_file_path" {
  description = "Path to GCP service account credentials file"
  default     = "../service-account.json"
}

variable "project_id" {
  type    = string
  default = "unlucoin2025v2"
}
