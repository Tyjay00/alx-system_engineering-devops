#!/usr/bin/env puppet
# using Puppet to make changes to our configuration file.

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "# SSH client configuration\n
              Host *\n
              IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
}
