output "server_addresses" {
  value = {
    data = hcloud_server.data.ipv4_address
  }
}
