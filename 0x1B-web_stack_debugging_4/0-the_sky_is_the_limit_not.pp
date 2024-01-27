# Increase the amount of traffic to see how much pressure Nginx can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  # Modify ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # The path for sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
  # The path for the init.d script
  path    => '/etc/init.d/',
}
