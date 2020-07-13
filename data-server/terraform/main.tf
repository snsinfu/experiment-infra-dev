terraform {
  backend "s3" {}
}

resource "hcloud_server" "data" {
  name        = var.server_hostname
  location    = var.server_location
  server_type = var.server_type
  image       = var.server_image
  user_data   = data.template_file.startup_script.rendered
}

data "template_file" "startup_script" {
  template = file("${path.module}/assets/startup.sh.in")
  vars = {
    admin_user            = var.admin_user
    admin_authorized_keys = join("\n", var.admin_ssh_pubkeys)
  }
}

resource "hcloud_volume_attachment" "data" {
  volume_id = var.volume_id
  server_id = hcloud_server.data.id
}
