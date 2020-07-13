# .

## Configurations

### API tokens

This project uses Hetzner Cloud for infrastructure and AWS S3 for Terraform
state management. Define these environment variables containing API tokens:

```sh
HCLOUD_TOKEN=...
AWS_DEFAULT_REGION=...
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

### Ansible vault password

Create Ansible vault password file used to encrypt/decrypt files (mainly in
the `config` directory).

```console
$ openssl rand -hex 32 > .vaultpass
```

### Configurations

Create `config/production.yml` containing system configuration variables. See
[production.yml.example](config/production.yml.example).

### Volume

This project assumes that Hetzner volume is already created. Use following
command to create one (50GB myvolume at Falkenstein datacenter):

```console
$ scripts/hetzner-create-volume myvolume 50 fsn1
```

The script prints API response in JSON. Copy the value of `volume.id` to your
`config/production.yml` as the `volume_id` field.


## Deployment

```console
$ cd data-server
$ ansible-playbook instance_up.yml
$ ansible-playbook provision.yml
```

To destroy the infrastructure:

```console
$ ansible-playbook instance_down.yml
```
