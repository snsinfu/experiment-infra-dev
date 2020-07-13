variable "server_hostname" {
  type = string
}

variable "server_location" {
  type = string
}

variable "server_type" {
  type = string
}

variable "server_image" {
  type = string
}

variable "volume_id" {
  type = string
}

variable "admin_user" {
  type = string
}

variable "admin_ssh_pubkeys" {
  type = list(string)
}
